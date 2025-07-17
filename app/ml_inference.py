import torch
from app.ml_model import FraudDetectionModel
from app.schemas import Transaction
from datetime import datetime
"""
This file loads a trained PyTorch model (`FraudDetectionModel`) and provides
functions to run inference on individual or batch transactions.
- Features used:
---------------
    1. Transaction amount
    2. Hour of transaction (from timestamp)
    3. Day of week (0=Monday)
    4. High-risk category flag (1 if 'gambling' or 'crypto', else 0)
    5. Length of merchant ID
    6. Round-number amount flag (1 if divisible by 100)  
Example Output:
---------------
- 0.91 → High probability of fraud
- 0.02 → Likely legitimate transaction
"""
# Automatically selects GPU (CUDA) if available, otherwise uses CPU.
device = torch.device("cuda" if torch.cuda.is_available() else "cpu")

# Loads the model architecture and pre-trained weights from `model.pth`.
model = FraudDetectionModel()
model.load_state_dict(torch.load("model.pth", map_location=device))
model.to(device)
# Sets the model to evaluation mode.
model.eval()

def encode_transaction(tx):
    # convert date from str to datetime
    dt = datetime.fromisoformat(tx.timestamp.replace('Z', '+00:00'))
    # Transforms a `Transaction` object into a 6 - dimensional input tensor
    features = torch.tensor([
        tx.amount,
        dt.hour,
        dt.weekday(),
        1 if tx.category in {"gambling", "crypto"} else 0,
        len(tx.merchant_id),
        1 if tx.amount % 100 == 0 else 0,
    ], dtype=torch.float32)
    return features

"""
############## run_inference(tx) ##############
- Runs fraud prediction on a **single transaction**.
- Returns probability (float between 0 and 1).
"""
def run_inference(tx):
    x = encode_transaction(tx).unsqueeze(0).to(device)  # [1, input_dim]
    with torch.no_grad():
        output = model(x)
    return float(output.item())

"""
############## batch_run_inference(transactions) ##############
- Runs predictions on a **batch of transactions**.
- Returns a list of probabilities.
"""
def batch_run_inference(transactions: list[Transaction]) -> list[float]:
    batch = torch.stack([encode_transaction(tx) for tx in transactions]).to(device)
    with torch.no_grad():
        outputs = model(batch)
    return outputs.squeeze().tolist()