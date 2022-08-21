from operator import ne
from re import L
from tkinter import *
from turtle import left
from unittest.mock import AsyncMock
from PIL import Image, ImageTk

root = Tk()
root.geometry("1000x800")

Newspaper = Label(text="~~THE TIMES OF KUCH BHI NEWS~~", font = "Algerian 20 bold", bg = "black", fg = "white")
Newspaper.pack(side=TOP, fill= X)

f1 = Frame(root, pady = 10, padx = 20)
f1.pack(anchor=NW, fill = X)

image1 = Image.open("a.jpg")
resImg1 = image1.resize((200, 200), Image.Resampling.LANCZOS)
photo = ImageTk.PhotoImage(resImg1)
label = Label(f1, image = photo, relief=SUNKEN, borderwidth=5)
label.pack(side = LEFT)

label = Label(f1, text = "This is Mr gadha who ate a lot of ghass", font = "sansserif 14", pady = 10, padx = 20)
label.pack(anchor=NW)
label = Label(f1, text = '''The domestic donkey is a hoofed mammal in the family Equidae, the same family as the horse. It derives from the African \nwild ass, Equus africanus, and may be \nclassified either as a subspecies thereof, Equus africanus asinus, or as a\n separate species, Equus asinus. It was domesticated in\n Africa, probably about 5,000[1]or 6,000years ago, and has been used mainly as\n a working animal since that time.

There are more than 40 million donkeys in the world, mostly in underdeveloped countries, where they are \nused principally as draught or pack animals''', font = "sansserif 10 italic", padx = 20)
label.pack(anchor=NW)




f2 = Frame(root, padx = 20, pady = 10)
f2.pack(anchor= NW, fill = X)

image2 = Image.open("R (1).jfif")
resImg2 = image2.resize((200, 200), Image.Resampling.LANCZOS)
photo2 = ImageTk.PhotoImage(resImg2)
label = Label(f2, image=photo2, relief = SUNKEN, borderwidth=5)
label.pack(side = LEFT)

label = Label(f2, text = "Scientists ki nayi khoj.... Pata nhi Kya h", font = "sansserif 14", pady = 10, padx = 20)
label.pack(anchor= NW)
label = Label(f2, text = '''Taare Zameen par... OOOOOO tare zameen par kya baat h kya baat h....
kehete hn khuda ne iss jahan me sabhi k liye kisi na kisiko h banaya har kisi k liye
likho kuchbhi karo kuchbhi suno apne dil ki....
haan bhaiii aa gya swaad ''', font = "sansserif 10 italic", pady = 10, padx = 20)
label.pack(anchor= NW)



root.mainloop()