#Multilevel inheritance in python 

class GrandFather:
    def ownhouse(self):
        print("Grandpa house")
        
class Father(GrandFather):
    def ownbike(self):
        print("Father's bike")
        
class Son(Father):
    def ownbook(self):
        print("son have a book")
        
o=Son()
o.ownbike()
o.ownbook()
o.ownhouse()
