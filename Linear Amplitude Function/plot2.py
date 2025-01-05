import matplotlib.pyplot as plt
import statistics

# 数据部分
data1 = [0.4957364341085271, 0.5041579406631762, 0.48983532934131735, 0.45694128787878785, 0.4819295900178253, 0.4619747474747474, 0.4758918128654971, 0.4485055865921788, 0.487287037037037, 0.4692708333333333, 0.461239837398374, 0.4812957610789981, 0.485332422586521, 0.4479968944099378, 0.5149423480083856, 0.4989907407407407, 0.4697061657032755, 0.4912254901960784, 0.4679255319148936, 0.440510101010101, 0.4672619047619047, 0.4659319526627219, 0.4848443223443223, 0.498826164874552, 0.4602914110429448, 0.4894496855345911, 0.4938450292397659, 0.5055068728522335, 0.4739880952380952, 0.4891945996275604, 0.5241865079365079, 0.4716711711711711, 0.4635848126232742, 0.5144444444444444, 0.4528395061728395, 0.4773007246376811, 0.4794292929292929, 0.4978333333333333, 0.5006290322580645, 0.4731687898089171, 0.5055607966457022, 0.4715435606060606, 0.4718248945147679, 0.4940581854043392, 0.5124904214559386, 0.4972916666666666, 0.4969139194139193, 0.4970164609053497, 0.4684451219512195, 0.4820580110497237, 0.5195944741532975, 0.4933870967741935, 0.5054761904761903, 0.4698559670781893, 0.4727504816955684, 0.4647604166666666, 0.5106051587301587, 0.5148535353535352, 0.4902600849256899, 0.4890226337448559, 0.4763666666666666, 0.487581799591002, 0.4706470588235294, 0.4724056603773585, 0.4948314606741572, 0.4947565543071161, 0.4800047619047619, 0.5081060606060605, 0.4845467836257309, 0.4618431372549019, 0.4492197452229299, 0.502940251572327, 0.5368981481481481, 0.4884259259259258, 0.4637770562770562, 0.4881589147286821, 0.4714102564102564, 0.5154727095516568, 0.4563235294117646, 0.4697083333333333] # 第一段数据
data2 = [0.49136904761904765, 0.4440238095238095, 0.4545424836601307, 0.4492171717171717, 0.4900490196078431, 0.5227873563218389, 0.4554591836734693, 0.4641993464052287, 0.5030492424242423, 0.4960815602836878, 0.4794753086419752, 0.4016830065359476, 0.4437380952380952, 0.5019542772861355, 0.4353178694158074, 0.4660460992907801, 0.4716590214067278, 0.5102304964539006, 0.5119736842105264, 0.4845471014492754, 0.5049311926605505, 0.47750000000000004, 0.5215378006872852, 0.48453900709219856, 0.5028436426116839, 0.4854166666666667, 0.46543269230769236, 0.5105166666666666, 0.47911666666666664, 0.4987462462462463, 0.47284798534798534, 0.5053235294117647, 0.4642017543859649, 0.46800200803212856, 0.48928571428571433, 0.4827040816326531, 0.48374595469255667, 0.46896417445482864, 0.4858918128654971, 0.45661003236245957, 0.5037886597938145, 0.4975673400673401, 0.5416358024691358, 0.43957446808510637, 0.5106746031746031, 0.499656862745098, 0.49700191570881226, 0.49095098039215686, 0.5167124542124543, 0.5236214953271028, 0.48869528619528625, 0.48377450980392157, 0.4747222222222223, 0.5140686274509804, 0.5024826388888889, 0.48189068100358424, 0.47765151515151517, 0.4995132013201321, 0.5421315789473684, 0.48356481481481485, 0.5047982456140351, 0.4958676975945017, 0.4707936507936508, 0.5200076452599388, 0.5183823529411765, 0.489513201320132, 0.4606325301204819, 0.5100471698113208, 0.467139175257732, 0.41963058419243993, 0.47671768707483, 0.4888194444444445, 0.4911458333333333, 0.4920454545454546, 0.5166929824561404, 0.48343939393939396, 0.46874213836477986, 0.46816666666666674, 0.48979591836734694, 0.46633141762452107] # 第二段数据
data3 = [0.5300833333333334, 0.5343987341772153, 0.47111111111111115, 0.48405660377358495, 0.48090707964601775, 0.47737987987987995, 0.5037534435261708, 0.5043672839506174, 0.5035062893081762, 0.46874316939890714, 0.5196726190476191, 0.4880657492354741, 0.5349839743589744, 0.5342105263157895, 0.4607188295165394, 0.5119444444444444, 0.4671296296296297, 0.5413888888888889, 0.5483636363636364, 0.4815350877192983, 0.48013157894736846, 0.5192937853107346, 0.5023370927318296, 0.5112155963302752, 0.4948299319727891, 0.47551932367149763, 0.5114047619047619, 0.47071678321678323, 0.4877941176470588, 0.4475904392764858, 0.4986728395061728, 0.47024193548387094, 0.5327621722846442, 0.4893863049095607, 0.4694219219219219, 0.49806047197640124, 0.5377586206896552, 0.4860752688172043, 0.42973456790123454, 0.42086206896551726, 0.5094373219373219, 0.5278306878306879, 0.4615, 0.4819012944983819, 0.507577519379845, 0.4380284552845529, 0.5525333333333334, 0.4873540145985402, 0.47827485380116963, 0.4737426900584796, 0.5077836879432625, 0.47956790123456794, 0.46945454545454546, 0.4698394495412844, 0.44069940476190483, 0.48056010928961745, 0.5053061224489795, 0.46179663608562693, 0.4876127819548872, 0.5500993883792049, 0.47691358024691355, 0.4472012578616352, 0.5169619422572179, 0.42381746031746037, 0.4836983471074381, 0.4686827956989248, 0.5424694189602447, 0.4958472222222222, 0.48154530744336577, 0.47737356321839086, 0.5571604938271605, 0.5143571428571428, 0.49835978835978834, 0.5096311475409837, 0.48785168195718653, 0.5407013201320132, 0.48069327731092437, 0.5418333333333333, 0.4629239766081872, 0.5299542124542125]
data4 = [0.5550629139072848,
 0.5105906862745098,
 0.5430198135198135,
 0.5092486772486773,
 0.5411666666666667,
 0.5359666666666667,
 0.5119146981627297,
 0.4987307692307693,
 0.5056111111111111,
 0.5165910973084886,
 0.5027428940568476,
 0.5102098765432099,
 0.5071095238095238,
 0.5229871794871795,
 0.49575570776255706,
 0.5254810874704492,
 0.5101349206349207,
 0.5064483568075118,
 0.4920438596491228,
 0.49872916666666667,
 0.49746551724137933,
 0.4941808510638298,
 0.5367635135135135,
 0.4983807785888078,
 0.5536880341880343,
 0.514351598173516,
 0.49726960784313734,
 0.5495694444444444,
 0.5289020356234096,
 0.49341891891891904,
 0.5280402298850575,
 0.5526756756756757,
 0.49890740740740747,
 0.5403690476190476,
 0.5310705128205129,
 0.5356538461538461,
 0.5112380952380953,
 0.5802671957671958,
 0.5369468085106383,
 0.546047619047619]  # 第四段数据

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
ax.set_yticks([0.4, 0.45, 0.5, 0.55, 0.6])

plt.tight_layout()

# 关闭坐标轴的网格线
ax.grid(False)

plt.show()
