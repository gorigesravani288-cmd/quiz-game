# -*- coding: utf-8 -*-
"""
Created on Mon Apr 13 23:14:12 2026

@author: lokes
"""

import pyttsx3

engine = pyttsx3.init()
engine.say("heloo welcome!")
engine.runAndWait()
engine.setProperty('rate', 50)
import speech_recognition as sr
import pyttsx3
import datetime
import wikipedia
import pywhatkit
import time

engine = pyttsx3.init()
listener = sr.Recognizer()

def talk(text):
    print("Alexa:", text)
    engine.say(text)
    engine.runAndWait()

def take_command():
   def take_command():
    command = ""
    try:
        with sr.Microphone(device_index=2) as source: 
            print("Listening... Speak now 🎤")

            listener.adjust_for_ambient_noise(source, duration=2)
            listener.energy_threshold = 300
            listener.pause_threshold = 0.8

            voice = listener.listen(source,phrase_time_limit=5)

            command = listener.recognize_google(voice)
            command = command.lower()

            print("You said:", command)

            if "alexa" in command:
                command = command.replace("alexa", "")

            return command

    except Exception as e:
        print("Error:", e)
        return ""


def run_alexa():
    command = take_command()

    if not command == "":
        return   # 

    if "time" in command:
        time_now = datetime.datetime.now().strftime('%I:%M %p')
        talk("Current time is " + time_now)

    elif "who is" in command:
        person = command.replace("who is", "")
        try:
            info = wikipedia.summary(person, 1)
            talk(info)
        except:
            talk("Sorry, I couldn't find information")

    elif "play" in command:
        song = command.replace("play", "")
        talk("Playing " + song)
        pywhatkit.playonyt(song)

    elif "hello" in command:
        talk("Hello! How can I help you?")

    elif "stop" in command or "exit" in command:
        talk("Goodbye!")
        exit()

    else:
        talk("I didn't understand that")


talk("Hello, I am your mini Alexa")

while True:
    run_alexa()
    time.sleep(2)