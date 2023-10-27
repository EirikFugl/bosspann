liste=["1","2","3","4","5"]

def endreListe(nmr,endring):
    liste[nmr]=endring

print(liste)

while True:
    endreListe((int(input("\nSkriv inn hvilken indeks du vil ha endret:\t\t")))-1,(input("\nSkriv inn det nye som skal stå der:\t\t")))
    print(f"\nEndret liste: {liste}\n\n")