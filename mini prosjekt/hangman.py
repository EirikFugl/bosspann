# Hangman
import os
import time
from random_word import RandomWords         #importerer moduler jeg trenger
import sys

r=RandomWords()
os.system("cls")                            #tømmer terminalen
#gjettetOrd="zxzxzxxxzxz"                    #setter gjettetOrd til noe som ikke er i databasen til get_random_word() (hint: linje 20)
strin=0
gjettet=0
hemList=[]
feiList=[]
tegning=0
tegn=["    ----------",
      "\t|\n\t|\n\t|\n\t|\n\t|\n\t|\n\t|\n\t|\n\t|\n\t|\n\t|\n   ----------"
      ]

print(tegn[0])
print(tegn[1])
print("#\t#########\t#\n#######  HANGMAN  #######\n#\t#########\t#")

if input("Enter for å starte\t") == "n":
    os.system("cls")
    exit()
os.system("cls")

print("#\t#########\t#\n#######  HANGMAN  #######\n#\t#########\t#")


while strin==0:
    hemmeligOrd = str.lower(input("\n\nSkriv inn det hemmelige ordet, eller Enter for tilfeldig:\t"))

    while hemmeligOrd == "":                       #her trenger vi greiene fra linje 8
        lengde = input("\n\nSkriv inn lengde på ordet, [ENTER] for ingen begrensning: \t")
        
        try:
            lengde = int(lengde)
        except ValueError:
            if lengde=="":
                hemmeligOrd=r.get_random_word()
                strin=1
            else:
                print("skriv riktig din løk")
        
        
        if isinstance(lengde,int):
            print("Loading...")
            while len(hemmeligOrd)!=lengde:
                hemmeligOrd=r.get_random_word()
                print(hemmeligOrd)

    if not isinstance(hemmeligOrd,str):
        print("\n Skjerpings du, skriv et ord!")
        strin=strin-1
    strin+=1


print(hemmeligOrd)

for i in range (len(hemmeligOrd)):
    hemList.append("-")


# # # # # # # # # S T A R T # # # # # # # # # 
tidStart = time.time_ns()

#for loop



while gjettet==0:
    os.system("cls")
    print("#\t#########\t#\n#######  HANGMAN  #######\t",hemmeligOrd,"\n#\t#########\t#")
    telle=0
    riktig=0

    print("\n\n"+" ".join(hemList))
    print("\n"+" , ".join(feiList))
    guess=input("\n\nGjett en bokstav:\t")

    try:
            guess=str(guess)
            guess=guess.lower()
    except ValueError:
        print("skriv en bokstav!")
        time.sleep(3)
        break

    for bokstav in feiList:
        if bokstav==guess:
            print("Du har allerede gjettet denne bokstaven")
            time.sleep(3)
            break


    for bokstav in hemmeligOrd:
        if bokstav==guess:
            print("Riktig!")
            hemList[telle]=bokstav
            riktig=1
        telle+=1

    if riktig==0:
        if guess not in feiList:
            feiList.append(guess)
        #tegning+=1
        #print(tegn[tegning])

    if "-" not in hemList:
        gjettet=1
        os.system("cls")
        print("#\t#########\t#\n#######  HANGMAN  #######\t",hemmeligOrd,"\n#\t#########\t#")
        print("\n\n"+" ".join(hemList))
        print("\n\nRIKTIG!!!!")        

            
tidSlutt = time.time_ns()
# # # # # # # # # S L U T T # # # # # # # # # 

totTid = round(((tidSlutt-tidStart)/1000000000),4)

#print (tidSlutt, tidStart)
print("\n\nDet tok cirka",totTid,"sekunder å gjette ordet!")