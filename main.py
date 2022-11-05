import speech_recognition as sr
import webbrowser
import time
import playsound
import os
import random
from gtts import gTTS
from time import ctime

r = sr.Recognizer()


def recorder(ask = False):
    with sr.Microphone() as source:
        # r.adjust_for_ambient_noise(source)
        if ask:
            speak(ask)
        audio = r.listen(source)
        voice_data = ''
        try:
            voice_data = r.recognize_google(audio)
            # print(voice_data)
        except sr.UnknownValueError:
            speak('Sorry, I did not get that')
        except sr.RequestError:
            speak('Sorry, my speech service is not available at the moment')
        return voice_data


def speak(audio_string):
    tts = gTTS(text=audio_string, lang='en')
    r = random.randint(1,10000000)
    audio_file = 'audio-' + str(r) + '.mp3'
    tts.save(audio_file)
    playsound.playsound(audio_file)
    print(audio_string)
    os.remove(audio_file)


def respond(voice_data):
    if 'what is your name' in voice_data:
        speak('My name is Zeeya')
    if 'what time is it' in voice_data:
        speak(ctime())
    if 'who is Isah' in voice_data:
        speak('Isah is a mumu comrade, ashawo boy')
    if 'search' in voice_data:
        search = recorder('What do you want to search for?')
        url = 'https://google.com/search?q=' + search
        webbrowser.get().open(url)
        speak('Here is what I found for' + search)
    if 'find location' in voice_data:
        location = recorder('What location are you looking for?')
        url = 'https://google.nl/maps/place' + search + '/&amp'
        webbrowser.get().open(url)
        speak('Here is the location of' + location)
    if 'exit' in voice_data:
        exit()


time.sleep(1)
speak('Hi, I am Zeeya, How can I help you?')
while 1:
    voice_data = recorder()
    respond(voice_data)