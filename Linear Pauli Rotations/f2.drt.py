import pandas as pd
import numpy as np
import random

def detect_fail_intervals_with_drt(file_path, epsilon, delta):
    df = pd.read_csv(file_path).copy()
    unique_partitions = df['partition'].unique()
    partition_probabilities = {partition: 1 / len(unique_partitions) for partition in unique_partitions}
    
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
            
            # Adjust probabilities
            partition_probabilities[selected_partition] = max(min(partition_probabilities[selected_partition] - delta, 1), 0.00000001)
            
            # Normalize probabilities
            total = sum(partition_probabilities.values())
            partition_probabilities = {partition: prob / total for partition, prob in partition_probabilities.items()}
            
            df = df.drop(row_index)
        
        t += 1

    return 0  # Return 0 if less than 2 fails are found

# Example usage
epsilon = 0.07
delta = 0.07
num_iterations = 40
interval_counts = []

for _ in range(num_iterations):
    interval = detect_fail_intervals_with_drt('filtered_data.csv', epsilon, delta)
    interval_counts.append(interval)
print(interval_counts)

average_interval = np.mean(interval_counts)

print("Average Interval Count Between First and Second Fail:", average_interval)
