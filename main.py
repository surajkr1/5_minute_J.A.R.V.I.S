
from logics import *

jarvis = pyttsx3.init('sapi5')
voices = jarvis.getProperty('voices')
jarvis.setProperty('voice', voices[0].id)

def speak(text):
    jarvis.say(words)
    jarvis.runAndWait()

def cmdinput():
    cinput = input("Command : ")
    logicofai(cinput)


while True:
    cmdinput()




