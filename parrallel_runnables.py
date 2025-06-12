from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv, find_dotenv
load_dotenv(find_dotenv(), override=True)\

from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain.schema.runnable import RunnableSequence, RunnableParallel

prompt1 = PromptTemplate(
    template='Write a tweet about {topic}',
    input_variables=['topic']
)
model1 = ChatGoogleGenerativeAI(model='gemini-1.5-flash')
model2 = ChatGoogleGenerativeAI(model='gemini-1.5-flash')

parser = StrOutputParser()

prompt2 = PromptTemplate(
    template='Generate a Linkedin post of - {topic}',
    input_variables=['topic']
)
chain = RunnableParallel(
    {
        'tweet': RunnableSequence(prompt1, model1, parser),  
        'linkedin': RunnableSequence(prompt2,model2,parser)
    }
    )

result = chain.invoke({'topic':'AI'})
print(result['tweet'])
print(result['linkedin'])