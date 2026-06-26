import os
import webbrowser
import subprocess
import psutil
import datetime


def execute(command):

    command = command.lower()

    # ---------------- BROWSER ----------------

    if "open chrome" in command:
        os.system("start chrome")
        return "Opening Chrome"

    if "close chrome" in command:
        os.system("taskkill /f /im chrome.exe")
        return "Closing Chrome"

    # ---------------- NOTEPAD ----------------

    if "open notepad" in command:
        subprocess.Popen("notepad.exe")
        return "Opening Notepad"

    # ---------------- CALCULATOR ----------------

    if "open calculator" in command:
        subprocess.Popen("calc.exe")
        return "Opening Calculator"

    # ---------------- EXCEL ----------------

    if "open excel" in command:
        os.system("start excel")
        return "Opening Excel"

    # ---------------- WORD ----------------

    if "open word" in command:
        os.system("start winword")
        return "Opening Microsoft Word"

    # ---------------- WHATSAPP ----------------

    if "open whatsapp" in command:
        webbrowser.open("https://web.whatsapp.com")
        return "Opening WhatsApp"

    # ---------------- YOUTUBE ----------------

    if "open youtube" in command or command == "youtube":
        webbrowser.open("https://www.youtube.com")
        return "Opening YouTube"

    # ---------------- GOOGLE ----------------

    if "open google" in command:
        webbrowser.open("https://www.google.com")
        return "Opening Google"

    # ---------------- GMAIL ----------------

    if "open gmail" in command:
        webbrowser.open("https://mail.google.com")
        return "Opening Gmail"

    # ---------------- CHATGPT ----------------

    if "open chatgpt" in command:
        webbrowser.open("https://chatgpt.com")
        return "Opening ChatGPT"

    # ---------------- FILE EXPLORER ----------------

    if "open file explorer" in command:
        os.system("explorer")
        return "Opening File Explorer"

    # ---------------- TASK MANAGER ----------------

    if "open task manager" in command:
        os.system("taskmgr")
        return "Opening Task Manager"

    # ---------------- CONTROL PANEL ----------------

    if "open control panel" in command:
        os.system("control")
        return "Opening Control Panel"

    # ---------------- SETTINGS ----------------

    if "open settings" in command:
        os.system("start ms-settings:")
        return "Opening Settings"

    # ---------------- CPU ----------------

    if "cpu" in command:
        return f"CPU usage is {psutil.cpu_percent()} percent"

    # ---------------- RAM ----------------

    if "ram" in command or "memory usage" in command:
        return f"RAM usage is {psutil.virtual_memory().percent} percent"

    # ---------------- BATTERY ----------------

    if "battery" in command:

        battery = psutil.sensors_battery()

        if battery:
            return f"Battery is {battery.percent} percent"

        return "Battery information unavailable"

    # ---------------- TIME ----------------

    if "time" in command:
        return datetime.datetime.now().strftime("%I:%M %p")

    # ---------------- DATE ----------------

    if "date" in command:
        return datetime.date.today().strftime("%d %B %Y")

    # ---------------- SHUTDOWN ----------------

    if "shutdown computer" in command:
        os.system("shutdown /s /t 1")
        return "Shutting down computer"

    # ---------------- RESTART ----------------

    if "restart computer" in command:
        os.system("shutdown /r /t 1")
        return "Restarting computer"

    # ---------------- LOCK ----------------

    if "lock computer" in command:
        os.system("rundll32.exe user32.dll,LockWorkStation")
        return "Locking computer"

    # ---------------- SEARCH GOOGLE ----------------

    if command.startswith("search "):

        query = command.replace("search ", "").strip()

        if query:
            webbrowser.open(
                f"https://www.google.com/search?q={query}"
            )

            return f"Searching Google for {query}"

    # ---------------- UNKNOWN ----------------

    return None