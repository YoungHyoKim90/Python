def showDan(dan):
    for i in range(1,9+1) :
        print("{}*{}={}".format(dan,i,i*dan))

    
a = int(input("원하는 숫자를 입력해주세요. 구구단 해드립니다."))
showDan(a)