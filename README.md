# Q-DDRT
## Description
This is a repository for the paper '_Dynamic Random Testing of Multi-subroutine Quantum Programs: A Distance Based Strategy_'.
More details will be updated if the manuscript is possibly accepted for publication.
## Environment

First create a conda environment, such as named `env`.

```bash
conda create -n env python=3.11.7
```

Then, activate the environment and install the packages in `requirements.txt`.

```bash
conda activate env
pip install -r requirements.txt
```

Here are the requirements:

```bash
numpy==2.2.3
pandas==2.2.3
qiskit==2.0.0
scipy==1.15.2
tqdm==4.66.1
matplotlib==3.10.1
```

## Codes
### Object Programs
The files `Quadratic Form`, `LinearPauliRotations`, `LinearAmplitudeFunction`,  `IntegerComparator` and `WeightedAdder` correspond to 5 employed quantum programs. In each file,

- `aaa.py`: The bug-free version downloaded from `qiskit.circuit.library` ([link](https://github.com/Qiskit/qiskit/tree/stable/1.2/qiskit/circuit/library)), where `aaa` refers to the name of the object program (i.e., `quadratic`, `linear`, `amplitude`, `comparator` and `weightedAdder`).

- `aaa_defectbbb.py`: The buggy version mutating from the raw one. bbb indicates the name of the buggy version. For example, `weightedAdder_defect2.py` is the v2 of the object WA.

- `depth.py`: This file is used to collect basic information (# Qubits, # Gates and Depths) of the quantum circuit corresponding to each program version. The relevant results are displayed in Table 1 of the manuscript.

### Implementation
At first, use `cd` to locate at the path of this repository.

- **Test suite generation:** Implement `test_main.py` to generate test suites and then save the data table.

- **Partition:** Implement `(partition)aaa.py` to obtain the segmented data.

- **Distance Calculation:** Run `distance_tra.py` and `distance_qua.py` to obtain the classical distance and quantum distance separately. Then, execute `total_distance.py` to compute the total distance and save the results in a CSV file stored in matrix form.

- **Metrics Calculation:** Run `ccc_ddd.py` to obtain various metrics, such as APFD, $F_2$ and $t_{12}$, where `ccc` refers to the name of metrics (i.e., `APFD`, `f2` and `t12`), `ddd` refers to the name of testing strategies (i.e., `ddrt`, `drt`， `rpt` and `rt`).

### Data Processing

Run `plotxxx.py` to generate the corresponding figures.
