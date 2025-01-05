import pandas as pd
import numpy as np

df = pd.read_csv('Weighted Adder (part1).csv')

selected_columns = ['partition', 'n', 'weights']
df_selected = df[selected_columns].copy()

average_values = df_selected.groupby('partition').agg({'n': 'mean'}).reset_index()

df_selected['weights'] = df_selected['weights'].apply(eval).apply(lambda x: np.linalg.norm(x, ord=2))

distances = pd.DataFrame(columns=['partition1', 'partition2', 'distance'])

rows_list = []

for i in range(len(average_values) - 1):
    for j in range(i + 1, len(average_values)):
        partition1 = average_values['partition'].iloc[i]
        partition2 = average_values['partition'].iloc[j]
        
        sum_diff = sum(abs(average_values.loc[i, ['n']] - average_values.loc[j, ['n']]))

        A_diff = abs(df_selected[df_selected['partition'] == partition1]['weights'].mean() - df_selected[df_selected['partition'] == partition2]['weights'].mean())
       
        total_distance = sum_diff + A_diff
        rows_list.append({'partition1': partition1, 'partition2': partition2, 'distance': total_distance})

new_rows_df = pd.DataFrame(rows_list)
distances = pd.concat([distances, new_rows_df], ignore_index=True)

distances.to_csv('distance_updated.csv', index=False)
