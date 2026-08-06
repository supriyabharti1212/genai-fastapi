

from sqlalchemy import Column, Integer, String, Text

from app.db.database import Base



class ChatHistory(Base):
    __tablename__ = "chat_history"

    id = Column(Integer, primary_key=True, index=True)

    question = Column(Text, nullable=False)

    answer = Column(Text, nullable=False)

    model = Column(String, nullable=False)