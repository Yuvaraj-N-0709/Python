#Tuple
#Immutable
#surrounded by Round Brackets(1,1,5)

a=(1,2.5,"yuva")
print(a)
print(type(a))
print(a[1])
print(a[-1])
print(a[0:2])
b=list(a)
print(b)
b.append("praveen")
print(b)
print(type(b))
a= tuple(b)
print(a)
print(type(a))
"""del a
print (a)/"""

for i in a:
    print(i)
    
if "yuva" in a:
    print("yuva is found")
else:
    print("not found")
print(len(a))
#single value if you will use in tuple , is importent
a=(1,)
print(type(a))

a=(1,2,3,4)
b=(5,6,7,8,9)
c=a+b
print(c)
print(c.count(2))


a=(1,2,3,4)
b=(5,6,7,8,9)
c=(a,b)
print(c)
print(c[0])
print(c[1])
print(c[0][1])

x=("yuva",)*10
print(x)

a=(1,3,5,7,9,10)
print(min(a))
print(max(a))







    
    
