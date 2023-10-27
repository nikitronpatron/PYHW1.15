import os
import sys
import logging
from collections import namedtuple

logging.basicConfig(filename='directory_info.log', level=logging.INFO, format='%(message)s')

FileInfo = namedtuple('FileInfo', ['name', 'extension', 'is_dir', 'parent_dir'])

def list_directory_contents(path):
    for root, dirs, files in os.walk(path):
        for directory in dirs:
            full_path = os.path.join(root, directory)
            parent_dir = os.path.basename(root)
            logging.info(f"Name: {directory}, Extension: <DIR>, Is Directory: True, Parent Directory: {parent_dir}")
        for filename in files:
            name, extension = os.path.splitext(filename)
            full_path = os.path.join(root, filename)
            parent_dir = os.path.basename(root)
            logging.info(f"Name: {name}, Extension: {extension}, Is Directory: False, Parent Directory: {parent_dir}")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python directory_info.py <directory_path>")
    else:
        directory_path = sys.argv[1]
        if os.path.exists(directory_path):
            list_directory_contents(directory_path)
        else:
            print("Directory does not exist.")

# python directory_info.py "C:\Users\nikitos\OneDrive\Рабочий стол\PYHW1.15" - пример