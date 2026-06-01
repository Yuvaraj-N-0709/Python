"""
name ={'yuva','praveen','kalish'}
print(name)
print(type(name))

#access values using For loop
for names in name:
    print(names)
#adding new name
name.add('sara')
print(name)

#update Another Set of Data
a={'kumar','kavin','main','jana'}
name.update(a)
print(name)
name.remove('sara')
print(name)
name.pop()
print(name)

name.clear()
print(name)

del name
print(name)

name={'kumar','kumar','kavin','main','jana','yuva','praveen','kalish'}
print(name)

a={1,2,3,4}
b={'a','b','c','d'}
c=a.union(b)
print(c)
a.update(b)
print(a)

a={1,2,3,4,5}
b={5,6,7,8,9}

c=a.intersection(b)
print(c)
a.intersection_update(b)
print(a)

c=a.symmetric_difference(b)
print(c)
a.symmetric_difference_update(b)
print(a)
"""

a={5,6,7}
b={5,6,7}
c=a.isdisjoint(b)
print(c)
c=a.issubset(b)
print(c)
c=a.issuperset(b)
print(c)

  

