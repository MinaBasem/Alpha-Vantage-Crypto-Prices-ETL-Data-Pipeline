import time

count = 0

number = int(input("Number to generate the multiplication table of: "))
fullMultiplications = int(input("Number of multiplications to show: "))
print("")

while count <= fullMultiplications:
    result = number * count
    print("| " , number , " x " , count , " = " , result , " |")
    count = count + 1

time.sleep(100)
