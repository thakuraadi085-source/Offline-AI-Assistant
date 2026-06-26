from speech import speak
from listen import listen_wake_word, listen_command
from commands import execute
from brain import ask_ai

print("=" * 60)
print("JARVIS OFFLINE AI STARTED")
print("Wake Word : Jarvis")
print("Exit Word : Exit")
print("=" * 60)

speak("Jarvis system online")

while True:

    print("\nWaiting For Wake Word...")

    # Wait until user says Jarvis
    listen_wake_word()

    speak("Yes Sir, I am listening")

    while True:

        command = listen_command()

        if not command:
            continue

        command = command.lower().strip()

        print("Command:", command)

        # ---------------- INTERRUPT ----------------

        if command == "jarvis":
            speak("Yes Sir")
            continue

        # ---------------- EXIT ----------------

        if any(word in command for word in [
            "exit",
            "stop",
            "stop jarvis",
            "shutdown assistant",
            "goodbye"
        ]):
            speak("Goodbye Sir")
            raise SystemExit

        # ---------------- PERSONAL INFO ----------------

        elif "hello" in command:
            speak("Hello Aditya")

        elif "mother" in command:
            speak("Your mother's name is Rakhi Kanwar")

        elif "father" in command:
            speak("Your father's name is Pawan Kumar")

        elif "sister" in command:
            speak("Your sisters are Raksha and Niharika Kanwar")

        elif "caste" in command:
            speak("Your caste is Rajput")

        elif "rajput" in command:
            speak(
                "Rajputs are known for courage, leadership and honor."
            )
        elif "who makes you jarvis" in command:
            speak("I was created by aditya singh rao and my purpose is to assist him in various tasks and provide information.")

        # ---------------- SYSTEM COMMANDS ----------------

        else:

            result = execute(command)

            if result:
                speak(result)
                continue

            # ---------------- AI ----------------

            try:

                response = ask_ai(command)

                if response:
                    print("\nJarvis:", response)
                    speak(response)

                else:
                    speak("I could not generate a response.")

            except Exception as e:

                print("AI Error:", e)

                speak(
                    "I am unable to connect to the AI model."
                )