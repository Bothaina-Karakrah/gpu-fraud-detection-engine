 🚀 GPU-Accelerated Fraud Detection Engine

A fraud detection backend combining rule-based heuristics and a deep learning model, with GPU acceleration using PyTorch and FastAPI.

---

## 📌 Project Goals

- Detect fraudulent transactions using a hybrid of:
  - 🧠 Machine Learning (PyTorch)
  - ✅ Business Rules Engine
- Leverage GPU acceleration for fast batch inference.
- Build a full-stack fraud engine with:
  - PostgreSQL + SQLAlchemy (data layer)
  - FastAPI (API layer)
  - PyTorch (ML layer)

---

## ✅ Completed (Day 1–4)

### 🔧 Day 1-2: Core Architecture
- API endpoints for transaction processing
- Rule-based fraud detection engine (like my Meta project)
- Database schema for transactions and fraud patterns


### ✅ Day 3-4: GPU Acceleration
- Implement ML model inference on GPU
- Batch processing for high throughput
- Performance benchmarking (CPU vs GPU)

### 🧪 Testing
- Wrote and ran unit tests for `services.py` and `rules_engine.py`
- Verified creating the database table

---

## 🗂️ Project Structure

app/
├── init.py
├── database.py         # SQLAlchemy engine + session setup
├── init.db             # init the table
├── models.py           # DB model: TransactionRecord
├── schemas.py          # Pydantic schemas for API
├── ml_model.py         # PyTorch fraud detection model
├── ml_inference.py     # Inference logic (GPU/CPU)
├── rules_engine.py     # Simple rule-based fraud detection
├── services.py         # Core service: process_transaction()
tests/
└── test_services.py    # Unit test for service logic
└── test_rules.py       # Unit test for rules engine

---

## ▶️ How to Run Tests

```bash
PYTHONPATH=. .venv/bin/pytest tests/test_services.py
```

## 💡 What’s Next (Day 5+)

### 🏗️ Day 5-6: Advanced Features
- Real-time scoring with sub-millisecond latency
- Anomaly detection algorithms
- Performance monitoring dashboard
### Day 7: Polish & Documentation
- Comprehensive testing suite
- Performance metrics and benchmarks
- Clean code documentation


## 🧠 Example Prediction

POST /predict
{
  "user_id": 123,
  "amount": 1200.0,
  "timestamp": "2025-07-17T12:34:56",
  "merchant_id": 42,
  "category": "electronics"
}

Response:
{
  "is_fraud": true,
  "score": 0.81
}

--- 

## 📌 Author

Built by Bothaina Karakrah
With assistance from PyTorch, FastAPI, and SQLAlchemy ❤️