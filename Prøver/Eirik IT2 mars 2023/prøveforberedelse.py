import csv
import matplotlib.pyplot as plt
import time

filnavn = r"C:\SKOLE\VG3\DATA OG SÅNT\bosspann\Prøver\Eirik IT2 mars 2023\run_ww_2020_w-PROVE.csv"

# C:\SKOLE\VG3\DATA OG SÅNT\bosspann\Prøver\Eirik IT2 mars 2023\prøveforberedelse.py

folk_dict = {}

# linenumber,datetime,athlete,distance,duration,gender,age_group,country,major

with open(filnavn,"r",encoding="utf-8") as fil:
    fil = csv.reader(fil, delimiter = ",")

    kolonner = next(fil)
    print(kolonner)

    for rad in fil:
        if rad[2] not in folk_dict.keys():
            folk_dict[rad[2]] = float(rad[3])
        else:
            folk_dict[rad[2]] = (folk_dict[rad[2]])+float(rad[3])

for i in range(0,100):
    print(f"Athlete: {list(folk_dict.keys())[i]}\tDistance: {round(folk_dict[list(folk_dict.keys())[i]])}")

def sorter_folkDistanse_stigende():
    starttid = time.perf_counter()

    folk_dict2 = folk_dict
    # for i in range(1000):
    #     folk_dict2[list(folk_dict.keys())[i]] = folk_dict[list(folk_dict.keys())[i]]

    # print(folk_dict2)
    folk_sortert = {}

    for i in range(len(folk_dict2.keys())):
        lavest = folk_dict2[list(folk_dict2.keys())[0]]
        lavest_distanse = list(folk_dict2.keys())[0]
        for ting in folk_dict2.keys():
            if folk_dict2[ting] > lavest:
                lavest = folk_dict2[ting]
                lavest_distanse = ting
        folk_sortert[lavest_distanse] = lavest
        folk_dict2.pop(lavest_distanse)

    for i in range(len(list(folk_sortert.keys()))):
        print(f"Person: {list(folk_sortert.keys())[i]}\t\t{list(folk_sortert.values())[i]}")


    print(f"\nTid: {time.perf_counter()-starttid} s")
    print(len(list(folk_dict2.keys())))


    plt.plot(list(folk_sortert.keys()),list(folk_sortert.values()))
    # plt.savefig('C:\SKOLE\VG3\DATA OG SÅNT\bosspann\Prøver\Eirik IT2 mars 2023\foo.png', bbox_inches='tight')
    print("ferdig")

# sorter_folkDistanse_stigende()

