import pandas as pd

csv_filename = "IC (part4).csv"  
csv_data = pd.read_csv(csv_filename)

sample_size = 600  
num_iterations = 80  

def apfd(test_results):
    test_results_list = list(test_results['result'])
    failure_order = [index + 1 for index, value in enumerate(test_results_list) if value == 'fail']
    number_failure = len(failure_order)
    number_tests = len(test_results_list)
    metric_value = 1 - (sum(failure_order) / (number_failure * number_tests)) + 1 / (2 * number_tests)
    return metric_value

average_apfd = 0
results_array = []

for _ in range(num_iterations):
    random_sample = csv_data.sample(n=sample_size)
    result = apfd(random_sample)
    average_apfd += result
    results_array.append(result)

average_apfd /= num_iterations

print("Average APFD over", num_iterations, "iterations:", average_apfd)
print(results_array)
