# src/retriever.py
from pathlib import Path
from langchain_huggingface import HuggingFaceEmbeddings
from langchain_community.vectorstores import FAISS
from langchain.text_splitter import CharacterTextSplitter
from langchain.docstore.document import Document

DATA_DIR = Path("data/docs")
FAISS_DIR = Path("faiss_index")

def build_faiss_index():
    """
    Reads all .txt files from DATA_DIR, splits them into chunks, builds FAISS index,
    and saves it locally in FAISS_DIR.
    """
    if not DATA_DIR.exists():
        raise FileNotFoundError(f"Docs directory not found: {DATA_DIR}")
    
    all_docs = []
    for file_path in DATA_DIR.glob("*.txt"):
        text = file_path.read_text(encoding="utf-8")
        all_docs.append(Document(page_content=text, metadata={"source": file_path.name}))

    # Split documents into smaller chunks for better retrieval
    splitter = CharacterTextSplitter(chunk_size=500, chunk_overlap=50)
    split_docs = splitter.split_documents(all_docs)
    
    print(f"Found {len(all_docs)} documents, split into {len(split_docs)} chunks")

    # Build embeddings and FAISS vector store
    embeddings = HuggingFaceEmbeddings(model_name="sentence-transformers/all-MiniLM-L6-v2")
    vect = FAISS.from_documents(split_docs, embeddings)
    
    FAISS_DIR.mkdir(exist_ok=True)
    vect.save_local(str(FAISS_DIR))
    print(f"✅ FAISS index saved to {FAISS_DIR}")

def load_faiss_index():
    """
    Loads the FAISS index from FAISS_DIR
    """
    if not FAISS_DIR.exists():
        raise FileNotFoundError(f"FAISS index directory not found: {FAISS_DIR}")
    
    embeddings = HuggingFaceEmbeddings(model_name="sentence-transformers/all-MiniLM-L6-v2")
    vect = FAISS.load_local(str(FAISS_DIR), embeddings, allow_dangerous_deserialization=True)
    return vect

if __name__ == "__main__":
    build_faiss_index()
