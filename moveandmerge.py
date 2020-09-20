import os
import shutil
import pathlib
from subprocess import run

# ceiling equivalent of // operator
def ceildiv(a, b):
    return -(-a // b)

picAmount = 15
imageMergePath = os.getcwd() + '\\ImageMerge.exe'


print(f'Enter path of cropped images to move every {str(picAmount)} images into created folders then merge')
path = input()
sum = 0
count = 1
dest1 = path + "\\Old" + str(count)
pathlib.Path(dest1).mkdir(parents=True, exist_ok=True) 
os.chdir(path)
# Put in list all files that end with jpg
listjpeg = [os.path.join(path, f) for f in os.listdir(path) if f.endswith(".jpg")]

# Move every 15 images into created folders
for f in listjpeg:
    if  sum % picAmount != 0:
        shutil.move(f, dest1)
    else:
        dest1 = path + "\\Old" + str(count)
        pathlib.Path(dest1).mkdir(parents=True, exist_ok=True)
        shutil.move(f, dest1)
        count += 1
    sum += 1
        
pathlib.Path(path + "\\Merged Images").mkdir(parents=True, exist_ok=True)
numFolders = ceildiv(len(listjpeg), picAmount)
for count in range(1, numFolders + 1):
    os.rename(path + "\\Old"+str(count), path + "\\Old Images")
    run([{imageMergePath}])
    os.rename(path + "\\Merged Images\\merged.jpg", path + f"\\Merged Images\\merged{str(count).zfill(3)}.jpg")
    os.rename(path + "\\Old Images", path + "\\Old"+str(count))
    