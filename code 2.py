# -*- coding: utf-8 -*-
"""
Created on Mon Apr 13 23:08:14 2026

@author: lokes
"""

import pyttsx3

engine = pyttsx3.init()
engine.say("hello nishanth")
engine.runAndWait()
engine.setProperty('rate', 100)
