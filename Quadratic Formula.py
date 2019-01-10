import math
import os
import sys

def sqr():
    a = float(input("a: "))
    b = float(input("b: "))
    c = float(input("c: "))

    num1 = b * -1
    num2 = ((b) * (b)) - 4 * a * c
    den = 2 * a

    if num2 <= 0:
        print("No solution")
        rst = input("Press ENTER to restart")
        sqr()

    positive = str((num1 + math.sqrt(num2)) / den)
    negative = str((num1 - math.sqrt(num2)) / den)
        
    print("-----------------------")
    print("X = " + positive)
    print("X = " + negative)
    print("-----------------------")
        
    ext = input("Press ENTER to restart")
    os.system('cls')
    sqr()

sqr()

