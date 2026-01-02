from fastapi import APIRouter
from ingestion.loader import load_documents
from ingestion.splitter import split_docs
from vectorstore.vector_db import create_or_load_vectorstore
from chains.rag_chains import get_rag_chain

router = APIRouter()

@router.post("/ingest")
def ingest(file_path: str):
    docs = load_documents(file_path)
    chunks = split_docs(docs)
    create_or_load_vectorstore(chunks)

    return {
        "status": "success",
        "message": "Documents ingested successfully",
        "chunks_created": len(chunks)
    }

@router.post("/query")
def query(question: str):
    chain = get_rag_chain()
    answer = chain.invoke(question)

    return {
        "question": question,
        "answer": answer
    }
