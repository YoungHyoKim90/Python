#첫수를 넣으세요. 1
#끝수를 넣으세요. 5
#배수를 입력하세요 2
#1에서 5까지 2의 배수의 합은 6입니다.

a = input("첫수를 넣으세요")
b = input("두번째 수를 넣으세요.")
c = input("배수를 입력하세요.")

aa = int(a)
bb = int(b)
cc = int(c)

print("받은값 출력",aa,bb,cc)

sum = 0 

for i in range(aa,bb+1):
    print(i)
    if i%cc ==0:
        sum += i
    
print("sum",sum)

print("{}에서 {}까지 {}의 배수의 합은 {}입니다.".format(a,b,c,sum))
    