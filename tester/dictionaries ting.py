#Dictionaries i Python er en datastruktur som lar deg lagre og hente data ved hjelp av nøkler. Hver verdi i en dictionary er tilknyttet en unik nøkkel, og dette gjør det enkelt å organisere og hente data. La oss se på hvordan du bruker dictionaries med noen enkle eksempler:

### Opprette en dictionary:
#Du kan opprette en dictionary ved å bruke krøllparenteser `{}` og definere nøkler og tilhørende verdier, separert med kolon `:`. Her er et eksempel:

person = {
    "navn": "Ola Nordmann",
    "alder": 30,
    "jobb": "Ingeniør"
}

### Hente verdier fra en dictionary:
#Du kan hente verdier ved å bruke nøkkelen som indeks:

print(person["navn"])  # Gir: "Ola Nordmann"
print(person["alder"]) # Gir: 30


### Legge til og endre verdier i en dictionary:
#Du kan legge til nye nøkkel-verdi-par eller endre eksisterende verdier:

person["adresse"] = "Oslo"
person["alder"] = 31

### Sjekke om en nøkkel eksisterer i dictionary:
#Du kan sjekke om en nøkkel eksisterer ved å bruke `in`-operatoren:

if "jobb" in person:
    print("Jobb:", person["jobb"])
else:
    print("Jobb ikke funnet")

### Fjerne nøkkel-verdi-par fra en dictionary:
#Du kan fjerne nøkkel-verdi-par ved å bruke `del`-kommandoen:

del person["jobb"]

### Iterere gjennom en dictionary:
#Du kan iterere gjennom nøkkel-verdi-parene i en dictionary ved hjelp av en `for`-løkke:

for nøkkel, verdi in person.items():
    print(nøkkel + ":", verdi)

#Dette er noen grunnleggende operasjoner du kan utføre med dictionaries i Python. Dictionaries er nyttige når du trenger å lagre data som er assosiert med en nøkkel, for eksempel når du oppretter kart over data.