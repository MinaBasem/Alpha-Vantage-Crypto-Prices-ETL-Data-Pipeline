import time

def loading():
    for x in range(0,5):
        b = "Loading" + "." * x
        print(b, end="\r")
        time.sleep(0.2)

loading()