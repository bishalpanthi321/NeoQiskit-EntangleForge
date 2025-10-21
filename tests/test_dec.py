"""Unit tests for DEC algorithm."""

import unittest
import numpy as np
from src.dec_algorithm import DynamicEntanglementCascade

class TestDEC(unittest.TestCase):
    def setUp(self):
        self.dec = DynamicEntanglementCascade(num_qubits=3, iterations=2)
        self.state = np.array([1, 0, 0, 0, 0, 0, 0, 0])  # |000> mock

    def test_cascade_entangle(self):
        circuit = self.dec.cascade_entangle(self.state)
        self.assertIsNotNone(circuit)
        self.assertEqual(circuit.num_qubits, 3)

    def test_simulate_step(self):
        from qiskit import QuantumCircuit
        qc = QuantumCircuit(3)
        new_state = self.dec.simulate_step(qc, self.state)
        self.assertEqual(len(new_state), len(self.state))

if __name__ == '__main__':
    unittest.main()