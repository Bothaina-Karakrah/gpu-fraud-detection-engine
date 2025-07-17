from pydantic import BaseModel

# Define the Transaction schema
class Transaction(BaseModel):
    user_id: int
    amount: float
    timestamp: str
    merchant_id: str
    category: str

# Define the Prediction schema
class Prediction(BaseModel):
    is_fraud: bool
    score: float