# rag_engine.py

from langchain.chains import RetrievalQA
from langchain_community.llms import Ollama

from langchain_google_genai import ChatGoogleGenerativeAI

local = True

if(local):
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

else:
    def build_qa_chain(vectorstore, model_name="gemini-2.0-flash"):
            """
            Builds a RetrievalQA chain using a FAISS vector store and Google Gemini model.
            Returns the chain object which can be used to run queries.
            """
            try:
                llm = ChatGoogleGenerativeAI(model=model_name, temperature=0.2)
                retriever = vectorstore.as_retriever()
                qa_chain = RetrievalQA.from_chain_type(
                    llm=llm,
                    retriever=retriever,
                    return_source_documents=True  # Optional: helpful for debugging
                )
                return qa_chain
            except Exception as e:
                raise RuntimeError(f"Failed to build RAG chain: {e}")
          
