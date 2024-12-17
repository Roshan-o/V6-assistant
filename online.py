import requests
import wikipedia
import pywhatkit as kit
import smtplib
sender='roshankalluri1@gmail.com'
password='vijayagowri@ct'

def find_myip():
    # ip_add=requests.get("http://ip-api.com/json/{query}?fields=status,continent,country,regionName,city,district,lat,lon").json()
    ip_add=requests.get("http://ip-api.com/json/?fields=status,continent,country,regionName,city,district,lat,lon,query").json()
    # .json() give us the date in somewhat dictionary format
    # query-ipaddress manully filled
    return ip_add

def search_on_wikipedia(query):
    results=wikipedia.summary(query,sentences=2)
    # can use info() pywhatkit.info("Python programming language", lines=3)
    return results

def search_on_google(query):
    kit.search(query)

def youtube(video):
    kit.playonyt(video)

def send_email(reciver,subject,message):
    try:
        email=kit.EmailMessage()
        email['To']=reciver
        email['From']=sender
        email['Subject']=subject

        email.set_content(message)
        s=smtplib.SMTP("stmp.gmail.com", 465)
        s.starttls()
        s.login(sender,password)
        s.send_message(email)
        s.close()
        return True
    
    except Exception as exc:
        print(exc)
        return False
