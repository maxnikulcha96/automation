"""Merge PDF utility."""

from abc import ABC
from pypdf import PdfMerger
import os


class MergePDF(ABC):
    def __init__(self, ):
        """
        Initializes a new MergePDF instance.
        """

        self.merger = PdfMerger()
    
    
    def merge_files_in_folder(self, input_folder, output_file = "result.pdf"):
        """
        Merges the files inside of specific folder and saves into the output file.

        :param input_folder: The input folder with PDF files to merge.
        :param output_file: Output file.
        """

        for filename in os.listdir(input_folder):
            full_path = os.path.join(input_folder, filename)
            self.merger.append(full_path)

        self.merger.write(output_file)
        self.merger.close()
