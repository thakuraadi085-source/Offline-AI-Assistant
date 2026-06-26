import pyttsx3
import threading

engine = pyttsx3.init()

engine.setProperty("rate", 180)
engine.setProperty("volume", 1.0)

voices = engine.getProperty("voices")

if voices:
    engine.setProperty(
        "voice",
        voices[0].id
    )

is_speaking = False


def speak(text):

    global is_speaking

    try:

        text = str(text).replace("\n", " ")[:500]

        print(f"\nJarvis: {text}")

        is_speaking = True

        engine.say(text)

        engine.runAndWait()

        is_speaking = False

    except Exception as e:

        is_speaking = False

        print("Speech Error:", e)


def speak_async(text):

    thread = threading.Thread(
        target=speak,
        args=(text,),
        daemon=True
    )

    thread.start()


def stop_speaking():

    global is_speaking

    try:

        engine.stop()

        is_speaking = False

    except:
        pass


def jarvis_status():

    return is_speaking


if __name__ == "__main__":

    speak(
        "Hello Aditya. Jarvis speech engine is working perfectly."
    )