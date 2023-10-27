handlekurv = {   
    "melk": 17.90,   
    "smør": 38.90,   
    "kokt skinke": 23.10,   
    "sjokolade": 11.90,   
    "oppvaskmiddel": 24.40,   
    "frossenpizza": 29.90 
    } 

for k, v in handlekurv.items():
    if v == min(handlekurv.values()):
        minProd = k

for k, v in handlekurv.items():
    if v == max(handlekurv.values()):
        maxProd = k

print(f"den laveste prisen er {min(handlekurv.values())} og tilhørende produkt er {minProd}")
print(f"den høyeste prisen er {max(handlekurv.values())} og tilhørende produkt er {maxProd}")
print(f"totalsummen er {round(sum(handlekurv.values()),5)}")