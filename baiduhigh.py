from aip import AipOcr
import os
import re
from shutil import move
from pathlib import Path

# This script is only good for images exported with VideoSubFinder
# Srt is automatically created based on the timestamp filenames.

#APP_ID ='21233964'
#API_KEY ='nT74Rfand5wBq0TVevGGQsMi'
#SECRET_KEY ='fP5E5Ao6BqEeyPPCYmEbZHtU9rWugziZ'

client = AipOcr(APP_ID, API_KEY, SECRET_KEY)

print("Enter path of single unmerged images to OCR:")
path = input()
listimg = [os.path.join(path, f) for f in os.listdir(path) if f.endswith(".jpeg") or f.endswith(".jpg")]
# Sort natural numbers
# listimg.sort(key=lambda f: int(re.sub('\D', '', f)))

# Create folder
Path(path + "\\TXTResults").mkdir(parents=True, exist_ok=True)
Path(path + "\\DONE").mkdir(parents=True, exist_ok=True)
dest1 = path + "\\DONE"

for file in listimg:
    image = open(file, 'rb').read()
    result = client.basicGeneral(image)
    #result = client.basicAccurate(image)
    
    # Full path + same filename as the picture
    completeName = os.path.join(path + "\\TXTResults", Path(file).stem + ".txt")         

    # Writes a txt for each file
    with open(completeName, "w", encoding='utf-8') as resfile:
        for item in result['words_result']:
            resfile.write(item['words'])
            resfile.write('\n')
    print(Path(file).stem)
    
    move(file, dest1)

# Converts the filename to time format
def convertToTime(mytext):
    mytext = re.sub("_", ":", mytext)
    mytext2 = "0" + mytext[:7] + "," + mytext[8:13] + "0" + mytext[13:20] + "," + mytext[21:24]
    mytext = re.sub("::", " --> ", mytext2)
    return mytext

# Combines all the txt files into the final srt
def combinetxt(path):
    txtpath = path + "\\TXTResults"
    listtxt = [os.path.join(txtpath, f) for f in os.listdir(txtpath) if f.endswith(".txt")]
        
    count = 0
    with open(path+"\\final.srt", "a", encoding="utf-8", errors='ignore') as resfile:
        for file in listtxt:
            resfile.write(f"{count+1}")
            resfile.write("\n")
            resfile.write(convertToTime(Path(file).stem))
            resfile.write("\n")
            with open(file, "r", encoding="utf-8", errors='ignore') as readfile:
                for line in readfile:
                    resfile.write(line)
            resfile.write("\n")
            count +=1

# Create the final.srt
combinetxt(path)