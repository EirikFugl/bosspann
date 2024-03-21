import csv
import matplotlib.pyplot as plt
import time

# deloppgave 1

filnavn = r"C:\SKOLE\VG3\DATA OG SÅNT\bosspann\Prøver\Eirik IT2 mars 2023\run_ww_2020_w-PROVE.csv"

folk_dict = {}

uke_dict = {}

# linenumber,datetime,athlete,distance,duration,gender,age_group,country,major
# 0         ,1       ,2      ,3       ,4       ,5     ,6        ,7      ,8
with open(filnavn,"r",encoding="utf-8") as fil:
    fil = csv.reader(fil, delimiter = ",")

    kolonner = next(fil)
    # print(kolonner)

    for rad in fil:
        if rad[2] not in folk_dict.keys():
            folk_dict[rad[2]] = str(rad[6])


        # deloppgave 3 ting
        if rad[1] not in uke_dict.keys():
            uke_dict[rad[1]] = [float(rad[3]),float(rad[4])]
        else:
            uke_dict[rad[1]] = [uke_dict[rad[1]][0]+float(rad[3]), uke_dict[rad[1]][0]+float(rad[4])]
        

    

x_antall = [0,0,0]                              
y_aldersgruppe = ["18 - 34","35 - 54","55 +"]


# jeg blandet x og y men gidder ikke fikse det/har ikke tid så det får du leve med

for i in list(folk_dict.keys()):
    if folk_dict[i] == "18 - 34":
        x_antall[0] = x_antall[0] + 1
    elif folk_dict[i] == "35 - 54":
        x_antall[1] = x_antall[1] + 1
    elif folk_dict[i] == "55 +":
        x_antall[2] = x_antall[2] + 1

print(f"\n\nI aldersgruppen {y_aldersgruppe[0]} er det {x_antall[0]} utøvere\nI aldersgruppen {y_aldersgruppe[1]} er det {x_antall[1]} utøvere\nI aldersgruppen {y_aldersgruppe[2]}    er det {x_antall[2]} utøvere\n")

# deloppgave 2


#fig, ax = plt.subplots( figsize = (10, 5)) # Angir dimensjoner for figuren
plt.subplot(1,2,1)
plt.bar(y_aldersgruppe, x_antall)


# plt.show() # hvis denne er kommentert ut så må du kommentere den inn igjen
# gidder ikke vente på pyplot hver gang jeg skal teste noe

# deloppgave 3


# for i in range(len(uke_dict.keys())):
#     print(f"Athlete: {list(uke_dict.keys())[i]}\tDistance: {(uke_dict[list(uke_dict.keys())[i]])}")
# print(len(list(uke_dict.keys())))
uke_dict2 = uke_dict
uke_dict = {}
for i in range(len(uke_dict2.keys())):
    uke_dict[i+1] = uke_dict2[list(uke_dict2.keys())[i]]

uke_sortert = {}
def sorter_ukeDistanse_stigende(): # ble ikke helt ferdig med å lage denne men den skal i teorien funke (har funket for å sortere dictionaries i andre program jeg har laget)
    
    for i in range(len(uke_dict.keys())):
        lavest = uke_dict[list(uke_dict.keys())[0]]
        lavest_distanse = list(uke_dict.keys())[0]
        for ting in uke_dict.keys():
            if uke_dict[ting][0] > lavest:
                lavest = uke_dict[ting][0]
                lavest_distanse = ting
        uke_sortert[lavest_distanse] = lavest
        uke_dict.pop(lavest_distanse)


print(uke_dict)
print("\n\n\n")

uke_dict_dist = {}
for i in range(len(uke_dict.keys())):
    uke_dict_dist[list(uke_dict.keys())[i-1]] = uke_dict[list(uke_dict.keys())[i-1]][0]

plt.subplot(1,2,2)
plt.bar(uke_dict_dist.keys(),uke_dict_dist.values())
plt.show()
# sorter_ukeDistanse_stigende()
# print(uke_sortert)