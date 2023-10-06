
tallListe = []
spesialnummer = 7
listelengde = 100

for i in range(listelengde):
    tallListe.append(i+1)

print(f"listen har {len(tallListe)} elementer.")

def funksjon(liste,tall):
    liste3=[]
    for i in liste:
        a=tall*i
        if a<=len(liste):
            liste3.append(a)
    return liste3

print(f"Startar søket etter tall delbare med {spesialnummer}:\n{funksjon(tallListe,spesialnummer)}")