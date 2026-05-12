class Animal:
    def speak(self):
        raise NotImplementedError("Subclass must implement this method")

class Dog(Animal):
    def speak(self):
        return "Woof"

class Cat(Animal):
    def speak(self):
        return "Meow"


# Testing
dog = Dog()
cat = Cat()

print(dog.speak())  # Woof
print(cat.speak())  # Meow


class Shape:
    def area(self):
        raise NotImplementedError

    def perimeter(self):
        raise NotImplementedError


class Rectangle(Shape):
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def area(self):
        return self.length * self.width

    def perimeter(self):
        return 2 * (self.length + self.width)


# Testing
rect = Rectangle(5, 3)

print("Area:", rect.area())          # 15
print("Perimeter:", rect.perimeter())  # 16


#Exercise 3: Everyday Abstraction

# Here are 3 examples:

# 1. ATM Machine
# Exposes: Withdraw, deposit, check balance
# Hides: Banking server logic, transaction processing, security systems
# 2. Smartphone
# Exposes: Apps, touch interface, camera
# Hides: OS internals, memory management, hardware communication
# 3. Car
# Exposes: Steering wheel, pedals, gear shift
# Hides: Engine mechanics, fuel injection system, transmission system


from abc import ABC, abstractmethod
import math

class Shape(ABC):
    
    @abstractmethod
    def area(self):
        pass

    @abstractmethod
    def perimeter(self):
        pass


class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return math.pi * self.radius ** 2

    def perimeter(self):
        return 2 * math.pi * self.radius


class Rectangle(Shape):
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def area(self):
        return self.length * self.width

    def perimeter(self):
        return 2 * (self.length + self.width)


class Triangle(Shape):
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c

    def area(self):
        # Heron's Formula
        s = (self.a + self.b + self.c) / 2
        return (s * (s - self.a) * (s - self.b) * (s - self.c)) ** 0.5

    def perimeter(self):
        return self.a + self.b + self.c


# Testing
c = Circle(3)
r = Rectangle(4, 5)
t = Triangle(3, 4, 5)

print(c.area(), c.perimeter())
print(r.area(), r.perimeter())
print(t.area(), t.perimeter())

from abc import ABC, abstractmethod

class Employee(ABC):
    
    def __init__(self, name, id):
        self.name = name
        self.id = id

    @abstractmethod
    def calculate_salary(self):
        pass

    def display_info(self):
        print(f"Name: {self.name}, ID: {self.id}")


class FullTime(Employee):
    def __init__(self, name, id, monthly_salary):
        super().__init__(name, id)
        self.monthly_salary = monthly_salary

    def calculate_salary(self):
        return self.monthly_salary


class PartTime(Employee):
    def __init__(self, name, id, hours, rate):
        super().__init__(name, id)
        self.hours = hours
        self.rate = rate

    def calculate_salary(self):
        return self.hours * self.rate


# Testing
emp1 = FullTime("Aashu", 101, 50000)
emp2 = PartTime("Ram", 102, 20, 500)

emp1.display_info()
print("Salary:", emp1.calculate_salary())

emp2.display_info()
print("Salary:", emp2.calculate_salary())


from abc import ABC, abstractmethod

class Notifier(ABC):

    @abstractmethod
    def send(self, message):
        pass


class EmailNotifier(Notifier):
    def send(self, message):
        print(f"Sending Email: {message}")


class SMSNotifier(Notifier):
    def send(self, message):
        print(f"Sending SMS: {message}")


class PushNotifier(Notifier):
    def send(self, message):
        print(f"Sending Push Notification: {message}")


# Testing
notifiers = [
    EmailNotifier(),
    SMSNotifier(),
    PushNotifier()
]

for notifier in notifiers:
    notifier.send("Hello User!")
    
    
from abc import ABC, abstractmethod

class Drawable(ABC):

    @abstractmethod
    def draw(self):
        pass


class Circle(Drawable):
    def draw(self):
        print("Drawing a Circle")


class Square(Drawable):
    def draw(self):
        print("Drawing a Square")


class Triangle(Drawable):
    def draw(self):
        print("Drawing a Triangle")


# Testing
shapes = [Circle(), Square(), Triangle()]

for shape in shapes:
    shape.draw()
    
from abc import ABC, abstractmethod

class Readable(ABC):

    @abstractmethod
    def read(self):
        pass


class Writable(ABC):

    @abstractmethod
    def write(self, data):
        pass


class TextFile(Readable, Writable):
    
    def __init__(self, content=""):
        self.content = content

    def read(self):
        return self.content

    def write(self, data):
        self.content += data


# Testing
file = TextFile()

file.write("Hello ")
file.write("World!")

print(file.read())  # Hello World!

from abc import ABC, abstractmethod

class Plugin(ABC):

    @abstractmethod
    def activate(self):
        pass

    @abstractmethod
    def deactivate(self):
        pass


class AudioPlugin(Plugin):
    def activate(self):
        print("Audio Plugin Activated")

    def deactivate(self):
        print("Audio Plugin Deactivated")


class VideoPlugin(Plugin):
    def activate(self):
        print("Video Plugin Activated")

    def deactivate(self):
        print("Video Plugin Deactivated")


# Testing
plugins = [AudioPlugin(), VideoPlugin()]

for plugin in plugins:
    plugin.activate()

for plugin in plugins:
    plugin.deactivate()        