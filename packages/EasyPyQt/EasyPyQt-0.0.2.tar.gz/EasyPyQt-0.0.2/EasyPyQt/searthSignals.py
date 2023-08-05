IgnoreSignals = {
    "customContextMenuRequested - PyQt5.QtWidgets.QWidget",
    "windowIconChanged - PyQt5.QtWidgets.QWidget",
    "windowIconTextChanged - PyQt5.QtWidgets.QWidget",
    "windowTitleChanged - PyQt5.QtWidgets.QWidget",
    "objectNameChanged - PyQt5.QtCore.QObject",
}

supportedSignals = {
    "Layouts": {
        "Horizontal Layout": [],
        "Vertical Layout": [],
        "Grid Layout": [],
        "Form Layout": [],
    },
    "Spacers": {
        "Horizontal Spacer": [],
        "Vertical Spacer": [],
    },
    "Buttons": {
        "Push Button": [],
        "Tool Button": [],
        "Radio Button": [],
        "Check Box": [],
        "Command Link Button": [],
        "Dialog Button Box": [],
    },
    "Item Views (Model-Based)": {
        "List View": [],
        "Tree View": [],
        "Table View": [],
        "Column View": [],
    },
    "Item Widgets (Item-Based)": {
        "List Widget": [],
        "Tree Widget": [],
        "Table Widget": [],
    },
    "Containers": {
        "Group Box": [],
        "Scroll Area": [],
        "Tool Box": [],
        "Tab Widget": [],
        "Stacked Widget": [],
        "Frame": [],
        "Widget": [],
        "MDI Area": [],
        "Dock Widget": [],
    },
    "Input Widgets": {
        "Combo Box": [],
        "Font Combo Box": [],
        "Line Edit": [],
        "Text Edit": [],
        "Plain Text Edit": [],
        "Spin Box": [],
        "Double Spin Box": [],
        "Time Edit": [],
        "Date Edit": [],
        "Date/Time Edit": [],
        "Dial": [],
        "Horizontal Scroll Bar": [],
        "Vertical Scroll Bar": [],
        "Horizontal Slider": [],
        "Vertical Slider": [],
        "Key Sequence Edit": [],
    },
    "Display Widgets": {
        "Label": [],
        "Text Browser": [],
        "Graphics View": [],
        "Calendar Widget": [],
        "LCD Number": [],
        "Progress Bar": [],
        "Horizontal Line": [],
        "Vertical Line": [],
        "OpenGL Widget": [],
    }
}

classSignals = {}



from PyQt5 import QtCore, QtWidgets
import json

def getSignals(source):
    result = []
    cls = source if isinstance(source, type) else type(source)
    signal = type(QtCore.pyqtSignal())
    for subcls in cls.mro():
        clsname = f"{subcls.__module__}.{subcls.__name__}"
        for key, value in sorted(vars(subcls).items()):
            if isinstance(value, signal):
                text = f"{cls.__name__} - {key} - {clsname}"
                if text in IgnoreSignals: continue
                result.append([cls.__name__, key, clsname])
    return result

for t in supportedSignals:
    for n in supportedSignals[t]:
        try:
            widgetClass = ("Q"+n
                .replace("Horizontal", "")
                .replace("Vertical", "")
                .replace(" ", "")
                .replace("/", "")
            )
            widget = getattr(QtWidgets, widgetClass)
            signals = getSignals(widget)
            supportedSignals[t][n] = signals
            classSignals[widgetClass] = [pair for pair in signals]
        except: pass


with open("supportedSignals.py", "w") as f:
    f.write("supportedSignals = " + json.dumps(supportedSignals, indent=4, ensure_ascii=False))
    f.write("\n\n")
    f.write("classSignals = " + json.dumps(classSignals, indent=4, ensure_ascii=False))