import matplotlib.pyplot as plt
import statistics


data1 = [0.4844028520499109, 0.3951571684129823, 0.41988482384823844, 0.41700085065013975, 0.4951618578465869, 0.408068783068783, 0.47551401869158877, 0.4713751438434983, 0.4155660377358491, 0.4795525532069442, 0.44690337224383914, 0.5241748323878288, 0.4383128778164499, 0.42897727272727265, 0.4542990966878555, 0.47579787234042553, 0.5112244897959184, 0.38988428518103774, 0.5686177248677249, 0.4947650663942799, 0.5162679425837321, 0.42690311418685123, 0.4706576463184393, 0.535875451263538, 0.5269914417379856, 0.42057003977021656, 0.5127519539284245, 0.40765602322206096, 0.5223478037503211, 0.4577672101449276, 0.46702548031066904, 0.5624056603773584, 0.3971476510067114, 0.45585026019808633, 0.45329949238578676, 0.4562448075325395, 0.4509232264334305, 0.5133291614518147, 0.48428819444444443, 0.4378600318666503, 0.46776155717761564, 0.5016, 0.38029907084785136, 0.44837287104622875, 0.4045321637426901, 0.665909090909091, 0.4525258112094395, 0.506936272991887, 0.5308420665563522, 0.5577777777777778] # 第一段数据
data2 = [0.5577200577200577, 0.41233766233766234, 0.438597775175644, 0.534831069313828, 0.4451269451269451, 0.4119957395819465, 0.5331041507512095, 0.4015594541910331, 0.5066666666666666, 0.42697329216100555, 0.40587234042553194, 0.535016835016835, 0.5640472078295913, 0.5412422985037093, 0.40472356414385396, 0.5463874190198309, 0.4929208987380732, 0.48642217245240765, 0.5098364279398762, 0.5337311883757135, 0.5955882352941176, 0.5457509157509157, 0.5051207983193278, 0.4946060037523452, 0.5671877142465378, 0.5731068906744582, 0.5908616577221228, 0.6169258373205742, 0.42197986577181207, 0.5779032258064516, 0.47528735632183905, 0.5006950880444857, 0.4216279069767442, 0.3817016317016317, 0.4696348957705748, 0.4813025585972446, 0.5386243386243386, 0.46961789375582474, 0.4893095277456329, 0.60734394124847, 0.44806695615632436, 0.4817073170731707, 0.4792127377266696, 0.4341039450063488, 0.5651139068344101, 0.4768880208333333, 0.5311750599520384, 0.3575949367088608, 0.6578165938864629, 0.40232142857142855]  # 第二段数据
data3 = [0.4586196365857383, 0.6621969696969696, 0.6547201336675021, 0.6151577412513256, 0.5781357224552041, 0.547656713466482, 0.7129812981298129, 0.5584905660377358, 0.4800857843137255, 0.5296174413821473, 0.5692271218587008, 0.4780986372485399, 0.6063880126182966, 0.5120262390670554, 0.5471622273433733, 0.521972920696325, 0.4391574279379158, 0.663472781603222, 0.5733399079552925, 0.49659511472982976, 0.5799307327743347, 0.5994480056980057, 0.4796710117939168, 0.525628306878307, 0.5094985985674245, 0.5783071095571096, 0.5640215355805244, 0.5732292917166868, 0.4506883090199302, 0.5057037557037557, 0.541311824434982, 0.5172909129602044, 0.5570324926153147, 0.5792864943574808, 0.5889487870619946, 0.6771043771043772, 0.5078011611030478, 0.5176040494938132, 0.5548210470085471, 0.5433226495726495, 0.5976018782492035, 0.6310339458112737, 0.5712962962962963, 0.469010989010989, 0.5320163886450102, 0.43555555555555553, 0.5967124427798586, 0.5670937012400428, 0.4658444022770398, 0.5265295970817443]

data4 = [0.5915289256198347, 0.54, 0.37248995983935745, 0.5623427955443765, 0.40427098674521356, 0.5192307692307693, 0.4392712550607287, 0.6499999999999999, 0.46445578231292517, 0.5002723311546841, 0.3875318066157761, 0.538073908174692, 0.47874999999999995, 0.5404191616766467, 0.536875, 0.33759124087591236, 0.42214912280701755, 0.3191142191142191, 0.42204301075268813, 0.5489270386266095, 0.48055555555555557, 0.5195918367346939, 0.3586826347305389, 0.5293650793650794, 0.4778523489932886, 0.48104838709677417, 0.5206481481481481, 0.38690476190476186, 0.5159076731129133, 0.4251179245283019, 
0.44336219336219335, 0.4945054945054945, 0.5533769063180828, 0.6135828877005347, 0.6038123167155425, 0.4557471264367816, 0.4588785046728972, 0.3581504702194358, 0.58780276816609, 0.670164609053498, 0.6503597122302158, 0.5542452830188679, 0.6711130235226621, 0.5487046632124353, 0.5636209813874787, 0.5820381664371435, 0.47514124293785304, 0.42864845434938886, 0.6090301003344482, 0.7400793650793651]  # 第四段数据
data5 = [0.46913956639566395, 0.48535825545171335, 0.498936170212766, 0.6573909961006735, 0.5518013433747201, 0.49261583011583016, 0.6041264589651687, 0.6369412298615837, 0.41985320768394346, 0.46699929971988796, 0.7484809027777778, 0.6969138645785352, 0.5356465680697763, 0.413662486938349, 0.5266825965750697, 0.5646686911933091, 0.5144335511982572, 0.6153125807284939, 0.6109215017064847, 0.4527710355987055, 0.627371273712737, 0.6409704203425013, 0.5179536679536679, 0.5393354769560558, 0.5670546558704453, 0.588998538011696, 0.4848169191919192, 0.5202260559190958, 0.6298238798238798, 0.6263157894736842, 0.4487874097007224, 0.5279073323648596, 0.6899509803921569, 0.4383232016210739, 0.4402726341501852, 0.44001212751212754, 0.5603132499684224, 0.6404494382022472, 0.6404761904761904, 0.3558734939759036, 0.5597750463821893, 0.5390201224846894, 0.6020886615515771, 0.520706819313091, 0.6926594167078596, 0.4944804952636683, 0.5697381362183428, 0.44296796796796795, 0.43644948064211525, 0.5917601604874061]
data6 = [0.6316724738675958, 0.5649643758020976, 0.5934430130187973, 0.6393739424703893, 0.5371164009415109, 0.586334073604061, 0.6240576777131293, 0.5065162066168862, 0.5923686042464322, 0.56859375, 0.6419902912621359, 0.6121277915632753, 0.5748752926804439, 0.5994832041343668, 0.5638128349992756, 0.6064267352185089, 0.46801174818030905, 0.6187155768959187, 0.5604239256678281, 0.4719478737997256, 0.5826617980357593, 0.550402144772118, 0.6064690928552315, 0.6377403846153846, 0.5818324520819563, 0.5844174439535263, 0.6358250825082509, 0.5778536391356225, 0.5990587299482965, 0.6226708894167327, 0.4610226456960125, 0.5137337483977293, 0.5361435897435897, 0.6269791666666666, 0.5498258872342002, 0.5870449884644963, 0.5574774532238524, 0.6695732838589982, 0.5979786636720944, 0.5928970985984755, 0.6452502956247537, 0.5637860082304526, 0.5939966605950212, 0.5935706084959816, 0.5558041398377533, 0.6228477191413239, 0.5311381531853973, 0.6659061097049532, 0.664798393843065, 0.5960919540229884]

data7 = [0.5287383177570094, 0.5689947089947089, 0.45416413988275717, 0.4124360487996851, 0.483270202020202, 0.4909863945578231, 0.44730167676483024, 0.529952300785634, 0.454390243902439, 0.3946531504671039, 0.43532654792196773, 0.46759803921568627, 0.4678362573099415, 0.5554181098466106, 0.4937669376693767, 0.5470485096434834, 0.41520979020979015, 0.5678390304946321, 0.4611510791366906, 0.5066993464052287, 0.45675334055615746, 0.4742979533555449, 0.4375, 0.48689880051240253, 0.4600182426269383, 0.52462792345854, 0.5797794117647059, 0.4177208517815728, 0.4605847520355293, 0.476231884057971, 0.45386029411764706, 0.4759569605789374, 0.49298642533936654, 0.46358629130966955, 0.45716198125836677, 0.5352209944751382, 0.3884477216865192, 0.4587585034013606, 0.4290322580645161, 0.5106660666066607, 0.4886627906976744, 0.42730352303523034, 0.4966887417218543, 0.4796401515151515, 0.45203735144312396, 0.47910965152344465, 0.5975421348314606, 0.5053638059701493, 0.44076399790685505, 0.3864297040169133]
data8 = [0.5018796992481204, 0.41393178893178895, 0.4886545222115692, 0.5798863636363636, 0.4793402777777778, 0.362719298245614, 0.5226381461675579, 0.4350034435261709, 0.46431535269709545, 0.4515262860373092, 0.4600840336134454, 0.5001932740626207, 0.556595744680851, 0.48420517632340293, 0.5300429184549357, 0.5749047820567075, 0.4865996649916248, 0.5164090726615816, 0.5368098159509203, 0.45226648351648346, 0.41858237547892724, 0.46958083832335334, 0.43259710586443256, 0.4929213483146067, 0.3197333333333333, 0.416535742340927, 0.580717137712362, 0.44866126258904443, 0.471257932064203, 0.5038746630727763, 0.48628618113912225, 0.5117442595323363, 0.4801282051282051, 0.4769524959742351, 0.49446356426754445, 0.4159663865546218, 0.4838568935427574, 0.4825147125396107, 0.496561004784689, 0.48554860088365237, 0.5418953687821613, 0.5860633727175081, 0.4181216931216931, 0.4074248120300752, 0.5384542705971277, 0.5507762879322512, 0.45042613636363643, 0.4861861861861862, 0.4710457647531112, 0.48595733189305973]
data9 = [0.4234394637620444, 0.6381158759124087, 0.5865397417121556, 0.4394202898550724, 0.5435483870967741, 0.5880924053142971, 0.534733893557423, 0.5023045267489712, 0.5873922107457594, 0.5939176245210729, 0.53, 0.5203138538557812, 0.46572249589490966, 0.43451845184518456, 0.4914148351648352, 0.6268268597761685, 0.46867924528301885, 0.581472777124951, 0.5996818663838812, 0.4577478824115595, 0.5886206896551724, 0.5293944738389184, 0.6605905942398833, 0.5551496666193786, 0.49481145186695075, 0.5044, 0.5144331243469173, 0.4297235023041474, 0.4647960962007668, 0.5196508427932576, 0.5203161559093763, 0.49777795103695616, 0.5389380530973451, 0.5393447418458388, 0.5044281376518219, 0.5727272727272728, 0.5715041572184429, 0.43852813852813854, 0.5975378787878789, 0.5167859466493169, 0.6359953703703705, 0.4936802606892466, 0.4584257206208426, 0.49645161290322587, 0.43961469969240735, 0.47581775700934575, 0.47375, 0.5547934880916491, 0.4803221288515406, 0.5594460006224712]

data10 = [0.5640967498110355, 0.4847006067000792, 0.5095634095634095, 0.40074309978768574, 0.38921568627450975, 0.5201465201465201, 0.6043514744665548, 0.4903140943877551, 0.4820316554229372, 0.5180084745762712, 0.4178254615200192, 0.5289143480632842, 0.5233842991134524, 0.4318014435115628, 0.4586275238449151, 0.47941919191919197, 0.5847749006124422, 0.5183112366876766, 0.47934635920905944, 0.48479831426851294, 0.48192640692640687, 0.47347972972972974, 0.50438153016515, 0.4943669905647092, 0.5034129692832765, 0.5380447678557304, 0.5069543003122339, 0.5430563978168588, 0.4700083310191614, 
0.45897534668721107, 0.46735407449693167, 0.5067282472345763, 0.47248, 0.5467246907924874, 0.4576261661234124, 0.4432297660145761, 0.5218778908418131, 0.5243386243386243, 0.5851865354235023, 0.46661472069048193]
data11 = [0.4760284331518451, 0.564116985376828, 0.5625726141078837, 0.48933465959328026, 0.525105708245243, 0.5557795698924731, 0.627578373466606, 0.5371287128712872, 0.498, 0.4947643979057591, 0.4888649115235218, 0.4915377176015474, 0.5371647509578543, 0.506811145510836, 0.5619209039548022, 0.5715267595307918, 0.45876409774436094, 0.4443168143529155, 0.6179096638655461, 0.6024787535410764, 0.5557945344129555, 0.45939125114713986, 0.5958227040816326, 0.4801024428684003, 0.47889461626575025, 0.482421875, 0.5964035964035964, 0.46528517478454534, 0.3704594017094017, 0.5138849798292523, 0.6072635135135135, 0.49782703172533677, 0.5012793176972281, 0.5318590704647675, 0.42536002809975415, 0.5000827814569536, 0.5527753496503497, 0.5710608913998744, 0.5863270005757053, 0.5016092693916961]
data12 = [0.48245891276864733, 0.5785340314136126, 0.510948905109489, 0.5532511210762332, 0.5757037037037037, 0.5131221719457013, 0.5270736253494874, 0.48006535947712414, 0.5281250000000001, 0.6192829457364342, 0.5751984126984127, 0.5332383665716999, 0.5525874125874126, 0.5396875793751588, 0.5663534938344098, 0.46106110201854883, 0.48152709359605905, 0.573567101584343, 0.5648148148148149, 0.508387445887446, 0.4324624791550862, 0.5333214962121212, 0.5647988505747127, 0.4472089314194578, 0.51544, 0.4937466307277628, 0.5262978142076502, 0.5455153949129853, 0.47056030389363723, 0.4926964536791127, 0.45625, 0.5149311615280202, 0.49695767195767193, 0.5804839968774395, 0.5930612244897959, 0.554233320327741, 0.5127570945066389, 0.675460760998811, 0.43745454545454543, 0.6307275655101742]

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


fig, ax = plt.subplots(figsize=(9,6))


positions = [1 - 0.25, 1, 1 + 0.25, 2 - 0.25, 2, 2 + 0.25, 3 - 0.25, 3, 3 + 0.25, 4 - 0.25, 4, 4 + 0.25]  
widths = 0.2 
bp = ax.boxplot([data1, data2, data3, data4, data5, data6, data7, data8, data9, data10, data11, data12], patch_artist=True, positions=positions, widths=widths, medianprops=dict(color='black', linewidth=2))


colors = ['#8B8B00', '#8B4726', '#7A378B', '#8B8B00', '#8B4726', '#7A378B', '#8B8B00', '#8B4726', '#7A378B', '#8B8B00', '#8B4726', '#7A378B']
for patch, color in zip(bp['boxes'], colors):
    patch.set_facecolor(color)


plt.ylabel('APFD', fontsize=24)
ax.set_xticklabels(['', 'V1', '','', 'V2', '','', 'V3', '', '', 'V4', ''], fontsize=24)
ax.set_xticks([1, 2, 3, 4])  
ax.tick_params(axis='y', labelsize=20)  


ax.set_yticks([0.3, 0.4, 0.5, 0.6,0.7])


ax.grid(False)

plt.show()