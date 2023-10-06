varer = {
    "Asus Zenbook GH215": 
        {"varenavn": "Asus laptop",
         "pris": 9999,
         "varelager": 10,
         "produktinfo": "En bærbar PC med 15.6 tommer skjerm, 8 GB RAM og 256 GB SSD",
         "tekniske egenskaper": 
            {"prosessor": "Intel Core i5-1135G7",
             "grafikkort": "Intel Iris Xe Graphics",
             "batterikapasitet": "Opptil 8 timer",
             "vekt": 1.8},
         "farger": ["blå","svart","grå"]
         },
    
    "Samsung Galaxy S22 GH67": 
        {"varenavn": "Samsung mobiltelefon",
         "pris": 6999,
         "varelager": 20,
         "produktinfo": "En smarttelefon med 6.7 tommer skjerm, 128 GB lagring og 12 MP kamera ",
         "tekniske egenskaper": 
            {"prosessor": "Qualcomm Snapdragon 888",
             "grafikkort": "Adreno 660",
             "batterikapasitet": "4500 mAh",
             "vekt": 0.2},
         "farger": ["svart", "hvit", "grønn"],
         },
    "Apple Airpods Pro Gen 3 (2023)":
        {"varenavn": "trådløse hodetelefoner",
         "pris": 2499,
         "varelager": 30,
         "produktinfo": "Trådløse hodetelefoner med aktiv støydemping",
         "tekniske egenskaper": 
            {"batterikapasitet": "Opptil 4.5 timer",
             "vekt": 0.0054},
         "farger": ["hvit", "gul", "spygrønn"]
         }
    }


for nøkkel in varer.keys():
    print(f"Vare-ID: {nøkkel}\nVarenavn: {varer[nøkkel]['varenavn']}\nPris: {varer[nøkkel]['pris']}\nVarer på lager: {varer[nøkkel]['varelager']}\nProduktinfo: {varer[nøkkel]['produktinfo']}\nTekniske egenskaper:")
    if 'prosessor' in varer[nøkkel]['tekniske egenskaper'].keys():
        print(f"\tProsessor: {varer[nøkkel]['tekniske egenskaper']['prosessor']}")
    if 'grafikkort' in varer[nøkkel]['tekniske egenskaper'].keys():
        print(f"\tGrafikkort: {varer[nøkkel]['tekniske egenskaper']['grafikkort']}")
    if 'batterikapasitet' in varer[nøkkel]['tekniske egenskaper'].keys():
        print(f"\tBatterikapasitet: {varer[nøkkel]['tekniske egenskaper']['batterikapasitet']}")
    if 'vekt' in varer[nøkkel]['tekniske egenskaper'].keys():
        print(f"\tVekt: {varer[nøkkel]['tekniske egenskaper']['vekt']} kg")
    print("\n\n")

def søk(vareId):
    if vareId in varer.keys():
        print(f"\nVare-ID: {vareId}\nVarenavn: {varer[vareId]['varenavn']}\nPris: {varer[vareId]['pris']}\nVarer på lager: {varer[vareId]['varelager']}\nProduktinfo: {varer[vareId]['produktinfo']}\nTekniske egenskaper:")
        if 'prosessor' in varer[vareId]['tekniske egenskaper'].keys():
            print(f"\tProsessor: {varer[vareId]['tekniske egenskaper']['prosessor']}")
        if 'grafikkort' in varer[vareId]['tekniske egenskaper'].keys():
            print(f"\tGrafikkort: {varer[vareId]['tekniske egenskaper']['grafikkort']}")
        if 'batterikapasitet' in varer[vareId]['tekniske egenskaper'].keys():
            print(f"\tBatterikapasitet: {varer[vareId]['tekniske egenskaper']['batterikapasitet']}")
        if 'vekt' in varer[vareId]['tekniske egenskaper'].keys():
            print(f"\tVekt: {varer[vareId]['tekniske egenskaper']['vekt']} kg")
        print("\n\n")
    else:
        print("Varen finnes ikke, eller Vare-IDen er feil")


søk(str(input("skriv inn Vare-ID:\t")))

def oppdaterPris(vareId,nyPris):
    varer[vareId]['pris']=nyPris
    print(f"Ny pris er:\t {varer[vareId]['pris']}")

oppdaterPris(input("Skriv inn Vare-ID på vare som skal endres pris på_\t"),input("\nSkriv inn ny pris:\t"))