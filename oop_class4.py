# class Animal:
#     def sound(self):
#         print("makes sound")

# class Dog(Animal):
#     pass
# class Cow(Animal):
#     pass

# bd=Dog()
# bd.sound()
# c=Cow()
# c.sound()
        
        
# class Animal:
#     def __init__(self,name):
#       self.name=name
#     def sound(self):
#         print(f"{self.name} makes sound")

# class Dog(Animal):
#     pass
# class Cow(Animal):
#     pass

# bd=Dog("max")
# bd.sound()
# c=Cow("laxmi")
# c.sound()
 
       
class Animal:
    def __init__(self,name,breed):
      self.name=name
      self.breed=breed
    def sound(self):
        print(f"{self.name} makes sound")

class Dog(Animal):
    def __init__(self,name,breed):
        super().__init__( name,breed)
    def eat(self):
        print(f"{self.name} eats meat")
    def sound(self):
        print(f"{self.name} bhau bhau")
class Cow(Animal):
    def __init__(self,name,breed):
        super().__init__( name,breed)
    def eat(self):
        print(f"{self.name} eats grass")
    def sound(self):
        print(f"{self.name} baa baa")
bd=Dog("max","lab")
bd.sound()
bd.eat() 
c=Cow("asteroid destroyer","holstein") 
c.sound()