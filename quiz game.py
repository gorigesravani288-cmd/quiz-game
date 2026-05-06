# -*- coding: utf-8 -*-
"""
Created on Sat Apr  4 22:48:32 2026

@author: sravani
"""

score = 0

print("Welcome to the Quiz Game!")
print("1. What is the capital of India?")
answer = input("Your answer: ").lower()
if answer == "delhi":
    print("Correct!")
    score += 1
else:
    print("Wrong! Correct answer is Delhi")
print("\n2. Which language is used for AI?")
answer = input("Your answer: ").lower()
if answer == "python":
    print("Correct!")
    score += 1
else:
    print("Wrong! Correct answer is Python")
print("\n3. 5 + 3 = ?")
answer = input("Your answer: ")

if answer == "8":
    print("Correct!")
    score += 1
else:
    print("Wrong! Correct answer is 8")
print("\n4. Who is known as the father of computers?")
answer = input("Your answer: ").lower()

if answer == "charles babbage":
    print("Correct!")
    score += 1
else:
    print("Wrong! Correct answer is Charles Babbage")
print("\n Your final score is:", score, "/ 4")
