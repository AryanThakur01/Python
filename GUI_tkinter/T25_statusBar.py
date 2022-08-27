from tkinter import *

def upload():
    statusVar.set("Busy....")
    sBar.update()
    import time
    time.sleep(2)
    statusVar.set("Ready Now")

root = Tk()
root.geometry("500x500")
root.title("Status Bar Tutorial")


statusVar = StringVar()
statusVar.set("Ready")
sBar = Label(root, textvariable= statusVar, relief= SUNKEN, anchor = W)
sBar.pack(side= BOTTOM, fill=X)
Button(root, text = "Upload", command = upload).pack()

root.mainloop()