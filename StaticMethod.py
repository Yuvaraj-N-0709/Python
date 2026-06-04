#Static Method in pyton

class Student:
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def printall(self):
        print("Name : ", self.name, "Age : ", self.age)
        
    @staticmethod   
    def welcome():
        print("welcom to python")
        
s1=Student("yuvaraj",23)
s1.printall()
s1.welcome()

s2=Student("praveen",25)
s2.printall()
s2.welcome()
