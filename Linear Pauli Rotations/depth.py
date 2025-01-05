from qiskit import QuantumCircuit
from linear_defect import LinearPauliRotations_defect

def fully_decompose(qc):
    while True:
        decomposed_qc = qc.decompose()
        if decomposed_qc == qc:
            break
        qc = decomposed_qc
    return qc

num_state_qubits = 6
slope = 1.5
offset = 0.5
basis = "Y"

linear_rotation_circuit = LinearPauliRotations_defect(
    num_state_qubits=num_state_qubits,
    slope=slope,
    offset=offset,
    basis=basis
)

print("Original Circuit:")
print(linear_rotation_circuit)

decomposed_circuit = fully_decompose(linear_rotation_circuit)

print("\nDecomposed Circuit:")
print(decomposed_circuit)

depth = decomposed_circuit.depth()
gate_counts = decomposed_circuit.count_ops()

print(f"\nDecomposed Circuit Depth: {depth}")
print(f"Decomposed Circuit Gate Counts: {gate_counts}")
