from tkinter import *

def myFunc():
    print("Mai ek bahut he natkhat aur shaitann funcion h")

root = Tk()
root.geometry("744x544")
root.title("Menus And Submenus")


'''Use these to create a non drop down menu'''
# myMenu = Menu(root)
# myMenu.add_command(label = "File", command = myFunc)
# myMenu.add_command(label = "Exit", command = quit)
# root.config(menu = myMenu)

mainMenu = Menu(root)

m1 = Menu(mainMenu, tearoff= 0)         # To remove tear off from python menu
m1.add_command(label = "New Project", command = myFunc)
m1.add_command(label = "Save", command = myFunc)
m1.add_separator()              #To add a horizontal line
m1.add_command(label = "Save as", command = myFunc)
m1.add_command(label = "Print", command = myFunc)
m1.add_command(label = "Exit", command = quit)
root.config(menu = mainMenu)
mainMenu.add_cascade(label = "file", menu = m1)

m2 = Menu(mainMenu, tearoff= 0)         # To remove tear off from python menu
m2.add_command(label = "Cut", command = myFunc)
m2.add_command(label = "Copy", command = myFunc)
m2.add_command(label = "Paste", command = myFunc)
m2.add_separator()              #To add a horizontal line
m2.add_command(label = "Find", command = myFunc)
root.config(menu = mainMenu)
mainMenu.add_cascade(label = "Edit", menu = m2)


root.mainloop()