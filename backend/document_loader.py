from langchain_community.document_loaders import PyPDFium2Loader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.schema import Document

def load_and_chunk_pdf(file_path):
    """
    Loads a PDF using PyPDFium2Loader and splits into chunks for RAG.
    Returns a list of LangChain Document objects.
    """
    try:
        loader = PyPDFium2Loader(file_path)
        docs = loader.load()
    except Exception as e:
        raise RuntimeError(f"Failed to load PDF: {e}")

    # Split the documents into smaller chunks
    splitter = RecursiveCharacterTextSplitter(
        chunk_size=500,
        chunk_overlap=100
    )

    chunked_docs = splitter.split_documents(docs)

    return chunked_docs
