

from langchain_ollama import ChatOllama

from app.rag.vector_store import get_vector_store


def ask_rag(question: str) -> str:
    vector_store = get_vector_store()

    documents = vector_store.similarity_search(question, k=2)

    context = "\n\n".join(
        document.page_content for document in documents
    )

    prompt = f"""
Answer the question using the context below.

Context:
{context}

Question:
{question}

Answer:
"""

    llm = ChatOllama(
        model="qwen2.5:3b",
        base_url="http://localhost:11434",
        temperature=0,
    )

    response = llm.invoke(prompt)

    return response.content