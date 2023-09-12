print("Skriv inn værdata plis")

# skrive inn del

liste_vind=[]
liste_regn=[]
liste_temp=[]
liste_trykk=[]
liste_dager=["Mandag","Tirsdag","Onsdag","Torsdag","Fredag","Lørdag","Søndag"]
#liste_data=["temperatur","nedbørsmengde","vindstyrke","trykk"]

for i in range(0,len(liste_dager)):
    print(f"Tast inn data for {liste_dager[i]}")
    liste_temp.append(float(input("Skriv inn temperatur (C)\t:\t")))
    liste_regn.append(float(input("Skriv inn regnmengde (mm)\t:\t")))
    liste_vind.append(float(input("Skriv inn vindstyrke (m/s)\t:\t")))
    liste_trykk.append(float(input("Skriv inn trykk (Bar)\t\t:\t")))

# skrive ut del

print(f"\n\nGjennomsnittstemperaturen denne uken var {sum(liste_temp)/len(liste_temp)}")
print(f"Det var høyest temperatur på {liste_dager[liste_temp.index((max(liste_temp)))]} og da var det {max(liste_temp)}")
print(f"Det var lavest temperatur på {liste_dager[liste_temp.index((min(liste_temp)))]} og da var det {min(liste_temp)}")

print(f"\n\nGjennomsnittsregnmengden denne uken var {sum(liste_regn)/len(liste_regn)}")
print(f"Det var høyest regnmengde på {liste_dager[liste_regn.index((max(liste_regn)))]} og da var det {max(liste_regn)}")
print(f"Det var lavest regnmengde på {liste_dager[liste_regn.index((min(liste_regn)))]} og da var det {min(liste_regn)}")

print(f"\n\nGjennomsnittsvindstyrken denne uken var {sum(liste_vind)/len(liste_vind)}")
print(f"Det var høyest vindstyrke på {liste_dager[liste_vind.index((max(liste_vind)))]} og da var det {max(liste_vind)}")
print(f"Det var lavest vindstyrke på {liste_dager[liste_vind.index((min(liste_vind)))]} og da var det {min(liste_vind)}")

print(f"\n\nGjennomsnittstrykket denne uken var {sum(liste_trykk)/len(liste_trykk)}")
print(f"Det var høyest trykk på {liste_dager[liste_trykk.index((max(liste_trykk)))]} og da var det {max(liste_trykk)}")
print(f"Det var lavest trykk på {liste_dager[liste_trykk.index((min(liste_trykk)))]} og da var det {min(liste_trykk)}")