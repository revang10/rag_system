from ingestion.loader import load_documents
from ingestion.splitter import split_docs
from vectorstore.vector_db import create_or_load_vectorstore

docs = load_documents("data/raw/Flutter_Documentation.pdf")
chunks = split_docs(docs)

vectorstore = create_or_load_vectorstore(chunks)

results = vectorstore.similarity_search("What is this document about?", k=3)

print("Retrieved chunks:\n")
for i, doc in enumerate(results, 1):
    print(f"--- Chunk {i} ---")
    print(doc.page_content[:300])
    print()
