from dataclasses import replace


name = "Adam D'Angelo"
nameb = 'Adam D\'Angelo'
name2 = 'John'
name3 = '''Twinkle, twinkle, little star
How I wonder what you are
Up above the world so high
Like a diamond in the sky
Twinkle, twinkle, little star
How I wonder what you are

Twinkle, twinkle, little star
How I wonder what you are
Up above the world so high
Like a diamond in the sky
Twinkle, twinkle, little star
How I wonder what you are

Twinkle, twinkle, little star
How I wonder what you are
Up above the world so high
Like a diamond in the sky
Twinkle, twinkle, little star
How I wonder what you are

Twinkle, twinkle, little star
How I wonder what you are
Up above the world so high
Like a diamond in the sky
Twinkle, twinkle, little star
How I wonder what you are'''

print(name)
print(type(name))

print(nameb)
print(type(nameb))

print(name2)
print(type(name2))

print(name3)
print(type(name3))


# String Slicing

name = "Harry"
myStr = "abcdefghijklmnopqrstuvwxyz"
print("name", name)
print("name[1]:",name[1])
print("name[-1]:",name[-1])
print("myStr[-4:-1]",myStr[-4:-1])
print("myStr[0:2]",myStr[0:2])        #last index is not included
print("myStr[0:20:2]",myStr[0:40:2])    #name[initialIndex: finalInde: skipValue]



# String functions
myStr = "abcdefghijklmnopqrstuvwxyz"
print(len(myStr))                   #length function                          ->len()
print(myStr.endswith('xyz'))        #endswith function                        -> endswith("")
print(myStr.startswith('abcde'))    #startswith function                      -> startswith("")
print(myStr.count("a"))             #count function (counts the number of a)  ->count("a")
myStr = "my name is Aryan name"
print(myStr.capitalize())           #capitalizes the first alphavet           ->capitalize()
print(myStr.find("name"))           #to find the index of a word's first alphabet ->find("")
print(myStr.replace("name", "date"))#replace the both the occurences


# Escape sequence characters
# \' can be used to print a single quote(')
# \\ can be used to print a backslash(\)
myName = "My\tname\nis\tAryan"
print(myName)
