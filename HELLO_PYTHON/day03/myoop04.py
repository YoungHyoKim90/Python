class Xi:
    def __init__(self):
        self.pos = 100
        
    def nodaedap(self):
        self.pos -= 10
        
        
class Gelensky:
    def __init__(self):
        self.cnt_tank = 100
        
    def goG7(self):
        self.cnt_tank *= 2
class Lamiran:
    def __init__(self):
        self.cnt_pig = 1
        
    def momstouch(self):
        self.cnt_pig += 100
        
class MunYoungTak(Xi,Gelensky,Lamiran):#다중상속!!!!!
    def __init__(self):
        Xi.__init__(self)#다중상속!!!!!
        Gelensky.__init__(self)#다중상속!!!!!
        Lamiran.__init__(self)#다중상속!!!!!

    
    
if __name__ == '__main__':
    myt = MunYoungTak()
    print(myt.pos)
    print(myt.cnt_tank)
    print(myt.cnt_pig)
    myt.nodaedap()
    myt.goG7()
    myt.momstouch()
    print(myt.pos)
    print(myt.cnt_tank)
    print(myt.cnt_pig)