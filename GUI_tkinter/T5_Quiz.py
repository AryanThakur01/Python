from tkinter import *
from PIL import Image, ImageTk
import os

ImageList = os.listdir('./RandomImages')    # Getting the names of the imgages using os module


root = Tk()
root.geometry("200x550")

Heading = Label(text="This is my album")
Heading.pack()


image1 = Image.open("./RandomImages/"+ImageList[0])
resizedImage = image1.resize((100,100), Image.Resampling.LANCZOS)
photo= ImageTk.PhotoImage(resizedImage)
label = Label(image=photo)
label.pack()

image2 = Image.open("./RandomImages/"+ImageList[1])
resizedImage2 = image2.resize((100,100), Image.Resampling.LANCZOS)
photo2 = ImageTk.PhotoImage(resizedImage2)
label = Label(image = photo2)
label.pack()

image3 = Image.open("./RandomImages/"+ ImageList[2])
resizedImage3 = image3.resize((100,100), Image.Resampling.LANCZOS)
photo3 = ImageTk.PhotoImage(resizedImage3)
label = Label(image = photo3)
label.pack()

image4 = Image.open("./RandomImages/"+ ImageList[3])
resizedImage4 = image4.resize((100,100), Image.Resampling.LANCZOS)
photo4 = ImageTk.PhotoImage(resizedImage4)
label = Label(image = photo4)
label.pack()

image5 = Image.open("./RandomImages/"+ ImageList[4])
resizedImage5 = image5.resize((100,100), Image.Resampling.LANCZOS)
photo5 = ImageTk.PhotoImage(resizedImage5)
label = Label(image = photo5)
label.pack()

root.mainloop()