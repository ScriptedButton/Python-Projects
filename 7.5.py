# File Statistics

import sys

file = sys.argv[1]

def getLength(file):
    read = open(file, 'r')
    lines = len(read.readlines())
    read.seek(0) # reset reader position
    chars = len(read.read())
    read.seek(0)
    words = len(read.read().split())

    print("Lines: " , lines)
    print("Characters: " , chars)
    print("Words: ", words)

getLength(file)