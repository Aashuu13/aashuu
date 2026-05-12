class Shape:
    def area(self):
        return 0
    def describe(self):
        return f"This is a shape with area {self.area()}"

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius
    def area(self):
        return 3.14159 * self.radius ** 2

class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height
    def area(self):
        return self.width * self.height

def showArea(shape):
    print(f"The area of the shape is: {shape.area()}")

shapes = [Circle(5), Rectangle(4, 6)]
for shape in shapes:
    showArea(shape)
    print(shape.describe())
    
    
#Week 7 Polymorphism 
# Practice Exercises
# Exercise 1: Vehicle Sounds
# Create classes Car, Motorcycle, and Truck, each with a honk() method. Loop through a list of vehicles and call honk() on each.

class Car:
    def honk(self):
        print("Car says: Beep beep!")

class Motorcycle:
    def honk(self):
        print("Motorcycle says: Meep meep!")

class Truck:
    def honk(self):
        print("Truck says: HONK HONK!")

# Polymorphism in action
vehicles = [Car(), Motorcycle(), Truck()]

for v in vehicles:
    v.honk()   # same call, different behavior


# Exercise 2: Shape Describer
# Create classes Circle, Square, and Triangle, each with a describe() method that returns a string like "I am a circle." Write a
# function that accepts any shape and prints its description.

class Circle:
    def describe(self):
        return "I am a circle."

class Square:
    def describe(self):
        return "I am a square."

class Triangle:
    def describe(self):
        return "I am a triangle."
def describe_shape(shape):
    print(shape.describe())     
  
  
    
class Triangle:
    def describe(self):
        return "I am a triangle."

shapes=[Circle(),Square(),Triangle()]

for shape in shapes:
    print(shape.describe())

# Exercise 3: File Exporters
# Create classes CSVExporter, JSONExporter, and PDFExporter, each with an export(data) method that prints which format the data is
# being exported as.

class CSVExporter:
    def export(self, data):
        print(f"Exporting data as CSV: {data}")

class JSONExporter:
    def export(self, data):
        print(f"Exporting data as JSON: {data}")

class PDFExporter:
    def export(self, data):
        print(f"Exporting data as PDF: {data}")

exporters=[CSVExporter(),JSONExporter(),PDFExporter()]

# Test
data = {"name": "Shivanz", "age": 18}

for exporter in exporters:
    exporter.export(data)
            
        