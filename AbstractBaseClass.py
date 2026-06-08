# Abstract Base Class in Python

import abstractmethod

class Bank(ABC):
    @abstractmethod
    def loan(self): pass
     
	@abstractmethod
	def credit(self): pass
     
	@abstractmethod
	def debit(self): pass
	 
class HDFC(Bank):
       
    def loan(self):
        print("we can provide 7.5% Interest Loan")
     
    def credit(self):
        print("HDFC provide Credit")
              
    def debit(self):
        print("HDFC provide debit")
         
    def card(self):
        print("HDFC provide Credit card")
         
o=HDFC()
o.loan()
o.credit()
o.debit()
o.card()
