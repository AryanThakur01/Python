'''Single Inheritance'''
class Employee:
    a = 44


class Programmer(Employee):
    b = 34


pr = Programmer()
print(pr.a)
print(pr.b)

pr = Employee()
print(pr.a)
# print(pr.b)           # This line will throw an error



'''Multiple Inheritance'''

class Parent1:
    a = 12

class Parent2:
    b = 1233

class child(Parent1, Parent2):
    c = 164

ch = child()
print(ch.a)
print(ch.b)
print(ch.c)


'''Multilevel Inheritance'''
class Parent:
    a = 6

class Child1(Parent):
    b = 66

class Child2(Child1):
    c = 636

ch = Child2()
print(ch.a)
print(ch.b)
print(ch.c)




'''Super'''
class Parent:
    a = 6
    def __init__(self) -> None:
        print("Parent")

class Child1(Parent):
    b = 66
    def __init__(self) -> None:
        super().__init__()                  #this is to call the constructor of child 1
        print("Child1")

class Child2(Child1):
    c = 636
    def __init__(self) -> None:
        super().__init__()                  #this is to call the constructor of child 1
        print("Child2")

ch = Child2()