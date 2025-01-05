import pandas as pd
import numpy as np
import random

def read_csv_and_select_data(file_path, m, epsilon, delta, epsilon_matrix_file, delta_matrix_file):
    # 读取CSV文件的拷贝
    df = pd.read_csv(file_path).copy()

    # 获取不同分块的种类
    unique_partitions = df['partition'].unique()

    # 初始化分块概率字典，初始概率为1/n
    partition_probabilities = {partition: 1 / len(unique_partitions) for partition in unique_partitions}

    # 读取 epsilon_matrix 和 delta_matrix 文件
    epsilon_matrix = pd.read_csv(epsilon_matrix_file, index_col=0)
    delta_matrix = pd.read_csv(delta_matrix_file, index_col=0)

    selected_data = []

    for _ in range(m):
        # 根据概率选择一个分块
        selected_partition = random.choices(unique_partitions, weights=list(partition_probabilities.values()))[0]

        # 在选择的分块中选择一个数据
        selected_rows = df[df['partition'] == selected_partition]

        # 检查是否存在满足条件的行
        if selected_rows.empty:
            continue  # 如果没有找到满足条件的行，跳过本次循环

        selected_row = selected_rows.sample(n=1)

        # 获取 'result' 列的值
        result_value = selected_row['result'].values[0]

        # 调整分块概率
        p = partition_probabilities[selected_partition]
        if result_value == 'pass':
            # 判断当前分块的概率 p 是否小于预设的 delta
            if p < delta:
                partition_probabilities[selected_partition] = 0
            else:
                # 减少 delta
                partition_probabilities[selected_partition] -= delta

            # 遍历 delta_matrix 矩阵，调整其他分块的概率
            for other_partition in partition_probabilities:
                if other_partition != selected_partition:
                    delta_j = delta_matrix.loc[selected_partition, other_partition]
                    # 判断应该调整概率的分块的概率
                    if partition_probabilities[other_partition] > delta:
                        # 大于 delta，则上调 delta_j
                        partition_probabilities[other_partition] += delta_j
                    else:
                        # 小于 delta，则上调 delta_j * p / delta
                        partition_probabilities[other_partition] += delta_j * p / delta

        elif result_value == 'fail':
            total_probability_except_selected = sum(prob for partition, prob in partition_probabilities.items() if partition != selected_partition)
            for other_partition in partition_probabilities:
                if other_partition != selected_partition:
                    # 从 epsilon_matrix 矩阵中读取每个分块对应的 epsilon_j
                    epsilon_j = epsilon_matrix.loc[selected_partition, other_partition]

                    # 检查当前概率是否大于 epsilon_j
                    if partition_probabilities[other_partition] > epsilon_j:
                        # 大于 epsilon_j，则减少 epsilon_j
                        partition_probabilities[other_partition] -= epsilon_j
                    else:
                        # 小于等于 epsilon_j，则调整为0
                        partition_probabilities[other_partition] = 0

            # 对于当前被选中的分块，按照概率和为1计算
            partition_probabilities[selected_partition] = 1 - sum(partition_probabilities.values()) + partition_probabilities[selected_partition]

        # 将结果添加到列表
        selected_data.append(result_value)

        # 从数据框中删除选择的行
        df = df[df.index != selected_row.index[0]]

    return selected_data

def apfd(test_results):
    failure_order = [index + 1 for index, value in enumerate(test_results) if value == 'fail']
    number_failure = len(failure_order)
    number_tests = len(test_results)
    metric_value = 1 - (sum(failure_order) / (number_failure * number_tests)) + 1 / (2 * number_tests)
    return metric_value

# 设置 epsilon 和 delta 的值
epsilon = 0.05
delta = 0.05

# 重复20次计算APFD指标并记录结果
num_iterations = 50
average_metric_values = []

for _ in range(num_iterations):
    selected_data = read_csv_and_select_data('partition_n_ini.csv', m=600, epsilon=epsilon, delta=delta, epsilon_matrix_file='epsilon_matrix.csv', delta_matrix_file='delta_matrix.csv')
    metric_value = apfd(selected_data)
    average_metric_values.append(metric_value)

# 计算平均值
print(average_metric_values)
average_metric = np.mean(average_metric_values)

# 打印计算得到的平均指标值
print("Average APFD Metric Value:", average_metric)
