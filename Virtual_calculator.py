from tkinter import *
import math
import cmath
import sympy
import cv2
from cvzone.HandTrackingModule import HandDetector
import numpy


def virtual_calculator():
    class Button:
        def __init__(self, pos, width, height, value):
            self.pos = pos
            self.width = width
            self.height = height
            self.value = value

        def draw(self, img):
            cv2.rectangle(
                img, self.pos, (self.pos[0] + self.width, self.pos[1] + self.height), (140, 0, 0))
            cv2.rectangle(
                img, self.pos, (self.pos[0] + self.width, self.pos[1] + self.height), (0, 0, 0), 4)
            cv2.putText(
                img, self.value, (self.pos[0] + 20, self.pos[1] + 30), cv2.FONT_HERSHEY_PLAIN, 2, (255, 0, 0), 2)

        def checkclick(self, x, y):
            if self.pos[0] < x < self.pos[0] + self.width and \
                    self.pos[1] < y < self.pos[1] + self.height:
                cv2.rectangle(
                    img, self.pos, (self.pos[0] + self.width, self.pos[1] + self.height), (250, 250, 250), cv2.FILLED)
                cv2.rectangle(
                    img, self.pos, (self.pos[0] + self.width, self.pos[1] + self.height), (0, 0, 0), 4)
                cv2.putText(
                    img, self.value, (self.pos[0] + 20, self.pos[1] + 30), cv2.FONT_HERSHEY_PLAIN, 2, (0, 0, 0), 2)
                return True
            else:
                return False
 # Webcam
    cap = cv2.VideoCapture(0)
    cap.set(3, 1350)
    cap.set(4, 1000)
    detector = HandDetector(detectionCon=0.8, maxHands=1)
 # creating button
    buttonList1 = [['C', 'CE', "sqrt", "+", "cos", "tan", "sin"], ['7', "8", "9", "-", "acos", "asin", "atan"], ["4", "5", "6", "*", 'cosh', 'tanh', "sinh"],
                   ["1", "2", "3", "/", "sec", "cosec", "cot"],
                   ["0", ".", "2^x", "=", "x^y", "x^2", "x^3"],
                   ["(", ")", "pi", "2pi", "|x|", "e^x", "1/x"],
                   ["e", "log10", "ln", "rad", "deg", "10^x", "x!"]]
    buttonList = []
    for x in range(7):
        for y in range(7):
            xpos = x * 120 + 300
            ypos = y * 50 + 200
            buttonList.append(Button((xpos, ypos), 120, 50, buttonList1[y][x]))
    myEquation = ""
    delayCounter = 0
    while True:
        # nonlocal lmList
        success, img = cap.read()
        img = cv2.flip(img, 1)
        # detection of hand
        hands, img = detector.findHands(img, flipType=False)
        # draw all buttons
        cv2.rectangle(img, (300, 120), (500 + 640, 120 + 80), (0, 0, 0))
        cv2.rectangle(img, (300, 120), (500 + 640, 120 + 80), (0, 0, 0), 4)
        for button in buttonList:
            button.draw(img)

        # Check for Hand
        if hands:
            lmList = hands[0]["lmList"]
            length, _, img = detector.findDistance(lmList[8], lmList[12], img)
        
            x, y = lmList[8]
            if length < 70:
                for i, button in enumerate(buttonList):
                    if button.checkclick(x, y) and delayCounter == 0:
                        my_value = (buttonList1[int(i % 7)][int(i / 7)])
                        try:
                            if my_value == 'C':
                                myEquation = myEquation[0:len(myEquation) - 1]
                            elif my_value == "CE":
                                myEquation = ""
                            elif my_value == "sqrt":
                                myEquation = round(
                                    math.sqrt(eval(str(myEquation))), 4)
                            elif my_value == 'pi':
                                myEquation = myEquation + str(round(math.pi, 4))
                            elif my_value == 'cos':
                                myEquation = round(
                                    math.cos(math.radians(eval(str(myEquation)))), 4)
                            elif my_value == 'tan':
                                myEquation = round(
                                    math.tan(math.radians(eval(str(myEquation)))), 4)
                            elif my_value == 'sin':
                                myEquation = round(
                                    math.sin(math.radians(eval(str(myEquation)))), 4)
                            elif my_value == 'cosh':
                                myEquation = round(
                                    math.cosh(eval(str(myEquation))), 4)
                            elif my_value == 'tanh':
                                myEquation = round(
                                    math.tanh(eval(str(myEquation))), 4)
                            elif my_value == 'sinh':
                                myEquation = round(
                                    math.sinh(eval(str(myEquation))), 4)
                            elif my_value == "x^y":
                                myEquation = str(myEquation) + "**"
                            elif my_value == "x!":
                                myEquation = math.factorial(
                                    int(eval(str(myEquation))))
                            elif my_value == 'log10':
                                myEquation = round(math.log10(
                                    int(eval(str(myEquation)))), 4)
                            elif my_value == "ln":
                                myEquation = round(
                                    math.log(int(eval(str(myEquation)))), 4)
                            elif my_value == "=":
                                myEquation = round(float(eval(str(myEquation))), 4)
                            elif my_value == "e":
                                myEquation = myEquation + str(round(math.e, 4))
                            elif my_value == "2pi":
                                myEquation = str(myEquation) + \
                                    str(round(2 * math.pi, 4))
                            elif my_value == "acos":
                                myEquation = round(
                                    math.acos((eval(str(myEquation)))), 4)
                            elif my_value == "asin":
                                myEquation = round(
                                    math.asin((eval(str(myEquation)))), 4)
                            elif my_value == "atan":
                                myEquation = round(
                                    math.atan((eval(str(myEquation)))), 4)
                            elif my_value == "sec":
                                myEquation = round(
                                    1 / math.cos(math.radians(eval(str(myEquation)))), 4)
                            elif my_value == "cosec":
                                myEquation = round(
                                    1 / math.sin(math.radians(eval(str(myEquation)))), 4)
                            elif my_value == "cot":
                                myEquation = round(
                                    1 / math.tan(math.radians(eval(str(myEquation)))), 4)
                            elif my_value == "e^x":
                                myEquation = str(myEquation) + \
                                    str(round(math.e, 4)) + "**"
                            elif my_value == "2^x":
                                myEquation = str(myEquation) + "2**"
                            elif my_value == "x^2":
                                myEquation = round(
                                    (float(eval(str(myEquation))) ** 2), 4)
                            elif my_value == "x^3":
                                myEquation = round(
                                    (float(eval(str(myEquation))) ** 3), 4)
                            elif my_value == "|x|":
                                myEquation = round(
                                    math.fabs(float(eval(str(myEquation)))), 4)
                            elif my_value == "1/x":
                                myEquation = round(
                                    1 / float(eval(str(myEquation))), 4)
                            elif my_value == "10^x":
                                myEquation = str(myEquation) + "10**"
                            elif my_value == "rad":
                                myEquation = round(math.radians(
                                    float(eval(str(myEquation)))), 4)
                            elif my_value == "deg":
                                myEquation = round(math.degrees(
                                    float(eval(str(myEquation)))), 4)
                            else:
                                myEquation = str(myEquation) + my_value
                        except ZeroDivisionError:
                            myEquation = "Division by 0 invalid"
                        except SyntaxError:
                            myEquation = "Syntax error"
                        except TypeError:
                            myEquation = "Type Error"
                        except ValueError:
                            myEquation = "Value Error "
                        delayCounter = 3
                # Avoid repitions:
                if delayCounter != 0:
                    delayCounter += 1
                    if delayCounter > 10:
                        delayCounter = 0
                # Display equation
                cv2.putText(img, str(myEquation), (300 + 20, 120 + 50),
                            cv2.FONT_HERSHEY_PLAIN, 2.5, (0, 0, 235), 2)
                # Display image
                cv2.imshow("image", img)
                key = cv2.waitKey(1)
                if key == ord("C"):
                    cv2.destroyAllWindows()
                    break
