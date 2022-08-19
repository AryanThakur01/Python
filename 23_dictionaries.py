# No repetition of keywords is allowed
oxford = {
    "gift": "Something willingly given to someone to appreciate",
    "this": "A keyword in c++",
    "Youtube": "A video sharing platform",
    "instagram": "a picture sharing platform",
    "mylist": [1, 2, 54, 3, 4]
    # [1,2,45]: "6g"    this will give an error
}


print("\n")
print(oxford)
print(oxford["gift"])
print(oxford.get("instagram"))     # if a key is not present in the dictionary then NONE is printed

# Dict Methods

# print(oxford.items())   # This will print a tuple of key value pairs

oxford.update({"harry": "Good boy", "mylist":[12,434,32]})

print("\n")
for a,b in oxford.items():
    print(a,":",b)

print("\n")
for key in oxford.keys():
    print(key)

print("\n")
for value in oxford.values():
    print(value)
