import pyttsx3 #pip install pyttsx3
import speech_recognition as sr #pip install speechRecognition
import datetime
import wikipedia #pip install wikipedia
import webbrowser
import os
import smtplib
import pyaudio
import requests
import time


engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
#print(voices[1].id)
engine.setProperty('voice', voices[1].id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good Morning!")

    elif hour>=12 and hour<18:
        speak("Good Afternoon!")   

    else:
        speak("Good Evening!")  

def takeCommand():
    #It takes microphone input from the user and returns string output

    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognizing...")    
        query = r.recognize_google(audio, language='en-in')
        print(f"User said: {query}\n")

    except Exception as e:
        # print(e)    
        print("Say that again please...")  
        return "None"
    return query

def sendEmail(to, content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login('mail@gmail.com', 'password')
    server.sendmail('mail@gmail.com', to, content)
    server.close()

def basicDetails():
    speak("Let's Start with some basic information exchange. ")
    speak("Hi, I am your Cyber Pal")
    speak("What shall I call you?")
    query=takeCommand().lower()
    speak("Nice to meet you "+query+"How may I help you?")
    return query

if __name__ == "__main__":
    wishMe()
    name=basicDetails()
    while True:
    #if 1:
        query = takeCommand().lower()

        # Logic for executing tasks based on query
        if 'wikipedia' in query:
            speak('Searching Wikipedia...')
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=2)
            speak("According to Wikipedia")
            print(results)
            speak(results)

        elif 'can you do' in query:
            speak('I can open websites like Youtube, Google, Wikipedia and Music Player. Let me inform you todays time and date. What else am I forgetting? ')
            speak('Yes, I can ask you Riddles, tell you a joke and can suggest you some random activity.')
            speak("Well, I can even search on youtube and google too, which you want me to.")
            speak('I am at your service'+name)

        #search on youtube
        elif 'search on youtube' in query:
            innerquery = query.replace("search on youtube", "")
            speak("Searching "+innerquery)
            webbrowser.open("https://www.youtube.com/results?search_query="+innerquery)

        elif 'open youtube' in query:
            speak("Opening Youtube")
            webbrowser.open("youtube.com")

        elif 'open google' in query:
            speak("Opening Google")
            webbrowser.open("google.com")

        elif 'open music player' in query:
            speak("Opening WYNk player")
            webbrowser.open("https://wynk.in/music")   

        elif 'the time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")    
            speak(f"Sir, the time is {strTime}")

        #suggest random activity
        elif 'random activity' in query:
            response = requests.get('https://www.boredapi.com/api/activity')
            data=response.json()
            print(data['activity'])
            speak(data['activity'])

        #riddles
        elif 'riddle' in query:
            response = requests.get('https://riddles-api.vercel.app/random')
            data=response.json()
            print(data['riddle'])
            speak(data['riddle'])
            print("You have 10 seconds to guess the answer")
            speak("You have 10 seconds to guess the answer")
            
            time.sleep(10)
            print("here is the answer")
            print(data["answer"])
            speak(data["answer"])
        
        #random joke
        elif 'joke' in query:
            response = requests.get('https://icanhazdadjoke.com/slack')
            data=response.json()
            jokeText=str(data['attachments'])
            joke=jokeText[jokeText.find('text')+6:-2]
            print(joke)
            speak(joke)

        elif 'email to riya' in query:
            try:
                speak("What should I say?")
                content = takeCommand()
                to = "riyatyagi@gmail.com"    
                sendEmail(to, content)
                speak("Email has been sent!")
            except Exception as e:
                print(e)
                speak("Sorry my friend riya. I am not able to send this email")  

        else:
            speak("Searching "+query)
            webbrowser.open("https://www.google.com/search?q="+query)
        
                
