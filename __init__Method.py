#init method in python 

class user:
    def __init__(self,name):
        print("call when new Instance Created")
        self.name = name
        
    def printall(self):
        print("Name : ",self.name)
        
o1=user("Yuvaraj N")
o1.printall()
print(o1.__dict__)
o2=user("yuva")
o2.printall()
print(o2.__dict__)
print(user.__dict__)

