import time                         #gir deg litt ventetid her og der
from colorama import Fore           # gir deg farger
import os                           # clearer terminalen
os.system('cls')


##########################################################################

# FIVE STEPS TO GREATNESS:

# 1. FIKSE DEKOMPRIMERING (Skrive over fra ny algoritme.py) DONE SÅNN CIRKA ISH EGENTLIG
# 2. FIKSE FILSYSTEM (.SJEF (Super Jalla Eirik Fil) fil) SJEF FUNKER, FIKS RESTEN AV LASTING
# 3. RYDDE OPP FUNKSJONER (standardisere og fikse return istedenfor det dritet som er nå)
#    Gjøre inputs og print i match case steget, ikke i selve funksjonen
# 4. GJØRE SÅNN AT MATCH CASE MULIGHETER DUKKER OPP ETTERHVERT SOM TING BLIR MULIG
#    Ingen "du må gjøre x før y", men at du kan ikke gjøre x før y er gjort


# 5. FIKSE ALGORITME (m,p,s for ikke-mellomrom, punktum, stor bokstav) (mulig V2)
#    Bør være rimelig enkelt, men må inn med noen if-er

# 6. FIKSE MØNSTERGJENKJENNING (mulig V3)
#    Vet at det kan gå an, ingen peiling på hvordan

# 7. OPTIONAL: FIKSE INPUTS MED TRY EXCEPT (drit kjedelig, men viktig)
#    JÆVELIG VIKTEIG MEN FORBANNEDE KJEDELIGE
#    Første input, match case input, hver fil input
#    Jo Bjørnar hvis dette ikke funker i komprimering_V2_Final_Endelig_ferdig-v5.py så
#    er det fordi jeg bare ikke gidder fordi jeg har bedre ting å finne på

#############################################################################


# BUG LISTE MÅ FIKSES:
# SkrivKompTil krever to filplasseringer, kan fikses i steg 3
# Litt usikker på hva self.ORDukomp og self.TALLukomp er

class Tekst:
    """Inneholder tekst som kan komprimeres, endres eller dekomprimeres"""

    def __init__(self,string):
        self.string = string
        self.HEMMELIGSEPARATOR="#1?=;`|"

        self.komprimert=0
        self.ORDktf = "" # ORD komprimert til fil - midlertidig lagring som skal skrives til fil
        self.TALLktf = "" # TALL komprimert til fil - midlertidig lagring som skal skrives til fil
        self.ORDukomp = ""
        self.TALLukomp = ""


    def __str__(self):
        """Gir deg teksten til et objekt, returnerer det som verdi"""

        return self.string

    def printKomp(self):
        print(self.ORDktf,"\n\n",self.TALLktf)

    def endreTekst(self,nytekst=""):
        """Endrer teksten"""

        print(f"Nåverende tekst:\n\n{self.string}")
        endretTekst=str(input("Endre tekst? [Y/N]:\t"))
        if str.lower(endretTekst)=="y":
            self.string=nytekst
            print(self.string)
            self.komprimert=0
            print("Endret")
            
        elif endretTekst=="N":
            print("Ikke endret")
            
    
    def sizeTekst(self):
        """Gir deg størrelsen til teksten"""

        from sys import getsizeof
        return getsizeof(self.string)
    
    def sizeKomp(self):
        """Regner ut hvor mye komprimering som gjøres"""
        
        from sys import getsizeof
        orgtekst=getsizeof(self.string)

        if self.komprimert==1:            
            komptekst=getsizeof(self.TALLktf)+getsizeof(self.ORDktf)
            komprimering=komptekst/orgtekst*100
            print(komprimering,"%")

            print(f"Størrelse i minnet, originaltekst:\n{orgtekst}\n\nStørrelse i minnet, komprimert:\n{komptekst}\n\nKomprimering:\n{round(komprimering,0)}%")
            if komptekst > orgtekst:
                print(f"Komprimeringen gjør i dette tilfellet filen {round(komprimering-100,0)}% større")
        else:
            print(f"Størrelse i minnet, originaltekst:\n{getsizeof(self.string)}\n\nKjør komprimering for å få komprimert størrelse")


    # def lastTekst(self,filnavn):
    #     """WORK IN PROGRESS"""
    #     textInn = open(filnavn,"r")
    #     self.string = textInn
    #     print(self.string)

    def lastKomp(self,filnavn):

        with open(filnavn,'r') as f:
            linje1=f.readlines()[0]
            linje2=f.readlines()[1]
        self.ORDktf=linje1
        self.TALLktf=linje2


    def zimbabwe(self):
        print(f"{self.ORDktf}\n{self.ORDukomp}\n{self.TALLktf}\n{self.TALLukomp}")



    def skrivTekstTil(self,filnavn):
        """Skriver teksten til en fil"""

        with open(filnavn,"w") as f:
            f.write(str(self.string))


    def skrivKompTil(self,filnavn):
        """Skriver den komprimerte teksten til en fil"""

        with open(filnavn,"a") as f:
            f.write((self.ORDktf))
            f.write(("\n"))
            f.write((self.TALLktf))


    def komprimer(self):
        """Komprimerer teksten ved hjelp av en avansert komprimeringsalgoritme"""

        lengde=0
        start=0
        self.komprimert=1
        endelig=[]
        

        seps = [" ",".",",",":",";"]

        #hvert ord separert av '.', ',', ' ', etc. skal ligge i en liste, og ha en annen liste med indeksene deres

        for bokstav in self.string:

            if bokstav in seps:
                endelig.append(self.string[start:(start+lengde)])
                endelig.append(bokstav)


                start+=lengde+1
                lengde=0
            
            else:
                lengde+=1


            ordliste = []
            talliste = []

            for ord_eller_separator in endelig:
                if ord_eller_separator not in ordliste:
                    ordliste.append(ord_eller_separator)
                    talliste.append(ordliste.index(ord_eller_separator))
                else:
                    talliste.append(ordliste.index(ord_eller_separator))
                    pass

        self.HEMMELIGSEPARATOR="#1?=;`|"

        tString=''
        for item in talliste:
            tString+=str(item)
            tString+=","

        oString=''
        for item in ordliste:
            oString+=str(item)
            oString+=self.HEMMELIGSEPARATOR

        self.ORDktf=oString
        self.TALLktf=tString

        print("Ordliste:\n",self.ORDktf.split(self.HEMMELIGSEPARATOR),"\n\nTalliste:\n",self.TALLktf)

    def printKomp(self):

        ba=Tekst(self.string)
        ba.komprimer()
        return ("Ordliste:\n",self.ORDktf,"\n\nTalliste:\n",self.TALLktf)

    def filKomp(self,filnavn):
        """Komprimerer teksten ved hjelp av en avansert komprimeringsalgoritme\nSender den dermed til filen UTPUT.txt"""

        self.komprimert=1
        ab=Tekst(self.string)
        ab.komprimer()
        skrivkomptingtil=input("Skriv inn filplassering")
        if skrivkomptingtil=="":
            skrivkomptingtil=r"Objekt orientert\komprimering\UTPUTKOMP.txt"
        ab.skrivKompTil(skrivkomptingtil)
        print("\n\nFerdig!")
    
    def dekomprimer(self):
        fTalliste = self.TALLktf.split(",")

        fTalliste.pop(-1)   # fjerner den siste tingen i listen, er alltid tom

        for ting in fTalliste:          # gjør tallene til faktiske tall
            fTalliste[fTalliste.index(ting)]=int(ting)
        
        self.TALLukomp=fTalliste

        print(self.TALLukomp)

        fOrdliste = self.ORDktf.split(self.HEMMELIGSEPARATOR)

        fOrdliste.pop(-1)

        print(self.ORDukomp)

        self.ORDukomp=fOrdliste

        print("Dekomprimert!")
    
    def printDekomp(self):
        print("\n\nDekomprimert tekst:\n")
        for tall in self.TALLukomp:
            print(self.ORDukomp[int(tall)],end="")

        



tekst=input("Skriv inn din tekst:\t")
if tekst=="":
    tekst=Tekst("The European languages are members of the same family. Their separate existence is a myth. For science, music, sport, etc, Europe uses the same vocabulary. The languages only differ in their grammar, their pronunciation and their most common words. Everyone realizes why a new common language would be desirable: one could refuse to pay expensive translators. To achieve this, it would be necessary to have uniform grammar, pronunciation and more common words. If several languages coalesce, the grammar of the resulting language is more simple and regular than that of the individual languages. The new common language will be more simple and regular than the existing European languages. It will be as simple as Occidental; in fact, it will be Occidental. To an English person, it will seem like simplified English, as a skeptical Cambridge friend of mine told me what Occidental is.The European languages are members of the same family. Their separate existence is a myth. For science, music, sport, etc, Europe uses the same vocabulary. The languages only differ in their grammar, their pronunciation and their most common words. Everyone realizes why a new common language would be desirable: one could refuse to pay expensive translators.")
    print(f"Bruker standardtekst: The European languages")



while True:

    print(f"{Fore.WHITE}\n\nHva vil du gjøre? Skriv inn tallet tilsvarende funksjonen du vil bruke:\n")
    print(f"{Fore.RED}1. Printe teksten\n2. Endre teksten (endreTekst())\n3. Få størrelsen til teksten (sizeTekst())\n4. Få størrelsen til den komprimerte teksten (sizeKomp())\n5. Skrive tekst til fil (skrivTekstTil())\n6. Skrive komprimert tekst til fil (skrivKompTil())\n7. Komprimere tekst ved hjelp av ERM algoritmen (komprimer())\n8. Komprimere tekst og sende den til fil (filKomp())\n9. Dekomprimere teksten (dekomp()){Fore.GREEN}\n")
    a=int(input())                              # FIKS INT TING MAN KAN SKRIVE KUN TALL TRY EXCEPT
    match a:
        case 1: print(f"\n{tekst}\n")                   #   Printer teksten
        
        case 2:                                         #   Endrer teksten
            # print(f"Gammel Tekst:\n{tekst}\n\n")
            tekst.endreTekst(str(input("Ny tekst:\n")))

        case 3: print(tekst.sizeTekst())                #   Gir tekstens størrelse
        
        case 4: tekst.sizeKomp()                        #   Gir tekstens størrelse og 
        
        case 5:                                         #   Skriver teksten til en fil

            skrivteksttilting=input("Skriv inn filnavn [ENTER] for default (UTPUT.txt):\t")
            if skrivteksttilting=="":
                skrivteksttilting=r"Objekt orientert\komprimering\UTPUT.txt"
            tekst.skrivTekstTil(skrivteksttilting)
            print(f"Ferdig! Skrev til {skrivteksttilting}")
        
        case 6:                                         # Skriver komprimert tekst til en fil
            
            skrivkomptingtil=input("Skriv inn filnavn [ENTER] for default (KompUt.sjef):\t")
            if skrivkomptingtil=="":
                skrivkomptingtil=r"Objekt orientert\komprimering\KompUt.sjef"
            tekst.skrivKompTil(skrivkomptingtil)
            print(f"Ferdig! Skrev til {skrivkomptingtil}")
        
        case 7: 
            
            tekst.komprimer()
            print("\nKomprimert!")
        
        case 8: 
            
            abab=input("Skriv inn filnavn [ENTER] for default (UTPUTKOMP.txt):\t")
            if abab=="":
                abab=r"Objekt orientert\komprimering\UTPUTKOMP.txt"
            tekst.filKomp(abab)
        
        case 9: 
            tekst.dekomprimer()

        case 10:
            tekst.printDekomp()

        case 11:

            tekst.zimbabwe()


    time.sleep(1)