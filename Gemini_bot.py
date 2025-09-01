from google import genai
from google.genai import types
import os
api_key = os.environ.get('GEMINI_API')


client = genai.Client(api_key=api_key)

while True:
    user_input = input("You: ")
    if user_input.lower() in ["bye", "exit", "quit"]:
        print("Goodbye!")
        break

    try:
        response = client.models.generate_content(
            model="gemini-2.5-flash",
            contents=user_input,
            config=types.GenerateContentConfig(
            thinking_config=types.ThinkingConfig(thinking_budget=0)# Rember to enable to thinking based on need 
    ),
)
        print("Bot:", response.text)
    except Exception as e:
        print(f"An error occurred: {e}")