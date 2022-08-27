from tkinter import *
from PIL import ImageTk, Image

def every_100(text):
    final_text = ""
    for i in range(0, len(text)):
        final_text += text[i]
        if i%150==0 and i !=0:
            final_text +="\n"
    return final_text

root = Tk()

root.title("The Times of Kuch Bhi News")
root.geometry("1000x800")

texts = []
photos = []
for i in range(0,3):
    with open(f"{i+1}.txt") as f:
        text = f.read()
        texts.append(every_100(text))

    image = Image.open(f"{i+1}.png")
    # TODO: resize these Images
    imgResize = image.resize((200, 200), Image.Resampling.LANCZOS)
    
    photos.append(ImageTk.PhotoImage(imgResize))

f0 = Frame(root, width = 800, height = 70, bg = "black")
Label(f0, text = "~~THE TIMES OF KUCH BHI NEWS~~", font = "lucida 25 bold", fg = "white", bg = "black").pack()
Label(f0, text = "december 18, 3030", font = "lucida 16 bold", fg = "white", bg = "black").pack()
f0.pack(fill = X)

f1 = Frame(root, width = 900, height = 200, borderwidth=4, relief=RAISED)
Button(f1, image=photos[0]).pack(side = LEFT, padx = 5, pady = 10)
Label(f1, text =texts[0], font = "sansserif", padx = 10, pady=10, anchor = "e").pack()
f1.pack(anchor=NW, padx = 10, pady = 5, fill=X)

f2 = Frame(root, width = 900, height = 200, borderwidth=4, relief=RAISED)
Button(f2, image=photos[1]).pack(padx = 5, pady = 10, side = RIGHT)
Label(f2, text =texts[1], font = "sansserif", padx = 10, pady=10, anchor = E).pack()
f2.pack(anchor=NW, padx = 10, pady = 5, fill=X)




root.mainloop()