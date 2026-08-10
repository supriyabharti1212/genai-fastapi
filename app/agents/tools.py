from langchain_core.tools import tool

from app.rag.vector_store import get_vector_store


@tool
def search_documents(question: str) -> str:
    """Search the knowledge base for information relevant to the user's question."""

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