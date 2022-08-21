from textwrap import fill
from tkinter import *
from tkinter.font import BOLD
from PIL import Image, ImageTk

root = Tk()
root.title("PracticePage")
root.geometry("600x500")

heading = Label(text = "~~This is just a practice page~~", bg = "Black", font = "Algerian 20 bold", fg = "white", pady = 5)
heading.pack(fill = X)

frame = Frame(root, borderwidth=5, relief=SOLID)
frame.pack(fill = X, pady = 2, padx = 2)

image1 = Image.open("R (1).jfif")
imgResize = image1.resize((200, 200), Image.Resampling.LANCZOS)
photo = ImageTk.PhotoImage(imgResize)
label = Label(frame, image = photo, borderwidth=3, relief= SUNKEN)
label.pack(side = LEFT, pady=10, padx = 20)

imgDescribe = Label(frame, text = "THIS IS MIND YOUR OWN BUSINESS", font = "sansserif 15 italic")
description = Label(frame, text = '''Description of the image is provided right here and right now and\nnobody is supposed to haveany problem with that''', font = "sansserif 12 italic")
imgDescribe.pack(anchor = NW, pady = 10)
description.pack(anchor = NW, pady = 10)

def Description():
    print("Only scientists can understand what this is")
    frame2 = Frame(root, borderwidth=5, relief=SOLID)
    frame2.pack(fill = X, pady = 2, padx = 2)

    image2 = Image.open("a.jpg")
    imgResize = image2.resize((200, 200), Image.Resampling.LANCZOS)
    photo = ImageTk.PhotoImage(imgResize)
    label = Label(frame2, image = photo, borderwidth=3, relief= SUNKEN)
    label.pack(side = LEFT, pady=10, padx = 20)

    imgDescribe = Label(frame2, text = "THIS IS MIND YOUR OWN BUSINESS", font = "sansserif 15 italic")
    description = Label(frame2, text = '''Description of the image is provided right here and right now and\nnobody is supposed to haveany problem with that''', font = "sansserif 12 italic")
    imgDescribe.pack(anchor = NW, pady = 10)
    description.pack(anchor = NW, pady = 10)
    
button = Button(frame, bg = "black", fg = "lightgreen", text ="Whatever", padx = 20, relief= RAISED, borderwidth=4, command = Description)
button.pack(side = RIGHT, padx = 22)

root.mainloop()