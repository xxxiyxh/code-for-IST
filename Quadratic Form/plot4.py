import matplotlib.pyplot as plt
import statistics

# 数据部分
data1 = [0.5584876543209877, 0.5335925925925926, 0.5026360544217687, 0.48457482993197276, 0.530429292929293, 0.519929718875502, 0.5100555555555556, 0.570812757201646, 0.4474259259259259, 0.45820652173913046, 0.5206684981684983, 0.48803571428571435, 0.5029891304347825, 0.4297222222222222, 0.5101907630522088, 0.5669705882352941, 0.4839262820512821, 0.4671274509803922, 0.5390438596491228, 0.5148611111111111, 0.4819097222222223, 0.5127057613168725, 0.4968814432989691, 0.4626418439716312, 0.5094841269841269, 0.49884538152610447, 0.5277941176470589, 0.5537301587301587, 0.5098180076628352, 0.5508720930232559, 0.46063008130081307, 0.5427057613168724, 0.5378909465020577, 0.4859912280701755, 0.47372549019607846, 0.5237770562770563, 0.49107638888888894, 0.5275617283950618, 0.550491967871486, 0.5017798353909465] # 第一段数据
data2 = [0.5362671232876712, 0.4900541125541126, 0.4526004016064257, 0.4924801587301587, 0.5218201754385965, 0.5529292929292929, 0.5448232323232324, 0.5296193415637861, 0.5059415584415584, 0.5238095238095238, 0.5368881856540085, 0.4663571428571429, 0.4987087912087912, 0.4738924050632911, 0.4686111111111111, 0.4634111111111111, 0.5051940639269407, 0.462162447257384, 0.4563805970149254, 0.5198555555555556, 0.4898983739837398, 0.503785140562249, 0.4755722891566265, 0.494212962962963, 0.5453544061302682, 0.4892291666666667, 0.5091458333333333, 0.5738888888888889, 0.45386546184738963, 0.46290404040404043, 0.5227205882352942, 0.4873870056497175, 0.4721581196581197, 0.5096747967479675, 0.46986263736263734, 0.4885389610389611, 0.5283904109589042, 0.4897420634920635, 0.5228065134099616, 0.5444871794871795]  # 第二段数据
data3 = [0.5165226542594439, 0.4787909604519774, 0.534208641680592, 0.4850691347011597, 0.5318300343724073, 0.5038164815897137, 0.5099721383793825, 0.4640225286872302, 0.5152330508474576, 0.4962386812166241, 0.5212304644508035, 0.47702943800178416, 0.48441519413391027, 0.4738828967642527, 0.5242844314737907, 0.43248215878679747, 0.5056344480073294, 0.5177629363564935, 0.5308992185121284, 0.5163120981881941, 0.5164120315111005, 0.5074867753427615, 0.5073880921338549, 0.5132891181527881, 0.5276718455743881, 0.5552179176755448, 0.5363801452784505, 0.5072664983772088, 0.5049329623071086, 0.47766864968009876, 0.5016528428897704, 0.4696253345227475, 0.47817224003664677, 0.5027449099243151, 0.5188377723970945, 0.5134019370460049, 0.5610352396049263, 0.4892912172573189, 0.48815677966101695, 0.5216015219647181, 0.5164836476486035, 0.5371186440677966, 0.4569029275808936, 0.532656433216075, 0.49244022898192835, 0.512216072869826, 0.5175141242937853, 0.4646085552865214, 0.5127987831377663, 0.4602405358773977]  # 第三段数据
data4 = [0.5846543104499451, 0.5694125697441836, 0.5514747963900506, 0.5205653226655438, 0.5880775481773857, 0.5658510384339939, 0.5330301777594048, 0.5560063559322035, 0.5864568714239448, 0.5246176105828855, 0.5402223963946311, 0.5049390046421246, 0.5480835271961892, 0.545099734809178, 0.5805205811138014, 0.55, 0.5261190786614516, 0.5389356774397305, 0.5676142458699851, 0.5363838016152884, 0.509002238567317, 0.5531056531005785, 0.5202582728006457, 0.5815322488909112, 0.5504180790960452, 0.5382829771554901, 0.49946605270892525, 0.54798031056531, 0.5317510658209421, 0.4914153021162501, 0.517489406779661, 0.5054895822087877, 0.5765172225259705, 0.5411069261351747, 0.621292372881356, 0.5864406779661018, 0.5250453043385567, 0.5421520287621984, 0.573381138635376, 0.5411416693316278, 0.4982512001567551, 0.5485427862753205, 0.592813559322034, 0.5351377839271303, 0.5569458291791294, 0.532149065623642, 0.5582600300364728, 0.5893733273862622, 0.5407948568088837, 0.5707131851199648]  # 第四段数据

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