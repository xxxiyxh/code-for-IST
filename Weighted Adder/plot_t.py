import matplotlib.pyplot as plt
import numpy as np


data = {
    'V1': [8.11, 4.15, 3.04],
    'V2': [14.2, 8.3, 6.1],
    'V3': [3.98, 3.87, 2.96],
    'V4': [4.6, 4.8, 4.5]
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
