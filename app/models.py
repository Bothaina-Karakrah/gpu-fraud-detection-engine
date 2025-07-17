from sqlalchemy import Column, Integer, String, Float, Boolean
from app.database import Base

class TransactionRecord(Base):
    __tablename__ = "transactions"
    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer)
    amount = Column(Float)
    timestamp = Column(String)
    merchant_id = Column(String)
    category = Column(String)
    is_fraud = Column(Boolean, default=False, nullable=False)
    risk_score = Column(Float)