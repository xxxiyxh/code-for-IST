import matplotlib.pyplot as plt
import statistics


data1 = [4, 5, 10, 4, 1, 4, 20, 1, 1, 1, 5, 5, 4, 9, 1, 9, 3, 4, 22, 2, 8, 5, 2, 2, 6, 5, 7, 3, 3, 16, 8, 11, 9, 3, 1, 5, 8, 7, 6, 1, 7, 20, 7, 8, 4, 1, 6, 1, 1, 3, 5, 1, 14, 2, 3, 14, 3, 4, 3, 3, 12, 4, 3, 5, 3, 6, 1, 18, 13, 16, 1, 3, 17, 22, 11, 3, 15, 5, 9, 1]  
data2 = [15, 5, 3, 16, 7, 21, 4, 2, 12, 2, 2, 15, 6, 7, 9, 2, 3, 8, 3, 5, 4, 7, 7, 5, 7, 1, 1, 1, 4, 6, 4, 8, 1, 1, 1, 4, 3, 2, 2, 14, 13, 5, 26, 3, 4, 12, 9, 1, 1, 1, 3, 2, 4, 5, 7, 2, 1, 3, 2, 6, 5, 6, 7, 5, 3, 4, 12, 4, 13, 2, 2, 12, 11, 13, 6, 8, 7, 2, 10, 9]  
data3 = [3, 6, 15, 3, 2, 8, 3, 13, 6, 9, 4, 12, 6, 12, 2, 1, 6, 5, 16, 7, 9, 9, 1, 2, 6, 5, 7, 11, 9, 7, 4, 4, 2, 12, 2, 7, 8, 1, 17, 16, 10, 6, 7, 3, 5, 4, 5, 4, 5, 1, 3, 9, 12, 3, 6, 6, 4, 2, 8, 8, 3, 7, 15, 4, 5, 4, 9, 2, 7, 4, 8, 6, 9, 24, 3, 13, 4, 3, 9, 14]
data4 = [7, 7, 2, 7, 2, 3, 3, 5, 3, 7, 5, 2, 1, 4, 1, 3, 2, 8, 5, 2, 1, 6, 2, 6, 6, 2, 2, 3, 13, 5, 6, 1, 1, 1, 4, 6, 4, 8, 3, 2, 2, 11, 10, 3, 6, 5, 2, 7, 2, 2, 7, 2, 9, 7, 3, 1, 11, 7, 3, 1, 1, 1, 5, 4, 5, 9, 9, 3, 11, 10, 5, 3, 2, 4, 7, 5, 4, 7, 1, 1]  


variance1 = statistics.variance(data1)
variance2 = statistics.variance(data2)
variance3 = statistics.variance(data3)
variance4 = statistics.variance(data4)


print("Data1 Variance:", variance1)
print("Data2 Variance:", variance2)
print("Data3 Variance:", variance3)
print("Data4 Variance:", variance4)

mean1 = statistics.mean(data1)
mean2 = statistics.mean(data2)
mean3 = statistics.mean(data3)
mean4 = statistics.mean(data4)


print("Data1 Mean:", mean1)
print("Data2 Mean:", mean2)
print("Data3 Mean:", mean3)
print("Data4 Mean:", mean4)


fig, ax = plt.subplots()
ax.boxplot([data1, data2, data3, data4])


ax.set_title('boxplot')
ax.set_xticklabels(['rt', 'rpt', 'drt', 'ddrt'])

plt.show()
