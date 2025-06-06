from langchain_huggingface import HuggingFaceEndpoint,ChatHuggingFace
import os
from dotenv import load_dotenv
load_dotenv()


llm = HuggingFaceEndpoint(repo_id="deepseek-ai/DeepSeek-R1",task="text-generation",provider="together")
model=ChatHuggingFace(llm=llm)
history = []
while True:
    user_input=input("You: ")
    history.append(user_input)
    if user_input == "exit":
        break
    
    else:
        result = model.invoke(history)
        import re

        def clean_response(text):
            return re.sub(r"<think>.*?</think>", "", text, flags=re.DOTALL).strip()

        cleaned_output = clean_response(result.content)
        print(f"AI: {cleaned_output}")

        history.append(cleaned_output)
        #print(f"AI: {result.content}")

