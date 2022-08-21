from tkinter import *

root = Tk()
root.geometry("600x500")

frame = Frame(root, borderwidth = 6, bg = "grey", relief = SUNKEN)
frame.pack(side = LEFT, anchor = "nw")

def hello():
    print("Hello tkinter buttons")
def name():
    print("My name is aryan")
b1 = Button(frame,bg = "black", fg = "light green", text = "BIG BUTTON", command = hello)
b1.pack(side = LEFT, padx = 5, pady = 2)
b2 = Button(frame,bg = "black", fg = "light green", text = "BIG BUTTON", command = name)
b2.pack(side = LEFT, padx = 5, pady = 2)
b3 = Button(frame,bg = "black", fg = "light green", text = "BIG BUTTON")
b3.pack(side = LEFT, padx = 5, pady = 2)
b4 = Button(frame,bg = "black", fg = "light green", text = "BIG BUTTON")
b4.pack(side = LEFT, padx = 5, pady = 2)

root.mainloop()