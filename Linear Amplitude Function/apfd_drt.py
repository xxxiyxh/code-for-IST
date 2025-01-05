import pandas as pd
import numpy as np
import random

def read_csv_and_select_data(file_path, m, epsilon, delta):
    # 读取CSV文件的拷贝
    df = pd.read_csv(file_path).copy()

    # 获取不同分块的种类
    unique_partitions = df['partition'].unique()

    # 初始化分块概率字典，初始概率为1/n
    partition_probabilities = {partition: 1 / len(unique_partitions) for partition in unique_partitions}

    selected_data = []

    for _ in range(m):
        # 循环直到选择到非空数据集
        while True:
            # 根据概率选择一个分块
            selected_partition = random.choices(unique_partitions, weights=list(partition_probabilities.values()))[0]

            # 在选择的分块中选择一个数据
            selected_rows = df[df['partition'] == selected_partition]

            # 检查是否存在满足条件的行
            if not selected_rows.empty:
                break  # 如果找到满足条件的行，跳出循环

        selected_row = selected_rows.sample(n=1)

        # 获取 'result' 列的值
        result_value = selected_row['result'].values[0]

        # 调整分块概率
        p = partition_probabilities[selected_partition]
        if result_value == 'pass':
            # 如果是pass，判断p是否小于delta，如果是则将该分块概率调整为0，否则下降delta
            if p < delta:
                partition_probabilities[selected_partition] = 0
            else:
                partition_probabilities[selected_partition] -= delta
            total_probability_except_selected = sum(prob for partition, prob in partition_probabilities.items() if partition != selected_partition)
            for partition in partition_probabilities:
                if partition != selected_partition:
                    # 判断其他分块概率是否大于delta，如果是则提高delta/n-1，否则提高p/n-1
                    if partition_probabilities[partition] > delta / (len(unique_partitions) - 1):
                        partition_probabilities[partition] += delta / (len(unique_partitions) - 1)
                    else:
                        partition_probabilities[partition] += p / (len(unique_partitions) - 1)
        elif result_value == 'fail':
            total_probability_except_selected = sum(prob for partition, prob in partition_probabilities.items() if partition != selected_partition)
            for partition in partition_probabilities:
                if partition != selected_partition:
                    # 判断其他分块概率是否大于epsilon/n-1，如果是则降低epsilon/n-1，否则调整为0
                    if partition_probabilities[partition] > epsilon / (len(unique_partitions) - 1):
                        partition_probabilities[partition] -= epsilon / (len(unique_partitions) - 1)
                    else:
                        partition_probabilities[partition] = 0
            # p计算方式不变
            partition_probabilities[selected_partition] = min(p + epsilon, 1)

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
epsilon = 0.07
delta = 0.04

num_iterations = 40
average_metric_values = []

for _ in range(num_iterations):
    selected_data = read_csv_and_select_data('Linear Amplitude Function (part1).csv', m=600, epsilon=epsilon, delta=delta)
    metric_value = apfd(selected_data)
    average_metric_values.append(metric_value)

# 计算平均值
print(average_metric_values)
average_metric = np.mean(average_metric_values)

# 打印计算得到的平均指标值
print("Average APFD Metric Value:", average_metric)
