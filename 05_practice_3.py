# pip install pyttsx3

import pyttsx3
engine = pyttsx3.init()
""" RATE"""
rate = engine.getProperty('rate')   # getting details of current speaking rate
print (rate)                        #printing current voice rate
engine.setProperty('rate', 1)     # setting up new voice rate
engine.say("Hello Sir i am python module. Welcome to the world of Python")
engine.runAndWait()