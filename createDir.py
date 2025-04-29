import os
from pathlib import Path


def createDir(currentDir):
    if not os.path.exists(os.path.join(currentDir, "DOCUMENTS")):
        os.makedirs(os.path.join(currentDir, "DOCUMENTS"))
    if not os.path.exists(os.path.join(currentDir, "LaTeX")):
        os.makedirs(os.path.join(currentDir, "LaTeX"))
    if not os.path.exists(os.path.join(currentDir, "IMAGES")):
        os.makedirs(os.path.join(currentDir, "IMAGES"))
    if not os.path.exists(os.path.join(currentDir, "VIDEOS")):
        os.makedirs(os.path.join(currentDir, "VIDEOS"))
    if not os.path.exists(os.path.join(currentDir, "GOOGLE")):
        os.makedirs(os.path.join(currentDir, "GOOGLE"))
    if not os.path.exists(os.path.join(currentDir, "PDF")):
        os.makedirs(os.path.join(currentDir, "PDF"))
    if not os.path.exists(os.path.join(currentDir, "AUDIO")):
        os.makedirs(os.path.join(currentDir, "AUDIO"))
    if not os.path.exists(os.path.join(currentDir, "COMPRESSED FILES")):
        os.makedirs(os.path.join(currentDir, "COMPRESSED FILES"))
    if not os.path.exists(os.path.join(currentDir, "EXECUTABLES")):
        os.makedirs(os.path.join(currentDir, "EXECUTABLES"))
    if not os.path.exists(os.path.join(currentDir, "PROGRAMMING")):
        os.makedirs(os.path.join(currentDir, "PROGRAMMING"))








