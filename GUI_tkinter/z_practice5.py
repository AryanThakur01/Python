from ast import main
from tkinter import *

root = Tk()

root.geometry("699x500")
root.title("This is something else")


mainMenu = Menu(root)
m1 = Menu(mainMenu, tearoff=0)
m1.add_command(label = "New")
m1.add_command(label = "Save")
m1.add_command(label = "Save As")
m1.add_command(label = "Exit", command= quit)
root.config(menu = mainMenu)
mainMenu.add_cascade(label = "File", menu = m1)

m2 = Menu(mainMenu, tearoff=0)
m2.add_command(label = "Find")
m2.add_command(label = "Clear")
m2.add_checkbutton(label = "Font Wrap")
root.config(menu = mainMenu)
mainMenu.add_cascade(label = "Edit", menu = m2)

m3= Menu(mainMenu, tearoff=0)
m3.add_command(label = "About Creator")
root.config(menu = mainMenu)
mainMenu.add_cascade(label = "Help", menu = m3)


Label(root, text = "THIS IS THE HEADING OF THE PYTHON PROGRAMME", font = "Algerian 20 bold", bg = "black", fg = "white", pady = 6).pack(fill = X)

frame = Frame(root, bg = "black", relief = SUNKEN, borderwidth=3)
Label(frame, text = "This is an Important file created purely for practice purpose only. It contains no harmful data so no need to worry while reading this programme", pady = 7, padx = 20).pack()
frame.pack(pady = 10)

root.mainloop()