from chains.rag_chains import get_rag_chain

qa = get_rag_chain()

question = "What is this document mainly about?"
answer = qa.invoke(question)

print("Question:", question)
print("\nAnswer:\n", answer)
