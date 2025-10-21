"""Demo: Use DEC for graph partitioning on a 4-node graph."""

from src.dec_algorithm import DynamicEntanglementCascade
import numpy as np

# Mock graph adjacency as initial state (Hamiltonian encoding)
initial_state = np.random.rand(16)  # 4 qubits: 2^4 states
initial_state /= np.linalg.norm(initial_state)

dec = DynamicEntanglementCascade(num_qubits=4, iterations=5)
final_circuit = dec.cascade_entangle(initial_state)

# Simulate and extract partition (mock measurement)
from qiskit_aer import AerSimulator
sim = AerSimulator()
job = sim.run(final_circuit, shots=1024)
result = job.result().get_counts()
best_partition = max(result, key=result.get)  # e.g., '0101' -> cut size calc

print(f"Optimal partition state: {best_partition}")
print(f"Counts: {result}")
# In full impl, compute cut value: sum over edges crossing partition