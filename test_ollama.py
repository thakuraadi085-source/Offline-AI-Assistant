import ollama

MODEL_NAME = "llama3:latest"


def test_ollama():

    try:

        print("Testing Ollama...")
        print(f"Model : {MODEL_NAME}\n")

        response = ollama.chat(
            model=MODEL_NAME,
            messages=[
                {
                    "role": "user",
                    "content": "What is artificial intelligence?"
                }
            ]
        )

        answer = response["message"]["content"]

        print("AI Response:\n")
        print(answer)

        print("\n✅ Ollama Working Successfully")

    except Exception as e:

        print("\n❌ Ollama Error")
        print(e)

        print(
            "\nMake sure Ollama is installed and running."
        )


if __name__ == "__main__":
    test_ollama()