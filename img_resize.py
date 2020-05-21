from PIL import Image
import os

path = os.chdir(r'c:/pyml-master/3/image')
file_list = os.listdir(path)
os.makedirs('./resize/')

for i in file_list:
    image = Image.open(i)
    resize_image = image.resize((1000,1000))
    resize_image.save('./resize/'+'{}'.format(i))
   
    
