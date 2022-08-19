# a list contains multiplication table of 7. Write a program to convert it to a vertical string of same numbers 
a = [i*7 for i in range(1, 11)]
st = ""
for item in a:
    st += str(item) + '\n'

print(st)