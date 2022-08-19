'''
Modes of opening a file:
1. r: open for reading
2. w: open for writing
3. a: open for appending
4. +: open for updating

rb: will open for read in binary mode
rt: will open for read in text mode
'''

# f = open("this.txt", "r")

# # text = f.read(6)                # Read 6 characters of a file
# # print(text)

# # text = f.readline()
# # print(text)
# # text = f.readline()
# # print(text)

# # text = f.readlines()        #returs a list of lines 
# # print(text)

# f.close()



# Writing in a file
# f = open("write.txt", "w")
# # f.write("this is a text, I want to write to this file\n")
# # f.write("Second Line: this is a text, I want to write to this file")
# f.close()



# Append mode
f = open("write.txt", "a")
f.write("this is a text, I want to write to this file\n")
f.write("Second Line: this is a text, I want to write to this file\n")
f.close()


# With Statement
with open("mine.txt", "w") as f:
    f.write("This file is mine\n")
    f.write("This file is mine\n")