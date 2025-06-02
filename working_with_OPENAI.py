from langchain_openai import OpenAI
from dotenv import load_dotenv
load_dotenv()

llm = OpenAI(model='gpt-3.5-turbo-instruct')

result = llm.invoke("Who is Batman")

print(result)


from langchain_openai import ChatOpenAI
from dotenv import load_dotenv

load_dotenv()

model=ChatOpenAI(model='gpt-4',temperature=0.9, max_completion_tokens=200)
result2 = model.invoke("What is capital of India?")
print(result2.content)

