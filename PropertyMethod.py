#property Method

class Student:
    def __init__(self,total):
        self.total =total
    def average(self):
        return self.total/5.0
   
    def getter(self):
        return self._total
    
    def setter(self,t):
        if t<0 or t>=500:
            print("Invalid total and can' Change")
        else:
            self._total=t
        
    total=property(getter,setter)
    
    
o=Student(450)
print("total : ",o.total)
print("average: ",o.average())
o.total=350
print("total : ",o.total)
print("average : ",o.average())