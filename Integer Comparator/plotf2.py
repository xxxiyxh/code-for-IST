import matplotlib.pyplot as plt
import statistics


data1 = [13, 18, 16, 22, 4, 1, 20, 3, 10, 23, 1, 18, 1, 3, 5, 12, 33, 2, 22, 6, 24, 4, 25, 10, 28, 48, 10, 9, 14, 9, 47, 3, 14, 3, 1, 3, 1, 8, 3, 41, 15, 1, 7, 4, 26, 3, 9, 1, 53, 4, 6, 59, 47, 4, 5, 57, 7, 15, 19, 2, 3, 3, 2, 6, 23, 9, 30, 37, 18, 8, 3, 4, 6, 24, 38, 7, 14, 2, 16, 9]   
data4 = [15, 5, 3, 16, 7, 21, 4, 2, 12, 2, 2, 15, 6, 7, 9, 2, 3, 8, 3, 5, 4, 7, 7, 5, 7, 1, 1, 1, 4, 6, 4, 8, 1, 1, 1, 4, 3, 2, 2, 14, 13, 5, 26, 3, 4, 12, 9, 1, 1, 1, 3, 2, 4, 5, 7, 2, 1, 3, 2, 6, 5, 6, 7, 5, 3, 4, 12, 4, 13, 2, 2, 12, 11, 13, 6, 8, 7, 2, 10, 9]  
data2 = [1, 19, 14, 22, 17, 47, 7, 30, 54, 15, 22, 12, 3, 3, 1, 6, 1, 12, 1, 23, 6, 17, 6, 2, 15, 17, 2, 1, 10, 11, 17, 13, 47, 16, 7, 16, 9, 27, 9, 5, 3, 26, 16, 5, 1, 32, 8, 49, 2, 8, 5, 6, 3, 3, 16, 5, 1, 1, 14, 55, 25, 6, 22, 10, 3, 8, 13, 25, 3, 22, 13, 1, 39, 1, 13, 15, 14, 25, 38, 28]
data3 = [3, 19, 21, 5, 13, 8, 8, 6, 32, 1, 8, 18, 10, 4, 13, 16, 7, 8, 5, 14, 4, 6, 15, 1, 3, 12, 3, 5, 3, 14, 21, 14, 14, 26, 1, 17, 2, 5, 3, 1, 7, 2, 5, 13, 22, 26, 6, 6, 1, 8, 12, 30, 4, 2, 11, 2, 9, 25, 1, 12, 22, 17, 14, 9, 7, 4, 17, 11, 26, 9, 7, 3, 3, 2, 23, 15, 1, 5, 6, 21] 


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
