import pandas as pd

trace_distances = pd.read_csv('trace_distances.csv', index_col=0)


distance_tradition = pd.read_csv('distance_updated.csv')


result_data = pd.DataFrame(columns=['partition1', 'partition2', 'total_distance'])


for index, row in distance_tradition.iterrows():
    partition1 = row['partition1']
    partition2 = row['partition2']


    trace_distance = trace_distances.loc[partition1, partition2]


    total_distance = row['distance'] + trace_distance


    result_data = pd.concat([result_data, pd.DataFrame([[partition1, partition2, total_distance]], columns=['partition1', 'partition2', 'total_distance'])], ignore_index=True)


result_data.to_csv('total_distance.csv', index=False)
