byer= {
    "Oslo": 1043168,
    "Bergen": 265470,
    "Stavanger": 229911,
    "Trondheim": 191771,
    "Fredrikstad": 117663,
    "Drammen": 110236,
    "Porsgrunn": 94102,
    "Kristiansand": 64913,
    "Ålesund": 54399,
    "Tønsberg": 53818
}
lav_grense = int(input("Skriv inn en nedre grense:\n\t\t"))
øvr_grense = int(input("Skriv inn en øvre grense:\n\t\t"))

for k,v in byer.items():
    if lav_grense <= v <= øvr_grense:
        print(k)