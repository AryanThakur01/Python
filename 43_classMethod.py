# ClassMethod decorator
class Employee:
    a = 10
    b = 33
    c = 55
    @classmethod
    def setAttrs(cls, a, b, c):
        cls.a = a
        cls.b = b
        cls.c = c

emp = Employee()
print(Employee.a)
print(Employee.b)
print(Employee.c)
emp.setAttrs(1,2,3)
print(Employee.a)
print(Employee.b)
print(Employee.c)



#Property decorator
class Employee:
    a = 10
    b = 33
    c = 55
    @classmethod
    def setAttrs(cls, a, b, c):
        cls.a = a
        cls.b = b
        cls.c = c

    @property
    def length(self):                   #Remember to pass self in the variable even if you do not use it because the syntax requires to pass self
        return self.a +self.b +self.c
    
    @length.setter
    def length(self, value):
        self.a = value

emp = Employee()
emp.setAttrs(1,2,3)
emp.length = 111            # works because of setter decorator
print(emp.length)           # this works because of property decorator