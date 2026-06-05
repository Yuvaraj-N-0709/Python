#MultipleInheritance in python 

class Father:
    def fishing(self):
      print("Fishing in rivers")
      
    def chess(self):
        print("playing chess from Father")

  
class Mother:
    def cooking(self):
        print("cooking food")
        
    def chess(self):
        print("playing chess from Mother")
    
class Son(Father,Mother):
    def ride(self):
        print("Riding Biycycle")
        
a=Son()
a.ride()
a.fishing()
a.cooking()
a.chess()
