from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv, find_dotenv
load_dotenv(find_dotenv(), override=True)
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnableParallel

model1 = ChatGoogleGenerativeAI(model='gemini-1.5-flash')
model2 = ChatGoogleGenerativeAI(model='gemini-1.5-flash')

parser = StrOutputParser()



prompt1 = PromptTemplate(
    template="Generate short notes related to topic: {text}",
    input_variables=["text"]
    
)

prompt2 = PromptTemplate(
    template="Generate 5 short question-answer on the following topic {text}",
    input_variables=['paper']

)

prompt3 = PromptTemplate(
    template = "Merge the provided paper and answers into single document \n paper->{paper} and answers->{answers}",
    input_variables=['paper','answers']
)

parallel_chain = RunnableParallel(
    {
        'paper': prompt1 | model1 | parser,
        'answers': prompt2 | model2 | parser
    }
)

merged_chain = prompt3 | model1 | parser

chain = parallel_chain | merged_chain

result=chain.invoke({'text':'deep learning'})
print(result)