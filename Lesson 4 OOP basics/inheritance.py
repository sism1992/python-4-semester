

class Machine:
    
    def __init__(self):
        self.power = True
        
    
    def power(self, power):
        self.power = power
    
    def powerButton(self):
        if self.power == True:
            self.power = False
        else:
            self.power == True

class PaperTray:
    
    
    def __init__(self, paper):
        self.paper = paper
    
    def printText(self, text):
        if self.paper > 1:
            print('**from printer ** : '+ text)
            self.paper = paper - 1
        else:
            print('not enough paper')
    
    def fillPaper(self, amount):
        self.paper = paper + amount
        
        
        
class Printer(Machine):
    
    def __init__(self, tray) :
        self.tray = tray
    
    def printText(self, text):
        tray.printText(text)
  
t = PaperTray(5)        
#p = Printer(t)
t.printText('hej')
#p.printText('hej')