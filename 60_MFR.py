from functools import reduce
# Map applies a function to all the items in an input.txt

square = lambda x: x*x
l = [1,3,4,5,6,7]
c = map(square, l)          # Mapping square function to all the values
print(list(c))


# Demonstration for filter
greater = lambda x: x>4
a = [1, 2, 3, 4, 54, 67, 71, 89]
d = filter(greater, a)          # only prints those elements which returns true from a list
print(list(d))

# Demonstration for reduce
sum = lambda x, y: x+y
a = [1, 2, 3, 7]
d = reduce(sum, a)
print(d)