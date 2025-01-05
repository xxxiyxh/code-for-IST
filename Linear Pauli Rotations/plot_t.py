import matplotlib.pyplot as plt
import numpy as np


data = {
    'V1': [16.525, 14.3, 11.2],
    'V2': [8.6, 8.1, 7.8],
    'V3': [10.1, 10.5, 9.8],
    'V4': [6.4, 6.2, 6.1]
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
