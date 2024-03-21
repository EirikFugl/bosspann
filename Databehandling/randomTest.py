import random as r
import matplotlib.pyplot as plt
import time

dict = {}

storttall = 100000
fordeling = 10

starttid = time.perf_counter()

for i in range(storttall):
    a = r.randint(0,fordeling)

    if a not in list(dict.keys()):
        dict[a] = 1
    else:
        dict[a] = dict[a] + 1


print(time.perf_counter()-starttid, " s")

avvik = 0
gjen = 0
a = storttall/fordeling
for ting in list(dict.values()):
    avvik += abs(a-ting)
    gjen += abs(ting)

print(avvik)
print(gjen/fordeling)


plt.subplot(1,2,1)
plt.bar(list(dict.keys()),list(dict.values()))



dict = {}
liste = []

for i in range(fordeling):
    liste.append(i)

starttid = time.perf_counter()

for i in range(storttall):
    a = r.choice(liste)
    if a not in list(dict.keys()):
        dict[a] = 1
    else:
        dict[a] = dict[a] + 1

print(time.perf_counter()-starttid, " s")


avvik = 0
gjen = 0
a = storttall/fordeling
for ting in list(dict.values()):
    avvik += abs(a-ting)
    gjen += abs(ting)


print(avvik)
print(gjen/fordeling)

plt.subplot(1,2,2)
plt.bar(list(dict.keys()),list(dict.values()))

plt.show()