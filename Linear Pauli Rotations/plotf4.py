import matplotlib.pyplot as plt
import statistics


data1 = [4, 1, 10, 17, 3, 2, 40, 19, 7, 3, 24, 36, 27, 20, 7, 5, 4, 10, 3, 13, 2, 49, 2, 3, 5, 9, 26, 21, 10, 22, 4, 21, 15, 1, 37, 11, 4, 8, 19, 30] 
data2 = [5, 4, 17, 18, 24, 10, 43, 11, 26, 27, 4, 12, 2, 13, 12, 3, 38, 1, 6, 18, 5, 11, 45, 15, 27, 9, 10, 25, 19, 20, 13, 11, 11, 4, 1, 27, 18, 5, 28, 16] 
data3 = [22, 6, 3, 72, 4, 2, 3, 11, 3, 14, 6, 14, 18, 3, 2, 8, 24, 5, 3, 3, 8, 22, 2, 2, 13, 5, 20, 14, 7, 45, 30, 9, 10, 6, 25, 7, 36, 6, 41, 9] 
data4 = [9, 6, 23, 6, 7, 25, 3, 20, 6, 4, 4, 6, 27, 1, 2, 30, 4, 13, 6, 12, 14, 14, 19, 7, 13, 9, 16, 6, 13, 8, 5, 4, 31, 2, 13, 16, 3, 3, 3, 30] 


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
