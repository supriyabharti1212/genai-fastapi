from sqlalchemy.orm import Session

from app.db.crud import save_chat
from app.llm.ollama_client import llm
# from app.prompts.prompt_template import chat_prompt
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
You are a question-answering assistant.

Use ONLY the information provided in the context below to answer the question.

Rules:
- Do not use outside knowledge.
- Do not make up facts.
- Do not add Python code or unrelated examples.
- If the answer is not present in the context, say:
  "I don't have enough information in the provided context."
- Keep the answer concise and directly related to the question.

Context:
{context}

Question:
{question}

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