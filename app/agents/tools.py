
from app.rag.vector_store import get_vector_store


def search_documents(question: str) -> str:
    vector_store = get_vector_store()

    documents = vector_store.similarity_search(
        question,
        k=2
    )

    if not documents:
        return "No relevant information found in the documents."

    return "\n\n".join(
        document.page_content
        for document in documents
    )