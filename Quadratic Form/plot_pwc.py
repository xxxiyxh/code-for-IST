import matplotlib.pyplot as plt
import statistics

# 数据部分

data1 = [0.470952682148128, 0.5030943785456421, 0.48282954973033987, 0.47782995551161644, 0.49356071840500904, 0.48540626214898774, 0.5133350637552319, 0.502577030812325, 0.4869936034115139, 0.487865915597008, 0.49561157796451916, 0.47936620431305055, 0.48891978609625664, 0.4845980183118024, 0.48003103680496584, 0.4872375805445853, 0.48683252828690526, 0.49848672536743777, 0.498313649784238, 0.5123988056761166, 0.5105175639160258, 0.5048832131277707, 0.47348615916955017, 0.5162988936581827, 0.5069183837918729, 0.5148427186966741, 0.4643931991401211, 0.5031376579408742, 0.5228730908421763, 0.4983993597438976, 0.5120561877887686, 0.48001265022137884, 0.49233686254285103, 0.509513118224389, 0.48421087184873945, 0.4856473023992206, 0.47951119379049334, 0.4707807486631016, 0.4632824558394787, 0.49579244285126634, 0.45744206773618534, 0.48587576206953365, 0.5023975181470437, 0.505966991112992, 0.48676254006757347, 0.49070069204152245, 0.48776670519508913, 0.488403963736032, 0.4752928908789793, 0.508173374613003] # 第一段数据
data2 = [0.513753466872111, 0.5165446170200201, 0.4897475405949982, 0.5022077779606166, 0.48635470400393027, 0.49078615218175264, 0.47353096352964447, 0.4969186310799402, 0.4919782636822357, 0.4756526042311023, 0.47500580450429536, 0.5034886506558065, 0.5058769344141489, 0.4736409290646579, 0.4750385208012326, 0.4747694416749751, 0.472972717535127, 0.46978406417757407, 0.4692653356656011, 0.4599031476997579, 0.4994903190783521, 0.46472376762841244, 0.49995936846993266, 0.5164114552893045, 0.4795823244552058, 0.4865295721227924, 0.488308936825886, 0.4885866593767086, 0.5090344489995717, 0.5255285380607295, 0.4683254747037084, 0.4945272241882411, 0.48130212536992195, 0.5010461290122308, 0.5254428443991335, 0.4725484261501211, 0.4447314682458648, 0.4575940148305085, 0.48991460732306896, 0.5278719397363465, 0.4845146379044684, 0.4428204151590173, 0.49092630533308496, 0.5031136926299753, 0.5176349241748439, 0.523737991800771, 0.47837596302003077, 0.48736571974218185, 0.49803350566062426, 0.4404823989569752]     # 第二段数据
data3 = [0.48856124989269467, 0.5156640358846242, 0.5080233325996037, 0.48487910501623965, 0.4849936555818909, 0.5243041298639294, 0.5038270299898207, 0.5023770454092352, 0.48407688278563454, 0.48071454330019064, 0.5007161125319693, 0.4935697656083331, 0.5187981510015409, 0.4590592334494773, 0.4900891833056342, 0.5061147327249023, 0.5341637737390239, 0.4984725763711814, 0.493325947742441, 0.48243156911887564, 0.4563258636788049, 0.4998472116119175, 0.5048709013147474, 0.5036826140656786, 0.48992467043314497, 0.4693937329700273, 0.5263480097949778, 0.5008161885443833, 0.49225679513828285, 0.4596133535381366, 0.46937102113572704, 0.46911894378113006, 0.4918930899608866, 0.5015071515331797, 0.47391366803131507, 0.5392838847097522, 0.4985994113467979, 0.4983336924513395, 0.5046289702321607, 0.5002720108216198, 0.4948826597131682, 0.4969024809629084, 0.4914064233548474, 0.4821017537449762, 0.4882445032807644, 0.532870198182881, 0.5025308947108256, 0.5009181692976914, 0.5107057852042551, 0.46975231037296805]
data4 = [0.4837655307521782, 0.513905894257526, 0.48885311133799314, 0.4738534396809571, 0.5144689783859431, 0.5125019202212096, 0.5054557924928296, 0.49670550847457623, 0.4808905054559137, 0.5045166177445318, 0.517890160686771, 0.47943520535571965, 0.4770179560328914, 0.4681436243936244, 0.4996265172735761, 0.502023521272916, 0.4883261183261184, 0.45389945451864955, 0.4861452513966481, 0.480854248859789, 0.46400693610777644, 0.49511309277741683, 0.49759687173361206, 0.505149519594084, 0.5198558057171769, 0.5207481915623846, 0.4965939760336823, 0.5134229802705449, 0.485350259641633, 0.4936654428406176, 0.5120116909039065, 0.5038265306122449, 0.4741873164700427, 0.4843751619758461, 0.4942881880673768, 0.5053672777384902, 0.49162389806583096, 0.4806771545827634, 0.5352982192662519, 0.4838204538050047, 0.519518600747279, 0.5050436615477266, 0.5049703649786836, 0.5228764431343651, 0.5074389644437163, 0.4924835240218537, 0.4903975918725699, 0.5051003060183611, 0.49074074074074076, 0.49824271588977476]
data5 = [0.48964578214578214, 0.4948887587822014, 0.4988168238993711, 0.47819547325102885, 0.4758373205741627, 0.49344276094276096, 0.4882068273092369, 0.4998692077727952, 0.4678579676674365, 0.4918420015760442, 0.5124197371256195, 0.476316425120773, 0.4867510288065844, 0.49485202492211844, 0.4939583333333334, 0.4850987361769352, 0.49127192982456147, 0.5010531574740208, 0.48297901821060973, 0.48958633093525183, 0.486484126984127, 0.48126250000000004, 0.5007970137207426, 0.4953777258566978, 0.49587751330898855, 0.48486714975845413, 0.4825737100737101, 0.49448630136986305, 0.49985083532219576, 0.49396464646464644, 0.4958294663573086, 0.48922467130703795, 0.48955098039215683, 0.5008333333333334, 0.4908990147783251, 0.4882170542635659, 0.49809934318555005, 0.48771844660194175, 0.5054000780640125, 0.49376698641087136, 0.47493104806934594, 0.4903577044025157, 0.4905303030303031, 0.4713915662650603, 0.4902701149425287, 0.46763333333333335, 0.48720325203252035, 0.4961868686868687, 0.4835747663551402, 0.49743447993448]
data6 = [0.45103435309981776, 0.4611361348100259, 0.47221366204417053, 0.49946722634807883, 0.46851588092864266, 0.4304617117117117, 0.49064640410958904, 0.444461707304173, 0.527781217750258, 0.5286371100164203, 0.4562985004959449, 0.49281896551724136, 0.4910009496112529, 0.4794320192933711, 0.46552915938344186, 0.496611136874398, 0.45353194678658426, 0.5058895972181976, 0.5004734444246097, 0.5100370262813997, 0.4556573618632365, 0.49858398669517695, 0.43174503726175556, 0.4098867384835413, 0.4275854746230622, 0.45042906628877344, 0.5751040428061831, 0.4324036511156186, 0.4158618198410586, 0.5116332435398583, 0.45425258568110155, 0.466948090090564, 0.48861125276219614, 0.47411255640157923, 0.44155290102389083, 0.4896345894321603, 0.4278133702023251, 0.41109017179586416, 0.5004971562661575, 0.4553637861394558, 0.5041945366160575, 0.4803146107358691, 0.4682291666666667, 0.4630775311697128, 0.5070275236531394, 0.46988648307756997, 0.4562100709291212, 0.45200041352217507, 0.46959984459984466, 0.4448677571201192]
data7 = [0.48602132684922855, 0.5199059962968238, 0.508822311533309, 0.5147403750846442, 0.5005585763717252, 0.504184225619031, 0.5103664995409929, 0.48706480686903353, 0.5053868363364167, 0.480742866252192, 0.4703081232492997, 0.474734555984556, 0.4967457415161908, 0.49944980694980695, 0.4974715986101186, 0.48365403446925187, 0.4840336134453781, 0.48213426157027733, 0.4928207868885835, 0.501134936733314, 0.4947194816380863, 0.4843027098479842, 0.4709988540870894, 0.4853362548457778, 0.4998248313409871, 0.46346347861178366, 0.4727086183310534, 0.5166062197663803, 0.49190563444800733, 0.5033716892137046, 0.5077991398937516, 0.4938867331635204, 0.4894005666285601, 0.4905096185668405, 0.4685854745356356, 0.4846974092736805, 0.49112187247780464, 0.48975659229208923, 0.48553951495127967, 0.4940034327397554, 0.494839255499154, 0.48626086537766966, 0.4762633203415414, 0.49071758784814734, 0.5079062811565305, 0.49737764452514677, 0.48048774166796243, 0.4733956250905403, 0.49231992291014215, 0.45652991742377225]
data8 = [0.5027801774915573, 0.5018478204530141, 0.5087253033798015, 0.4850018480384392, 0.5004931109499637, 0.5232593037214885, 0.4894781864841745, 0.5056805341551105, 0.48959608012389244, 0.47774309088121747, 0.499933532735128, 0.479758660957571, 0.4850560657699612, 0.48312759575449926, 0.5073363804981452, 0.47216754722193444, 0.4721713047825362, 0.4773736313184341, 0.503948088110984, 0.4887878130424002, 0.47063311637756533, 0.48769464675445695, 0.5204355987412357, 0.4829992630803242, 0.47789703315881327, 0.4824765834076717, 0.5026158518663663, 0.5141324454310026, 0.509492317637114, 0.4892009425878321, 0.5170021496970881, 0.48170845574001964, 0.5266509561731404, 0.4866310299869622, 0.4831932773109243, 0.49799593306710443, 0.4936950146627566, 0.4910179640718563, 0.48532345905227264, 0.5162481690730278, 0.47650793650793655, 0.48234784283513094, 0.4707354544553474, 0.45900507848568795, 0.4595767575322812, 0.4929329529977129, 0.5123947512301805, 0.47032502483309846, 0.47229755538579066, 0.5098136105279328]
data9 = [0.5005329457364341, 0.4878736604624929, 0.4929624277456648, 0.45811092161509664, 0.4499501163950781, 0.44162814586543403, 0.48220198675496695, 0.48853037766830865, 0.4902029914529915, 0.4540873015873016, 0.4677743556492139, 0.4310864978902954, 0.44288708740561156, 
0.48487430167597767, 0.47514767932489455, 0.4875694444444445, 0.4876144713836824, 0.45656407035175883, 0.4535988308366825, 0.5286589403973511, 0.45409717186366927, 0.42363258026159334, 0.5148319761961546, 0.43848349729870006, 0.4786625514403292, 0.4845297718419588, 
0.5284302325581395, 0.4862012987012987, 0.4715335305719921, 0.4438507625272331, 0.48036008230452676, 0.44012315270935953, 0.5357279693486591, 0.4764227642276423, 0.4607630522088354, 0.5076911244423935, 0.5105908584169454, 0.547927927927928, 0.5133450704225352, 0.46854856512141285, 0.4888087934560328, 0.485, 0.46592222222222224, 0.5400539777954978, 0.44683908045977017, 0.48729810728724576, 0.509911313518696, 0.4374583333333334, 0.44359881687173325, 0.49201071733041046]
data10 = [0.48784977908689253, 0.46940906483075157, 0.49333600561178476, 0.5434851661266755, 0.45986599392361116, 0.49950540153585843, 0.3715983920161229, 0.46332336380358624, 0.5335103448275862, 0.48569116551493824, 0.548331437239287, 0.478800501202208, 0.6084654731457801, 
0.5520887327458772, 0.5143122505018807, 0.5748984407307403, 0.5477157758080401, 0.5334383622939817, 0.4102233676975945, 0.55004921004921, 0.5154857090340961, 0.5057620388267922, 0.5000449769717905, 0.5139477678337782, 0.49001605718429503, 0.483254572587434, 0.5390535816210045, 0.3951963708675118, 0.5351611480555867, 0.44485638058279336, 0.4293941979522184, 0.4467125645438898, 0.4998193954805525, 0.49815824523432944, 0.5170135076137431, 0.4875313365879404, 0.4192673543432397, 0.409900279218189, 0.5125609235675943, 0.41980257711550223, 0.485550184521025, 0.5347679877223074, 0.4474475383373688, 0.49015927468757664, 0.5323521046643913, 0.48337889557135044, 0.5465401361119331, 0.4692556808400757, 0.45148795639256517, 0.5451796988829529]
data11 = [0.5096551031426167, 0.5541514428641886, 0.5381627271871176, 0.5054000078832233, 0.46409488341968913, 0.535761931988347, 0.46393140589569154, 0.5063359820772219, 0.5957283134983483, 0.4504039400354258, 0.533224701723376, 0.4777910394760205, 0.4908076790038049, 0.47983539094650207, 0.42888145549481926, 0.4509920634920635, 0.4528739675998057, 0.4837374764048207, 0.5065014109445029, 0.5013415629463375, 0.47587474645030425, 0.5557611645694548, 0.5462992889463477, 0.480487400530504, 0.5091201941178931, 0.40669048841157657, 0.5123553240740741, 0.45371084898149167, 0.4936825667234526, 0.4998821681068343, 0.5042405498281787, 0.4625503329719684, 0.4264768835616438, 0.5360834911616161, 0.48045652234133907, 0.5427304964539007, 0.4783620229347301, 0.5768646321387868, 0.4492748488284202, 0.5157643669807208, 0.5698671960251677, 0.42343849224349084, 0.47660195707070707, 0.4204712812960235, 0.5211772630021922, 0.5125328481908227, 0.49487864952541155, 0.4828898222339321, 0.5297094508301405, 0.5428902085476479]
data12 = [0.49576097112297907, 0.5314876383829095, 0.5823305429601209, 0.5215109458076433, 0.3631937710179939, 0.5149726655907527, 0.5706622551992294, 0.5605314909693112, 0.5192648940361103, 0.5024093550212639, 0.48968442013460034, 0.4310475004011061, 0.49051081567508836, 0.5708157512300177, 0.49847034981055605, 0.5527843485117288, 0.47564791133844836, 0.49440430841980826, 0.49387136835766965, 0.44826993749638283, 0.4675988034807832, 0.5159765064489715, 0.6151379067663125, 0.49811779454069843, 0.5934322572445349, 0.5153011633440319, 0.5377092610337636, 0.49299872564523806, 0.47841807867067715, 0.5276419982402972, 0.4836833168737114, 0.4899844646375227, 0.5018932874354561, 0.48793291518952825, 0.5500517280082765, 0.5848039349637928, 0.5632450613079019, 0.47627856602895857, 0.4643612304754109, 0.47325183797799086, 0.5594609783511705, 0.5641613106490233, 0.5261947778207942, 0.4951984005593672, 0.4471337166737844, 0.5356040427173832, 0.4739447934719815, 0.5468339424325711, 0.5886166440863625, 0.4756467038962706]
data13 = [0.49540069686411153, 0.4751814882032668, 0.49034058152309884, 0.4714133734968562, 0.5045662100456622, 0.5145538895196337, 0.5100979990311884, 0.49261474609375, 0.5167132318317376, 0.45061570737936696, 0.51097351287649, 0.4731207239382768, 0.5070211734281558, 0.5246566503825238, 0.5420185486081858, 0.5285162065126287, 0.4900579280614307, 0.4831334074032227, 0.5034472569683837, 0.5175787777512534, 0.522643603946489, 0.44069348673132, 0.5242238726080557, 0.4508071100161851, 0.49542490054131616, 0.48231750918059413, 0.5303673552754435, 0.5002307932499763, 0.522765503389405, 0.497812990773459, 0.4861229213907785, 0.5090187350518204, 0.4966752822144167, 0.49739512012946596, 0.5452325108671857, 0.5472289996514464, 0.4686514886164624, 0.49759162303664917, 0.5158190378388691, 0.5366889003586506, 0.5097456166272656, 0.4998718512009373, 0.5320859794821691, 0.49201977606514463, 0.535657695652692, 0.4918425661351276, 0.5318337337576574, 0.5196726838883701, 0.5277391365854809, 0.5040057417676793]
data14 = [0.49095656498673734, 0.49123029603998464, 0.5201213854955931, 0.45597390464676285, 0.4772385710087737, 0.49786533249947884, 0.5252869573840395, 0.5024089590718659, 0.4971696108784071, 0.5098630338192633, 0.5146662949984071, 0.47719252724442135, 0.513763873485845, 0.49095525896079917, 0.49085015896610096, 0.49930941394356027, 0.4938235512109957, 0.5037071875172909, 0.5234602076124567, 0.5095858714643244, 0.5172616156710377, 0.48630210667861945, 0.5096973258889216, 0.4895031177973521, 0.5260356227755236, 0.4913666580333247, 0.5267379679144385, 0.47763082144047514, 0.5087237668030817, 0.5047928148601756, 0.4869574958392011, 0.47933755929641914, 0.4761984061867897, 0.4929460229677492, 0.47428474627315165, 0.4488088147706968, 0.499543177129384, 0.4672902791289381, 0.4861132611526448, 0.5337584857500903, 0.5343042685705606, 0.5057836278841433, 0.482782225316162, 0.5103778328796102, 0.4904223867445174, 0.4735632183908046, 0.4814514646658757, 0.5339805439745882, 0.5246753550074739, 0.4951494288843686]
data15 = [0.4661654135338346, 0.5249775928297055, 0.5014717101080737, 0.49899730916300805, 0.49302963984364123, 0.4509263517111186, 0.5084494858423899, 0.4906283791901958, 0.4819496929617383, 0.5136756940297634, 0.5164014301498088, 0.5103517877739331, 0.5122487075522585, 0.4798766107833796, 0.5321596273762339, 0.5024703557312252, 0.4696961505190312, 0.4865591825269373, 0.5226278216723491, 0.4915272887323944, 0.4960823960571212, 0.46775395336370945, 0.4975206302975991, 0.5190183830816693, 0.4986796576215626, 0.5029953499216352, 0.513700701097946, 0.5167572204746926, 0.5290027996267164, 0.49667873882758345, 0.5050080207877606, 0.5092412617220802, 0.467858807082945, 0.5299316221084567, 0.4948062601877204, 0.5531073284971726, 0.508398450926923, 0.4788173806107809, 0.47795325150916945, 0.5180155464106081, 0.49648115942028986, 0.49669876600161456, 0.4965577300652353, 0.5169893649501323, 0.48316376306620207, 0.5071622873882761, 0.5060034645170056, 0.5062810290356552, 0.533150321847785, 0.5016687979539642]



# 创建箱线图，设置图形大小为6x9英寸
fig, ax = plt.subplots(figsize=(9,6))

# 绘制箱线图，设置patch_artist=True以允许填充箱体颜色
bp = ax.boxplot([data1, data2, data3, data4, data5, data6, data7, data8, data9, data15], patch_artist=True, medianprops=dict(color='black', linewidth=2))

# 统一设置每个箱体的颜色
uniform_color = '#36648B'  # 选择统一颜色
for patch in bp['boxes']:
    patch.set_facecolor(uniform_color)

# 设置x轴和y轴的标签，增大字体大小
#ax.set_xticklabels(['RT', 'RPT', 'DRT', 'D-DRT'], fontsize=16)
ax.tick_params(axis='y', labelsize=20)  # 增大y轴字体大小

# 设置y轴的具体刻度值
ax.set_yticks([0.4,0.45,0.5,0.55])

plt.ylabel('APFD', fontsize=24)
plt.tick_params(axis='both', which='major', labelsize=20)
plt.xticks(rotation=45)
plt.xlabel('m', fontsize=24)
plt.tight_layout()

# 计算平均值
means = [statistics.mean(data1), statistics.mean(data2), statistics.mean(data3), statistics.mean(data4), statistics.mean(data5), statistics.mean(data6), statistics.mean(data7), statistics.mean(data8), statistics.mean(data9), statistics.mean(data10),
        statistics.mean(data11), statistics.mean(data12), statistics.mean(data13), statistics.mean(data14), statistics.mean(data15)]
mean_of_all = statistics.mean(means)
ax.axhline(y=0.46248581918, color='black', linestyle='--')

print(mean_of_all)

# 关闭坐标轴的网格线
ax.grid(False)

plt.show()
