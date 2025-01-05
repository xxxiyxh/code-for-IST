import pandas as pd
import numpy as np

def read_csv_and_select_data_enhanced(file_path):
    # 读取CSV文件的拷贝
    df = pd.read_csv(file_path).copy()
    
    # 统计所有数据数和'fail'的数量
    total_fail_count = df['result'].value_counts().get('fail', 0)
    
    fail_count = 0
    t = 0  # 记录循环次数
    
    # 当已选到的fail数和总fail数相等时退出循环
    while fail_count < total_fail_count and t < len(df):
        selected_row = df.sample(n=1)
        row_index = selected_row.index
        selected_result = selected_row['result'].values[0]
        
        # 如果抽取到'fail'，则已选到的'fail'数加一
        if selected_result == 'fail':
            fail_count += 1
        
        # 从DataFrame中删除已选数据
        df = df.drop(row_index)
        
        t += 1  # 更新循环次数
    
    return t

num_iterations = 40
t_values = []

for _ in range(num_iterations):
    t = read_csv_and_select_data_enhanced('filtered_data.csv')
    t_values.append(t)

# 计算t值的平均值
average_t = np.mean(t_values)

print("Average t Value:", average_t)
