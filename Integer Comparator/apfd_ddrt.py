import pandas as pd
import numpy as np
import random

def read_csv_and_select_data(file_path, m, epsilon, delta, epsilon_matrix_file, delta_matrix_file):
    df = pd.read_csv(file_path).copy()

    unique_partitions = df['partition'].unique()

    partition_probabilities = {partition: 1 / len(unique_partitions) for partition in unique_partitions}

    epsilon_matrix = pd.read_csv(epsilon_matrix_file, index_col=0)
    delta_matrix = pd.read_csv(delta_matrix_file, index_col=0)

    selected_data = []

    for _ in range(m):
        selected_partition = random.choices(unique_partitions, weights=list(partition_probabilities.values()))[0]
        selected_rows = df[df['partition'] == selected_partition]

        if selected_rows.empty:
            continue

        selected_row = selected_rows.sample(n=1)

        result_value = selected_row['result'].values[0]

        p = partition_probabilities[selected_partition]
        if result_value == 'pass':
            if p < delta:
                partition_probabilities[selected_partition] = 0
            else:
                partition_probabilities[selected_partition] -= delta

            for other_partition in partition_probabilities:
                if other_partition != selected_partition:
                    delta_j = delta_matrix.loc[selected_partition, other_partition]
                    if partition_probabilities[other_partition] > delta:
                        partition_probabilities[other_partition] += delta_j
                    else:
                        partition_probabilities[other_partition] += delta_j * p / delta

        elif result_value == 'fail':
            total_probability_except_selected = sum(prob for partition, prob in partition_probabilities.items() if partition != selected_partition)
            for other_partition in partition_probabilities:
                if other_partition != selected_partition:
                    epsilon_j = epsilon_matrix.loc[selected_partition, other_partition]
                    if partition_probabilities[other_partition] > epsilon_j:
                        partition_probabilities[other_partition] -= epsilon_j
                    else:
                        partition_probabilities[other_partition] = 0

            partition_probabilities[selected_partition] = 1 - sum(partition_probabilities.values()) + partition_probabilities[selected_partition]

        selected_data.append(result_value)
        df = df[df.index != selected_row.index[0]]

    return selected_data

def apfd(test_results):
    failure_order = [index + 1 for index, value in enumerate(test_results) if value == 'fail']
    number_failure = len(failure_order)
    number_tests = len(test_results)
    metric_value = 1 - (sum(failure_order) / (number_failure * number_tests)) + 1 / (2 * number_tests)
    return metric_value

epsilon = 0.05
delta = 0.05

num_iterations = 40
average_metric_values = []
metric_value_array = []

for _ in range(num_iterations):
    selected_data = read_csv_and_select_data('Integer Comparator (test_reports).csv', m=600, epsilon=epsilon, delta=delta, epsilon_matrix_file='epsilon_matrix.csv', delta_matrix_file='delta_matrix.csv')
    metric_value = apfd(selected_data)
    average_metric_values.append(metric_value)
    metric_value_array.append(metric_value)

average_metric = np.mean(average_metric_values)

print("Average APFD Metric Value:", average_metric)
print(metric_value_array)
