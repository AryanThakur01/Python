from tkinter import *
from turtle import left

root = Tk()
root.geometry("900x600")
root.title("Buttons")

def hello():
    print("Hello World")
def creator():
    print("Aryan Thakur")


f1 = Frame(root, borderwidth=4, relief = SUNKEN, bg = "gray")
f1.pack(fill = X)

b1 = Button(f1, text = "Hello Button", command = hello, relief = RAISED, borderwidth = 3, bg = "green", fg = "lightgreen", padx = 5)
b1.pack(side = LEFT, padx = 10, pady = 5)

b2 = Button(f1, text = "creator", bg = "green", fg = "lightgreen", relief=RAISED, command= creator, borderwidth = 3, padx = 10)
b2.pack(side = LEFT, padx = 10, pady = 5)

root.mainloop()