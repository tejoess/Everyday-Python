from langchain_huggingface import HuggingFaceEndpoint,ChatHuggingFace
from dotenv import load_dotenv
import os
load_dotenv()
token = os.getenv("HUGGINGFACEHUB_API_TOKEN")
print(f"TOKEN: {token}")

llm = HuggingFaceEndpoint(
    repo_id="TinyLlama/TinyLlama-1.1B-Chat-v1.0",
    task="text-generation",
    huggingfacehub_api_token=token
)
model = ChatHuggingFace(llm=llm)

result = model.invoke("what is ML")

print(result.content)