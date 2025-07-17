from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base

# Create engine - connects to PostgreSQL database
DATABASE_URL = "postgresql://bothainakarakrah@localhost/fraud_db"
engine = create_engine(DATABASE_URL)

# Create session factory - manages database transactions
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()