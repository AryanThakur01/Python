from tkinter import *
from turtle import right
from PIL import Image, ImageTk

root = Tk()
root.geometry("600x600")

heading = Label(text = "~~This is whatever~~", bg = "black", relief = RAISED, font = "algerian 20 bold", fg = "wheat")
heading.pack(fill = X)

def darkMode():
    root.configure(bg = "black")


button = Button(text = "ModeChange", bg = "blue", relief=RAISED, command = darkMode)
button.pack(padx = 10, pady = 10, anchor = NE)

frame = Frame(root, borderwidth=5, relief = SUNKEN)
frame.pack(fil = X, padx = 10, pady = 6)


image = Image.open("car.png")
resImg = image.resize((200,100), Image.Resampling.LANCZOS)
photo = ImageTk.PhotoImage(resImg)
label = Label(frame, image = photo, relief = SUNKEN)
label.pack(side = LEFT, padx = 10, pady = 10)

title = Label(frame, text = "THIS IS AN AWESOME SPORTS CAR", font = "sansserif 16 bold")
title.pack(anchor = NW, padx = 10, pady = 10)
description = Label(frame, text = "It doesn't matter what I write here cuz nobody can change the fact that this is an awesome supercar\nI too love this extremely amazing and extraordinary supercar", font = "sansserif 12 italic")
description.pack(side = LEFT, padx = 10)



root.mainloop()