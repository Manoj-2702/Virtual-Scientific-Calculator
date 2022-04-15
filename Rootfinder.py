from tkinter import *
import math
import cmath
import sympy
import numpy

def root_finder():
    window = Tk()
    window.title("Root Finder")
    window.config(bg="dodgerblue3")
    window.geometry("800x500+100+100")
    L1 = Label(window, text="Root finder of polynomial equation", font=("Arial", 25),bg="dodgerblue3")
    L1.pack()
    def square():
        L2 = Label(window, text="2nd degree: x^2   + x     +    = 0", font=("Arial", 20),bg="dodgerblue3")
        L2.place(x=0, y=50)
        E1 = Entry(window, font=("Arial", 20), width=3)
        E1.place(x=175, y=50)
        E2 = Entry(window, font=("Arial", 20), width=3)
        E2.place(x=300, y=50)
        E3 = Entry(window, font=("Arial", 20), width=3)
        E3.place(x=400, y=50)
        def square_root():
            coeficcients = [int(E1.get()), int(E2.get()), int(E3.get())]
            roots = numpy.roots(coeficcients)
            L3 = Label(window, text=f"x = {roots[0].round(2)}, {roots[1].round(2)}", font=("Arial",20),bg="dodgerblue3")
            L3.place(x=10, y=140)
            def clear_answer():
                L3.destroy()
            Button_sample = Button(window, text="Clear answer",font=("Arial", 15),command=clear_answer)
            Button_sample.place(x=400, y=140)
        def clear1():
            E1.delete(0, END)
            E2.delete(0, END)
            E3.delete(0, END)
        B1 = Button(window, text="Submit", font=("Arial", 15), command=square_root)
        B1.place(x=10, y=100)
        B2 = Button(window, text="Clear", font=("Arial", 15), command=clear1)
        B2.place(x=100, y=100)
    square()
    def cube():
        L2 = Label(window, text="3rd degree: x^3 + x^2 + x + = 0", font=("Arial",20),bg="dodgerblue3")
        L2.place(x=10, y=190)
        E1 = Entry(window, font=("Arial", 20), width=3)
        E1.place(x=175, y=190)
        E2 = Entry(window, font=("Arial", 20), width=3)
        E2.place(x=300, y=190)
        E3 = Entry(window, font=("Arial", 20), width=3)
        E3.place(x=430, y=190)
        E4 = Entry(window, font=("Arial", 20), width=3)
        E4.place(x=530, y=190)
        def clear1():
            E1.delete(0, END)
            E2.delete(0, END)
            E3.delete(0, END)
            E4.delete(0, END)
        def cubic_root():
            coeficcients = [int(E1.get()), int(E2.get()), int(E3.get()), int(E4.get())]
            roots = numpy.roots(coeficcients)
            L3 = Label(window, text=f"x = {roots[0].round(2)}, {roots[1].round(2)},{roots[2].round(2)}",font=("Arial", 20), bg="dodgerblue3")
            L3.place(x=10, y=290)
            def clear_answer():
                L3.destroy()
            Button_sample =Button(window, text="Clear answer",font=("Arial", 15),command=clear_answer)
            Button_sample.place(x=550, y=290)
        B1 = Button(window, text="Submit", font=("Arial", 15), command=cubic_root)
        B1.place(x=10, y=240)
        B2 = Button(window, text="Clear", font=("Arial", 15), command=clear1)
        B2.place(x=100, y=240)
    cube()
    def four_degree():
        L2 = Label(window, text="4th degree: x^4 + x^3 + x^2 + x + = 0",font=("Arial", 20),bg="dodgerblue3")
        L2.place(x=10, y=340)
        E1 = Entry(window, font=("Arial", 20), width=3)
        E1.place(x=175, y=340)
        E2 = Entry(window, font=("Arial", 20), width=3)
        E2.place(x=300, y=340)
        E3 = Entry(window, font=("Arial", 20), width=3)
        E3.place(x=430, y=340)
        E4 = Entry(window, font=("Arial", 20), width=3)
        E4.place(x=550, y=340)
        E5 = Entry(window, font=("Arial", 20), width=3)
        E5.place(x=650, y=340)
        def clear1():
            E1.delete(0, END)
            E2.delete(0, END)
            E3.delete(0, END)
            E4.delete(0, END)
            E5.delete(0, END)
        def fourth_root():
            coeficcients = [int(E1.get()), int(E2.get()), int(E3.get()), int(E4.get()), int(E5.get())]
            roots = numpy.roots(coeficcients)
            L3 = Label(window,text=f"x = {roots[0].round(2)}, {roots[1].round(2)}, {roots[2].round(2)},{roots[3].round(2)}",font=("Arial", 20), bg="dodgerblue3")
            L3.place(x=10, y=440)
            def clear_answer():
                L3.destroy()
            Button_sample =Button(window, text="Clear answer",font=("Arial", 15),command=clear_answer)
            Button_sample.place(x=700, y=440)
        B1 = Button(window, text="Submit", font=("Arial", 15), command=fourth_root)
        B1.place(x=10, y=390)
        B2 = Button(window, text="Clear", font=("Arial", 15), command=clear1)
        B2.place(x=100, y=390)
    four_degree()
    window.mainloop()