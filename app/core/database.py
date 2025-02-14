from sqlalchemy import create_engine, MetaData
from sqlalchemy.orm import sessionmaker, close_all_sessions
from app.core.config import DATABASE_URL

if DATABASE_URL is None:
    raise ValueError("DATABASE_URL environment variable is not set!")

print(f"Using database URL: {DATABASE_URL}")

# Close all previous database sessions to ensure no lingering connections
close_all_sessions()

engine = create_engine(DATABASE_URL)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

def get_metadata():
    metadata = MetaData()
    metadata.reflect(engine)
    return metadata