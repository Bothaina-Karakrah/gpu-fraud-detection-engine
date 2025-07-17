from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base
"""
SQLAlchemy Database Configuration for Fraud Detection Backend
-------------------------------------------------------------

Purpose:
--------
This file sets up the SQLAlchemy engine, session, and base class
for interacting with a PostgreSQL database named `fraud_db`.

Components:
-----------
1. Engine
   - Core interface to the database.
   - Used to issue SQL commands and manage DB connections.

2. Base
   - The declarative base class for ORM models.
   - All models should inherit from `Base`:
     Example: class Transaction(Base): ...
"""
# Create engine - connects to PostgresSQL database
DATABASE_URL = "postgresql://bothainakarakrah@localhost/fraud_db"
engine = create_engine(DATABASE_URL)

# Session Factory - Used to create session instances per request
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()