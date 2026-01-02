import os
from langchain_community.vectorstores import FAISS
from embeddings.embedder import get_embeddings
from config.settings import VECTOR_DB_PATH

def create_or_load_vectorstore(chunks=None):
    embeddings = get_embeddings()

    if os.path.exists(VECTOR_DB_PATH) and os.listdir(VECTOR_DB_PATH):
        return FAISS.load_local(
            VECTOR_DB_PATH,
            embeddings,
            allow_dangerous_deserialization=True
        )

    if chunks is None:
        raise ValueError("No chunks provided for vectorstore creation")

    vectorstore = FAISS.from_documents(chunks, embeddings)
    vectorstore.save_local(VECTOR_DB_PATH)
    return vectorstore
