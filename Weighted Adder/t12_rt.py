import pandas as pd
import numpy as np
import random

def read_csv_and_detect_fail_times(file_path):
    df = pd.read_csv(file_path).copy()
    
    # Initialize variables
    fail_count = 0
    t = 0  # Total loop count
    first_fail_time = -1  # Time when the first failure was found
    second_fail_time = -1  # Time when the second failure was found
    
    while len(df) > 0 and fail_count < 2:  # Continue until 2 fails are found or no data left
        np.random.seed()  # Ensure randomness
        selected_index = np.random.choice(df.index)
        selected_result = df.loc[selected_index, 'result']
        
        df = df.drop(selected_index)  # Remove the selected row
        
        if selected_result == 'fail':
            fail_count += 1
            if fail_count == 1:
                first_fail_time = t  # Record the time of the first failure
            elif fail_count == 2:
                second_fail_time = t  # Record the time of the second failure
                return (first_fail_time, second_fail_time)  # Return times of both failures
        
        t += 1
    
    return (first_fail_time, second_fail_time)  # Return times, might still be -1 if fails are not found

# Example usage
num_iterations = 40
fail_times = []

for _ in range(num_iterations):
    times = read_csv_and_detect_fail_times('WA4.csv')
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