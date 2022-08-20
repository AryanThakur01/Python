from tkinter import *

root = Tk()

'''setting size of GUI window'''
# Width X Height
root.geometry("733x434")

root.minsize(733, 434)
root.maxsize(733, 434)

label = Label(text="PyCharm Community Edition")
label.pack()

root.mainloop()
