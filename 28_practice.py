# loops practice 1
from glob import iglob


num = int(input("Enter the number for the table: "))
for i in range(10):
    print(f"{num} X {i+1}\t= {num*(i+1)}")


# loops practice 2
l1 = ["Shivam", "Sohan", "Harry", "Deepika", "Sachin"]
for item in l1:
    if item.startswith("S"):
        print(f"Good morning {item}")


# prime number test

num = 2
for i in range(2, num):
    if (num % i == 0):
        print("Not prime")
        break
else:
    print("This is a prime number")


# first n natural numbers sum
i = 4
sum = 0
while (i <= 10):
    sum += i
    i += 1
print(f"The sum of first n natural numbers is {sum}")

# print a star pattern
'''
      *
     ***
    *****
   *******
  *********
'''

n = int(input("Enter a number: "))

for i in range(1, n+1):
    for j in range(n-i):
        print(" ", end="")
    for j in range(2*i-1):
        print("*", end="")
    for j in range(n-i):
        print(" ", end="")
    print("\n", end="")

'''
*  *  *  *  *
*           *
*           *
*           *
*  *  *  *  *
'''

n = int(input("Enter a number: "))
for i in range(n):
    for j in range(n):
        if(i == 0 or j == 0 or i == n-1 or j == n-1):
            print(" * ", end="")
        else:
            print("   ", end="")
    print('\n', end='')


# multiplication table using reversed for loop

n = 12
for j in range(1, 11):
    i = 11-j
    print(f"{n} X {i} = {n*i}")
