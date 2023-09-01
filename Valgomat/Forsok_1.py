#Valgomat
import random as r

start=str.lower(input("Velkommen til Valgomat!"))

spørsmål_1="Er skattene for høye?"



svar=str.lower(input(f"Første spørsmål:\n\t\t{spørsmål_1}\n\t\tEr du\n\t\thelt enig\tenig\tuenig\thelt uenig?\n\t\t"))

poengsum=0

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

print(poengsum)



