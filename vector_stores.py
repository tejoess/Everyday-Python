#chroma vector store 
#in between store and Database - Tenet(database) -> collections -> Docs
from dotenv import load_dotenv, find_dotenv
load_dotenv(find_dotenv(), override=True)
from langchain_google_genai import GoogleGenerativeAIEmbeddings
from langchain_chroma import Chroma
from langchain.schema import Document

doc1 = Document(
    page_content="David Warner is a destructive opener known for his explosive starts. He has been a key player for Sunrisers Hyderabad.",
    metadata={"team": "Sunrisers Hyderabad"}
)

doc2 = Document(
    page_content="KL Rahul is a technically sound batsman who consistently performs under pressure. He captains the Lucknow Super Giants.",
    metadata={"team": "Lucknow Super Giants"}
)

doc3 = Document(
    page_content="Faf du Plessis brings international experience and leadership to Royal Challengers Bangalore as their captain.",
    metadata={"team": "Royal Challengers Bangalore"}
)

doc4 = Document(
    page_content="Sanju Samson is a stylish batsman and the captain of Rajasthan Royals. His calm presence adds strength to the batting order.",
    metadata={"team": "Rajasthan Royals"}
)

doc5 = Document(
    page_content="Andre Russell is a powerful all-rounder known for his big-hitting and death-over bowling, playing for Kolkata Knight Riders.",
    metadata={"team": "Kolkata Knight Riders"}
)

docs = [doc1,doc2,doc3,doc4,doc5]

vector_store = Chroma(
    embedding_function=GoogleGenerativeAIEmbeddings(model="models/embedding-001"),
    persist_directory='my_chroma_db',
    collection_name='sample'
)

vector_store.add_documents(docs)

result=vector_store.get(include=['embeddings','documents','metadatas'])
print(result)

vector_store.similarity_search(
    query="who among these are a bowler",
    k=1
)

vector_store.similarity_search(
    query="who among these are a bowler",
    k=2
)

vector_store.similarity_search_with_score(
    query="who among these are a bowler",
    k=2
)

vector_store.similarity_search_with_score(
    query="who among these are a bowler",
    filter={'team':'Chennai Super kings' }
)

updated_doc1 = Document(
    page_content='Virat kohli is Goat',
    metadata={"team":"India"}
)

vector_store.update_document(document_id='',document=updated_doc1)
vector_store.delete(ids='')