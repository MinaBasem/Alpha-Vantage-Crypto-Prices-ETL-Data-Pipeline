
import random
import time

number = random.randint(1, 25)
number = int(number)
guesses = 0

name = input("Hello! What is your name?? ")
print("Hi " + name + " I'm guessing a number between 1 and 25")
time.sleep(2.5)

lowAnswers = ["This is a little bit low, try a bigger number", "Try a bigger number please", "Try a bigger number", "Number is bigger than that"]
highAnswers = ["This is kinda high try a smaller number", "Try a smaller number", "Number is large, try a smaller one", "The number i am guessing is lower"]

while guesses <= 8:
    guess = input("Guess a number ")
    guess = int(guess)
    guesses = guesses + 1

    if guess < number:
        print(random.choice(lowAnswers))

    if guess > number:
        print(random.choice(highAnswers))

    if guess == number:
        print("Chongratulations, you beat me!")
        time.sleep(6)
        break

if guess != number:
    print("Sorry, you have reached your guess limit, you lost")
    print("The number i was thinking of is %s" % number)
    time.sleep(7)
