# Voice-Controlled Weather Forecast Assistant

## Description
This project is a voice-controlled weather forecast assistant that utilizes Python libraries such as `requests` for fetching weather data, `pyttsx3` for text-to-speech, `speech_recognition` for converting spoken language into text, and `pygame` for playing audio files. The assistant prompts the user to specify a city and then fetches and vocalizes the current weather conditions for the requested location. It plays distinct sounds to indicate listening, processing, and having retrieved the information, making the interaction intuitive and user-friendly.

## Features
- **Voice Recognition**: Captures user voice input for city names using the `speech_recognition` library.
- **Text-to-Speech**: Utilizes `pyttsx3` to communicate with the user, asking for input and vocalizing weather information.
- **Weather Data Fetching**: Retrieves current weather conditions from the WeatherAPI using the `requests` library.
- **Audio Feedback**: Plays specific sounds to indicate the assistant's status (listening, processing, etc.) using `pygame`.

## How It Works
1. The assistant asks the user to specify a city for the weather forecast.
2. Upon receiving the voice input, it recognizes the city name and fetches the weather data for that location.
3. The assistant then vocalizes the current weather conditions, including temperature, feels-like temperature, and general weather status.
4. Throughout the process, audio cues are played to indicate listening, processing, and completion of tasks.

## Dependencies
- requests
- pyttsx3
- speech_recognition
- pygame

## Setup and Usage
Ensure you have Python installed on your system and install the required libraries using pip:

```pip install requests pyttsx3 SpeechRecognition pygame```

To run the assistant, execute the provided Python script. Ensure you have a working microphone and speakers/headphones for the best experience.

## API Key
The project uses the WeatherAPI for fetching weather data. You need to obtain an API key from [WeatherAPI](https://www.weatherapi.com/) and replace the placeholder in the script with your actual API key.

## Disclaimer
This project is for educational purposes only. Be mindful of the API's usage limits and terms of service.

