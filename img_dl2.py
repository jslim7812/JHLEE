import urllib.request
from bs4 import BeautifulSoup
 
url = 'http://www.applen.or.kr/news/articleView.html?idxno=58429'
url_base = 'http://www.applen.or.kr'
req = urllib.request.Request(url)
res = urllib.request.urlopen(url).read()
 
soup = BeautifulSoup(res,'html.parser')
images = soup.find_all("img")

for i, img in enumerate(images):
    src = img.get('src')
    link = url_base + src
    urllib.request.urlretrieve(link, './img/'+'{}.jpg'.format(i))
