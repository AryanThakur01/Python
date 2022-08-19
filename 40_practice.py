# Write a class programmer capable of storing the details of the programmers in a certain company
class Programmer:
    def __init__(self, language, name):
        self.language = language
        self.name = name


harry = Programmer("Harry", "Python")
rohan = Programmer("Rohan", "Java")

print(rohan.name)
print(harry.name)

# square, cube and square root calculator
from cmath import sqrt
import math
class calculator:
    def __init__(self, number):
        self.number = number

    def square(self):
        return self.number * self.number
    
    def cube(self):
        return self.number * self.number * self.number
    
    def squareRoot(self):
        return sqrt(self.number)

value = calculator(-25)
print(value.number)
print(value.square())
print(value.cube())
print(value.squareRoot())