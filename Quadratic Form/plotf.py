import matplotlib.pyplot as plt
import statistics


data1 = [3, 3, 2, 5, 3, 4, 2, 3, 5, 3, 1, 2, 4, 11, 17, 1, 1, 2, 2, 6, 12, 3, 1, 4, 3, 2, 2, 1, 4, 9, 3, 2, 2, 6, 2, 2, 4, 5, 5, 2, 1, 3, 2, 3, 1, 6, 1, 3, 14, 11, 2, 1, 5, 1, 2, 3, 5, 2, 7, 11, 2, 1, 4, 5, 1, 1, 8, 7, 8, 3, 11, 1, 5, 4, 1, 1, 2, 7, 1, 4] 
data2 = [2, 3, 6, 1, 3, 2, 2, 1, 3, 7, 4, 3, 7, 1, 4, 1, 2, 1, 3, 1, 2, 2, 4, 6, 2, 1, 2, 1, 3, 8, 2, 2, 5, 3, 2, 1, 4, 4, 2, 1, 3, 4, 1, 2, 2, 7, 1, 4, 1, 1, 1, 4, 7, 5, 4, 1, 1, 1, 1, 3, 4, 2, 1, 1, 4, 6, 1, 5, 2, 4, 1, 3, 7, 2, 5, 5, 1, 4, 1, 6]  
data3 = [1, 1, 3, 2, 2, 4, 3, 4, 4, 1, 1, 2, 4, 1, 1, 4, 4, 3, 1, 6, 2, 3, 9, 3, 1, 4, 1, 2, 1, 1, 2, 2, 1, 1, 2, 4, 2, 1, 1, 1, 1, 4, 1, 6, 6, 2, 1, 3, 1, 1, 1, 1, 1, 2, 1, 5, 1, 2, 2, 3, 2, 1, 1, 1, 4, 2, 1, 1, 1, 2, 2, 4, 2, 3, 3, 1, 5, 3, 1, 3]  
data4 = [1, 1, 2, 2, 3, 3, 4, 2, 1, 2, 1, 1, 2, 1, 1, 4, 2, 1, 2, 2, 2, 2, 1, 2, 2, 1, 1, 1, 1, 1, 2, 3, 4, 1, 4, 1, 1, 1, 1, 1, 1, 4, 1, 4, 4, 2, 1, 3, 1, 1, 3, 1, 2, 3, 2, 1, 1, 3, 1, 4, 4, 3, 4, 4, 6, 1, 2, 1, 1, 2, 1, 1, 1, 2, 3, 3, 4, 4, 1, 2]  


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
