# Write a program to display when a and b are integers. If b = 0, display infinite by handling the ZeroDivisionError
try:
    a = int(input("Enter the value of a: "))
    b = int(input("Enter the value of b: "))
    c = a/b
    print(c)

except ZeroDivisionError:
    print("infinite(oo)")