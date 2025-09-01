from openai import OpenAI
import os
api_key = os.environ.get('GPT_API')


client = OpenAI(api_key=api_key)

while True:
    user_input = input("You: ")
    if user_input.lower() in ["bye", "exit", "quit"]:
        print("Goodbye!")
        break

    try:
        response = client.chat.completions.create(
            model="gpt-5-nano",  
            messages=[{"role": "user", "content": user_input}] 
        )
        print("GPT:", response.choices[0].message.content)
    except Exception as e:
        print(f"An error occurred: {e}")