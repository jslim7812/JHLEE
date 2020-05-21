import requests
import re
import os
from PIL import Image

# http://www.useragentstring.com/ 의 내용 복사
headers = {'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.138 Safari/537.36'}

os.chdir(r'C:/pyml-master/3')

with open("./yogi_listing2.csv") as f:
    url_csv= f.readlines()

os.makedirs(r'C:/pyml-master/3/image/resize') #**
os.chdir(r'C:/pyml-master/3/image') #**

i = 1
for url in url_csv:
    resp = requests.get(url, headers = headers)
    soup = resp.text
    ama = re.findall('{"hiRes":"h.*?",', soup)
    print("URL","(",i, "/", len(url_csv),")", url)
    
    for j in range(len(ama)):
        img = ama[j][10:-2]
        r = requests.get(img)
        file = open("{0:04}-".format(i)+"{0:04}.jpg".format(j+1),"wb")
        file.write(r.content)
        file.close()
        filename = str(file)[26:-2]
        image = Image.open(filename)
        resize_image = image.resize((1000,1000))
        resize_image.save('./resize/'+filename)
        print(" [", j+1, "/", len(ama), "] ", img, "==>>", file)
    i = i+1

    
    print()
    print()
