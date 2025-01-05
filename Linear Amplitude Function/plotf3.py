import matplotlib.pyplot as plt
import statistics

# 数据部分
data1 = [2, 7, 2, 7, 1, 4, 2, 2, 6, 8, 1, 1, 1, 5, 1, 1, 6, 1, 8, 1, 1, 8, 5, 7, 2, 2, 1, 3, 1, 4, 4, 7, 1, 2, 2, 3, 4, 8, 11, 3]  # 第一段数据
data2 = [1, 2, 1, 2, 1, 4, 2, 3, 7, 3, 3, 9, 1, 1, 14, 1, 9, 1, 3, 7, 2, 3, 1, 3, 3, 1, 3, 6, 16, 5, 4, 9, 2, 10, 4, 12, 4, 1, 2, 2]  # 第二段数据
data3 = [3, 10, 3, 10, 13, 55, 2, 10, 2, 11, 5, 6, 2, 3, 7, 6, 7, 1, 21, 13, 5, 21, 4, 15, 31, 14, 6, 8, 8, 3, 1, 3, 11, 1, 4, 2, 43, 3, 11, 17]  # 第三段数据
data4 = [1, 2, 4, 1, 7, 1, 1, 23, 22, 1, 1, 1, 15, 18, 13, 27, 16, 6, 16, 3, 12, 28, 4, 31, 16, 10, 9, 12, 17, 5, 37, 11, 3, 4, 4, 8, 7, 4, 9, 25]  # 第四段数据

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
