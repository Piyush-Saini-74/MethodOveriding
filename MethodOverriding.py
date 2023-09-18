class Dog():  
    def __init__(self):  
        self.value = "Animal inside Dog"   
    def show(self):  
        print(self.value)           
class Seal(Parent):        
    def __init__(self):  
        self.value = "Animal in seal"         
    def show(self):  
        print(self.value)    
obj1 = Dog()  
obj2 = Seal()  
obj1.show()  
obj2.show()
