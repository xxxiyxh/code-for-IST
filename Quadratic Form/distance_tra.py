import pandas as pd
import numpy as np

df = pd.read_csv('Quadratic Form (part1).csv')

selected_columns = ['partition', 'n', 'm', 'A', 'b', 'c']
df_selected = df[selected_columns].copy()

average_values = df_selected.groupby('partition').agg({'n': 'mean', 'm': 'mean', 'c': 'mean'}).reset_index()

df_selected['A'] = df_selected['A'].apply(eval).apply(lambda x: np.linalg.norm(x, ord=2))
df_selected['b'] = df_selected['b'].apply(eval).apply(lambda x: np.linalg.norm(x, ord=2))

distances = pd.DataFrame(columns=['partition1', 'partition2', 'distance'])

rows_list = []

for i in range(len(average_values) - 1):
    for j in range(i + 1, len(average_values)):
        partition1 = average_values['partition'].iloc[i]
        partition2 = average_values['partition'].iloc[j]
        
        sum_diff = sum(abs(average_values.loc[i, ['n', 'm', 'c']] - average_values.loc[j, ['n', 'm', 'c']]))
        
        A_diff = abs(df_selected[df_selected['partition'] == partition1]['A'].mean() - df_selected[df_selected['partition'] == partition2]['A'].mean())
        b_diff = abs(df_selected[df_selected['partition'] == partition1]['b'].mean() - df_selected[df_selected['partition'] == partition2]['b'].mean())
        
        total_distance = sum_diff + A_diff + b_diff
        rows_list.append({'partition1': partition1, 'partition2': partition2, 'distance': total_distance})

new_rows_df = pd.DataFrame(rows_list)
distances = pd.concat([distances, new_rows_df], ignore_index=True)

distances.to_csv('distance_updated.csv', index=False)
