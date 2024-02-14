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


print(f"\n\n\n{kolonner[0]}\t\t{kolonner[1]}\t\t{kolonner[2]}  {kolonner[3]}\t\t\t{kolonner[4]}")

def normaliserTekst(tekst):
    if len(str(tekst)) > 24:
        while len(str(tekst)) > 24:
            tekst = tekst[:-1]
    
    if len(str(tekst))< 24:
        while len(str((tekst))) < 24:
            tekst = str(tekst) + " "

    return tekst








for i in range(len(startTid)):
    a=input()
    print(f"{normaliserTekst(startTid[i-1])}\t{normaliserTekst(slutTid[i-1])}\t{normaliserTekst(tid[i-1])}\t{normaliserTekst(start[i-1])}\t\t\t{normaliserTekst(slutt[i-1])}")