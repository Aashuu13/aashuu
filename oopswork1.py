# 1. Fruit class
class Fruit:
    pass

fruit1 = Fruit()
fruit1.name = "Apple"

fruit2 = Fruit()
fruit2.name = "Banana"

fruit3 = Fruit()
fruit3.name = "Mango"

print("Fruits:")
print(fruit1.name)
print(fruit2.name)
print(fruit3.name)


# 2. Phone class
class Phone:
    pass

phone1 = Phone()
phone1.brand = "iPhone"

phone2 = Phone()
phone2.brand = "Samsung"

print("\nPhone Type Checking:")
print(type(phone1))
print(type(phone2))
print(isinstance(phone1, Phone))
print(isinstance(phone2, Phone))


# 3. Color class
class Color:
    pass

color1 = Color()
color1.name = "Red"

color2 = Color()
color2.name = "Blue"

# Change only one object
color1.name = "Green"

print("\nColors:")
print("color1:", color1.name)
print("color2:", color2.name)



# 1. Book class
class Book:
    pass

book1 = Book()
book1.title = "Atomic Habits"
book1.author = "James Clear"
book1.pages = 320

book2 = Book()
book2.title = "Rich Dad Poor Dad"
book2.author = "Robert Kiyosaki"
book2.pages = 336

print("Books:")
print(book1.title, "-", book1.author, "-", book1.pages)
print(book2.title, "-", book2.author, "-", book2.pages)


# 2. Pet class
class Pet:
    pass

pet1 = Pet()
pet1.name = "Buddy"
pet1.age = 2

print("\nPet before change:")
print(pet1.name, "-", pet1.age)

# Modify age
pet1.age = 3

print("Pet after change:")
print(pet1.name, "-", pet1.age)


# 3. Product class
class Product:
    pass

product1 = Product()
product1.name = "Laptop"
product1.price = 800
product1.quantity = 2

product2 = Product()
product2.name = "Phone"
product2.price = 500
product2.quantity = 3

print("\nProduct Total Values:")
print(product1.name, "Total =", product1.price * product1.quantity)
print(product2.name, "Total =", product2.price * product2.quantity)