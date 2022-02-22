import re

def isWordpresent(question,query):
    resp = [word for word in re.split("\W+",query) if word.lower() in question]
    if (len(resp) >0) : 
            return True
    return False