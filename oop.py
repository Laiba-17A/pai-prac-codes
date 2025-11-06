
# ============================================================
# 🧠 PYTHON OOP (OBJECT-ORIENTED PROGRAMMING) FULL CONCEPTS
# ============================================================

print("========== PYTHON OOP CONCEPTS ==========\n")

# ============================================================
# 1️⃣ CLASS AND OBJECT
# ============================================================

class Student:
    # class attribute (shared by all objects)
    school_name = "City High School"

    # constructor (special method)
    def __init__(self, name, age):
        self.name = name      # instance variable
        self.age = age

    # instance method
    def display(self):
        print(f"Student Name: {self.name}, Age: {self.age}, School: {Student.school_name}")

# creating objects
s1 = Student("Ali", 18)
s2 = Student("Sara", 17)
print("=== CLASS AND OBJECT ===")
s1.display()
s2.display()

# ============================================================
# 2️⃣ ENCAPSULATION (Hiding Data)
# ============================================================

class Account:
    def __init__(self, owner, balance):
        self.owner = owner
        self.__balance = balance   # private attribute

    def deposit(self, amount):
        self.__balance += amount

    def withdraw(self, amount):
        if amount <= self.__balance:
            self.__balance -= amount
        else:
            print("Insufficient balance!")

    def show_balance(self):
        print(f"{self.owner}'s Balance: {self.__balance}")

print("\n=== ENCAPSULATION ===")
acc = Account("Ahmed", 5000)
acc.show_balance()
acc.deposit(2000)
acc.show_balance()
acc.withdraw(8000)

# Try accessing private var directly
# print(acc.__balance)  # ❌ will give error
# correct way:
print("Access private balance:", acc._Account__balance)  # Not recommended but possible

# ============================================================
# 3️⃣ INHERITANCE
# ============================================================

class Person:
    def __init__(self, name):
        self.name = name

    def speak(self):
        print(f"{self.name} can speak")

# Single inheritance
class Employee(Person):
    def __init__(self, name, emp_id):
        super().__init__(name)     # call parent constructor
        self.emp_id = emp_id

    def show_info(self):
        print(f"Employee: {self.name}, ID: {self.emp_id}")

print("\n=== INHERITANCE ===")
emp1 = Employee("Zain", 101)
emp1.speak()
emp1.show_info()

# Multiple Inheritance
class Manager:
    def manage(self):
        print("Manages team and resources")

class TechLead(Employee, Manager):
    def lead_project(self):
        print(f"{self.name} leads the technical project")

print("\n=== MULTIPLE INHERITANCE ===")
tl = TechLead("Laiba", 205)
tl.show_info()
tl.manage()
tl.lead_project()

# ============================================================
# 4️⃣ POLYMORPHISM (Same function name, different behavior)
# ============================================================

class Bird:
    def sound(self):
        print("Birds make sounds")

class Sparrow(Bird):
    def sound(self):
        print("Sparrow chirps")

class Parrot(Bird):
    def sound(self):
        print("Parrot talks")

print("\n=== POLYMORPHISM ===")
for bird in [Sparrow(), Parrot()]:
    bird.sound()  # same method name -> different behavior

# ============================================================
# 5️⃣ ABSTRACTION (Hiding implementation details)
# ============================================================

from abc import ABC, abstractmethod

class Vehicle(ABC):
    @abstractmethod
    def start_engine(self):
        pass

class Car(Vehicle):
    def start_engine(self):
        print("Car engine started!")

print("\n=== ABSTRACTION ===")
car1 = Car()
car1.start_engine()

# ============================================================
# 6️⃣ CLASS METHODS AND STATIC METHODS
# ============================================================

class EmployeeRecord:
    company = "TechCorp"

    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    # instance method
    def show(self):
        print(f"{self.name} earns {self.salary} at {EmployeeRecord.company}")

    # class method (works with class data)
    @classmethod
    def change_company(cls, new_name):
        cls.company = new_name

    # static method (no self or cls)
    @staticmethod
    def greet():
        print("Welcome to the company!")

print("\n=== CLASS & STATIC METHODS ===")
empA = EmployeeRecord("Ali", 80000)
empA.show()
EmployeeRecord.greet()
EmployeeRecord.change_company("FutureTech")
empA.show()

# ============================================================
# 7️⃣ MAGIC METHODS (Dunder Methods)
# ============================================================

class Box:
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def __str__(self):
        return f"Box({self.length} x {self.width})"

    def __add__(self, other):
        return Box(self.length + other.length, self.width + other.width)

print("\n=== MAGIC METHODS ===")
b1 = Box(2, 3)
b2 = Box(4, 5)
print("Box 1:", b1)
print("Box 2:", b2)
print("Box after + :", b1 + b2)

# ============================================================
# 8️⃣ COMPOSITION (HAS-A relationship)
# ============================================================

class Engine:
    def start(self):
        print("Engine started")

class Car:
    def __init__(self):
        self.engine = Engine()  # Car HAS-A Engine

    def drive(self):
        self.engine.start()
        print("Car is moving")

print("\n=== COMPOSITION ===")
c = Car()
c.drive()

# ============================================================
# 9️⃣ PROPERTY DECORATOR (Getter, Setter)
# ============================================================

class Circle:
    def __init__(self, radius):
        self._radius = radius

    @property
    def radius(self):
        return self._radius

    @radius.setter
    def radius(self, value):
        if value > 0:
            self._radius = value
        else:
            print("Radius must be positive!")

    @property
    def area(self):
        return 3.14 * self._radius ** 2

print("\n=== PROPERTY DECORATOR ===")
circle = Circle(5)
print("Radius:", circle.radius)
print("Area:", circle.area)
circle.radius = 10
print("New Radius:", circle.radius)
print("New Area:", circle.area)

# ============================================================
# 🔟 OOP COMBINATION EXAMPLE
# ============================================================

print("\n=== OOP COMBINATION EXAMPLE ===")

class Library:
    def __init__(self, name):
        self.name = name
        self.books = []

    def add_book(self, book):
        self.books.append(book)

    def show_books(self):
        print(f"\nLibrary '{self.name}' has books:")
        for b in self.books:
            print("-", b.title, "by", b.author)

class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author

lib = Library("City Library")
b1 = Book("Python Basics", "Hasan Javed")
b2 = Book("Data Science 101", "Laiba Noor")

lib.add_book(b1)
lib.add_book(b2)
lib.show_books()

print("\n✅ All OOP concepts executed successfully!")
