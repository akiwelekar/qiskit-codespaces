"""
01_bell_state.py

Creates a Bell state and simulates it using Qiskit Aer.
"""

from qiskit import QuantumCircuit
from qiskit_aer import AerSimulator


def main():
    # Create a two-qubit quantum circuit
    qc = QuantumCircuit(2, 2)

    # Put qubit 0 into superposition
    qc.h(0)

    # Entangle qubit 1 with qubit 0
    qc.cx(0, 1)

    # Measure both qubits
    qc.measure([0, 1], [0, 1])

    print("Quantum Circuit")
    print("----------------")
    print(qc.draw())

    simulator = AerSimulator()

    job = simulator.run(qc, shots=1024)
    result = job.result()

    print("\nMeasurement Counts")
    print("------------------")
    print(result.get_counts())


if __name__ == "__main__":
    main()
