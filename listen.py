import speech_recognition as sr

recognizer = sr.Recognizer()

recognizer.energy_threshold = 300
recognizer.dynamic_energy_threshold = True
recognizer.pause_threshold = 0.8
recognizer.phrase_threshold = 0.3
recognizer.non_speaking_duration = 0.5


def listen():

    try:

        with sr.Microphone() as source:

            print("🎤 Listening...")

            recognizer.adjust_for_ambient_noise(
                source,
                duration=0.3
            )

            audio = recognizer.listen(
                source,
                timeout=10,
                phrase_time_limit=8
            )

        text = recognizer.recognize_google(
            audio,
            language="en-IN"
        )

        text = text.lower().strip()

        print(f"You: {text}")

        return text

    except sr.WaitTimeoutError:
        return ""

    except sr.UnknownValueError:
        return ""

    except sr.RequestError:
        return ""

    except Exception as e:
        print("Listen Error:", e)
        return ""


def listen_wake_word():

    while True:

        text = listen()

        if not text:
            continue

        if "jarvis" in text:
            print("✅ Wake Word Detected")
            return True


def listen_command():

    print("🎙️ Waiting For Command...")

    command = listen()

    return command


if __name__ == "__main__":

    print("JARVIS LISTENER TEST")

    while True:

        print("Say: Jarvis")

        listen_wake_word()

        print("Wake Successful")

        command = listen_command()

        print("Command:", command)

        if "exit" in command:
            break