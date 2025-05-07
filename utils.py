import os
import shutil
from pathlib import Path

DIRECTORIES = {
    "DOCUMENTS": [".doc", ".txt", ".odt", ".odm", ".ans", ".docx", ".dotx", ".readme", ".md", ".ipynb", ".ott", ".epub",
                  ".xls", ".xlsx", ".ppt", ".pages"],
    "LaTeX": [".sty", ".ltx", ".tex", ".bib", ".latex"],
    "GOOGLE": [".gsite", ".gform", ".gdoc", ".gdraw", ".gsheet", ".gslides", ".gscript", ".gtable", ],
    "IMAGES": [".jpeg", ".jpg", ".png", ".tiff", ".bmp", ".gif", ".bpg", ".svg"],
    "VIDEOS": [".mp4", ".flv", ".mov", ".avi", ".wmv", ".webm", ".vob"],
    "COMPRESSED FILES": [".zip", ".7z", ".ar", ".gz", ".tar", ".rz"],
    "AUDIO": [".mp3", ".wav", ".m4a", ".m4b", ".m4p", ".ogg"],
    "PDF": [".pdf"],
    "EXECUTABLES": [".exe", ".apk"],
    "PROGRAMMING": [".py", ".c", ".cpp", ".sh", ".rs", ".js", ".html", ".css", ".java", ".h",],
}

def isEmpty(current_dir):
    if len(os.listdir(current_dir)) == 1:
        print("There are no files to organize\n")
        print("Please enter any key to exit\n")
        input()
        exit()

def createDir(current_dir):
    for category in DIRECTORIES:
        if not os.path.exists(os.path.join(current_dir, category)):
            os.makedirs(os.path.join(current_dir, category))
            print(f"Creating directory \"{category}\"...")

def moveFiles(current_dir):
    for file in os.listdir(current_dir):
        file_path = os.path.join(current_dir, file)
        if os.path.isdir(file_path): continue
        moved = False
        for category, extensions in DIRECTORIES.items():
            if Path(file).suffix in extensions:
                shutil.move(file_path, os.path.join(current_dir, category, file))
                print(f"The file \"{file}\" has been moved to \"{category}\".")
                moved = True
                break
        if not moved:
            print(f"The extension of the file \"{file}\" is not on our database. We're sorry!\n")
    
def deleteEmptyDirs(current_dir):
    for dir in os.listdir(current_dir):
        dir_path = os.path.join(current_dir, dir)
        if os.path.isfile(dir_path): continue
        if not os.listdir(dir_path):
            print(f"Deleting the folder \"{dir}\" due to lack of files.")
            os.rmdir(dir_path)

def organize():
    current_dir = os.path.dirname(os.path.realpath(__file__))
    isEmpty(current_dir)
    createDir(current_dir)
    print("\n")
    moveFiles(current_dir)
    print("\n")
    deleteEmptyDirs(current_dir)