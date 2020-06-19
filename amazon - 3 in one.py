from bs4 import BeautifulSoup
import requests
import re
import os
from PIL import Image

# http://www.useragentstring.com/ 의 내용 복사
headers = {'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.106 Safari/537.36'}

os.chdir(r'C:/pyml-master/3')

with open("./bieore100.csv") as f:
    url_csv= f.readlines()

f = open("bieore_cate.csv", "w")
g = open("bieore_weight.csv", "w")

os.makedirs(r'C:/pyml-master/3/image/resize') #**
os.chdir(r'C:/pyml-master/3/image') #**

i = 1

for url in url_csv:
    resp = requests.get(url, headers = headers)
    soup = resp.text
    soup2 = BeautifulSoup(resp.text, features='lxml')
    ama = re.findall('{"hiRes":"h.*?",', soup)
    cate = soup2.find_all("a", class_ = 'a-link-normal a-color-tertiary')
    sweight = re.findall('Weight:</b> .*?s', soup)
    pdetail = soup2.find_all("table", id="productDetails_techSpec_section_1")
    cate_list=[]

## categories
    for k in range(0,len(cate)):
        a=cate[k].get_text(" ", strip=True)
        cate_list.append(a)
    b=(" > ".join(cate_list))
    f.write(b + '\n')
    print("URL","(",i, "/", len(url_csv),")", url)
    print("Categories : ", b)
     
## shippingweight
    if len(pdetail) == 0:
        a=str(sweight)[14:-2]
        print("Weight : ", a)
        g.write(a + '\n')

    else :
        for l in range(0,len(pdetail)):
            b=cate[l].get_text(" ", strip=True)
            sweight2 = re.findall('Weight .*?s', b)
            c=str(sweight2)[9:-2]
            print("Weight : ", c)
            g.write(c + '\n')

## resizing image              
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
                
        resize_image = image.resize(nsize)
        background = Image.new('RGB', (1000, 1000), (255, 255, 255, 255))
        offset = (int(round(((1000 - width) / 2), 0)), int(round(((1000 - height) / 2),0)))
        background.paste(resize_image, offset)
        background.save('./resize/'+filename)
        print(" [", j+1, "/", len(ama), "] ", nsize, img, "==>>", file)
    i = i+1
    
    print()
    print()
f.close()
g.close()
