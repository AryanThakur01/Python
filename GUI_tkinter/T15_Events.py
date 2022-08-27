from tkinter import *

def harry(event):                       # tkinter passes an event when trigered 
    print(f"You clicked on the button at {event.x}, {event.y}")

root = Tk()
root.title("Events in tkinter")
root.geometry("899x499")

widget = Button(root, text="Click me please")
widget.pack()

widget.bind('<Button-1>', harry)          # Search for Button events online
widget.bind('<Double-1>', quit)

root.mainloop()