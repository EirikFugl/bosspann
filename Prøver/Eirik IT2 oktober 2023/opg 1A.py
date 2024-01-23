høgd = int(input("Skriv inn høyde:\t"))
bred = int(input("Skriv inn bredde:\t"))

def vend(høyde,bredde):
    if høyde>bredde:
        return("Portrettbilde")
    elif høyde==bredde:
        return("Kvadratisk bilde")
    else:
        return("Landskapsbilde")

print(vend(høgd,bred))

