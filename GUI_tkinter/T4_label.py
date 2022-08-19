# Label
from cProfile import label
from tkinter import *

root = Tk()


'''Setting the size of the GUI Window'''
# width X height
root.geometry("444x234")

# width, height
root.minsize(200, 200)

# width, height
root.maxsize(800, 400)


# LABEL
aryan = Label(text="Aryan is a good boy and this is his GUI")
aryan.pack()

root.mainloop()