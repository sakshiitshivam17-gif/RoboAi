
import os
import subprocess
from openai import OpenAI, APIError

client = OpenAI()

MODEL = "gpt-4.1-mini"

def speak(text):
    subprocess.run(["spd-say", text], check=False)

def ask_ai(question):
    response = client.responses.create(
        model=MODEL,
        instructions="You are Robo, a friendly AI assistant. Explain things simply and clearly.",
        input=question,
        max_output_tokens=300,
    )
    return response.output_text

def main():
    print("Robo AI is ready! Type 'exit' to quit.")
    speak("Hello! Robo is ready.")

    while True:
        question = input("You: ").strip()

        if question.lower() in ("exit", "quit", "bye"):
            speak("Goodbye!")
            break

        if not question:
            continue

        try:
            print("Robo is thinking...")
            answer = ask_ai(question)
            print(f"\nRobo: {answer}\n")
            speak(answer)

        except APIError as error:
            print(f"OpenAI API error: {error}")

if __name__ == "__main__":
    main()
