from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from .config import settings

username = settings.database_username
password = settings.database_password
hostname = settings.database_hostname
port = settings.database_port
name = settings.database_name


SQLALCHEMY_DATABASE_URL=f"postgresql://{username}:{password}@{hostname}:{port}/{name}"

engine = create_engine(SQLALCHEMY_DATABASE_URL)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()    
