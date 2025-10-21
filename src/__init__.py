"""NeoQiskit-EntangleForge: Dynamic Entanglement Cascade Framework."""

from .dec_algorithm import DynamicEntanglementCascade
from .forge_circuit import EntanglementForgeCircuit

__version__ = "0.1.0"
__all__ = ["DynamicEntanglementCascade", "EntanglementForgeCircuit"]