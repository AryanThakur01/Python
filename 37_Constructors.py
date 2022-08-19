class Employee:
    center = "Unknown"
    def __init__(self, name , marks, center):           # We can also replace the self with some other variable name but we are supposed to use that variable at all places in place of self
        self.name = name
        self.marks = marks
        self.center = center

    def printObj(self):
        print(f"The name is {self.name}")
        print(f"The marks is {self.marks}")
        print(f"The center is {self.center}")
    
    @staticmethod
    def greet():
        print("good day")

harry = Employee("Harry", 34, "Delhi")
rohan = Employee("Rohan", 96, "Kolkata")
harry.printObj()
rohan.printObj()