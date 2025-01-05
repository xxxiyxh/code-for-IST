import pandas as pd
import numpy as np
from scipy.spatial.distance import pdist, squareform

file_path = 'initial_state.csv'  
df = pd.read_csv(file_path)

partitions = df['partition'].unique()

distance_matrix = np.zeros((len(partitions), len(partitions)))

for i in range(len(partitions)):
    for j in range(i + 1, len(partitions)):
        prob_i = eval(df[df['partition'] == partitions[i]]['property'].values[0])
        prob_j = eval(df[df['partition'] == partitions[j]]['property'].values[0])

        distance = pdist([prob_i, prob_j], metric='sqeuclidean')[0]

        distance_matrix[i, j] = distance
        distance_matrix[j, i] = distance

result_df = pd.DataFrame(distance_matrix, index=partitions, columns=partitions)
result_df.to_csv('trace_distances.csv')
