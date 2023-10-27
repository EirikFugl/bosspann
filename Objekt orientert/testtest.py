import string

tekst="The European languages are members of the same family. Their separate existence is a myth. For science, music, sport, etc, Europe uses the same vocabulary. The languages only differ in their grammar, their pronunciation and their most common words. Everyone realizes why a new common language would be desirable: one could refuse to pay expensive translators. To achieve this, it would be necessary to have uniform grammar, pronunciation and more common words. If several languages coalesce, the grammar of the resulting language is more simple and regular than that of the individual languages. The new common language will be more simple and regular than the existing European languages. It will be as simple as Occidental; in fact, it will be Occidental. To an English person, it will seem like simplified English, as a skeptical Cambridge friend of mine told me what Occidental is. The European languages are members of the same family. Their separate existence is a myth. For science, music, sport, etc, Europe uses the same vocabulary. The languages only differ in their grammar, their pronunciation and their most common words. Everyone realizes why a new common language would be desirable: one could refuse to pay expensive translators."

print(len(tekst))

splitlist = [word.strip(string.punctuation) for word in tekst.split()]
ordliste=[]

for ting in splitlist:
    if ting not in ordliste:
        ordliste.append(ting)


endelig=[]
start=0
lengde=0
mellomrom = " "
punktum = "."
komma = ","

for bokstav in tekst:

    if bokstav == mellomrom:
        #print(tekst[start:(start+lengde)],start,lengde)
        endelig.append(tekst[start:(start+lengde)])
        endelig.append(mellomrom)
        start+=lengde+1
        lengde=0

    elif bokstav == punktum:
        #print(tekst[start:(start+lengde)])
        endelig.append(tekst[start:(start+lengde)])
        endelig.append(punktum)
        start+=lengde+1
        lengde=0

    elif bokstav == komma:
        #print(tekst[start:(start+lengde)])
        endelig.append(tekst[start:(start+lengde)])
        endelig.append(komma)
        start+=lengde+1
        lengde=0
    
    else:
        lengde+=1

for ord in endelig:
    print(ord,end="")

for ord in endelig:
    if ord in ordliste:
        endelig[endelig.index(ord)]=endelig.index(ord)

for ord in endelig:
    print(ord,end="")


endelig2 = endelig
ordliste2 = ordliste
ferdig=[]

for indeks in endelig2:
    try:
        ferdig.append(ordliste2[int(indeks)+1])
    except ValueError:
        ferdig.append(indeks)
    except IndexError:
        print(indeks)

print(ferdig)