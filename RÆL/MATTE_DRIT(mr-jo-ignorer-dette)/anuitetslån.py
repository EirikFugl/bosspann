a=58

for i in range(10):
    a = a + 58*0.94**(i+1)

print("Totalsum = ",a)



b = 0.8 #milligram
c = 1

while b <= 5:
    print(b)
    b += b*0.88**c
    c+=1

print(b, i+1)