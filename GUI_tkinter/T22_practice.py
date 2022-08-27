from cgitb import text
from tkinter import *

with open("T22_practice.txt") as f:
    LongTextList = f.readlines()

root = Tk()
root.geometry("699x399")
root.title("Long Scrollable text")

scrollbar = Scrollbar(root)
scrollbar.pack(fill = Y, side = RIGHT)
scrollx = Scrollbar(root, orient=HORIZONTAL)
scrollx.pack(fill=X, side=BOTTOM)

listbox = Listbox(root, yscrollcommand=scrollbar.set, xscrollcommand=scrollx.set)
for i in LongTextList:
    listbox.insert(END, i)
    text = Text(root)

listbox.pack(fill=BOTH)
scrollbar.config(command = listbox.yview)
scrollx.config(command=listbox.xview)

root.mainloop()