import pandas as pd
import numpy as np
import random

def read_csv_and_detect_fail_times(file_path):
    df = pd.read_csv(file_path).copy()
    unique_partitions = df['partition'].unique()

    # Initial conditions
    first_fail_time = -1
    second_fail_time = -1
    fail_count = 0
    t = 0  # Total loop count

    while fail_count < 2 and t < len(df):  # Stop after second fail or check all data
        selected_partition = np.random.choice(unique_partitions)
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
                    break  # Stop after detecting second fail

            # Remove selected data only if first fail hasn't been detected or after first fail
            df = df.drop(row_index)

        t += 1
    
    return (first_fail_time, second_fail_time)

# Example usage
num_iterations = 40
fail_times = []

for _ in range(num_iterations):
    times = read_csv_and_detect_fail_times('QF4.csv')
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