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

    ids = [
        "krishna-info",
        "bhagavad-gita-info",
    ]

    vector_store = get_vector_store()

    existing = vector_store.get(ids=ids)
    existing_ids = set(existing.get("ids", []))

    new_documents = []
    new_ids = []

    for document, doc_id in zip(documents, ids):
        if doc_id not in existing_ids:
            new_documents.append(document)
            new_ids.append(doc_id)

    if new_documents:
        vector_store.add_texts(
            texts=new_documents,
            ids=new_ids,
        )
        print(f"Added {len(new_documents)} new documents to ChromaDB.")
    else:
        print("All documents already exist in ChromaDB.")


if __name__ == "__main__":
    ingest_documents()