from google import genai
from google.genai import types
import json
from dotenv import load_dotenv
import os

load_dotenv()
client = genai.Client(api_key=os.getenv("GOOGLE_API_KEY"))

response = client.models.generate_content(
    model='gemini-2.0-flash',
    
    config=types.GenerateContentConfig(
        system_instruction='You are a subjective answer evaluator and your task is to assign marks to given answer out of 2',

        max_output_tokens=500,
        temperature=1
    ),
    contents=['AI is type of intelligence made by human which mimic human intelligence like learning, pattern identification, deicision making etc']
)
print(response.text)