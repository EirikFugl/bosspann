import csv
import matplotlib.pyplot as plt


# oppgave 1

filnavn = r"Databehandling/Datasett/youtube.csv"

land = []

with open(filnavn, "r") as fil:
    fil = csv.reader(fil,delimiter=",")

    nøkler = next(fil)
    print(nøkler)

    for rad in fil:
        land.append(rad[7])

print(land)

# lager dict med mengde

land_dict = {}

for ting in land:
    if ting not in land_dict.keys():
        land_dict[ting] = 1
    else:
        land_dict[ting] += 1

print("\n\n")
print(land_dict)

# sorterer

land_sortert = {}
for i in range(len(land_dict.keys())):
    lavest = land_dict[list(land_dict.keys())[0]]
    lavest_land = list(land_dict.keys())[0]
    for ting in land_dict.keys():
        if land_dict[ting] < lavest:
            lavest = land_dict[ting]
            lavest_land = ting
    land_sortert[lavest_land] = lavest
    land_dict.pop(lavest_land)


print(land_sortert)

fig = plt.figure(figsize = (8,8))

x = list(land_sortert.values())[-10:]
y = list(land_sortert.keys())[-10:]

plt.barh(y,x, left=0.3)
plt.show()