# Class
# A very basic sample class
class Employee:
    name = "Harry"
    marks = "34"
    center = "Delhi"


harry = Employee()      # A basic object
print(harry.name)
print(harry.marks)
print(harry.center)


# Class Methods
class Employee:
    name = "Harry"  # A class attribute
    marks = "34"
    center = "Delhi"

    def printObj(self):  # selfqoricasdf can also be used in place of self
        print(f"The name is {self.name}")
    
    @staticmethod               # this will not need any of the object
    def greet():
        print("good day")


harry = Employee()
harry.printObj()  # Employee printObj(harry)


# Modelling a problem in OOP
'''
Noun -> Class -> Employee
Adjective -> Attributes -> name, age, salary
Verb -> Methods -> getSalary(), income()
'''

# Class Attributes
Employee.name = "HarryNew"      # Setting a class attribute for Employee
shyam = Employee()
print(shyam.name)
shyam.name = "Shyam"            # Setting an instance attribute to shyam
print(shyam.name)

harry.greet()
Employee.greet()