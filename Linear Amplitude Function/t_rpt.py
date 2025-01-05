import pandas as pd
import numpy as np

def read_csv_and_select_data_enhanced(file_path):
    df = pd.read_csv(file_path).copy()
    unique_partitions = df['partition'].unique()
    
    # 统计'fail'的数量
    total_fail_count = df['result'].value_counts().get('fail', 0)
    
    fail_count = 0
    t = 0  # 记录循环次数
    
    while fail_count < total_fail_count and t < len(df):
        selected_partition = np.random.choice(unique_partitions)
        partition_df = df[df['partition'] == selected_partition]
        if not partition_df.empty:
            selected_row = partition_df.sample(n=1)
            row_index = selected_row.index
            selected_result = selected_row['result'].values[0]
            
            if selected_result == 'fail':
                fail_count += 1
            
            # 从DataFrame中删除已选数据
            df = df.drop(row_index)
        
        t += 1
    
    return t

num_iterations = 40
t_values = []

for _ in range(num_iterations):
    t = read_csv_and_select_data_enhanced('filtered_data.csv')
    t_values.append(t)

average_t = np.mean(t_values)

print("Average t Value:", average_t)
