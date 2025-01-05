import matplotlib.pyplot as plt
import statistics


data1 = [0.4814481707317073, 0.47966496865203756, 0.516183774834437, 0.49965568862275445, 0.48279807692307686, 0.5312194625407166, 0.48976362179487176, 0.5024695121951219, 0.5038717532467533, 0.4780676229508196, 0.4982313829787234, 0.49500599041533544, 0.49712970219435737, 0.4864666905444126, 0.519625822368421, 0.4956289808917197, 0.5150870743034056, 0.47817338709677415, 0.49231121700879765, 0.5001577476038338, 0.48814786585365855, 0.4941272189349112, 0.498103813559322, 0.4949733231707317, 0.4739301470588235, 0.4801673728813559, 0.5134739263803682, 0.5019020061728395, 0.4875436930091185, 0.4764816978193146, 0.5276386778115502, 0.4799939710610932, 0.4853966346153846, 0.5073573151125402, 0.5007379283489096, 0.5142761075949367, 0.5054944029850746, 0.5278088662790698, 0.48467499999999997, 0.5024301242236024, 0.49497140522875815, 0.48286309523809523, 0.5112220670391061, 0.5068117088607594, 0.472687125748503, 0.525921052631579, 0.5038020833333333, 0.5168562874251497, 0.49937087458745877, 0.47282720588235294, 0.49339312688821746, 0.47930855481727574, 0.5014003164556963, 0.49547142857142856, 0.5104089506172839, 0.4959981884057971, 0.500580223880597, 0.5171344339622642, 
0.48107085987261144, 0.5316635196374623, 0.513849921630094, 0.49486321548821544, 0.49731048387096777, 0.48712009803921563, 0.4996478013029316, 0.4811601681957186, 0.4974723451327433, 0.5030345911949685, 0.5068201013513514, 0.4821594551282051, 0.5006568471337579, 0.5015337423312883, 0.4696458333333333, 0.5032612179487179, 0.5250877192982456, 0.5022287735849057, 0.502766167192429, 0.5147629310344827, 0.49355574324324325, 0.49133207070707074] # 第一段数据
data2 = [0.5146641791044776, 0.4764703237410072, 0.4961860236220472, 0.5199295774647887, 0.5424563953488372, 0.5184330985915493, 0.4847916666666666, 0.49313454198473283, 0.4825674460431655, 0.46875, 0.5193924825174825, 0.5425253378378379, 0.4804115853658536, 0.42260964912280696, 0.4799181034482759, 0.4891843220338983, 0.4789375, 0.4846607142857142, 0.515986328125, 0.48272977941176465, 0.5065576923076923, 0.476640037593985, 0.48924726277372266, 0.5079039115646259, 0.5241826923076923, 0.487383064516129, 0.5201194852941177, 0.5101288167938931, 0.5198641304347825, 0.4853219696969697, 0.525295, 0.5499017857142857, 0.5254021317829457, 0.5048982558139535, 0.5444303797468354, 0.5169052419354839, 0.522594696969697, 0.5076188016528925, 0.5029528985507247, 0.5104619565217391, 0.500066056910569, 0.48170405982905984, 0.525, 0.506968984962406, 0.4664617768595041, 0.5049253731343283, 0.4999094202898551, 0.49118371212121215, 0.541734022556391, 0.5565688775510204, 0.5275833333333333, 0.48768668831168827, 0.510531462585034, 0.5136607142857142, 0.5088505244755245, 0.4595055970149253, 0.48770047169811315, 0.4632657284768211, 0.44365, 0.5287451550387597, 0.5192757936507936, 0.45116346153846154, 0.5241560218978102, 0.5243562030075187, 0.46396098726114643, 0.46066694630872485, 0.5023403284671533, 0.5377403846153846, 0.5179675925925925, 0.5115234375000001, 0.5200138888888889, 0.4965742481203007, 0.45022685185185185, 0.5215178571428571, 0.507294776119403, 0.5141495901639345, 0.5164130434782609, 0.5010140728476821, 0.5201005244755245, 0.4957510504201681]  # 第二段数据
data3 = [0.5857314295677569, 0.5892890506351075, 0.5776327754429943, 0.5769346714329696, 0.5825589912510629, 0.58136951434947, 0.5809827052232313, 0.5641340403221824, 0.5748195902391152, 0.5891009524730455, 0.5707966121445174, 0.5733004314085395, 0.5613532435810042, 0.5750410745091596, 0.5727233429778708, 0.5821633698923607, 0.5702935548960184, 0.5660289452815226, 0.5722645850796595, 0.56520794334886, 0.5701678812923417, 0.5743930873148665, 0.5556962169035833, 0.570295973285519, 0.5585851087902022, 0.5753634189693398, 0.5759135139832896, 0.5784641784641784, 0.5714823518825805, 0.5629586053337381, 0.5760740137021735, 0.5742492422050725, 0.5938400746750356, 0.564934554927928, 0.5683801504319222, 0.5707031326914368, 0.5767541622633247, 0.5675997723315924, 0.5786732042578158, 0.5675801676054146, 0.5672259669229553, 0.5610252187234239, 0.5860689779703863, 0.5628408787393163, 0.5702484351995788, 0.5712333649723689, 0.5764932755268319, 0.5750726691374173, 0.5637234949619422, 0.5730139375511275]
data4 = [0.5645205479452, 0.512786791232387, 0.529240451388889, 0.5284571428571428, 0.5513725490196076, 0.5263656195462478, 0.5074185946872323, 0.5040719696969698, 0.5056927083333334, 0.5791292735042736, 0.5615488656195462, 0.567402329749104, 0.6116689008042896, 0.5072236614853195, 0.4984758203799655, 0.500769230769235, 0.5166141141141141, 0.5677213374287918, 0.5499920634920635, 0.6045668425681618, 0.5141187739463601, 0.5619818652849741, 0.5148330837765117, 0.5164775051124745, 0.503705612829324, 0.5059911792014856, 0.5114070227497528, 0.49881828316615, 0.5134598603839442, 0.5158511586452763, 0.495965447154472, 0.519421661409044, 0.5053954423592494, 0.4933652900688299, 0.5177072310405644, 0.52840395480226, 0.47049684542586756, 0.5008568075117371, 0.5190251141552512, 0.4865979853479854, 0.5469328743111515, 0.5148465533522191, 0.5081476449275363, 0.5066970121381886, 0.4950484764542936, 0.506840077071291, 0.5461045278326384, 0.505851598173516, 0.510170349907919, 0.5096990740740741, 0.49534855650803034, 0.4919535519125683, 0.5031003584229391, 0.5266932624113475, 0.47344607843137254, 0.5636454545454546, 0.546632183908046, 0.5022229791099001, 0.4639856230031949, 0.5675434782608696, 0.5536031175059952, 0.5681899641577062, 0.5786091549295774, 0.5626561538461539, 0.5694202412868633]  # 第四段数据


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



fig, ax = plt.subplots(figsize=(7,9))


bp = ax.boxplot([data1, data2, data3, data4], patch_artist=True, medianprops=dict(color='black', linewidth=2))


colors = ['#FF9999', '#FFFF99', '#99FF99', '#99CCFF']
for patch, color in zip(bp['boxes'], colors):
    patch.set_facecolor(color)


ax.set_xticklabels(['RT', 'RPT', 'DRT', '$Q_{D-DRT}$'], fontsize=28)
ax.tick_params(axis='y', labelsize=28)  


ax.set_yticks([0.45, 0.5, 0.55, 0.6])

plt.tight_layout()


ax.grid(False)

plt.show()
