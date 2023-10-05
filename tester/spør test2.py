import random as r




landdata = {
            "Land":         ["Norge", "Sverige",   "USA", "Tyskland", "Kina"],
            "Innbyggertall":[5504329,  10409248,    331449281,         83149300,   1443497378],
            "Hovedstad":    ["Oslo",  "Stockholm", "Washington D.C.", "Berlin",   "Beijing"],
            "Grenser":      [["Sverige", "Finland", "Russland"],["Norge", "Finland"],
            ["Canada", "Mexico"],["Danmark","Polen","Tsjekkia","Østerrike","Sveits","Frankrike", "Luxembourg", "Belgia","Nederland"],["Mongolia", "Russland", "Nord-Korea", "India", "Nepal", "Pakistan", "Afghanistan", "Tadsjikistan", "Kirgisistan", "Kasakhstan", "Bhutan", "Myanmar", "Laos", "Vietnam"]]
            }

# Velg et tilfeldig indeksnummer innenfor området av antall land
tilfeldig_indeks = r.randint(0, len(landdata["Land"]) - 1)

# Bruk indeksen til å hente ut et tilfeldig land, innbyggertall og hovedstad
tilfeldig_land = landdata["Land"][tilfeldig_indeks]
innbyggertall = landdata["Innbyggertall"][tilfeldig_indeks]
hovedstad = landdata["Hovedstad"][tilfeldig_indeks]

print(tilfeldig_indeks,tilfeldig_land, innbyggertall,hovedstad)

# Du kan nå bruke 'tilfeldig_land', 'innbyggertall' og 'hovedstad' i spørsmålet ditt til brukeren.
print(f"Hvor mange innbyggere bor i {tilfeldig_land}?")