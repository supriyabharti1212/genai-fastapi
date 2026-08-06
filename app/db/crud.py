

from sqlalchemy.orm import Session

from app.db.models import ChatHistory


def save_chat(db: Session, question: str, answer: str, model: str):

    chat = ChatHistory(
        question=question,
        answer=answer,
        model=model
    )

    db.add(chat)

    db.commit()

    db.refresh(chat)

    return chat