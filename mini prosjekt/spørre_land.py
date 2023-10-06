#start
import random
a=0
b=0
spurt = []
svar=()


landdata = {"Land":["Norge", "Sverige", "USA", "Tyskland", "Kina"],
            "Innbyggertall":[5504329,10409248,331449281,83149300,1443497378],
            "Hovedstad":["Oslo", "Stockholm", "Washington D.C.", "Berlin", "Beijing"],
            "Grenser":[["Sverige", "Finland", "Russland"],["Norge", "Finland"],
            ["Canada", "Mexico"],["Danmark","Polen","Tsjekkia","Østerrike","Sveits","Frankrike", "Luxembourg", "Belgia","Nederland"],
            ["Mongolia", "Russland", "Nord-Korea", "India", "Nepal", "Pakistan", "Afghanistan", "Tadsjikistan", "Kirgisistan", "Kasakhstan", "Bhutan", "Myanmar", "Laos", "Vietnam"]]}



spørsmål = [("Hvor mange innbyggere er det i ",{landdata["Land"](a)},"?"),
            ("Hva er hovedstaden i ",{landdata.keys(a)},"?"),
            ("Hvilke land grenser ",{landdata.keys(a)} ,"til?"),
            ("Hvilket land har flest innbyggere av ",{landdata.keys(a)}," og ",{landdata.keys(a2)},"?")]

svar     = [("Det bor {landdata.values(2)[a]} innbyggere i {landdata.keys(a)}")]



#funksjoner
def spør():
    a = random.randint(1,4)
    a2 = random.randint(1,5)
    b = random.randint(1,5)
    svar=input(f"")


    return

#kjør

spør()

print(landdata["Grenser"][3])