import os
import re
from pathlib import Path

def convertToTime(mytext):
    mytext = re.sub("_", ":", mytext)
    mytext2 = "0" + mytext[:7] + "," + mytext[8:13] + "0" + mytext[13:20] + "," + mytext[21:24]
    mytext = re.sub("::", " --> ", mytext2)
    return mytext

def create_empty_sub():
    print("enter path of images to create empty sub")
    path = input()
    listimg = [os.path.join(path, f) for f in os.listdir(path) if f.lower().endswith(('.jpg', '.jpeg'))]
        
    count = 0
    with open(path+'\\empty_sub.srt', 'w', encoding='utf-8', errors='ignore') as resfile:
        for file in listimg:
            resfile.write(f"{count+1}")
            resfile.write("\n")
            resfile.write(convertToTime(Path(file).stem))
            resfile.write("\n")
            resfile.write("\n")
            count +=1

create_empty_sub()