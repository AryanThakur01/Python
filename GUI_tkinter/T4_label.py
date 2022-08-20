# Label
from cProfile import label
from tkinter import *

root = Tk()


'''Setting the size of the GUI Window'''
# width X height
root.geometry("400x400")

# width, height
root.minsize(300, 300)

# width, height
root.maxsize(600, 600)


# LABEL
aryan = Label(text="Aryan is a good boy and this is his GUI")
aryan.pack()

root.mainloop()