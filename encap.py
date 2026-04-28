
class BankAccount:
    def __init__(self, balance=0):
        self.__balance = balance

    def deposit(self, amount):
        self.__balance += amount

    def withdraw(self, amount):
        if amount > self.__balance:
            print("Insufficient funds. Withdrawal denied.")
        else:
            self.__balance -= amount

    def get_balance(self):
        return self.__balance

    def transfer(self, other_account, amount):
        if amount > self.__balance:
            print("Insufficient funds. Transfer denied.")
        else:
            self.withdraw(amount)
            other_account.deposit(amount)
account1 = BankAccount(100)
account2 = BankAccount(50)
account1.transfer(account2, 30)
print(account1.get_balance())  # This will print 70
print(account2.get_balance())  # This will print 80

class Library:
    def __init__(self):
        self.__books = []

    def add_book(self, title):
        self.__books.append(title)

    def remove_book(self, title):
        if title in self.__books:
            self.__books.remove(title)
        else:
            print("Book not found in the library.")

    def search_by_title(self, title):
        return title in self.__books
library = Library()
library.add_book("The Great Gatsby")
print(library.search_by_title("The Great Gatsby"))  # This will print True
library.remove_book("The Great Gatsby")


class Inventory:
    def __init__(self):
        self.__stock = {}

    def add_stock(self, item, quantity):
        if item in self.__stock:
            self.__stock[item] += quantity
        else:
            self.__stock[item] = quantity

    def sell_item(self, item, quantity):
        if item not in self.__stock or self.__stock[item] < quantity:
            print("Insufficient stock. Sale denied.")
        else:
            self.__stock[item] -= quantity

    @property
    def total_items_in_stock(self):
        return sum(self.__stock.values())
inventory = Inventory()
inventory.add_stock("Widget", 100)
inventory.sell_item("Widget", 30)

class BankAccount:
    def __init__(self, balance=0):
        self.__balance = balance

    def deposit(self, amount):
        self.__balance += amount

    def withdraw(self, amount):
        if amount > self.__balance:
            print("Insufficient funds. Withdrawal denied.")
        else:
            self.__balance -= amount

    def get_balance(self):
        return self.__balance

    def transfer(self, other_account, amount):
        if amount > self.__balance:
            print("Insufficient funds. Transfer denied.")
        else:
            self.withdraw(amount)
            other_account.deposit(amount)
account1 = BankAccount(100)
account2 = BankAccount(50)
account1.transfer(account2, 30)
print(account1.get_balance())  # This will print 70
print(account2.get_balance())  # This will print 80

class Library:
    def __init__(self):
        self.__books = []

    def add_book(self, title):
        self.__books.append(title)

    def remove_book(self, title):
        if title in self.__books:
            self.__books.remove(title)
        else:
            print("Book not found in the library.")

    def search_by_title(self, title):
        return title in self.__books
library = Library()
library.add_book("The Great Gatsby")
print(library.search_by_title("The Great Gatsby"))  # This will print True
library.remove_book("The Great Gatsby")


class Inventory:
    def __init__(self):
        self.__stock = {}

    def add_stock(self, item, quantity):
        if item in self.__stock:
            self.__stock[item] += quantity
        else:
            self.__stock[item] = quantity

    def sell_item(self, item, quantity):
        if item not in self.__stock or self.__stock[item] < quantity:
            print("Insufficient stock. Sale denied.")
        else:
            self.__stock[item] -= quantity

    @property
    def total_items_in_stock(self):
        return sum(self.__stock.values())
inventory = Inventory()
inventory.add_stock("Widget", 100)
inventory.sell_item("Widget", 30)

print(inventory.total_items_in_stock)  # This will print 70