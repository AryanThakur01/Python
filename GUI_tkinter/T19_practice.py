from tkinter import *
import tkinter.messagebox as tmsg

def rate():
    print(f"Customer rated {Rating.get()} out of 6 stars")
    with open("Customer rating", "a") as f:
        f.write(f"Customer rating:\n\t{Rating.get()} out of 6\n\n")
    tmsg.showinfo("Successful", "Thanks for your feedback")

root = Tk()

root.geometry("600x300")
root.title("Rating Page")

Label(text="Please rate Us").grid(row = 0, column = 0)
Rating = Scale(root, from_=0, to=6, orient=HORIZONTAL, tickinterval=3)
Rating.grid(row = 0, column = 1)

Button(root, text = "Submit", command=rate).grid(row = 1, column=0)


root.mainloop()