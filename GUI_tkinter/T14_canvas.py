from tkinter import *

root = Tk()
root.title("Canvas")

canvas_width = 900
canvas_height = 500

root.geometry(f"{canvas_width}x{canvas_height}")
can_widget = Canvas(root, width = canvas_width, height = canvas_height, bg = "red")
can_widget.pack()

'''The line goes from the point x1,y1 to x2,y2'''
can_widget.create_line(9, 9, 791, 391, fill = "blue")
can_widget.create_line(9, 391, 791, 9, fill = "blue")

# can_widget.create_rectangle(3,5, 700, 300, fill = "brown")
can_widget.create_text(200, 200, text = "This is the thing called Text")

can_widget.create_rectangle(9,9, 791,391, activefill= "skyblue")
can_widget.create_oval(10,10, 790,390)

root.mainloop()