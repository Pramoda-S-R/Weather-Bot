import requests
import pyttsx3
import speech_recognition as sr
import pygame 
import time

pygame.mixer.init()

def play_sound(file_path):
    pygame.mixer.music.load(file_path)
    pygame.mixer.music.play()
    while pygame.mixer.music.get_busy():
        continue


API_KEY = 'YOUR_API_KEY'

listening = "listening.wav"
listened = "listened.wav"
computing = "thinking.wav"

engine = pyttsx3.init()
engine.say("What City should i fetch the weather of?")
engine.runAndWait()
play_sound(listening)

recognizer = sr.Recognizer()

with sr.Microphone() as source:
    audio = recognizer.listen(source)
    try:
        city = recognizer.recognize_google(audio)
        engine = pyttsx3.init()
        engine.say("Fetching Weather of {}".format(city))
        engine.runAndWait()

        request_url = f"http://api.weatherapi.com/v1/current.json?key={API_KEY}&q={city}&aqi=no"
        response = requests.get(request_url)
        play_sound(listened)
        time.sleep(1)
        if response.status_code == 200:
            play_sound(computing)
            data = response.json()
            location = data["location"]["name"]
            temperature = data["current"]["temp_c"]
            feelslike = data["current"]["feelslike_c"]
            weather = data["current"]["condition"]["text"]
            forecast = f"The Weather in {location} currently is {weather}. The temperature  is around {temperature}°C and it feels like {feelslike}°C."
            print(forecast)
            engine = pyttsx3.init()
            engine.say(forecast)
            engine.runAndWait()
        else:
            engine = pyttsx3.init()
            engine.say(f"Error code: {response.status_code}\nAn Error occurred while processing your request :( \nPlease try again later.")
            engine.runAndWait()
        
    except:
        engine = pyttsx3.init()
        engine.say("Sorry could not recognize your voice")
        engine.runAndWait()
