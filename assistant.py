import speech_recognition as sr
import ollama
import win32com.client
import webbrowser
import os
import json
import datetime
import psutil
import subprocess
import threading

# ---------------- TTS ----------------

speaker = win32com.client.Dispatch("SAPI.SpVoice")
speaker.Rate = 0
speaker.Volume = 100


def speak(text):
    try:
        text = str(text).replace("\n", " ")[:500]
        print(f"Jarvis: {text}")
        speaker.Speak(text)
    except Exception as e:
        print("Speech Error:", e)


# ---------------- MEMORY ----------------

MEMORY_FILE = "memory.json"


def load_memory():
    if os.path.exists(MEMORY_FILE):
        try:
            with open(MEMORY_FILE, "r", encoding="utf-8") as f:
                return json.load(f)
        except:
            pass

    return {"facts": []}


def save_memory(data):
    with open(MEMORY_FILE, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=4)


memory = load_memory()

# ---------------- SPEECH RECOGNITION ----------------

r = sr.Recognizer()
r.energy_threshold = 300
r.pause_threshold = 0.8
r.dynamic_energy_threshold = True


def listen():
    try:
        with sr.Microphone() as source:
            r.adjust_for_ambient_noise(source, duration=0.3)

            print("Listening...")

            audio = r.listen(
                source,
                timeout=10,
                phrase_time_limit=8
            )

        text = r.recognize_google(audio, language="en-IN")
        text = text.lower()

        print("You:", text)

        return text

    except:
        return ""


# ---------------- SYSTEM INFO ----------------

def battery_status():
    battery = psutil.sensors_battery()

    if battery:
        return f"Battery is {battery.percent} percent"

    return "Battery information unavailable"


def cpu_status():
    return f"CPU usage is {psutil.cpu_percent()} percent"


def ram_status():
    return f"RAM usage is {psutil.virtual_memory().percent} percent"


# ---------------- APPS ----------------

def open_notepad():
    subprocess.Popen("notepad.exe")


def open_excel():
    os.system("start excel")


def open_whatsapp():
    webbrowser.open("https://web.whatsapp.com")


def open_youtube():
    webbrowser.open("https://youtube.com")


def open_google():
    webbrowser.open("https://google.com")


def open_chrome():
    os.system("start chrome")


# ---------------- AI CHAT ----------------

chat_history = [
    {
        "role": "system",
        "content": """
You are Jarvis.

Rules:
1. Give short and useful answers.
2. Be professional.
3. Help with computer tasks.
4. Do not write unnecessary long paragraphs.
"""
    }
]

# ---------------- STARTUP ----------------

print("=" * 50)
print("JARVIS OFFLINE AI READY")
print("Wake Word : Jarvis")
print("Exit Word : Exit")
print("=" * 50)

speak("Jarvis is online")

active = False

# ---------------- MAIN LOOP ----------------

while True:

    text = listen()

    if not text:
        continue

    # ---------------- WAKE WORD ----------------

    if not active:

        if "jarvis" in text:
            active = True
            speak("Yes sir, I am listening")

        continue

    # ---------------- EXIT ----------------

    if any(word in text for word in ["exit", "stop jarvis", "shutdown assistant"]):
        speak("Shutting down. Goodbye sir.")
        break

    # ---------------- TIME ----------------

    if "time" in text:
        speak(datetime.datetime.now().strftime("%I:%M %p"))
        continue

    if "date" in text:
        speak(datetime.date.today().strftime("%d %B %Y"))
        continue

    # ---------------- BATTERY ----------------

    if "battery" in text:
        speak(battery_status())
        continue

    # ---------------- CPU ----------------

    if "cpu" in text:
        speak(cpu_status())
        continue

    # ---------------- RAM ----------------

    if "ram" in text or "memory usage" in text:
        speak(ram_status())
        continue

    # ---------------- OPEN APPS ----------------

    if "open notepad" in text:
        speak("Opening Notepad")
        open_notepad()
        continue

    if "open excel" in text:
        speak("Opening Excel")
        open_excel()
        continue

    if "open whatsapp" in text:
        speak("Opening WhatsApp")
        open_whatsapp()
        continue

    if "open youtube" in text:
        speak("Opening YouTube")
        open_youtube()
        continue

    if "open google" in text:
        speak("Opening Google")
        open_google()
        continue

    if "open chrome" in text:
        speak("Opening Chrome")
        open_chrome()
        continue

    # ---------------- CLOSE CHROME ----------------

    if "close chrome" in text:
        speak("Closing Chrome")
        os.system("taskkill /f /im chrome.exe")
        continue

    # ---------------- SHUTDOWN PC ----------------

    if "shutdown computer" in text:
        speak("Shutting down computer")
        os.system("shutdown /s /t 1")
        continue

    # ---------------- RESTART PC ----------------

    if "restart computer" in text:
        speak("Restarting computer")
        os.system("shutdown /r /t 1")
        continue

    # ---------------- MEMORY SAVE ----------------

    if "my name is" in text or "i like" in text:

        if text not in memory["facts"]:
            memory["facts"].append(text)
            save_memory(memory)

        speak("I will remember that")
        continue

    # ---------------- MEMORY RECALL ----------------

    if "what do you know about me" in text:

        if memory["facts"]:

            speak("Here is what I know")

            for fact in memory["facts"][-5:]:
                speak(fact)

        else:
            speak("I do not have any memories yet")

        continue

    # ---------------- AI ----------------

    try:

        chat_history.append(
            {
                "role": "user",
                "content": text
            }
        )

        response = ollama.chat(
            model="llama3:latest",
            messages=chat_history
        )

        answer = response["message"]["content"]

        chat_history.append(
            {
                "role": "assistant",
                "content": answer
            }
        )

        speak(answer)

    except Exception as e:

        print("AI Error:", e)

        speak(
            "I am unable to connect to the AI model. Please make sure Ollama is running."
        )