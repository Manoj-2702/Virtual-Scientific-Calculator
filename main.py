from tkinter import *
import math
import cv2
from cvzone.HandTrackingModule import HandDetector
import numpy
from Simultaneous import simultaneous_equation_solver
from Rootfinder import root_finder
from Virtual_calculator import virtual_calculator
from Derivative import calculus
from complex_calci import complex_calculator
from Volume import volume_finder
from Area import Area_finder
import cmath
import sympy


def click(value):
    ex = entryField.get()
    answer = ''
    try:
        if value == 'C':
            ex = ex[0:len(ex) - 1]
            entryField.delete(0, END)
            entryField.insert(0, ex)
            return
        elif value == 'CE':
            entryField.delete(0, END)
        elif value == '√':
            answer = round(math.sqrt(eval(ex)), 4)
        elif value == 'π':
            answer = str(ex) + str(round(math.pi, 4))
        elif value == 'cosθ':
            answer = round(math.cos(math.radians(eval(ex))), 4)
        elif value == 'tanθ':
            answer = round(math.tan(math.radians(eval(ex))), 4)
        elif value == 'sinθ':
            answer = round(math.sin(math.radians(eval(ex))), 4)
        elif value == '2π':
            answer = str(ex) + str(round(2 * math.pi, 4))
        elif value == 'cosh':
            answer = round(math.cosh(eval(ex)), 4)
        elif value == 'tanh':
            answer = round(math.tanh(eval(ex)), 4)
        elif value == 'sinh':
            answer = round(math.sinh(eval(ex)), 4)
        elif value == chr(8731):
            answer = round(eval(ex) ** (1 / 3), 4)
        elif value == 'x\u02b8': # 7**2
            entryField.insert(END, '**')
            return
        elif value == 'x\u00B3':
            answer = round(eval(ex) ** 3, 4)
        elif value == 'x\u00B2':
            answer = round(eval(ex) ** 2, 4)
        elif value == 'ln':
            answer = round(math.log(eval(ex)), 4)
        elif value == 'deg':
            answer = round(math.degrees(eval(ex)), 4)
        elif value == "rad":
            answer = round(math.radians(eval(ex)), 4)
        elif value == 'e':
            answer = str(ex) + str(round(math.e, 4))
        elif value == 'log₁₀':
            answer = round(math.log10(eval(ex)), 4)
        elif value == 'x!':
            answer = math.factorial(int(ex))
        elif value == chr(247): # 7/2=3.5
            entryField.insert(END, "/")
            return
        elif value == '=':
            answer = round(eval(str(ex)), 4)
        else:
            entryField.insert(END, str(value))
            return
        entryField.delete(0, END)
        entryField.insert(0, str(answer))
    except SyntaxError:
        entryField.delete(0, END)
        entryField.insert(0, "Syntax Error")
    except ZeroDivisionError:
        entryField.delete(0, END)
        entryField.insert(0, "Zero division Error")
    except ValueError:
        entryField.delete(0, END)
        entryField.insert(0, "Value Error")
        
root = Tk()
root.title('Scientific Calculator')
root.config(bg='SpringGreen2')
root.geometry('680x486+100+100')
entryField = Entry(root, font=('arial', 20, 'bold'), bg="SpringGreen3", fg='black', bd=10,relief=SUNKEN, width=30)
entryField.grid(row=0, column=0, columnspan=8)
button_text_list = ["C", "CE", "√", "+", "π", "cosθ", "tanθ", "sinθ",
 "1", "2", "3", "-", "2π", "cosh", "tanh", "sinh",
 "4", "5", "6", "*", chr(8731), "x\u02b8", "x\u00B3", "x\u00B2",
 "7", "8", "9", chr(247), "ln", "deg", "rad", "e",
 "0", ".", "%", "=", "log₁₀", "(", ")", "x!"]
rowvalue = 1
columnvalue = 0
for i in button_text_list:
    button = Button(root, width=5, height=2, bd=2, relief=SUNKEN, text=i, bg="SpringGreen3",fg='black',font=('arial', 18, 'bold'), activebackground='dodgerblue', command=lambda button=i:click(button))
    button.grid(row=rowvalue, column=columnvalue, pady=1)
    columnvalue += 1
    if columnvalue > 7:
        rowvalue += 1
        columnvalue = 0
menubar = Menu(root)
filemenu = Menu(menubar, tearoff=0)
filemenu.add_command(label="Simultaneous equation solver",command=simultaneous_equation_solver)
filemenu.add_command(label="Rootfinder", command=root_finder)
filemenu.add_command(label="Virtual Calculator", command=virtual_calculator)
filemenu.add_command(label="Derivative", command=calculus)
filemenu.add_command(label="Complex Calculator", command=complex_calculator)
filemenu.add_command(label="Volume finder", command=volume_finder)
filemenu.add_command(label="Area finder", command=Area_finder)
filemenu.add_separator()
filemenu.add_command(label="Exit", command=root.quit)
menubar.add_cascade(label="Functions", menu=filemenu)
root.config(menu=menubar)
root.mainloop()



