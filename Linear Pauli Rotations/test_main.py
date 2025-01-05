from linear import LinearPauliRotations
from linear_defect import LinearPauliRotations_defect
from qiskit.circuit import QuantumRegister, QuantumCircuit
from qiskit.quantum_info import Statevector
from qiskit import Aer, execute
import math
import numpy as np
import csv

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
    backend = Aer.get_backend('qasm_simulator')
    test_report = []

    n_list = range(1, 4)
    slop_list = np.arange(0, 5.1, 0.5)
    offset_list = np.arange(-math.pi/2, math.pi/2 + 1e-9, math.pi/10)
    basis_list = ['X', 'Y', 'Z']
    try:
        for n in n_list: # range(1, 4)
            initial_vectors = []

            for index in range(0, 2 ** n):
                zero_list = (np.zeros(2 ** n)).tolist()
                zero_list[index] = 1
                initial_vectors.append(zero_list)

            for initial_vector in initial_vectors:
                desired_vector = Statevector([1, 0]).tensor(Statevector(initial_vector))
                qc = QuantumCircuit(n + 1)
                qc.initialize(desired_vector, qc.qubits)
                for slop in slop_list: # (0, 10, 0.5)
                    for offset in offset_list: # range(-math.pi/2, math.pi/2 + 1e-9, math.pi/10)
                        for basis in basis_list:
                            qc_exp, qc_def = qc.copy(), qc.copy()
                            linear_exp = LinearPauliRotations(n, slop, offset, basis)
                            linear_def = LinearPauliRotations_defect(n, slop, offset, basis)
                            qc_exp.append(linear_exp, qc_exp.qubits)
                            qc_def.append(linear_def, qc_def.qubits)
                            qc_exp.measure_all()
                            qc_def.measure_all()
                            job_exp = execute(qc_exp, backend, shots=10000)
                            job_def = execute(qc_def, backend, shots=10000)
                            count_exp = job_exp.result().get_counts()
                            count_def = job_def.result().get_counts()
                            prob_exp = output_prob(count_exp, n + 1)
                            prob_def = output_prob(count_def, n + 1)
                            test_result = distance_oracle(prob_exp, prob_def, 1e-2)
                            temp = [n, initial_vector, slop, offset, basis, prob_exp.tolist(), prob_def.tolist(), test_result]
                            print(temp)
                            test_report.append(temp)

    except BreakLoop:
        pass  
   
    file_name = "test_suites.csv"

  
    with open(file_name, mode='w', newline='') as file:
        writer = csv.writer(file)

       
        header = ['n','initial_state','slop','offset','basis','oracle_prob','test_prob','result']
        writer.writerow(header)

        for data in test_report:
          
            writer.writerow(data)
    print('done!')

def mixedStateInput():
    """
    quantum registers: 
        n: provide uniform probability, 
        2 * n: are input to each versions |0\rangle|i\rangle. And there are 2 versions
        1: perform the swap test
    classical registers:  n + 1
        n: store the bit information to control quantum input
        1: store the result of swap test

        qn: -------------------   control input
        qn: -------------------   |i\rangle
        qn: -------------------   |0\rangle
        qn: -------------------   |j\rangle
        qn: -------------------   |0\rangle
        q1: -------------------   ancilla qubit of swap test
        cn: -------------------   control clbits
        c1: -------------------   swap test result
    """
    backend = Aer.get_backend('qasm_simulator')
    test_report = []

    n_list = range(1, 6)
    slop_list = np.arange(0, 5.1, 1)
    offset_list = np.arange(-math.pi/2, math.pi/2 + 1e-9, math.pi/5)
    basis_list = ['X', 'Y', 'Z']
    try:
        for n in n_list: # range(1, 4)
            qc_raw = QuantumCircuit(3 * n + 3, n + 1)
            qc_raw.h(qc_raw.qubits[:n])
            qc_raw.measure(qc_raw.qubits[:n], qc_raw.clbits[:n])
            for index in range(n, 2 * n):
                qc_raw.x(qc_raw.qubits[index]).c_if(qc_raw.clbits[index - n], 1)
                qc_raw.x(qc_raw.qubits[index + n + 1]).c_if(qc_raw.clbits[index - n], 1)
                for slop in slop_list:
                    for offset in offset_list:
                        for basis in basis_list:
                            qc = qc_raw.copy()
                            linear_exp = LinearPauliRotations(n, slop, offset, basis)
                            linear_def = LinearPauliRotations_defect(n, slop, offset, basis)
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
                            temp = [n, slop, offset, basis, test_result]
                            print(temp)
                            test_report.append(temp)
                            if len(test_report) > 1500:
                                raise BreakLoop

    except BreakLoop:
        pass  

    file_name = "test_suites.csv"


    with open(file_name, mode='w', newline='') as file:
        writer = csv.writer(file)

      
        header = ['n', 'slop','offset','basis', 'result']
        writer.writerow(header)

        for data in test_report:
         
            writer.writerow(data)
    print('done!')

if __name__ == '__main__':
    mixedStateInput()


 
