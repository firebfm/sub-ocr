from aip import AipOcr
import os

# This script is useful for all images, including merged.

#APP_ID ='18076987'
#API_KEY ='valGdP9rOgrm5KWs3HQeioq9'
#SECRET_KEY ='V9cf2x9dRqHGSXWAk6oQ8BBOR9LcBj2B'

client = AipOcr(APP_ID, API_KEY, SECRET_KEY)

print(f'Enter path of (merged) images to OCR')
path = input()
os.chdir(path)
listimg = [os.path.join(path, f) for f in os.listdir(path) if f.lower().endswith(('.png', '.jpg', '.jpeg', '.tiff', '.bmp', '.gif'))]
# Sort natural numbers
#listimg.sort(key=lambda f: int(re.sub('\D', '', f)))

for file in listimg:
    image = open(file, 'rb').read()
    result = client.basicGeneral(image)
    #result = client.basicAccurate(image)

    with open("result.txt", "a", encoding='utf-8') as resfile:
        for item in result['words_result']:
            resfile.write(item['words'])
            resfile.write('\n')
    print(file)
