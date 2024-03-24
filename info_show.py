import json
file=open("data.txt", "r")
jsonStr=file.read()
file.close()
copii_list=json.loads(jsonStr)
while True:
    copil=input ("Scrie numele: ")
    for prunc in copii_list:
        nume_copil=prunc[0]
        clasa_copil=prunc[1]
        copil_good=True
        for nume in copil.split(' '):
            if nume not in nume_copil:
                copil_good=False
                break
        if copil_good==True:
            print ("Found match: "+nume_copil+" in class "+clasa_copil)
    print ("-------------------------------------------")
    
