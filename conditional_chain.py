from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv, find_dotenv
load_dotenv(find_dotenv(), override=True)
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnableParallel, RunnableBranch, RunnableLambda
from langchain_core.output_parsers import PydanticOutputParser
from pydantic import BaseModel, Field
from typing import Literal

model = ChatGoogleGenerativeAI(model='gemini-1.5-flash')

class Feedback(BaseModel):
    sentiment: Literal['positive','negative']=Field(description='give snetiment of the feedback')

parser2 = PydanticOutputParser(pydantic_object=Feedback)

parser = StrOutputParser()
prompt1 = PromptTemplate(
    template = "Classify following sentiment of the following feedback into positive or negavtive \n feedback->{feedback}\n {format_instruction}",
    input_variables=['feedback'],
    partial_variables={'format_instruction':parser2.get_format_instructions()}
)
classifier_chain = prompt1 | model | parser2

prompt2 = PromptTemplate(
    template = "Given the following positive feedback, write a short, friendly response in 1-2 sentences:\nFeedback: {feedback}",
    input_variables=['feedback']
)
prompt3 = PromptTemplate(
    template = "Given the following negative feedback, write a short, friendly response in 1-2 sentences:\nFeedback: {feedback}",
    input_variables=['feedback']
)

branch_chain = RunnableBranch(
    (lambda x:x.sentiment=='positive', prompt2 | model | parser),
    (lambda x:x.sentiment=='negative', prompt3 | model | parser),
    RunnableLambda(lambda x: "could not find sentiment")
)

chain = classifier_chain | branch_chain

print(chain.invoke({'feedback':'I did not liked the product, it is used by someone already and has scratches'}))

chain.get_graph().print_ascii()