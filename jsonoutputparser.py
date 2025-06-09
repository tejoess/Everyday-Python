from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv, find_dotenv
load_dotenv(find_dotenv(), override=True)
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import JsonOutputParser
model = ChatGoogleGenerativeAI(model='gemini-1.5-flash')


parser = JsonOutputParser()
template1 = PromptTemplate(
    template="give me the name, age and city of a fictional person \n {format_instruction}",
    input_variables=[],
    partial_variables={'format_instruction': parser.get_format_instructions()}
)
chain = template1 | model | parser

result = chain.invoke({})
print(result)