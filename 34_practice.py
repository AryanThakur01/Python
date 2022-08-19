from msilib.schema import tables
import random
import os

# Read a file poems.txt and check whether it contains the word twinkle or not
with open("poems.txt", "r") as f:
    if('twinkle' in f.read()):
        print("Yes twinkle is present")
    else:
        print("Twinkle is not present")


# Read a file that contains the high score which you need to update whenever the user breaks the high score
def game():
    score = random.randint(1,100)
    print(f"The score is {score}")
    return score

score = game()
with open("highscore.txt", "r") as f:
    highscore = int(f.read())

if highscore<score:
    with open("highscore.txt", "w") as f:
        f.write(str(score))



# write a program to generate multiplication table from 2 to 20 and place these files in a folder for a 13 yr old
for i in range(2, 21):
    table = ''
    for j in range(1,11):
        table += f"{i} X {j} = {i*j}\n"
    with open(f'34_tables/{i}.txt', "w") as f:
        f.write(table)



# A file contains a word "Donkey" multiple times you need to write a program to replace this word with ###### by updating the same file

with open("file.txt", "r") as f:
    text = f.read()

text = text.replace('donkey', "######")

with open("file.txt", "w") as f:
    f.write(text)



oldName = input("Enter the name of the file to rename: ")
newName = input("Enter the new name of the file: ")
with open(oldName, "r") as f:
    text = f.read()

with open(newName, 'w') as f:
    f.write(text)
os.remove(oldName)