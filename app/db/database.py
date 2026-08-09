from app.core.config import settings




print("Database Connected...")
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, DeclarativeBase

# DATABASE_URL = "postgresql://postgres@localhost:5432/genai_db"
# DATABASE_URL = "postgresql://postgres@host.docker.internal:5432/genai_db"
DATABASE_URL = settings.DATABASE_URL
engine = create_engine(DATABASE_URL)

SessionLocal = sessionmaker(
    autocommit=False,
    autoflush=False,
    bind=engine
)


class Base(DeclarativeBase):
    pass


from app.db.models import ChatHistory

Base.metadata.create_all(bind=engine)    