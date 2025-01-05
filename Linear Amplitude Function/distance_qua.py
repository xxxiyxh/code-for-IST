import pandas as pd
import numpy as np
from ast import literal_eval

# 读取包含 partition 和 property 列的 CSV 文件
file_path = 'state_frequencies.csv'
df = pd.read_csv(file_path)

# 获取分组和概率信息
partitions = df['partition'].apply(lambda x: literal_eval(x))
properties = df['property'].apply(lambda x: literal_eval(x))

# 初始化距离矩阵
distance_matrix = np.zeros((len(partitions), len(partitions)))

# 计算迹距离
for i in range(len(partitions)):
    for j in range(i + 1, len(partitions)):
        # 提取两个分组的概率信息并转换为NumPy数组
        prob_i = np.array(properties[i])
        prob_j = np.array(properties[j])

        # 为了确保两个分布具有相同的长度，需要进行填充
        max_len = max(len(prob_i), len(prob_j))
        prob_i = np.pad(prob_i, (0, max_len - len(prob_i)), 'constant')
        prob_j = np.pad(prob_j, (0, max_len - len(prob_j)), 'constant')

        # 计算迹距离
        distance = 0.5 * np.sum(np.abs(prob_i - prob_j))

        # 更新距离矩阵
        distance_matrix[i, j] = distance
        distance_matrix[j, i] = distance  # 对称更新

# 将结果保存到CSV文件
result_df = pd.DataFrame(distance_matrix, index=partitions, columns=partitions)
result_df.to_csv('trace_distances.csv')
