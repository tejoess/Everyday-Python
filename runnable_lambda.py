from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv, find_dotenv
load_dotenv(find_dotenv(), override=True)
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain.schema.runnable import RunnableSequence, RunnablePassthrough, RunnableParallel, RunnableLambda

def wordcoount(text):
    return len(text.split())

prompt1 = PromptTemplate(
    template='Write a joke about {topic}',
    input_variables=['topic']
)
model = ChatGoogleGenerativeAI(model='gemini-1.5-flash')
parser = StrOutputParser()

#prompt2 = PromptTemplate(
 #   template='Explain the folling joke - {text}',
 #   input_variables=['text']
#)

gen_chain = RunnableSequence(prompt1,model,parser)

parallel_chain = RunnableParallel({
    'joke': RunnablePassthrough(),
    'word_count': RunnableLambda(wordcoount),
    #'explanation': RunnableSequence(prompt2, model, parser)
})

final_chain = RunnableSequence(gen_chain,parallel_chain)
print(final_chain.invoke({'topic':'Cricket'}))

