from ast import Name
from tkinter import *

'''All Functions Here'''
def dataEntry():
    with open("T10_pr_DanceClassForm.txt", "a") as file:
        file.write(f"Name = {nameValue.get().upper()}\n")
        file.write(f"age = {ageValue.get()}\n")
        file.write(f"address = {addressValue.get()}\n")
        file.write(f"mobile.No = {mobileNoValue.get()}\n")
        file.write("\n==== X ========== X ====\n\n")



root = Tk()

root.geometry("500x500")
root.title("Dance class Form")

'''Putting Labels'''
name = Label(text = "Name")
age = Label(text = "Age")
address = Label(text = "address")
mobileNo = Label(text = "Mobile.No")

'''Software Geometry Management'''
name.grid(row = 0, column = 0)
age.grid(row = 1, column = 0)
address.grid(row = 2, column = 0)
mobileNo.grid(row = 3, column = 0)

'''Storing Inputs'''
nameValue = StringVar()
ageValue = IntVar()
addressValue = StringVar()
mobileNoValue = IntVar()

'''Taking Entries'''
nameEntry = Entry(root, textvariable=nameValue)
ageEntry = Entry(root, textvariable=ageValue)
addressEntry = Entry(root, textvariable = addressValue)
mobileNoEntry = Entry(root, textvariable= mobileNoValue)

'''Taking And Storing Entries'''
nameEntry.grid(row = 0, column = 1, padx = 15, pady = 3)
ageEntry.grid(row = 1, column = 1, padx = 15, pady = 3)
addressEntry.grid(row = 2, column = 1, padx = 15, pady = 3)
mobileNoEntry.grid(row = 3, column = 1, padx = 15, pady = 3)

submit = Button(root, text = "Submit", padx = 15, pady = 3, bg = "black", fg = "wheat", relief=RAISED, command = dataEntry)
submit.grid(row = 4, column = 1)

root.mainloop()