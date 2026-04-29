# Number Guessing Game

import random

for attempt in range(5):
    guess=random.randint(1,51)
    user=int(input("Enter a number:"))
    if user==guess:
        print("Congratulations! You guessed the number correctly.")
        break
    if user>guess:
        print("Your guess is too high.")
    else:
        print("Your guess is too low.")
    remaining = 4 - attempt
    if remaining > 0:
        print("Wrong guess.",remaining, "attempt(s) remaining.")
    else:     
        print("Maximum attempts reached.")
        print("Game over! The correct number was",guess)