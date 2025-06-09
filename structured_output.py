from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv, find_dotenv
load_dotenv(find_dotenv(), override=True)
from pydantic import BaseModel,Field


llm = ChatGoogleGenerativeAI(model='gemini-1.5-flash')

import fitz  # PyMuPDF

def extract_text_from_pdf(pdf_path):
    text = ""
    # Open the PDF
    with fitz.open(pdf_path) as doc:
        for page in doc:
            text += page.get_text()
    return text

# Example usage
pdf_file = "AIsample.pdf"  # Replace with your PDF file path
content = extract_text_from_pdf(pdf_file)
#print(content)

class Review(BaseModel):
    key_points: list[str] = Field(description="the most important top 5 keywords and key terms from the following document. Provide them as a comma-separated list of single words or very short phrases, without any descriptive sentences.")

structured_llm = llm.with_structured_output(Review)


result=structured_llm.invoke(content)



key_term=result.key_points
for item in key_term:
    print(item)