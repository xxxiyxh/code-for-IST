import pandas as pd

# 读取 trace_distances.csv 文件
trace_distances = pd.read_csv('trace_distances.csv', index_col=0)

# 读取 distance_tradition.csv 文件
distance_tradition = pd.read_csv('distance_updated.csv')

# 初始化结果数据框
result_data = pd.DataFrame(columns=['partition1', 'partition2', 'total_distance'])

# 遍历 distance_tradition 中的每一行
for index, row in distance_tradition.iterrows():
    partition1 = row['partition1']
    partition2 = row['partition2']

    # 使用 trace_distances 中对应位置的距离
    trace_distance = trace_distances.loc[partition1, partition2]

    # 将两个距离相加
    total_distance = row['distance'] + trace_distance

    # 将结果添加到结果数据框
    result_data = pd.concat([result_data, pd.DataFrame([[partition1, partition2, total_distance]], columns=['partition1', 'partition2', 'total_distance'])], ignore_index=True)

# 将结果保存为 total_distance.csv
result_data.to_csv('total_distance.csv', index=False)
