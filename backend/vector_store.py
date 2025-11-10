import os
from langchain_community.vectorstores import FAISS
from langchain_ollama import OllamaEmbeddings

# Path to persistent FAISS index
INDEX_DIR = os.path.join(os.path.dirname(__file__), '..', 'indexes')
os.makedirs(INDEX_DIR, exist_ok=True)

def create_vectorstore(documents, doc_name="default", model_name="mistral"):
    """
    Creates (or loads) a FAISS vector store from a list of documents.
    Stores index persistently by document name.
    """
    embeddings = OllamaEmbeddings(model=model_name)
    index_path = os.path.join(INDEX_DIR, doc_name)

    if os.path.exists(index_path):
        print(f"📂 Loading existing FAISS index for {doc_name}...")
        vectorstore = FAISS.load_local(index_path, embeddings, allow_dangerous_deserialization=True)
        vectorstore.add_documents(documents)
    else:
        print(f"🆕 Creating new FAISS index for {doc_name}...")
        vectorstore = FAISS.from_documents(documents, embeddings)
    
    vectorstore.save_local(index_path)
    return vectorstore


def load_vectorstore(doc_name="default", model_name="mistral"):
    """
    Loads an existing FAISS vector store for the given doc name.
    Returns None if the index doesn't exist.
    """
    embeddings = OllamaEmbeddings(model=model_name)
    index_path = os.path.join(INDEX_DIR, doc_name)

    if not os.path.exists(index_path):
        return None

    print(f"📦 Loading FAISS index for {doc_name}...")
    return FAISS.load_local(index_path, embeddings, allow_dangerous_deserialization=True)
