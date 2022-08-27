from tkinter import *

root = Tk()

root.geometry("608x684")

mainMenu = Menu(root)
m1 = Menu(mainMenu, tearoff = 0)
m1.add_command(label = "New")
m1.add_command(label = "Save")
m1.add_command(label = "Save As")
m1.add_checkbutton(label = "Check This", onvalue= 1, offvalue=0)
m1.add_command(label = "Edit")
m1.add_command(label = "Exit")
root.config(menu = mainMenu)
mainMenu.add_cascade(label = "File", menu = m1)

m2 = Menu(mainMenu, tearoff=0)
m2.add_command(label = "Font")
m2.add_command(label = "Font Wrap")
root.config(menu = mainMenu)
mainMenu.add_cascade(label = "Edit", menu = m2)

root.mainloop()