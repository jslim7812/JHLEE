import requests
page = requests.get("https://m.post.naver.com/viewer/postView.nhn?volumeNo=28076219&memberNo=45627708")
html_contents = page.text
#print(html_contents)

f=open('text.txt','w', encoding='utf-8')
f.write(html_contents)
f.close()