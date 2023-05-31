import sys
from PyQt5.Qt import QApplication

class WindowClass():
    def __init__(self):
        self.setupUi(self)
        self.pb.clicked.connect(self.myclick)
        
        def getStar(self,cnt):
            ret=""
            for i in range(cnt):
                ret += "*"
            ret += "\n"
            return ret
        
        def myclick(self):
            f = self.le_first.text()
            l = self.le_last.text()
            ff = int(f)
            ll = int(l)
            txt = ""
            
            for i in range(ff,ll+1):
                txt += self.getStar(i)
                
            self.te.setText(txt)
            
if __name__ "__main__":
    app = QApplication(sys.argv)
    myWindow = WindowClass()
    