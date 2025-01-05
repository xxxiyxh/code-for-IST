from qiskit.circuit import QuantumRegister, QuantumCircuit, ParameterVector
from qiskit.quantum_info import Statevector
from qiskit.circuit.library import RYGate
from qiskit import Aer, execute

from scipy.special import kl_div

import math
import numpy as np
import csv
import time
from tqdm import tqdm

from qiskit.circuit.library import IntegerComparator
from comparator_defect import IntegerComparator_defect

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

def Oracle_WOODM(expNum, results):
    resultSet = list(set(results))
    if len(resultSet) > 1 or resultSet[0] != expNum:
        return 'fail'
    else:
        return 'pass'

def Oracle_OPODM(expProbs, resProbs, tolerErr):
    arrayExp = np.array(expProbs)
    arrayRes = np.array(resProbs)
    kl_diver = kl_div(arrayExp, arrayRes).sum()
    if kl_diver < tolerErr:
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

def PurePS_WOODM(number, L, sign):
    if sign == True:
        return int(number >= L)
    else:
        return int(number < L)

def PurePS_OPODM(number, L, sign):
    Prob = [0, 0]
    if sign == True:
        Prob[int(number >= L)] = 1
    else:
        Prob[int(number < L)] = 1
    return Prob

class BreakLoop(Exception):
    pass

def PSTC_WOODM():
    initial_gates = [0, 1]
    n_list = range(1, 5)
    L_list = np.arange(-10, 10.1, 1)
    sign_list =  [True, False]
    shotTimes = 20
    test_report = []
    try:
        for n in n_list:            
            initial_states = generate_base_m_numbers(n, len(initial_gates))
            test_cases = 0
            total_fails = 0
            
            for L in L_list:
                for sign in sign_list:
                    fails = 0
                    for initial_state in initial_states:
                        number = int(''.join(map(str, initial_state)), 2)
                        qc_initial = QuantumCircuit(2 * n, n)
                        initial_state = initial_state[::-1]
                        for index, val in enumerate(initial_state):
                            if initial_gates[val] == 1:
                                qc_initial.x(index)
                                   
                        qc = qc_initial.copy()
                        qc_test = IntegerComparator_defect(n, L, geq=sign)
                        qc.append(qc_test, qc.qubits)
                        qc.measure(qc.qubits[n:],qc.clbits[:])
                        job = execute(qc, backend=Aer.get_backend('qasm_simulator'), shots=shotTimes, memory=True)
                        result = job.result().get_memory()
                        
                        resultDec = [int(bit, 2) for bit in result]
                        
                        expRes = PurePS_WOODM(number, L, sign)     
                        test_result = Oracle_WOODM(expRes, resultDec)
                        
                        temp = [n, initial_state, L, sign, test_result]
                        print(temp)
                        test_report.append(temp)
                        if len(test_report) > 5000:
                            raise BreakLoop
    except BreakLoop:
        pass

    file_name = "test_suites_woo.csv"

    with open(file_name, mode='w', newline='') as file:
        writer = csv.writer(file)
        header = ['n', 'initial_vector', 'L', 'geq', 'test_result']
        writer.writerow(header)
        for data in test_report:
            writer.writerow(data)

def PSTC_OPODM():
    tolerErr = 1e-3
    initial_gates = [0, 1]
    n_list = range(1, 5)
    L_list = np.arange(-5, 5.1, 1)
    sign_list =  [True, False]
    shotTimes = 10000
    test_report = []
    
    try:
        for n in n_list:            
            initial_states = generate_base_m_numbers(n, len(initial_gates))
            test_cases = 0
            total_fails = 0
            
            for L in L_list:
                for sign in sign_list:
                    fails = 0
                    for initial_state in initial_states:
                        number = int(''.join(map(str, initial_state)), 2)
                        qc_initial = QuantumCircuit(2 * n, n)
                        initial_state = initial_state[::-1]
                        for index, val in enumerate(initial_state):
                            if initial_gates[val] == 1:
                                qc_initial.x(index)
                                      

                        qc = qc_initial.copy()
                        qc_test = IntegerComparator_defect(n, L, geq=sign)
                        qc.append(qc_test, qc.qubits)
                        qc.measure(qc.qubits[n:],qc.clbits[:])
                        
                        job = execute(qc, backend=Aer.get_backend('qasm_simulator'), shots=shotTimes)
                        count = job.result().get_counts()
                    
                        expProbs = PurePS_OPODM(number, L, sign)
                        resProbs = output_prob(count, 1)
                        test_result = Oracle_OPODM(expProbs, resProbs, tolerErr)
                    
                        temp = [n, initial_state, L, sign, test_result]
                        print(temp)
                        test_report.append(temp)
                        if len(test_report) > 5000:
                            raise BreakLoop
    except BreakLoop:
        pass

    file_name = "test_suites_opo.csv"

    with open(file_name, mode='w', newline='') as file:
        writer = csv.writer(file)
        header = ['n', 'initial_vector', 'L', 'geq', 'test_result']
        writer.writerow(header)
        for data in test_report:
            writer.writerow(data)
    print('done!')

if __name__ == '__main__':
    PSTC_WOODM()
