liste1=["Afrika","Asia","Nord-Amerika","Sør-Amerika","Europa","Antarktis"]
print(f"første: {liste1[1]}\nmidterste: {liste1[(len(liste1)//2)]}\nsiste: {liste1[-1]}\n\n")

liste2=[]
for i in range(1,51):
    liste2.append(i)
#print(liste2)
for i in range(0,len(liste2)):
    print(liste2[i],end=", ")

print("\n\n\n")

liste3=[]
for i in range (1,101,2):
    liste3.append(i)
for i in range (0,len(liste3)):
    print(liste3[i],end=", ")

print("\n\n\n")

liste4=[]
for i in range (1,21):
    liste4.append(i**2)
for i in range (0,len(liste4)):
    print(liste4[i],end=", ")

print("\n\n\n")

liste5=[]
for i in range (1,21):
    liste5.append(i**3)
for i in range (0,len(liste5)):
    print(liste5[i],end=", ")


print("\n\n\n")
print(sum(liste2))
print(sum(liste3))
print(max(liste4))
print(min(liste5))