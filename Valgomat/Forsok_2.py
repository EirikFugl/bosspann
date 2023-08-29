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

while n<=antall_spm:
    HorV=r.randint(1,2)
    spmn=r.randint(0,3)
    #print(HorV,"\t",spmn)
    
    if HorV==1:
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
    if HorV==2:
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
    print(poengsum)
    n+=1
'''
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
