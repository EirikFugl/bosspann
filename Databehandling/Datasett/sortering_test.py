import random
import matplotlib.pyplot as plt

usortert = []
sortert = []

for i in range(100):
    usortert.append(random.randint(0,100))

print(usortert)

for i in range(len(usortert)):
    a = usortert[0]
    for tall in usortert:
        if tall < a:
            a = tall
    sortert.append(a)
    usortert.pop(usortert.index(a))

print(sortert)

