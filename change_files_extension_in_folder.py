#!/usr/bin/python

import sys
import os


def setUp():
    global dir, extension

    dir = str(sys.argv[1])
    extension = str(sys.argv[2])


def change():
    for filename in os.listdir(dir):
        full_path = dir + filename
        base = os.path.splitext(full_path)[0]

        if (extension in full_path): 
            os.rename(full_path, base)
        else:
            os.rename(full_path, base + extension)

def main():
    setUp()
    change()

if __name__ == "__main__":
    main()
