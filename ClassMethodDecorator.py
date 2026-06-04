#Class Method Decorator 

class Student:
    count = 0
         
    def __init__(self,name,age):
        self.name =name
        self.age =age
        Student.count += 1
       
    def printall(self):
        print("Name : ", self.name, "Age : ", self.age)
        
    @classmethod
    def total(cls):
        return cls.count
        
o=Student("yuva", 22)
o.printall()
print("Total Admission :",o.total())
a=Student("raj", 23)
a.printall()

print("Total Admission :",Student.total())
print("Total Admission :",o.total())

