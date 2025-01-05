import matplotlib.pyplot as plt
import statistics

# 数据部分
data1 = [0.46343023255813953, 0.4990355805243446, 0.5058720930232558, 0.5058666666666667, 0.5217528735632184, 0.5038419913419914, 0.5182113821138211, 0.5313068181818182, 0.5087407407407408, 0.514, 0.5298408239700375, 0.4872491039426523, 0.4676666666666667, 0.4889604810996564, 0.5032575757575758, 0.5148484848484849, 0.5103333333333334, 0.49442028985507247, 0.49060975609756097, 0.5005381944444445, 0.5202887788778878, 0.5174456521739131, 0.48302434456928844, 0.5075354609929078, 0.5007958801498128, 0.5485861423220973, 0.5001851851851852, 0.5436702127659575, 0.4752946127946128, 0.5297631578947369, 0.5013825757575757, 0.4906395348837209, 0.5080494505494505, 0.49699799196787153, 0.5152721088435374, 0.5242543859649124, 0.4639191419141915, 0.5125000000000001, 0.48802083333333335, 0.4905149812734083, 0.4485590277777778, 0.46373015873015877, 0.4676190476190476, 0.5032303370786517, 0.5216477272727272, 0.4898863636363636, 0.5182865168539327, 0.5614057239057239, 0.557204641350211, 0.46687293729372936, 0.4976807228915663, 0.46038530465949823, 0.5169252873563218, 0.5009782608695653, 0.4927145214521452, 0.46576388888888887, 0.46950757575757573, 0.5082482993197279, 0.521358695652174, 0.5237234042553192, 0.5360077519379846, 0.5254746835443038, 0.49688202247191016, 0.5301470588235294, 0.4995454545454545, 0.5018869731800767, 0.5179938271604939, 0.4734219858156029, 0.5260326086956523, 0.531510989010989, 0.5013945578231292, 0.5503205128205129, 0.5248859649122807, 0.5243371212121212, 0.5246535580524344, 0.4627356902356903, 0.500177304964539, 0.4985984848484849, 0.48818100358422944, 0.48067647058823526]  # 第一段数据
data2 = [0.5148287671232877, 0.5290986394557823, 0.5502777777777778, 0.46480769230769237, 0.47100694444444446, 0.4698, 0.47558333333333336, 0.4565476190476191, 0.5028900709219858, 0.5432692307692307, 0.46853825136612026, 0.41488095238095235, 0.5414772727272728, 0.5034322033898305, 0.47409574468085103, 0.5028409090909091, 0.4919535519125683, 0.5091279069767441, 0.5481720430107527, 0.48622023809523807, 0.602427536231884, 0.4817424242424243, 0.4778174603174603, 0.45411375661375664, 0.4734294871794872, 0.5064516129032258, 0.4662847222222223, 0.4953385416666667, 0.50687106918239, 0.5185493827160493, 0.5112272727272728, 0.4347321428571429, 0.54625, 0.51875, 0.5260128205128206, 0.5345987654320988, 0.40329710144927533, 0.5138611111111112, 0.5446014492753624, 0.5472043010752689]  # 第二段数据
data3 = [0.5251101555449382, 0.5682692307692307, 0.542433647260274, 0.5578910120311394, 0.5065439672801636, 0.5744704570791528, 0.49892371003482117, 0.4730564759276818, 0.5846370226117061, 0.5978605935127674, 0.601839229687331, 0.47777777777777775, 0.6087286324786325, 0.4900123635972693, 0.46533713200379867, 0.6361575622445188, 0.46380153738644303, 0.6066346153846154, 0.6016804888694893, 0.5571026722925457, 0.569017094017094, 0.6473290598290597, 0.6055905357415194, 0.4970294311443004, 0.5962962962962963, 0.5513097431336424, 0.5746998059881496, 0.5932371794871795, 0.6108853410740203, 0.5014157621519585, 0.4803902596355426, 0.586595530073791, 0.6108839121497349, 0.6008119658119658, 0.6213991769547325, 0.603116002094058, 0.60550986400043, 0.5858895705521472, 0.5750285807610649, 0.5008667999659662]  # 第三段数据
data4 = [0.5652797935816803, 0.6424871575342466, 0.651161516546132, 0.6318845111528038, 0.6242409941796445, 0.6322791595197256, 0.59413352970054, 0.6393534002229655, 0.5825747863247863, 0.5975526888570366, 0.6431119605032649, 0.5438602185437629, 0.635042735042735, 0.5910418695228822, 0.6063372941421722, 0.5908424908424909, 0.6141651031894935, 0.6404610204610204, 0.5659508547008547, 0.5867034512604132, 0.6380665799175884, 0.6055315664085765, 0.570159563075605, 0.6618630314832846, 0.6043162393162393, 0.6402240271805489, 0.6170231340026189, 0.5653765521690051, 0.5965290806754222, 0.64, 0.6363174182139699, 0.5732813080639168, 0.6017459624618071, 0.5963917525773196, 0.5755982905982906, 0.569066591397616, 0.6519395623330748, 0.595497849637977, 0.6013325539354183, 0.6188517980970811]  # 第四段数据

# 计算方差
variance1 = statistics.variance(data1)
variance2 = statistics.variance(data2)
variance3 = statistics.variance(data3)
variance4 = statistics.variance(data4)

# 打印方差值
print("Data1 Variance:", variance1)
print("Data2 Variance:", variance2)
print("Data3 Variance:", variance3)
print("Data4 Variance:", variance4)

mean1 = statistics.mean(data1)
mean2 = statistics.mean(data2)
mean3 = statistics.mean(data3)
mean4 = statistics.mean(data4)

# 打印平均值
print("Data1 Mean:", mean1)
print("Data2 Mean:", mean2)
print("Data3 Mean:", mean3)
print("Data4 Mean:", mean4)

# 创建箱线图，设置图形大小为6x9英寸
fig, ax = plt.subplots(figsize=(7,9))

# 绘制箱线图，设置patch_artist=True以允许填充箱体颜色
bp = ax.boxplot([data1, data2, data3, data4], patch_artist=True, medianprops=dict(color='black', linewidth=2))

# 自定义每个箱体的颜色
colors = ['#FF9999', '#FFFF99', '#99FF99', '#99CCFF']
for patch, color in zip(bp['boxes'], colors):
    patch.set_facecolor(color)

# 设置x轴和y轴的标签，增大字体大小
ax.set_xticklabels(['RT', 'RPT', 'DRT', '$Q_{D-DRT}$'], fontsize=28)
ax.tick_params(axis='y', labelsize=28)  # 增大y轴字体大小

# 设置y轴的具体刻度值
ax.set_yticks([0.4,0.45,0.5,0.55,0.6,0.65])

plt.tight_layout()
# 关闭坐标轴的网格线
ax.grid(False)

plt.show()
