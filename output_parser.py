from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv, find_dotenv
load_dotenv(find_dotenv(), override=True)
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
model = ChatGoogleGenerativeAI(model='gemini-1.5-flash')

topicname=input("Enter any topic to generate question paper: ")
template1 = PromptTemplate(
    template="generate a detailed report on following topic: {topic}",
    input_variables=['topic']
)

template2 = PromptTemplate(
    template="Summerize following text document: {text}",
    input_variables=['paper']
)

parser = StrOutputParser()

chain = template1 | model | parser | template2 | model | parser

result=(chain.invoke({'topic':'Machine Learning'}))
print(result)
