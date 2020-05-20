import requests
import re
import os

# http://www.useragentstring.com/ 의 내용 복사
headers = {'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.138 Safari/537.36'}


with open("./yogi_listing2.csv") as f:
    url_csv= f.readlines()
   
i = 1
for url in url_csv:
    resp = requests.get(url, headers = headers)
    soup = resp.text
    ama = re.findall('hiRes":".*?",', soup)
    print("URL","(",i, "/", len(url_csv),")", url)
    i = i+1

    for j in range(len(ama)):
        img = ama[j][8:-2]
        print(" [", j+1, "/", len(ama), "] ", img)
    
    print()
    print()
