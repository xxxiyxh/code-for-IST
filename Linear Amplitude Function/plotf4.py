import matplotlib.pyplot as plt
import statistics


data1 = [10, 3, 3, 5, 4, 7, 4, 1, 8, 3, 4, 4, 4, 13, 15, 6, 5, 12, 8, 1, 8, 2, 3, 1, 3, 2, 2, 2, 10, 5, 3, 6, 2, 3, 2, 6, 3, 7, 1, 3] 
data2 = [5, 5, 5, 5, 7, 14, 2, 9, 2, 4, 7, 1, 1, 6, 1, 10, 5, 2, 4, 4, 2, 7, 15, 5, 1, 1, 4, 1, 4, 9, 5, 7, 4, 1, 4, 1, 1, 9, 2, 6]  
data3 = [2, 4, 2, 2, 4, 2, 2, 4, 3, 2, 1, 6, 5, 2, 13, 8, 7, 19, 6, 4, 2, 2, 2, 5, 1, 1, 3, 1, 1, 9, 8, 7, 1, 3, 9, 3, 1, 4, 2, 4]  
data4 = [1, 5, 7, 1, 8, 6, 3, 8, 1, 7, 2, 3, 3, 8, 3, 1, 3, 2, 2, 5, 2, 2, 3, 5, 4, 3, 1, 3, 1, 6, 1, 2, 3, 2, 5, 1, 2, 7, 2, 2] 


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
