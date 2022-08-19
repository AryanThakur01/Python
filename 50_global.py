a = 9
def func():
    global a        # this will make the a used inside the function to global and will change global variable
    a = 7
    print(a)
    a = 900
    print(a)

print(a)
func()
print(a)