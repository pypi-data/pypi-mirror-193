from .constants import *

from xml.etree import ElementTree as ET
import os





def PRINT_ERROR(msg, beg="", end="\n"):
    print(f"{beg}ERROR:", msg, end=end)

def PRINT_EVENT(msg, beg="", end="\n"):
    print(f"{beg}EVENT:", msg, end=end)

def PRINT_START(msg, beg="\n", end="\n"):
    print(f"{beg}START:", msg, end=end)

def PRINT_ENDED(msg, beg="\n", end="\n"):
    print(f"{beg}ENDED:", msg, end=end)





def READ_UI_XML_FILE(filePath):
    """
    return UI_XML, UI, ROOT
    """
    error = False
    try:
        uiXml = ET.parse(filePath)
        PRINT_EVENT(f"UI XML OK")
        uiObject = uiXml.getroot()
        PRINT_EVENT(f"UI Object OK")
        uiRoot = uiObject.find("widget")
        PRINT_EVENT(f"UI Root Object OK")
        return uiXml, uiObject, uiRoot
    except FileNotFoundError:
        error = True
        PRINT_ERROR("[FileNotFoundError] the specified XML file does not exist")
        PRINT_ERROR(f"Error when attempting to read XML file: {filePath}")
    except PermissionError:
        error = True
        PRINT_ERROR("[PermissionError] the user does not have sufficient permissions to read the specified XML file")
        PRINT_ERROR(f"Error when attempting to read XML file: {filePath}")
    except IsADirectoryError:
        error = True
        PRINT_ERROR("[IsADirectoryError] the specified XML file path is a directory and not a file")
        PRINT_ERROR(f"Error when attempting to read XML file: {filePath}")
    except IOError:
        error = True
        PRINT_ERROR("[IOError] there is an input/output error while reading the XML file")
        PRINT_ERROR(f"Error when attempting to read XML file: {filePath}")
    except OSError:
        error = True
        PRINT_ERROR("[IOError] there is an input/output error while reading to the XML file")
        PRINT_ERROR(f"Error when attempting to read XML file: {filePath}")
    except UnicodeDecodeError:
        error = True
        PRINT_ERROR("[OSError] the file being read is not encoded in a compatible character encoding")
        PRINT_ERROR(f"Error when attempting to read XML file: {filePath}")
    finally:
        if(error): os._exit(0)





def readFile(filePath):
    error = False
    try:
        with open(filePath, "r") as f: return f.read()
    except FileNotFoundError:
        error = True
        PRINT_ERROR("[FileNotFoundError] the specified file does not exist")
        PRINT_ERROR(f"Error when attempting to read file: {filePath}")
    except PermissionError:
        error = True
        PRINT_ERROR("[PermissionError] the user does not have sufficient permissions to read the specified file")
        PRINT_ERROR(f"Error when attempting to read file: {filePath}")
    except IsADirectoryError:
        error = True
        PRINT_ERROR("[IsADirectoryError] the specified file path is a directory and not a file")
        PRINT_ERROR(f"Error when attempting to read file: {filePath}")
    except TypeError:
        error = True
        PRINT_ERROR("[TypeError] the mode argument passed to open() is invalid for reading")
        PRINT_ERROR(f"Error when attempting to read file: {filePath}")
    except IOError:
        error = True
        PRINT_ERROR("[IOError] there is an input/output error while reading the file")
        PRINT_ERROR(f"Error when attempting to read file: {filePath}")
    except OSError:
        error = True
        PRINT_ERROR("[IOError] there is an input/output error while reading to the file")
        PRINT_ERROR(f"Error when attempting to read file: {filePath}")
    except UnicodeDecodeError:
        error = True
        PRINT_ERROR("[OSError] the file being read is not encoded in a compatible character encoding")
        PRINT_ERROR(f"Error when attempting to read file: {filePath}")
    finally:
        if(error): os._exit(0)


def writeFile(filePath, content):
    error = False
    try:
        with open(filePath, "w") as f:
            f.write(content)
    except FileNotFoundError:
        error = True
        PRINT_ERROR("[FileNotFoundError] the specified file does not exist")
        PRINT_ERROR(f"Error when attempting to write file: {filePath}")
    except PermissionError:
        error = True
        PRINT_ERROR("[PermissionError] user does not have sufficient permissions to write to the specified file")
        PRINT_ERROR(f"Error when attempting to write file: {filePath}")
    except IsADirectoryError:
        error = True
        PRINT_ERROR("[IsADirectoryError] the specified file path is a directory and not a file")
        PRINT_ERROR(f"Error when attempting to write file: {filePath}")
    except TypeError:
        error = True
        PRINT_ERROR("[TypeError] the mode argument passed to open() is invalid for writing")
        PRINT_ERROR(f"Error when attempting to write file: {filePath}")
    except IOError:
        error = True
        PRINT_ERROR("[IOError] there is an input/output error while writing to the file")
        PRINT_ERROR(f"Error when attempting to write file: {filePath}")
    except OSError:
        error = True
        PRINT_ERROR("[OSError] there is a system error while attempting to create or write to the file")
        PRINT_ERROR(f"Error when attempting to write file: {filePath}")
    finally:
        if(error): os._exit(0)
        else: return True
