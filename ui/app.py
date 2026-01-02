import streamlit as st
import requests

API_URL = "http://127.0.0.1:8000"

st.set_page_config(page_title="Enterprise RAG System", layout="wide")

st.title("📄 Enterprise RAG System")
st.markdown("Ask questions from your PDF documents using RAG")

# ---------------------------
# Document Ingestion Section
# ---------------------------
st.header("📥 Document Ingestion")

file_path = st.text_input(
    "Enter PDF file path (relative to project root)",
    placeholder="data/raw/sample.pdf"
)

if st.button("Ingest Document"):
    if not file_path:
        st.warning("Please enter a file path")
    else:
        with st.spinner("Ingesting document..."):
            response = requests.post(
                f"{API_URL}/ingest",
                params={"file_path": file_path}
            )

            if response.status_code == 200:
                data = response.json()
                st.success("Ingestion successful!")
                st.json(data)
            else:
                st.error("Ingestion failed")
                st.text(response.text)

# ---------------------------
# Query Section
# ---------------------------
st.header("💬 Ask a Question")

question = st.text_input(
    "Enter your question",
    placeholder="What is this document about?"
)

if st.button("Ask"):
    if not question:
        st.warning("Please enter a question")
    else:
        with st.spinner("Generating answer..."):
            response = requests.post(
                f"{API_URL}/query",
                params={"question": question}
            )

            if response.status_code == 200:
                answer = response.json()["answer"]
                st.subheader("Answer")
                st.write(answer)
            else:
                st.error("Query failed")
                st.text(response.text)
