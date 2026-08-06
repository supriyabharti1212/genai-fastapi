from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.db.session import get_db
from app.schemas.chat_schema import ChatRequest, ChatResponse
from app.services.chat_service import ask_llm

router = APIRouter()


@router.post("/chat", response_model=ChatResponse)
def chat(
    request: ChatRequest,
    db: Session = Depends(get_db)
):
    answer = ask_llm(
        db=db,
        question=request.question
    )

    return ChatResponse(
        question=request.question,
        answer=answer,
        model="qwen2.5:3b"
    )