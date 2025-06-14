from langchain_text_splitters import RecursiveCharacterTextSplitter

text = """Passionate and driven third-year B.Tech student in Artificial Intelligence and Data Science, seeking a Python Developer Intern role to apply my knowledge of software development, AI models, and data structures in building scalable and intelligent systems. Eager to contribute to real-world projects and grow as a backend and AI-focused developer."""
splitter = RecursiveCharacterTextSplitter(
    chunk_size=120,
    chunk_overlap = 0,
    
)

result = splitter.split_text(text)

print(result)

