# File Content Copier

import sys
import Image


class FileHandler:
    def __init__(self):
        self.copy = "" # Text of copied file
    def loadFile(self, file):
        self.copy = open(file, 'r').read() # Loads specified file name as text
    def saveTo(self, file):
        write = open(file, 'w')
        write.write(self.copy) # Writes to specified file


to_copy = "" # To_copy file name
to_save = "" # To_save file name
try:
    to_copy = sys.argv[1]
except Exception as err:
    print(err)

try:
    to_save = sys.argv[2]
except Exception as err:
    print(err)

try:
    fh = FileHandler()
    fh.loadFile(to_copy)
    fh.saveTo(to_save)
except Exception as err:
    print(err)
