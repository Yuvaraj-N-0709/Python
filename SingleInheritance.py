#Single inheritance in python

class jio:
    company="jio india"
    website="www.jio-india.com"
    
    def contact_details(self):
        print("Address : karur,tamil nadu,india")
        
class jio123(jio):
    def __init__(self):
        self.name ="jio 123"
        self.year = 2000
        
    def product_details(self):
        print("Name    : ", self.name)
        print("Year    : ", self.year)
        print("company : ", self.company)
        print("Website : ",self.website)
        
mobile=jio123()
mobile.product_details()
mobile.contact_details()
