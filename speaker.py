import pyttsx3


engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)


def speak(audio):
    try:
        print('Friday: '+audio)
        engine.say(audio)
        engine.runAndWait()
    except:
        pass