import os
import re

# 0 find_empty: identify empty lines if 北京 appears consecutively
# 1 find double lines (sandwich) and merge with /N excluding empty
# 2 find double lines (beijing start) and merge with /N
# 3 remove all beijing by itself at the start
# 4 remove all empty lines

def find_empty(txtpath, beijing, empty):
    contents = ""
    numEmpty = 0
    with open(txtpath, 'r', encoding='utf-8') as f:
        lines = f.readlines()
        for line in lines:
            if line.strip() == beijing:
                numEmpty += 1
                if line is lines[-1]:
                    contents += f'{empty}\n'*(numEmpty)                
            else:
                if numEmpty >= 2:
                    contents += f'{empty}\n'*(numEmpty-1)
                    contents += f'{beijing}\n'
                elif numEmpty == 1:
                    contents += f'{beijing}\n'

                contents += line    
                numEmpty = 0
    return contents                

beijing = "北京"
bei = beijing[0]
empty = "empty"
e = empty[0]

print(f'Enter path of result.txt excluding filename')
txtpath = input() + '\\result.txt'
contents = find_empty(txtpath, beijing, empty)
contents = re.sub(rf'{beijing}\n([^{bei}].*)\n([^{bei}{e}].*$)', rf'{beijing}\n\1\\N\2\n', contents, 0, re.M)
contents = re.sub(rf'^{beijing}([^\n]+)\n(.*$)', rf'{beijing}\n\1\\N\2\n', contents, 0, re.M)
contents = re.sub(rf'^{beijing}$', '', contents, 0, re.M)
contents = "\n".join([line for line in contents.split('\n') if line.strip()])
with open(os.path.dirname(txtpath)+'\\result_2.txt', 'w', encoding='utf-8') as g:
    g.write(contents)
