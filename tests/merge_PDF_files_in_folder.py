#!/usr/bin/python

import sys
from framework.utils.mergePDF import MergePDF


def setUp():
    global mergePDF

    mergePDF = MergePDF()

    global input_folder, output_file
    input_folder = str(sys.argv[1])
    output_file = str(sys.argv[2])


def merge_files_in_folder():
    mergePDF.merge_files_in_folder(input_folder, output_file)


def main():
    setUp()
    merge_files_in_folder()


if __name__ == "__main__":
    main()