# regn ut alkohol
pris=float(eval(input("Skriv inn pris:\t\t")))
mengde=float(eval(input("Skriv inn mengde i cl:\t\t")))
abv=float(eval(input("Skriv inn alkoholprosent/ABV (kun tallet):\t\t")))

alk=mengde*abv/100
ppe=pris/(mengde*(abv/100))

print(f"Denne alkohol tingen koster {round(ppe,2)} per cl ren alkohol")
print(f"Det tilsvarer rundt {round(alk/2.35)} bokser øl")