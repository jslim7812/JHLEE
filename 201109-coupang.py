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

if not os.path.isdir(brandName):
    os.mkdir(brandName)
os.chdir('./'+brandName)

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
        if c == None:
            price = "None"
        else:
            price=c.get_text(" ", strip=True)
        url3= "https://www.coupang.com"+a
        
        s=(j+1)+60*(i-1)
        
        resp2 = requests.get(url3, headers = headers)
        soup = resp2.text
        cate = re.findall('parentsCategoryNames":(.+?)"KAN"', soup)
        cate2 = "".join(cate)
        cate3 = re.findall('"(.+?)"', cate2)
        cate3.reverse()
        coup = re.findall('parentsCategoryNames.*?hasBrandShop', soup, flags=re.IGNORECASE)
        coup2 = "".join(coup)
        coup3 = re.findall('"origin":".*?g"', coup2, flags=re.IGNORECASE)
        
        print(str(s)+".", cate3)
        print("[ "+name+" ]", "[ "+price+"원 ]")

        for k in range(len(coup3)):
            img = coup3[k][10:-1]
            img2 = "https:"+img
            img3 = "{0:04}-".format(s)+"{0:04}.jpg".format(k+1)
            print(img3)
            r = requests.get(img2)
            file = open(img3,"wb")
            file.write(r.content)
            file.close()
        data = []
        data.append(url3)
        data.append(cate3)
        data.append(name)
        data.append(price)
        datalist.append(data)
         
with open(brandName+'.csv','w', encoding = 'utf-8-sig', newline='') as f: 
    a = csv.writer(f) 
    for value in datalist: 
        a.writerow(value)
