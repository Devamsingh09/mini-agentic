# src/retriever.py
from pathlib import Path
from langchain_community.vectorstores import FAISS
from langchain_huggingface import HuggingFaceEmbeddings
from langchain.docstore.document import Document

DATA_DIR = Path("data/docs")
FAISS_DIR = Path("faiss_index")

def build_faiss_index():
    embeddings = HuggingFaceEmbeddings(model_name="sentence-transformers/all-MiniLM-L6-v2")
    docs = []
    for file_path in DATA_DIR.glob("*.txt"):
        text = file_path.read_text(encoding="utf-8")
        docs.append(Document(page_content=text, metadata={"source": file_path.name}))
    vect = FAISS.from_documents(docs, embeddings)
    vect.save_local(str(FAISS_DIR))
    print(f"FAISS index saved to {FAISS_DIR}")

def load_faiss_index():
    embeddings = HuggingFaceEmbeddings(model_name="sentence-transformers/all-MiniLM-L6-v2")
    return FAISS.load_local(str(FAISS_DIR), embeddings)
