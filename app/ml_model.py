import torch
import torch.nn as nn
import torch.nn.functional as F
"""
FraudDetectionModel: Fully Connected Neural Network (Multilayer Perceptron - MLP)

Architecture:
-------------
Input Layer:       6 features (default input_dim=6)
Hidden Layer 1:    Linear(6 → 32) + ReLU
Hidden Layer 2:    Linear(32 → 16) + ReLU
Output Layer:      Linear(16 → 1) + Sigmoid

Forward Pass:
-------------
x → fc1 → ReLU → fc2 → ReLU → fc3 → Sigmoid → output ∈ [0, 1]

Activation Functions:
---------------------
1. ReLU(x)    = max(0, x)
2. Sigmoid(x) = 1 / (1 + exp(-x))

Usage:
------
- Output is a probability between 0 and 1
- Output > 0.5 → Class 1 → Fraudulent transaction
- Output ≤ 0.5 → Class 0 → Legitimate transaction
"""
class FraudDetectionModel(nn.Module):
    def __init__(self, input_dim=6):
        super().__init__()
        self.fc1 = nn.Linear(input_dim, 32)
        self.fc2 = nn.Linear(32, 16)
        self.fc3 = nn.Linear(16, 1)

    def forward(self, x):
        x = F.relu(self.fc1(x))
        x = F.relu(self.fc2(x))
        return torch.sigmoid(self.fc3(x))