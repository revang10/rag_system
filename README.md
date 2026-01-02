# 📌 Enterprise RAG System (End-to-End)

An **end-to-end Retrieval Augmented Generation (RAG) system** built using **FastAPI, LangChain, FAISS, and Streamlit**, designed to ingest documents, store embeddings, and answer user queries using Large Language Models (LLMs).

This project demonstrates **real-world MLOps + GenAI engineering practices** and is suitable for production-scale knowledge-based applications.

---

## 🚀 Project Objective

The main goal of this project is to:

- Build a **complete RAG pipeline from scratch**
- Enable **document ingestion and semantic search**
- Generate **context-aware answers using LLMs**
- Follow **clean architecture and MLOps best practices**
- Provide both **API access and UI-based interaction**

---

## 🧠 What Problem Does It Solve?

Traditional LLMs:
- Do not have access to private or dynamic data
- Can hallucinate answers

This system solves that by:
- Retrieving **relevant document chunks**
- Passing them as **context to the LLM**
- Producing **grounded and accurate responses**

---

## 🏗️ System Architecture

PDF Documents
    ↓
Text Chunking
    ↓
Embedding Generation
    ↓
FAISS Vector Store
    ↓
Retriever
    ↓
LLM (Ollama / Mistral)
    ↓
Final Answer




---

## 🛠️ Tech Stack

### 🔹 Backend
- **Python**
- **FastAPI** – API framework
- **LangChain** – RAG orchestration
- **FAISS** – Vector database
- **Sentence Transformers** – Embedding generation

### 🔹 LLM
- **Ollama**
- **Mistral / LLaMA (local inference)**

### 🔹 Frontend
- **Streamlit** – Interactive UI

---

## 📂 Project Structure

enterprise-rag-system/
│
├── api/ # FastAPI routes
├── ingestion/ # Document ingestion logic
├── embeddings/ # Embedding generation
├── vectorstore/ # FAISS vector database
├── chains/ # RAG chains and retrievers
├── ui/ # Streamlit application
├── config/ # Configurations
│
├── requirements.txt
├── README.md
├── .gitignore


---

## ⚙️ How the System Works (Step-by-Step)

### 1️⃣ Document Ingestion
- PDFs are loaded and parsed
- Text is split into overlapping chunks

### 2️⃣ Embedding Generation
- Each chunk is converted into a vector using sentence transformers

### 3️⃣ Vector Storage
- Embeddings are stored in a FAISS index for fast similarity search

### 4️⃣ Query Processing
- User query is embedded
- Relevant chunks are retrieved from FAISS

### 5️⃣ Answer Generation
- Retrieved context is passed to the LLM
- LLM generates a grounded answer

---

## ▶️ How to Run the Project

### 1️⃣ Install Dependencies
```bash
pip install -r requirements.txt
```

## 🚀 Running the Application

### 2️⃣ Start Ollama (LLM)
ollama run mistral

### 3️⃣ Run FastAPI Backend
uvicorn api.main:app --reload


FastAPI will be available at:

http://localhost:8000

### 4️⃣ Run Streamlit UI
streamlit run ui/app.py


Streamlit UI will be available at:

http://localhost:8501

## 👨‍💻 Author

Revan Gaikwad
End-to-End RAG System Project

