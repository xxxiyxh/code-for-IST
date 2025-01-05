import matplotlib.pyplot as plt
import numpy as np


data = {
    'V1': [6.325, 4.211, 4.155],
    'V2': [8.12, 6.075, 4.98],
    'V3': [10.65, 7.9, 8.1],
    'V4': [4.5, 5.1, 4.3]
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
