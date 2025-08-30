# V6 - The Virtual Voice Assistant 🤖🎙️  

📌 **Tech Stack used:** Python 3.x, Speech Recognition, Text-to-Speech (TTS), PyWhatKit, Wikipedia API, Email (SMTP), OpenWeather API, NewsAPI, GIT, VS Code <br>  
✏️ V6 is a lightweight **virtual voice assistant** for Windows built with Python 3.x.  
✏️ It combines **speech recognition, natural voice responses, and web-powered queries** to help automate daily tasks.  
✏️ With simple hotkeys, you can toggle listening, pause execution, or exit the assistant at any time.  

---

## Features 🚀  
- **Speech Recognition & Response**: Listens to your commands and replies with natural voice.  
- **System Operations**: Open apps like Notepad, Command Prompt, Camera, ArmouryCrate, Spotify, etc.  
- **Web Integration**:  
  - Search on **Google, YouTube, Wikipedia**  
  - Fetch **current news headlines**  
  - Get **weather updates** using OpenWeather & WeatherStack APIs  
- **Networking Tools**: Find your IP address and location.  
- **Emailing**: Send emails directly from the assistant using Gmail SMTP.  
- **Hotkey Controls**:  
  - `p` → Start listening 🎧  
  - `5` → Stop listening 📴  
  - `2` → Pause/Resume program ⏯  
  - `esc` → Exit program ❌  

---

## Project Structure 📂  
```text
📦 Virtual Assistant V6
 ┣ 📜 main.py        # Entry point, handles assistant loop & hotkeys
 ┣ 📜 cntrl_cmd.py   # Core speech recognition & text-to-speech functions
 ┣ 📜 online.py      # Online services (Google, YouTube, Wikipedia, Email, News, Weather, IP lookup)
 ┣ 📜 README.md      # Documentation
Setup & Installation ⚙️
1. Clone the repository
bash
Copy code
git clone https://github.com/YourUsername/VirtualAssistant-V6.git
cd VirtualAssistant-V6
2. Install dependencies
bash
Copy code
pip install -r requirements.txt
Dependencies include:

speechrecognition

pyttsx3

requests

wikipedia

pywhatkit

keyboard

3. API Setup
Email: Use your Gmail App Password (not your login password) in online.py.

Weather API: Replace API keys in online.py with your own from OpenWeather and WeatherStack.

News API: Get your API key from NewsAPI.

Usage 🖥️
Run the assistant with:

bash
Copy code
python main.py
Example commands you can try:
"How are you?"

"Open Notepad"

"Find my IP address"

"Open YouTube" → (then say video name)

"Open Wikipedia" → (then say query)

"Send an email"

"News today"

"What is the weather today?"

Contribution 🛠️
Fork 🍴 the repo

Create a new branch 🌱

Make your changes ✏️

Submit a pull request 🔥

Author ✨
Developed by Kalluri Roshan Lal 💻

vbnet
Copy code
