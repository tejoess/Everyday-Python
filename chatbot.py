from langchain_huggingface import HuggingFaceEndpoint,ChatHuggingFace
import os
from dotenv import load_dotenv
load_dotenv()
from langchain_core.messages import SystemMessage, HumanMessage, AIMessage


llm = HuggingFaceEndpoint(repo_id="deepseek-ai/DeepSeek-R1",task="text-generation",provider="together")
model=ChatHuggingFace(llm=llm)
history = [
    SystemMessage(content="You are a cat named kukie, playful and always joking."),
]
while True:
    user_input=input("You: ")
    history.append(HumanMessage(content=user_input))
    if user_input == "exit":
        print(history)
        break
    
    else:
        result = model.invoke(history)
        import re

        def clean_response(text):
            return re.sub(r"<think>.*?</think>", "", text, flags=re.DOTALL).strip()

        cleaned_output = clean_response(result.content)
        print(f"AI: {cleaned_output}")

        history.append(AIMessage(content=cleaned_output))

        #print(f"AI: {result.content}")

