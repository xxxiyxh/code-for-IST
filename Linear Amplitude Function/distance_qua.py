import pandas as pd
import numpy as np
from ast import literal_eval


file_path = 'state_frequencies.csv'
df = pd.read_csv(file_path)


partitions = df['partition'].apply(lambda x: literal_eval(x))
properties = df['property'].apply(lambda x: literal_eval(x))


distance_matrix = np.zeros((len(partitions), len(partitions)))


for i in range(len(partitions)):
    for j in range(i + 1, len(partitions)):

        prob_i = np.array(properties[i])
        prob_j = np.array(properties[j])

 
        max_len = max(len(prob_i), len(prob_j))
        prob_i = np.pad(prob_i, (0, max_len - len(prob_i)), 'constant')
        prob_j = np.pad(prob_j, (0, max_len - len(prob_j)), 'constant')


        distance = 0.5 * np.sum(np.abs(prob_i - prob_j))


        distance_matrix[i, j] = distance
        distance_matrix[j, i] = distance 


result_df = pd.DataFrame(distance_matrix, index=partitions, columns=partitions)
result_df.to_csv('trace_distances.csv')
