import os
from pathlib import Path
import dictionaries, isEmpty, createDir
import importlib.util

def importModule(moduleName, path):
    spec = importlib.util.spec_from_file_location(moduleName, path)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module

def searchModule(moduleName):
    folder_path = "C:"
    for root, dirs, files in os.walk(folder_path):
        if moduleName in files:
            module_path = os.path.join(root, moduleName+".py")
            module = importModule(moduleName, module_path)
            break
    return module

def organize():
    isEmpty()
    current_dir = os.path.dirname(os.path.realpath(__file__))
    createDir(current_dir)
