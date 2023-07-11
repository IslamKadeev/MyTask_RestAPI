from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.exc import OperationalError

from models.task import Base


DATABASE_URL = "postgresql://username:password@localhost:5432/task_manager"


def get_engine():
    return create_engine(DATABASE_URL)


def create_database():
    engine = get_engine()
    Base.metadata.create_all(bind=engine)


def check_database_connection():
    try:
        engine = get_engine()
        engine.connect()
        print("Database connection successful.")
    except OperationalError as e:
        print(f"Failed to connect to the database. Error: {str(e)}")


def get_db():
    engine = get_engine()
    SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
