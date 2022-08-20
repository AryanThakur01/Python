from tkinter import *
from PIL import Image, ImageTk

root = Tk()

root.geometry("500x500")

image = Image.open("R.jfif")
photo = ImageTk.PhotoImage(image)

label = Label(image = photo)
label.pack()

root.mainloop()