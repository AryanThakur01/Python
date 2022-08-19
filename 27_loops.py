a = 1

# While loop
'''
while(a <= 100):
    print(a)
    a += 1
'''


a= [1,2,"apple",3,4,5,6,"banana"]
        #printing the contents of a list
'''
i = 0
while(i<len(a)):
    print(a[i])
    i+=1
'''


# for loops
'''for i in range(34):
    print(i)
'''

'''
for i in range(len(a)):
    print(a[i])
    i+=1
'''
'''
for i in a:
    print(i)
'''
    # range(start,stop,skipSize)
'''
for i in range(1,6,2):
    print(a[i])
    i+=1
'''


# Break and continue
'''
a = [1,2,3,4,5]
for item in a:
    print(item)
    if(item == 3):
        break
print("We have finished this loop\n")

a = [1,2,3,4,5]
for item in a:
    print(item)
    if(item == 3):
        continue
    print("done this iteration for",item)
    
'''

# for else loop
'''
a = [1,23,4,5,6,9]
for item in a:
    print(item)
    if(item== 4):
        break           #if the loop is broken in between then the else statement will not be printed
    print("done this iteration for ", item)
else:
    print("we are inside else")
print("We have finished this loop")
'''


# pass
for i in range(0,56):
    pass                #without pass the the python will throw an error
print("do something")
