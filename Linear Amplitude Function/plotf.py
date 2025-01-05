import matplotlib.pyplot as plt
import statistics

# 数据部分
data1 = [2, 1, 2, 3, 2, 5, 9, 1, 2, 2, 9, 5, 2, 6, 1, 5, 2, 3, 4, 2, 8, 9, 8, 5, 2, 4, 2, 4, 1, 1, 1, 3, 2, 9, 6, 3, 1, 5, 3, 2, 7, 3, 1, 1, 1, 8, 17, 2, 6, 1, 5, 2, 14, 1, 2, 3, 4, 1, 1, 4, 6, 5, 10, 1, 1, 1, 4, 6, 7, 2, 10, 8, 2, 8, 6, 3, 2, 3, 1, 1]   # 第一段数据
data2 = [6, 3, 2, 21, 2, 11, 2, 2, 2, 13, 23, 3, 3, 4, 1, 11, 3, 4, 1, 21, 5, 19, 13, 5, 21, 7, 4, 22, 1, 12, 3, 11, 12, 14, 7, 1, 1, 2, 2, 1, 3, 6, 1, 13, 7, 5, 16, 7, 5, 1, 2, 1, 1, 8, 9, 4, 9, 8, 5, 3, 3, 4, 17, 1, 7, 7, 14, 17, 1, 2, 1, 1, 13, 5, 7, 6, 5, 3, 5, 4]  # 第二段数据
data3 = [3, 6, 15, 3, 2, 8, 37, 13, 6, 9, 4, 12, 6, 12, 2, 18, 6, 5, 16, 7, 9, 9, 19, 2, 6, 5, 7, 11, 9, 7, 4, 4, 2, 12, 2, 7, 8, 1, 17, 16, 10, 6, 7, 3, 5, 4, 5, 4, 5, 18, 3, 9, 12, 3, 6, 6, 4, 2, 8, 8, 3, 7, 15, 4, 5, 4, 9, 2, 7, 4, 8, 6, 9, 24, 3, 13, 4, 3, 9, 14] # 第三段数据
data4 = [1, 1, 1, 3, 1, 20, 3, 3, 18, 8, 3, 3, 1, 6, 4, 16, 3, 2, 5, 2, 5, 3, 9, 9, 11, 8, 2, 9, 3, 1, 1, 7, 6, 2, 7, 7, 10, 6, 3, 15, 14, 1, 2, 19, 1, 5, 1, 1, 1, 2, 1, 12, 8, 6, 13, 10, 16, 2, 1, 1, 4, 4, 8, 2, 4, 7, 1, 20, 7, 18, 13, 14, 7, 19, 3, 3, 16, 12, 4, 6]  # 第四段数据

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
ax.set_xticklabels(['rt', 'rpt', 'drt', 'ddrt'])

plt.show()
