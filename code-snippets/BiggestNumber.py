# Biggest number
# Returns the biggest number from 3 user inoutted integers

import time

num1 = int(input("Please input the first number: "))
num2 = int(input("Please input the second number: "))
num3 = int(input("Please input the third number: "))

if (num1 > num2 and num1 > num3):
    print("The largest number is %s" % num1)
    time.sleep(6)
    
if (num2 > num1 and num2 > num3):
    print("The largest number is %s" % num2)
    time.sleep(6)
    
if (num3 > num1 and num3 > num2):
    print("The largest number is %s" % num3)
    time.sleep(6)
