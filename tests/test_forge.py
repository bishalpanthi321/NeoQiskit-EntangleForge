"""Unit tests for EntanglementForgeCircuit."""

import unittest
from src.forge_circuit import EntanglementForgeCircuit

class TestForgeCircuit(unittest.TestCase):
    def setUp(self):
        self.forge = EntanglementForgeCircuit(num_qubits=4)

    def test_build_base_circuit(self):
        qc = self.forge.build_base_circuit()
        self.assertEqual(qc.num_qubits, 4)
        self.assertEqual(len(qc.data), 7)  # 4 H + 3 CX

    def test_add_forge_layer(self):
        from qiskit import QuantumCircuit
        qc = QuantumCircuit(4)
        layer = [('RY', 0, None), ('CZ', 1, 2)]
        new_qc = self.forge.add_forge_layer(qc, layer)
        self.assertGreater(len(new_qc.data), len(qc.data))

if __name__ == '__main__':
    unittest.main()