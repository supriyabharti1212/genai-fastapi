from sqlalchemy.orm import Session
from langchain_core.messages import HumanMessage

from app.db.crud import save_chat
from app.db.crud import get_chat_history
from app.agents.graph import agent_graph

from app.utils.logger import logger
from app.core.exceptions import LLMException


def ask_llm(db: Session, question: str, thread_id: str):
    logger.info(f"User Question: {question}")

    try:
        result = agent_graph.invoke(
            {
                "messages": [
                    HumanMessage(content=question)
                ]
            },
            config={
                "configurable": {
                    "thread_id": thread_id
                }
            }
        )

        answer = result["messages"][-1].content

        save_chat(
            db=db,
            question=question,
            answer=answer,
            model="qwen2.5:3b"
        )

        logger.info("Chat saved successfully.")

        return answer

    except Exception:
        logger.exception("Agent/RAG error")
        raise LLMException()


def get_history(db: Session):
    return get_chat_history(db)