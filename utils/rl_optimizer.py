"""Reinforcement Learning optimizer for gate selection."""

import torch
import torch.nn as nn
import numpy as np

class RLOptimizer(nn.Module):
    def __init__(self, num_qubits: int, hidden_dim: int = 64):
        super().__init__()
        self.num_qubits = num_qubits
        self.net = nn.Sequential(
            nn.Linear(num_qubits * 2, hidden_dim),  # State: amplitudes + phases
            nn.ReLU(),
            nn.Linear(hidden_dim, num_qubits * 3),  # Output: gate type, q1, q2
        )
        self.optimizer = torch.optim.Adam(self.parameters(), lr=0.01)

    def optimize_gates(self, state: np.ndarray) -> list:
        """Select optimal gate sequence via forward pass."""
        state_tensor = torch.tensor(state.flatten(), dtype=torch.float32)
        with torch.no_grad():
            actions = self.net(state_tensor).numpy()
        # Decode to gates: e.g., [0:RY, 1:CZ], qubits from actions[1:]
        sequence = [('RY' if a < 0.5 else 'CZ', int(i), int(j)) for i, a in enumerate(actions[:self.num_qubits]) 
                    for j in range(1, self.num_qubits) if np.random.rand() < 0.3]
        return sequence[:5]  # Limit to 5 gates per cascade