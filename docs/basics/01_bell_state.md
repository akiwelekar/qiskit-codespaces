# Bell State using Qiskit Aer

## Objective

This program demonstrates how to create one of the most fundamental quantum states—the **Bell State**. It introduces superposition, entanglement, and quantum measurement using Qiskit.

---

# Learning Outcomes

After completing this exercise, you should be able to:

- Create a quantum circuit with two qubits.
- Apply the Hadamard gate.
- Apply the Controlled-NOT gate.
- Perform measurements.
- Execute the circuit on the Aer simulator.
- Interpret measurement statistics.

---

# Quantum Concepts

## Superposition

A Hadamard gate transforms

|0⟩

into

(|0⟩ + |1⟩)/√2

allowing the qubit to exist in both states simultaneously.

---

## Entanglement

Applying a CNOT gate produces

(|00⟩ + |11⟩)/√2

This Bell state cannot be separated into two independent qubit states.

---

## Measurement

Measuring either qubit immediately determines the state of the other.

Expected measurement counts:

```
00 ≈ 50%
11 ≈ 50%
```

---

# Qiskit Features Used

| Component | Purpose |
|------------|---------|
| QuantumCircuit | Create the circuit |
| H Gate | Generate superposition |
| CX Gate | Create entanglement |
| measure() | Convert quantum information into classical bits |
| AerSimulator | Local simulation |
| result().get_counts() | Obtain measurement statistics |

---

# Program Flow

```
Create circuit
      │
      ▼
Apply H gate
      │
      ▼
Apply CNOT
      │
      ▼
Measure
      │
      ▼
Execute using Aer
      │
      ▼
Display results
```

---

# QSAF Mapping

This example illustrates the following reusable architectural components.

| QSAF Component | Present |
|----------------|---------|
| State Preparation | ✓ |
| Entanglement | ✓ |
| Measurement | ✓ |
| Classical Result Collection | ✓ |

Circuit primitives:

- Hadamard
- Controlled-NOT
- Measurement

---

# Computational Thinking

Classical equivalent:

- Produce two perfectly correlated random bits.

Quantum advantage:

- Correlation is produced naturally through entanglement rather than classical synchronization.

---

# Experiments

Try the following modifications.

## Experiment 1

Remove the Hadamard gate.

Question:

What measurements do you observe?

---

## Experiment 2

Remove the CNOT gate.

Question:

How does the probability distribution change?

---

## Experiment 3

Increase the number of shots to

```
10000
```

Observe how the frequencies converge toward theoretical probabilities.

---

## Experiment 4

Replace

```
H
```

with

```
X
```

Predict the outcome before executing.   

---

# Reflection

- Why is the Bell state impossible to describe as two independent qubits?
- Why do only two outcomes appear?
- What role does measurement play?

---

# References

- Qiskit Documentation
- Nielsen & Chuang, *Quantum Computation and Quantum Information*
- IBM Quantum Learning