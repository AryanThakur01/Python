from cgitb import text
from tkinter import *
def changeDimensions():
    root.geometry(f"{width.get()}x{height.get()}")

root = Tk()
root.geometry("300x100")


Label(text="width").grid(row = 0, column = 0)
Label(text="height").grid(row = 1, column = 0)

width = StringVar()
height = StringVar()

widthEntry = Entry(root, textvariable= width)
heightEntry = Entry(root, textvariable= height)

widthEntry.grid(row = 0, column = 1)
heightEntry.grid(row = 1, column = 1)



Button(text="Apply", command= changeDimensions).grid(row = 2, column = 1)


root.mainloop()