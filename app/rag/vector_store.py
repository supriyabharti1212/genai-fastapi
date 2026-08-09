

from langchain_chroma import Chroma

from app.rag.embeddings import get_embeddings


def get_vector_store():
    return Chroma(
        collection_name="genai_documents",
        embedding_function=get_embeddings(),
        persist_directory="./chroma_db",
    )