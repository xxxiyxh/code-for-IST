from weightedAdder import WeightedAdder
from weightedAdder_defect2 import WeightedAdder_defect
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
    
def distance_oracle(pro1, pro2, eps):
    abs_div = np.abs(pro1 - pro2)
    dis = 1 / 2 * np.sum(abs_div)
    if dis < eps:
        return 'pass'
    else:
        return 'fail'

def generate_base_m_numbers(n, m):
    if n <= 0:
        return [[]]

    if n == 1:
        return [[i] for i in range(m)]

    smaller_numbers = generate_base_m_numbers(n - 1, m)
    numbers = []
    for digit in range(m):
        for smaller_number in smaller_numbers:
            numbers.append([digit] + smaller_number)

    return numbers


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
    test_report = []
    n_list = np.arange(1, 5)  # [1, 4]

    weights_list = [0, 1, 2, 3]
    initial_gates = [0, 1]

    backend = Aer.get_backend('qasm_simulator')

    try:    
        for n in n_list:
            weight_list = generate_base_m_numbers(n, len(weights_list))
            for weight in weight_list:
                if np.sum(weight) == 0:
                    s = 1
                else:
                    s = 1 + math.floor(math.log2(np.sum(weight)))
                initial_states = generate_base_m_numbers(n, len(initial_gates))
                for initial_state in initial_states:
                    adder_exp = WeightedAdder(n, weight)
                    adder_def = WeightedAdder_defect(n, weight)
                    qc_initial = QuantumCircuit(adder_exp.num_qubits, s)
                    qc = qc_initial.copy()

                    for index, val in enumerate(initial_state):
                        if initial_gates[val] == 1:
                            qc.x(index)
                        
                    qc_exp, qc_def = qc.copy(), qc.copy()
                    qc_exp.append(adder_exp, qc_exp.qubits)
                    qc_def.append(adder_def, qc_def.qubits)
                    qc_exp.measure(qc_exp.qubits[n: n + s], qc_exp.clbits)
                    qc_def.measure(qc_def.qubits[n: n + s], qc_def.clbits)
                    job_exp = execute(qc_exp, backend, shots=10)
                    job_def = execute(qc_def, backend, shots=10)
                    count_exp = job_exp.result().get_counts()
                    count_def = job_def.result().get_counts()
                    prob_exp = output_prob(count_exp, s)
                    prob_def = output_prob(count_def, s)
                    test_result = result_oracle(prob_exp, prob_def)
                    temp = [n, initial_state, weight, count_exp, count_def, test_result]
                    print(temp)
                    test_report.append(temp)
                    if len(test_report) > 2000:
                        raise BreakLoop
    except BreakLoop:
        pass

    file_name = "test_suites.csv"

    with open(file_name, mode='w', newline='') as file:
        writer = csv.writer(file)

        header = ['n', 'initial_state', 'weight', 'oracle_prob', 'test_prob', 'result']
        writer.writerow(header)

        for data in test_report:
            writer.writerow(data)
    print('done!') 

def mixedStateInput():
    test_report = []
    n_list = np.arange(1, 5)
    weights_list = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    backend = Aer.get_backend('qasm_simulator')

    try:    
        for n in n_list:
            weight_list = generate_base_m_numbers(n, len(weights_list))
            for weight in weight_list:
                if np.sum(weight) == 0:
                    s = 1
                else:
                    s = 1 + math.floor(math.log2(np.sum(weight)))
                num_carry = s - 1
                num_control = int(s > 2)

                qc_raw = QuantumCircuit(2 * n + s + num_carry + num_control, n + s)
                qc_raw.h(qc_raw.qubits[:n])
                qc_raw.measure(qc_raw.qubits[:n], qc_raw.clbits[:n])
                qc_exp, qc_def = qc_raw.copy(), qc_raw.copy()  
                for index in range(n, 2 * n):
                    qc_exp.x(qc_exp.qubits[index]).c_if(qc_exp.clbits[index - n], 1)
                    qc_def.x(qc_def.qubits[index]).c_if(qc_def.clbits[index - n], 1)
                
                adder_exp = WeightedAdder(n, weight)
                adder_def = WeightedAdder_defect(n, weight)
                qc_exp.compose(adder_exp, qubits=np.arange(n, 2 * n + s + num_carry + num_control), inplace=True)
                qc_def.compose(adder_def, qubits=np.arange(n, 2 * n + s + num_carry + num_control), inplace=True)                

                qc_exp.measure(qc_exp.qubits[n: 2 * n + s], qc_exp.clbits)
                qc_def.measure(qc_def.qubits[n: 2 * n + s], qc_def.clbits)
                backend = Aer.get_backend('qasm_simulator')
                job_exp = execute(qc_exp, backend, shots=10000)
                job_def = execute(qc_def, backend, shots=10000)
                count_exp = job_exp.result().get_counts()
                count_def = job_def.result().get_counts()
                prob_exp = output_prob(count_exp, n + 1)
                prob_def = output_prob(count_def, n + 1)
                test_result = distance_oracle(prob_exp, prob_def, 3e-2)
                temp = [n, weight, prob_exp.tolist(), prob_def.tolist(), test_result]
                print(temp)
                test_report.append(temp)

                if len(test_report) > 800:
                    raise BreakLoop
    except BreakLoop:
        pass

    file_name = "test_suites.csv"

    with open(file_name, mode='w', newline='') as file:
        writer = csv.writer(file)

        header = ['n', 'weight', 'oracle_prob', 'test_prob', 'result']
        writer.writerow(header)

        for data in test_report:
            writer.writerow(data)
    print('done!')

if __name__ == '__main__':
    pureStateInput()
