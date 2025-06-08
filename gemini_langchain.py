import os
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser


os.environ["GOOGLE_API_KEY"] = "AIzaSyD5zU6Se0-MwQPRl7AkjeG79TsdrqnGCRY"


llm = ChatGoogleGenerativeAI(model="gemini-1.5-flash", temperature=0.7)


prompt = ChatPromptTemplate.from_messages(
    [
        ("system", "You are a helpful AI assistant. Respond to user queries concisely."),
        ("human", "{question}"),
    ]
)


output_parser = StrOutputParser()


chain = prompt | llm | output_parser

question = "What is the capital of France?"
print(f"Question: {question}\n")

try:
    response = chain.invoke({"question": question})
    print(f"Answer: {response}")
except Exception as e:
    print(f"An error occurred: {e}")
    print("Please ensure your GOOGLE_API_KEY is correctly set as an environment variable and is valid.")
    print("Also, check your internet connection and Google API usage limits.")


print("\n--- Streaming Response Example ---")
streaming_question = "Tell me a short, imaginative story about a robot who discovered emotions."
streaming_prompt = ChatPromptTemplate.from_messages(
    [
        ("system", "You are a creative storyteller. Keep the story around 100 words."),
        ("human", "{story_prompt}"),
    ]
)
streaming_chain = streaming_prompt | llm | output_parser

print(f"Story Prompt: {streaming_question}\n")
print("Generating story...\n")

for chunk in streaming_chain.stream({"story_prompt": streaming_question}):
    print(chunk, end="", flush=True)
print("\n")