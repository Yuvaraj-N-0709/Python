# Handling Multiple Exception in python

try:
    a=10/2
    print(a)
    b=[10,20,30,40]
    print(b[2])
except ZeroDivisionError:
    print("denominator cant be zero")
except IndexError:
    print("Invalid index")