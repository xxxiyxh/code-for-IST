import matplotlib.pyplot as plt
import statistics

# 数据部分
data1 = [0.5068706896551723, 0.5140103857566765, 0.4960718309859155, 0.49101733333333336, 0.495379679144385, 0.5129306784660767, 0.49115263157894734, 0.5005243902439024, 0.5052022471910111, 0.500635359116022, 0.5020675675675674, 0.49721808510638293, 0.5042597765363128, 0.5035976253298152, 0.4852958115183246, 0.48718010752688173, 0.4831016483516483, 0.5011370967741935, 0.4784472361809045, 0.5066516853932583, 0.5136930294906166, 0.5172982195845697, 0.5105948275862069, 0.49026294277929156, 0.5114578651685393, 0.5210718015665796, 0.5044550561797752, 0.49337988826815643, 0.4751141732283464, 0.5005, 0.5014815303430078, 0.5000013623978201, 0.498468660968661, 0.47442243767313025, 0.48651949860724236, 0.5008243967828417, 0.5004251336898395, 0.5060776566757492, 0.49116141732283464, 0.5240951086956521, 0.4972384196185286, 0.4655338983050848, 0.4914083094555874, 0.49414490861618804, 0.5001565096952908, 0.5049747191011236, 0.5070682451253481, 0.5119242424242424, 0.47417486338797815, 0.5192783783783783, 0.5024695290858725, 0.5010734463276836, 0.48537823834196886, 0.4939649122807018, 0.4989779005524862, 0.5061571428571428, 0.5043582887700534, 0.48816312997347483, 0.5066407185628742, 0.4972802197802198, 0.4892513513513514, 0.5091005586592179, 0.4910903307888041, 0.49626781002638526, 0.5006917808219178, 0.5022762803234501, 0.5012989417989417, 0.4820821727019498, 0.508852, 0.5056851851851851, 0.5045550724637681, 0.487216577540107, 0.48629946524064166, 0.48986772486772484, 0.49831318681318676, 0.4799235924932976, 0.5067446808510638, 0.478307486631016, 0.5015681198910081, 0.519519943019943]  # 第一段数据
data2 = [0.49507407407407406, 0.4866060903732809, 0.5104585062240663, 0.4838890020366599, 0.5004098039215685, 0.48952049180327867, 0.503068, 0.5007761904761905, 0.48118958742632617, 0.5082167381974249, 0.5007145748987853, 0.4905285132382892, 0.5168214990138067, 0.5067952755905512, 0.49429843444227, 0.4928162055335968, 0.491009394572025, 0.5015831643002028, 0.497978527607362, 0.5062884615384615, 0.5011159999999999, 0.4972240663900415, 0.49781343283582086, 0.5037874743326488, 0.49814904862579285, 0.5057373225152129, 0.5148877952755905, 0.48170833333333335, 0.5138380566801619, 0.5014387308533916, 0.4977008456659619, 0.48908299595141697, 0.5022210300429184, 0.49838176352705416, 0.4964230769230769, 0.49987804878048786, 0.4977079831932773, 0.4903755020080321, 0.49511181434599155, 0.492732, 0.4932808764940239, 0.5049425887265135, 0.4956730382293763, 0.4937556701030928, 0.4976687242798354, 0.4849843423799583, 0.5008228346456692, 0.5045626262626262, 0.4911072144288577, 0.5047394678492239, 0.5026406844106464, 0.48414543524416137, 0.4997229038854805, 0.5106296660117877, 0.5025881147540983, 0.49689200000000006, 0.5171558044806517, 0.49782258064516133, 0.4958658536585366, 0.4762818930041152, 0.5101285714285714, 0.4949190871369295, 0.5062304687499999, 0.5088161904761904, 0.5143003875968992, 0.4914227722772277, 0.4977264150943396, 0.4784938271604939, 0.49685477582846, 0.5079826883910387, 0.5077604562737642, 0.4994692898272553, 0.48725107296137343, 0.49996848739495797, 0.5071812749003983, 0.4868781676413256, 0.5032972166998011, 0.49012893081761005, 0.4958832335329341, 0.4902853982300885]  # 第二段数据
data3 = [0.5272719315574331, 0.5071741996233522, 0.5051956115779646, 0.5077797731568998, 0.5135382205513784, 0.5098991596638656, 0.5068199490121097, 0.5115965608465609, 0.5272239843305744, 0.5173440593319178, 0.5205592301436703, 0.5137433616430587, 0.5100548564603506, 0.5119591503267974, 0.511919821139465, 0.5082607189383419, 0.5212142423979902, 0.5227909830598907, 0.5100939393939394, 0.500808618504436, 0.5086454664057404, 0.5000495513713507, 0.5162778034837381, 0.5049103010354922, 0.5258915743288466, 0.5077925438216524, 0.5217635941536147, 0.5147403542061987, 0.501784806844698, 0.5131890243902439, 0.5086569390402076, 0.526272786037492, 0.5147998737373738, 0.518126226714462, 0.495070594910034, 0.5152595790609822, 0.5200382601873783, 0.5031949313996249, 0.5239751604345442, 0.518659742548705, 0.5089876956018009, 0.514727457765113, 0.5244516473255969, 0.525099003042077, 0.5065395590142672, 0.5111887412404408, 0.5045345911949686, 0.5019124513618677, 0.5264122984947155, 0.5176129768980764]  # 第三段数据
data4 = [0.5313343812345082, 0.5187898578116368, 0.5140311355311356, 0.5266871104462727, 0.5292698846980652, 0.5413952033368092, 0.5164284970625419, 0.5098255189001396, 0.5176143578271939, 0.5333580916237464, 0.5218280793799002, 0.5306468934622149, 0.5303437630371297, 0.5476349730903598, 0.5229061015710632, 0.514354124748491, 0.5281911419046594, 0.5228716808215293, 0.5243438564615035, 0.5205670057496683, 0.5126046172981829, 0.509807806049249, 0.5232833154277473, 0.5235641611930735, 0.5455598587260991, 0.5214669618280589, 0.5175715619581166, 0.5285552094963859, 0.5610430590840988, 0.5232985656074153, 0.506730404617363, 0.5240933104424566, 0.5205257260799057, 0.5118569954297508, 0.5387364400305577, 0.5159743911624404, 0.5164367991098878, 0.5405088633993744, 0.5142904393073956, 0.5476356487549148, 0.5191798379459118, 0.5237778039411912, 0.5212078918523931, 0.5192172001330653, 0.5130305483449925, 0.5359718538017617, 0.5390048129749138, 0.5288387000818027, 0.522246730816679, 0.5365003986996258]  # 第四段数据

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
ax.set_yticks([0.45,0.48,0.51,0.54,0.57])

plt.tight_layout()
# 关闭坐标轴的网格线
ax.grid(False)

plt.show()
