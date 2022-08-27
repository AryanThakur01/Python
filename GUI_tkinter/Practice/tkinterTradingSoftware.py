from tkinter import *
from PIL import ImageTk, Image



root = Tk()
root.title("Trading Software")

mainMenu = Menu(root)


m1 = Menu(mainMenu, tearoff=0)
m1.add_command(label = "Sign In")
root.config(menu = mainMenu)
mainMenu.add_cascade(label="File", menu = m1)

m2 = Menu(mainMenu, tearoff=0)
root.config(menu= mainMenu)
mainMenu.add_cascade(label="Help", menu = m2)


frame = Frame(root, borderwidth=5, relief=SUNKEN)
frame.grid(row = 0, column = 1, padx = 10, pady = 10)

'''BITCOIN'''
frameBit = Frame(frame, pady = 4)
frameBit.grid(row = 0, column = 0, padx = 5)
bitCoin = Image.open("BTC.png")
bitRes = bitCoin.resize((20,20), Image.Resampling.LANCZOS)
photoBit= ImageTk.PhotoImage(bitRes)
bitC = Label(frameBit, image=photoBit)
bitC.grid(row = 0, column = 0, padx = 5)

Label(frameBit, text = "BTC",padx = 10).grid(row = 0, column = 1)

Button(frameBit, text="BUY", bg = "green", fg = "white", padx = 10).grid(row = 0, column = 2, padx = 10)
Button(frameBit, text="SELL", bg = "red", fg = "white", padx = 10).grid(row = 0, column = 3, padx = 10)
Button(frameBit, text = "Chart", bg = "blue", fg = "white", padx = 10).grid(row = 0, column = 4, padx = 10)


'''LITECOIN'''
frameLite = Frame(frame, pady = 4)
frameLite.grid(row = 1, column = 0, padx = 5)
liteCoin = Image.open("litecoin.png")
liteRes = liteCoin.resize((20,20), Image.Resampling.LANCZOS)
photoLite= ImageTk.PhotoImage(liteRes)
liteC = Label(frameLite, image=photoLite)
liteC.grid(row = 1, column = 0, padx = 5)

Label(frameLite, text = "LTC",padx = 10).grid(row = 1, column = 1)

Button(frameLite, text="BUY", bg = "green", fg = "white", padx = 10).grid(row = 1, column = 2, padx = 10)
Button(frameLite, text="SELL", bg = "red", fg = "white", padx = 10).grid(row = 1, column = 3, padx = 10)
Button(frameLite, text = "Chart", bg = "blue", fg = "white", padx = 10).grid(row = 1, column = 4, padx = 10)


'''BNB'''
frameBNB = Frame(frame, pady = 4)
frameBNB.grid(row = 2, column = 0, padx = 5)
BNBCoin = Image.open("BNB.png")
BNBRes = BNBCoin.resize((20,20), Image.Resampling.LANCZOS)
photoBNB= ImageTk.PhotoImage(BNBRes)
BNBC = Label(frameBNB, image=photoBNB)
BNBC.grid(row = 0, column = 0, padx = 5)

Label(frameBNB, text = "BNB",padx = 10).grid(row = 0, column = 1)

Button(frameBNB, text="BUY", bg = "green", fg = "white", padx = 10).grid(row = 0, column = 2, padx = 10)
Button(frameBNB, text="SELL", bg = "red", fg = "white", padx = 10).grid(row = 0, column = 3, padx = 10)
Button(frameBNB, text = "Chart", bg = "blue", fg = "white", padx = 10).grid(row = 0, column = 4, padx = 10)


'''doge'''
framedoge = Frame(frame, pady = 4)
framedoge.grid(row = 3, column = 0, padx = 5)
dogeCoin = Image.open("doge.png")
dogeRes = dogeCoin.resize((20,20), Image.Resampling.LANCZOS)
photodoge= ImageTk.PhotoImage(dogeRes)
dogeC = Label(framedoge, image=photodoge)
dogeC.grid(row = 0, column = 0, padx = 5)

Label(framedoge, text = "Doge",padx = 10).grid(row = 0, column = 1)

Button(framedoge, text="BUY", bg = "green", fg = "white", padx = 10).grid(row = 0, column = 2, padx = 10)
Button(framedoge, text="SELL", bg = "red", fg = "white", padx = 10).grid(row = 0, column = 3, padx = 10)
Button(framedoge, text = "Chart", bg = "blue", fg = "white", padx = 10).grid(row = 0, column = 4, padx = 10)


'''ETH'''
frameETH = Frame(frame, pady = 4)
frameETH.grid(row = 4, column = 0, padx = 5)
ETHCoin = Image.open("eth.png")
ETHRes = ETHCoin.resize((20,20), Image.Resampling.LANCZOS)
photoETH= ImageTk.PhotoImage(ETHRes)
ETHC = Label(frameETH, image=photoETH)
ETHC.grid(row = 0, column = 0, padx = 5)

Label(frameETH, text = "ETH",padx = 10).grid(row = 0, column = 1)

Button(frameETH, text="BUY", bg = "green", fg = "white", padx = 10).grid(row = 0, column = 2, padx = 10)
Button(frameETH, text="SELL", bg = "red", fg = "white", padx = 10).grid(row = 0, column = 3, padx = 10)
Button(frameETH, text = "Chart", bg = "blue", fg = "white", padx = 10).grid(row = 0, column = 4, padx = 10)


'''grid'''
framegrid = Frame(frame, pady = 4)
framegrid.grid(row = 4, column = 0, padx = 5)
gridCoin = Image.open("grid.png")
gridRes = gridCoin.resize((20,20), Image.Resampling.LANCZOS)
photogrid= ImageTk.PhotoImage(gridRes)
gridC = Label(framegrid, image=photogrid)
gridC.grid(row = 0, column = 0, padx = 5)

Label(framegrid, text = "Grid",padx = 10).grid(row = 0, column = 1)

Button(framegrid, text="BUY", bg = "green", fg = "white", padx = 10).grid(row = 0, column = 2, padx = 10)
Button(framegrid, text="SELL", bg = "red", fg = "white", padx = 10).grid(row = 0, column = 3, padx = 10)
Button(framegrid, text = "Chart", bg = "blue", fg = "white", padx = 10).grid(row = 0, column = 4, padx = 10)


'''HEX'''
frameHEX = Frame(frame, pady = 4)
frameHEX.grid(row = 5, column = 0, padx = 5)
HEXCoin = Image.open("HEX.png")
HEXRes = HEXCoin.resize((20,20), Image.Resampling.LANCZOS)
photoHEX= ImageTk.PhotoImage(HEXRes)
HEXC = Label(frameHEX, image=photoHEX)
HEXC.grid(row = 0, column = 0, padx = 5)

Label(frameHEX, text = "HEX",padx = 10).grid(row = 0, column = 1)

Button(frameHEX, text="BUY", bg = "green", fg = "white", padx = 10).grid(row = 0, column = 2, padx = 10)
Button(frameHEX, text="SELL", bg = "red", fg = "white", padx = 10).grid(row = 0, column = 3, padx = 10)
Button(frameHEX, text = "Chart", bg = "blue", fg = "white", padx = 10).grid(row = 0, column = 4, padx = 10)


'''NMC'''
frameNMC = Frame(frame, pady = 4)
frameNMC.grid(row = 6, column = 0, padx = 5)
NMCCoin = Image.open("NMC.png")
NMCRes = NMCCoin.resize((20,20), Image.Resampling.LANCZOS)
photoNMC= ImageTk.PhotoImage(NMCRes)
NMCC = Label(frameNMC, image=photoNMC)
NMCC.grid(row = 0, column = 0, padx = 5)

Label(frameNMC, text = "NMC",padx = 10).grid(row = 0, column = 1)

Button(frameNMC, text="BUY", bg = "green", fg = "white", padx = 10).grid(row = 0, column = 2, padx = 10)
Button(frameNMC, text="SELL", bg = "red", fg = "white", padx = 10).grid(row = 0, column = 3, padx = 10)
Button(frameNMC, text = "Chart", bg = "blue", fg = "white", padx = 10).grid(row = 0, column = 4, padx = 10)

root.mainloop()