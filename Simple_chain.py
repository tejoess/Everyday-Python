from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv, find_dotenv
load_dotenv(find_dotenv(), override=True)
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser

model = ChatGoogleGenerativeAI(model='gemini-1.5-flash')
parser = StrOutputParser()


prompt = PromptTemplate(
    template="Generate 5 one line facts about {topic}",
    input_variables=["topic"]
    
)
chain = prompt | model | parser
result = chain.invoke({"topic": "Python"})
print(result)
chain.get_graph().print_ascii()