from tkinter import *

root = Tk()

root.geometry("500x400")
root.title("Practice page")

readyLabel = Label(text="~~READY~~", bg = "purple", fg = "lightgreen", pady = 5, font = ("Algerian 10 italic"), borderwidth=5, relief = SUNKEN)
readyLabel.pack(side=BOTTOM, fill = X)


root.mainloop()