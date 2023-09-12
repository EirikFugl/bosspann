personer = {   
    "Sophie": 18, "Noah": 18, "Olivia": 29, 
    "Oscar": 21,   "Oliver": 25, "Sofia": 27, 
    "Ella": 23, "Leah": 21,   "Lucas": 23, 
    "Maya": 25, "Isaac": 29, "Axel": 27,    
    "Frida": 23, "Emil": 26, "Emma": 23, 
    "Ingrid": 18, "Phillip": 25, "Jacob": 24, 
    "Nora": 21, "William": 22 
    } 

liste=[]
listefolk=[]

for k,v in personer.items():
    if v not in liste:
        liste.append(int(v))
        listefolk.append(k)

unikealdre={}
print(liste,'\n',listefolk)
a=0
for i in listefolk:
    unikealdre[i]=int(liste[a])
    a+=1

print(unikealdre)