import matplotlib.pyplot as plt
import statistics

# 数据部分
data1 = [0.546578631452581, 0.6101183330475047, 0.6059736938253562, 0.614, 0.5400353825740822, 0.5777478991596638, 0.5144604376404027, 0.5768084553408992, 0.6131874531991014, 0.5521189120809614, 0.618351856871781, 0.4465224387627391, 0.49134363422788474, 0.568172268907563, 0.6420079610791685, 0.6364116780732911, 0.5274807795458609, 0.5979426253259925, 0.5788235294117647, 0.6138424600609474, 0.5068415244885833, 0.6199602421613807, 0.5140496648097441, 0.5969549109966568, 0.5857685009487665, 0.6338060224089637, 0.5786262331019365, 0.5784313725490196, 0.5658172946597995, 0.5310291858678955, 0.5838603482630165, 0.7090470230645449, 0.5555683325961964, 0.5728466386554623, 0.6245751633986928, 0.5931446262715612, 0.5594024276377217, 0.5890231092436975, 0.6078031212484993, 0.5695592522723375, 0.5916331750091341, 0.6211834733893558, 0.5663865546218487, 0.6195378151260504, 0.6567778626602156, 0.5324250912486206, 0.5427521008403362, 0.5994604157452454, 0.587823700908935, 0.5860718755587342]
data2 = [0.6121388888888889, 0.575828125, 0.5766621621621623, 0.5548385416666668, 0.5780000000000001, 0.663154970760234, 0.5388790849673203, 0.6210277777777778, 0.6254848484848485, 0.5782005649717515, 0.4950630630630631, 0.5666717171717173, 0.5677407407407408, 0.5750000000000001, 0.4808076923076923, 
0.51075, 0.5887288557213931, 0.6312777777777778, 0.5619576271186442, 0.5964883040935673, 0.6032152777777778, 0.560546511627907, 0.5768333333333334, 0.5570537634408603, 0.5758071895424838, 0.5565833333333334, 0.5661944444444446, 0.5615000000000001, 0.5076617647058824, 0.6159550264550265, 0.6312708333333333, 0.5255277777777778, 0.5447651515151516, 0.6043870056497176, 0.5437820512820514, 0.5796543209876545, 0.589437106918239, 0.5511919191919192, 0.5584473684210527, 0.5703695652173913, 0.5048508771929825, 0.6709722222222223, 0.6007573099415205, 0.5986056910569106, 0.5266857923497269, 0.6283141025641027, 0.549956989247312, 0.5639298245614036, 0.5292058823529413, 0.6235112994350284, 0.5356607142857144, 0.48988690476190483, 0.5556587700406797, 0.6316052631578949, 0.548686046511628, 0.4690454545454546, 0.583413043478261, 0.6042126436781611, 0.5670730994152048, 0.6071149425287358, 0.5797678571428572, 0.5543697916666668, 0.5724239766081872, 0.6796724137931035, 0.5808513513513515, 0.6364387755102042, 0.5455937500000001, 0.6149074074074075, 0.5897040816326532, 0.6145490196078432, 0.6475246913580247, 0.5535123456790124, 0.593493710691824, 0.5899093567251462, 0.5770520833333334, 0.5422575757575758, 0.5110217391304348, 0.5800434782608697, 0.5838703703703704, 0.5041666666666668]  # 第四段数据
data3 = [0.5575862068965518, 0.5824354281065691, 0.5458333333333334, 0.5844022415278118, 0.600484949832776, 0.5168213572854291, 0.6115340382118346, 0.5717702169625247, 0.6033641975308642, 0.6134944751381216, 0.5654096045197741, 0.602128514056225, 0.5713995726495728, 0.5675316455696203, 0.5812474747474748, 0.5417096870853132, 0.626162767244857, 0.5516354166666667, 0.5019863731656184, 0.6618709836875927, 0.6151525423728814, 0.5508701657458565, 0.5367708333333334, 0.5673301486199577, 0.5626495726495727, 0.5432855626326965, 0.5182246376811595, 0.5765625000000001, 0.5434510357815443, 0.5669632768361583, 0.5839513108614233, 0.5582352941176472, 0.571686507936508, 0.5650730994152048, 0.5347009243047356, 0.5528934817170112, 0.5516325536062379, 0.5534756097560977, 0.5780959595959597, 0.5911094674556213]
data4 = [0.5513367036260682, 0.5567787657009214, 0.6087632494858409, 0.5830620907106476, 0.5378686125613036, 0.5825286330507216, 0.5969291415412837, 0.5746665875065555, 0.5899075149673845, 0.5814157527417748, 0.6027220838522209, 0.5840155755658312, 0.5523627947118591, 0.5887814062596457, 0.5576456964130178, 0.5611328767850507, 0.5304658067158067, 0.5710278840896665, 0.5950868523510033, 0.6005360776789349, 0.5569593466128967, 0.6079287406795505, 0.5502523112480739, 0.6046916811491029, 0.6071419637273296, 0.5951566599783917, 0.5754159592529712, 0.5692023928215354, 0.6165845626975764, 0.577622089721749, 0.6173619562767636, 0.5890903945208581, 0.5518233498262975, 0.6027813812733449, 0.5596776239081965, 0.5941144076257738, 0.5943005885977775, 0.5972471353493582, 0.5913160648874936, 0.602863610639502]
data5 = [0.5538368818294469, 0.5109775185499649, 0.5756273764258555, 0.5597461517688361, 0.5605041057245052, 0.5905267175572521, 0.5246576151121605, 0.5720850978019763, 0.6074048949824042, 0.5728718517345162, 0.5925008117410222, 0.5884481991996443, 0.6222897196261683, 0.5831031621940714, 0.5818308202968013, 0.5764208555379519, 0.5912764142897755, 0.6337820304342616, 0.588208405407137, 0.5635976789168279, 0.607063449281796, 0.5750253367939687, 0.6039598664324487, 0.5598263043199591, 0.6094971788914704, 0.5914224137931035, 0.5711673447882212, 0.5357060255629945, 0.644734993614304, 0.5944206679046188, 0.5593254774481918, 0.6407300085419542, 0.545018817567061, 0.5982928818425003, 0.6035198443703857, 0.5933620689655174, 0.5728254875636973, 0.5418233115852584, 0.5804156862745099, 0.6371338383838385]

data6 = [0.5998627002288329, 0.6532300884955753, 0.6378514739229024, 0.6306795422031474, 0.5689443436176649, 0.5997619599659944, 0.6405744712764362, 0.6193159173380897, 0.5588274104063579, 0.6071218587008061, 0.6180010204660129, 0.6363381966036834, 0.5958973884623686, 0.603006703751248, 0.6319258006866737, 0.5630695850377204, 0.5817080139321508, 0.6038656166344094, 0.6201184585395112, 0.5909688636004425, 0.5570115658224499, 0.6322519433013261, 0.6211756282126653, 0.6338330606042897, 0.651165033680343, 0.5648888663204016, 0.6044162234855431, 0.571815373330136, 0.6361180707198406, 0.6090976896488995, 0.5840402404347982, 0.6302549167815275, 0.6025019069412663, 0.6120739178177195, 0.5777463451680274, 0.5979923558444685, 0.5946808571592277, 0.6320490110596118, 0.577658145176339, 0.6171151992743353]
# 计算方差
variance1 = statistics.variance(data1)
variance2 = statistics.variance(data2)
variance3 = statistics.variance(data3)
#variance4 = statistics.variance(data4)

# 打印方差值
print("Data1 Variance:", variance1)
print("Data2 Variance:", variance2)
print("Data3 Variance:", variance3)
#print("Data4 Variance:", variance4)

# 创建箱线图，设置图形大小为6x9英寸
fig, ax = plt.subplots(figsize=(9,6))

# 绘制箱线图，设置patch_artist=True以允许填充箱体颜色
bp = ax.boxplot([data1, data2, data3, data4, data5, data6], patch_artist=True, medianprops=dict(color='black', linewidth=2))

# 统一设置每个箱体的颜色
uniform_color = '#7A378B'  # 选择统一颜色
for patch in bp['boxes']:
    patch.set_facecolor(uniform_color)

# 设置x轴和y轴的标签，增大字体大小
#ax.set_xticklabels(['RT', 'RPT', 'DRT', 'D-DRT'], fontsize=16)
ax.tick_params(axis='y', labelsize=20)  # 增大y轴字体大小

# 设置y轴的具体刻度值
ax.set_yticks([0.45,0.5,0.55,0.6,0.65,0.6,0.65,0.7])

plt.ylabel('APFD', fontsize=24)
plt.tick_params(axis='both', which='major', labelsize=20)
plt.xticks(rotation=45)
plt.xlabel('m', fontsize=24)
plt.tight_layout()

# 计算平均值
means = [statistics.mean(data1), statistics.mean(data2), statistics.mean(data3), statistics.mean(data4), statistics.mean(data5), statistics.mean(data6)]
mean_of_all = statistics.mean(means)
ax.axhline(y=0.50919018573, color='black', linestyle='--')

print(mean_of_all)

# 关闭坐标轴的网格线
ax.grid(False)

plt.show()
