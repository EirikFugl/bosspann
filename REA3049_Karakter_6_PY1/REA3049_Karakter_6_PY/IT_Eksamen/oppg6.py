p=int(input("Skriv inn poengsummen din: "))
if p>=0 and p<50:
    print("Ikke bestått")
elif p>=50 and p<=69:
    print("Bestått")
elif p>=70 and p<=89:
    print("Godt bestått")
elif p>=90 and p<=100:
    print("Meget godt bestått")
else: print("Ikke gyldig poengsum!")