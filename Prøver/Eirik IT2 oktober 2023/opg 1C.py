import time

fødselsnummer =  input("Vennligst skriv inn ditt fødselsnummer:\t")

if len(fødselsnummer)<11:
    print("Avslutter...")
    exit()

fødselsdato = fødselsnummer[0:6]

if fødselsnummer[0:1] == "0":
    fødselsdag = fødselsnummer[1:2]
else:
    fødselsdag = fødselsnummer[0:2]

'''
#måned versjon 1
måned = int(fødselsnummer[2:4])
print(måned, "hø")

if måned==1:
    måned=". januar"
elif måned==2:
    måned=". februar"
elif måned==3:
    måned=". mars"
elif måned==4:
    måned=". april"
elif måned==5:
    måned=". mai"
elif måned==6:
    måned=". juni"
elif måned==7:
    måned=". juli"
elif måned==8:
    måned=". august"
elif måned==9:
    måned=". september"
elif måned==10:
    måned=". oktober"
elif måned==11:
    måned=". november"
elif måned==12:
    måned=". desember"
'''

# måned versjon 2

måneder = [". januar", ". februar",". mars",". april",". mai",". juni",". juli",". august",". september",". oktober",". november",". desember"]

for månedr in måneder:
    if int(fødselsnummer[2:4]) == måneder.index(månedr)+1:
        måned = månedr

lokalTid = time.localtime()
(årstall, *tuppel2) = lokalTid


# år
if int(fødselsnummer[4:6])>int(str(årstall)[2:4]):
    år="19"+fødselsnummer[4:6]
else:
    år="20"+fødselsnummer[4:6]


# kjønn
if int(fødselsnummer[8:9])%2 == 0:
    kjønn="kvinne"
else:
    kjønn="mann"


print(f"Din fødselsdag er: {fødselsdato[0:2]}.{fødselsdato[2:4]}.{fødselsdato[4:6]}")

# bedre utskrift


print(f"Fødselsdatoen er {fødselsdag}{måned} {år} ({kjønn})")