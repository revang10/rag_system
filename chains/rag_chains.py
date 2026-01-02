from langchain_community.llms import Ollama
from langchain_core.prompts import PromptTemplate
from langchain_core.runnables import RunnablePassthrough
from langchain_core.output_parsers import StrOutputParser

from vectorstore.vector_db import create_or_load_vectorstore

def get_rag_chain():
    vectorstore = create_or_load_vectorstore()
    retriever = vectorstore.as_retriever(search_kwargs={"k": 5})

    llm = Ollama(model="mistral")

    prompt = PromptTemplate.from_template(
        """
        You are an assistant that answers questions using the provided context.
        If the answer is not in the context, say you don't know.

        Context:
        {context}

        Question:
        {question}

        Answer:
        """
    )

    chain = (
        {"context": retriever, "question": RunnablePassthrough()}
        | prompt
        | llm
        | StrOutputParser()
    )

    return chain
