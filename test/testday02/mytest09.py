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

# 1~100사이의 수를 고르세요 71(10회이상시)
# 실패하셨습니다. 정답은 70이였네요

com=(int)(random()*100+1)
print(com)

user=input("1~100사이의 수를 고르세요")
userNum=int(user)
# arr=range(1,10+1)
# arr=list(arr)
# print(arr)
count=1
# for i in arr: 
while userNum!=com:
    if count!=10:
        if userNum>com:
            print("down입니다.")
        else:
            print("up입니다.")
        user=input("1~100사이의 수를 고르세요")
        userNum=int(user)
        count+=1
        print(count,"회")
    else:    
        print("실패하셨습니다. 정답은 ",com,"이였네요.")
        break
if count!=10:
    print("정답은",com,"입니다.")

    
