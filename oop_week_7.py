class Vector:
    def __init__(self,x,y):
        self.x=x
        self.y=y
    def __add__(self,other):
        return Vector(self.x + other.x, self.y + other.y)
    def __str__(self):
        return f"({self.x },{self.y})"
v1 = Vector(2,3)
v2 = Vector(4,5)
v3 = v1 + v2
print(v3)  

class Add:
    def __init__ (self,x):
        self.x = x
    def __add__(self,other):
        return self.x - other.x
a1 = Add(10)
a2 = Add(5)
a3 = a1 + a2
print(a3)
    
        