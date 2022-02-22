from recognizer import myCommand
import datetime
import os
from speaker import speak
import web1
import wakeup
import wolfram
import simpleaudio as sa
import time
import wordchecker
from wordremover import remover
from youtube import youtubeSearch
from googl import googlSearch
from opfiles import openfiles
from explorer import openFun
#import subprocess

friwakeup = ["hey friday","Hey Friday","hey friday","hey Friday"]


vid=['video search','open youtube','i want to watch video','i want to watch a video']
greetings = ['hey there', 'hello', 'hi', 'Hai', 'hey!', 'hey']
wkp=['wikipedia']
question=['what','who','when','weather','how']
google = ['search for']
gmail = ['gmail','email','login']
dellist = ['google','wikipedia','youtube','search','for']
youtube = ['video','youtube']
googls = ['google','search','for','where']
opf = ['open']

registeruser = ['register','credentials']
    
explorer = ['file explorer','explorer']

filename = 'eventually.wav'
wave_obj = sa.WaveObject.from_wave_file(filename)



def greetMe():
    currentH = int(datetime.datetime.now().hour)
    if currentH >= 0 and currentH < 12:
        speak('Hi, Good Morning!')

    if currentH >= 12 and currentH < 18:
        speak('Hi, Good Afternoon!')

    if currentH >= 18 and currentH !=0:
        speak('Hi, Good Evening!')

greetMe()
print("Warning: If you want to login to a website you should register your credentials...")
print("For registering the credentials Say: Register credentials")


if __name__ == '__main__':

    while True:
        wakeupp = wakeup.callMe()
        if(wakeupp in friwakeup):
            flag = False
            play_obj = wave_obj.play()
            time.sleep(1.7)
            speak("Hi, I'm here to help you!\n What do you want me to do?")
            query = str(myCommand())
            query.lower()
            print("You: "+query)
            
            if(query == 'who are you' and flag == False):
                speak("I'm your digital assistant Friday!")
                flag = True
                
            if(query == "bye" and flag == False):
                speak("It's sad to hear Bye!")
                flag = True
                #sys.exit()
                
            if(wordchecker.isWordpresent(question,query) == True and flag == False):
                finres = wolfram.searched(query)
                try:
                    for counter,pod in enumerate(finres.pods):
                        speak(pod.text)
                        if(counter == 1):
                            break
                except:
                    googlSearch(query)
                    speak("Ok")
                    flag = True
                
                flag = True
                
            if(wordchecker.isWordpresent(wkp,query) == True and flag == False):
                remover(dellist,query)
                resp = wolfram.wikie(query)
                speak(resp)
                flag= True
            
            if(wordchecker.isWordpresent(gmail,query) == True and  flag == False):
                speak("which website to login?")
                logwebsite = str(input())
                speak("Please wait...\nWebsite: {}".format(logwebsite))
                web1.webChecker(logwebsite)
                flag = True
                
            if(wordchecker.isWordpresent(youtube,query)):
                query = remover(dellist,query)
                youtubeSearch(query)
                flag = True
                
            if(wordchecker.isWordpresent(registeruser,query) and flag == False):
                speak("Please enter your credentials in the command line...")
                #os.system("cmd /k python newcrypt.py")
                os.system("start cmd /k python newcrypt.py")
                flag = True
                
                
            if(wordchecker.isWordpresent(explorer,query) == True and flag == False):
                speak("Which Disk do you want to open")
                ls = os.popen("fsutil fsinfo drives").readlines()
                print (ls[1])
                diskname = myCommand()
                openFun(diskname)
                speak("Ok!")
                flag = True
                
            if(wordchecker.isWordpresent(opf,query) == True and flag == False):
                query = remover(opf,query)
                openfiles(query)
                flag = True
                
            
            if(wordchecker.isWordpresent(googls,query) == True and flag == False):
                query = remover(googls,query)
                googlSearch(query)
                speak("Ok")
                flag = True