# rag_engine.py

from langchain.chains import RetrievalQA
from langchain_community.llms import Ollama


def build_qa_chain(vectorstore, model_name="mistral"):
    """
    Builds a RetrievalQA chain using a FAISS vector store and local Ollama model.
    Returns the chain object which can be used to run queries.
    """
    try:
        llm = Ollama(model=model_name)
        retriever = vectorstore.as_retriever()
        qa_chain = RetrievalQA.from_chain_type(
            llm=llm,
            retriever=retriever,
            return_source_documents=True  # Optional: helpful for debugging
        )
        return qa_chain
    except Exception as e:
        raise RuntimeError(f"Failed to build RAG chain: {e}")
