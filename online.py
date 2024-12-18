import requests
import wikipedia
import pywhatkit as kit

import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

from pywhatkit.mail import send_mail

sender="roshankalluri1@gmail.com"
# password="vijayagowri@ct"
password="famn xxaj qayk vvma" #should use only app password 
# google has stopped allowing third party aplication to use google so, we need to use 
# app password

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

def send_email(receiver,subject,body):
    try:
        # MIME-Multipurpose Internet Mail Extensions
        message = MIMEMultipart()
        message["From"] = sender
        message["To"] = receiver
        message["Subject"] = subject
        message.attach(MIMEText(body, "plain"))
        # email.set_content(message)
        # Gmail: smtp.gmail.com
        # Yahoo: smtp.mail.yahoo.com
        # Outlook: smtp.office365.com

        s=smtplib.SMTP("smtp.gmail.com", 587)
        s.starttls()
        s.login(sender,password)
        s.sendmail(sender,receiver,message.as_string())
        # s.close()
        # send_mail(sender,password,message,subject,receiver)
        return True
    
    except Exception as exc:
        print(exc)
        return False

def get_news():
    url="https://newsapi.org/v2/top-headlines?country=us&apiKey=155ca96a8e0942bcad7aaaf0373510d3"
    news=requests.get(url).json()
    return news["articles"][0]["title"]

if __name__=='__main__':
    # f=send_email("roshanlalkalluri@gmail.com","hi2","hi")
    # print(f)
    print(get_news())

