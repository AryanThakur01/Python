# from datetime import date


name = input("Enter your name: ")
print("Hello",name)

name = input("Enter the name: ")
date = input("Enter the date: ")

template = '''
Dear <|name|>
you are selected
<|date|>
'''
print(template.replace('<|name|>', name).replace('<|date|>', date))

myStr = "this  me and   I  am  a  good  boy"
print(myStr.find("  "))
print(myStr.find("harry"))      # if not found then the result will be -1
print(myStr.replace("  ", " "))

# Using escape sequence characters
letter = "Dear Harry,\n\tThis python course is amazing.\nThanks"
print(letter)