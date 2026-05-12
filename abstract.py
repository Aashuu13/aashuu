from abc import ABC,abstractmethod
class Shape(ABC):
    @abstractmethod
    def area(self):
        pass
    def desc(self):
        print("describe")

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        print("area")

    
class Square(Shape):
    def __init__(self,length):
       self.length=length   
    def area(self):
        print("area of square")
     
c = Circle(5)
c.desc()
print(c.area())
s=Square(4)
s.desc()
print(s.area()) 
