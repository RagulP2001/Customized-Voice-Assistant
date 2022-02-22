import subprocess
from speaker import speak


def openFun(query):
    try:
        subprocess.call("explorer "+query+":", shell=True)
    except:
        speak("No such disk drives")