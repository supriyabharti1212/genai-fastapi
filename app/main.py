from fastapi import FastAPI
from app.services.chat_service import ask_llm
from app.schemas.chat_schema import ChatRequest , ChatResponse

app = FastAPI()


@app.get("/")
def home():
    return {
        "message": "Welcome to GenAI FastAPI Project"
    }


@app.post("/chat", response_model=ChatResponse)
def chat(request: ChatRequest):
    answer = ask_llm(request.question)
    return ChatResponse(
        answer = answer
    )
