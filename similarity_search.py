from langchain_huggingface import HuggingFaceEmbeddings
import numpy as np 
from sklearn.metrics.pairwise import cosine_similarity


embedding = HuggingFaceEmbeddings(model_name='sentence-transformers/all-MiniLM-L6-v2')

query="i don't like python"
document=[
    "The sky is blue.",
    "I love playing football.",
    "Python is a great programming language.",
    "Artificial intelligence is the future.",
    "He is reading a book on machine learning.",
    "The weather is sunny and bright today."
]
Query_Em = embedding.embed_query(query)
document_Em = embedding.embed_documents(document)

similarity_socre = cosine_similarity([Query_Em],document_Em)[0]
index,score=sorted(list(enumerate(similarity_socre)),key=lambda x:x[1])[-1]
print(query)
print(document[index])
print(f"Similarity score is {score}")