class Dog:
    name="buddy"
    breed="labrador"
    eat="food"
    def noise(self,sound):
        self.sound=sound
        print(f'{self.name} says {sound}')
    def eat(self,eat):
        self.eat=eat 
           
        print(f"{self.name} eats {self.eat}")
dog1=Dog()
dog1.name="max"
dog1.noise('bark1')        
dog1.eat("pedigree")
dog2=Dog()
dog2.name="max2"
dog2.noise('bark2')
dog2.eat('pedigree2')


class Greeter:
    name=""
    
    def greet(self,greet):
        self.greet=greet
        print(f"{self.greet} My name is {self.name}")
    
p1=Greeter()
p1.name="shivanz"
p1.greet("hello")        


class Rectangle:
    width=0
    height=0
    def area(self,width,height):
        self.width=width
        self.height=height
        area=width*height
        return area
    
rect1=Rectangle()
rect1.width=5
rect1.height=3
print(f"Area of rectangle: {rect1.area(5,3)}")    
           
        
        
        
class BankAccount:
    balance = 0

    def deposit(self, amount):
        self.balance += amount

    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
            print(f"Withdrew ${amount}. Balance: ${self.balance}")
        else:
            print("Insufficient funds.")
    
    def check_balance(self):
        print(f"Current balance: ${self.balance}")

acc = BankAccount()
acc.deposit(1000)     # Deposited $1000. Balance: $1000
acc.check_balance()

class Book:
    def __init__(self,title,author,pages):
        self.tite=title
        self.author=author
        self.pages=pages
b1=Book("Atomic Habits","James Clear",320)
b2=Book("Rich Dad Poor Dad","Robert Kiyosaki",336)
print(f"Book 1: {b1.tite} by {b1.author}, {b1.pages} pages")
print(f"Book 2: {b2.tite} by {b2.author}, {b2.pages} pages")


class Car:
    def __init__(self,color="White"):
        self.color=color
car1=Car("blue")
car2=Car()
print(f"Car 1 color: {car1.color}")
print(f"Car 2 color: {car2.color}")

class Rectangle:
    def __init__(self,width,height):
        self.width=width
        self.height=height
    def area(self):
        return self.width*self.height
rectangle1=Rectangle(5,3)
print(f"Area of rectangle: {rectangle1.area()}")    
        

                            
        
         
         