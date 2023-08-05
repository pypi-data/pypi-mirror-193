from EasyPyQt import VERSION, utils, builder

import time
import sys
import os





def PRINT_HELP():
    print("""usage: 
pyqtc [-h] [-v] [-t TEMPLATE_NAME] [-F] [-D] [-n NAME] [-d DIRECTORY] UI_FILE

      [-h] [--help] for usage helps (DEFAULT OFF)

      [-v] [--version] for version info (DEFAULT OFF)

      [-t TEMPLATE_NAME] [--template TEMPLATE_NAME] generate premade pyqt templates

      [-F] [--onefile] generate a onefile python template code from QtDesigner .ui file (DEFAULT ON)

      [-D] [--onedir] generate a onedir python module template code from QtDesigner .ui file (DEFAULT OFF)

      [-n NAME] [--name NAME] specify the 'NAME' of the generated output file/module name (DEFAULT use .ui filename)

      [-d DIRECTORY] [--dir DIRECTORY] specify a directory where to generate the files

      UI_FILE the .ui file to generate python template code for
      **required if [-t] or [--template] is not specified**
    """)


def GET_FLAG_VALUE(p, args):
    index = args.index(p)
    if(index+1 == len(args)):
        utils.PRINT_ERROR(f"{p} missing following flag value")
        os._exit(0)
    return args[index+1]





def main():
    args = sys.argv
    if len(args) <= 1 or "-h" in args or "--help" in args: return PRINT_HELP()

    if "-v" in args or "--version" in args: return print(VERSION)



    TARGET_DIR = ""
    UI_FILE = ""
    UI_FILE_ARG = ""

    TARGET_NAME = ""

    ONEDIR = "-D" in args or "--onedir" in args
    ONEFILE = "-F" in args or "--onefile" in args or not ONEDIR

    UI_XML = None
    UI = None
    ROOT = None



    for arg in args:
        if(".ui" in arg):
            UI_FILE_ARG = arg.strip("\" ")
    if(not UI_FILE_ARG): return utils.PRINT_ERROR("the following arguments are required: UI_FILE")
    if(os.path.exists(UI_FILE_ARG)):
        UI_FILE = UI_FILE_ARG
    elif(os.path.exists(os.path.join(os.getcwd(), UI_FILE_ARG))):
        UI_FILE = os.path.join(os.getcwd(), UI_FILE_ARG)
    else:
        return utils.PRINT_ERROR("ui file specified does not exist")
    UI_FILE = os.path.abspath(UI_FILE)
    utils.PRINT_EVENT(f"UI file OK: {UI_FILE}")
    TARGET_NAME = os.path.split(UI_FILE)[1].strip()[:-3]

    if "-d" in args:
        TARGET_DIR = GET_FLAG_VALUE("-d", args)
    elif "--dir" in args:
        TARGET_DIR = GET_FLAG_VALUE("--dir", args)
    else:
        TARGET_DIR = os.path.split(UI_FILE)[0]
    if(not os.path.exists(TARGET_DIR)): 
        return utils.PRINT_ERROR("result directory specified does not exist (-d / --dir)")
    utils.PRINT_EVENT(f"target directory OK: {TARGET_DIR}")

    if "-n" in args:
        TARGET_NAME = GET_FLAG_VALUE("-n", args)
    elif "--name" in args:
        TARGET_NAME = GET_FLAG_VALUE("--name", args)
    utils.PRINT_EVENT(f"target name OK: {TARGET_NAME}")



    UI_XML, UI, ROOT = utils.READ_UI_XML_FILE(UI_FILE)



    if ONEFILE: 
        utils.PRINT_START("ONEFILE start")
        startTime = time.time()
        target_name = TARGET_NAME + (".py" if(".py" not in TARGET_NAME)else "")
        builder.buildOneFile(
            ui=UI, 
            root=ROOT, 
            ui_xml_path=UI_FILE, 
            target_path=TARGET_DIR, 
            target_name=target_name,
        )
        utils.PRINT_ENDED(f"ONEFILE ended (time used: {time.time()-startTime}s)", beg="\n")
        utils.PRINT_ENDED(f"result file path: {os.path.join(TARGET_DIR, target_name)}")



    if ONEDIR: 
        utils.PRINT_START("ONEDIR start")
        startTime = time.time()
        target_name = (TARGET_NAME if(".py" not in TARGET_NAME)else TARGET_NAME.replace(".py", ""))
        builder.buildOneDir(
            ui=UI, 
            root=ROOT, 
            ui_xml_path=UI_FILE, 
            target_path=TARGET_DIR, 
            target_name=target_name,
        )
        utils.PRINT_ENDED(f"ONEDIR ended (time used: {time.time()-startTime}s)")
        utils.PRINT_ENDED(f"result module path: {os.path.join(TARGET_DIR, target_name)}")

