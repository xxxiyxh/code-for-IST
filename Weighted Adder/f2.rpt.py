import pandas as pd
import numpy as np
import random

def read_csv_and_detect_fail_intervals(file_path):
    df = pd.read_csv(file_path).copy()
    unique_partitions = df['partition'].unique()

    # Initial conditions
    first_fail_detected = False
    fail_count = 0
    t = 0  # Total loop count
    interval_count = 0  # Loop count after first fail

    while fail_count < 2 and t < len(df):  # Stop after second fail or check all data
        selected_partition = np.random.choice(unique_partitions)
        partition_df = df[df['partition'] == selected_partition]
        if not partition_df.empty:
            selected_row = partition_df.sample(n=1)
            row_index = selected_row.index
            selected_result = selected_row['result'].values[0]
            
            if selected_result == 'fail':
                fail_count += 1
                if first_fail_detected:
                    break  # Stop after detecting second fail
                first_fail_detected = True  # Mark first fail detected

            # Remove selected data only if first fail hasn't been detected or after first fail
            if not first_fail_detected or interval_count > 0:
                df = df.drop(row_index)
            
            if first_fail_detected:
                interval_count += 1  # Count intervals only after first fail

        t += 1
    
    return interval_count

# Example usage
num_iterations = 40
interval_counts = []

for _ in range(num_iterations):
    interval_count = read_csv_and_detect_fail_intervals('WA4.csv')
    interval_counts.append(interval_count)

print(interval_counts)
average_interval = np.mean(interval_counts)
print("Average Interval Count:", average_interval)
