"""
Run it using `PYTHONPATH=. .venv/bin/pytest tests/test_services.py`
"""
import pytest
from app.schemas import Transaction
from app.services import process_transaction

def test_process_transaction():
    # Create a sample transaction
    tx = Transaction(
        user_id=1,
        amount=12000,  # high amount to trigger fraud rules
        timestamp="2025-07-17T03:00:00Z",  # late night triggers time rule
        merchant_id="12345",
        category="gambling"
    )

    prediction = process_transaction(tx)

    assert prediction.is_fraud is True
    assert 0 <= prediction.score <= 1