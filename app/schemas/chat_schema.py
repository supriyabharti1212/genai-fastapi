from pydantic import BaseModel


class ChatRequest(BaseModel):
    question: str


class ChatResponse(BaseModel):
    question: str
    answer: str
    model: str


class ChatHistoryResponse(BaseModel):
    id: int
    question: str
    answer: str
    model: str

    class Config:
        from_attributes = True