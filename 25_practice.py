oxford = {
    "lakdi" : "wood",
    "kursi" : "chair",
    "chaku" : "knife"
}
key = input("Enter the key\n")
if(oxford.get(key)== None):
    print("Value not found")
else:
    print("The value corresponding to your key is: ", oxford.get(key))


# question 2
s = set()
for i in range(8):
    s.add(input("Enter your number: "))
# question 3
s.add(18)
s.add("18")
s.add(20)
s.add(20.0)
print(s)

# s = {}  this will create an empty dictionary and not set
