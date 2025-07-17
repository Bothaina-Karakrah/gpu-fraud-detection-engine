from datetime import datetime
from app.schemas import *
import re

# Fraud policies to detect fraud txn
def apply_rules(tx) -> Prediction:
    """Apply fraud detection rules to a transaction."""
    fraud_score = 0.0
    current_time = datetime.fromisoformat(tx.timestamp.replace('Z', '+00:00'))

    # ============ AMOUNT RULES ============
    if tx.amount > 10000:
        fraud_score += 0.8
    elif tx.amount > 5000:
        fraud_score += 0.4

    # Round numbers
    if tx.amount % 100 == 0 and tx.amount > 500:
        fraud_score += 0.2

    # Just under limits
    if 9000 <= tx.amount < 10000:
        fraud_score += 0.4

    # ============ CATEGORY RULES ============
    high_risk_categories = {"gambling", "cash_advance", "crypto", "wire_transfer", "money_transfer"}
    if tx.category.lower() in high_risk_categories:
        fraud_score += 0.3
    # Gambling specific
    if tx.category == "gambling" and tx.amount > 500:
        fraud_score += 0.6

    # ============ TIME RULES ============
    # Late night (2-5 AM)
    if 2 <= current_time.hour <= 5:
        fraud_score += 0.3

    # Weekend
    if current_time.weekday() >= 5:
        fraud_score += 0.1

    # ============ MERCHANT RULES ============
    # Suspicious merchant patterns
    if len(tx.merchant_id) < 3 or re.match(r'^[0-9]+$', tx.merchant_id):
        fraud_score += 0.2

    # Determine fraud flag
    is_fraud = fraud_score >= 0.5

    return Prediction(is_fraud=is_fraud, score=min(fraud_score, 1.0))