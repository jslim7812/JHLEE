import requests
import re
import glob, os, shutil
import time
import random
from PIL import Image
from selenium import webdriver
from bs4 import BeautifulSoup

# http://www.useragentstring.com/ 의 내용 복사
headers = {'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.138 Safari/537.36'}

os.chdir(r'C:/pyml-master/3') #요기

with open("./ravensburger2.csv") as f: #요기
    url_csv= f.readlines()

#os.makedirs(r'C:/pyml-master/3/image/resize/1') #요기
os.chdir(r'C:/pyml-master/3/image') #요기
path = "c:/crawling/chromedriver.exe"


i = 36
for url in url_csv[i-1:]:
    while True:
        wd = webdriver.Chrome(path)
        wd.get(url)
        html = wd.page_source
        bs = BeautifulSoup(html, 'html.parser').get_text()
        ama = re.findall('{"hiRes":"h.*?",', bs)
        wd.close()
        #resp = requests.get(url, headers = headers, timeout = 2).text
        #soup = resp.text
        #ama = re.findall('{"hiRes":"h.*?",', resp)
        print("URL","(",i, "/", len(url_csv),")", url, "(",len(ama),")")
        time.sleep( random.uniform(0,1))
        if len(ama) != 0:
            #break

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
            break

    i = i+1
    time.sleep( random.uniform(1,3) )

    
    print()
    print()

#대표이미지 '/1'폴더로 복사
files = glob.iglob(os.path.join('./resize/', "*01.jpg"))
for file in files:
    if os.path.isfile(file):
        shutil.copy2(file, './resize/1')
