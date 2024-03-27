from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine

from config import get_settings

settings = get_settings()

DB_URL = f"postgresql://{settings.DB_USERNAME}:{settings.DB_PASSWORD}@3.10.22.240:5432/{settings.DB_NAME}"

engine = create_engine(DB_URL, connect_args={}, future=True)
SessionLocal = sessionmaker(future=True, autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()


# get the db
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
