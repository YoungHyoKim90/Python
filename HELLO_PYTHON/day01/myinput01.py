# 첫수를 입력하세요.
a = input("첫수를 입력하세요")

# 두번째 수를 입력하세요.
b = input("두번째 수를 입력하세요")
#모든 값은 string으로 받아온다.
print("a+b는")
print(int(a)+int(b))
print("입니다.")

print("----------------------------------------------")
print("입력하신 a값은 " + a + " 입력하신 b값은 " + b)
print("a+b는"+str(int(a)+int(b))+"입니다.")
print("a-b는"+str(int(a)-int(b))+"입니다.")
print("a*b는"+str(int(a)*int(b))+"입니다.")
print("a/b는"+str(int(a)/int(b))+"입니다.")

aa = int(a)
bb = int(b)
sum = a+b
print("a+b는 " + sum)

print("{}와 {}의 합은 {}입니다.".format(a,b,sum))