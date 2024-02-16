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



stasjoner = {}
for stasjon in start:
    if stasjon not in stasjoner.keys():
        stasjoner[stasjon] = 1
    else:
        stasjoner[stasjon]+=1

stasjonerKopi = stasjoner
sortert = {}
usortert = True
while usortert:
    