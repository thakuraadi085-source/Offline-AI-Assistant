import pyttsx3

try:

    engine = pyttsx3.init()

    engine.setProperty("rate", 180)
    engine.setProperty("volume", 1.0)

    voices = engine.getProperty("voices")

    if voices:
        engine.setProperty(
            "voice",
            voices[0].id
        )

    print("Testing Voice Engine...\n")

    test_text = (
        "Hello Aditya. "
        "Jarvis voice engine is online and working successfully."
    )

    print("Speaking:")
    print(test_text)

    engine.say(test_text)

    engine.runAndWait()

    print("\n✅ Voice Test Successful")

except Exception as e:

    print("\n❌ Voice Test Failed")
    print(e)