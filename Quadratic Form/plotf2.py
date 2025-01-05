import matplotlib.pyplot as plt
import statistics


data1 = [2, 1, 3, 1, 1, 1, 1, 4, 4, 1, 3, 3, 3, 1, 2, 2, 14, 4, 1, 3, 1, 1, 1, 1, 2, 1, 1, 4, 2, 4, 1, 7, 2, 2, 2, 5, 1, 4, 2, 2, 9, 2, 2, 4, 2, 3, 2, 6, 3, 3, 2, 2, 1, 2, 1, 1, 2, 1, 1, 4, 11, 2, 10, 1, 2, 1, 1, 2, 2, 1, 1, 8, 1, 3, 2, 1, 4, 1, 3, 3]  
data2 = [6, 1, 2, 1, 1, 1, 3, 2, 2, 1, 1, 3, 1, 5, 3, 1, 1, 2, 1, 4, 3, 3, 6, 2, 1, 1, 2, 2, 3, 1, 1, 4, 1, 4, 1, 1, 2, 1, 1, 1, 2, 1, 1, 1, 1, 2, 3, 1, 1, 2, 2, 1, 4, 3, 2, 5, 1, 2, 2, 1, 1, 1, 1, 1, 5, 1, 1, 2, 3, 5, 5, 2, 1, 3, 9, 5, 1, 1, 2, 1] 
data3 = [1, 3, 1, 2, 5, 1, 4, 2, 3, 2, 1, 3, 2, 1, 2, 1, 3, 1, 2, 3, 1, 3, 5, 5, 1, 1, 1, 1, 1, 2, 1, 5, 3, 1, 2, 2, 2, 1, 1, 1, 1, 4, 3, 2, 1, 2, 1, 1, 2, 1, 2, 1, 1, 5, 7, 5, 2, 2, 3, 1, 1, 3, 1, 3, 2, 1, 2, 2, 1, 1, 1, 1, 3, 2, 1, 3, 1, 1, 6, 3] 
data4 = [1, 7, 2, 3, 2, 1, 4, 1, 1, 1, 1, 2, 2, 1, 6, 1, 2, 2, 1, 2, 1, 1, 4, 2, 1, 4, 1, 1, 1, 3, 1, 1, 3, 5, 1, 1, 4, 3, 1, 4, 2, 1, 1, 4, 1, 1, 1, 2, 2, 2, 1, 1, 1, 2, 2, 3, 1, 1, 3, 2, 4, 2, 1, 1, 2, 1, 2, 2, 2, 1, 1, 1, 6, 2, 1, 3, 3, 1, 1, 1]  


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
