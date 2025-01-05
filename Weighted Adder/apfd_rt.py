import pandas as pd
import numpy as np
import random

def read_csv_and_select_data(file_path, m):
    df = pd.read_csv(file_path)

    selected_data = []

    for _ in range(m):
        selected_row = df.sample(n=1)

        selected_data.append(selected_row['result'].values[0])

    return selected_data

def apfd(test_results):
    failure_order = [index + 1 for index, value in enumerate(test_results) if value == 'fail']
    number_failure = len(failure_order)
    number_tests = len(test_results)
    metric_value = 1 - (sum(failure_order) / (number_failure * number_tests)) + 1 / (2 * number_tests)
    return metric_value

num_iterations = 40
average_metric_values = []

for _ in range(num_iterations):
    selected_data = read_csv_and_select_data('WA4.csv', m=600)
    metric_value = apfd(selected_data)
    average_metric_values.append(metric_value)

print(average_metric_values)
average_metric = np.mean(average_metric_values)

print("Average APFD Metric Value:", average_metric)
