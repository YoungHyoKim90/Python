class KimJu : 
    def __init__(self):
        print("생성자")
        self.cnt_nuclear = 200
        
    def aoji(self):
        self.cnt_nuclear += 1

    def __del__(self):
        print("소멸자")
        #메모리에서 사라지는 순간 ! 자바를 제외한 나머지는 소멸자 명령어를 넣어줘야 한다.
        
    def __str__(self):
        return "최종 핵 갯수 : "+str(self.cnt_nuclear)
    
   
        
if __name__ == '__main__':
    kju = KimJu()
    print(kju.cnt_nuclear)
    kju.aoji()
    print(kju.cnt_nuclear)
    print(kju)
    