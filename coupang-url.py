import requests
from bs4 import BeautifulSoup
import os

# http://www.useragentstring.com/ 의 내용 복사
headers = {'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.97 Safari/537.36'}

os.chdir(r'C:/pyml-master/coupang')
  
"""
with open("./sleepingpadurl.csv") as f:
    url_csv= f.readlines()
"""

f = open("coupnag_url.csv", "w")
url = "https://www.coupang.com/np/products/brand-shop?brandName=%ED%97%A4%EB%9D%BC&page=1"

resp = requests.get(url, headers = headers)
soup = BeautifulSoup(resp.text, features='lxml')
url2 = soup.find_all("a", class_ = "baby-product-link")


for i in range(0, len(url2)):
    a=url2[i].attrs['href']
    b=url2[i].find("div", class_ ="name")
    c=url2[i].find("strong", class_ ="price-value")
    name=b.get_text(" ", strip=True)
    price=c.get_text(" ", strip=True)
    url3= "https://www.coupang.com"+a
    #d=i+1, url3,name,price+"원"
    d=i+1
    e=url3
    print(d)
    f.write(d+e+ '\n')
    i = i+1
f.close()
