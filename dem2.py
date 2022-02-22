import subprocess
from speaker import speak
import os
from recognizer import myCommand

yeslist = ['Yes','yes','YES']
def openFun(query):
    try:
        print("Do you want to open any directories in",query,": ?","Reply YES if you want to.")
        subquery = myCommand()
        if(subquery in yeslist):
            dictionary = {}
            print("Which directory do you want to open in {}?".format(query))
            
            direc = os.listdir(query+":\\")
            for i in direc:
                dictionary.update({str(i.lower()) : str(i)})
            print(direc)
            speak("Which Directory to open?")
            dirname = myCommand()
            subprocess.call("explorer "+query+":\\"+dirname+"\\", shell=True)
            # targetdirec = (myCommand()).lower
            # if(targetdirec in direc):
            #     Speak("Opening...")
            #     subprocess.call("explorer "+query+":\\", shell=True)
    except:
        print('No such disk!')

openFun('G')