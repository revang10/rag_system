from embeddings.embedder import get_embeddings

embeddings = get_embeddings()

vectors = embeddings.embed_documents([
    "Machine learning is fun",
    "I love studying generative AI"
])

print("Number of vectors:", len(vectors))
print("Vector length:", len(vectors[0]))
