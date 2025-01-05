import pandas as pd

distance_tradition_path = 'distance_tradition.csv'
df_distance_tradition = pd.read_csv(distance_tradition_path)

trace_distance_path = 'trace_distances.csv'
df_trace_distance = pd.read_csv(trace_distance_path, index_col=0)

result_df = pd.DataFrame()

for index, row in df_distance_tradition.iterrows():
    partition1 = row['partition1']
    partition2 = row['partition2']
    
    distance_b = df_trace_distance.loc[partition1, partition2]
    
    total_distance = row['distance'] + distance_b
    
    result_df = pd.concat([result_df, pd.DataFrame({
        'partition1': [partition1],
        'partition2': [partition2],
        'total_distance': [total_distance]
    })], ignore_index=True)

result_path = 'total_distances.csv'
result_df.to_csv(result_path, index=False)
