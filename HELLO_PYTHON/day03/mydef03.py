from random import random

def getHollJjak():
    rnd = random()
    ret = "홀"
    if rnd >0.5:
        ret = "짝"
    return ret
        
com = getHollJjak()
print("com : ",com)