

from app.rag.vector_store import get_vector_store


def ingest_documents():
    documents = [
        """
        Krishna is a major figure in Hindu traditions.
        He is traditionally associated with the Mahabharata and the Bhagavad Gita.
        Krishna is also widely known for his teachings in the Bhagavad Gita.
        """,
        """
        The Bhagavad Gita is a dialogue between Krishna and Arjuna.
        Krishna gives Arjuna guidance about duty, action, and spiritual knowledge.
        """
    ]

    vector_store = get_vector_store()

    vector_store.add_texts(documents)

    print("Documents successfully added to ChromaDB.")


if __name__ == "__main__":
    ingest_documents()