from random import random

arr9 = [1,2,3,4,5,6,7,8,9]

for i in range(99) :
    rnd = int(random()*9)
    a = arr9[0]
    arr9[0]=arr9[rnd]
    arr9[rnd] =a

print(arr9)

