#첫수를 넣으세요. 1
#끝수를 넣으세요. 5
#배수를 입력하세요 2
#1에서 5까지 2의 배수의 합은 6입니다.
a = input("첫수를 넣으세요.")
aa = int(a)
b= input("끝수를 넣으세요.")
bb = int(b)
c= input("배수를 넣으세요.")
cc= int(c)

print(aa,bb,cc)

d = range(aa,bb)
print(d)

sum = 0;
sum2 =0;

for i in range(aa,bb+1) :
    print(i,"번째 for입니다.")
    sum += i
    print("sum의 값은 " , sum)


sum2 %cc == sum
print("cc로 sum2를 나눈값은 " ,sum2)
print("{}에서 {}까지 배수의 합은 {}입니다.".format(aa,bb,sum2))
    