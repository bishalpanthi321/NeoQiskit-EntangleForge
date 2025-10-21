from setuptools import setup, find_packages

setup(
    name="neoqiskit-entangleforge",
    version="0.1.0",
    packages=find_packages(where="src"),
    package_dir={"": "src"},
    description="Dynamic Entanglement Cascade Quantum Algorithm",
    author="YourName",
    python_requires=">=3.8",
    install_requires=[
        "qiskit>=0.45.0",
        "qiskit-aer>=0.13.0",
        "numpy>=1.24.0",
        "torch>=2.0.0",  # For RL components
    ],
)