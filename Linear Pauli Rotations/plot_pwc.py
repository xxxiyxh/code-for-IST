import matplotlib.pyplot as plt
import statistics



data1 = [0.5681175595238096, 0.5385788690476191, 0.5727351313969572, 0.5459388185654009, 0.5597317596566523, 0.5615676567656765, 0.5477601969057666, 0.5175868878357031, 0.5406818181818183, 0.510425608011445, 0.542085289514867, 0.5127448657187994, 0.502443365695793, 0.5558962264150944, 0.49960210210210215, 0.529673579109063, 0.569221183800623, 0.5275789889415482, 0.5020896147403686, 0.5366630276564774, 0.5336383928571429, 0.542183908045977, 0.4993945868945869, 0.5556505847953217, 0.506325561312608, 0.5235451977401131, 0.4987687687687688, 0.5122945205479452, 0.5057232704402517, 0.535982142857143, 0.5109272300469484, 0.5329263565891473, 0.5521347031963472, 0.5629814814814815, 0.5280957767722474, 0.5607152777777779, 0.5285328638497653, 0.5266528925619836, 0.5205223285486444, 0.5171238938053098]  # 第一段数据
data2 = [0.5250350877192983, 0.5503894927536233, 0.5347685185185186, 0.5694895287958116, 0.5600138121546961, 0.5453130511463845, 0.5301498127340825, 0.5547687609075044, 0.5339907407407408, 0.5321862745098039, 0.5677626811594204, 0.5220764272559854, 0.528575, 0.5300044091710759, 0.520911306042885, 0.5331296296296297, 0.5692364746945899, 0.5080656565656566, 0.528249063670412, 0.5294223484848486, 0.5311929824561404, 0.5061172161172162, 0.5093825561312608, 0.5504693486590039, 0.5195977011494254, 0.5560677083333334, 0.5227285714285714, 0.5204493891797557, 0.5193032786885247, 0.5504864636209815, 0.5367992424242425, 0.5537154696132597, 0.5520878136200718, 0.5473028673835126, 0.5079213483146068, 0.5548217726396918, 0.5421254681647941, 0.5453747795414462, 0.5514019607843138, 0.5227264492753624]  # 第二段数据
data3 = [0.5239271457085829, 0.5291475095785441, 0.5626332476269646, 0.5429761904761906, 0.5716818181818183, 0.5162869822485208, 0.5306439393939395, 0.5098550724637682, 0.5301070763500931, 0.5270652173913044, 0.5452467411545624, 0.5568975903614458, 0.5658063063063064, 0.5214341085271318, 0.5345769230769232, 0.5253373015873016, 0.5506065088757397, 0.5240476190476191, 0.5593627450980393, 0.5403654970760234, 0.5478468208092486, 0.5274712643678161, 0.5296105072463768, 0.5531914893617021, 0.5574709302325581, 0.5423158914728683, 0.5296714285714286, 0.5347659176029963, 0.5291756756756757, 0.5457666666666667, 0.5376329787234043, 0.5264558232931728, 0.5396696252465484, 0.5296640488656196, 0.5402482269503547, 0.5478639846743295, 0.5308868092691623, 0.5753160919540231, 0.5331007751937985, 0.5826275045537341]  # 第三段数据
data4 = [0.5416812015503877, 0.5396550855991944, 0.5598265895953758, 0.5333359293873313, 0.5462620228814418, 0.5144692603266091, 0.5379754901960785, 0.5268628950050969, 0.5222751710654937, 0.5512391304347827, 0.5509749455337691, 0.5284472049689442, 0.5476830443159924, 0.5215729783037476, 0.5401928640308583, 0.5244838872104733, 0.514625382262997, 0.5383185404339251, 0.5563377843719091, 0.5478352769679301, 0.537233935742972, 0.5528007135575944, 0.52608934169279, 0.5167042042042043, 0.5448607038123168, 0.544974437627812, 0.5298885658914729, 0.5449785100286534, 0.5244203980099503, 0.5320288753799393, 0.5558726647000983, 0.546796914349336, 0.5368957703927493, 0.5380245098039216, 0.5428181818181819, 0.5408231707317074, 0.5130387713997987, 0.5398639960435213, 0.5275337186897882, 0.5352678571428572]  # 第四段数据
data5 = [0.516347857788204, 0.5633099906629319, 0.5136619047619048, 0.5528723207344612, 0.5663729155067738, 0.5127457757296466, 0.6007768821814441, 0.5609469153515065, 0.5844847885678337, 0.6142155996465581, 0.5325892032205551, 0.5438966697790227, 0.5184646612268096, 0.5465582361977049, 0.5382331394096099, 0.5862518110692554, 0.5695563465560898, 0.5774136321195146, 0.49468579234972676, 0.5524082998128161, 0.5717424056333416, 0.5416515837104073, 0.5858162590879049, 0.6093102612181561, 0.5267727809946517, 0.5313885554221688, 0.5003913197601837, 0.5306072468905568, 0.5761236107346165, 0.5947820988860661, 0.5981184668989548, 0.5915029612793379, 0.5921926548397137, 0.5254767822622006, 0.5945784156359173, 0.5276242833582031, 0.5015740596222881, 0.5553532182103611, 0.5288448844884488, 0.5732246580475924]
data6 = [0.5305268199233717, 0.521783875904285, 0.5037380952380953, 0.5203603555697358, 0.524232868405094, 0.50246336996337, 0.5193622448979592, 0.5150829283344905, 0.5030759162303665, 0.5142613636363637, 0.5041880007817081, 0.5226029962546817, 0.5655185185185186, 0.509676684881603, 0.5343528368794327, 0.5523767426045563, 0.5237963420662383, 0.5233865248226951, 0.5088240740740742, 0.5184834827056244, 0.530743512974052, 0.4976429344744033, 0.5234943181818182, 0.5227898550724638, 0.531437908496732, 0.5368838383838385, 0.5391088631984586, 0.52853550295858, 0.5186834319526628, 0.4867254901960784, 0.5445993031358886, 0.49294736842105263, 0.49252645502645503, 0.5474734042553192, 0.5309867075664623, 0.543531746031746, 0.5273369565217392, 0.4809090909090909, 0.4936942645910823, 0.5711688311688312]
data7 = [0.5305268199233717, 0.521783875904285, 0.5037380952380953, 0.5203603555697358, 0.524232868405094, 0.50246336996337, 0.5193622448979592, 0.5150829283344905, 0.5030759162303665, 0.5142613636363637, 0.5041880007817081, 0.5226029962546817, 0.5655185185185186, 0.509676684881603, 0.5343528368794327, 0.5523767426045563, 0.5237963420662383, 0.5233865248226951, 0.5088240740740742, 0.5184834827056244, 0.530743512974052, 0.4976429344744033, 0.5234943181818182, 0.5227898550724638, 0.531437908496732, 0.5368838383838385, 0.5391088631984586, 0.52853550295858, 0.5186834319526628, 0.4867254901960784, 0.5445993031358886, 0.49294736842105263, 0.49252645502645503, 0.5474734042553192, 0.5309867075664623, 0.543531746031746, 0.5273369565217392, 0.4809090909090909, 0.4936942645910823, 0.5711688311688312]
data8 = [0.529510752688172, 0.559258691206544, 0.5453131634819534, 0.5194556840077071, 0.5542634408602151, 0.5686238095238095, 0.5138777777777779, 0.5492013888888889, 0.5355042462845011, 0.5190113871635611, 0.5514781746031746, 0.5653739316239317, 0.5562200736648252, 0.5226884920634921, 0.5285635964912281, 0.5449683544303797, 0.5271138211382115, 0.5324472573839663, 0.5563008130081301, 0.5190320910973085, 0.5655327868852459, 0.5354273504273505, 0.5007068965517242, 0.5304588014981274, 0.5193181818181819, 0.5742763157894738, 0.5267356687898089, 0.5597530864197532, 0.5467110453648916, 0.5500980392156863, 0.5329791666666667, 0.5607549019607844, 0.502371794871795, 0.5571820809248555, 0.5108157894736842, 0.5145422535211268, 0.5286546184738956, 0.5558557046979866, 0.532190170940171, 0.5747843822843823]
data9 = [0.5645199843260188, 0.539120670995671, 0.5409693762028756, 0.5628981461073153, 0.56003339777594, 0.5407619047619048, 0.5312610837438424, 0.5517774481410845, 0.5532872707945787, 0.5442272747288234, 0.546299321282044, 0.5401729163578874, 0.5535208711433757, 0.5252768963891953, 0.5682565571963853, 0.5566936830729934, 0.5458863305782712, 0.5240626320484529, 0.5294237288135593, 0.5424420024420025, 0.5207704839962904, 0.5149059737214868, 0.5629745084477819, 0.5358439882968186, 0.555875024816359, 0.5221658788139235, 0.5307084955795558, 0.5684890838604366, 0.5482612578134967, 0.545123376309817, 0.5313334890920243, 0.5492162043802805, 0.5453066591528131, 0.5381454005934718, 0.5655203019791879, 0.5467017338788234, 0.532709762850608, 0.528394258802422, 0.5622625816933131, 0.5583815601168423]
data10 = [0.528809809638141, 0.5183090701069161, 0.502945019222955, 0.5548413463746155, 0.49470365137205324, 0.5334722297775119, 0.4927838721695575, 0.57885262050657, 0.5229761792378615, 0.5545433047590895, 0.5076159337093795, 0.5158294069072716, 0.49608097784568367, 0.5437085256637867, 0.5582184885155183, 0.5559714965749449, 0.4659715025906736, 0.5345888635828163, 0.4597740583241272, 0.4507226495828272, 0.5523404917522565, 0.5264589453584019, 0.5157307589165997, 0.5533596295661122, 0.5473625780587464, 0.46101373066711776, 0.4927792792792793, 0.4949091627172196, 0.5221716922062943, 0.4718162908727847, 0.5696535173241339, 0.4892757102841136, 0.5294285714285715, 0.4709459459459459, 0.49215744328819605, 0.508386825241664, 0.4842410714285715, 0.5488666835314951, 0.5087720249390079, 0.5028776683087028]



'''
variance1 = statistics.variance(data1)
variance2 = statistics.variance(data2)
variance3 = statistics.variance(data3)
variance4 = statistics.variance(data4)


print("Data1 Variance:", variance1)
print("Data2 Variance:", variance2)
print("Data3 Variance:", variance3)
print("Data4 Variance:", variance4)
'''


fig, ax = plt.subplots(figsize=(9,6))


bp = ax.boxplot([data1, data2, data3, data4, data5, data6, data7, data8, data9, data10], patch_artist=True, medianprops=dict(color='black', linewidth=2))


uniform_color = '#8B8B00'  
for patch in bp['boxes']:
    patch.set_facecolor(uniform_color)


#ax.set_xticklabels(['RT', 'RPT', 'DRT', 'D-DRT'], fontsize=16)
ax.tick_params(axis='y', labelsize=20) 


ax.set_yticks([0.46,0.5,0.55,0.6])


plt.ylabel('APFD', fontsize=24)
plt.tick_params(axis='both', which='major', labelsize=20)
plt.xticks(rotation=45)
plt.xlabel('m', fontsize=24)
plt.tight_layout()



means = [statistics.mean(data1), statistics.mean(data2), statistics.mean(data3), statistics.mean(data4), statistics.mean(data5), statistics.mean(data6), statistics.mean(data7), statistics.mean(data8), statistics.mean(data9),  statistics.mean(data10)]
mean_of_all = statistics.mean(means)
ax.axhline(y=0.5121312749, color='black', linestyle='--')

print(mean_of_all)


ax.grid(False)

plt.show()
