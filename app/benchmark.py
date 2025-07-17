import torch
import time
from app.ml_model import FraudDetectionModel
from app.ml_inference import encode_transaction
from app.schemas import Transaction
from datetime import datetime, timezone
import random

def generate_dummy_transaction():
    return Transaction(
        user_id=random.randint(1, 100),
        amount=random.uniform(1, 15000),
        timestamp = datetime.now(timezone.utc).isoformat().replace('+00:00', 'Z'),
        merchant_id=str(random.randint(100, 9999)),
        category=random.choice(["shopping", "gambling", "crypto", "transfer"])
    )

def benchmark(device, batch_size=512, iterations=10):
    model = FraudDetectionModel()
    model.load_state_dict(torch.load("model.pth", map_location=device))
    model.to(device)
    model.eval()

    transactions = [generate_dummy_transaction() for _ in range(batch_size)]
    batch = torch.stack([encode_transaction(tx) for tx in transactions]).to(device)

    start = time.time()
    with torch.no_grad():
        for _ in range(iterations):
            _ = model(batch)
    end = time.time()
    avg_time = (end - start) / iterations
    print(f"{device} | Batch size: {batch_size} | Time: {avg_time*1000:.2f} ms")

if __name__ == "__main__":
    benchmark(torch.device("cpu"))
    if torch.cuda.is_available():
        benchmark(torch.device("cuda"))