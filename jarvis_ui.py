import tkinter as tk
import threading
import speech_recognition as sr
import ollama
import win32com.client
import datetime
import psutil

# ---------------- TTS ----------------

speaker = win32com.client.Dispatch("SAPI.SpVoice")
speaker.Rate = 0
speaker.Volume = 100


def speak(text):
    try:
        speaker.Speak(str(text)[:500])
    except:
        pass


# ---------------- AI ----------------

chat_history = [
    {
        "role": "system",
        "content": "You are Jarvis, a helpful AI assistant."
    }
]


def ask_ai(text):

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

        return answer

    except Exception as e:

        return f"AI Error: {e}"


# ---------------- SPEECH ----------------

recognizer = sr.Recognizer()


def listen():

    try:

        with sr.Microphone() as source:

            recognizer.adjust_for_ambient_noise(
                source,
                duration=0.3
            )

            audio = recognizer.listen(
                source,
                timeout=10,
                phrase_time_limit=8
            )

        return recognizer.recognize_google(
            audio,
            language="en-IN"
        )

    except:
        return ""


# ---------------- UI ----------------

root = tk.Tk()

root.title("JARVIS AI CORE")

root.configure(bg="black")

root.attributes("-fullscreen", True)

root.bind("<Escape>", lambda e: root.destroy())

# ---------------- HEADER ----------------

title = tk.Label(
    root,
    text="JARVIS AI CORE ONLINE",
    font=("Consolas", 28, "bold"),
    fg="#00FFFF",
    bg="black"
)

title.pack(pady=15)

status = tk.Label(
    root,
    text="SYSTEM READY",
    font=("Consolas", 16),
    fg="white",
    bg="black"
)

status.pack()

# ---------------- SYSTEM INFO ----------------

system_info = tk.Label(
    root,
    text="",
    font=("Consolas", 12),
    fg="#00FFFF",
    bg="black"
)

system_info.pack(pady=10)


def update_system_info():

    cpu = psutil.cpu_percent()

    ram = psutil.virtual_memory().percent

    battery = psutil.sensors_battery()

    battery_percent = (
        str(battery.percent) + "%"
        if battery
        else "N/A"
    )

    now = datetime.datetime.now().strftime(
        "%d-%m-%Y %I:%M:%S %p"
    )

    system_info.config(
        text=f"CPU: {cpu}%    RAM: {ram}%    BATTERY: {battery_percent}    TIME: {now}"
    )

    root.after(
        1000,
        update_system_info
    )


# ---------------- CONSOLE ----------------

output = tk.Text(
    root,
    bg="black",
    fg="#00FF00",
    font=("Consolas", 12),
    insertbackground="white"
)

output.pack(
    fill="both",
    expand=True,
    padx=20,
    pady=10
)


def log(text):

    output.insert(
        tk.END,
        text + "\n"
    )

    output.see(tk.END)


# ---------------- SEARCH BOX ----------------

command_entry = tk.Entry(
    root,
    font=("Consolas", 14),
    bg="black",
    fg="white",
    insertbackground="white",
    width=80
)

command_entry.pack(pady=10)


# ---------------- TEXT COMMAND ----------------

def send_text_command():

    text = command_entry.get().strip()

    if not text:
        return

    command_entry.delete(0, tk.END)

    log(f"YOU ➜ {text}")

    answer = ask_ai(text)

    log(f"JARVIS ➜ {answer}")

    speak(answer)


# ---------------- VOICE COMMAND ----------------

def run_jarvis():

    status.config(
        text="LISTENING..."
    )

    text = listen()

    if not text:

        status.config(
            text="NO INPUT DETECTED"
        )

        return

    log(f"YOU ➜ {text}")

    status.config(
        text="PROCESSING..."
    )

    answer = ask_ai(text)

    log(f"JARVIS ➜ {answer}")

    status.config(
        text="SPEAKING..."
    )

    speak(answer)

    status.config(
        text="READY")


def activate():

    threading.Thread(
        target=run_jarvis,
        daemon=True
    ).start()


# ---------------- BUTTONS ----------------

activate_btn = tk.Button(
    root,
    text="🎤 ACTIVATE JARVIS",
    command=activate,
    font=("Consolas", 16, "bold"),
    fg="black",
    bg="#00FFFF",
    width=25
)

activate_btn.pack(
    pady=5
)

search_btn = tk.Button(
    root,
    text="🔍 SEND",
    command=send_text_command,
    font=("Consolas", 14, "bold"),
    fg="black",
    bg="#00FFFF",
    width=15
)

search_btn.pack(
    pady=5
)

command_entry.bind(
    "<Return>",
    lambda e: send_text_command()
)

# ---------------- FOOTER ----------------

footer = tk.Label(
    root,
    text="PRESS ESC TO EXIT",
    font=("Consolas", 12),
    fg="gray",
    bg="black"
)

footer.pack(
    side="bottom",
    pady=15
)

# ---------------- START ----------------

update_system_info()

root.mainloop()