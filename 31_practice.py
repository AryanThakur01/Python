'''greatest number finding '''
def greatest(num1, num2, num3):
    if(num1>num2):
        greater = num1
    else:
        greater = num2
    if(num3>greater):
        greater = num3
    
    return greater

a = greatest(1,5,2)
print(a)



'''celsius to farenhite'''
def cel2far(cel):
    return (cel+ 9/5) + 32

a = cel2far(134)
print(a)



'''end of a line is not with the \n'''
print("Harry and raj", end = "\t")
print("And Simran")



'''sum of first n natural numbers'''
def sum(n):
    if(n == 1):
        return 1
    return sum(n-1) + n

print("Sum of first 100 natural numbers is: ", sum(100))



'''printing * pattern'''
def printPattern(n):
    for i in range(n):
        print("*" * (i))

printPattern(10)