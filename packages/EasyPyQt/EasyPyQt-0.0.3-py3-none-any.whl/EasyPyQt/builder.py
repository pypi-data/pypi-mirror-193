from . import supportedSignals, header
from . import utils

from .constants import *

import os





def recursedOneDir(root, path):
    childNames = []
    childSignals = []
    for child in root:
        if(child.tag != "widget"): continue
        className = child.attrib["class"]
        widgetName = child.attrib["name"]
        widgetPath = os.path.join(path, widgetName)

        if(not os.path.exists(widgetPath)): os.mkdir(widgetPath)
        childNames.append(widgetName)

        signals = supportedSignals.classSignals.get(className, [])
        content = ""
        for signal in signals:
            content += f"# CLASS {className} SIGNAL {signal[1]} FROM {signal[2]}\n"
            content += f"def on_{signal[1]}():\n"
            content += f"    print(\"{widgetName} {signal[1]}\")\n"
            content += "\n\n\n"
            childSignals.append([widgetName, signal[1], f"{widgetName}.on_{signal[1]}"])
        utils.writeFile(os.path.join(widgetPath, "__init__.py"), content)
        childSignals.extend([childWidgetName, signalName, f"{widgetName}.{signalPath}"] for childWidgetName, signalName, signalPath in recursedOneDir(child, widgetPath))
    rootImportContent = "\n".join([f"from . import {name}" for name in childNames])
    rootContent = utils.readFile(os.path.join(path, "__init__.py"))
    neededSpacing = (rootImportContent != "" and rootContent != "")*6
    utils.writeFile(os.path.join(path, "__init__.py"), rootImportContent + "\n"*neededSpacing + rootContent)
    return childSignals


def buildOneDir(ui, root, ui_xml_path, target_path, target_name):
    rootClassName = root.attrib["name"]
    for child in root: 
        if(child.tag == "property" and child.attrib["name"] == "windowTitle"):
            rootClassName = child.find("string").text

    codeHeader = header.makeUIcodeHeader(VERSION, ui_xml_path, ui.attrib["version"], end="\n\n")
    utils.writeFile(os.path.join(target_path, f"runUI_{target_name}.py"), (
        f"{codeHeader}\n"
        f"\n"
        f"from PyQt5.QtWidgets import QApplication\n"
        f"\n"
        f"import sys\n"
        f"\n"
        f"from {target_name} import {rootClassName}\n"
        f"\n"
        f"\n"
        f"\n"
        f"def main():\n"
        f"    app = QApplication(sys.argv)\n"
        f"    ui = {rootClassName}()\n"
        f"    ui.show()\n"
        f"    sys.exit(app.exec_())\n"
        f"\n"
        f"if __name__ == \"__main__\":\n"
        f"    main()\n"
    ))

    dist = os.path.join(target_path, target_name)
    if(not os.path.exists(dist)): os.mkdir(dist)

    utils.writeFile(os.path.join(dist, "__init__.py"), "")

    rootImportContent = (
        f"from PyQt5.QtWidgets import {root.attrib['class']}\n"
        f"from PyQt5 import uic\n"
    )

    rootClassDefinition = (
        f"class {rootClassName}({root.attrib['class']}):\n"
        f"    def __init__(self):\n"
        f"        super(self.__class__, self).__init__()\n"
        f"        uic.loadUi(r\"{ui_xml_path}\", self)\n"
    )
    prevWidgetName = ""
    for widgetName, signalName, signalPath in recursedOneDir(root, dist):
        if(prevWidgetName != widgetName): rootClassDefinition += "\n"
        rootClassDefinition += f"        self.{widgetName}.{signalName}.connect({signalPath})\n"
        prevWidgetName = widgetName

    rootFileContent = utils.readFile(os.path.join(dist, "__init__.py"))
    neededSpacing = (rootFileContent != "" and rootClassDefinition != "")*6
    utils.writeFile(os.path.join(dist, "__init__.py"), (
        rootImportContent + "\n" + 
        rootFileContent + "\n"*neededSpacing + 
        rootClassDefinition
    ))
    return True





def recursedOneFile(root, content):
    childNames = []
    childSignals = {}
    for child in root:
        if(child.tag != "widget"): continue
        className = child.attrib["class"]
        widgetName = child.attrib["name"]

        utils.PRINT_EVENT(f"recursedOneFile found child widget: {className} - {widgetName}")

        childNames.append(widgetName)
        childSignals[widgetName] = []

        signals = supportedSignals.classSignals.get(className, [])
        if(signals): content += "\n\n\n"
        for signal in signals:
            funcName = f"{widgetName}_on_{signal[1]}"
            content += f"    # CLASS {className} SIGNAL {signal[1]} FROM {signal[2]}\n"
            content += f"    def {funcName}(self, *args, **kwargs):\n"
            content += f"        print(\"{widgetName} {signal[1]}\")\n"
            content += f"        print(\"signal arguments:\", args)\n"
            content += f"        print(\"signal keyword args:\", kwargs)\n"
            content += f"\n"
            childSignals[widgetName].append([signal[1], funcName])
            utils.PRINT_EVENT(f"recursedOneFile WIDGET[{widgetName}] FUNCTION[{funcName} generated")
        grandSignals, content = recursedOneFile(child, content)
        childSignals.update(grandSignals)
    return childSignals, content


def buildOneFile(ui, root, ui_xml_path, target_path, target_name):
    windowTitle = root.attrib["name"]
    for child in root: 
        if(child.tag == "property" and child.attrib["name"] == "windowTitle"):
            windowTitle = child.find("string").text
    rootClassName = windowTitle

    contentBeg = (
        f"from PyQt5.QtWidgets import QApplication, {root.attrib['class']}\n"
        f"from PyQt5 import uic\n"
        f"\n"
        f"import sys\n"
        f"\n"
        f"\n"
        f"\n"
        f"class {rootClassName}({root.attrib['class']}):\n"
        f"    def __init__(self):\n"
        f"        super(self.__class__, self).__init__()\n"
        f"        uic.loadUi(r\"{ui_xml_path}\", self)\n"
    )
    utils.PRINT_EVENT("buildOneFile contentBeg created")
    contentEnd = (
        f"\n"
        f"\n"
        f"\n"
        f"\n"
        f"\n"
        f"def main():\n"
        f"    app = QApplication(sys.argv)\n"
        f"    ui = {rootClassName}()\n"
        f"    ui.show()\n"
        f"    sys.exit(app.exec_())\n"
        f"\n"
        f"if __name__ == \"__main__\":\n"
        f"    main()\n"
    )
    utils.PRINT_EVENT("buildOneFile contentEnd created")

    utils.PRINT_START("buildOneFile start recursedOneFile")
    childSignals, signalContent = recursedOneFile(root, "")
    utils.PRINT_ENDED("buildOneFile ended recursedOneFile")

    connectContent = ""
    for widgetName, signalFuncNames in childSignals.items():
        utils.PRINT_START(f"buildOneFile start connecting signals for widget: {widgetName}")
        connectContent += f"\n"
        connectContent += f"        # CONNECT {widgetName} SIGNALS\n"
        for signalName, funcName in signalFuncNames:
            utils.PRINT_EVENT(f"buildOneFile FUNCTION[{signalName}] connected to WIDGET[{widgetName}]")
            connectContent += f"        self.{widgetName}.{signalName}.connect(self.{funcName})\n"
        utils.PRINT_ENDED(f"buildOneFile ended connecting signals for widget: {widgetName}")

    codeContent = header.makeUIcodeHeader(VERSION, ui_xml_path, ui.attrib["version"], end="\n\n") + contentBeg + connectContent + signalContent + contentEnd

    utils.writeFile(os.path.join(target_path, target_name), codeContent)

