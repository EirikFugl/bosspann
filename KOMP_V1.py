import time                         #gir deg litt ventetid her og der
from colorama import Fore           # gir deg farger
import os                           # clearer terminalen
os.system('cls')


defaultTINN=r"TekstINN.txt"
defaultTUT=r"TekstUT.txt"
defaultINN=r"KompINN.sjef"
defaultUT=r"KompUT.sjef"

# DISCLAIMER DETTE PROGRAMMET SUGER OG KOMPRIMERINGEN FUNKER IKKE

# LAG UML TING VIKTIGVIKTIG

###############################################################################

# FIVE STEPS TO GREATNESS:

# 1. FIKSE DEKOMPRIMERING (Skrive over fra ny algoritme.py) DONE SÅNN CIRKA ISH EGENTLIG
# 2. FIKSE FILSYSTEM (.SJEF (Super Jalla Eirik Fil) fil) SJEF FUNKER, FIKS RESTEN AV LASTING
# 3. RYDDE OPP FUNKSJONER (standardisere og fikse return istedenfor det dritet som er nå)
#    Gjøre inputs og print i match case steget, ikke i selve funksjonen
# 4. GJØRE SÅNN AT MATCH CASE MULIGHETER DUKKER OPP ETTERHVERT SOM TING BLIR MULIG
#    Ingen "du må gjøre x før y", men at du kan ikke gjøre x før y er gjort

# 5. Fikse lasting av komprimerte ting

############################################## OPPDATERING

# 6. Sjekk om HASH av self.string er lik dekomprimert

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

    def filsturrels(self,filnavn):
        
        filnavn=defaultTUT
        print(os.path.getsize(filnavn))

        filnavn=defaultUT
        print(os.path.getsize(filnavn))
        


    def lastTekst(self,filnavn):

        with open(filnavn,"r") as f:
            self.string=f.read()
        

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
        with open(filnavn,"w") as f:
            pass


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
        global brababa
        brababa=time.time()
        

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
        
        global datata
        datata=time.time()


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
            skrivkomptingtil=defaultUT
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
    tekst=Tekst("""The European languages are members of the same family. Their separate existence is a myth. For science, music, sport, etc, Europe uses the same vocabulary. The languages only differ in their grammar, their pronunciation and their most common words. Everyone realizes why a new common language would be desirable: one could refuse to pay expensive translators. To achieve this, it would be necessary to have uniform grammar, pronunciation and more common words. If several languages coalesce, the grammar of the resulting language is more simple and regular than that of the individual languages. The new common language will be more simple and regular than the existing European languages. It will be as simple as Occidental; in fact, it will be Occidental. To an English person, it will seem like simplified English, as a skeptical Cambridge friend of mine told me what Occidental is.The European languages are members of the same family. Their separate existence is a myth. For science, music, sport, etc, Europe uses the same vocabulary. The languages only differ in their grammar, their pronunciation and their most common words. Everyone realizes why a new common language would be desirable: one could refuse to pay expensive translators. The Gulf War was an armed conflict between Iraq and a 42-country coalition led by the United States. The coalition's efforts against Iraq were carried out in two key phases: Operation Desert Shield, which marked the military buildup from August 1990 to January 1991; and Operation Desert Storm, which began with the aerial bombing campaign against Iraq on 17 January 1991 and came to a close with the American-led Liberation of Kuwait on 28 February 1991. On 2 August 1990, Iraq invaded neighboring Kuwait, and had fully occupied the country within two days. Initially, Iraq ran the occupied territory under a puppet government known as the "Republic of Kuwait" before proceeding with an outright annexation in which Kuwaiti sovereign territory was split, with the "Saddamiyat al-Mitla' District" being carved out of the country's northern portion and the "Kuwait Governorate" covering the rest. Varying speculations have been made regarding the true intents behind the Iraqi invasion, most notably including Iraq's inability to repay the debt of more than US$14 billion that it had borrowed from Kuwait to finance its military efforts during the Iran–Iraq War. Kuwait's demands for repayment were coupled with its surge in petroleum production levels, which kept revenues down for Iraq and further weakened its economic prospects; throughout much of the 1980s, Kuwait's oil production was above its mandatory quota under OPEC, which kept international oil prices down. Iraq interpreted the Kuwaiti refusal to decrease oil production as an act of aggression towards the Iraqi economy, leading up to the hostilities. The invasion of Kuwait was immediately met with international condemnation, including in Resolution 660 by the United Nations Security Council (UNSC), which unanimously imposed economic sanctions against Iraq in Resolution 661. British prime minister Margaret Thatcher and American president George H. W. Bush deployed troops and equipment into Saudi Arabia and openly urged other countries to send their own forces to the scene. In response to the joint call, an array of countries joined the American-led coalition, forming the largest military alliance since World War II. The bulk of the coalition's military power was from the United States, with Saudi Arabia, the United Kingdom, and Egypt as the largest lead-up contributors, in that order; Saudi Arabia and the Kuwaiti government-in-exile paid around US$32 billion of the US$60 billion cost to mobilize the coalition against Iraq. UNSC Resolution 678 adopted on 29 November 1990 offered Iraq one final chance until 15 January 1991 to implement Resolution 660 and withdraw from Kuwait; it further empowered states after the deadline to use "all necessary means" to force Iraq out of Kuwait. Initial efforts to dislodge the Iraqi presence in Kuwait began with an aerial and naval bombardment on 17 January 1991, which continued for five weeks. During this time, as the Iraqi military found itself unable to ward off the coalition's attacks, Iraq began to fire missiles at Israel. While the coalition itself did not include Israel, the Iraqi leadership had launched the campaign under the expectation that the missile barrage would provoke an independent Israeli military response, and hoped that such a response would prompt the coalition's Muslim-majority countries to withdraw (see Arab–Israeli conflict). However, the jeopardization attempt was ultimately unsuccessful as Israel did not respond to any Iraqi attacks, and Iraq continued to remain at odds with most Muslim-majority countries. Iraqi missile barrages aimed at coalition targets stationed in Saudi Arabia were also largely unsuccessful, and on 24 February 1991, the coalition launched a major ground assault into Iraqi-occupied Kuwait. The offensive was a decisive victory for American-led coalition forces, who liberated Kuwait and promptly began to advance past the Iraq–Kuwait border into Iraqi territory. A hundred hours after the beginning of the ground campaign, the coalition ceased its advance into Iraq and declared a ceasefire. Aerial and ground combat was confined to Iraq, Kuwait, and areas straddling the Iraq–Saudi Arabia border. The conflict marked the introduction of live news broadcasts from the front lines of the battle, principally by the American network CNN. It has also earned the nickname Video Game War, after the daily broadcast of images from cameras onboard American bombers during Operation Desert Storm. The Gulf War has gained notoriety for including three of the largest tank battles in American military history. The Gulf War was an armed conflict between Iraq and a 42-country coalition led by the United States. The coalition's efforts against Iraq were carried out in two key phases: Operation Desert Shield, which marked the military buildup from August 1990 to January 1991; and Operation Desert Storm, which began with the aerial bombing campaign against Iraq on 17 January 1991 and came to a close with the American-led Liberation of Kuwait on 28 February 1991. On 2 August 1990, Iraq invaded neighboring Kuwait, and had fully occupied the country within two days. Initially, Iraq ran the occupied territory under a puppet government known as the "Republic of Kuwait" before proceeding with an outright annexation in which Kuwaiti sovereign territory was split, with the "Saddamiyat al-Mitla' District" being carved out of the country's northern portion and the "Kuwait Governorate" covering the rest. Varying speculations have been made regarding the true intents behind the Iraqi invasion, most notably including Iraq's inability to repay the debt of more than US$14 billion that it had borrowed from Kuwait to finance its military efforts during the Iran–Iraq War. Kuwait's demands for repayment were coupled with its surge in petroleum production levels, which kept revenues down for Iraq and further weakened its economic prospects; throughout much of the 1980s, Kuwait's oil production was above its mandatory quota under OPEC, which kept international oil prices down. Iraq interpreted the Kuwaiti refusal to decrease oil production as an act of aggression towards the Iraqi economy, leading up to the hostilities. The invasion of Kuwait was immediately met with international condemnation, including in Resolution 660 by the United Nations Security Council (UNSC), which unanimously imposed economic sanctions against Iraq in Resolution 661. British prime minister Margaret Thatcher and American president George H. W. Bush deployed troops and equipment into Saudi Arabia and openly urged other countries to send their own forces to the scene. In response to the joint call, an array of countries joined the American-led coalition, forming the largest military alliance since World War II. The bulk of the coalition's military power was from the United States, with Saudi Arabia, the United Kingdom, and Egypt as the largest lead-up contributors, in that order; Saudi Arabia and the Kuwaiti government-in-exile paid around US$32 billion of the US$60 billion cost to mobilize the coalition against Iraq. UNSC Resolution 678 adopted on 29 November 1990 offered Iraq one final chance until 15 January 1991 to implement Resolution 660 and withdraw from Kuwait; it further empowered states after the deadline to use "all necessary means" to force Iraq out of Kuwait. Initial efforts to dislodge the Iraqi presence in Kuwait began with an aerial and naval bombardment on 17 January 1991, which continued for five weeks. During this time, as the Iraqi military found itself unable to ward off the coalition's attacks, Iraq began to fire missiles at Israel. While the coalition itself did not include Israel, the Iraqi leadership had launched the campaign under the expectation that the missile barrage would provoke an independent Israeli military response, and hoped that such a response would prompt the coalition's Muslim-majority countries to withdraw (see Arab–Israeli conflict). However, the jeopardization attempt was ultimately unsuccessful as Israel did not respond to any Iraqi attacks, and Iraq continued to remain at odds with most Muslim-majority countries. Iraqi missile barrages aimed at coalition targets stationed in Saudi Arabia were also largely unsuccessful, and on 24 February 1991, the coalition launched a major ground assault into Iraqi-occupied Kuwait. The offensive was a decisive victory for American-led coalition forces, who liberated Kuwait and promptly began to advance past the Iraq–Kuwait border into Iraqi territory. A hundred hours after the beginning of the ground campaign, the coalition ceased its advance into Iraq and declared a ceasefire. Aerial and ground combat was confined to Iraq, Kuwait, and areas straddling the Iraq–Saudi Arabia border. The conflict marked the introduction of live news broadcasts from the front lines of the battle, principally by the American network CNN. It has also earned the nickname Video Game War, after the daily broadcast of images from cameras onboard American bombers during Operation Desert Storm. The Gulf War has gained notoriety for including three of the largest tank battles in American military history. Throughout the Cold War, Iraq had been an ally of the Soviet Union, and there was a history of friction between Iraq and the United States.[32] The US was concerned with Iraq's position on Israeli–Palestinian politics. The US also disliked Iraqi support for Palestinian militant groups, which led to Iraq's inclusion on the developing US list of State Sponsors of Terrorism in December 1979.[33] The US remained officially neutral after Iraq's invasion of Iran in 1980, which became the Iran–Iraq War, although it provided resources, political support, and some "non-military" aircraft to Iraq.[34] In March 1982, Iran began a successful counteroffensive (Operation Undeniable Victory), and the US increased its support for Iraq to prevent Iran from forcing a surrender. In a US bid to open full diplomatic relations with Iraq, the country was removed from the US list of State Sponsors of Terrorism.[35] Ostensibly, this was because of improvement in the regime's record, although former US Assistant Defense Secretary Noel Koch later stated: "No one had any doubts about [the Iraqis'] continued involvement in terrorism ... The real reason was to help them succeed in the war against Iran."[36][37] With Iraq's newfound success in the war, and the Iranian rebuff of a peace offer in July, arms sales to Iraq reached a record spike in 1982. When Iraqi President Saddam Hussein expelled Abu Nidal to Syria at the US's request in November 1983, the Reagan administration sent Donald Rumsfeld to meet Saddam as a special envoy and to cultivate ties. By the time the ceasefire with Iran was signed in August 1988, Iraq was heavily debt-ridden and tensions within society were rising.[38] Most of its debt was owed to Saudi Arabia and Kuwait.[39] Iraq's debts to Kuwait amounted to $14 billion.[40] Iraq pressured both nations to forgive the debts, but they refused.[39][41]
Donald Rumsfeld, US special envoy to the Middle East, meets Saddam Hussein on 19–20 December 1983. The Iraq–Kuwait border dispute involved Iraqi claims to Kuwaiti territory.[34] Kuwait had been a part of the Ottoman Empire's province of Basra, something that Iraq claimed made Kuwait rightful Iraqi territory.[42] Kuwait's ruling dynasty, the al-Sabah family, had concluded a protectorate agreement in 1899 that assigned responsibility for Kuwait's foreign affairs to the United Kingdom. The UK drew the border between Kuwait and Iraq in 1922, making Iraq almost entirely landlocked.[34] Kuwait rejected Iraqi attempts to secure further provisions in the region.[42] Iraq also accused Kuwait of exceeding its OPEC quotas for oil production.[43] In order for the cartel to maintain its desired price of $18 per barrel, discipline was required. The United Arab Emirates and Kuwait were consistently overproducing; the latter at least in part to repair losses caused by Iranian attacks in the Iran–Iraq War and to pay for the losses of an economic scandal. The result was a slump in the oil price – as low as $10 per barrel ($63/m3) – with a resulting loss of $7 billion a year to Iraq, equal to its 1989 balance of payments deficit.[44] Resulting revenues struggled to support the government's basic costs, let alone repair Iraq's damaged infrastructure. Jordan and Iraq both looked for more discipline, with little success.[45] The Iraqi government described it as a form of economic warfare,[45] which it claimed was aggravated by Kuwait slant-drilling across the border into Iraq's Rumaila oil field.[46] According to oil workers in the area, Iraq's slant drilling claim was fabricated, as "oil flows easily from the Rumaila field without any need for these techniques."[47] At the same time, Saddam looked for closer ties with those Arab states that had supported Iraq in the war. This move was supported by the US, who believed that Iraqi ties with pro-Western Gulf states would help bring and maintain Iraq inside the US' sphere of influence.[48] In 1989, it appeared that Saudi–Iraqi relations, strong during the war, would be maintained. A pact of non-interference and non-aggression was signed between the countries, followed by a Kuwaiti-Iraqi deal for Iraq to supply Kuwait with water for drinking and irrigation, although a request for Kuwait to lease Iraq Umm Qasr was rejected.[48] Saudi-backed development projects were hampered by Iraq's large debts, even with the demobilization of 200,000 soldiers. Iraq also looked to increase arms production so as to become an exporter, although the success of these projects was also restrained by Iraq's obligations; in Iraq, resentment to OPEC's controls mounted.[49] Iraq's relations with its Arab neighbors, particularly Egypt, were degraded by mounting violence in Iraq against expatriate groups, who were well-employed during the war, by unemployed Iraqis, among them demobilized soldiers. These events drew little notice outside the Arab world because of fast-moving events directly related to the fall of Communism in Eastern Europe. However, the US did begin to condemn Iraq's human rights record, including the well-known use of torture.[50] The UK also condemned the execution of Farzad Bazoft, a journalist working for the British newspaper The Observer.[34] Following Saddam's declaration that "binary chemical weapons" would be used on Israel if it used military force against Iraq, Washington halted part of its funding.[51] A UN mission to the Israeli-occupied territories, where riots had resulted in Palestinian deaths, was vetoed by the US, making Iraq deeply skeptical of US foreign policy aims in the region, combined with the reliance of the US on Middle Eastern energy reserves.[52] In early July 1990, Iraq complained about Kuwait's behavior, such as not respecting their quota, and openly threatened to take military action. On the 23rd, the CIA reported that Iraq had moved 30,000 troops to the Iraq-Kuwait border, and the US naval fleet in the Persian Gulf was placed on alert. Saddam believed an anti-Iraq conspiracy was developing – Kuwait had begun talks with Iran, and Iraq's rival Syria had arranged a visit to Egypt.[53] On 15 July 1990, Saddam's government laid out its combined objections to the Arab League, including that policy moves were costing Iraq $1 billion a year, that Kuwait was still using the Rumaila oil field, and that loans made by the UAE and Kuwait could not be considered debts to its "Arab brothers".[53] He threatened force against Kuwait and the UAE, saying: "The policies of some Arab rulers are American ... They are inspired by America to undermine Arab interests and security."[54] The US sent aerial refuelling planes and combat ships to the Persian Gulf in response to these threats.[55] Discussions in Jeddah, Saudi Arabia, mediated on the Arab League's behalf by Egyptian President Hosni Mubarak, were held on 31 July and led Mubarak to believe that a peaceful course could be established.[56] It was revealed during Saddam Hussein's 2003–2004 interrogation following his capture that in addition to economic disputes, an insulting exchange between the Kuwaiti emir Al Sabah and the Iraqi foreign minister – during which Saddam claimed that the emir stated his intention to turn "every Iraqi woman into a $10 prostitute" by bankrupting the country – was a decisive factor in triggering the Iraqi invasion.[57] On the 25th, Saddam met with April Glaspie, the US Ambassador to Iraq, in Baghdad. The Iraqi leader attacked American policy with regards to Kuwait and the UAE: So what can it mean when America says it will now protect its friends? It can only mean prejudice against Iraq. This stance plus maneuvers and statements which have been made has encouraged the UAE and Kuwait to disregard Iraqi rights ... If you use pressure, we will deploy pressure and force. We know that you can harm us although we do not threaten you. But we too can harm you. Everyone can cause harm according to their ability and their size. We cannot come all the way to you in the United States, but individual Arabs may reach you ... We do not place America among the enemies. We place it where we want our friends to be and we try to be friends. But repeated American statements last year made it apparent that America did not regard us as friends.[58] Glaspie replied: I know you need funds. We understand that and our opinion is that you should have the opportunity to rebuild your country. But we have no opinion on the Arab-Arab conflicts, like your border disagreement with Kuwait ... Frankly, we can only see that you have deployed massive troops in the south. Normally that would not be any of our business. But when this happens in the context of what you said on your national day, then when we read the details in the two letters of the Foreign Minister, then when we see the Iraqi point of view that the measures taken by the UAE and Kuwait is, in the final analysis, parallel to military aggression against Iraq, then it would be reasonable for me to be concerned.[58] Saddam stated that he would attempt last-ditch negotiations with the Kuwaitis but Iraq "would not accept death."[58] According to Glaspie's own account, she stated in reference to the precise border between Kuwait and Iraq, "... that she had served in Kuwait 20 years before; 'then, as now, we took no position on these Arab affairs'."[citation needed] Glaspie similarly believed that war was not imminent.[56] On 26 July 1990, only a few days before the Iraqi invasion, OPEC officials said that Kuwait and the United Arab Emirates had agreed to a proposal to limit their oil output to 1.5 million barrels (240,000 m3) per day, "down from the nearly 2 million barrels a day they had each been pumping," thus potentially settling differences over oil policy between Kuwait and Iraq.[59] """)
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

            skrivteksttilting=input(f"Skriv inn filnavn [ENTER] for default ({defaultTUT}):\t")
            if skrivteksttilting=="":
                skrivteksttilting=defaultTUT
            tekst.skrivTekstTil(skrivteksttilting)
            print(f"Ferdig! Skrev til {skrivteksttilting}")
        
        case 6:                                         # Skriver komprimert tekst til en fil
            
            skrivkomptingtil=input(f"Skriv inn filnavn [ENTER] for default ({defaultUT}):\t")
            if skrivkomptingtil=="":
                skrivkomptingtil=defaultUT
            tekst.skrivKompTil(skrivkomptingtil)
            print(f"Ferdig! Skrev til {skrivkomptingtil}")
        
        case 7: 
            
            tekst.komprimer()
            print(f"\nKomprimert!, det tok {datata-brababa} sekunder")

        
        case 8: 
            
            abab=input("Skriv inn filnavn [ENTER] for default ({defaultUT}):\t")
            if abab=="":
                abab=defaultUT
            tekst.filKomp(abab)
        
        case 9: 
            tekst.dekomprimer()

        case 10:
            tekst.printDekomp()

        case 11:

            tekst.zimbabwe()

        case 12:

            abhaha=defaultINN
            tekst.lastKomp((abhaha))
        
        case 13:

            tekst.filsturrels(123)


    time.sleep(1)