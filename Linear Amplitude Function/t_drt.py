import pandas as pd
import numpy as np
import random

def read_csv_and_select_data_enhanced(file_path, epsilon, delta):
    df = pd.read_csv(file_path).copy()
    unique_partitions = df['partition'].unique()
    partition_probabilities = {partition: 1 / len(unique_partitions) for partition in unique_partitions}
    
    total_fail_count = df['result'].value_counts().get('fail', 0)
    fail_count = 0
    t = 0  # 记录循环次数
    
    while fail_count < total_fail_count and t < len(df):
        selected_partition = random.choices(unique_partitions, weights=list(partition_probabilities.values()))[0]
        partition_df = df[df['partition'] == selected_partition]
        
        if not partition_df.empty:
            selected_row = partition_df.sample(n=1)
            row_index = selected_row.index
            selected_result = selected_row['result'].values[0]
            
            if selected_result == 'fail':
                fail_count += 1
                partition_probabilities[selected_partition] = min(partition_probabilities[selected_partition] + epsilon, 1)
            else:
                p = partition_probabilities[selected_partition]
                if p < delta:
                    partition_probabilities[selected_partition] = 0.00000001
                else:
                    partition_probabilities[selected_partition] -= delta

            # 从DataFrame中删除已选数据
            df = df.drop(row_index)
        
        t += 1
    
    return t

epsilon = 0.1
delta = 0.1

num_iterations = 80
t_values = []

for _ in range(num_iterations):
    t = read_csv_and_select_data_enhanced('Linear Amplitude Function (part1).csv', epsilon=epsilon, delta=delta)
    t_values.append(t)

average_t = np.mean(t_values)

print("Average t Value:", average_t)
