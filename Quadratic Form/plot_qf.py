import matplotlib.pyplot as plt
import statistics


data1 = [0.5001905660377358, 0.505371972318339, 0.4769552845528456, 0.5141327272727272, 0.5162940074906366, 0.5116999999999999, 0.49573228346456694, 0.4803416988416988, 0.5029566037735849, 0.5258933823529411, 0.5234007936507936, 0.5164667896678966, 0.5120461538461538, 0.5243315789473684, 0.46884671532846717, 0.5040384615384614, 0.509546875, 0.49589694656488553, 0.5232773851590106, 0.4948198529411764, 0.5314124087591241, 0.5134372693726936, 0.4991705426356589, 0.4877310606060606, 0.48832716049382713, 0.4933538461538462, 0.4972686567164179, 0.5003129770992366, 0.50276171875, 0.4863576512455516, 0.49444531249999996, 0.5026798561151078, 0.4908964285714286, 0.4916867219917012, 0.4574816176470588, 0.4825369003690037, 0.5079597701149425, 0.4959106463878327, 0.4922, 0.5055833333333333, 0.4893266129032258, 0.5100917602996254, 0.4766811594202898, 0.4995456273764259, 0.5165975609756097, 0.5186124497991967, 0.48217669172932326, 0.5006481481481482, 0.4750625, 0.4947129963898917, 0.5210106382978723, 0.4779166666666667, 0.49490659340659343, 0.48494, 0.5041806083650189, 0.5040182186234817, 0.4842551867219917, 0.5361070038910505, 0.5224323308270676, 0.48711627906976745, 0.5122586206896551, 0.5176314878892734, 0.49829704797047975, 0.4971459854014599, 0.5270851851851852, 0.49103225806451617, 0.4932529411764706, 0.5274543859649122, 0.532695652173913, 0.49951052631578946, 0.4959352941176471, 0.4878947368421052, 0.4988319672131148, 0.49473791821561336, 0.49432462686567163, 0.5027352941176471, 0.4751593886462882, 0.5085470085470085, 0.5068111111111111, 0.4983525896414343]  # 第一段数据
data2 = [0.5043676470588234, 0.4953727735368956, 0.4902933673469388, 0.5138921052631578, 0.4967061281337047, 0.4968430079155673, 0.49649232736572885, 0.4918619791666667, 0.5110985401459853, 0.49460025706940874, 0.5144376623376623, 0.4907845528455284, 0.5038349875930521, 0.49735472154963684, 0.4950423340961098, 0.4882838541666667, 0.4862889447236181, 0.493359375, 0.4841876712328767, 0.4946384615384615, 0.5133497409326424, 0.5078727506426735, 0.5201202531645569, 0.497586513994911, 0.5157131147540983, 0.4660890410958904, 0.5058112745098038, 0.5211327683615818, 0.48805080213903745, 0.5123354114713217, 0.5036320754716981, 0.507180904522613, 0.48790983606557375, 0.5039122340425531, 0.5012771883289124, 0.48411658031088084, 0.5107499999999999, 0.5150498721227621, 0.5010271317829457, 0.5075623306233061, 0.482264705882353, 0.5050800524934382, 0.5022388059701492, 0.5055103359173125, 0.5033302387267904, 0.4994390862944162, 0.5194581280788177, 0.49059498680738783, 0.48900000000000005, 0.4998675675675676, 0.4932277227722773, 0.5082486338797814, 0.5039908136482939, 0.5028462532299741, 0.5008073047858941, 0.49249731182795703, 0.4826933174224343, 0.4975716112531969, 0.4963072916666667, 0.5009581280788177, 0.5024299999999999, 0.4894972899728997, 0.499359296482412, 0.507705513784461, 0.5058858267716535, 0.5026194029850746, 0.513124649859944, 0.4949490358126722, 0.5061650246305418, 0.5097398081534772, 0.48773177083333336, 0.49016748166259166, 0.4876911764705882, 0.5133875305623472, 0.5052202970297028, 0.5014199029126213, 0.5115611702127659, 0.4961404199475065, 0.5070259067357512, 0.5250360824742267]  # 第二段数据
data4 = [0.5702126704953338, 0.5888538699786773, 0.5755270961897314, 0.5708000861025957, 0.5770014964459408, 0.5731449548596741, 0.5807894896167586, 0.5661950101384113, 0.5791468655494668, 0.5765414127649031, 0.5699372833158038, 0.5797523276473414, 0.5895810368027733, 0.5852166751816746, 0.5852041271445988, 0.5605914186316197, 0.5860258936110329, 0.5611443340382153, 0.5739308161603123, 0.5727412875587377, 0.5739722709935219, 0.5412499243203972, 0.5682460000916884, 0.5706639256890513, 0.5707168127633685, 0.5794915875853849, 0.5941061853098889, 0.5620349702380952, 0.5771850047784938, 0.5787505827505827, 0.5850150140948646, 0.575813985701863, 0.5843434343434343, 0.574429992466522, 0.5751901545576245, 0.5717073281541046, 0.580550728721489, 0.5735552494643403, 0.5615589023403577, 0.5745605758047881, 0.5845219983710602, 0.5430512555899553, 0.573689824308388, 0.5757301107754279, 0.5729216653839769, 0.5823274266067179, 0.5794861155932568, 0.5884358299433676, 0.5744557185733655, 0.5798132657933653]  # 第三段数据
data3 = [0.546507124588966, 0.5414417422598179, 0.5633646836217931, 0.5261840683986012, 0.5155172413793103, 0.5519895375368691, 0.5576521517697988, 0.5362282330875457, 0.546218487394958, 0.5388499504605335, 0.5536194746957079, 0.5448947720681192, 0.5439900801084765, 0.5636406943729872, 0.5147876849854987, 0.5297525379578583, 0.550652713915755, 0.5282521742321382, 0.5367550941945405, 0.540827517447657, 0.5079677659400693, 0.54700377967781, 0.5175693503207734, 0.5411711854553142, 0.5274497464183912, 0.5435793364965034, 0.5494908978710275, 0.5469676807816402, 0.5260668258626662, 0.5567170868347339, 0.5124170720919947, 0.5471686713901247, 0.5366306867574616, 0.5523236710414503, 0.5383941049421929, 0.5460438004523472, 0.5377558953096657, 0.5400506699495085, 0.5361897390535162, 0.5636767882098843, 0.5393924012558043, 0.5349923685549376, 0.5320689469817778, 0.5423390271141136, 0.4932990437554332, 0.551869656159407, 0.5381039333693567, 0.535250558106612, 0.5358991596638656, 0.5507781587971512]  # 第四段数据


variance1 = statistics.variance(data1)
variance2 = statistics.variance(data2)
variance3 = statistics.variance(data3)
variance4 = statistics.variance(data4)


print("Data1 Variance:", variance1)
print("Data2 Variance:", variance2)
print("Data3 Variance:", variance3)
print("Data4 Variance:", variance4)


fig, ax = plt.subplots(figsize=(7,9))


bp = ax.boxplot([data1, data2, data3, data4], patch_artist=True, medianprops=dict(color='black', linewidth=2))


colors = ['#FF9999', '#FFFF99', '#99FF99', '#99CCFF']
for patch, color in zip(bp['boxes'], colors):
    patch.set_facecolor(color)


ax.set_xticklabels(['RT', 'RPT', 'DRT', '$Q_{D-DRT}$'], fontsize=28)
ax.tick_params(axis='y', labelsize=28)  


ax.set_yticks([0.45,0.5,0.55,0.6])
plt.ylabel('APFD', fontsize=30)
plt.tight_layout()

ax.grid(False)

plt.show()
