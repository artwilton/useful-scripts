import os

directory = 'directory/name/here'

def rename(file):
    print(file.name)

with os.scandir(directory) as entries:
    for entry in entries:
        rename(entry)