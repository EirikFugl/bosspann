#Valgomat
import random as r

start=str.lower(input("Velkommen til Valgomat!"))

spørsmål_1="Er skattene for høye?"

spm_liste_H=["Skattene for høye for alle","Flere offentlige institusjoner bør privatiseres","Det bør være lov med privatskoler","Mer penger bør brukes på å bygge motorveier"]
spm_liste_V=["Skatten bør økes for de med høy inntekt","Mer ressurser bør gå til å utbedre de offentlige institusjonene","Privat rus- og eldreomsorg burde avskaffes","De bør finnes et øvre tak på hvor mye det er lov å tjene"]
#print(len(spm_liste_V))
#print(len(spm_liste_H))

poengsum=0

#print(poengsum)

antall_spm=len(spm_liste_H)+len(spm_liste_V)

n=0
spmn=0
svart=[]

while n<=antall_spm:
    HorV=r.randint(1,2)
    #print(HorV)
    spmn=r.randint(0,3)
    #print(spmn)
    #print(HorV,"\t",spmn)
    svartn=()
    #print(svart)
    svartn=str(HorV)+str(spmn)
    #print(svartn)    

    if svartn in svart:
        n=n-1
    elif HorV==1:
        svar=str.lower(input(f"Spørsmål:\n\t\t{spm_liste_H[spmn]}\n\t\tEr du\n\t\thelt enig\tenig\tuenig\thelt uenig?\n\t\t"))
        if svar=="helt enig":
            poengsum+=2
        elif svar=="enig":
            poengsum+=1
        elif svar=="uenig":
            poengsum=poengsum-1
        elif svar=="helt uenig":
            poengsum=poengsum-2
        else:
            svar=str.lower(input("Du skrev feil, prøv på nytt\n\t\t"))
    elif HorV==2:
        svar=str.lower(input(f"Spørsmål:\n\t\t{spm_liste_V[spmn]}\n\t\tEr du\n\t\thelt enig\tenig\tuenig\thelt uenig?\n\t\t"))
        if svar=="helt enig":
            poengsum=poengsum-2
        elif svar=="enig":
            poengsum=poengsum-1
        elif svar=="uenig":
            poengsum+=1
        elif svar=="helt uenig":
            poengsum+=2
        else:
            svar=str.lower(input("Du skrev feil, prøv på nytt\n\t\t"))
    svart.append(svartn)
    #print(poengsum)
    n+=1
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


partier=["Rødt","SV","Arbeiderpartiet","Høyre","FRP"]


if poengsum > -20+40/len(partier)*(len(partier)-1):
    print(f"Du fikk:\t{partier[len(partier)]}")
elif poengsum > -20+40/len(partier)*(len(partier)-2):
    print(f"Du fikk:\t{partier[len(partier)-1]}")
elif poengsum > -20+40/len(partier)*(len(partier)-3):
    print(f"Du fikk:\t{partier[len(partier)-2]}")
elif poengsum > -20+40/len(partier)*(len(partier)-4):
    print(f"Du fikk:\t{partier[len(partier)-3]}")
elif poengsum > -20+40/len(partier)*(len(partier)-2):
    print(f"Du fikk:\t{partier[len(partier)-1]}")
else:
    print("eirik har gjort noe feil")

'''
if poengsum > 10:
    print("Du fikk:\tFRP")
elif poengsum > 2:
    print("Du fikk:\tHøyre")
elif poengsum > -6:
    print("Du fikk:\tArbeiderpartiet")
elif poengsum > -14:
    print("Du fikk:\tSV")
elif poengsum > -20:
    print("Du fikk:\tArbeiderpartiet")