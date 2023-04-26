
from os import listdir
from os.path import isfile, join
import re


mypath = "./nostriches/images"
onlyfiles = [f for f in listdir(mypath) if isfile(join(mypath, f))]

for i in onlyfiles:

    img_name = re.sub('.jpeg', '', i)
    print(img_name)
    with open("nostriches/" + img_name + ".qmd", "w") as file:
        file.write('---\ntitle:' + ' \"\"' + '\n' + 'image: ' + 'images/'+ i + '\n' + '---' + '\n' + '![]' + '(images/' + i +')')