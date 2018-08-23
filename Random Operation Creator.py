
# Author: Mina Basem

from tkinter import *
import sys
import time
import random
import tkinter.messagebox

def num1():
    global num1
    num1 = random.randint(1, 101)
    num1 = int(num1)
    print(num1)

def num2():
    global num2
    num2 = random.randint(1, 101)
    num2 = int(num2)
    print(num2)

def operator():
    global operators
    operators = ['+', '-', '/', '*']
    global random_operator
    random_operator = random.choice(operators)
    print(random_operator)

def exit():
    sys.exit()

def calculate():
    if random_operator == operators[0]:
        answer1 = num1 + num2
        tkinter.messagebox.showinfo("Answer", answer1)
        print("Answer: %s" % answer1)

    if random_operator == operators[1]:
        answer2 = num1 - num2
        tkinter.messagebox.showinfo("Answer", answer2)
        print("Answer: %s" % answer2)

    if random_operator == operators[2]:
        answer3 = num1 / num2
        tkinter.messagebox.showinfo("Answer", answer3)
        print("Answer: %s" % answer3)

    if random_operator == operators[3]:
        answer4 = num1 * num2
        tkinter.messagebox.showinfo("Answer", answer4)
        print("Answer: %s" % answer4)
    

root = Tk()

frame_one = Frame(root)
frame_one.pack()

frame_two = Frame(root)
frame_two.pack()

button_one = Button(frame_one, text="Number", command=num1, bg="black", fg="white", width="15")
button_one.pack()

operator_button = Button(frame_two, text="Operator", command=operator, bg="yellow", fg="black", width="15")
operator_button.pack()

button_two = Button(frame_two, text="Number", command=num2, bg="black", fg="white", width="15")
button_two.pack()

calculate = Button(frame_two, text="Calculate", command=calculate, bg="green", fg="black", width="15")
calculate.pack()

exit_Button = Button(frame_two, text="Exit", command=exit, bg="red", fg="white", width="15")
exit_Button.pack()


root.mainloop()
