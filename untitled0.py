# -*- coding: utf-8 -*-
"""
Created on Wed Apr 15 22:53:13 2026

@author: lokes
"""

import speech_recognition as sr

listener = sr.Recognizer()

with sr.Microphone(device_index=2) as source:
    print("Speak something...")
    listener.adjust_for_ambient_noise(source, duration=2)
    audio = listener.listen(source)

print("Processing...")
try:
    text = listener.recognize_google(audio)
    print("You said:", text)
except Exception as e:
    print("Error:", e)