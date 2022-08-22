from tkinter import *
from tkinter.tix import ROW

def submitSuccessful():
    print("Submitted Successfully")

root = Tk()
root.title("FORM")
# root.geometry("699x699")

# Label(root, text ="WELCOME TO THE UNDERWORLD BANK", bg = "black", fg = "white", font = "Algerian 20 italic").grid(column = 5)

user = Label(root, text = "Username", padx = 5, pady = 5)
password = Label(root, text = "Password", padx = 5, pady = 5)

user.grid(row = 1, column = 0)
password.grid(row = 2, column = 0)

userValue = StringVar()
passValue = StringVar()

userEntry = Entry(root, textvariable=userValue)
passEntry = Entry(root, textvariable=passValue)

userEntry.grid(row = 1, column = 1)
passEntry.grid(row = 2, column = 1)


button = Button(root, text = "Submit Form", padx = 10, command=submitSuccessful)
button.grid(row = 3, column = 1, padx = 10, pady = 5)

root.mainloop()