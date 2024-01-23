n=-25
poengsum=-25
while n<25:
    '''
    partier=["Rødt","SV","Arbeiderpartiet","Høyre","FRP"]


    if poengsum < 20-((40/(len(partier)))*(len(partier)-1)):
        print(poengsum)
        print(f"Du fikk:\t{partier[len(partier)-1]}")
        print(f"\n\t\t\t{20-((40/(len(partier)))*(len(partier)-1))}\n")
    elif poengsum < 20-((40/(len(partier)))*(len(partier)-2)):
        print(poengsum)
        print(f"Du fikk:\t{partier[len(partier)-2]}")
        print(f"\n\t\t\t{20-((40/(len(partier)))*(len(partier)-2))}\n")
    elif poengsum < 20-((40/(len(partier)))*(len(partier)-3)):
        print(poengsum)
        print(f"Du fikk:\t{partier[len(partier)-3]}")
        print(f"\n\t\t\t{20-((40/(len(partier)))*(len(partier)-3))}\n")
    elif poengsum < 20-((40/(len(partier)))*(len(partier)-4)):
        print(poengsum)
        print(f"Du fikk:\t{partier[len(partier)-4]}")
        print(f"\n\t\t\t{20-((40/(len(partier)))*(len(partier)-4))}\n")
    elif poengsum <= 20-((40/(len(partier)))*(len(partier)-5)):
        print(poengsum)
        print(f"Du fikk:\t{partier[len(partier)-5]}")
        print(f"\n\t\t\t{20-((40/(len(partier)))*(len(partier)-5))}\n")
    else:
        print("eirik har gjort noe feil")
        print(f"\n\t\t\t{poengsum}\n")
    '''

    if poengsum > 12:
        print("Du fikk:\tFRP",poengsum)
    elif poengsum > 3:
        print("Du fikk:\tHøyre",poengsum)
    elif poengsum > -6:
        print("Du fikk:\tArbeiderpartiet",poengsum)
    elif poengsum > -14:
        print("Du fikk:\tSV",poengsum)
    elif poengsum > -20:
        print("Du fikk:\tRødt",poengsum)
    n+=1
    poengsum+=1
    
