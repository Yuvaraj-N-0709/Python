#keyword Arguments function in python

def message(name,age):
     print(name,"age is",age)
     
message(age=25,name="yuva")

#Arbitrary Keyword Arguments in python 

def bioData(**data):
    print(data)
    
bioData(name="yuvaraj",age=22,gender="male")
