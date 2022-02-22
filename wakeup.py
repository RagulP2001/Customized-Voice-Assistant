import speech_recognition as sr

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

    return query