from sqlalchemy import create_engine, text
from sqlalchemy.orm import sessionmaker
import os
from pathlib import Path
from dotenv import load_dotenv

env_path = Path('.')/'.env'
load_dotenv(dotenv_path=env_path)

SQLALCHEMY_DATABASE_URL=""

def get_engine():
    if os.getenv('Service').lower()=="sqlite":
        SQLALCHEMY_DATABASE_URL = os.environ['SQLite_URL']
        return create_engine(
            SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False}
        )
    elif os.getenv('Service').lower()=="postgres":
        SQLALCHEMY_DATABASE_URL = os.environ['PostgreSQL_URL']
    elif os.getenv('Service').lower()=="mysql":
        SQLALCHEMY_DATABASE_URL = os.environ['MySQL_URL']
    else:
        SQLALCHEMY_DATABASE_URL = os.environ['SQLServer_URL']
    return create_engine(
            SQLALCHEMY_DATABASE_URL
        )

engine = get_engine()

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

def get_db():
  db = SessionLocal()
  try:
    if os.getenv('Service').lower()=="sqlite":
        db.execute(text("PRAGMA foreign_keys=ON"))
    yield db
  finally:
    db.close()
