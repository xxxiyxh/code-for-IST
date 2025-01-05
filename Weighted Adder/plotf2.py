import matplotlib.pyplot as plt
import statistics

# 数据部分
data4 = [4, 2, 1, 1, 1, 2, 1, 1, 4, 2, 4, 1, 2, 6, 3, 3, 4, 3, 1, 1, 1, 2, 1, 2, 2, 3, 2, 1, 2, 1, 2, 3, 2, 2, 2, 9, 2, 2, 1, 3, 3, 1, 2, 1, 2, 4, 4, 3, 2, 2, 2, 1, 1, 3, 3, 1, 5, 1, 4, 1, 4, 2, 4, 1, 2, 1, 1, 1, 6, 2, 4, 6, 2, 3, 6, 1, 4, 2, 8, 3]   # 第一段数据
data2 = [1, 24, 10, 9, 6, 6, 1, 2, 3, 3, 3, 12, 2, 5, 3, 8, 6, 16, 5, 6, 8, 10, 4, 2, 5, 3, 1, 25, 4, 4, 2, 11, 2, 3, 4, 17, 2, 10, 2, 2, 9, 4, 4, 3, 7, 12, 2, 4, 3, 2, 2, 20, 13, 8, 1, 3, 1, 2, 2, 8, 6, 4, 9, 10, 1, 8, 3, 1, 5, 6, 8, 16, 27, 1, 4, 10, 4, 1, 4, 8]  # 第二段数据
data3 = [2, 3, 11, 2, 2, 3, 4, 9, 12, 12, 3, 9, 2, 6, 3, 6, 1, 4, 2, 9, 2, 4, 8, 6, 11, 12, 13, 3, 8, 1, 1, 1, 11, 2, 4, 7, 5, 6, 6, 1, 2, 1, 9, 3, 12, 2, 7, 7, 5, 6, 1, 1, 16, 3, 2, 5, 13, 7, 2, 2, 4, 12, 1, 10, 3, 2, 1, 7, 2, 3, 2, 1, 4, 1, 7, 8, 3, 1, 5, 4]  # 第三段数据
data1 = [5, 1, 16, 1, 18, 14, 1, 2, 2, 6, 1, 8, 6, 8, 1, 4, 7, 2, 2, 18, 5, 43, 1, 9, 13, 1, 6, 7, 1, 7, 7, 3, 4, 4, 15, 1, 10, 3, 2, 2, 6, 10, 21, 6, 1, 2, 10, 5, 5, 3, 10, 6, 3, 7, 14, 2, 10, 3, 1, 3, 4, 4, 1, 24, 6, 7, 5, 4, 1, 4, 1, 2, 1, 7, 8, 2, 5, 5, 2, 5]  # 第四段数据

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
