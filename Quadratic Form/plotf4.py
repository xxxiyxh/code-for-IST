import matplotlib.pyplot as plt
import statistics


data3 = [4, 7, 4, 2, 7, 3, 4, 1, 3, 23, 15, 1, 4, 19, 3, 16, 3, 2, 2, 23, 2, 3, 9, 8, 14, 6, 2, 3, 3, 6, 5, 22, 10, 21, 8, 6, 2, 6, 4, 5]  
data2 = [5, 1, 9, 6, 21, 14, 1, 3, 11, 7, 13, 17, 11, 3, 2, 12, 5, 1, 8, 5, 5, 17, 3, 7, 1, 14, 15, 12, 10, 3, 3, 3, 29, 11, 4, 5, 1, 7, 1, 11]  
data1 = [1, 9, 8, 9, 10, 1, 1, 1, 2, 27, 6, 22, 14, 2, 8, 2, 16, 10, 17, 4, 12, 37, 10, 13, 10, 1, 12, 2, 2, 5, 5, 8, 4, 5, 2, 1, 6, 2, 21, 23] 
data4 = [17, 1, 4, 5, 12, 5, 6, 2, 1, 4, 2, 3, 3, 3, 7, 6, 2, 6, 14, 3, 9, 9, 8, 6, 6, 6, 16, 14, 1, 3, 12, 4, 1, 6, 3, 1, 7, 1, 4, 17]  


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
