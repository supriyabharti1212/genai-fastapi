from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.db.session import get_db
from app.schemas.chat_schema import ChatRequest, ChatResponse
from app.services.chat_service import ask_llm
from typing import List
from app.schemas.chat_schema import ChatHistoryResponse
from app.services.chat_service import get_history

router = APIRouter()


@router.post("/chat", response_model=ChatResponse)
def chat(
    request: ChatRequest,
    db: Session = Depends(get_db)
    ):
    answer = ask_llm(
    db=db,
    question=request.question,
    thread_id=request.thread_id
)
    return ChatResponse(
        question=request.question,
        answer=answer,
        model="qwen2.5:3b"
    )


@router.get("/history", response_model=List[ChatHistoryResponse])
def history(
    db: Session = Depends(get_db)
):
    return get_history(db)