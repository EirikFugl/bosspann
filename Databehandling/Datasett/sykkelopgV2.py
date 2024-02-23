import csv
import matplotlib.pyplot as plt

filnavn = r"Databehandling\Datasett\sykkelV2.csv"


                # Kolonne nr.
startTid = []   # 0
slutTid = []    # 1
tid = []        # 2
start = []      # 4
slutt = []      # 9

with open(filnavn, encoding = "utf-8-sig") as fil:
    filinnhold = csv.reader(fil,delimiter=",")

    kolonner = next(filinnhold)
    print(kolonner)
    


    for rad in filinnhold:
        startTid.append((rad[0]))
        slutTid.append((rad[1]))
        tid.append(int(rad[2]))
        start.append((rad[3]))
        slutt.append((rad[4]))

# start

stasjoner = {}
for stasjon in start:
    if stasjon not in stasjoner.keys():
        stasjoner[stasjon] = 1
    else:
        stasjoner[stasjon]+=1


stasjoner_sortert = {}


for i in range(len(stasjoner.keys())):
    lavest = stasjoner[list(stasjoner.keys())[0]]
    lavest_stasjonsnavn = list(stasjoner.keys())[0]
    for ting in stasjoner.keys():
        if stasjoner[ting] < lavest:
            lavest = stasjoner[ting]
            lavest_stasjonsnavn = ting
    stasjoner_sortert[lavest_stasjonsnavn] = lavest
    stasjoner.pop(lavest_stasjonsnavn)


print("\n\n")
print(stasjoner_sortert)

# stasjoner_slutt = {}
# for stasjon in slutt:
#     if stasjon not in stasjoner_slutt.keys():














stasjonsliste = list(stasjoner_sortert.keys())
verdiliste = list(stasjoner_sortert.values())


fig = plt.figure(figsize = (15,50))

plt.barh(stasjonsliste,verdiliste,color = "blue")

plt.savefig('sykkelSortert.png', bbox_inches='tight')

plt.close(fig)
# plt.show()