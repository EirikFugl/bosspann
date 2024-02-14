import json
import matplotlib.pyplot as plt

# Definerer masse lister som jeg skal bruke for å lagre dataen fra json filen
ratinger = []
installasjoner = []
installasjonerPerKat = []
kategorier = []
forskjelligeKategorier = []
# Prøvde å fikse slik at jeg kunne lagre antall fra de forskjellige kategoriene her, men fikk det ikke til å fungere
antallKategori = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0] 
apper = []
topKategorier = []
topAntall = []


n = 0
# importerer filen
fil = r"REA3049_Karakter_4_PY1\REA3049_Karakter_4_PY\Elevsvar\googleplaystore.json"
# åppner filen
with open(fil, encoding="utf-8") as f:
    data = json.load(f)
    # skjekker at appen ikke fårekommer mer enn en gang, siden det fantes duplikater inni filen
    for i in data:
        if i["App"] not in apper:
            apper.append(i["App"])
# putter de forskjellige inn i kategorier uten duplikat av kategorier
            if i["Category"] not in forskjelligeKategorier:
                forskjelligeKategorier.append(i["Category"])
# lagrer alle kategoriene i en liste som jeg skal telle gjennom for å se hvor mange det er av hver
            kategorier.append(i["Category"])
# Forsøker å telle gjennom listen for å finne hvor mange det er av hver, fungerte dessverre ikke 
            for j in forskjelligeKategorier:
                for y in kategorier:
                    if j == y:
                        antallKategori[n] = antallKategori[n] + 1
# Printen her viser godt hva jeg ikke fikk grep på
                        print(antallKategori[n])
                n = n + 1
# Denne hadde klart å telle gjennom hvilke kategorier som de fleste appene tilhørte, men fikk dessverre ikke til
    for i in range(0,3):
# Brukte indeksen for å hente posisjonen til verdien og kategorien
        storst = max(antallKategori)
        indeksStorst = antallKategori.index(storst)
        topKategorier.append(forskjelligeKategorier[indeksStorst])
        topAntall.append(antallKategori[indeksStorst])
        del topAntall[indeksStorst]
        del topKategorier[indeksStorst]
print(topAntall)
print(topKategorier)
print(len(forskjelligeKategorier))            
            # if i["Rating"] == "NaN":
            #     ratinger.append(0)
            # else:
            #     ratinger.append(float(i["Rating"]))
           
            # Denne installsfunksjonen fungerte heller ikke dessverre, men prøvde å fjere de forskjellige bokstavene som ødela inten
            
           # installs = i["Installs"]
            
            # if len(installs) == 2:
            #     installasjoner.append(int(installs[0]))
            # elif len(installs) == 3:
            #     installasjoner.append(int(installs[0:2]))
            # elif len(installs) == 4:
            #     installasjoner.append(int(installs[0:3]))
            # elif len(installs) == 5:
            #     a = installs[0:3] + installs[4]
            #     installasjoner.append(int(a))
            # elif len(installs) == 6:
            #     a = installs[0:3] + installs[4:6]
            #     installasjoner.append(int(a))
            # elif len(installs) == 7:
            #     a = installs[0:3] + installs[4:7]
            #     installasjoner.append(int(a))
            # elif len(installs) == 8:
            #     a = installs[0:3] + installs[4:7] + installs[8]
            #     installasjoner.append(int(a))
            # elif len(installs) == 9:
            #     a = installs[0:3] + installs[4:7] + installs[8:10]
            #     installasjoner.append(int(a))
            # elif len(installs) == 10:
            #     a = installs[0:3] + installs[4:7] + installs[8:11]
            #     installasjoner.append(int(a))
            # elif len(installs) == 11:
            #     a = installs[0:3] + installs[4:7] + installs[8:11] + installs[12]
            #     installasjoner.append(int(a))
            # elif len(installs) == 12:
            #     a = installs[0:3] + installs[4:7] + installs[8:11] + installs[12:14]
            #     installasjoner.append(int(a))
            # elif len(installs) == 13:
            #     a = installs[0:3] + installs[4:7] + installs[8:11] + installs[12:15]
            #     installasjoner.append(int(a))


# plt.xlabel("Antall reviews (i 10 millioner)")
# plt.ylabel("Appnavn")
# plt.title("Informasjon over app-reviews")
# plt.barh(topp10ApperAntallReviewsNavn, topp10ApperAntallReviews)
# plt.show()







