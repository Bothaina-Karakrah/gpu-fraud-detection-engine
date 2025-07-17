'''
Run the file using `PYTHONPATH=. python app/init_db.py`
Test if it succeeded using ` psql -U bothainakarakrah -d fraud_db`
Then `\dt`
'''
from app.database import Base, engine
from app.models import TransactionRecord

def init():
    print("📦 Creating database tables...")
    print(f"👉 Using database: {engine.url}")
    Base.metadata.create_all(bind=engine)
    print("✅ All tables created successfully.")

if __name__ == "__main__":
    init()