from tkinter import*
from PIL import Image, ImageTk
# PIL: python imaging library       for getting jpg files in tkinter


root = Tk()

root.geometry("1200x700")
# photo = PhotoImage(file="car.png")


# For other image format

image = Image.open("R.jfif")
photo= ImageTk.PhotoImage(image)

label = Label(image=photo)
label.pack()

root.mainloop()

# pip install pillow