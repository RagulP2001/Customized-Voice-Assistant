from youtube_search import YoutubeSearch
import webbrowser

def youtubeSearch(query):
    results = YoutubeSearch(query, max_results=1).to_dict()
    
    link = "www.youtube.com"+results[0]["url_suffix"]
    webbrowser.open_new_tab(link)