# Hangman -- Laget av Eirik

# TIL INFO
# 1. Av en eller annen grunn må du cleare terminalen manuelt før du kjører
# programmet ellers så oppfører det seg ikke
# 2. Hvis du har Mac så må du (kanskje) bytte ut "cls" i os.system("cls") med "clear"
# Eventuelt kjør spørsmål på det og smell inn en variabel men det får du gjøre selv
# 3. IKKE VELG ORD LENGDER LENGRE ENN 15-16 BOKSTAVER ELLER UNDER 3 (hvis de skal være tilfeldige)
# Det tar DRITLANG tid for get_random_word() å finne ordene så plis ikke
# 4. I TEORIEN skal man kunne skrive inn det man vil som hemmelig ord, og gjette hva man vil
# Jeg har prøvd å få til sånn at uansett hva man skriver så skal ikke koden krasje
# Men det går sikkert an så gjerne finn ut av og fiks og oppdater meg

# import - Importerer moduler jeg trenger (random_word må installeres fra pip)

import os                                   # trengs for os.system("cls") som clearer terminalen
import time                                 # trengs for å ta tiden
from random_word import RandomWords         # fikser tilfeldig ord
ossystem='cls' # 'clear'                    # SKIFT HER OM DU BRUKER MAC


# setter opp litt forskjellig
r = RandomWords()
os.system(ossystem)                        
strin=0                     # trengs for å kjøre while løkken som finner hemmeligOrd helt til man har fått et fungerende ord (str)
gjettet=0                   # hvis ordet er gjettet, gjetter = 1, ellers, gjettet = 0. Er for å kjøre spille-loopen til riktig ord er funnet
hemList=[]                  # listifiserer det hemmelige ordet
feiList=[]                  # liste over feile bokstaver
antFeil=0                   # antall feil
tapt=0                      # har du tapt, ja eller nei (1 eller 2)

alfabet=[]                  # lager et alfabet uten at jeg trenger å skrive inn "a","b"...
for bokstav in "abcdefghijklmnopqrstuvwxyzæøå":
    alfabet.append(bokstav)


tegn=[                      # Liste med tegninger (skal IKKE tukles med, sensitivt)

    "\n\n\n\n\n\n\n\n\n\n\n   ----------",
    "\t|\n\t|\n\t|\n\t|\n\t|\n\t|\n\t|\n\t|\n\t|\n\t|\n\t|\n   ----------",
    "\t|----------------\n\t|\n\t|\n\t|\n\t|\n\t|\n\t|\n\t|\n\t|\n\t|\n\t|\n   ----------",
    "\t|----------------\n\t|  /\n\t| /\n\t|\n\t|\n\t|\n\t|\n\t|\n\t|\n\t|\n\t|\n   ----------",
    "\t|----------------\n\t|  /            |\n\t| /\n\t|\n\t|\n\t|\n\t|\n\t|\n\t|\n\t|\n\t|\n   ----------",
    "\t|----------------\n\t|  /            |\n\t| /            ---\n\t|             /   \ \n\t|	      (   )\n\t|	       ---\n\t|\n\t|\n\t|\n\t|\n\t|\n   ----------",
    "\t|----------------\n\t|  /            |\n\t| /            ---\n\t|             /   \ \n\t|	      (   )\n\t|	       ---\n\t|               |\n\t|               |\n\t|               |\n\t|\n\t|\n   ----------",
    "\t|----------------\n\t|  /            |\n\t| /            ---\n\t|             /   \ \n\t|	      (   )\n\t|	       ---\n\t|               |\n\t|            ---|\n\t|               |\n\t|\n\t|\n   ----------",
    "\t|----------------\n\t|  /            |\n\t| /            ---\n\t|             /   \ \n\t|	      (   )\n\t|	       ---\n\t|               |\n\t|            ---|---\n\t|               |\n\t|\n\t|\n   ----------",
    "\t|----------------\n\t|  /            |\n\t| /            ---\n\t|             /   \ \n\t|	      (   )\n\t|	       ---\n\t|               |\n\t|            ---|---\n\t|               |\n\t|              /\n\t|             /\n   ----------",
    "\t|----------------\n\t|  /            |\n\t| /            ---\n\t|             /   \ \n\t|	      (   )\n\t|	       ---\n\t|               |\n\t|            ---|---\n\t|               |\n\t|              / \ \n\t|             /   \ \n   ----------",
    "\t|----------------\n\t|  /            |\n\t| /            ---\n\t|             /x x\ \n\t|	      (   )\n\t|	       ---\n\t|               |\n\t|            ---|---\n\t|               |\n\t|              / \ \n\t|             /   \ \n   ----------",
    "\t|----------------\n\t|  /            |\n\t| /            ---\n\t|             /x x\ \n\t|	      ( O )\n\t|	       ---\n\t|               |\n\t|            ---|---\n\t|               |\n\t|              / \ \n\t|             /   \ \n   ----------",
    
    ]

print("#\t#########\t#\n#######  HANGMAN  #######\n#\t#########\t#")


# denne while løkken gir oss et hemmelig ord enten bestemt av brukeren eller tilfeldig

while strin==0:
    hemmeligOrd =input("\n\nSkriv inn det hemmelige ordet, eller trykk [ENTER] for tilfeldig (potensielt snålt engelsk ord):\t")
    try:
        hemmeligOrd=int(hemmeligOrd)
        print("\nDETTE ER IKKE ET ORD ER DET??")
    except ValueError:
        hemmeligOrd = str.lower(hemmeligOrd)
    

    while hemmeligOrd == "":             
        lengde = input("\n\nSkriv inn lengde på ordet, [ENTER] for ingen begrensning: \t")
        
        try:                            # tester om brukeren skrev inn et tall
            lengde = int(lengde)

            if lengde<3 or lengde>16:   # informerer om lang lastetid
                print("For lang lastetid, avbryter")
                time.sleep(1)
                continue
            elif lengde<4 or lengde>15:
                print("\n ADVARSEL: Sykt lang lastetid!\n")
        
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
                print(hemmeligOrd)                 # gjør denne synlig hvis du kjeder deg under loading

    if not isinstance(hemmeligOrd,str):         # hvis brukeren ikke skrev et ord eller trykket [ENTER] så får de kjeft og løkken kjøres på nytt
        print("\n Skjerpings du, skriv et ord!")
        strin=strin-1
    strin+=1


for bokstav in hemmeligOrd:              # lager hemmelig ord liste og setter den til kun -
    if bokstav==" ":
        hemList.append("-")
    else:
        hemList.append("__")

# # # # # # # # # # # # # # # # # # # # # # #
# # # # # # # # # S T A R T # # # # # # # # #   # selve spillet starter
tidStart = time.time_ns()                       # tiden tas


while gjettet==0:
    os.system(ossystem)
    print("#\t#########\t#\n#######  HANGMAN  #######\t\n#\t#########\t#")
    telle=0
    riktig=0
    repetert=0
    if tapt==1:
        break
    
    print("\n\nOrd:\t\t"+" ".join(hemList))             # printer listene hemmelig liste og feil liste
    print("\nFeil bokstaver:\t"+" | ".join(feiList))
    print("\nBokstaver igjen i alfabetet:\t"+" | ".join(alfabet))
    print(f"\nAntall feil: {antFeil}\n\n")
    
    
    if antFeil>0:                                       # tegner riktig tegning til terminalen
        print(tegn[antFeil-1])                  
        if antFeil>=(len(tegn)):                        # hvis du har tapt, avslutt spillet
             os.system(ossystem)
             print("#\t#########\t#\n#######  HANGMAN  #######\t\n#\t#########\t#")
             print("\n\n\n\n"+tegn[antFeil-1])
             print("\nDU TAPTE !\n\nFyren døde :(\n\nOrdet var "+hemmeligOrd+"!")
             tapt=1
             break

    guess=input("\n\nGjett en bokstav eller et ord:\t")
        
    if guess=="ex1t":                                               # hvis du ikke finner ut av det og vil avslutte
        print(f"Det hemmelige ordet var:\t{hemmeligOrd}\n\n\n")     # bruker ex1t fordi hemmeligOrd ikke kan ha bokstaver og tall
        quit()                                                      # lukker programmet
    
    try:
        guess=int(guess)
        print("DET ER IKKE TALL I ORD ER DET??")# mer kjeft
        time.sleep(2)
        continue
    except ValueError:
        print("",end="")                        # må lage indented block her så maskinen  slutter å mase


    try:                                        # tester om brukeren har skrevet bokstav, og setter den til lowercase
            guess=str(guess)
            guess=guess.lower()
    except ValueError:                          # eventuelt kjeft
        print("\nskriv en bokstav!")
        time.sleep(2)
        break                                   # restarter loopen fra while gjettet==0

    if guess==hemmeligOrd:                      # sjekker om du gjettet riktig ord
        hemList=[]
        for bokstav in hemmeligOrd:             # gjør teit fix og gjerner alle "-" fra hemmelig liste
                hemList.append(bokstav)

    elif guess=="":
        print("\ndu skrev ikke noe, skjerpings!")
        time.sleep(2)
        continue

    elif len(guess)>1:                          # sjekker om du gjettet feil ord 
        print("\ntaper, du gjettet helt feil ord")
        if guess not in feiList:
            feiList.append(guess)
        antFeil+=1
        time.sleep(2)
        continue

    elif guess==" ":                            # gir kjeft om man skriver mellomrom
        print("\nHelst noe mer enn bare mellomrom")
        time.sleep(2)
        continue

    for bokstav in feiList:          # sjekker om bokstaven allerede er skrevet
        if str.lower(bokstav)==guess:
            print("\nDu har allerede gjettet denne bokstaven")
            time.sleep(1.5)
            break
    
    for bokstav in hemList:                     # sjekker om du allerede har gjettet riktig
        if bokstav==guess:
            if repetert==0:
                print("\nDu har allerede gjettet denne bokstaven")
                repetert=1                      # unngår å printe samme melding flere ganger om bokstaven finnes flere ganger i hemmeligOrd
                time.sleep(1)
                continue
    
    for bokstav in hemmeligOrd:                 # sjekker om gjettet bokstav er i hemmelig ord og endrer hemmelig liste tilsvarende
        if bokstav==guess:
            riktig=1                            # unngår å printe samme melding flere ganger om bokstaven finnes flere ganger i hemmeligOrd
            if repetert==0:
                print("\nRiktig!")
                
                try:                            # sjekker om man kan fjerne guess fra alfabetliste
                    alfabet.remove(guess)
                except ValueError:
                    print("",end="")
                
                time.sleep(1)
            hemList[telle]=bokstav
            repetert=1

        telle+=1
    
    if riktig==0:                               # hvis ikke gjettet riktig og gjettet bokstav ikke i feil liste så legg til i feil liste
        if  guess not in feiList:
            feiList.append(guess)
            
            try:                                # sjekker om man kan fjerne guess fra alfabetet
                alfabet.remove(guess)
            except ValueError:
                print("",end="")
            
            antFeil+=1


    if "__" not in hemList:                      # hvis ikke flere ugjettede bokstaver, ordet er gjettet riktig og du vant
        gjettet=1
        telle=0
        for bokstav in hemList:
            if bokstav=="-":
                hemList[telle]=bokstav
            telle+=1
        os.system(ossystem)
        print("#\t#########\t#\n#######  HANGMAN  #######\t\n#\t#########\t#")
        print("\n\n"+" ".join(hemList))
        print(f"\n\nRIKTIG!!!!\nAntall feil:{antFeil}")        

            
tidSlutt = time.time_ns()                       # vi stopper tidtakningen
# # # # # # # # # S L U T T # # # # # # # # # 
# # # # # # # # # # # # # # # # # # # # # # #



totTid = round(((tidSlutt-tidStart)/1000000000),1)
# regner det om til sekunder (time.time_ns() tar unix tid i nanosekunder så det er ganske nøyaktig)

print(f'\n\nDet tok cirka {totTid } sekunder å gjette ordet "{hemmeligOrd}"!\n\n')

time.sleep(30)                                  # i tilfelle man kjører programmet i terminalen