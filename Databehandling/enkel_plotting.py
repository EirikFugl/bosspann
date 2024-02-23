import matplotlib.pyplot as plt
import numpy as np

yverd = [1,2,3,4,5,6]
y2verd = [1,4,6,3,5,0]
y3verd = [4,7,2,3,8,10]
xverd = [1,2,3,4,5,6]

plt.plot(xverd,yverd)
plt.plot(xverd,y2verd)
plt.plot(xverd,y3verd)
plt.scatter(xverd,y2verd)

def f(x):
    return (x**2*2-1*x*3+1)/(3*2)

exverd=[]
iyverd=[]
for i in range(0,20):
    exverd.append(i)
    iyverd.append(f(i))

# plt.plot(exverd,iyverd)

def g(x):
    return 4*x**3-x**5

xverdier = np.linspace(-2,2,100)
yverdier = g(xverdier)

plt.plot(xverdier,yverdier)
plt.title("rare ting typ $math$")
plt.xlabel("$x$")
plt.ylabel("$y$")
plt.xlim(-2,6)
plt.ylim(-10,10)



utdanningsprogram = [
  "Bygg- og anleggsteknikk", 
  "Elektro og datateknologi",
  "Helse- og oppvekstfag",
  "Naturbruk",
  "Restaurant- og matfag",
  "Teknologi- og industrifag",
  "Håndverk, design og produktutvikling",
  "Frisør, blomster, interiør og eksponeringsdesign",
  "Informasjonsteknologi og medieproduksjon",
  "Salg, service og reiseliv"
]

antallGutter = [3811, 4168, 8661, 2057, 1484, 5501, 313, 901, 1309, 2061]
antallJenter = [352, 268, 7286, 1028, 709, 851, 243, 826, 200, 895]

fig, ax = plt.subplots(figsize=(10, 5))    # Angir dimensjoner for figure-objektet

y = np.arange(10)

ax.barh(y+0.2, antallJenter, height=0.4, label="Jenter")  # Lager stolpediagram jenter
ax.barh(y-0.2, antallGutter, height=0.4, label="Gutter")  # Lager stolpediagram gutter
ax.set_yticks(y, utdanningsprogram)                       # Legger til akseverdier
ax.legend()                                               # Legger til beskrivelse

fig.subplots_adjust(left=0.4)  # Øker plassen på venstre side av diagrammet

ax.grid(axis="x")  # Legger til rutenett (bare vertikale linjer)
plt.show()         # Viser diagrammet













plt.show()