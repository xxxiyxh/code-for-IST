import pandas as pd

file_path = 'Linear Amplitude Function (part1).csv'
df = pd.read_csv(file_path)


df_copy = df.copy()

df_copy_1 = df_copy.loc[:, ['partition', 'n', 'slope', 'offset']]

result_df = df_copy_1.groupby('partition').mean()  


columns_to_calculate = ['n', 'slope', 'offset']


def calculate_distance(row1, row2):
    return (abs(row1['n'] - row2['n']) / 2 + abs(row1['slope'] - row2['slope']) / 6 + abs(row1['offset'] - row2['offset'] / 6)) / 3


distance_df = pd.DataFrame(columns=['distance', 'x', 'y'])


for x in result_df.index:
    for y in result_df.index:
        if x < y:  
            distance = calculate_distance(result_df.loc[x], result_df.loc[y])
            distance_df.loc[len(distance_df)] = [distance, x, y]

output_path = 'D:\lz\Linear Amplitude Function\distance_tradition.csv'
distance_df.to_csv(output_path, sep=',', index=False, header=['distance','partition1','partition2'])
