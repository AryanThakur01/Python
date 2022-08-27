from tkinter import *
import tkinter.messagebox as tmsg

def getDollar():
    print(f"We have credited {myslider2.get()} dollars to your bank account")
    tmsg.showinfo("Credited amount", f"We have credited {myslider2.get()} dollars to your bank account")

root = Tk()
root.geometry("600x400")
root.title("Slider tutorial")

# myslider = Scale(root, from_=0, to = 100)
# myslider.pack()

Label(root, text= "How many dollars do you want").pack()

myslider2 = Scale(root, from_ = 0, to= 100, orient=HORIZONTAL, tickinterval = 50)
myslider2.set(50)
myslider2.pack()

Button(text="Get Dollars", command = getDollar).pack()

root.mainloop()