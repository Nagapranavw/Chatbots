from google import genai
from google.genai import types
from openai import OpenAI
import os



api_key_gpt = os.environ.get('GPT_API')
api_key_gemini = os.environ.get('GEMINI_API')

openai_client = OpenAI(api_key=api_key_gpt)
gemini_client = genai.Client(api_key=api_key_gemini)

def gpt():
  while True:
    user_input = input("You: ")
    if user_input.lower() in ["gemini"]:
      gemini()
      break
    if user_input.lower() in ["bye", "exit", "quit"]:
      print("Goodbye!")
      break

    try:
      response = openai_client.chat.completions.create(
        model="gpt-5-nano",
        messages=[{"role": "user", "content": user_input}]
      )
      print("GPT:", response.choices[0].message.content)
    except Exception as e:
      print(f"An error occurred: {e}")

def gemini():
  while True:
    user_input = input("You: ")
    if user_input.lower() in ["gpt", "chatgpt", "chat"]:
      gpt()
      break
    if user_input.lower() in ["bye", "exit", "quit"]:
        print("Goodbye!")
        break

    try:
        response = gemini_client.models.generate_content(
            model="gemini-2.5-flash",
            contents=user_input,
            config=types.GenerateContentConfig(
            thinking_config=types.ThinkingConfig(thinking_budget=0)# Rember to enable to thinking based on need
    ),
)
        print("gemini:", response.text)
    except Exception as e:
        print(f"An error occurred: {e}")


bot_which = input("Please tell me which bot you would like to use chatgpt 5 nano or gemini flash. If you dont like the respones you can change later >")
if bot_which.lower() in ["gemini"]:
  gemini()

elif bot_which.lower() in ["gpt","chat"]:
  gpt()