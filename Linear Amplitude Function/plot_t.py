import matplotlib.pyplot as plt
import numpy as np


data = {
    'V1': [7.01,6.88,3.22],
    'V2': [7.1, 5.2, 3.17],
    'V3': [4.2, 6.2, 6.02],
    'V4': [4.2, 4.18, 3.98]
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
