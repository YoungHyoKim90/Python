# 만약 70일 경우 (최종 10회후 )
from random import random

# 1~100사이의 수를 고르세요 50
# UP입니다.

# 1~100사이의 수를 고르세요 60
# UP입니다.

# 1~100사이의 수를 고르세요 80
# DOWN입니다.

# 1~100사이의 수를 고르세요 70
# 정답은 70입니다.

# 1~100사이의 수를 고르세요 71(10회이상시) for range 10!
# 실패하셨습니다. 정답은 70이였네요

com = int(random()*100)+1

flagFind = False

print("나오는 숫자" , com)

for i in range(10):
    mine = input("1~100사이의 수를 고르세요")
    imine = int(mine)
    if com > imine : 
        print("UP!")
    if com < imine : 
        print("DOWN!")
    if com == imine : 
        flagFind = True 
        break
    
if flagFind:
    print("정답입니다! 정답은 {} 입니다.".format(com))
    
else:
    print("실패하셨습니다. 정답은{}입니다.".format(com))
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    