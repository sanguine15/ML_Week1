# Simple Number Guessing Game

import random

secret = random.randint(1, 20)

print("Guess the number between 1 and 20. You have 5 attempts.")

for i in range(5):
    try:
        guess = int(input(f"Attempt {i+1}: "))
    except ValueError:
        print("Invalid input! Please enter a number.")
        continue

    if guess == secret:
        print("Congratulations! You guessed it right.")
        break
    elif guess < secret:
        print("Too low!")
    else:
        print("Too high!")
else:
    print(f"Sorry, the correct number was {secret}.")
