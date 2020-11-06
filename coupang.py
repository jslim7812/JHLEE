import requests
import re
import os
from PIL import Image

# http://www.useragentstring.com/ 의 내용 복사
headers = {'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.138 Safari/537.36'}

os.chdir(r'C:/pyml-master/coupang')

#with open("./bieore100.csv") as f:
    #url_csv= f.readlines()

#os.makedirs(r'C:/pyml-master/coupang/image') #**
url = "https://www.coupang.com/vp/products/22674288?itemId=88123406&vendorItemId=70871808157&isAddedCart="

resp = requests.get(url, headers = headers)
soup = resp.text
coup = re.findall('"origin":".*?jpg"}]', soup)
coup2 = "".join(coup[0])
coup3 = re.findall('"origin":".*?jpg', coup2)
#print(len(coup3))

j=1
for j in range(len(coup3)):
        img = coup3[j][10:]
        img2 = "https:"+img
        print(img2)
        r = requests.get(img2)
        file = open("{0:04}-".format(j)+"{0:04}.jpg".format(j),"wb")
        file.write(r.content)
        file.close()
        j = j+1