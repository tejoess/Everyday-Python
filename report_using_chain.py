from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv, find_dotenv
load_dotenv(find_dotenv(), override=True)
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser

model = ChatGoogleGenerativeAI(model='gemini-1.5-flash')
parser = StrOutputParser()

topic = input("Enter the topic: ")

prompt1 = PromptTemplate(
        template="Generate a detailed report having topics like title, abstraction, research gaps, introduction, application, future scopre on the topic of {topic}",
        input_variables=["topic"]
)

prompt2 = PromptTemplate(
    template="Generate a simple 5 line summary the following report: {report}",
    input_variables=['report']
)

chain = prompt1 | model | parser | prompt2 | model | parser


result = chain.invoke(topic)

print(result)

chain.get_graph().print_ascii()


