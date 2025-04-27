import os

def isEmpty():
    if not os.listdir():
        print("There are no files to organize\n")
        print("Please enter any key to exit\n")
        input()
        exit()