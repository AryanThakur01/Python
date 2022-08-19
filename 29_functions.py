# # Dry Principle
# # Functions and recursions
'''
# Types of functions:
    1. Built in function
    2. User defined functions
'''


# def func1():
#     print("Hello Harry")
#     print("You are the best")
#     print("I am another function\n")


# func1()


'''Functions with arguments'''


def average(a, b, c):
    return (a + b + c) / 3


print("The average of 1, 41, 2 is:",average(1, 41, 2))


def greet(name = "Harry"):      # harry is the default argument of the greet function
    return "Hello "+name

# print(greet("shubh"))
print(greet())