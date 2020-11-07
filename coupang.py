import requests
from bs4 import BeautifulSoup
import re
import os
import csv

# http://www.useragentstring.com/ 의 내용 복사
headers = {'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.97 Safari/537.36'}

os.chdir(r'C:/pyml-master/coupang')

brandName = '헤라' #검색어(브랜드네임) 지정
page = 3 #페이지수 지정


datalist=[]
for i in range(1,page+1):
    url = "https://www.coupang.com/np/products/brand-shop?brandName="+brandName+"&page="+str(i)
    resp = requests.get(url, headers = headers)
    soup = BeautifulSoup(resp.text, features='lxml')
    url2 = soup.find_all("a", class_ = "baby-product-link")
    for j in range(0, len(url2)):
        a=url2[j].attrs['href']
        b=url2[j].find("div", class_ ="name")
        c=url2[j].find("strong", class_ ="price-value")
        name=b.get_text(" ", strip=True)
        price=c.get_text(" ", strip=True)
        url3= "https://www.coupang.com"+a
        data = []
        data.append(url3)
        data.append(name)
        data.append(price)
        datalist.append(data)
        s=(j+1)+60*(i-1)
        print(str(s)+".", "[ "+url3+" ],", "[ "+name+" ],", "[ "+price+"원 ]")
        resp2 = requests.get(url3, headers = headers)
        soup = resp2.text
        coup = re.findall('"origin":".*?jpg"}]', soup, flags=re.IGNORECASE)
        
        if len(coup) == 0:
            coup = re.findall('"origin":".*?g"}]', soup, flags=re.IGNORECASE)
            coup2 = "".join(coup[0])
            coup3 = re.findall('"origin":".*?g"', coup2, flags=re.IGNORECASE)
            for k in range(len(coup3)):
                img = coup3[k][10:-1]
                img2 = "https:"+img
                print(img2)
                r = requests.get(img2)
                file = open("{0:04}-".format(s)+"{0:04}.jpg".format(k+1),"wb")
                file.write(r.content)
                file.close()
        else :
            coup2 = "".join(coup[0])
            coup3 = re.findall('"origin":".*?g"', coup2, flags=re.IGNORECASE)
            for k in range(len(coup3)):
                img = coup3[k][10:-1]
                img2 = "https:"+img
                print(img2)
                r = requests.get(img2)
                file = open("{0:04}-".format(s)+"{0:04}.jpg".format(k+1),"wb")
                file.write(r.content)
                file.close()
        
with open(brandName+'.csv','w', newline='') as f: 
    a = csv.writer(f) 
    for value in datalist: 
        a.writerow(value)
