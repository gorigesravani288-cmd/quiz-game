# -*- coding: utf-8 -*-
import tkinter as tk

# Questions and answers
questions = [
    ("What is the capital of India?", ["Delhi", "Mumbai", "Chennai", "Kolkata"], "Delhi"),
    ("2 + 2 = ?", ["3", "4", "5", "6"], "4"),
    ("Which language is used for AI?", ["Python", "HTML", "CSS", "C"], "Python")
]

score = 0
q_index = 0

def check_answer(answer):
    global score, q_index
    if answer == questions[q_index][2]:
        score += 1
    q_index += 1
    load_question()

def load_question():
    if q_index < len(questions):
        question, options, _ = questions[q_index]
        question_label.config(text=question)

        for i in range(4):
            buttons[i].config(text=options[i],
                              command=lambda opt=options[i]: check_answer(opt))
    else:
        question_label.config(text=f"Quiz Finished! Score: {score}/{len(questions)}")
        for btn in buttons:
            btn.pack_forget()

# GUI setup
root = tk.Tk()
root.title("Quiz Game")

question_label = tk.Label(root, text="", font=("Arial", 14))
question_label.pack(pady=20)

buttons = []
for i in range(4):
    btn = tk.Button(root, text="", width=20)
    btn.pack(pady=5)
    buttons.append(btn)

load_question()
root.mainloop()