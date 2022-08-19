def function():
    try:
        a = int(input("Enter a number: "))
        b = int(input("Enter another number: "))
        print(a / b)
        return a/b
    except Exception as e:
        print(f"XXXXXXXXXXXXXX {e} XXXXXXXXXXXXXXXX")
        return 0
    finally:
        print("I will always be executed always")
    print("this statement is unreachable when something is returned")

# function()

print(__name__)
if __name__ == '__main__':      #if we are running this file then this will be executed however it won't be executed if we run this by importing in another file
    function()
    print("main")