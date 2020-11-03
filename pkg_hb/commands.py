from utils import speak
import wikipedia
import webbrowser 
import datetime 


def handle_query(query):
    try:
        if 'wikipedia' in query: 
            speak('Searching Wikipedia...') 
            query = query.replace("wikipedia", "") 
            results = wikipedia.summary(query, sentences = 3) 
            speak("According to Wikipedia") 
            print(results) 
            speak(results) 

        elif 'open youtube' in query: 
            speak("Here you go to Youtube\n") 
            webbrowser.open("youtube.com") 

        elif 'open google' in query: 
            speak("Here you go to Google\n") 
            webbrowser.open("google.com") 

        elif 'open stackoverflow' in query: 
            speak("Here you go to Stack Over flow.Happy coding") 
            webbrowser.open("stackoverflow.com") 

        elif 'time' in query: 
            strTime = datetime.datetime.now().strftime("% H:% M:% S")	 
            speak(f"Sir, the time is {strTime}") 

        else:
            speak(f"Command {query} not recogonized")
    
    except Exception as e:
        print(f"Exception occured: {e}")