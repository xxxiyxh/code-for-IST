import matplotlib.pyplot as plt
import statistics


data1 = [0.527793609671848, 0.5189019607843137, 0.5105490196078432, 0.4849101307189543, 0.5269065040650407, 0.453936170212766, 0.49593243243243246, 0.48046875, 0.4704736842105264, 0.5279954954954955, 0.49815377532228367, 0.5038492063492064, 0.5181169429097606, 0.524457671957672, 0.49919257340241796, 
0.5074723756906078, 0.4818164794007491, 0.49618866328257194, 0.5043010752688172, 0.48400837988826817, 0.4765524534686971, 0.466436936936937, 0.5235085470085471, 0.5204912280701754, 0.5088761467889908, 0.496011586452763, 0.48162568306010933, 0.4897393162393162, 0.5146604938271605, 0.4821576576576577, 0.4888661202185792, 0.5035555555555556, 0.5419850187265918, 0.4694460500963391, 0.5028743315508021, 0.4960752688172043, 0.525719696969697, 0.489247311827957, 0.49497697974217314, 0.48960526315789477] # 第一段数据
data2 = [0.4886688311688312, 0.505412568306011, 0.5343074324324325, 0.5015635451505017, 0.4806587301587302, 0.5137445175438596, 0.4960096700796359, 0.48684735706580373, 0.4960868392664509, 0.49623903508771927, 0.5142956989247313, 0.4913927738927739, 0.47575854700854703, 0.5109662236987819, 0.5126770833333333, 0.4941122004357299, 0.5177277432712216, 0.5065011037527595, 0.5066111111111111, 0.5093192488262911, 0.5020382882882882, 0.5120858585858586, 0.48677868852459016, 0.4946153846153847, 0.4928387096774194, 0.5225709219858156, 0.5084361471861473, 0.5122578828828829, 0.49521867612293147, 0.49023462783171523, 0.49936396677050887, 0.49727366255144034, 0.5094795037756202, 0.486005376344086, 0.491052927927928, 0.5197241183162685, 0.4813219326818675, 0.513738425925926, 0.5092901234567901, 0.5012965921192759]  # 第二段数据
data3 = [0.5955915999346297, 0.5927357411341723, 0.5786161847817184, 0.5737667342799189, 0.5850792613172087, 0.591276683087028, 0.5701088285644411, 0.5668123876450399, 0.5990153619872528, 0.5927901548038332, 0.6036852426867134, 0.5591027945742768, 0.5955336617405582, 0.5608546973544106, 0.5750405679513184, 0.5673884621670207, 0.5738642910048555, 0.5675232881189737, 0.5655766238021132, 0.5992316784869975, 0.5873170136629797, 0.5870402981407159, 0.5849616858237547, 0.5857342799188641, 0.5881694790902421, 0.5909198113207548, 0.5911001642036124, 0.576418439716312, 0.5848842422760251, 0.5855004504873453, 0.5759230644111906, 0.580233843885658, 0.5538628899835796, 0.5965763546798029, 0.577195836044242, 0.5779844006568144, 0.5780059791956753, 0.5798178038640254, 0.5849117502859944, 0.5724402869487242]  # 第三段数据
data4 = [0.5879453681710214, 0.6054283725120813, 0.5865961522784706, 0.5967651888341543, 0.5812718052738337, 0.5801724137931035, 0.5883477692433403, 0.585026148063409, 0.6077011494252873, 0.5942782487038103, 0.5873950436129453, 0.6011656143759105, 0.5931933322438306, 0.6014560303580267, 0.5989993478438086, 0.6050294165713351, 0.5949671592775041, 0.5961676744566105, 0.6113008661546004, 0.6021011657291921, 0.5897690305790501, 0.6051621754443444, 0.592379962501019, 0.5974260210320371, 0.5820689655172413, 0.5904597701149426, 0.5948992546482104, 0.5895326033665631, 0.5869619784379887, 0.6042980295566502, 0.5825731637727236, 0.5994622331691297, 0.5945714053350684, 0.5994762370587756, 0.6006900647063642, 0.5915240074997962, 0.6104837391730675, 0.5961422928154061, 0.600321484151036, 0.5813422189614412]  # 第四段数据


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
