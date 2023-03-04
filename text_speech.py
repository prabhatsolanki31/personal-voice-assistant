import speech_recognition as sr
from time import  ctime
import time 
import webbrowser
import playsound
import os 
import random
from gtts import gTTS
r=sr.Recognizer()

def record_audio(ask=False):
    with sr.Microphone() as source :
        
        if ask:
            alex_speak(ask)
        audio=r.listen(source)
        voice_data=''
        try:
            voice_data=r.recognize_google(audio)
        except sr.UnknownValueError:
            alex_speak('Sorry , I did not get that ')
        except sr.RequestError:
            alex_speak('Sorry my speech service is down')
        return voice_data
    
def alex_speak(audio_string):
    tts=gTTS(audio_string,lang='en')
    r=random.randint(1,10000000)
    audio_file='audio-'+str(r)+'.mp3'
    tts.save(audio_file)
    playsound.playsound(audio_file)
    print(audio_string)
    os.remove(audio_file)

def respond(voice_data):
    if 'what is your name' in voice_data:
        alex_speak(' i am voice assistant made by prabhat')
    if 'what time is it ' in voice_data:
        alex_speak(ctime())
    if 'search' in voice_data:
        search=record_audio('what do you want to search for ?:')
        url='https://google.com/search?q='+search
        webbrowser.get().open(url)
        alex_speak('Here is what i found '+search)
    if 'find location' in voice_data:
        location=record_audio('what is the location ?:')
        url='https://google.nl/maps/place/'+location+'?&amp'
        webbrowser.get().open(url)
        alex_speak('Here is what i found '+location)
    if 'exit' in voice_data:
        exit()
#time.sleep(1)
alex_speak('How can i help You')
voice_data=record_audio()
respond(voice_data)
