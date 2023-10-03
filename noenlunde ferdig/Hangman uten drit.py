# Hangman

# TIL INFO
# 1. Min hangman kommer UTEN tegninger fordi det er stress å lage, gjør det selv
# 2. Av en eller annen grunn må du cleare terminalen manuelt før du kjører
# programmet ellers så oppfører det seg ikke
# 3. Hvis du har Mac så  må du bytte ut "cls" i os.system("cls") med "clear"
# Eventuelt kjør spørsmål på det og smell inn en variabel men det får du gjøre selv
# 4. IKKE VELG ORD LENGDER LENGRE ENN 15-16 BOKSTAVER ELLER UNDER 3
# Det tar DRITLANG tid for get_random_word() å finne ordene så plis ikke


# import - Importerer moduler jeg trenger (random_word må installeres fra pip)

import os                                   # trengs for os.system("cls") som clearer terminalen
import time                                 # trengs for å ta tiden
from random_word import RandomWords         # fikser tilfeldig ord


r=RandomWords()                             
os.system("cls")                        
strin=0                     # trengs for å kjøre while løkken som finner hemmeligOrd helt til man har fått et fungerende ord (str)
gjettet=0                   # hvis ordet er gjettet, gjetter = 1, ellers, gjettet = 0. Er for å kjøre spille-loopen til riktig ord er funnet
hemList=[]                  # listifiserer det hemmelige ordet
feiList=[]                  # liste over feile bokstaver

print("#\t#########\t#\n#######  HANGMAN  #######\n#\t#########\t#")


# denne while løkken gir oss et hemmelig ord enten bestemt av brukeren eller tilfeldig

while strin==0:
    hemmeligOrd = str.lower(input("\n\nSkriv inn det hemmelige ordet, eller trykk [ENTER] for tilfeldig:\t"))

    while hemmeligOrd == "":             
        lengde = input("\n\nSkriv inn lengde på ordet, [ENTER] for ingen begrensning: \t")
        
        try:                            # tester om brukeren skrev inn et tall
            lengde = int(lengde)
        except ValueError:              # hvis ikke, er det kanskje [ENTER] som er tastet og da må vi lage et tilfeldig tall
            if lengde=="":
                hemmeligOrd=r.get_random_word()
                strin=1
            else:                       # eller så har brukeren vært teit og vi gir den kjeft
                print("skriv et tall !!!!!!!")
        
        
        if isinstance(lengde,int):      # hvis det ble skrevet inn et tall så skal vi finne ord med den lengden
            print("Loading...")
            while len(hemmeligOrd)!=lengde:     # denne løkken kjører til vi får ord med riktig lengde
                hemmeligOrd=r.get_random_word()
                #print(hemmeligOrd)                 # gjør denne synlig hvis du kjeder deg under loading

    if not isinstance(hemmeligOrd,str):         # hvis brukeren ikke skrev et ord eller trykket [ENTER] så får de kjeft og løkken kjøres på nytt
        print("\n Skjerpings du, skriv et ord!")
        strin=strin-1
    strin+=1



for i in range (len(hemmeligOrd)):              # lager hemmelig ord liste og setter den til kun -
    hemList.append("-")


# # # # # # # # # S T A R T # # # # # # # # #   # selve spillet starter
tidStart = time.time_ns()                       # tiden tas


while gjettet==0:
    os.system("cls")
    print("#\t#########\t#\n#######  HANGMAN  #######\t\n#\t#########\t#")
    telle=0
    riktig=0


    #print(hemmeligOrd)     # jukselapp

    print("\n\n"+" ".join(hemList))             # printer listene hemmelig liste og feil liste
    print("\n"+" , ".join(feiList))
    guess=input("\n\nGjett en bokstav eller et ord:\t")


    try:                                        # tester om brukeren har skrevet bokstav, og setter den til lowercase
            guess=str(guess)
            guess=guess.lower()
    except ValueError:                          # eventuelt kjeft
        print("skriv en bokstav!")
        time.sleep(3)
        break                                   # restarter loopen fra while gjettet==0

    if guess==hemmeligOrd:                      # sjekker om du gjettet riktig ord
        hemList=[]
        for bokstav in hemmeligOrd:             # gjør teit fix og gjerner alle "-" fra hemmelig liste
                hemList.append(bokstav)

    elif len(guess)>1:                            # sjekker om du gjettet feil ord 
        print("taper du gjettet helt feil ord")
        break

    for bokstav in feiList:                     # sjekker om bokstaven allerede er skrevet feil
        if bokstav==guess:
            print("Du har allerede gjettet denne bokstaven")
            time.sleep(3)
            break

    for bokstav in hemmeligOrd:                 # sjekker om gjettet bokstav er i hemmelig ord og endrer hemmelig liste tilsvarende
        if bokstav==guess:
            print("Riktig!")
            hemList[telle]=bokstav
            riktig=1
        telle+=1

    if riktig==0:                               # hvis ikke gjettet riktig og gjettet bokstav ikke i feil liste så legg til i feil liste
        if guess not in feiList:
            feiList.append(guess)


    if "-" not in hemList:                      # hvis ikke flere ugjettede bokstaver, ordet er gjettet riktig og du vant
        gjettet=1
        os.system("cls")
        print("#\t#########\t#\n#######  HANGMAN  #######\t\n#\t#########\t#")
        print("\n\n"+" ".join(hemList))
        print("\n\nRIKTIG!!!!")        

            
tidSlutt = time.time_ns()                       # vi stopper tidtakningen
# # # # # # # # # S L U T T # # # # # # # # # 


totTid = round(((tidSlutt-tidStart)/1000000000),1)
# regner det om til sekunder (time.time_ns() tar unix tid i nanosekunder så det er ganske nøyaktig)

print(f"\n\nDet tok cirka {totTid }sekunder å gjette ordet!")

# (c) Eirik Midtun 2023