#instance Method

class Student:
    name="yuvaraj N"
    age=22
    
    def printall(self,gender):
        print("name : ",Student.name)
        print("age : ",Student.age)
        print("Gender : ", gender)

o=Student()
"""       
o.printall()
Student.printall(o)
"""
o.printall("Male")
Student.printall(o,"Male")
