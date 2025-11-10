from backend.document_loader import load_and_chunk_pdf
from backend.vector_store import create_vectorstore
from backend.rag_engine import build_qa_chain

# Replace this with an actual PDF path
file_path = "data/notes.pdf"

chunks = load_and_chunk_pdf(file_path)
vs = create_vectorstore(chunks)
qa = build_qa_chain(vs)

# response = qa.run("Summarize this document")
# print("\n🧠 RAG Response:\n", response)

response = qa.invoke({"query": "Summarize this document"})
print(response["result"])

