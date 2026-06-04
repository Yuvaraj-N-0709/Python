#Property Decorators getter setter

class Student:
    def __init__(self,total):
        self.total =total
    def average(self):
        return self.total/5.0
    @property   
    def total(self):
        return self._total
    @total.setter
    def total(self,t):
        self._total=t
    
o=Student(450)
print("total : ",o.total)
print("average: ",o.average())
o.total=250
print("total : ",o.total)
print("average : ",o.average())
