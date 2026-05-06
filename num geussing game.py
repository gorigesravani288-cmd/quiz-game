# -*- coding: utf-8 -*-
"""
Created on Sat Apr  4 22:32:07 2026

@author: lokes
"""

import random
number = random.randint(1, 100)
print("Welcome to the Number Guessing Game!")
print("Guess a number between 1 and 100")
attempts = 0
while True:
    guess = int(input("Enter your guess: "))
    attempts += 1

    if guess < number:
        print("Too low! Try again.")
    
    elif guess > number:
        print("Too high! Try again.")
    
    else:
        print("🎉 Correct! You guessed the number.")
        print("Number of attempts:", attempts)
        break