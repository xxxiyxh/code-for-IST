import pandas as pd
import numpy as np
import random

def detect_fail_intervals_with_ddrt(file_path, epsilon, delta, epsilon_matrix_file, delta_matrix_file):
    df = pd.read_csv(file_path).copy()
    unique_partitions = df['partition'].unique()
    partition_probabilities = {partition: 1 / len(unique_partitions) for partition in unique_partitions}
    epsilon_matrix = pd.read_csv(epsilon_matrix_file, index_col=0)
    delta_matrix = pd.read_csv(delta_matrix_file, index_col=0)
    
    fail_count = 0
    t = 0
    first_fail_index = -1

    while len(df) > 0 and fail_count < 2:
        selected_partition = random.choices(list(unique_partitions), weights=list(partition_probabilities.values()), k=1)[0]
        partition_df = df[df['partition'] == selected_partition]
        
        if not partition_df.empty:
            selected_row = partition_df.sample(n=1)
            row_index = selected_row.index
            selected_result = selected_row['result'].values[0]
            
            if selected_result == 'fail':
                fail_count += 1
                if fail_count == 1:
                    first_fail_index = t
                elif fail_count == 2:
                    return t - first_fail_index
            
            # Adjust probabilities dynamically
            for other_partition in unique_partitions:
                if other_partition != selected_partition:
                    if selected_result == 'fail':
                        partition_probabilities[other_partition] -= epsilon_matrix.loc[selected_partition, other_partition]
                    else:
                        partition_probabilities[other_partition] += delta_matrix.loc[selected_partition, other_partition]
            
            # Normalize probabilities
            total = sum(partition_probabilities.values())
            partition_probabilities = {partition: prob / total for partition, prob in partition_probabilities.items()}
            
            df = df.drop(row_index)
        
        t += 1

    return 0  # Return 0 if less than 2 fails are found

# Example usage
epsilon = 0.02
delta = 0.02
epsilon_matrix_file = 'epsilon_matrix.csv'
delta_matrix_file = 'delta_matrix.csv'
num_iterations = 80
interval_counts = []

for _ in range(num_iterations):
    interval = detect_fail_intervals_with_ddrt(file_path='Linear Pauli Rotations (part1).csv', epsilon=epsilon, delta=delta, epsilon_matrix_file=epsilon_matrix_file, delta_matrix_file=delta_matrix_file)
    interval_counts.append(interval)
print(interval_counts)

average_interval = np.mean(interval_counts)
print("Average Interval Count Between First and Second Fail:", average_interval)
