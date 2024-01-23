ukomp="The European languages are members of the same family. Their separate existence is a myth. For science, music, sport, etc, Europe uses the same vocabulary. The languages only differ in their grammar, their pronunciation and their most common words. Everyone realizes why a new common language would be desirable: one could refuse to pay expensive translators. To achieve this, it would be necessary to have uniform grammar, pronunciation and more common words. If several languages coalesce, the grammar of the resulting language is more simple and regular than that of the individual languages. The new common language will be more simple and regular than the existing European languages. It will be as simple as Occidental; in fact, it will be Occidental. To an English person, it will seem like simplified English, as a skeptical Cambridge friend of mine told me what Occidental is.The European languages are members of the same family. Their separate existence is a myth. For science, music, sport, etc, Europe uses the same vocabulary. The languages only differ in their grammar, their pronunciation and their most common words. Everyone realizes why a new common language would be desirable: one could refuse to pay expensive translators."

lengde=0
start=0
endelig=[]


seps = [" ",".",",",":",";"]

#hvert ord separert av '.', ',', ' ', etc. skal ligge i en liste, og ha en annen liste med indeksene deres

for bokstav in ukomp:

    if bokstav in seps:
        endelig.append(ukomp[start:(start+lengde)])
        endelig.append(bokstav)


        start+=lengde+1
        lengde=0
    
    else:
        lengde+=1


    ordliste = []
    talliste = []

    for ord_eller_separator in endelig:
        if ord_eller_separator not in ordliste:
            ordliste.append(ord_eller_separator)
            talliste.append(ordliste.index(ord_eller_separator))
        else:
            talliste.append(ordliste.index(ord_eller_separator))
            pass

print(f"UNIKE ORD LISTE:\n{ordliste}\n\nTALLISTE:\n{talliste}\n\n\n")



HEMMELIGSEPARATOR="#1?=;`|"

# GJØR TALL TIL TEKST STRING

tString=''
for item in talliste:
    tString+=str(item)
    tString+=","

print("tString\n",tString,"\n\n\n")


# GJØR TEKST TIL TEKST STRING

oString=''
for item in ordliste:
    oString+=str(item)
    oString+=HEMMELIGSEPARATOR

print(oString)

# GJØR TALL TIL LISTE IGJEN

fTallliste=tString.split(",")

fTallliste.pop(-1)

for ting in fTallliste:
    fTallliste[fTallliste.index(ting)]=int(ting)

print("fTalliste\n",fTallliste)


# GJØR TEKST TIL LISTE IGJEN

fOrdliste=oString.split(HEMMELIGSEPARATOR)

fOrdliste.pop(-1)
print("fOrdliste\n",fOrdliste)


# PRINTER ORD

print("Print ord")
for tall in fTallliste:
    print(fOrdliste[int(tall)],end="")

