# List

a = 12
b = "This is a string"
c = False

myList = [a, b, c, 23.4]
print(myList)
print(type(myList))

# Slicing in List
L1 = [a, b, c, 23.4]
print(L1[0])
print(L1[3])
print(L1[-3])
print(L1[-3:-1])
print(L1[-2::])
print(L1[0:2])
print(L1[0:3:2])
print(L1[2::])


print("\n")


# List Methods
myListOfNumbers = [1, 2, 3, 42, 15, 1, 3, 1, 5, 7]
print(myListOfNumbers)

# myListOfNumbers.sort()          # This returns None, rather it updates the original list
# myListOfNumbers.reverse()       # reverses the original list
# myListOfNumbers.append(102)     # This will insert at the end of the list
# myListOfNumbers.insert(2,00)    # Inserts at 00 at index 2
# myListOfNumbers.pop()           #Removes an item from the end of the list
# myListOfNumbers.pop(3)          #Removes an item from the given index of the list
myListOfNumbers.remove(1)         # Removes the first occurence of a given item from the list

print(myListOfNumbers)