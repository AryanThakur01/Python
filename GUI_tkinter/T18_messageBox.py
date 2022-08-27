from tkinter import *
import tkinter.messagebox as tmsg

def myFunc():
    print("Mai ek bahut he natkhat aur shaitann funcion h")

def help():
    print("I will help you")
    a = tmsg.showinfo("Help", "Aryan will help you with this GUI")
    # print(a)

def rate():
    print("Rate us")
    value = tmsg.askquestion("Was your experience good", "You used this GUI... was your experience good?")
    print(value)
    if value == "yes":
        msg = "Great. Rate us on appstore please"
    else:
        msg = "Tell us what went wrong. We will call you soon"
    tmsg.showinfo("Experience", msg)

def divya():
    ans = tmsg.askretrycancel("Divya se dosti karlo", "Sorry divya nahi banegi aapki dost")
    if ans:
        print("Retry karne pe bhi kuch nahi hoga")
    else:
        print("Bahut badhiya bhai cancel kardiya warna pit te")


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

m3 = Menu(mainMenu, tearoff=0)
m3.add_command(label = "Help", command= help)
m3.add_command(label = "RateUs", command= rate)
m3.add_command(label = "Befriend Divya", command= divya)
root.config(menu=mainMenu)
mainMenu.add_cascade(label = "Edit", menu = m3)


root.mainloop()