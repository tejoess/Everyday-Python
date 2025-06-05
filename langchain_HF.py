from langchain_huggingface import HuggingFaceEndpoint,ChatHuggingFace
from dotenv import load_dotenv
import os
import streamlit as st

load_dotenv()
token = os.getenv("HUGGINGFACEHUB_API_KEY")
model_name = "deepseek-ai/DeepSeek-R1"

llm = HuggingFaceEndpoint(repo_id=model_name, task="summarization", provider='together')
model = ChatHuggingFace(llm=llm)
st.header("Research Tool")
user_input=st.text_input("Enter your prompt")

if st.button('Summarize'):
    result=model.invoke(user_input)
    print(result)
    st.write(result.content)
    