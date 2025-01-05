import matplotlib.pyplot as plt
import statistics


data1 = [0.4985884279475983, 0.5123546255506607, 0.5028861788617885, 0.5023085106382978, 0.5065696202531645, 0.4928591476091476, 0.49119242424242426, 0.48430864197530865, 0.49514255319148937, 0.49158880903490754, 0.5052459266802444, 0.49412202380952375, 0.4928072916666666, 0.49083995815899584, 0.48471015180265653, 0.48280333333333325, 0.4901239224137931, 0.518430412371134, 0.5202808008213552, 0.5157739005736137, 0.5042552966101695, 0.5079814049586776, 0.4960510526315789, 0.5055564516129032, 0.5057625260960333, 0.5161731578947368, 0.491568376068376, 0.4979669811320755, 0.5079303921568626, 0.4918326530612245, 0.4943466029723991, 0.5060358565737052, 0.5067006302521008, 0.5006588114754098, 0.5187407216494845, 0.5236666666666666, 0.4981158280922432, 0.4930804535637149, 0.49816533180778033, 0.5043220430107527, 0.5069908536585366, 0.4864005376344086, 0.4970847193347193, 0.5064223107569721, 0.5071975982532752, 0.48479291845493555, 0.5038763383297644, 0.4722489604989605, 0.49579276315789467, 0.5158917165668663, 0.4848393617021276, 0.49557457983193276, 0.485571961620469, 0.4912809734513274, 0.5006412579957356, 0.5098585011185682, 0.5098281584582441, 0.4813660896130346, 0.5185772921108741, 0.4975649999999999, 0.503414847161572, 0.4795144032921811, 0.5183341995841996, 0.4864427966101694, 0.5170476424361493, 0.4948805732484076, 0.4836829268292683, 0.49456978021978015, 0.48710937499999996, 0.4952839506172839, 0.4950902922755741, 0.4900025987525988, 0.4950084388185654, 0.5105694748358861, 0.5086994949494948, 0.49131673306772905, 0.5179312227074235, 0.5089563829787234, 0.5182714843749999, 0.5051680497925312]  # 第一段数据
data2 = [0.49590523465703973, 0.49547762645914395, 0.5035866141732283, 0.5055890410958904, 0.48238721804511275, 0.5203903846153846, 0.4927295539033457, 0.5057818021201413, 0.5041330508474576, 0.4937558365758754, 0.5101924342105263, 0.5221510989010989, 0.497513440860215, 0.5167499999999999, 0.48628501945525293, 0.49362588652482264, 0.49085374149659866, 0.5155872093023256, 0.5207946096654275, 0.5048131768953069, 0.5211804511278195, 0.5189665492957746, 0.4972463768115942, 0.5076030534351145, 0.5194953874538745, 0.49374414062499994, 0.4756669741697417, 0.4788395522388059, 0.5014673913043478, 0.48891118421052626, 0.49306003584229385, 0.5339577464788733, 0.5131452205882353, 0.5000952830188679, 0.48379198473282436, 0.4720994809688581, 0.5038449152542372, 0.5082276422764228, 0.4839441176470588, 0.5095320512820513, 0.4774253472222222, 0.5066924603174603, 0.5008377551020408, 0.5091975409836066, 0.5279037102473497, 0.5000528169014085, 0.5074523411371238, 0.47224440298507464, 0.5205279783393502, 0.489554347826087, 0.4901084229390681, 0.5164237588652482, 0.513757042253521, 0.49677941176470586, 0.4800472440944882, 0.48282089552238805, 0.4706518518518519, 0.49189315352697094, 0.48951779026217224, 0.5237384615384615, 0.5082333887043189, 0.5147904411764705, 0.5019044117647059, 0.48265074906367034, 0.47120522388059694, 0.5011377952755905, 0.504498, 0.49356886792452825, 0.493960332103321, 0.5031722222222222, 0.4999948979591836, 0.4865104166666666, 0.5071472332015811, 0.5147385496183207, 0.5173645038167939, 0.5134236641221374, 0.4861443396226415, 0.49708152173913045, 0.4853368725868725, 0.4881392988929889]  # 第二段数据
data3 = [0.5300833333333334, 0.5343987341772153, 0.47111111111111115, 0.48405660377358495, 0.48090707964601775, 0.47737987987987995, 0.5037534435261708, 0.5043672839506174, 0.5035062893081762, 0.46874316939890714, 0.5196726190476191, 0.4880657492354741, 0.5349839743589744, 0.5342105263157895, 0.4607188295165394, 0.5119444444444444, 0.4671296296296297, 0.5413888888888889, 0.5483636363636364, 0.4815350877192983, 0.48013157894736846, 0.5192937853107346, 0.5023370927318296, 0.5112155963302752, 0.4948299319727891, 0.47551932367149763, 0.5114047619047619, 0.47071678321678323, 0.4877941176470588, 0.4475904392764858, 0.4986728395061728, 0.47024193548387094, 0.5327621722846442, 0.4893863049095607, 0.4694219219219219, 0.49806047197640124, 0.5377586206896552, 0.4860752688172043, 0.42973456790123454, 0.42086206896551726, 0.5094373219373219, 0.5278306878306879, 0.4615, 0.4819012944983819, 0.507577519379845, 0.4380284552845529, 0.5525333333333334, 0.4873540145985402, 0.47827485380116963, 0.4737426900584796, 0.5077836879432625, 0.47956790123456794, 0.46945454545454546, 0.4698394495412844, 0.44069940476190483, 0.48056010928961745, 0.5053061224489795, 0.46179663608562693, 0.4876127819548872, 0.5500993883792049, 0.47691358024691355, 0.4472012578616352, 0.5169619422572179, 0.42381746031746037, 0.4836983471074381, 0.4686827956989248, 0.5424694189602447, 0.4958472222222222, 0.48154530744336577, 0.47737356321839086, 0.5571604938271605, 0.5143571428571428, 0.49835978835978834, 0.5096311475409837, 0.48785168195718653, 0.5407013201320132, 0.48069327731092437, 0.5418333333333333, 0.4629239766081872, 0.5299542124542125]
data4 = [0.47669330289193307, 0.48270574811011263, 0.5732612895435886, 0.5074800039498372, 0.5171728013132142, 0.5874680028320898, 0.5641643170426065, 0.5050113617919169, 0.4279419170723519, 0.5852531645569621, 0.5546474358974359, 0.445822994210091, 0.4820644469799122, 0.5185607019320003, 0.4385005973715651, 0.5448151592652871, 0.518174133558749, 0.5325013528138528, 0.6390584723918057, 0.5413341645885287, 0.5908568443051201, 0.49727959138352207, 0.5663565290430962, 0.6281047516198703, 0.5241758241758241, 0.49879715260386887, 0.6489914797426535, 0.49916724496877163, 0.5368144252441773, 0.5135149459402162, 0.5602020202020203, 0.4806603900109976, 0.4888680425265791, 0.5527641277641278, 0.5814206569054214, 0.4894783081621554, 0.5187839112998349, 0.47215517241379307, 0.566587708909067, 0.5986213235294118, 0.5381006006006007, 0.5540517534899556, 0.5505319148936171, 0.4895446703957342, 0.49138044191642966, 0.5482929584536211, 0.5364590014395462, 0.572971065631616, 0.5450826805918189, 0.5018452380952381, 0.5512127410870836, 0.5104569743873226, 0.4652633738290064, 0.5245304643596569, 0.6002490932133024, 0.498046875, 0.5717761557177616, 0.646206896551724, 0.5222759193536208, 0.5478960438139947, 0.5373303167420814, 0.5472161572052401, 0.6144811115935735, 0.5254356627354339, 0.5535019455252919, 0.5842763157894737, 0.6148618538324421, 0.6042727272727272, 0.5795743504698729, 0.5795575127334465, 0.5524653447973329, 0.5825804776739356, 0.53874415497662, 0.5622291021671826, 0.5501976758116689, 0.5295424621461488, 0.5197583947583948, 0.48219975490196076, 0.5281117237638977, 0.5611501160230856]  # 第四段数据


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


ax.set_yticks([0.4, 0.45, 0.5, 0.55, 0.6, 0.65])
plt.ylabel('APFD', fontsize=30)
plt.tight_layout()


ax.grid(False)

plt.show()
