import requests
from bs4 import BeautifulSoup
import os
import time

# http://www.useragentstring.com/ 의 내용 복사
headers = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.97 Safari/537.36'}
os.chdir(r'C:/pyml-master/3')

with open("./Tent150.csv") as f:
    url_csv= f.readlines()

f = open("rain_cate.csv", "w")

j = 1
for url in url_csv:
    resp = requests.get(url, headers = headers)
    soup = BeautifulSoup(resp.text, features='lxml')
    cate = soup.find_all("a", class_ = 'a-link-normal a-color-tertiary')
    cate_list=[]
    time.sleep(0.5)
    for i in range(0,len(cate)):
        a=cate[i].get_text(" ", strip=True)
        cate_list.append(a)
    b=(" > ".join(cate_list))
    print("(", j ,"/",len(url_csv), ")", b)
    f.write(b + '\n')
    j += 1
f.close()
