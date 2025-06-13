from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv, find_dotenv
load_dotenv(find_dotenv(), override=True)
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain.schema.runnable import RunnableSequence, RunnablePassthrough, RunnableParallel, RunnableLambda, RunnableBranch

def wordcoount(text):
    return len(text.split())

prompt1 = PromptTemplate(
    template='Write a report on {topic}',
    input_variables=['topic']
)
model = ChatGoogleGenerativeAI(model='gemini-1.5-flash')
parser = StrOutputParser()

prompt2 = PromptTemplate(
   template='Summarize following report - {text}',
   input_variables=['text']
)

report_generation_chain = RunnableSequence(prompt1,model,parser)

branch_chain = RunnableBranch(
    (lambda x: len(x.split())>200, RunnableSequence(prompt2,model, parser)),
    RunnablePassthrough()
)

final_chain = RunnableSequence(report_generation_chain,branch_chain)
print(final_chain.invoke({'topic':'Cricket'}))

