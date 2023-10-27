import os
os.system("cls")


a=4
n=10
for i in range (n):
    print(a,end=",\t")
    a=a*2-3

def f(b):
    if b==1:
        return 1
    else:
        return f(b-1)*2-3


for i in range (10):
    print(f(i))