import webbrowser

def googlSearch(query):
    try:
        webbrowser.open_new_tab("www.google.com/search?q="+query)
    except:
        pass