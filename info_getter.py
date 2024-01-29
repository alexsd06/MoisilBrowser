import requests
from bs4 import BeautifulSoup
import json
cls_cif=['I', 'II', 'III', 'IV', 'V', 'VI', 'VII', 'VIII', 'IX', 'X', 'XI', 'XII']
cls_lit=['A', 'B', 'C', 'D', 'E', 'F', 'G']
base_url="http://info.tm.edu.ro/clasa/"
copii_list=[]
for cif in cls_cif:
    for lit in cls_lit:
        clasa=str(cif)+"_"+str(lit)
        url=base_url+clasa
        data=requests.get(url)
        if (data.status_code==200):
            print ("Found class: "+clasa)
            code=data.text
            soup=BeautifulSoup(code, features="html.parser")
            content=soup.find("div", {"id": "content"})
            for a in content.find_all('a', href=True):
                copil=a['href']
                if "profesori" in copil:
                    continue
                copil=copil.replace('/', '')
                copil=copil.replace('_', ' ')
                copil=copil.replace('-', ' ')
                #print (copil)
                pair=[copil, clasa]
                copii_list.append(pair)
jsonStr=json.dumps(copii_list)
file=open("data.txt", "w")
file.write(jsonStr)
file.close()
print ("Execution ended!")
