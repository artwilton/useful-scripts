# This script looks at files at the base level of the current directory and renames them.
# It ignores hidden files and directories.

import re
from pathlib import Path

files = Path.cwd().iterdir()

def rename(file_name):

    #seperate file stem and extension (suffix) for easier editing
    file_ext = file_name.suffix
    file_stem = file_name.stem

    #add your regex here
    replace_white_space = re.sub('\s', '_', file_stem)
    remove_special_characters = re.sub('\W', '', replace_white_space)
    final_file_name = remove_special_characters + file_ext

    Path(file_name).rename(final_file_name)

for file_name in files:
    if (file_name.is_file() and not file_name.name.startswith('.')):
        rename(file_name)