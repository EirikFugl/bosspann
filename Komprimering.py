import time
from colorama import Fore
import os
os.system('cls')

# Oppgradere komprimering:
# fjerne mellomrom, fjerne stor bokstav, punktum


# setter opp default filer
defaultTINN=r"TekstINN.txt"
defaultTUT=r"TekstUT.txt"
defaultKINN=r"KompINN.sjef"
defaultKUT=r"KompUT.sjef"

with open("EKSEMPELTEKST.sjef","r") as f:
    defaultTEKST=f.read()

# definerer farger
hvit = Fore.WHITE
rød = Fore.RED
blå = Fore.BLUE
grønn = Fore.GREEN
gul = Fore.YELLOW


# lages tekstklasse
class Tekst:
    """Inneholder tekst som kan komprimeres, endres eller dekomprimeres"""
    def __init__(self,string):
        self.string = string
        
        self.HEMSEP = "§¨~"
        self.komprimert = False
        self.kompTid = 0
        self.ORDkomp = ""
        self.TALLkomp = ""
        self.ORDukomp = ""
        self.TALLukomp = ""
        self.DekomString = ""
        self.dekomprimert = False

    
    def __str__(self):
        """Gir deg teksten til et objekt, returnerer det som string"""
        return self.string
    
    def kompTekst(self):
        """Gir deg teksten i komprimert form"""
        return f"Ordliste:\n{self.ORDkomp}\n\nTalliste:{self.TALLkomp}"
    
    def endreTekst(self,nytekst):
        """Endrer teksten"""

        self.string=nytekst

        self.dekomprimert = False
        self.komprimert = False

    def sizeTekst(self):
        """Gir deg tekstens størrelse i minnet"""
        from sys import getsizeof
        
        return int(getsizeof(self.string))
    
    def sizeKomp(self):
        """Gir deg størrelsen av den komprimerte teksten"""
        from sys import getsizeof

        return int(getsizeof(self.ORDkomp)+getsizeof(self.TALLkomp))
    
    def sizeFil(self,filnavn):
        """Gir deg størrelsen til en fil"""
        from sys import getsizeof

        return int(getsizeof(filnavn))

    def lastTekst(self, filnavn):
        """Laster tekst fra fil"""

        with open(filnavn,"r") as f:
            self.string=f.read()
        
        self.komprimert = False
        self.dekomprimert = False
        
    def lastKomp(self,filnavn):
        """Laster komprimert tekst fra fil"""               # FIKS LIST OUT OF INDEX TING - LAV PRIORITET

        with open(filnavn,"r") as f:
            linje1=f.readlines()[0]
            linje2=f.readlines()[1]
        self.ORDkomp = linje1
        self.TALLkomp = linje2


    def skrivTekstTil(self,filnavn):
        """Skriver teksten til en fil"""
        
        with open(filnavn,"w") as f:
            f.write(str(self.string))
    
    def skrivKompTil(self,filnavn):
        """Skriver komprimert tekst til en fil"""
        
        with open(filnavn,"w") as f:
            pass
        
        with open(filnavn,"a") as  f:
            f.write(self.ORDkomp)                           # SJEKK DETTE - NEWLINE OG SÅNT - LAV PRIORITET
            f.write(self.TALLkomp)

    def komprimer(self):                                   
        """Komprimerer teksten"""

        lengde = 0
        start = 0
        self.komprimert=True
        endelig = []
        global tidStart
        tidStart = time.time_ns()

        seps = [" ",".",",",":",";"]

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

        for ordEsep in endelig:
            if ordEsep not in ordliste:
                ordliste.append(ordEsep)
                talliste.append(ordliste.index(ordEsep))
            else:
                talliste.append(ordliste.index(ordEsep))
            
        
        mellomrom=ordliste.index(" ")
        

        print(len(talliste))
        print(talliste)
        
        # i=0
        # while i < len(talliste)-1:
        #     if talliste[i+1] == mellomrom:
        #         talliste[i] = "m"+str(talliste[i])
        #         talliste.pop(talliste[i+1])
        #     i+=1

        # for ting in talliste:
        #     if ting == mellomrom:
        #         talliste.pop(talliste.index(mellomrom))

    
        
        
        tString = ""

        for tall in talliste:
            tString+=str(tall)
            tString+=","
        
        oString = ""
        for ord in ordliste:
            oString+=str(ord)
            oString+=self.HEMSEP
        
        self.TALLkomp=tString
        self.ORDkomp=oString

        global tidStopp
        tidStopp = time.time_ns()

        self.kompTid = tidStopp-tidStart
    
    def kompStatus(self):
        """Sier om komprimering er kjørt"""

        return self.komprimert

    def tidKomp(self):
        """Gir tiden det tok å komprimere"""

        return self.kompTid

    def dekomprimer(self):
        """Dekomprimerer teksten"""

        fTalliste = self.TALLkomp.split(",")
        fOrdliste = self.ORDkomp.split(self.HEMSEP)

        fTalliste.pop(-1)
        fOrdliste.pop(-1)

        for ting in fTalliste:
            fTalliste[fTalliste.index(ting)]=int(ting)

        self.TALLukomp = fTalliste
        self.ORDukomp = fOrdliste

        for tall in self.TALLukomp:
            self.DekomString+=self.ORDukomp[int(tall)]

        self.dekomprimert = True
    
    def dekomprimertTekst(self):
        """Gir deg den dekomprimerte teksten"""

        return self.DekomString
    
    def dekompStatus(self):
        return self.dekomprimert
    
    def valider(self):
        """WORK IN PROGRESS"""

        orighash = hash(self.string)
        dekomphash = hash(self.DekomString)

        if orighash==dekomphash:
            return True
        else:
            return False





# setter opp tekst og default tekst
tekst=input("Skriv inn din tekst, [ENTER] for lang, 1 for kort:\t")
if tekst=="":
    tekst=Tekst(defaultTEKST)
    print(f"Bruker standardtekst: The European languages\nADVARSEL: LAAANG KOMPRIMERINGSTID",end="🗿")
elif tekst=="1":
    tekst=Tekst(defaultTEKST[0:2000])
    print(f"Bruker standardtekst: The European languages, kortversjon")


# om komprimert, om dekomprimert, om 


# arbeidsløkke
while True:
    print(f"{grønn}\n\nHva vil du gjøre? Skriv inn tallet tilsvarende funksjonen du vil bruke:\n")
    print(f"{rød}1. Print teksten\n2. Endre teksten\n3. Få størrelsen til teksten\n4. Få størrelsen til en fil\n5. Laste  tekst fra fil\n6. Laste  komprimert tekst fra fil\n7. Skrive tekst til fil\n\n8. Komprimere tekst")

    if tekst.kompStatus() == True:
        print(f"\n9. Print komprimert tekst\n10. Få størrelsen til den komprimerte teksten\n11. Skrive komprimert tekst til fil\n12. Få tiden det tok å komprimere teksten\n\n13. Dekomprimer tekst")

    if tekst.dekompStatus() == True:
        print(f"\n14. Print dekomprimert tekst\n15. Valider tekst")

    print(f"{gul}")
    tallin = input("\n\n")

    try:
        tallin = int(tallin)
    except ValueError:
        print("Skriv et tall!")
        continue
    
    print(f"{hvit}")

    match tallin:
        case 1: 
            print(f"Printer teksten:\n\n{tekst}")

        case 2:
            nytekst=str(input("\nSkriv inn ny tekst:\t"))
            print(f"Endrer teksten {tekst[0:1000]} til {nytekst}. Endre? [Y/N]:")
            if str.lower(input()) == "y":
                tekst.endreTekst(nytekst)
        
        case 3:
            print(f"Tekstens størrelse i minnet er {tekst.sizeTekst()} minnestørrelseenheter")
        
        case 4:
            filnavn = str(input("Skriv inn filnavn/lokasjon, klikk [ENTER] for default:\t"))
            if filnavn == "":
                filnavn = defaultTINN
            
            print(f"Filen {filnavn}s størrelse i minnet er {tekst.sizeFil(filnavn)} minnestørrelseenheter")
        
        case 5:
            print("Laster tekst fra fil")
            filnavn = str(input("Skriv inn filnavn/lokasjon, klikk [ENTER] for default:\t"))
            if filnavn == "":
                filnavn = defaultTINN

            tekst.lastTekst(filnavn) 
            print(f"Lastet teksten \n{tekst[0:150]}\nfra filen {filnavn}")

        case 6:
            print("Laster komprimert tekst fra fil")
            filnavn = str(input("Skriv inn filnavn/lokasjon, klikk [ENTER] for default:\t"))
            if filnavn == "":
                filnavn = defaultKINN                      

            tekst.lastKomp(filnavn)
            print(f"Lastet komprimert tekst fra filen {filnavn}")

        case 7:
            print("Skriver tekst til fil:")
            filnavn = str(input("Skriv inn filnavn/lokasjon, klikk [ENTER] for default:\t"))
            if filnavn == "":
                filnavn = defaultTUT
            
            tekst.skrivTekstTil(filnavn)
            print(f"Skrev tekst til filen {filnavn}")
        
        case 8:
            print("Komprimerer teksten")
            if tekst.sizeTekst() >= 5000:
                print("Komprimering kan ta litt tid")
            elif tekst.sizeTekst() >= 20000:
                print("Forbered deg på en stund med venting")
            elif tekst.sizeTekst() >= 40000:
                print("Rolige 3 minutter med komprimering i vente")
            
            tekst.komprimer()

            print("Komprimert!")
        
        case 9:
            print(tekst.kompTekst())
        
        case 10:
            print(f"Størrelse på originaltekst:\n{tekst.sizeTekst()} minnestørrelseenheter\n\nStørrelse på komprimert tekst:\n{tekst.sizeKomp()} minnestørrelseenheter\n\nKomprimering: {round(int(tekst.sizeKomp())/int(tekst.sizeTekst())*100,0)}%")
            if int(tekst.sizeKomp())/int(tekst.sizeTekst())*100 > 100:
                print(f"\nKomprimeringen økte altså størrelsen med {round(int(tekst.sizeKomp())/int(tekst.sizeTekst())*100-100,0)}%")
            else:
                print(f"\nKomprimeringen minket altså størrelsen med {round(100-int(tekst.sizeKomp())/int(tekst.sizeTekst())*100,0)}%")

        case 11:
            print("Skriver komprimert tekst til fil:")
            filnavn = str(input("Skriv inn filnavn/lokasjon, klikk [ENTER] for default:\t"))
            if filnavn == "":
                filnavn = defaultKUT
            
            tekst.skrivKompTil(filnavn)
            print(f"Skrev tekst til filen {filnavn}")
        
        case 12:
            print(f"Det tok {int(tekst.tidKomp())} nanosekunder å komprimere teksten\nDet vil si {int(tekst.tidKomp())/1000000} millisekunder")
        
        case 13:

            tekst.dekomprimer()
            print("Dekomprimert!")
        
        case 14:
            print(tekst.dekomprimertTekst())

        case 15:
            if tekst.valider()==True:
                print("Den originale teksten er identisk til den dekomprimerte teksten, og vi kan være sikker på at ingen informasjon er tapt!")
            else:
                print("Originalteksten og den dekomprimerte teksten er ikke like, og det har skjedd en feil")
            
            
    time.sleep(1)