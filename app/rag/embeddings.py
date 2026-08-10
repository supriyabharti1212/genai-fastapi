from langchain_google_genai import GoogleGenerativeAIEmbeddings
from app.core.config import settings


def get_embeddings():
    return GoogleGenerativeAIEmbeddings(
        model="gemini-embedding-2-preview",
        task_type="RETRIEVAL_QUERY",
        google_api_key=settings.GEMINI_API_KEY,
    )