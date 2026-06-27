from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base
from sqlalchemy.exc import OperationalError
from app.core.config import DATABASE_URL
import time

engine = None

# Retry database connection
for i in range(10):
    try:
        engine = create_engine(DATABASE_URL)
        connection = engine.connect()
        connection.close()
        print("✅ Connected to PostgreSQL")
        break
    except OperationalError:
        print(f"Database not ready... retrying ({i+1}/10)")
        time.sleep(3)

if engine is None:
    raise Exception("Could not connect to PostgreSQL.")

SessionLocal = sessionmaker(
    autocommit=False,
    autoflush=False,
    bind=engine
)

Base = declarative_base()


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()