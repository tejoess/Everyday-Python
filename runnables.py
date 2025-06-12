from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv, find_dotenv
load_dotenv(find_dotenv(), override=True)\

from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain.schema.runnable import RunnableSequence

prompt = PromptTemplate(
    template='Write a joke about {topic}',
    input_variables=['topic']
)
model = ChatGoogleGenerativeAI(model='gemini-1.5-flash')
parser = StrOutputParser()

chain = RunnableSequence(prompt,model,parser)

print(chain.invoke({'topic':'AI'}))
