# Create a class C2dVector and use it to create another class representing a 3-d Vector
from typing import List
from unicodedata import name


class Vector2d:
    def __init__(self, x, y) -> None:
        self.x = x
        self.y = y

    @property
    def displayVector(self):
        print(f"2D Vector representation: {self.x}î + {self.y}Ĵ")


class Vector3d(Vector2d):
    def __init__(self, x, y, z) -> None:
        super().__init__(x, y)
        self.z = z

    @property
    def displayVector(self):
        print(f"3D Vector representation: {self.x}î + {self.y}Ĵ + {self.z}k")


a = Vector2d(12, 21)
a.displayVector

b = Vector3d(23, 43, 54)
b.displayVector


# Create a class pets from a class Animals and further creqatr class Dog from Pets. Add a method bark to class
class Animals:
    def __init__(self, name):
        self.name = name

    def displayAnimalName(self):
        print(f"Animal name is: {self.name}")


class Pets(Animals):
    def __init__(self, animalName) -> None:
        super().__init__(animalName)
        self.animalName = animalName


class dog(Pets):
    def __init__(self, animalName) -> None:
        super().__init__(animalName)
        self.animalName = animalName

    @property
    def bark(self):
        print("The dog makes bhau bhau sound")


Spike = dog("spike")
Spike.bark


'''
Create a class Employee and add salary and increment properties to it
Write a method salaryAfterIncrement method with a @property decorator with a setter which changes the value of increment based on the salary
'''


class Employee:
    def __init__(self, name,  salary, increment) -> None:
        self.name = name
        self.salary = salary
        self.increment = increment

    @property
    def salaryAfterIncrement(self):
        print(f"The salary of {self.name} is: {self.salary+self.increment}")

    @salaryAfterIncrement.setter
    def salaryAfterIncrement(self, increment):
        self.increment =  increment
        print(f"The salary after the increment is: {self.salary + self.increment}")

Aman = Employee("Aman", 10000000, 10000)
Aman.salaryAfterIncrement
Aman.salaryAfterIncrement = 11000
