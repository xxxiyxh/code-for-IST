# Integer Comparator

This repository contains the source code and related data for the QP Integer Comparator. The project includes various versions of the code with different defects implanted and tools for evaluating and testing the function's performance, particularly in the context of defect detection and measurement.

## Files and Their Functions

- `comparator.py`: This is the bug-free version of the code implementing the Linear Amplitude Function.
- `comparator_defect.py` to `comparator_defect4.py`: These are versions of the code with four different types of defects implanted, intended for testing and evaluation purposes.
- `test_main.py`: This script is used to test the defective versions of the code and generate an initial set of test cases.
- `apfd_ddrt.py`, `apfd_drt.py`, `apfd_rpt.py`, `apfd_rt.py`: These scripts calculate the APFD (Average Percentage of Fault Detection) values after applying four different testing strategies.
- `depth.py`: This script calculates the depth of the quantum circuit used in the testing.
- `distance_qua.py`: This script computes the quantum variable distances.
- `distance_tra.py`: This script computes the classical variable distances.
- `total_distance.py`: This script calculates the total distance by combining the quantum and classical variable distances.
- `f2_ddrt.py, t12_ddrt.py`: These scripts compute the f2_measure and t2_measure, respectively, for defect detection evaluation.
- `plots`: Various plotting scripts corresponding to different Research Questions (RQs) to visualize the results.

## Usage

1. To run the test cases:
   ```bash
   python test_main.py
2. To calculate the APFD values after applying a particular strategy：
   ```bash
   python apfd_ddrt.py
3. To compute the quantum circuit depth:
   ```bash
   python depth.py
4. For plotting the results of a specific RQ, run the corresponding plotting script.
