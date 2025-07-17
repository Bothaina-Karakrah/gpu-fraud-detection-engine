from app.rules_engine import apply_rules
from app.schemas import Transaction

def test_high_amount_detected():
    tx = Transaction(
        user_id=1,
        amount=15000.0,
        timestamp="2025-07-13T04:00:00Z",  # Late night
        merchant_id="123",
        category="gambling"
    )
    result = apply_rules(tx)
    assert result.is_fraud is True
    assert result.score >= 0.5

def test_low_risk_transaction():
    tx = Transaction(
        user_id=2,
        amount=100.0,
        timestamp="2025-07-13T10:00:00Z",  # Morning
        merchant_id="BestBuy",
        category="groceries"
    )
    result = apply_rules(tx)
    assert result.is_fraud is False
    assert result.score < 0.5

def test_suspicious_merchant_id():
    tx = Transaction(
        user_id=3,
        amount=300.0,
        timestamp="2025-07-13T12:00:00Z",
        merchant_id="99",  # Numeric and short
        category="electronics"
    )
    result = apply_rules(tx)
    assert result.score > 0.0

def test_just_under_threshold():
    tx = Transaction(
        user_id=4,
        amount=9999.0,
        timestamp="2025-07-13T03:00:00Z",
        merchant_id="crypto123",
        category="crypto"
    )
    result = apply_rules(tx)
    assert result.is_fraud is True
    assert result.score >= 0.5