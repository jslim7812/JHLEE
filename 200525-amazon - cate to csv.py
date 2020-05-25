import requests
from bs4 import BeautifulSoup
import os

# http://www.useragentstring.com/ 의 내용 복사
headers = {'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.138 Safari/537.36'}

os.chdir(r'C:/pyml-master/3')
  

with open("./yogi_listing2.csv") as f:
    url_csv= f.readlines()

f = open("yogi_cate.csv", "w")


for url in url_csv:
    resp = requests.get(url, headers = headers)
    soup = BeautifulSoup(resp.text, features='lxml')
    cate = soup.find_all("a", class_ = 'a-link-normal a-color-tertiary')
    cate_list=[]
    for i in range(0,len(cate)):
        a=cate[i].get_text(" ", strip=True)
        cate_list.append(a)
    b=(" > ".join(cate_list))
    print(b)
    f.write(b + '\n')
f.close()
   
    


