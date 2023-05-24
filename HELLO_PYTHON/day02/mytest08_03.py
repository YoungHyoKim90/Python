# 가위/바위/보를 선택하시오 : 가위
# 나: 가위
# 컴: 바위 (랜덤이용)
#결과: 패배
from random import random

com =  ""
mine = ""
result = ""

mine = input("가위/바위/보를 선택하시오")

rnd = random()
print("내가 낸 것은",mine)
if rnd > 0.66:
    com = "가위"
elif rnd > 0.33 :
    com = "바위"
else :
    com = "보"

print("컴퓨터가 낸 것은",com)

if com == "가위" and mine =="가위" : result="비김"    
if com == "가위" and mine =="바위" : result="이김"    
if com == "가위" and mine =="보" : result="짐"    

if com == "바위" and mine =="가위" : result="짐"    
if com == "바위" and mine =="바위" : result="비김"    
if com == "바위" and mine =="보" : result="이김"   

if com == "보" and mine =="가위" : result="이김"    
if com == "보" and mine =="바위" : result="짐"    
if com == "보" and mine =="보" : result="비김"

print("결과 =" , result)
 