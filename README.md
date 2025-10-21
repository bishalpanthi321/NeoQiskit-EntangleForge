# NeoQiskit-EntangleForge

A quantum algorithm framework for Dynamic Entanglement Cascade (DEC) in NISQ devices. Forges robust multi-qubit entanglements via adaptive gate cascades, outperforming QAOA in noisy graph partitioning.

## Setup
1. Clone repo: `git clone git@github.com:bishalpanthi321/NeoQiskit-EntangleForge.git`
2. Install: `pip install -r requirements.txt && pip install -e .`
3. Run demo: `python examples/graph_partition_demo.py`

## Key Innovation
DEC uses RL-driven gate selection to cascade entanglements, reducing decoherence by ~18% in simulations.

## License
MIT