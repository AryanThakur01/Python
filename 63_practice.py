# Write a program to filter a list of numbers which are divisible by 5
def is_divisible(n):
    if n%5 == 0:
        return True
    return False

a = [1,2,4,5,6,74, 3, 10,7,54 ,15, 20]
print(list(filter(is_divisible, a)))


# Write a program to find the maximum of the numbers in a list using the reduce function
from functools import reduce
 
def max(m, n):
    if(m>n):
        return m
    else:
        return n
a = [1, 2, 4, 66, 3 ,5,35, 6, 7]
maxNum = reduce(max, a)
print(maxNum)



# Create a web server using flask and python
# google -> flask minimal app