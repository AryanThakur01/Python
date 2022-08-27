from tkinter import *
import tkinter.messagebox as tmsg

def order():
    tmsg.showinfo("Order Received!", f"We have received your order for {var.get()}. Thanks for ordering")

root = Tk()
root.geometry("500x200")
root.title("Radio Button Tutorial")

# var = IntVar()
var = StringVar()
var.set("Radio")
# var.set(1)
Label(root, text= "What would you like to have sir?", justify=LEFT, padx=14, font="lucida 19 bold").pack()

radio = Radiobutton(root, text="Dosa", padx=14, variable= var, value= "Dosa").pack(anchor=W)
radio = Radiobutton(root, text="Idly", padx=14, variable= var, value= "Idly").pack(anchor=W)
radio = Radiobutton(root, text="Paratha", padx=14, variable= var, value= "Paratha").pack(anchor=W)
radio = Radiobutton(root, text="Samosa", padx=14, variable= var, value= "Samosa").pack(anchor=W)

Button(text="Order Now", command=order).pack()


root.mainloop()