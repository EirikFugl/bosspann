n=-25
poengsum=-25
while n<25:
    partier=["Rødt","SV","Arbeiderpartiet","Høyre","FRP"]


    if poengsum > -20+40/len(partier)*(len(partier)-1):
        print(f"Du fikk:\t{partier[len(partier)]}")
        print(f"\n\t\t\t{poengsum}\n")
    elif poengsum > -20+40/len(partier)*(len(partier)-2):
        print(f"Du fikk:\t{partier[len(partier)-1]}")
        print(f"\n\t\t\t{poengsum}\n")
    elif poengsum > -20+40/len(partier)*(len(partier)-3):
        print(f"Du fikk:\t{partier[len(partier)-2]}")
        print(f"\n\t\t\t{poengsum}\n")
    elif poengsum > -20+40/len(partier)*(len(partier)-4):
        print(f"Du fikk:\t{partier[len(partier)-3]}")
        print(f"\n\t\t\t{poengsum}\n")
    elif poengsum > -20+40/len(partier)*(len(partier)-2):
        print(f"Du fikk:\t{partier[len(partier)-1]}")
        print(f"\n\t\t\t{poengsum}\n")
    else:
        print("eirik har gjort noe feil")
        print(f"\n\t\t\t{poengsum}\n")
    n+=1
    poengsum+=1
