import matplotlib.pyplot as plt
import statistics

# 数据部分
data3 = [5, 3, 4, 4, 9, 4, 2, 15, 10, 14, 3, 17, 5, 1, 4, 2, 1, 1, 1, 2, 4, 2, 9, 7, 1, 3, 9, 6, 1, 3, 3, 7, 1, 5, 1, 3, 1, 4, 2, 5]  # 第一段数据
data4 = [2, 1, 3, 2, 3, 3, 3, 1, 2, 4, 3, 5, 3, 1, 2, 1, 3, 1, 5, 9, 1, 3, 3, 4, 5, 1, 1, 3, 1, 2, 6, 4, 3, 8, 1, 9, 7, 1, 10, 3]  # 第二段数据
data1 = [3, 10, 3, 10, 13, 5, 2, 10, 2, 11, 5, 6, 2, 3, 7, 6, 7, 1, 2, 13, 5, 2, 4, 15, 3, 14, 6, 8, 8, 3, 1, 3, 11, 1, 4, 2, 4, 3, 11, 1]  # 第三段数据
data2 = [1, 2, 3, 1, 5, 2, 1, 9, 6, 1, 2, 2, 5, 1, 10, 4, 1, 3, 5, 2, 1, 1, 7, 1, 5, 4, 13, 1, 1, 1, 1, 3, 17, 2, 4, 1, 3, 2, 2, 3]  # 第四段数据

# 计算方差
variance1 = statistics.variance(data1)
variance2 = statistics.variance(data2)
variance3 = statistics.variance(data3)
variance4 = statistics.variance(data4)

# 打印方差值
print("Data1 Variance:", variance1)
print("Data2 Variance:", variance2)
print("Data3 Variance:", variance3)
print("Data4 Variance:", variance4)

mean1 = statistics.mean(data1)
mean2 = statistics.mean(data2)
mean3 = statistics.mean(data3)
mean4 = statistics.mean(data4)

# 打印平均值
print("Data1 Mean:", mean1)
print("Data2 Mean:", mean2)
print("Data3 Mean:", mean3)
print("Data4 Mean:", mean4)

# 创建箱线图
fig, ax = plt.subplots()
ax.boxplot([data1, data2, data3, data4])

# 设置箱线图的标题和x轴的标签
ax.set_title('boxplot')
ax.set_xticklabels(['RT', 'RPT', 'DRT', 'D-DRT'])

plt.show()
