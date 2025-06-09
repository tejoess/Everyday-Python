from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv, find_dotenv
load_dotenv(find_dotenv(), override=True)
from langchain_core.prompts import PromptTemplate

model = ChatGoogleGenerativeAI(model='gemini-1.5-flash')

topicname=input("Enter any topic to generate question paper: ")
template1 = PromptTemplate(
    template="generate a question paper consisting 10 questions of 2 marks for one word answers on following topic: {topic}",
    input_variables=['topic']
)
prompt1 = template1.invoke({'topic':topicname})
result1= model.invoke(prompt1)
paper=result1.content
print(paper)


template2 = PromptTemplate(
    template="Generate one word answers of questions from following question list: {paper}",
    input_variables=['paper']
)
prompt1=template2.invoke({'paper': paper})

result2=model.invoke(prompt1)

print(result2.content)

