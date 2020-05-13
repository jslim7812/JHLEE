import requests
from urllib.request import urlopen
from urllib.parse import quote_plus
from bs4 import BeautifulSoup
from selenium import webdriver
import time
# http://www.useragentstring.com/ 의 내용 복사
headers = {'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.138 Safari/537.36'}

url = 'https://www.amazon.com/Yogi-Tea-Variety-Sampler-Symptom/dp/B07WQFWGHV/ref=sr_1_2?dchild=1&keywords=Yogi+tea&qid=1588738362&refinements=p_85%3A2470955011&rnid=2470954011&rps=1&sr=8-2'

resp = requests.get(url, headers = headers)

soup = BeautifulSoup(resp.content, features='lxml')
ama = soup.select('span')

print(ama)