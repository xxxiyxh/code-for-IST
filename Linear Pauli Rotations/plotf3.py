import matplotlib.pyplot as plt
import statistics


data1 = [1, 4, 4, 2, 1, 2, 4, 1, 4, 10, 2, 1, 2, 13, 1, 3, 2, 3, 3, 6, 3, 5, 13, 9, 7, 2, 4, 4, 18, 1, 3, 1, 1, 1, 1, 2, 1, 2, 1, 5] 
data2 = [3, 2, 1, 1, 1, 4, 1, 3, 4, 1, 1, 2, 1, 3, 3, 3, 1, 1, 1, 1, 4, 1, 1, 2, 1, 1, 3, 1, 1, 1, 5, 1, 1, 3, 3, 3, 3, 1, 5, 4]  
data3 = [3, 1, 2, 1, 1, 2, 2, 1, 5, 3, 2, 3, 2, 1, 1, 1, 3, 2, 2, 3, 1, 1, 2, 1, 2, 2, 1, 2, 1, 1, 3, 5, 1, 2, 1, 1, 3, 1, 2, 4]  
data4 = [1, 1, 3, 1, 2, 2, 1, 1, 1, 2, 1, 3, 1, 2, 1, 1, 1, 1, 2, 1, 2, 3, 4, 3, 1, 2, 1, 2, 1, 1, 7, 1, 3, 1, 1, 2, 1, 2, 1, 1] 


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
