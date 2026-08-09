from sqlalchemy.orm import Session

from app.db.crud import save_chat
from app.llm.ollama_client import llm
from app.prompts.prompt_template import chat_prompt
from app.utils.logger import logger
from app.core.exceptions import LLMException
from app.db.crud import get_chat_history
from app.rag.vector_store import get_vector_store


def ask_llm(db: Session, question: str):
    logger.info(f"User Question: {question}")

    try:
        vector_store = get_vector_store()

        documents = vector_store.similarity_search(
            question,
            k=2
        )

        context = "\n\n".join(
            document.page_content
            for document in documents
        )

        prompt = f"""
Answer the user's question using the context below.

Context:
{context}

Question:
{question}

If the context does not contain enough information, say that you don't have enough information.

Answer:
"""

        response = llm.invoke(prompt)

        answer = response.content

        save_chat(
            db=db,
            question=question,
            answer=answer,
            model="qwen2.5:3b"
        )

        logger.info("Chat saved successfully.")

        return answer

    except Exception as e:
        logger.error(str(e))
        raise LLMException()


def get_history(db: Session):
    return get_chat_history(db)