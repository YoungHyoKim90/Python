from random import random

arr45 = [
    1, 2, 3, 4, 5, 6, 7, 8, 9, 10,
    11, 12, 13, 14, 15, 16, 17, 18, 19, 20,
    21, 22, 23, 24, 25, 26, 27, 28, 29, 30,
    31, 32, 33, 34, 35, 36, 37, 38, 39, 40,
    41, 42, 43, 44, 45        
        ]

a = arr45.pop(int(random()*45))
b = arr45.pop(int(random()*44))
#b = arr45.pop(int(random()*len(arr45)))
c = arr45.pop(int(random()*43))
d = arr45.pop(int(random()*42))
e = arr45.pop(int(random()*41))
f = arr45.pop(int(random()*40))

print(arr45)
print(a, end=" ")
print(b, end=" ")
print(c, end=" ")
print(d, end=" ")
print(e, end=" ")
print(f, end=" ")

print()
print("--------------------------------------")

for i in range(6) :
    a = arr45.pop(int(random()*len(arr45)))
    print(a,end=" ")