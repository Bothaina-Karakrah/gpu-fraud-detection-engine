from app.database import SessionLocal
from app.models import TransactionRecord
from app.schemas import Transaction, Prediction
from app.rules_engine import apply_rules
from app.ml_inference import run_inference

def process_transaction(tx: Transaction) -> Prediction:
    db = SessionLocal()
    try:
        record = TransactionRecord(
            user_id=tx.user_id,
            amount=tx.amount,
            timestamp=tx.timestamp,
            merchant_id=tx.merchant_id,
            category=tx.category,
            is_fraud=False
        )
        db.add(record)

        rule_result = apply_rules(tx)
        if rule_result.is_fraud:
            record.is_fraud = True
            prediction = rule_result
        else:
            score = run_inference(tx)
            fraud_detected = score > 0.7
            record.is_fraud = fraud_detected
            prediction = Prediction(is_fraud=fraud_detected, score=score)

        db.commit()
        return prediction

    finally:
        db.close()