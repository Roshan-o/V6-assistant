import cntrl_cmd as cc
import os
import subprocess as sp
import keyboard
import shutil
import online as o
#to get paths

running=True
listening =False
def start_listening():
    global listening
    listening=True
    print("started Listening....")

def stop_listening():
    global listening
    listening=False
    print("stopped Listening....")

def exit_program():
    global running
    print("program being stopped")
    running=False

keyboard.add_hotkey('k',start_listening)
keyboard.add_hotkey('space',stop_listening)    

keyboard.add_hotkey('esc',exit_program)


if __name__=='__main__':
    cc.speak("  hi i am V6")
    cc.greet_me()
    while running:
        if listening:
            query=cc.take_command()
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
            elif "open Notepad" in query:
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
                os.path(ar_path)
            elif "find my IP address" in query: 
                # ip=o.find_myip()["ip"]
                details=o.find_myip()
                ip=details['query']
                cc.speak(f"your ip adress is{ip}")
                print(f"your ip is {ip}") 
                location=details['country']+" "+details['regionName']
                print(f"your location is {location}")
            elif "open youtube" in query:
                cc.speak("what do you want on youtube")
                video=cc.take_command()
                o.youtube(video)
            
            
    

 

