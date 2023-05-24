from random import random
a = input("홀/짝을 선택하시오")

rnd = random()
rnd2 = ""

if rnd > 0.5:
    rnd2 = "홀"
    
else:
    rnd2 = "짝"
    
print("컴퓨터가 낸 것 : ", rnd2)
print("당신이 낸 것 : ", a)

if a == rnd2:
    print("승리하였습니다.")
    
else:
    print("패배하였습니다.")
    
if rnd % 2 == 0:
    rnd2 = "짝"
else:
    rnd2 = "홀"
    
if a == rnd2:
    print("승리하였습니다.")
    
else:
    print("패배하였습니다.")
    
# 풀이 

mine = input("홀/짝을 선택하시오")
com = ""
result = ""

rnd3 = random()

if rnd > 0.5:
    com = "홀"
else:
    com = "짝"
    
if com == mine:
    result = "이김"
else :
    result = "짐"
    
print("나: {}".format(mine))
print("컴: {}".format(com))
print("나: {}".format(result))