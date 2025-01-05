from quadratic import QuadraticForm
from quadratic_defect import QuadraticForm_defect
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

 

if __name__ == '__main__':

    backend = Aer.get_backend('qasm_simulator')

    test_report = []
   
    min_value = -4
    max_value = 4
    A_list = []
    b_list = []
    n_list = np.arange(2, 4)  

    for n in n_list:
        temp = []
        for i in range(n * 5):
            random_matrix = np.random.randint(min_value, max_value + 1, size=(n, n))
            temp.append(random_matrix.tolist())
        A_list.append(temp)

    for n in n_list:
        temp = []
        for i in range(n * 5):
            random_matrix = np.random.randint(min_value, max_value + 1, size=(1, n))
            random_matrix = random_matrix.tolist()
            temp.append(random_matrix[0])
        b_list.append(temp)

    c_list = np.arange(-2, 3, 1)    

    class BreakLoop(Exception):
        pass

    try:    
        for m in range(2,3):           

            for n in n_list:
                initial_vectors = []
                for index in range(0, 2 ** n):
                    zero_list = (np.zeros(2 ** n)).tolist()
                    zero_list[index] = 1
                    initial_vectors.append(zero_list)
                    qc = QuantumCircuit(n + m)
                
                for initial_vector in initial_vectors:
                    desired_vector = Statevector(initial_vector)

                    qc.initialize(desired_vector, qc.qubits[:n])
                    for c in c_list:
                        for A in A_list[n - 2]:
                            for b in b_list[n - 2]:
                                qc_exp, qc_def = qc.copy(), qc.copy()
                                quad_exp = QuadraticForm(num_result_qubits=m, quadratic=A, linear=b, offset=c)
                                quad_def = QuadraticForm_defect(num_result_qubits=m, quadratic=A, linear=b, offset=c)
                                qc_exp.append(quad_exp, qc_exp.qubits)
                                qc_def.append(quad_def, qc_def.qubits)
                                qc_exp.measure_all()
                                qc_def.measure_all()
                                job_exp = execute(qc_exp, backend, shots=10)
                                job_def = execute(qc_def, backend, shots=10)
                                count_exp = job_exp.result().get_counts()
                                count_def = job_def.result().get_counts()
                                prob_exp = output_prob(count_exp, m + n)
                                prob_def = output_prob(count_def, m + n)
                                test_result = result_oracle(prob_exp, prob_def)
                                temp = [n, m, initial_vector, A, b, c, test_result]
                                print(temp)
                                test_report.append(temp)
                                if len(test_report) > 1000:
                                    raise BreakLoop
    except BreakLoop:
        pass  

    file_name = "test_suites.csv"

    with open(file_name, mode='w', newline='') as file:
        writer = csv.writer(file)

        header = ['n','m','initial_state','A','b','c', 'result']
        writer.writerow(header)

        for data in test_report:
            writer.writerow(data)
    print('done!')
