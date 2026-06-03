#type of Excepetion in python

print(dir(locals()['__builtins__']))
print(len(dir(locals()['__builtins__'])))
print("=======")

#NameError Excepetion

try:
    print(a)
except NameError as e:
    print("a is not defined")
    
try:
    print(10/0)   
except ZeroDivisionError as e:
    print("denominator cant be Zero")
   
try:
   a=int("yuva")
except ValueError as e:
    print("Enter Number only")  

try:
    a=[10,20,30,40,50]
    print(a[10])
except IndexError as e:
    print("Invalid Index")   
    
try:
    f=open("yuva.txt")
except FileNotFoundError:
    print("file not found")
else:
    print(f.read())
    
 

    