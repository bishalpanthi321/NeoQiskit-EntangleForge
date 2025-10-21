"""Quantum circuit builder for entanglement forging."""

from qiskit import QuantumCircuit
import numpy as np

class EntanglementForgeCircuit:
    def __init__(self, num_qubits: int):
        self.num_qubits = num_qubits

    def build_base_circuit(self) -> QuantumCircuit:
        """Build initial forge circuit with H-gates and CNOTs."""
        qc = QuantumCircuit(self.num_qubits)
        for i in range(self.num_qubits):
            qc.h(i)  # Superposition base
        for i in range(self.num_qubits - 1):
            qc.cx(i, i + 1)  # Initial entanglement chain
        return qc

    def add_forge_layer(self, circuit: QuantumCircuit, layer_gates: list) -> QuantumCircuit:
        """Add a layer of forged gates (e.g., RY, CZ)."""
        for gate, q1, q2 in layer_gates:
            if gate == 'RY':
                circuit.ry(np.pi / 4, q1)
            elif gate == 'CZ':
                circuit.cz(q1, q2)
        return circuit