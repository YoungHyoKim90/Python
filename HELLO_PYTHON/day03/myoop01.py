class Animal :
    def __init__(self):
        self.age = 0
        
    def oneYear(self):
        self.age += 1

class Human(Animal) :
    def __init__(self):
        super().__init__()
        self.flagLang = False
        
    def momstouch(self):
        self.flagLang = True


if __name__ == '__main__':

    print("---------------------------------------")
    hum = Human()
    print("hum : ",hum.age)
    hum.oneYear()
    print("hum + oneYear : ",hum.age)
    hum = Human()
    print("hum : " , hum.flagLang)
    hum.momstouch()
    print("hum + momstouch : ", hum.flagLang)
    
    
    
    
    
    
    
    
    
    
    
    
    
    