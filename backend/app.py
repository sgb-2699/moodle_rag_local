import os
import sys
from flask import Flask, request, jsonify
from flask_cors import CORS

# Extend import path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from backend.document_loader import load_and_chunk_pdf
from backend.vector_store import create_vectorstore, load_vectorstore
from backend.rag_engine import build_qa_chain
from backend.sql_agent import build_sql_agent

def run_with_feedback(agent, query, max_attempts=1):
    attempt = 0
    last_error = ""
    while attempt < max_attempts:
        try:
            result = agent.run(query)
            return result
        except Exception as e:
            last_error = str(e)
            # Feedback prompt for self-correction
            query = (
                f"Your previous response could not be parsed due to this error:\n"
                f"{last_error}\n"
                "Please strictly follow the required format and do not provide troubleshooting advice or explanations. "
                "Respond only in the specified format."
                f"\nOriginal question: {query}"
            )
            attempt += 1
    # If all attempts fail, return the last error
    return f"❌ Structured query failed after {max_attempts} attempts: {last_error}"



app = Flask(__name__)
CORS(app)

qa_chain = None
current_doc_name = None

@app.route("/upload", methods=["POST"])
def upload_file():
    global qa_chain, current_doc_name

    if "file" not in request.files:
        return jsonify({"error": "No file part"}), 400

    file = request.files["file"]
    if file.filename == "":
        return jsonify({"error": "No selected file"}), 400

    filename = file.filename
    doc_name = os.path.splitext(filename)[0]
    current_doc_name = doc_name

    filepath = os.path.join("data", filename)
    os.makedirs("data", exist_ok=True)
    file.save(filepath)

    try:
        vectorstore = load_vectorstore(doc_name)
        if vectorstore is None:
            documents = load_and_chunk_pdf(filepath)
            vectorstore = create_vectorstore(documents, doc_name)

        qa_chain = build_qa_chain(vectorstore)
        return jsonify({"message": f"✅ {filename} uploaded and ready."}), 200

    except Exception as e:
        return jsonify({
            "message": "⚠️ File upload succeeded, but processing failed.",
            "error": str(e)
        }), 500

@app.route("/query", methods=["POST"])
def query():
    global qa_chain

    if not qa_chain:
        return jsonify({"error": "No document indexed yet."}), 400

    data = request.get_json()
    user_query = data.get("query", "")

    if not user_query:
        return jsonify({"error": "No query provided."}), 400

    try:
        result = qa_chain.invoke({"query": user_query})
        return jsonify({"response": result["result"]})
    except Exception as e:
        return jsonify({"error": f"Failed to answer query: {str(e)}"}), 500


# 🆕 Structured query endpoint
@app.route("/structured-query", methods=["POST"])
def structured_query():
    data = request.get_json()
    user_query = data.get("query")

    if not user_query:
        return jsonify({"error": "Query field is required."}), 400

    try:
        agent = build_sql_agent()  # No db_key needed
        response = run_with_feedback(agent, user_query)
        return jsonify({"response": response})
    except Exception as e:
        return jsonify({"error": f"Structured query failed: {str(e)}"}), 500

if __name__ == "__main__":
    print("✅ Flask server is running on http://localhost:5000 ...")
    app.run(host="0.0.0.0", port=5000, debug=True)
