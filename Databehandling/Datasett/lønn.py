import json
import matplotlib.pyplot as plt

filnavn = "Databehandling/Datasett/lonnstabell.json"

with open(filnavn, encoding="utf-8") as fil:
    data = json.load(fil)

årstall = list(data["dataset"]["dimension"]["Tid"]["category"]["label"])
lønnM = list(data["dataset"]["value"][0:6])
lønnK = list(data["dataset"]["value"][6:12])

print(årstall)
print(lønnM)
print(lønnK)


plt.subplot(2,1) # nr 1
plt.plot(årstall,lønnM)
plt.plot(årstall,lønnK)

plt.grid()
plt.legend()
plt.title("Lønn menn/kvinner")


plt.subplot(2,2)
plt.plot


plt.show()