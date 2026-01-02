from ingestion.loader import load_documents
from ingestion.splitter import split_docs

docs = load_documents("data/raw/Flutter_Documentation.pdf")
chunks = split_docs(docs)

print("Pages loaded:", len(docs))
print("Chunks created:", len(chunks))
print("\nSample chunk:\n")
print(chunks[0].page_content[:500])
