from random import random

arr45 = [
    1, 2, 3, 4, 5, 6, 7, 8, 9, 10,
    11, 12, 13, 14, 15, 16, 17, 18, 19, 20,
    21, 22, 23, 24, 25, 26, 27, 28, 29, 30,
    31, 32, 33, 34, 35, 36, 37, 38, 39, 40,
    41, 42, 43, 44, 45        
        ]

for i in range(999):
    rnd = int(random() * 45)
    a = arr45[0]
    arr45[0] = arr45[rnd]
    arr45[rnd] = a

print(arr45[0],end=" ")
print(arr45[1],end=" ")
print(arr45[2],end=" ")
print(arr45[3],end=" ")
print(arr45[4],end=" ")
print(arr45[5],end=" ")
print(arr45[6],end=" ")
