#첫수를 입력하시오. ex 1
#끝수를 입력하시오 ex 4
# 1에서 4까지의 합은 10입니다.

a = input("첫수 입력하시오")
b = input("끝수 입력하시오")

print("입력받은값",a,b)

aa = int(a)
bb = int(b)+1

arr = range(aa, bb)
# 이렇게 해줘도 된다.arr = range(aa, bb+1)

print("aa,bb의 값",aa,bb)
print(arr)
print(list(arr))

sum = 0;

for i in arr:
    sum += i
    print("더해지는 i값" , i ,"을 더합니다.")
    print("sum의 변화" , sum)

print("최종 합계 : " , sum)

print("첫 수 입력 값은 {}, 끝수 입력값은{} 모든 값의 합은 {}".format(a,b,sum))
    
if sum %2 == 0:
    print("총합의 결과는 짝수입니다.")
    
else :
    print("총합의 결과는 홀수입니다.")
    
if sum %3 == 0:
    print("총합의 결과는 3의 배수입니다.")
    

