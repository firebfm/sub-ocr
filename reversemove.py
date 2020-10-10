import os
import shutil
import pathlib

# undo moveandmerge.py
# take every image back out of Old folders

print("enter path of old folders to reverse the move")
path = input()
os.chdir(path)
# Put in list all folders
subfolders = [ f.path for f in os.scandir(path) if f.is_dir() and 'Old' in os.path.basename(f)]

listimg = []
for i in range(0, len(subfolders)-1):
    for f in os.listdir(subfolders[i]):
        if f.endswith('.png') or f.endswith('.jpg'):
            listimg.append(os.path.join(subfolders[i], f))
     
for f in listimg:
    shutil.move(f, os.path.join(path, os.path.basename(f)))