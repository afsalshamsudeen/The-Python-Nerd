#a simple  guess the number game to understand more about python

import random

print("Welcome to the Worlds BEST number guesser game!")
max_range = input("Enter a Number: ")
guesses = 0
if max_range.isdigit():
    max_range = int(max_range)

    if max_range <= 0:
        print("Please Enter a Number Larger Than ZERO")
else:
    print("Enter a Number Next Time")
    quit()

random_number = random.randint(0, max_range)

while True:
    guesses += 1
    user_guess = input("Make a Guess: ")
    if user_guess.isdigit():
        user_guess = int(user_guess)
    else:
        print("Enter a number next time")
        continue
    if user_guess == random_number:
        print("You Got It Correct!")
        break
    elif user_guess > random_number:
        print("The Guess is greater than the original number")
    else:
        print("Your guess is lower that the original number")

print("Bravo! you got it in", guesses, "guesses.")