from qiskit import QuantumCircuit
from amplitude_defect4 import LinearAmplitudeFunction_defect

def fully_decompose(qc):

    while True:
        decomposed_qc = qc.decompose() 
        if decomposed_qc == qc:  
            break
        qc = decomposed_qc
    return qc

def analyze_circuit(num_state_qubits, slope, offset, domain, image, rescaling_factor, breakpoints):

  
    linear_amplitude_circuit = LinearAmplitudeFunction_defect(
        num_state_qubits=num_state_qubits,
        slope=slope,
        offset=offset,
        domain=domain,
        image=image,
        rescaling_factor=rescaling_factor,
        breakpoints=breakpoints,
    )


    decomposed_circuit = fully_decompose(linear_amplitude_circuit)


    depth = decomposed_circuit.depth()
    gate_counts = decomposed_circuit.count_ops()

    return {
        "num_state_qubits": num_state_qubits,
        "original_circuit": linear_amplitude_circuit,
        "decomposed_circuit": decomposed_circuit,
        "depth": depth,
        "gate_counts": gate_counts,
    }


num_state_qubits = 4
slope = 1.0
offset = 0.5
domain = (0, 1)
image = (0, 1)
rescaling_factor = 1.0
breakpoints = None

result = analyze_circuit(
    num_state_qubits=num_state_qubits,
    slope=slope,
    offset=offset,
    domain=domain,
    image=image,
    rescaling_factor=rescaling_factor,
    breakpoints=breakpoints,
)


print("Results for LinearAmplitudeFunction:")
print("Original Circuit:")
print(result["original_circuit"])
print("\nDecomposed Circuit:")
print(result["decomposed_circuit"])
print(f"\nDecomposed Circuit Depth: {result['depth']}")
print(f"Decomposed Circuit Gate Counts: {result['gate_counts']}")
