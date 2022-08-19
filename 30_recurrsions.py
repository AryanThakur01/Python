# Factorial calculation
from pickle import NONE


def factorial(num):
    if(num == 0):
        return 1
    elif(num<0):
        return "Factorial of a negetive number is not possible"
    return num*factorial(num-1)

print(factorial(10))