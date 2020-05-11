import urllib.request
from bs4 import BeautifulSoup

print('Beginning file download with urllib2...')
 
url = 'https://movie.naver.com/movie/bi/mi/basic.nhn?code=157297'
req = urllib.request.Request(url)
res = urllib.request.urlopen(url).read()
 
soup = BeautifulSoup(res,'html.parser')
soup = soup.find("div",class_="poster")
#img의 경로를 받아온다
imgUrl = soup.find("img")["src"]

################################ 원본이미지 받는 코드
imgUrl2 = imgUrl.find('?')
#print(imgUrl2)
imgUrl3 = imgUrl[0:imgUrl2]
#print(imgUrl3)
################################


#urlretrieve는 다운로드 함수
#img.alt는 이미지 대체 텍스트 == 마약왕
urllib.request.urlretrieve(imgUrl, soup.find("img")["alt"]+'.jpg')
#urllib.request.urlretrieve(imgUrl3, soup.find("img")["alt"]+'.jpg') #원본이미지 받는 
