import subprocess
import wolframalpha
import pyttsx3
import json
import random
import speech_recognition as sr
import datetime
import wikipedia
import webbrowser
import os
import pyjokes
import requests
import ctypes
import time
from ecapture import ecapture as ec

# Initialize the text-to-speech engine
engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour < 12:
        speak("Good Morning Sir!")
    elif hour < 18:
        speak("Good Afternoon Sir!")
    else:
        speak("Good Evening Sir!")
    
    assname = "Jarvis"
    speak(f"I am your Assistant {assname}. How can I assist you today?")

def username():
    speak("What should I call you, Sir?")
    uname = takeCommand()
    speak(f"Welcome Mister {uname}")
    print(f"Welcome Mr. {uname}")
    speak("How can I help you today, Sir?")

def takeCommand():
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
        print(e)
        print("Unable to recognize your voice.")
        return "None"
    
    return query

def search_web(query):
    webbrowser.open(f"https://www.google.com/search?q={query}")

if __name__ == '__main__':
    os.system('cls' if os.name == 'nt' else 'clear')
    wishMe()
    username()
    
    while True:
        query = takeCommand().lower()
        
        # Wikipedia search
        if 'wikipedia' in query:
            speak('Searching Wikipedia...')
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=3)
            speak("According to Wikipedia")
            print(results)
            speak(results)

        # Open popular websites
        elif 'open youtube' in query:
            speak("Here you go to YouTube")
            webbrowser.open("youtube.com")

        elif 'open google' in query:
            speak("Opening Google")
            webbrowser.open("google.com")

        elif 'open facebook' in query:
            speak("Opening Facebook")
            webbrowser.open("facebook.com")

        elif 'open twitter' in query:
            speak("Opening Twitter")
            webbrowser.open("twitter.com")

        elif 'open instagram' in query:
            speak("Opening Instagram")
            webbrowser.open("instagram.com")

        # Play music
        elif 'play music' in query or "play song" in query:
            music_dir = "C:\\Users\\GAURAV\\Music"  # Change this to your music directory
            songs = os.listdir(music_dir)
            if songs:
                os.startfile(os.path.join(music_dir, random.choice(songs)))
            else:
                speak("No songs found in the directory.")

        # Check the time
        elif 'the time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"Sir, the time is {strTime}")

        # System functionalities (Shutdown, Lock, Hibernate, Log off)
        elif 'shutdown system' in query:
            speak("Hold On a Sec! Your system is shutting down")
            subprocess.call('shutdown /p /f')

        elif 'lock window' in query:
            speak("Locking the device")
            ctypes.windll.user32.LockWorkStation()

        elif "hibernate" in query or "sleep" in query:
            speak("Hibernating")
            subprocess.call("shutdown /h")

        elif "log off" in query or "sign out" in query:
            speak("Make sure all applications are closed before sign-out")
            time.sleep(5)
            subprocess.call(["shutdown", "/l"])

        # Fun and jokes
        elif 'joke' in query:
            speak(pyjokes.get_joke())

                    # Random advice
        elif 'give me advice' in query or 'random advice' in query:
            advice_list = [
                "Stay positive and keep learning.",
                "Take breaks and stay hydrated.",
                "Consistency is the key to success.",
                "Never stop believing in yourself.",
                "Learn something new every day!"
            ]
            advice = random.choice(advice_list)
            speak(advice)
            print(advice)

        # Small talk
        elif 'how are you' in query:
            speak("I'm just a program, but I'm feeling functional and ready to assist!")
            print("I'm just a program, but I'm feeling functional and ready to assist!")

        elif 'what do you do' in query:
            speak("I can assist you with calculations, provide information, tell the time, share jokes, and much more!")
            print("I can assist you with calculations, provide information, tell the time, share jokes, and much more!")


        # General Knowledge questions
        elif 'capital of india' in query:
            speak("The capital of India is New Delhi.")
            print("The capital of India is New Delhi.")

        elif 'largest planet' in query:
            speak("The largest planet in our solar system is Jupiter.")
            print("The largest planet in our solar system is Jupiter.")

        elif 'who is the president of india' in query:
            speak("The current President of India is Droupadi Murmu.")  # Update as needed
            print("The current President of India is Droupadi Murmu.")


        # Perform calculations using WolframAlpha
        elif "calculate" in query:
            app_id = "4Q2YTR-Q299K5KTWK"  # Replace with your WolframAlpha API key
            client = wolframalpha.Client(app_id)
            indx = query.lower().split().index('calculate')
            query = query.split()[indx + 1:]
            res = client.query(' '.join(query))
            answer = next(res.results).text
            print(f"The answer is {answer}")
            speak(f"The answer is {answer}")

                    # Normal calculations
        elif 'calculate' in query or 'solve' in query:
            query = query.replace('calculate', '').replace('solve', '').replace('what is', '').strip()
            try:
                result = eval(query)  # Evaluates the mathematical expression
                speak(f"The result of {query} is {result}")
                print(f"The result of {query} is {result}")
            except Exception as e:
                speak("I couldn't calculate that. Please try again with a valid mathematical expression.")
                print("Error: Invalid mathematical expression.")


        # Weather information
        elif 'weather' in query:
            api_key = "Your_OpenWeather_API_Key"  # Replace with your OpenWeather API key
            base_url = "http://api.openweathermap.org/data/2.5/weather?"
            speak("Please tell me the city name")
            city_name = takeCommand()
            complete_url = base_url + "appid=" + api_key + "&q=" + city_name
            response = requests.get(complete_url)
            x = response.json()
            
            if x["cod"] != "404":
                y = x["main"]
                current_temperature = y["temp"]
                current_pressure = y["pressure"]
                current_humidity = y["humidity"]
                z = x["weather"]
                weather_description = z[0]["description"]
                print(f"Temperature: {current_temperature}\nPressure: {current_pressure}\nHumidity: {current_humidity}\nDescription: {weather_description}")
                speak(f"The temperature is {current_temperature} Kelvin with {weather_description}.")
            else:
                speak("City not found")

        # Camera functionality
        elif "camera" in query or "take a photo" in query:
            ec.capture(0, "Jarvis Camera", "img.jpg")

        # Open applications
        elif 'open notepad' in query:
            speak("Opening Notepad")
            os.system("notepad")

        elif 'open calculator' in query:
            speak("Opening Calculator")
            os.system("calc")
        

        # Dynamic web search for general questions
        elif 'search' in query:
            query = query.replace("search", "")
            search_web(query)
 

        # Exit the assistant
        elif 'exit' in query:
            speak("Thanks for your time. Have a great day!")
            exit()

        # Trigger assistant again
        elif 'jarvis' in query:
            wishMe()

