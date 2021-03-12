from tkinter import *

def result(z1, z2):
    res = z1 + z2
    lblresult.delete(0, END)
    lblresult.insert(0, res)
    return

window = Tk()
window.title("Add Calculator")

label1 = Label(window, text="First Number: ").grid(row=1, column=1, sticky=W)
label2 = Label(window, text="Second Number: ").grid(row=3, column=1, sticky=W)

number1Var = IntVar()
entry1 = Entry(window, textvariable=number1Var, justify=LEFT).grid(row=2, column=1)

number2Var = IntVar()
entry2 = Entry(window, textvariable=number2Var, justify=LEFT).grid(row=4, column=1)

label3 = Label(window, text = "Result: ").grid(row = 5, column = 1, sticky = W)

lblresult = Entry(window, justify=RIGHT)
lblresult.grid(row=5, column=2, sticky=E)

btresult = Button(window, text="Compute Sum", command=result(number1Var.get(), number2Var.get()))
btresult.grid(row=6, column=2, sticky=E)

window.mainloop()