import subprocess 
import pyttsx3 
import json 
import random 
import operator 
import speech_recognition as sr 
import datetime 
import os 
import shutil
from commands import handle_query
from utils import clean, speak


ASSISTANT_NAME = "bhagwan"
  
def salutation(): 
    hour = int(datetime.datetime.now().hour) 
    if hour>= 0 and hour<12: 
        speak("Good Morning Sir !") 
   
    elif hour>= 12 and hour<18: 
        speak("Good Afternoon Sir !")    
   
    else: 
        speak("Good Evening Sir !")   
   
    assname =("Bhagwan 1 point o") 
    speak("I am your Assistant") 
    speak(assname) 

  
def takeCommand(): 
      
    r = sr.Recognizer() 

    try:
        with sr.Microphone(device_index = 18) as source:
            r.adjust_for_ambient_noise(source)
            print("Listening ...")
            audio = r.listen(source)

            query = r.recognize_google(audio)
            query = query.lower()

            print(f"Did you say {query}")
            return query.lower()

    except sr.RequestError as e:
        print("Could not request results; {0}".format(e))
    
    except sr.UnknownValueError:
        print("unknown error occured") 
    
    except Exception as e:
        print (e)

def main(): 
    clean() 
    salutation() 

    while True: 

        query = takeCommand() 
        if ASSISTANT_NAME in query:
            query = takeCommand()
            handle_query(query)