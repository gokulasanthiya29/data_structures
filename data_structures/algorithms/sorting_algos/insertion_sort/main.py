class Employee:    
    id = 10   
    name = "John"    
    def display (self):    
        print(self.id,self.name, sep="  ")    
# Creating a emp instance of Employee class  
emp = Employee()    
emp.display()  
del emp.id
emp.display()