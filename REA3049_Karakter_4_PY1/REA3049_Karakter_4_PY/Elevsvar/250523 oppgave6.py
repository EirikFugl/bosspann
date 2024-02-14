print("Skriv inn poengsummen din:")
poengsum = float(input(""))

if poengsum < 50 and poengsum >= 0:
    print("Ikke bestått")
elif poengsum <= 69 and poengsum >= 50:
    print("Bestått")
elif poengsum <= 89 and poengsum >= 70:
    print("Godt bestått")
elif poengsum <= 100 and poengsum >= 90:
    print("Meget godt bestått")
else:
    print("Ikke gyldig poengsum!")