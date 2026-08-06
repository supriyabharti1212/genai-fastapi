from sqlalchemy.orm import Session

from app.db.crud import save_chat
from app.llm.ollama_client import llm
from app.prompts.prompt_template import chat_prompt
from app.utils.logger import logger
from app.core.exceptions import LLMException


def ask_llm(db: Session, question: str):
    logger.info(f"User Question: {question}")

    try:
        chain = chat_prompt | llm

        response = chain.invoke(
            {
                "question": question
            }
        )

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