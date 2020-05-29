import requests
import re
from bs4 import BeautifulSoup
import pandas as pd
import os

# http://www.useragentstring.com/ 의 내용 복사
headers = {'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.138 Safari/537.36'}

os.chdir(r'C:/pyml-master/3')
  

with open("./bieore100.csv") as f:
    url_csv= f.readlines()

f = open("shipping_weight.csv", "w")

j=1
for url in url_csv:
    resp = requests.get(url, headers = headers)
    soup = resp.text
    soup2 = BeautifulSoup(resp.text, features='lxml')
    sweight = re.findall('Weight:</b> .*?s', soup)
    cate = soup2.find_all("table", id="productDetails_techSpec_section_1")
       
    if len(cate) == 0:
        a=str(sweight)[14:-2]
        print("(", j ,"/",len(url_csv), ")", a)
        f.write(a + '\n')

    else :
        for i in range(0,len(cate)):
            b=cate[i].get_text(" ", strip=True)
            sweight2 = re.findall('Weight .*?s', b)
            c=str(sweight2)[9:-2]
            print("(", j ,"/",len(url_csv), ")", c)
            f.write(c + '\n')

    
    j += 1

f.close()
