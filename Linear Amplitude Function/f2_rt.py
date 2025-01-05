import pandas as pd
import numpy as np
import random

def read_csv_and_detect_fail_intervals(file_path):
    df = pd.read_csv(file_path).copy()
    
    # Initialize variables
    fail_count = 0
    t = 0  # Total loop count
    first_fail_index = -1  # Index of the first failure
    
    while len(df) > 0 and fail_count < 2:  # Continue until 2 fails are found or no data left
        np.random.seed()  # Ensure randomness
        selected_index = np.random.choice(df.index)
        selected_result = df.loc[selected_index, 'result']
        
        df = df.drop(selected_index)  # Remove the selected row
        
        if selected_result == 'fail':
            fail_count += 1
            if fail_count == 1:
                first_fail_index = t  # Record the index of the first failure
            elif fail_count == 2:
                return t - first_fail_index  # Return the interval between the first and second failure
        
        t += 1
    
    return 0  # Return 0 if less than 2 fails are found

# Example usage
num_iterations = 40
interval_counts = []

for _ in range(num_iterations):
    interval = read_csv_and_detect_fail_intervals('filtered_data.csv')
    interval_counts.append(interval)
print(interval_counts)

average_interval = np.mean(interval_counts)

print("Average Interval Count Between First and Second Fail:", average_interval)
