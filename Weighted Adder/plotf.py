import matplotlib.pyplot as plt
import statistics


data1 = [6, 9, 24, 6, 6, 9, 6, 7, 6, 11, 10, 8, 6, 6, 10, 7, 9, 10, 6, 9, 16, 6, 7, 10, 6, 8, 16, 9, 10, 13, 13, 7, 7, 6, 7, 10, 6, 8, 8, 7, 6, 19, 7, 7, 15, 6, 8, 15, 11, 7, 6, 9, 9, 10, 6, 7, 8, 7, 6, 6, 7, 10, 10, 8, 6, 6, 6, 6, 7, 11, 6, 6, 11, 7, 6, 6, 7, 8, 9, 8]   
data2 = [6, 17, 8, 12, 3, 1, 4, 3, 5, 11, 1, 5, 6, 19, 2, 1, 9, 10, 7, 6, 3, 2, 15, 5, 4, 5, 1, 9, 8, 6, 1, 9, 1, 5, 2, 2, 1, 5, 13, 5, 13, 10, 7, 10, 4, 4, 32, 2, 6, 2, 8, 9, 2, 2, 1, 10, 7, 5, 4, 3, 3, 15, 6, 6, 21, 11, 3, 10, 48, 1, 4, 16, 10, 31, 57, 5, 9, 10, 1, 10]  
data3 = [1, 2, 13, 30, 7, 7, 8, 5, 1, 6, 2, 6, 1, 4, 2, 8, 3, 17, 6, 2, 5, 10, 2, 9, 13, 3, 4, 3, 3, 1, 3, 3, 4, 19, 1, 10, 19, 2, 3, 4, 2, 5, 7, 23, 4, 2, 7, 9, 13, 4, 11, 20, 1, 7, 20, 5, 1, 2, 26, 2, 8, 4, 10, 4, 4, 19, 7, 10, 4, 4, 5, 2, 7, 2, 18, 10, 1, 7, 4, 10] 
data4 = [1, 6, 8, 1, 3, 17, 8, 6, 7, 4, 1, 3, 1, 2, 1, 6, 2, 1, 11, 3, 5, 1, 6, 4, 2, 8, 2, 1, 1, 1, 8, 6, 11, 5, 12, 4, 1, 1, 7, 13, 4, 6, 1, 21, 6, 4, 5, 13, 8, 18, 21, 6, 7, 7, 9, 11, 9, 9, 12, 3, 7, 1, 13, 4, 2, 11, 2, 20, 8, 9, 6, 14, 2, 5, 3, 1, 1, 5, 3, 3]  


variance1 = statistics.variance(data1)
variance2 = statistics.variance(data2)
variance3 = statistics.variance(data3)
variance4 = statistics.variance(data4)


print("Data1 Variance:", variance1)
print("Data2 Variance:", variance2)
print("Data3 Variance:", variance3)
print("Data4 Variance:", variance4)


fig, ax = plt.subplots()
ax.boxplot([data1, data2, data3, data4])


ax.set_title('boxplot')
ax.set_xticklabels(['rt', 'rpt', 'drt', 'ddrt'])

plt.show()
