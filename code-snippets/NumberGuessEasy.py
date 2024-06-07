import random
import time

number = random.randint(1, 25)
number = int(number)
guesses = 0                 # always set this to zero, it defines the current number of guesses played already
totalGuesses = 8            # Number of guesses player is allowed for

name = input("Hello! What is your name?? ")
print("Hi " + name + " I'm guessing a number between 1 and 25")
time.sleep(2.5)

lowAnswers = ["Higher"]
highAnswers = ["Lower"]

while guesses <= totalGuesses:
    guess = input("Guess a number ")
    guess = int(guess)
    guesses = guesses + 1   # guesses variable increases as more plays are counted

    if guess < number:
        print(random.choice(lowAnswers))

    if guess > number:
        print(random.choice(highAnswers))

    if guess == number:
        print("Congratulations, you beat me!")
        time.sleep(6)
        break

if guess != number:
    print("Sorry, you have reached your guess limit, you lost")
    print("The number i was thinking of is %s" % number)
    time.sleep(7)
