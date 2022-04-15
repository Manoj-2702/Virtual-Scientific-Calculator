from tkinter import *
import math
import cmath
import sympy
import numpy


def complex_calculator():
    def click(value):
        ex = entryField.get()
        answer = ''
        try:
            if value == 'C':
                ex = ex[0:len(ex) - 1] # 78
                entryField.delete(0, END)
                entryField.insert(0, ex)
                return
            elif value == 'CE':
                entryField.delete(0, END)
            elif value == 'π':
                answer = ex + str(round(math.pi, 4))
            elif value == 'cos':
                answer1 = cmath.cos(complex(ex))
                answer = round(answer1.real, 4) + round(answer1.imag, 4) * 1j
            elif value == 'tan':
                answer1 = cmath.tan(complex(ex))
                answer = round(answer1.real, 2) + round(answer1.imag, 2) * 1j
            elif value == 'sin':
                answer1 = cmath.sin(complex(ex))
                answer = round(answer1.real, 2) + round(answer1.imag, 2) * 1j
            elif value == 'acos':
                answer1 = cmath.acos(complex(ex))
                answer = round(answer1.real, 2) + round(answer1.imag, 2) * 1j
            elif value == 'atan':
                answer1 = cmath.atan(complex(ex))
                answer = round(answer1.real, 2) + round(answer1.imag, 2) * 1j
            elif value == 'asin':
                answer1 = cmath.asin(complex(ex))
                answer = round(answer1.real, 2) + round(answer1.imag, 2) * 1j
            elif value == 'x\u00B2':
                answer1 = complex(ex) ** 2
                answer = round(answer1.real, 4) + round(answer1.imag, 4) * 1j
            elif value == 'ln':
                answer1 = cmath.log(complex(ex))
                answer = round(answer1.real, 4) + round(answer1.imag, 4) * 1j
            elif value == 'log₁₀':
                answer1 = cmath.log(complex(ex))
                answer = round(answer1.real, 4) + round(answer1.imag, 4) * 1j
            elif value == '=':
                if "j" in ex:
                    answer = ex
                    for i in range(0, len(ex)):
                        if ex[i] == "-" or ex[i] == "*" or ex[i] == "/" or ex[i] == "+" or ex[i] == "^":
                            if ex[i - 1] == ")":l, r = complex(ex[:i]), complex(ex[i + 1:])
                    if ex[i] == "+":
                        answer = l + r
                    elif ex[i] == "-":
                        answer = l - r
                    elif ex[i] == "*":
                        answer = l * r
                    elif ex[i] == "^":
                        answer = l ** r
                    else:
                        answer = l / r
                        answer = round(answer.real, 4) + round(answer.imag, 4) * 1j
                else:
                    answer = eval(str(ex))
            elif value == "real":
                answer = round(complex(ex).real, 4)
            elif value == "imag":
                answer = round(complex(ex).imag, 4)
            elif value == "phase":
                answer = round(cmath.phase(complex(ex)), 4)
            elif value == "rect":
                list1 = ex.split(",")
                a = list1[0].strip("(")
                b = list1[1].strip(")")
                c = b.strip(" ")
                tuple1 = (a, c)
                answer1 = cmath.rect(float(tuple1[0]), float(tuple1[1]))
                answer = round(answer1.real, 4) + round(answer1.imag, 4) * 1j
            elif value == "mod":
                answer1 = cmath.polar(complex(ex))
                answer = round(answer1[0], 4)
            elif value == chr(247):
                answer = ex + "/"
            elif value == "exp":
                answer1 = cmath.exp(complex(ex))
                answer = round(answer1.real, 4) + round(answer1.imag, 4) * 1j
            elif value == "√":
                answer1 = cmath.sqrt(complex(ex))
                answer = round(answer1.real, 4) + round(answer1.imag, 4) * 1j
            else:
                entryField.insert(END, str(value))
                return
            entryField.delete(0, END)
            entryField.insert(0, str(answer))
        except SyntaxError:
            entryField.delete(0, END)
            entryField.insert(0, "Syntax error")
        except ValueError:
            entryField.delete(0, END)
            entryField.insert(0, "Value Error")
        except ZeroDivisionError:
            entryField.delete(0, END)
            entryField.insert(0, "Zero division Error")
    window = Tk()
    window.title('Complex Calculator')
    window.config(bg='light sea green')
    window.geometry('680x486+100+100')
    entryField = Entry(window, font=('arial', 20, 'bold'), bg="turquoise", fg='black', bd=10,relief=SUNKEN, width=30)
    entryField.grid(row=0, column=0, columnspan=8)
    button_list = ["C", "CE", "j", "+", "(", "real", "imag", "phase","1", "2", "3", "-", ")", "mod", "rect", ",","4", "5", "6", "*", "√", "π", "x\u00B2", "exp","7", "8", "9", chr(247), "ln", "sin", "cos", "tan","0", ".", "^", "=", "log₁₀", "asin", "acos", "atan"]
    rowvalue = 1
    columnvalue = 0
    for i in button_list:
        button = Button(window, width=5, height=2, bd=2, relief=SUNKEN, text=i, bg='turquoise',fg='black',font=('arial', 18, "bold"), activebackground='dodgerblue', command=lambda button=i:click(button))
        button.grid(row=rowvalue, column=columnvalue, pady=1)
        columnvalue += 1
        if columnvalue > 7:
            rowvalue += 1
            columnvalue = 0
    window.mainloop()