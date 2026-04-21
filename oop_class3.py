<<<<<<< HEAD
class Employee:
    company = "TechCorp"   
  
    def __init__(self, name, role):
        self.name = name   
        self.role = role   

emp1 = Employee("Alice", "Developer")
emp2 = Employee("Bob", "Designer")
emp3 = Employee("Charlie", "Manager")

print(emp1.company, "-", emp1.name)
print(emp2.company, "-", emp2.name)
print(emp3.company, "-", emp3.name)
    
    
class Employee:
    company = "TechCorp"
    employee_count = 0    

    def __init__(self, name, role):
        self.name = name
        self.role = role
        Employee.employee_count += 1  


emp1 = Employee("Alice", "Developer")
emp2 = Employee("Bob", "Designer")
emp3 = Employee("Charlie", "Manager")

print("Total employees:", Employee.employee_count)


class Employee:
    company = "TechCorp"
   
empA=Employee()
empB=Employee()
print("empA company:", empA.company)       
print("empB company:", empB.company)       
print("Class company:", Employee.company)  

empA.company = "NewCorp"
print("empA company:", empA.company)       
print("empB company:", empB.company)       
print("Class company:", Employee.company)  

#Create a Password class that stores a private password. Add a check_password(guess)
#method that returns True or False, but never reveals the actual password.
class Password:
    def __init__(self,password):
        self.__password=password
        
    def check(self,guess):
        if guess==self.__password:
            return True
            
=======
class Employee:
    company = "TechCorp"   
  
    def __init__(self, name, role):
        self.name = name   
        self.role = role   

emp1 = Employee("Alice", "Developer")
emp2 = Employee("Bob", "Designer")
emp3 = Employee("Charlie", "Manager")

print(emp1.company, "-", emp1.name)
print(emp2.company, "-", emp2.name)
print(emp3.company, "-", emp3.name)
    
    
class Employee:
    company = "TechCorp"
    employee_count = 0    

    def __init__(self, name, role):
        self.name = name
        self.role = role
        Employee.employee_count += 1  


emp1 = Employee("Alice", "Developer")
emp2 = Employee("Bob", "Designer")
emp3 = Employee("Charlie", "Manager")

print("Total employees:", Employee.employee_count)


class Employee:
    company = "TechCorp"
   
empA=Employee()
empB=Employee()
print("empA company:", empA.company)       
print("empB company:", empB.company)       
print("Class company:", Employee.company)  

empA.company = "NewCorp"
print("empA company:", empA.company)       
print("empB company:", empB.company)       
print("Class company:", Employee.company)  

#Create a Password class that stores a private password. Add a check_password(guess)
#method that returns True or False, but never reveals the actual password.
class Password:
    def __init__(self,password):
        self.__password=password
        
    def check(self,guess):
        if guess==self.__password:
            return True
            
>>>>>>> 3884a84 (add all files)
    