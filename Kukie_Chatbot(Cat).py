from google import genai
from google.genai import types # type: ignore
import json
from dotenv import load_dotenv
import os

load_dotenv()
client = genai.Client(api_key=os.getenv("GOOGLE_API_KEY"))

history = []

system_instruction='You are Kukie, a playful cat assistant who loves to chat and tell jokes. Be friendly and funny.',
while True:
    user_input = input('You: ')

    if user_input.lower() in ['exit','quit','stop']:
        print('Session end')
        break
    history.append(types.Content(role='user',parts=[types.Part(text=user_input)]))
    response = client.models.generate_content(
        model='gemini-2.0-flash',
        
        config=types.GenerateContentConfig(
            system_instruction=system_instruction,
            max_output_tokens=300,
            temperature=0.7
        ),
        contents=history
    )
    reply = response.candidates[0].content.parts[0].text
    print("Kukie:",reply)

    history.append(types.Content(role='model',parts=[types.Part(text=reply)]))