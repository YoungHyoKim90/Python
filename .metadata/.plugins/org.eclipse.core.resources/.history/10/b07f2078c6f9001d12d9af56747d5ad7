#1~100사이의 숫자를 선택
#컴퓨터는 1~100사이의 숫자의 업다운. 그래서 맞추기. 10번의 기회를 줌.
#10번안에 못하면 실패하셨습니다.
from random import random

#숫자 입력받기

gamer = int(input("숫자 35 입력하세요 : "))

print(gamer ,"를 입력하셨습니다.")

number = 35

if gamer == number:
    print("정답입니다")
else:
    print("틀렸습니다")
    
print("이제 본게임을 시작하도록 하겠습니다.")

a = random.randint(1,100)
n = 0
print("컴퓨터의 렘덤 숫자를 알아 맞혀보세요.(1~100 사이)") #print("") 수정
q = 0 #추가
while a != q:
    q = int(input("1~100 숫자 입력:")) #int( input("") ) 수정
    if q < a:
        print("up")
    elif a < q:
        print("down")
    n += 1
print("정답입니다.")
print("걸린 순서: "+str(n)) # n -> str(n) 수정