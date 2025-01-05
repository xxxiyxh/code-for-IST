import matplotlib.pyplot as plt
import numpy as np

# 每组的数据
data = {
    'V1': [16.525, 14.3, 11.2],
    'V2': [8.6, 8.1, 7.8],
    'V3': [10.1, 10.5, 9.8],
    'V4': [6.4, 6.2, 6.1]
}
group_labels = list(data.keys())  # 横坐标标签
measurement_labels = ['RT', 'RPT', 'D-DRT']  # 图例标签

# 设置柱状图的宽度
bar_width = 0.25

# 创建图像和轴
fig, ax = plt.subplots()

# 计算组的位置
x_positions = np.arange(len(data))

# 绘制柱状图
for i in range(len(measurement_labels)):
    values = [group[i] for group in data.values()]  # 提取每个组的第 i 项数据
    ax.bar(x_positions + i * bar_width, values, width=bar_width, label=measurement_labels[i])

# 设置x轴的刻度位置和标签
ax.set_xticks(x_positions + bar_width)
ax.set_xticklabels(group_labels)

# 设置坐标轴标签和图表标题
ax.set_xlabel('Version')
ax.set_ylabel('APFD')


# 添加图例
ax.legend()

# 显示图表
plt.show()
