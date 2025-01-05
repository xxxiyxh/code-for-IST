import matplotlib.pyplot as plt
import numpy as np


data = {
    'V1': [4.3, 2.2, 1.97],
    'V2': [3.87, 2.01, 2.11],
    'V3': [14.3, 10.4, 8.3],
    'V4': [7.6, 6.8, 5.3]
}
group_labels = list(data.keys()) 
measurement_labels = ['RT', 'RPT', 'D-DRT']  


bar_width = 0.25


fig, ax = plt.subplots()


x_positions = np.arange(len(data))


for i in range(len(measurement_labels)):
    values = [group[i] for group in data.values()]  
    ax.bar(x_positions + i * bar_width, values, width=bar_width, label=measurement_labels[i])


ax.set_xticks(x_positions + bar_width)
ax.set_xticklabels(group_labels)


ax.set_xlabel('Version')
ax.set_ylabel('APFD')



ax.legend()


plt.show()
