#Class Method

class Student:
    name="yuvaraj N"
    age=22
    
    def printall():
        print("name : ",Student.name)
        print("age : ",Student.age)
        
Student.printall()
print(Student.__dict__)

print(getattr(Student, "printall"))
getattr(Student, "printall")()

Student.__dict__['printall']()
