import cntrl_cmd as cc
import os
import subprocess as sp
import keyboard
import shutil
import online as o
#to get paths


running=True
listening =False

pause=True


def start_listening():
    global listening
    listening=True
    

def stop_listening():
    global listening
    listening=False
    


def pause_program():
    global pause
    pause=not pause
    if not pause:
        print("program being stopped!")
    else:
        print("program started.....")


def exit_program():
    global running
    running=False

keyboard.add_hotkey('p',start_listening)
keyboard.add_hotkey('5',stop_listening)    

keyboard.add_hotkey('esc',exit_program)
keyboard.add_hotkey('2',pause_program)


def take_command_ftORv():
    if listening:
        q=cc.take_command()
        if not listening:
            print("stopped Listening....")
        return q
    else:
        q=input("Enter command:")
        if listening:
            print("started Listening....")
        return q


if __name__=='__main__':
    cc.speak("hi i am V6")
    cc.greet_me()
    while running:
        if pause:
            query=take_command_ftORv()
            # print(query)
            if "how are you" in query or "how r u" in query:
                cc.speak("I am fine sir")
                print("I am fine sir")
            elif "open command prompt" in query:
                cc.speak("opening command prompt")
                os.system("start cmd")
            elif "open notepad" in query:
                cc.speak("opening notepad")
                os.system("start notepad")
            elif "open camera" in query:
                cc.speak("opening camera")
                sp.run("start microsoft.windows.camera:",shell=True)
            elif "open notepad" in query:
                cc.speak("opening notepad")
                notepd_path="C:\\Users\ASUS\\AppData\\Local\\Microsoft\\WindowsApps\\notepad.exe"
                # will get path of notepad
                os.startfile(notepd_path)


            elif "open Whatsapp" in query:
                cc.speak("opening whatsapp")
                whatsapp_path=""
                os.startfile(whatsapp_path)
            elif "open Github" in query:
                cc.speak("opening github")
                github_path="https://github.com/Roshan-o"
                os.startfile(github_path)
            
            
            elif "open armour crate" in query:
                cc.speak("opening armour crate")
                ar_path="C:\\Users\\ASUS\\AppData\\Local\\Microsoft\\WindowsApps\\ArmouryCrate.exe"
                os.startfile(ar_path)


            elif "find my ip address" in query: 
                # ip=o.find_myip()["ip"]
                details=o.find_myip()
                ip=details['query']
                cc.speak(f"your ip adress is{ip}")
                print(f"your ip is {ip}") 
                location=details['country']+" "+details['regionName']
                print(f"your location is {location}")


            elif "open youtube" in query:
                cc.speak("what do you want on youtube")
                video=take_command_ftORv()
                o.youtube(video)


            elif "open google" in query:
                cc.speak("what do you want on google")
                query=take_command_ftORv()
                result=o.search_on_google(query)
                cc.speak(f"According to google,{result}")
                print(result)

            elif "open wikipedia" in query:
                cc.speak("what do you want search on wikipedia")
                query=take_command_ftORv()
                result=o.search_on_wikipedia(query)
                cc.speak(f"According to wikipedia,{result}")
                print(result)


            elif "send an email" in query:
                cc.speak("to which email address should I send")
                # fix=True
                # while fix:
                #     reciever=take_command_ftORv()
                #     cc.speak(f"reciever email address{reciever}")
                #     f=take_command_ftORv()
                #     if "ok" in f:
                #         f=False
                #     cc.speak("locking the email address")
                reciever=input("Enter Email address:")
                cc.speak("what is the subject")
                subject=take_command_ftORv().capitalize()
                cc.speak(f"subject is{subject}")
                cc.speak("what is the message")
                message=take_command_ftORv().capitalize()
                cc.speak(f"subject is{message}")
                if o.send_email(reciever,subject,message):
                    print("email sent")
                    cc.speak("email sent")
                else:
                    cc.speak("can't able to send email,sorry sir")
            
            elif "news today" in query:
                news=o.get_news()
                cc.speak(news)
                print(news)
            elif "what is the wheather today" in query:
                cc.speak("what is your city name sir")
                city=input("enter city:")
                cc.speak(f"temperature is {o.get_weather(city)} degree celceus")
            

    print("program terminated....")
                

            
            
            
    

 

