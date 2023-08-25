a=int(input("skriv et tall:\t"))
if a>9999:
    print("tallet er mer enn firesifret")
elif a>999:
    print("tallet er firesifret")
elif a>99:
    print("tallet er tresifret")
elif a>9:
    print("tallet er tosifret")
else:
    print("tallet er ensifret")