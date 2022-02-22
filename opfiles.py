import subprocess
from speaker import speak

listapps = {
        "firefox":"C:\\Program Files\\Mozilla Firefox\\firefox.exe",
        "chrome":"C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe",
        "word":"C:\\Program Files\\Microsoft Office\\root\\Office16\\WINWORD.exe",
        "powerpoint":"C:\\Program Files\\Microsoft Office\\root\\Office16\\POWERPNT.exe",
        "excel":"C:\\Program Files\\Microsoft Office\\root\\Office16\\EXCEL.exe"
        }

def openfiles(query):
    try:
        subprocess.call(listapps[query])
        speak("OK")
    except:
        pass