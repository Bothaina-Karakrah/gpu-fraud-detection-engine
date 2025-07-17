# save_dummy_model.py
import torch
from app.ml_model import FraudDetectionModel

model = FraudDetectionModel()
torch.save(model.state_dict(), "model.pth")

print("✅ Dummy model saved as model.pth")