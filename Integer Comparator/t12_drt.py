import pandas as pd
import numpy as np
import random

def detect_fail_times_with_drt(file_path, epsilon, delta):
    df = pd.read_csv(file_path).copy()
    unique_partitions = df['partition'].unique()
    partition_probabilities = {partition: 1 / len(unique_partitions) for partition in unique_partitions}
    
    fail_count = 0
    t = 0
    first_fail_time = -1
    second_fail_time = -1

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
                    first_fail_time = t  # Record the time of the first failure
                elif fail_count == 2:
                    second_fail_time = t  # Record the time of the second failure
                    return (first_fail_time, second_fail_time)  # Return times of both failures
            
            # Adjust probabilities
            partition_probabilities[selected_partition] = max(min(partition_probabilities[selected_partition] - delta, 1), 0.00000001)
            
            # Normalize probabilities
            total = sum(partition_probabilities.values())
            partition_probabilities = {partition: prob / total for partition, prob in partition_probabilities.items()}
            
            df = df.drop(row_index)
        
        t += 1

    return (first_fail_time, second_fail_time)  # Return times, might still be -1 if fails are not found

# Example usage
epsilon = 0.05
delta = 0.05
num_iterations = 40
fail_times = []

for _ in range(num_iterations):
    times = detect_fail_times_with_drt('IC (part3).csv', epsilon, delta)
    fail_times.append(times)

# Separate the times for better analysis
first_fail_times = [time[0] for time in fail_times if time[0] != -1]
second_fail_times = [time[1] for time in fail_times if time[1] != -1]

# Calculate the averages
average_first_fail = np.mean(first_fail_times)
average_second_fail = np.mean(second_fail_times)

print("Average Time to First Fail:", average_first_fail)
print("Average Time to Second Fail:", average_second_fail)
print( average_second_fail - average_first_fail)