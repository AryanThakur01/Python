try:
    print("Hello World")
    a = int(input("Enter a number: "))
    b = int(input("Enter another number: "))
    print(a / b)
    if b > 199:
        raise Exception("This number is too large")

except ValueError:
    print("Value error occured")
except ZeroDivisionError:
    print("you cannot divide by zero")
except Exception as e:
    print(f"A PROBLEM!!XXXXXXXXXXXXXX {e} XXXXXXXXXXXXXXXX")
else:                                                   # This will run only if try statement would be successful
    print("Try was successful")

print('NO OTHER ERRORS')