from tkinter import *

class addCalculator:
    def __init__(self):
        window = Tk()
        window.title("Add Calculator")

        def result(z1,z2):
            biz=z1+z2
            lblresult.delete(0,END)
            lblresult.insert(0,biz)
            return

        Label1 = Label(window, text = "First Number: ").grid(row = 1, column = 1, sticky = W)
        Label2 = Label(window, text = "Second Number: ").grid(row = 2, column = 1, sticky = W)

        self.number1Var = IntVar()
        Entry1 = Entry(window, textvariable = self.number1Var, justify = RIGHT).grid(row = 1, column = 2)

        self.number2Var = IntVar()
        Entry2 = Entry(window, textvariable = self.number2Var, justify = RIGHT).grid(row = 2, column = 2)

        Label3 = Label(window, text = "Result: ").grid(row = 3, column = 1, sticky = W)

        lblresult = Entry(window, justify = RIGHT)
        lblresult.grid(row = 3, column = 2, sticky = E)

        btresult = Button(window,text="Compute Sum",command=lambda:result(self.number1Var.get(),self.number2Var.get()))
        btresult.grid(row = 4, column = 2, sticky = E)

        window.mainloop()

addCalculator()