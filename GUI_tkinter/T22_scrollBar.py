from tkinter import *

root = Tk()
root.geometry("600x200")
root.title("Scrollbar totorial")

'''For connecting scrollbar to a widget'''
# 1. widget(yscrollcommand= scrollbar.set())
# scrollbar.config(command=widget.yview)

scrollBar = Scrollbar(root)
scrollBar.pack(fill=Y, side = RIGHT)


# listbox = Listbox(root, yscrollcommand=scrollBar.set)
# for i in range (344):
#     listbox.insert(END, f"Item {i}")


# listbox.pack(fill = BOTH, padx = 22)

text = Text(root, yscrollcommand= scrollBar.set)
text.pack(fill = BOTH)
scrollBar.config(command=text.yview)


root.mainloop()