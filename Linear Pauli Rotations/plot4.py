import matplotlib.pyplot as plt
import statistics


data1 = [0.5057478632478632, 0.5081, 0.5012500000000001, 0.46773333333333333, 0.5651923076923077, 0.4280284552845529, 0.48654166666666665, 0.5502777777777778, 0.5350675675675676, 0.4995833333333334, 0.4849, 0.48078828828828835, 0.5108333333333334, 0.49880434782608696, 0.4502777777777778, 0.5288750000000001, 0.5719444444444445, 0.49245833333333333, 0.4328409090909091, 0.5211036036036036, 0.5516145833333333, 0.5235, 0.5256904761904763, 0.4842901234567901, 0.5336842105263159, 0.5133888888888889, 0.5018089430894309, 0.5352450980392157, 0.46128048780487807, 0.532625, 0.4687393162393163, 0.47807017543859653, 0.5284803921568627, 0.41888211382113827, 0.4595325203252033, 0.5514189189189189, 0.44218253968253973, 0.513859649122807, 0.4603947368421053, 0.46939922480620155] # 第一段数据
data2 = [0.48034722222222226, 0.4983771929824562, 0.5594259259259259, 0.48573129251700686, 0.5243390804597702, 0.5519444444444445, 0.4197222222222222, 0.5054457364341086, 0.5479421768707483, 0.4900641025641026, 0.5126162790697675, 0.45787037037037037, 0.49710784313725487, 0.49916666666666665, 0.5291260162601626, 0.5682037037037037, 0.5611524822695035, 0.5293217054263566, 0.5152235772357724, 0.4485992907801418, 0.5372660818713451, 0.5530666666666667, 0.46511437908496733, 0.4997348484848485, 0.48213768115942035, 0.44720370370370377, 0.4915404040404041, 0.5371511627906976, 0.49170634920634926, 0.4320833333333334, 0.5792559523809524, 0.43556201550387597, 0.538462962962963, 0.5357795698924731, 0.447962962962963, 0.523563829787234, 0.5583730158730159, 0.49217320261437913, 0.5164772727272727, 0.5142948717948718]  # 第二段数据
data3 = [0.49620486366986, 0.5495291902071564, 0.5295235913879982, 0.5892120934493816, 0.44417833456153283, 0.43453389830508476, 0.48967642526964555, 0.5143260694108152, 0.47118644067796606, 0.5120090946672179, 0.45304314329738055, 0.4435409986257444, 0.5012159174649964, 0.4872881355932203, 0.4965510445407962, 0.5628813559322035, 0.5051617873651773, 0.5442520265291084, 0.5392952720785014, 0.5450693374422189, 0.4906385494678754, 0.4875517890772128, 0.4987583760346866, 0.5346275128104061, 0.509115336916081, 0.543427035965275, 0.6038026944806607, 0.5461755758365928, 0.480343116990492, 0.5298840321141838, 0.5262711864406779, 0.4699354317998386, 0.5222787193973635, 0.5759755616870319, 0.5250723439437784, 0.4861325115562403, 0.4447387005649717, 0.557015065913371, 0.4664164648910411, 0.4537357315807679]  # 第三段数据
data4 = [0.5087089794446449, 0.5433577645442053, 0.5474576271186441, 0.536633281972265, 0.5426685061095783, 0.49187680859859445, 0.6036288570186876, 0.4825047080979284, 0.5557875155022738, 0.5084299732381803, 0.5571112748710392, 0.49402319357716323, 0.46578154425612056, 0.49686809137803983, 0.48216486902927574, 0.5059322033898306, 0.5452459694088467, 0.49822804314329733, 0.5092372881355933, 0.5687680859859446, 0.4254661016949152, 0.5402427851580394, 0.5434463276836159, 0.4786252354048964, 0.43858757062146886, 0.5136064030131827, 0.46682513435303846, 0.5001773748521877, 0.5068952234206472, 0.4510015408320493, 0.5469733656174335, 0.5353352984524687, 0.55, 0.4509745762711865, 0.4903831982313928, 0.5398305084745763, 0.5738559322033898, 0.4786864406779661, 0.5243183492999264, 0.5761726448561293]  # 第四段数据


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