from cgitb import grey
from tkinter import *
from PIL import Image, ImageTk

root = Tk()

root.geometry("500x500")

# head = Label(text = "~~This is the heading of the page~~", bg = "black", font = "Algerian 20 italic", fg = "white")
# head.pack(fill = X)

f1 = Frame(root, bg = "grey", borderwidth=6, relief = SUNKEN)
f1.pack(side = LEFT, fill = Y, pady = 50)

f2= Frame(root, borderwidth = 8, bg = "grey", relief = SUNKEN)
f2.pack(side = TOP, fill = X)

l = Label(f1, text = "Project Tkinter - pycharm")
l.pack(pady = 142)

l = Label(f2, text = "Welcome to sublimetext", font = "Helvetica 16 italic", fg = "Blue")
l.pack()



root.mainloop()