import requests

OLLAMA_URL = "http://localhost:11434/api/generate"
MODEL_NAME = "llama3:latest"


def ask_ai(prompt):

    try:

        response = requests.post(
            OLLAMA_URL,
            json={
                "model": MODEL_NAME,
                "prompt": prompt,
                "stream": False
            },
            timeout=120
        )

        response.raise_for_status()

        data = response.json()

        answer = data.get("response", "").strip()

        if not answer:
            return "I could not generate a response."

        return answer

    except requests.exceptions.ConnectionError:
        return "Ollama is not running. Please start Ollama first."

    except requests.exceptions.Timeout:
        return "The AI model took too long to respond."

    except Exception as e:
        return f"AI Error: {str(e)}"


def test_ai():

    print("Testing AI...")

    reply = ask_ai("Who are you?")

    print("\nAI Response:\n")
    print(reply)


if __name__ == "__main__":
    test_ai()