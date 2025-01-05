from qiskit import QuantumCircuit
from amplitude_defect4 import LinearAmplitudeFunction_defect

def fully_decompose(qc):
    """
    完全分解量子电路，直到无法继续分解。
    Args:
        qc (QuantumCircuit): 待分解的量子电路
    Returns:
        QuantumCircuit: 完全分解后的量子电路
    """
    while True:
        decomposed_qc = qc.decompose()  # 分解一次
        if decomposed_qc == qc:  # 若分解前后相同，退出循环
            break
        qc = decomposed_qc  # 更新电路
    return qc

def analyze_circuit(num_state_qubits, slope, offset, domain, image, rescaling_factor, breakpoints):
    """
    分析指定参数的线性振幅函数电路。
    Args:
        num_state_qubits: 量子比特数量
        slope: 线性函数的斜率（或斜率列表）
        offset: 线性函数的偏移量（或偏移量列表）
        domain: 函数的定义域
        image: 函数的值域
        rescaling_factor: 缩放因子，用于调整泰勒展开的精度
        breakpoints: 若为分段线性函数，其分段点列表
    Returns:
        dict: 包括原始电路、分解电路、深度和门数量的结果
    """
    # 初始化原始电路
    linear_amplitude_circuit = LinearAmplitudeFunction_defect(
        num_state_qubits=num_state_qubits,
        slope=slope,
        offset=offset,
        domain=domain,
        image=image,
        rescaling_factor=rescaling_factor,
        breakpoints=breakpoints,
    )

    # 分解电路
    decomposed_circuit = fully_decompose(linear_amplitude_circuit)

    # 统计分解后电路的深度和门数量
    depth = decomposed_circuit.depth()
    gate_counts = decomposed_circuit.count_ops()

    return {
        "num_state_qubits": num_state_qubits,
        "original_circuit": linear_amplitude_circuit,
        "decomposed_circuit": decomposed_circuit,
        "depth": depth,
        "gate_counts": gate_counts,
    }

# 分析指定的测试参数
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

# 打印结果
print("Results for LinearAmplitudeFunction:")
print("Original Circuit:")
print(result["original_circuit"])
print("\nDecomposed Circuit:")
print(result["decomposed_circuit"])
print(f"\nDecomposed Circuit Depth: {result['depth']}")
print(f"Decomposed Circuit Gate Counts: {result['gate_counts']}")
