#Function overriding in python 

class Employee:
    def workingHrs(self):
        self.hrs = 50
        
    def printHrs(self):
        print("Total Working Hrs : ",self.hrs)
        
class Trainee(Employee):
    def workingHrs(self):
        self.hrs = 60
        
    def resetHrs(self):
        super().workingHrs()
        
E=Employee()
E.workingHrs()
E.printHrs()

T=Trainee()
T.workingHrs()
T.printHrs()
T.resetHrs()
T.printHrs()

