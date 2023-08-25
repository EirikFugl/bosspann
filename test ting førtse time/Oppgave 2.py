import random
a=int(input("Skriv inn et tall mellom 1 og 10:\t2"))
b=random.randint(0,10)
if (a<b):
    print("Lol taper du gjettet for lavt, det tilfeldige tallet var",b)
elif (a>b):
    print("Lol taper du gjettet for høyt, det tilfeldige tallet var",b)
else:
    print("wow du gjettet riktig")