
import os
import pyttsx3
import speech_recognition as sr
import webbrowser

def logicofai(cinput):

    if cinput == "open youtube":
        webbrowser.open("www.youtube.com")
        print("Khol diya Bhai")
    elif cinput == "open google":
        webbrowser.open("www.google.com")
        print("Khol diya Bhai")
    elif cinput == "open twitter":
        webbrowser.open("www.twitter.com")
        print("Khol diya Bhai")
    elif cinput == "open insta":
        webbrowser.open("www.instagram.com") 
        print("Khol diya Bhai")
    elif cinput == "open fb":
        webbrowser.open("www.facebook.com")
        print("Khol diya Bhai")
    elif cinput == "open AISC":
        webbrowser.open("https://aistudent.community/dashboard")
        print("Khol diya Bhai")
    else:
        print(f"Bhai aap kya bol rhe h mujhe kuch \n samjh me nhi aa rha ")