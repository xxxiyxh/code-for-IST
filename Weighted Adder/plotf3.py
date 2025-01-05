import matplotlib.pyplot as plt
import statistics


data1 = [7, 5, 2, 12, 5, 6, 4, 42, 9, 7, 49, 26, 8, 8, 5, 39, 11, 6, 17, 10, 1, 8, 12, 30, 16, 1, 17, 21, 2, 9, 1, 30, 14, 1, 16, 12, 3, 38, 25, 4]  
data2 = [11, 1, 1, 1, 2, 1, 6, 4, 7, 52, 7, 2, 4, 6, 5, 8, 3, 16, 23, 31, 34, 5, 3, 15, 21, 3, 2, 3, 9, 7, 24, 12, 1, 16, 20, 58, 10, 43, 10, 1]  
data3 = [3, 10, 3, 10, 13, 55, 2, 10, 2, 11, 5, 6, 2, 3, 7, 6, 7, 1, 21, 13, 5, 21, 4, 15, 31, 14, 6, 8, 8, 3, 1, 3, 11, 1, 4, 2, 43, 3, 11, 17] 
data4 = [3, 1, 13, 2, 3, 3, 6, 1, 6, 1, 8, 14, 9, 11, 2, 6, 5, 1, 11, 3, 8, 1, 5, 13, 1, 1, 3, 2, 12, 1, 6, 18, 7, 1, 4, 7, 1, 6, 11, 1] 

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
