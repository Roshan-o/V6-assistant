import requests
import wikipedia
import pywhatkit as kit


def find_myip():
    # ip_add=requests.get("http://ip-api.com/json/{query}?fields=status,continent,country,regionName,city,district,lat,lon").json()
    ip_add=requests.get("http://ip-api.com/json/?fields=status,continent,country,regionName,city,district,lat,lon,query").json()
    # .json() give us the date in somewhat dictionary format
    # query-ipaddress manully filled
    return ip_add

def search_on_wikipedia(query):
    results=wikipedia.summary(query,sentences=2)
    return results

def search_on_google(query):
    kit.search(query)

def youtube(video):
    kit.playonyt(video)




