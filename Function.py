#No Return Type Without Argument Function in Python
def add():
    a=int(input("Enter The Value Of A : "))
    b=int(input("Enter The Value Of B : "))
    c=a+b
    print("Total ",c)
    
add()

print("=========================")
#No return Type With Argument Function in Python

def sub(a,b):
    c=a-b
    print("Difference ",c)
    
sub(25,5)


print("=========================")
#Return Type Without Argument Function in Python

def mul():
    a=int(input("Enter The Value Of A : "))
    b=int(input("Enter The Value Of B : "))
    c=a*b
    return c
    
x=mul()
print("mul",x)
 
print("=========================")
#Return Type With Argument Function in Python

def div(a,b):
    c=a/b
    return c
    
x=div(25,2)
print("division",x)
 
print("=========================")
#Arbitrary Arguments Function in Python(*)

def class_10(*Student):
    print(Student)
    for user in Student:
        print(user)
 
class_10("yuva","praveen","jana","Mani")

