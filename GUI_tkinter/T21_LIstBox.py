from tkinter import *

def add():
    global i
    lbx.insert(ACTIVE, f"{i}")
    i+=1
i = 0

root = Tk()
root.geometry("600x300")
root.title("ListBox Tutorial")

lbx = Listbox(root)
lbx.pack()

lbx.insert(END, "First item of a listbox")

Button(root, text="Add Item", command=add).pack()

root.mainloop()