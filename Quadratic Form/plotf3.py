import matplotlib.pyplot as plt
import statistics


data1 = [3, 2, 1, 1, 3, 4, 1, 7, 4, 2, 2, 3, 1, 2, 4, 2, 1, 1, 7, 2, 1, 3, 12, 1, 2, 7, 3, 6, 2, 3, 2, 2, 2, 1, 1, 7, 3, 3, 3, 7]  
data2 = [9, 4, 1, 2, 4, 5, 2, 9, 5, 1, 2, 3, 2, 2, 5, 1, 2, 2, 5, 2, 7, 4, 4, 4, 2, 2, 6, 2, 1, 4, 1, 2, 1, 2, 2, 3, 1, 5, 4, 7]  
data3 = [1, 8, 1, 3, 2, 2, 1, 1, 1, 1, 1, 2, 6, 1, 1, 10, 1, 1, 2, 1, 1, 5, 1, 7, 5, 1, 1, 1, 6, 3, 3, 1, 1, 5, 3, 1, 9, 1, 3, 1]
data4 = [3, 2, 2, 1, 1, 2, 3, 1, 1, 4, 2, 1, 1, 1, 2, 1, 2, 3, 2, 3, 3, 3, 2, 1, 4, 5, 1, 2, 1, 1, 3, 5, 1, 1, 2, 1, 2, 2, 1, 1] 

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
ax.set_xticklabels(['RT', 'RPT', 'DRT', 'D-DRT'])

plt.show()
