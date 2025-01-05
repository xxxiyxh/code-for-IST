import matplotlib.pyplot as plt
import statistics


data1 = [1, 2, 2, 1, 4, 2, 5, 6, 4, 11, 1, 5, 7, 2, 5, 7, 2, 3, 2, 1, 3, 1, 1, 4, 2, 1, 6, 3, 1, 1, 10, 12, 2, 5, 2, 2, 5, 1, 3, 4, 2, 1, 2, 2, 1, 8, 1, 4, 5, 3, 2, 6, 1, 8, 1, 2, 7, 1, 9, 13, 4, 2, 1, 1, 4, 13, 4, 9, 6, 1, 7, 5, 1, 9, 6, 1, 1, 5, 7, 1]  
data2 = [4, 5, 1, 1, 2, 2, 5, 1, 6, 4, 1, 1, 1, 1, 3, 1, 4, 5, 2, 1, 8, 4, 12, 4, 1, 5, 7, 4, 6, 1, 2, 1, 9, 6, 1, 3, 7, 2, 1, 5, 2, 3, 5, 11, 6, 2, 7, 2, 1, 5, 1, 2, 5, 1, 4, 1, 1, 7, 6, 2, 4, 5, 5, 4, 8, 4, 2, 1, 5, 1, 4, 2, 5, 2, 2, 3, 5, 2, 2, 4] 
data3 = [1, 3, 4, 2, 2, 1, 4, 5, 1, 3, 3, 1, 7, 1, 2, 1, 4, 6, 2, 6, 3, 4, 2, 2, 7, 7, 5, 3, 4, 3, 1, 6, 3, 3, 1, 2, 2, 1, 8, 3, 5, 2, 1, 1, 4, 3, 4, 1, 3, 2, 1, 6, 8, 2, 2, 3, 2, 5, 3, 1, 3, 1, 2, 1, 2, 1, 2, 2, 15, 2, 2, 3, 3, 6, 8, 1, 5, 3, 2, 2] 
data4 = [3, 3, 5, 5, 6, 2, 5, 1, 1, 2, 3, 2, 3, 3, 3, 1, 1, 1, 2, 2, 2, 4, 2, 6, 6, 3, 2, 2, 1, 2, 2, 2, 4, 2, 3, 2, 2, 4, 4, 2, 2, 2, 4, 1, 3, 2, 3, 5, 2, 2, 4, 3, 6, 6, 1, 6, 2, 1, 1, 4, 5, 2, 3, 2, 2, 5, 4, 3, 3, 3, 1, 4, 2, 3, 4, 1, 3, 4, 1, 3]


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
