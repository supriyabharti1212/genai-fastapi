

from fastapi import FastAPI
from app.db import database
from app.routers.chat_router import router

app = FastAPI()


@app.get("/")
def home():
    return {
        "message": "Welcome to GenAI FastAPI Project"
    }


app.include_router(router)