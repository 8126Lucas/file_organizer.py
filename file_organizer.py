import os
from pathlib import Path
import dictionaries, isEmpty, createDir

def organize():
    isEmpty()
    current_dir = os.path.dirname(os.path.realpath(__file__))
    createDir(current_dir)
