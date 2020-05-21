from googletrans import Translator
import pandas as pd
import os

os.chdir(r'C:/pyml-master/3')
  
csv = pd.read_csv('./Search Term of Yogi tea.csv')
plist = csv["Product Name"]   
f = open("Product_list.csv", "w")
translator = Translator()

j=1
for i in plist:
    tr_results = translator.translate(i, dest='ko')
    a=tr_results.text
    print("(", j ,"/",len(plist),")"," ", a)
    f.write(a + '\n')
    j += 1

f.close()

