# myTuple = (3, 5, 2, 1, 5)
# A "," is needed to make a tuple with a single element
myTuple = (2,)
print(myTuple)
# myTuple[0] = 12           #This will throw an error because a tuple is immutable
print(type(myTuple))


# Tuple Methods
a = (1, 2, 3, 3, 3, 4, 5, 6, 7)
print(a.count(3))           # counts the number of a digit in a tuple
print(a.index(4))           # gives first occurence
