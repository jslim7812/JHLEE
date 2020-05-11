import cgi
import requests

index = 1

def downloadURLResource(url):
    global index
    r = requests.get(url.rstrip(), stream=True)
    if r.status_code == 200:
        targetFileName="{0:05}.jpg".format(index)
        with open("{}/{}".format(SAVE_DIR, targetFileName),'wb') as f:
            for chunk in r.iter_content(chunk_size=1024):
                f.write(chunk)
        index += 1
        return targetFileName

with open('123.csv') as f:
    print(list(map(downloadURLResource, f.readlines())))
