from langchain_community.document_loaders import PyPDFLoader
from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv, find_dotenv
load_dotenv(find_dotenv(), override=True)\

from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser

loader = PyPDFLoader('AIsample.pdf')

docs = loader.load()

model = ChatGoogleGenerativeAI(model='gemini-1.5-flash')
parser = StrOutputParser()
prompt = PromptTemplate(
    template = "Summarize the content of the following document in five lines: {docs}",
    input_variables=['docs']

)
chain = prompt | model | parser

print(docs[1].metadata)
print(chain.invoke({'docs': docs[0].page_content}))