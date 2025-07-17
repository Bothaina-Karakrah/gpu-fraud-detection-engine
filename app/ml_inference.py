import torch
from app.ml_model import FraudDetectionModel
from app.schemas import Transaction
from datetime import datetime

# Set device
device = torch.device("cuda" if torch.cuda.is_available() else "cpu")

model = FraudDetectionModel()
model.load_state_dict(torch.load("model.pth", map_location=device))
model.to(device)
model.eval()

def encode_transaction(tx):
    # convert date from str to datetime
    dt = datetime.fromisoformat(tx.timestamp.replace('Z', '+00:00'))

    features = torch.tensor([
        tx.amount,
        dt.hour,
        dt.weekday(),
        1 if tx.category in {"gambling", "crypto"} else 0,
        len(tx.merchant_id),
        1 if tx.amount % 100 == 0 else 0,
    ], dtype=torch.float32)
    return features

def run_inference(tx):
    x = encode_transaction(tx).unsqueeze(0).to(device)  # [1, input_dim]
    with torch.no_grad():
        output = model(x)
    return float(output.item())

def batch_run_inference(transactions: list[Transaction]) -> list[float]:
    batch = torch.stack([encode_transaction(tx) for tx in transactions]).to(device)
    with torch.no_grad():
        outputs = model(batch)
    return outputs.squeeze().tolist()  # قائمة احتمالات