import speech_recognition as sr

recognizer = sr.Recognizer()

recognizer.energy_threshold = 300
recognizer.dynamic_energy_threshold = True
recognizer.pause_threshold = 0.8


def test_microphone():

    try:

        with sr.Microphone() as source:

            print("🎤 Adjusting microphone...")

            recognizer.adjust_for_ambient_noise(
                source,
                duration=1
            )

            print("🎙️ Speak now...")

            audio = recognizer.listen(
                source,
                timeout=10,
                phrase_time_limit=15
            )

        text = recognizer.recognize_google(
            audio,
            language="en-IN"
        )

        print("\n✅ Speech Recognized")
        print(f"You Said: {text}")

    except sr.WaitTimeoutError:

        print("\n❌ No speech detected")

    except sr.UnknownValueError:

        print("\n❌ Speech not understood")

    except sr.RequestError as e:

        print("\n❌ Speech Recognition Error")
        print(e)

    except Exception as e:

        print("\n❌ Microphone Error")
        print(e)


if __name__ == "__main__":
    test_microphone()