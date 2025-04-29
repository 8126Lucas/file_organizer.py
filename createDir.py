import os
from pathlib import Path


def createDir(currentDir):
    if not os.path.exists(currentDir + "/DOCUMENTS"):
        os.makedirs(currentDir + "/DOCUMENTS")
    if not os.path.exists(currentDir + "/LaTeX"):
        os.makedirs(currentDir + "/LaTeX")
    if not os.path.exists(currentDir + "/IMAGES"):
        os.makedirs(currentDir + "/IMAGES")
    if not os.path.exists(currentDir + "/VIDEOS"):
        os.makedirs(currentDir + "/VIDEOS")
    if not os.path.exists(currentDir + "/GOOGLE"):
        os.makedirs(currentDir + "/GOOGLE")
    if not os.path.exists(currentDir + "/PDF"):
        os.makedirs(currentDir + "/PDF")
    if not os.path.exists(currentDir + "/AUDIO"):
        os.makedirs(currentDir + "/AUDIO")
    if not os.path.exists(currentDir + "/COMPRESSED FILES"):
        os.makedirs(currentDir + "/COMPRESSED FILES")
    if not os.path.exists(currentDir + "/EXECUTABLES"):
        os.makedirs(currentDir + "/EXECUTABLES")
    if not os.path.exists(currentDir + "/PROGRAMMING"):
        os.makedirs(currentDir + "/PROGRAMMING")








