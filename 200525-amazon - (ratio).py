import requests
import re
import os
import time
import random
from PIL import Image

# http://www.useragentstring.com/ 의 내용 복사
headers = {'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.138 Safari/537.36'}

os.chdir(r'C:/pyml-master/3')

with open("./barbie.csv") as f:
    url_csv= f.readlines()

#os.makedirs(r'C:/pyml-master/3/image/resize') #**
os.chdir(r'C:/pyml-master/3/image') #**

i = 100
for url in url_csv[i-1:i]:
    resp = requests.get(url, headers = headers, timeout = 2).text
    #soup = resp.text
    ama = re.findall('{"hiRes":"h.*?",', resp)
    print("URL","(",i, "/", len(url_csv),")", url)
    
    for j in range(len(ama)):
        img = ama[j][10:-2]
        r = requests.get(img)
        file = open("{0:04}-".format(i)+"{0:04}.jpg".format(j+1),"wb")
        file.write(r.content)
        file.close()
        filename = str(file)[26:-2]
        image = Image.open(filename)
        if image.size[0] <= image.size[1]:
            height = 1000
            width = int(image.size[0]/image.size[1]*1000)
        else:
            width = 1000
            height = int(image.size[1]/image.size[0]*1000)
        nsize = (width, height)
        print(nsize)
        
        resize_image = image.resize(nsize)
        background = Image.new('RGB', (1000, 1000), (255, 255, 255, 255))
        offset = (int(round(((1000 - width) / 2), 0)), int(round(((1000 - height) / 2),0)))
        background.paste(resize_image, offset)
        background.save('./resize/'+filename)
        print(" [", j+1, "/", len(ama), "] ", img, "==>>", file)

    i = i+1
    time.sleep( random.uniform(1,3) )

    
    print()
    print()
