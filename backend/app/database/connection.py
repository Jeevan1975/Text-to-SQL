from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from ..config import settings


DATABASE_URL = (
    f"postgresql://postgres:{settings.SUPABASE_PASSWORD}@{settings.SUPABASE_HOST}:{settings.SUPABASE_PORT}/postgres"
)

engine = create_engine(
    DATABASE_URL,
    pool_pre_ping=True,
    pool_size=10,
    max_overflow=20
)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()