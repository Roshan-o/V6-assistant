import pyttsx3
#text to speech converter module
from decouple import config
from datetime import datetime

import speech_recognition as sr
from ran import random_text
from random import choices #this will make the random text to be selected
USER='KRL'
HOSTNAME='BOT'


engine=pyttsx3.init('sapi5')

engine.setProperty('volume',1.5)
engine.setProperty('rate',225)
voices=engine.getProperty('voices')
engine.setProperty('voices',voices[1].id)
def speak(text):
    engine.say(text)
    engine.runAndWait()

def greet_me():
    hour=datetime.now().hour
    if(hour<=6)and(hour<12):
        speak(f"good morning{USER}")
    elif(hour>=12)and(hour<=19):
        speak(f"good afternoon{USER}")
    else:
        speak(f"good evening{USER}")

def take_command():
    r=sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening....")
        r.pause_threshold=1
        audio=r.listen(source)
    try:
        print("Recognising....")
        query=r.recognize_google(audio,language="en-in")
        print(query)
        if not 'stop' in query or not 'exit' in query:
            speak(choices(random_text))
        else:
            hour = datetime.now().hour
            if hour>=21 and hour<6:
                speak(f"good night{USER}")
            else:
                speak("have a good day")
            exit()
    except Exception:
        speak("can't able to recognise the voice")
        query="None"
    return query.lower()




