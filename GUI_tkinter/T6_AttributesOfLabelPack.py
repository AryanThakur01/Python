from tkinter import *
from tkinter.font import BOLD

root = Tk()
root.geometry("700x500")

root.title("This is Title")

'''Important Label options'''
# text => adds the text
# bg => Background
# fg => foreground
# font => sets the font
    # font=("comicsans", 10, BOLD)
# padx => x padding
# pady => y padding
# relief => border styling - SUNKEN, RAISED GROOVE RIDGE

title_label = Label(text = '''Joey Lynn King[1] (born July 30, 1999[2]) is an American actress. \nShe first gained recognition for portraying Ramona Quimby in the comedy film Ramona and \nBeezus (2010) and has since gained wider recognition for her lead role in The Kissing Booth (2018) and its two sequels. \nKing received \ncritical acclaim for her starring role in the crime drama series The Act (2019), for which \nshe was nominated for both a Primetime Emmy Award and a Golden Globe Award.\n
\nKing has also appeared in the films Battle: \nLos Angeles (2011), Crazy, Stupid, Love (2011), The Dark Knight Rises (2012), Oz the Great and Powerful (2013), The Conjuring (2013), White House Down (2013), Independence \nDay: \nResurgence (2016), Wish Upon (2017), Going in Style (2017), The Lie (2018) and Bullet Train (2022) as well as the first season \nof the FX black comedy crime drama series Fargo.''', bg = "lightgreen", fg = "white", padx = 13, pady = 40, font=("comicsans 10 bold"), borderwidth = 5, relief = SUNKEN)


'''Important Pack options'''
# anchor = nw, ne
# side = top, bottom, left, right
# fill
# padx
# pady


title_label.pack(side = LEFT, fill = Y, padx = 20, pady = 40)

root.mainloop()