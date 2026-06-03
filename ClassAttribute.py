#Class Attribute in python

class Student():
    name= "yuvaraj"
    age = 22

#getattr la output eduka mudium
print(getattr(Student,'name'))
print(getattr(Student,'age'))
print(getattr(Student,'gender','no such Attribute found'))
    
#Dot Notation la output eduka mudium 
print(Student.name)
print(Student.age)

#setattr la create panna mudium 
setattr(Student,'name','yuvaraj Narayanasamy') 
print(Student.name)

setattr(Student,'gender','Male')
print(Student.gender)

#dot Notation la kuda Attribute create panna mudium
Student.city="karur"
print(Student.city)

print(Student.__dict__)
delattr(Student,'city')
print(Student.__dict__)

#dot Notation la kuda Attribute del panna mudium
del Student.gender
print(Student.__dict__)




