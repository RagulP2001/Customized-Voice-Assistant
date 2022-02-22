import speech_recognition as sr
import pyttsx3

def myCommand():
   
    r = sr.Recognizer()
    r.energy_threshold = 4000
    with sr.Microphone() as source:                                                                       
        print("Listening...")
        r.pause_threshold =  1
        audio = r.listen(source)
    try:
        query = r.recognize_google(audio, language='en-in')
        return query.lower()

    except sr.UnknownValueError:
    	return 0

    return query