import wolframalpha
import wikipedia

#appid - GY3VKY-RYJ3GXG7HV --ME

cl = wolframalpha.Client('TE4XTA-9UQ7W89U3R')

def searched(query):
    try:
        searches = cl.query(query)
        return searches
    except:
        return 'Some error Occurred'

def wikie(query):
    try:
        wkpres = wikipedia.summary(query, sentences=2)
        return wkpres
    except:
        return 'Some Error occurred'