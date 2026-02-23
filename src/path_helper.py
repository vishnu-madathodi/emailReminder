import sys
import os

#to resolve the issue with paths in exe
def resource_path(relative_path):
    """ Get absolute path to resource (works for dev and for PyInstaller exe) """
    if getattr(sys, 'frozen', False):
        base_path = sys._MEIPASS   # temp folder where exe extracts
    else:
        base_path = os.path.abspath(".")

    return os.path.join(base_path, relative_path)