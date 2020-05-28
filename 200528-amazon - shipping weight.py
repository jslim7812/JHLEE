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
    sweight = re.findall('Weight:</b> .*?s', soup)
    b=str(sweight)[14:-2]
    print("(", j ,"/",len(url_csv), ")", b)
    f.write(b + '\n')
    j += 1

f.close()


