from sqlalchemy import create_engine, MetaData
from sqlalchemy.orm import sessionmaker, close_all_sessions
from app.core.config import DATABASE_URL

close_all_sessions()

engine = create_engine(DATABASE_URL)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

def get_db():
    db = SessionLocal()
    try:
        db.rollback()
        yield db
    finally:
        db.close()

def get_metadata():
    metadata = MetaData()
    metadata.reflect(engine)
    return metadata