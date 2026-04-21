#lesson 1
#Create a Vehicle class with a brand attribute and a honk() method. Then create a Car class that inherits from it and test calling honk() on a Car object.
class Vehicle:
    def __init__(self, brand):
        self.brand = brand
        
    def honk(self):
        print(f"{self.brand} goes honk!")
class Car(Vehicle):
    def __init__(self, brand):
        super().__init__(brand) 
car1 = Car("Toyota")
car1.honk()
#2. Create a Person class with name and age . Create a Student class that inherits from Person using pass . Verify the student can access name and age.
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age  
class Student(Person):
    pass
student1 = Student("Aashu",19)
print(f"Student Name: {student1.name}, Age: {student1.age}")
#3. Create a Phone class with a call() method. Create Smartphone that inherits from Phone. Does the smartphone have the call method without writing any extra code?
class Phone:
    def call(self):
        print("tapaile samparka gardai hunu hunxa")
class Smartphone(Phone):
    pass
smartphone1 = Smartphone()
smartphone1.call()  

#lesson 2
#1. Create a Person class with name and age . Create a Teacher child class that adds a subject attribute and a teach() method.
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
class Teacher(Person):
    def __init__(self, name, age, subject):
        super().__init__(name, age)
        self.subject = subject
        
    def teach(self):
        print(f"{self.name} teaches {self.subject}")
teacher1 = Teacher("Mr. Smith", 40, "Math")
teacher1.teach()
#Create a Shape class with color . Create a Circle class that adds radius and an area() method. Print the color and area.
class Shape:
    def __init__(self, color):
        self.color = color

class Circle(Shape):
    def __init__(self, color, radius):
        super().__init__(color)
        self.radius = radius

    def area(self):
        import math
        return math.pi * (self.radius ** 2)

my_Circle = Circle("Red", 5)
print(f"Color: {my_Circle.color}, Area: {my_Circle.area()}")

#3. Create a Vehicle class with brand and year. Create a Truck class that adds payload_capacity and a load() method.
class Vehicle:
    def __init__(self, brand, year):
        self.brand =brand
        self.year = year

class Truck(Vehicle):
    def __init__(self, brand, year, payload_cap):
        super().__init__(brand, year)
        self.payload_cap = payload_cap
    def load(self):
        return f"{self.brand} truck can load {self.payload_cap} tons"

my_truck = Truck("Ford", 2020, 10)
print(my_truck.load())

#1. Create a Shape class with an info() method that returns "I am a shape". Create Circle and Square children that override info() with their own messages.
class Shape:
    def info(self):
        return "I am a shape"
    
class Circle(Shape):
    def info(self):
        return "I am a circle"
class Square(Shape):
    def info(self):
        return "I am a square"
    
circle = Circle()
square = Square()
print(circle.info())
print(square.info())

#2. Create a Vehicle class with a fuel_type() method returning "Unknown". Override it in ElectricCar to return "Electric" and in GasCar to return "Gasoline".
class Vehicle:
    def fuel_type(self):
        return "Unknown"
    
class ElectricCar(Vehicle):
    def fuel_type(self):
        return "Electric"
class GasCar(Vehicle):
    def fuel_type(self):
        return "Gasoline"
    
electric_car = ElectricCar()
gas_car = GasCar()
print(electric_car.fuel_type())
print(gas_car.fuel_type())

#3. Create a Person class with a greet() method. Create a FormalPerson that does a partial override, calling super().greet() and adding "Pleased to meet you."
class Person:
    def greet(self):
        return "Hello!"

class FormalPerson(Person):
    def greet(self):
        return super().greet() + " Pleased to meet you."
    
formal_person = FormalPerson()
print(formal_person.greet())

#1. Create a Product class with name and price. Create an Electronics child that adds warranty_years using super().
class Product:
    def __init__(self, name, price):
        self.name = name
        self.price = price

class Electronics(Product):
    def __init__(self, name, price, warranty_years):
        super().__init__(name, price)
        self.warranty_years = warranty_years

my_electronic = Electronics("Laptop", 1000, 2)
print(f"Product: {my_electronic.name}, Price: {my_electronic.price}, Warranty: {my_electronic.warranty_years} years")

#2. Create a Bird class with a describe() method. Create a Parrot child that uses super().describe() and adds "and I can talk!".
class Bird:
    def describe(self):
        return "I am a bird"

class Parrot(Bird):
    def describe(self):
        return super().describe() + " and I can talk!"
    
my_parrot = Parrot()
print(my_parrot.describe())

#3. Create a Account class with a display() method. Create a SavingsAccount that extends display() using super() to also show the interest rate.
class Account:
    def __init__(self, account_number):
        self.account_number = account_number
    def display(self):
        return f"Account Number: {self.account_number}"

class SavingsAccount(Account):
    def __init__(self, account_number, interest_rate):
        super().__init__(account_number)
        self.interest_rate = interest_rate
    def display(self):
        return super().display() + f", Interest Rate: {self.interest_rate}%"
    
my_savings = SavingsAccount("123456789", 1.5)
print(my_savings.display())

#1. Create a multilevel chain: Vehicle to Car to ElectricCar. Each level adds one method. Test that ElectricCar can call all three.
class Vehicle:
    def start_engine(self):
        return "Engine started"
    
class Car(Vehicle):
    def drive(self):
        return "Car is driving"
class ElectricCar(Car):
    def charge(self):
        return "Car is charging"
    
my_electric_car = ElectricCar()
print(my_electric_car.start_engine())
print(my_electric_car.drive())
print(my_electric_car.charge())

#2. Create hierarchical inheritance: Shape as parent, with Circle, Rectangle, and Triangle as children. Each child has its own area() method.
class Shape:
    def area(self):
        return "Area not defined for generic shape"
    
class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius
    def area(self):
        import math
        return math.pi * (self.radius ** 2)
class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height
    def area(self):
        return self.width * self.height
class Triangle(Shape):
    def __init__(self, base, height):
        self.base = base
        self.height = height
    def area(self):
        return 0.5 * self.base * self.height
    
circle = Circle(5)
rectangle = Rectangle(4, 6)
triangle = Triangle(4, 5)
print(f"Circle Area: {circle.area()}")
print(f"Rectangle Area: {rectangle.area()}")
print(f"Triangle Area: {triangle.area()}")

#3. Identify which type of inheritance would be best for: (a) a school system with Teacher and Student, (b) a file system with File to TextFile to EncryptedTextFile, (c) a game with Character having Warrior, Mage, and Archer children.
# (a) For a school system with Teacher and Student, hierarchical inheritance would be best, with a common parent class (e.g., Person) that both Teacher and Student inherit from.
# (b) For a file system with File to TextFile to EncryptedTextFile,
#multilevel inheritance would be best, where File is the parent class, TextFile inherits from File, and EncryptedTextFile inherits from TextFile.
# (c) For a game with Character having Warrior, Mage, and Archer children, hierarchical inheritance would be best, with Character as the parent class and Warrior, Mage, and Archer as child classes that inherit from Character.

#Extend the Employee system: add an Intern class with a university attribute and override get_info()
    
    

       
    
