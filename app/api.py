from fastapi import APIRouter, HTTPException
from app.schemas import Transaction, Prediction
from app.services import process_transaction

router = APIRouter()
'''
Defines a POST endpoint at /predict.
Expects a request body matching the Transaction schema.
Returns a response shaped like the Prediction schema.
Both schemas are defined in schemas.py.
'''
@router.post("/predict", response_model=Prediction)
def predict_fraud(tx: Transaction):
    try:
        result = process_transaction(tx)
        return result
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))