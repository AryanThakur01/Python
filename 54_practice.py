list1 = [1, 2, 4, 6, 2, 8, 5]
for index, item in enumerate(list1):
    if(index+1 == 3 or index +1 == 5 or index +1 == 7):
        print(item)



# Write a list comprehension to print a list which contains the multiplication table of a user entered number
n = int(input("Enter the number for table calculation: "))
list = [f"{n} X {i} = {n*i}" for i in range(1,11)]
print(list)