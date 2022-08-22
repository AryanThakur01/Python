from tkinter import *

root = Tk()
def getvals():
    print("submitting Form")
    print(f"{nameValue.get(), phoneValue.get(), genderValue.get(), emergencyValue.get(), paymentModeValue.get(), foodServiceValue.get()}")
    with open("records.txt", "a") as f:
        f.write(f"{nameValue.get(), phoneValue.get(), genderValue.get(), emergencyValue.get(), paymentModeValue.get(), foodServiceValue.get()}\n")



root.geometry("499x500")


'''Heading''' 
Label(root, text = "Welcome to Aryan Travels", font = "sansserif 14 bold", pady = 15).grid(row = 0, column = 3)

'''Text for our form'''
name = Label(root, text="Name")
phone = Label(root, text = "Phone")
gender = Label(root, text = "Gender")
emergency = Label(root, text = "Emergency Contact")
paymentMode = Label(root, text = "Payment Mode")


'''Pack text for our form'''
name.grid(row = 1, column = 2)
phone.grid(row = 2, column = 2)
gender.grid(row = 3, column = 2)
emergency.grid(row = 4, column = 2)
paymentMode.grid(row = 5, column = 2)


'''Tkinter variables for storing entries'''
nameValue = StringVar()
phoneValue = StringVar()
genderValue = StringVar()
emergencyValue = StringVar()
paymentModeValue = StringVar()


'''Entries for our form'''
nameEntry = Entry(root, textvariable=nameValue)
phoneEntry = Entry(root, textvariable=phoneValue)
genderEntry = Entry(root, textvariable=genderValue)
emergencyEntry = Entry(root, textvariable=emergencyValue)
paymentModeEntry = Entry(root, textvariable=paymentModeValue)


'''Packing the entries for our form'''
nameEntry.grid(row = 1, column =3)
phoneEntry.grid(row = 2, column =3)
genderEntry.grid(row = 3, column =3)
emergencyEntry.grid(row = 4, column =3)
paymentModeEntry.grid(row = 5, column =3)


'''Checkbox and packing it'''
foodServiceValue = IntVar()
foodService = Checkbutton(text = "Want to prebook your meals", variable = foodServiceValue)
foodService.grid(row = 6, column = 3)


'''Button and packing it an dassigning it a command'''
Button(text = "Submit to Aryan Travels", command = getvals, relief=RAISED).grid(row = 7, column=3)


root.mainloop()