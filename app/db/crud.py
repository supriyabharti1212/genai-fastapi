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


def get_chat_history(db: Session):

    return (
        db.query(ChatHistory)
        .order_by(ChatHistory.id.desc())
        .all()
    )