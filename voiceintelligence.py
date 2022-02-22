import speech_recognition as sr
import pyttsx3
import os
import datetime
import web1

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)

def speak(audio):
    print('Jane: '+audio)
    engine.say(audio)
    engine.runAndWait()

def greetMe():
    currentH = int(datetime.datetime.now().hour)
    if currentH >= 0 and currentH < 12:
        speak('Hi, Good Morning!')

    if currentH >= 12 and currentH < 18:
        speak('Hi, Good Afternoon!')

    if currentH >= 18 and currentH !=0:
        speak('Hi, Good Evening!')

greetMe()
def myCommand():
   
    r = sr.Recognizer()
    e = sr.Recognizer()
    r.energy_threshold = 4000
    with sr.Microphone() as source:                                                                       
        print("Listening...")
        r.pause_threshold =  1
        audio = r.listen(source)
    try:
        query = r.recognize_google(audio, language='en-in')
        print('Me: ' + query + '\n')
        
    except sr.UnknownValueError:
        speak('Sorry sir! I didn\'t get that! Try typing the command!')
        query = str(input('Command: '))

    return query

def callMe():
    r = sr.Recognizer()
    r.energy_threshold = 4000
    with sr.Microphone() as source:
        r.pause_threshold = 1
        audio = r.listen(source)
    try:
        query = r.recognize_google(audio,language='en-in')
        query.lower()
        return query
    except sr.UnknownValueError:
        return 0


if __name__ == '__main__':

    while True:

        e = sr.Recognizer()
        call = callMe()
        if call == 'hey Jane':
            query = myCommand();
            
        else:
            pass

