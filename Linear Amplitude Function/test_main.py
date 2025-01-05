from amplitude import LinearAmplitudeFunction
from amplitude_defect2 import LinearAmplitudeFunction_defect
from qiskit.circuit import QuantumRegister, ClassicalRegister, QuantumCircuit
from qiskit.quantum_info import Statevector
from qiskit import Aer, execute
import math
import numpy as np
import csv

def result_oracle(pro1, pro2):
    abs_div = np.abs(pro1 - pro2)
    com = np.sum(abs_div)
    if com == 0: 
        return 'pass'
    else:
        return 'fail'

def generate_base_m_numbers(n, m):
    if n <= 0:
        return [[]]  # 返回一个包含空列表的列表

    if n == 1:
        return [[i] for i in range(m)]  # 生成 n=1 位的 m 进制数

    # 递归生成 n 位的 m 进制数
    smaller_numbers = generate_base_m_numbers(n - 1, m)
    numbers = []
    for digit in range(m):
        for smaller_number in smaller_numbers:
            numbers.append([digit] + smaller_number)

    return numbers


def distance_oracle(pro1, pro2, eps):
    abs_div = np.abs(pro1 - pro2)
    dis = 1 / 2 * np.sum(abs_div)
    if dis < eps:
        return 'pass'
    else:
        return 'fail'
    

def output_prob(counts, n):
    output_dic = counts.int_outcomes()
    psi_e = []
    for i in range(2**n):
        if i not in output_dic:
            psi_e.append(0)
        else:
            psi_e.append(output_dic[i]/counts.shots())
    psi_e = np.asarray(psi_e) / np.sum(psi_e)
    return psi_e


class BreakLoop(Exception):
    pass


def pureStateInput():
    # backend = Aer.get_backend('qasm_simulator')

    test_report = []
    n_list = np.arange(2, 4)  # [2, 3]

    # 测试

    initial_gates = [0, 1]

    backend = Aer.get_backend('qasm_simulator')

    domain = [0, 1]
    image = [0, 1]

    offsets = np.arange(-3, 3.1, 0.5)
    slops = np.arange(-3, 3.1, 0.5)

    try:    
        for n in n_list:
            initial_states = generate_base_m_numbers(n, len(initial_gates))
            for initial_state in initial_states:
                qc = QuantumCircuit(n + 1, 1)
                for index, val in enumerate(initial_state):
                    if initial_gates[val] == 1:
                        qc.x(index)
                    for slop in slops:
                        for offset in offsets:
                            qc_exp, qc_def = qc.copy(), qc.copy()
                            linear_exp = LinearAmplitudeFunction(n, slop, offset, domain, image)
                            linear_def = LinearAmplitudeFunction_defect(n, slop, offset, domain, image)
                            qc_exp.append(linear_exp, qc_exp.qubits)
                            qc_def.append(linear_def, qc_def.qubits)
                            qc_exp.measure(qc_exp.qubits[-1], qc_exp.clbits)
                            qc_def.measure(qc_def.qubits[-1], qc_def.clbits)
                            job_exp = execute(qc_exp, backend, shots=10000)
                            job_def = execute(qc_def, backend, shots=10000)
                            count_exp = job_exp.result().get_counts()
                            count_def = job_def.result().get_counts()
                            prob_exp = output_prob(count_exp, 1)
                            prob_def = output_prob(count_def, 1)
                            test_result = distance_oracle(prob_exp, prob_def, 2 * 1e-2)
                            temp = [n, initial_state, slop, offset, count_exp, count_def, test_result]
                            print(temp)
                            test_report.append(temp)
                            if len(test_report) > 5000:
                                raise BreakLoop
    except BreakLoop:
        pass  # 在这里不执行任何操作，只是用于捕获异常

    # 指定要保存的文件名
    file_name = "test_suites.csv"

    # 打开文件以进行写入，newline='' 用于确保在 Windows 上正确处理换行符
    with open(file_name, mode='w', newline='') as file:
        writer = csv.writer(file)

        # 写入表头（如果有的话）
        header = ['n', 'initial_state', 'slope', 'offset', 'oracle_prob', 'test_prob', 'result']
        writer.writerow(header)

        for data in test_report:
            # 写入数据
            writer.writerow(data)
    print('done!')

def mixedStateInput():
    """
    quantum registers: 5 * n + 1
        n: provide uniform probability, 
        2 * n: are input to each versions |0\rangle|i\rangle. And there are 2 versions
        1: perform the swap test
    classical registers:  n + 1
        n: store the bit information to control quantum input
        1: store the result of swap test

        qn: -------------------   control input
        qn: -------------------   |x\rangle
        q1: -------------------   |0\rangle
        qn: -------------------   |x\rangle
        q1: -------------------   |0\rangle
        q1: -------------------   ancilla qubit of swap test
        cn: -------------------   control clbits
        c1: -------------------   swap test result
    """
        
    test_report = []
    n_list = np.arange(1, 6)  # [1, 5]
    # 测试

    backend = Aer.get_backend('qasm_simulator')

    domain = [0, 1]
    image = [0, 1]
    offsets = np.arange(-4, 4.1, 0.5)
    slops = np.arange(-4, 4.1, 0.5)

    try:    
        for n in n_list:
            qc_raw = QuantumCircuit(3 * n + 3, n + 1)
            qc_raw.h(qc_raw.qubits[:n])
            qc_raw.measure(qc_raw.qubits[:n], qc_raw.clbits[:n])
            for index in range(n, 2 * n):
                qc_raw.x(qc_raw.qubits[index]).c_if(qc_raw.clbits[index - n], 1)
                qc_raw.x(qc_raw.qubits[index + n + 1]).c_if(qc_raw.clbits[index - n], 1)

                for slop in slops:
                    for offset in offsets:
                        qc = qc_raw.copy()
                        linear_exp = LinearAmplitudeFunction(n, slop, offset, domain, image)
                        linear_def = LinearAmplitudeFunction_defect(n, slop, offset, domain, image)
                        qc.compose(linear_exp, qubits=np.arange(n, 2 * n + 1), inplace=True)
                        qc.compose(linear_def, qubits=np.arange(2 * n + 1, 3 * n + 2), inplace=True)
                        # swap test:
                        qc.h(qc.qubits[-1])
                        for index in range(n, 2 * n + 1):
                            qc.cswap(-1, index, index + n + 1)
                        qc.h(qc.qubits[-1])
                        
                        qc.measure(qc.qubits[-1], qc.clbits[-1])
                        backend = Aer.get_backend('qasm_simulator')
                        job_def = execute(qc, backend, shots=100)
                        count_list = job_def.result().get_counts()
                        
                        test_bit = set([clbit[0] for clbit in list(count_list.keys())])
                        test_result = 'pass' if len(test_bit) == 1 and '0' in test_bit else 'fail'
                        temp = [n, slop, offset, test_result]
                        print(temp)
                        test_report.append(temp)
                        if len(test_report) > 2500:
                            raise BreakLoop
    except BreakLoop:
        pass  # 在这里不执行任何操作，只是用于捕获异常

    # 指定要保存的文件名
    file_name = "test_suites.csv"

    # 打开文件以进行写入，newline='' 用于确保在 Windows 上正确处理换行符
    with open(file_name, mode='w', newline='') as file:
        writer = csv.writer(file)

        # 写入表头（如果有的话）
        header = ['n', 'slop', 'offset', 'test_result']
        writer.writerow(header)

        for data in test_report:
            # 写入数据
            writer.writerow(data)
    print('done!')

if __name__ == '__main__':
    pureStateInput()
