#출력할 단수를 입력하세요.

print("★ 구구단을 출력합니다.\n")
for x in range(2, 10):
    print("------- [" + str(x) + "단] -------")
    for y in range(1, 10):
        print(x, "X", y, "=", x*y)
print("----------------------------------------------------------")


num = int(input("궁금한 숫자를 입력하세요."))
for i in range(1, 10):
    print(str(num) + " * " + str(i) + " = " + str(num * i))
    
dan = input("출력할 단수를 입력하세요.")
idan = int(dan)

for i in range(1,10) :
    print("{}*{}={}".format(idan,i,i*idan))
    print("{}*{}={}".format(idan,i,i*idan))

#수학적 규칙이 나와야 for문을 사용하기 좋다. 즉 규칙부터 적고 for문을 작성해라.