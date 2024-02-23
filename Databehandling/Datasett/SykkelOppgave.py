import csv
import matplotlib.pyplot as plt
import os

filnavn = r"Databehandling\Datasett\sykkel.csv"
nyfil = r"Databehandling\Datasett\sykkelV2.csv"

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
    
    kolonner = [kolonner[0],kolonner[1],kolonner[2],kolonner[4],kolonner[9]]
    print(kolonner)

    for rad in filinnhold:
        startTid.append((rad[0][:-13]))
        slutTid.append((rad[1][:-13]))
        tid.append(int(rad[2]))
        start.append((rad[4]))
        slutt.append((rad[9]))


midRader = []
rader = []
for i in range(len(startTid)):
    midRader = [startTid[(i-1)],slutTid[(i-1)],tid[(i-1)],start[(i-1)],slutt[(i-1)]]
    rader.append(midRader)


with open(nyfil,"w", encoding="utf-8-sig",newline="") as fil:
    writer = csv.writer(fil)

    writer.writerow(kolonner)

    writer.writerows(rader)

print(f"\n\n\n{kolonner[0]}\t\t{kolonner[1]}\t\t{kolonner[2]}  {kolonner[3]}\t\t\t{kolonner[4]}")


antall_bits = 3
def normaliserTekst(tekst):
    if len(str(tekst)) > antall_bits*8:
        while len(str(tekst)) > antall_bits*8:
            tekst = tekst[:-1]
    
    if len(str(tekst))< 24:
        while len(str((tekst))) < antall_bits*8:
            tekst = str(tekst) + " "

    return tekst




# plt.hist(tid,range=(0,3600),bins=101)
plt.show()

# for i in range(len(startTid)):
#     print(f"{normaliserTekst(startTid[i-1])}\t{normaliserTekst(slutTid[i-1])}\t{normaliserTekst(tid[i-1])}\t{normaliserTekst(start[i-1])}\t\t\t{normaliserTekst(slutt[i-1])}")