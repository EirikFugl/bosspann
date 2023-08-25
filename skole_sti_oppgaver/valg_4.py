poeng=int(input("skriv inn poengsummen din:\t"))
if poeng>0 and poeng<100:
    if poeng>90:
        print("karakter 6")
    elif poeng>80:
        print("karakter 5")
    elif poeng>60:
        print("karakter 4")
    elif poeng>40:
        print("karakter 3")
    elif poeng>20:
        print("karakter 2")
    else:
        print("karakter 1")
else:
    print("din snik skriv noe riktig")