from tkinter import *
import math
import cmath
import sympy
import numpy


def calculus():
    window = Tk()
    window.title("DERIVATIVE AND INTEGRAL CALCULATOR")
    window.config(bg="yellow")
    window.geometry("700x600")
    L1 = Label(window,text="Derivative and integral value calculator", font=("Arial",25),
    bg="yellow")
    L1.pack()
    L2 = Label(window,text='1.Derivative: ', font=("Arial", 20), bg="yellow")
    L2.place(x=10,y=50)
    L3 = Label(window,text='Enter the expression in terms of x: ', font=("Arial",17), bg="yellow")
    L3.place(x=10,y=100)
    E1 = Entry(window, font=("Arial", 17),width=40)
    E1.place(x=10, y=130)
    def derivative():
        entry1 = E1.get()
        x = sympy.symbols('x')
        y = sympy.diff(entry1)
        y1 = str(y).replace("**", "^")
        Label1 = Label(window, text=f"Derivative = {y1}", font=("Arial", 17), bg="yellow")
        Label1.place(x=200, y=230)
    B1 = Button(window,text="Submit",command=derivative, font=("Arial",15))
    B1.place(x=10, y=180)
    def clear1():
        global E2
        E1.delete(0,END)
    B2 = Button(window, text="Clear", command=clear1, font=("Arial",15))
    B2.place(x=100, y=180)
    L4 = Label(window,text='2. Indefinite integral: ', font=("Arial",20), bg="yellow")
    L4.place(x=10,y=280)
    L5 = Label(window,text='Enter the expression in terms of x: ', font = ("Arial",17), bg="yellow")
    L5.place(x=10,y=330)
    E4 = Entry(window, font=("Arial", 17),width=40)
    E4.place(x=10, y=380)
    def integration():
        entry1 = E4.get()
        x = sympy.symbols('x')
        y = sympy.integrate(entry1)
        y1 = str(y).replace("**", "^")
        Label2 = Label(window, text=f"Integral = {y1}", font=("Arial", 17), width=40, bg="yellow")
        Label2.place(x=10,y=480)
    def clear2():
        global E3
        E4.delete(0,END)
    B3 = Button(window,text="Submit",command=integration, font=("Arial",15))
    B3.place(x=10, y=430)
    B4 = Button(window, text="Clear", command=clear2, font=("Arial",15))
    B4.place(x=100,y=430)
    window.mainloop()
