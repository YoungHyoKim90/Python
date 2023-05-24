# 가위/바위/보를 선택하시오 : 가위
# 나: 가위
# 컴: 바위 (랜덤이용)
#결과: 패배
from random import random

a=input("가위/바위/보를 선택하시오")
com=''
com=random()
rnd=com
res=''

if com>0.6666:
    com='가위'
elif com>0.3333:
    com='바위'
else:
    com='보'
    
print("나: ",a)
print("컴: ",com)

if a==com:
    res='무승부'
elif (a=='가위' and com=='보')or(a=='바위' and com=='가위')or(a=='보' and com=='바위'):
    res='승리'
else:
    res="패배"
print("결과:",res)
    
    

