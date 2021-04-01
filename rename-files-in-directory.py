# This script ignores hidden files and directories

from pathlib import Path

directory = 'directory/name/here'

def rename(file):
    print(file.name)

files = Path(directory).iterdir()

for file_name in files:
    if (file_name.is_file() and not file_name.name.startswith('.')):
        rename(file_name)