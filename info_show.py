import json
file=open("data.txt", "r")
jsonStr=file.read()
file.close()
copii_list=json.loads(jsonStr)
while True:
    copil=input ("Scrie numele: ")
    for prunc in copii_list:
        nume=prunc[0]
        clasa=prunc[1]
        if copil in nume or nume in copil:
            print ("Found match: "+nume+" in class "+clasa)
    print ("-------------------------------------------")
    
