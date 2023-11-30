høgd = input("Skriv inn høyde:\t")
bred = input("Skriv inn bredde:\t")

try:
    int(høgd)
    riktig=True
except ValueError:
    print("feil")
    exit()

def vend(høyde,bredde):
    if høyde>bredde:
        return("Portrettbilde")
    elif høyde==bredde:
        return("Kvadratisk bilde")
    else:
        return("Landskapsbilde")

print(vend(høgd,bred))

