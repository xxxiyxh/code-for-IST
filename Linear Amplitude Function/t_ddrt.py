import pandas as pd
import numpy as np
import random

def read_csv_and_select_data_enhanced(file_path, epsilon, delta, epsilon_matrix_file, delta_matrix_file):
    df = pd.read_csv(file_path).copy()
    unique_partitions = df['partition'].unique()
    partition_probabilities = {partition: 1 / len(unique_partitions) for partition in unique_partitions}
    epsilon_matrix = pd.read_csv(epsilon_matrix_file, index_col=0)
    delta_matrix = pd.read_csv(delta_matrix_file, index_col=0)
    
    total_fail_count = df['result'].value_counts().get('fail', 0)
    fail_count = 0
    t = 0  # Record the loop count
    
    while fail_count < total_fail_count and t < len(df):
        selected_partition = random.choices(unique_partitions, weights=list(partition_probabilities.values()))[0]
        partition_df = df[df['partition'] == selected_partition]
        
        if not partition_df.empty:
            selected_row = partition_df.sample(n=1)
            row_index = selected_row.index
            selected_result = selected_row['result'].values[0]
            
            if selected_result == 'fail':
                fail_count += 1
                # Adjust probabilities based on epsilon_matrix
                for other_partition in unique_partitions:
                    if other_partition != selected_partition:
                        partition_probabilities[other_partition] -= epsilon_matrix.loc[selected_partition, other_partition]
                        partition_probabilities[selected_partition] += epsilon_matrix.loc[selected_partition, other_partition]
            else:
                # Adjust probabilities based on delta_matrix
                for other_partition in unique_partitions:
                    if other_partition != selected_partition:
                        partition_probabilities[other_partition] += delta_matrix.loc[selected_partition, other_partition]
                        partition_probabilities[selected_partition] -= delta_matrix.loc[selected_partition, other_partition]

            # Normalize probabilities
            total_probability = sum(partition_probabilities.values())
            partition_probabilities = {partition: prob / total_probability for partition, prob in partition_probabilities.items()}
            
            # Remove selected data from DataFrame
            df = df.drop(row_index)
        
        t += 1
    
    return t

epsilon = 0.02
delta = 0.02
epsilon_matrix_file = 'epsilon_matrix.csv'
delta_matrix_file = 'delta_matrix.csv'

num_iterations = 80
t_values = []

for _ in range(num_iterations):
    t = read_csv_and_select_data_enhanced('Linear Amplitude Function (part1).csv', epsilon, delta, epsilon_matrix_file, delta_matrix_file)
    t_values.append(t)

average_t = np.mean(t_values)

print("Average t Value:", average_t)
