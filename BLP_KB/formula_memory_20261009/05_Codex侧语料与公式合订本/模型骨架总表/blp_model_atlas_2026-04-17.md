# BLP Model Atlas

## 说明
- 这份文件覆盖 `E:\导出的条目.csv` 中全部 `28` 篇 BLP 相关文献。
- 这里说的“BLP 模型”不是都指严格意义上的 Berry-Levinsohn-Pakes 原始汽车模型；其中一部分是标准 BLP 需求-供给框架，一部分是 BLP 风格差异化需求，一部分是沿着 BLP 结构思路扩展出去的政策模型。
- 因为 OCR 对公式块的识别不总是稳定，我同时给出“按文意整理的模型骨架”和“OCR 原文模型片段”。前者便于理解，后者便于回到原文核对。

## 研究方向分布
- 汽车、EV 与交通政策: 21
- 住宅能源、耐用品与绿色采用: 4
- 平台、通信与服务市场结构: 2
- 食品、标签与信息披露: 1

## BLP 类型分布
- 标准 BLP 需求-供给: 14
- BLP 邻近结构政策模型: 10
- BLP 风格差异化需求: 4

## 总表

| Key | 论文 | 研究方向 | BLP 类型 | 如何利用 BLP | 主要改造 |
| --- | --- | --- | --- | --- | --- |
| 3XDZXLTP | Winners and Losers: the Distributional Effects of the French Feebate on the Automobile Market | 法国 feebate、汽车需求与分配效应 | 标准 BLP 需求-供给 | BLP 风格差异化产品需求 | 在汽车需求里加入 municipality / demographic 异质性，再把 feebate 税补规则映射到不同地区与人群的福利分布上。 |
| 5TWRWEP3 | Consumer Valuation of Fuel Costs and Tax Policy: Evidence from the European Car Market | 燃料成本估值、里程异质性与汽车税制 | 标准 BLP 需求-供给 | 带燃料成本与里程异质性的汽车 BLP | 把未来燃料成本显式写进效用，并用里程异质性来解释燃油税为何比产品税更能针对高里程消费者。 |
| 6Q55KN3G | How Much Do Consumers Value Fuel Economy and Performance? Evidence from Technology Adoption | 燃油经济性、性能与技术采用 | BLP 邻近结构政策模型 | 技术采用与均衡属性权衡模型 | 不是标准 share inversion，而是从技术采用与价格均衡里恢复消费者对 fuel economy 与 performance 的权衡。 |
| 99RBFASI | Fiscal Policy and CO2 Emissions of New Passenger Cars in the EU | 欧盟汽车购买税、财政政策与排放强度 | BLP 邻近结构政策模型 | 两类汽车 / 税制比较模型 | 用简化的两类车结构模型说明购买税、年税和未来成本如何共同影响车队构成与排放。 |
| 9HUJHUTJ | Disentangling sources of vehicle emissions reduction in France: 2003-2008 | 法国新车排放下降的来源分解 | 标准 BLP 需求-供给 | BLP 风格差异化产品需求 | 利用差异化汽车需求来分解排放下降是来自税制、柴油化、技术变化还是消费者替代，而不是只看平均排放变化。 |
| 9X84A7QK | Local Protectionism, Market Structure, and Social Welfare: China’s Automobile Market | 中国汽车市场地方保护主义与福利 | 标准 BLP 需求-供给 | 标准 BLP 需求-供给框架 | 在标准汽车 BLP 里加入 province-of-origin / 本地品牌偏好与补贴扭曲，并在供给侧允许全国统一定价和税楔。 |
| B9VX97UN | The impact of car specifications, prices and incentives for battery electric vehicles in Norway: Choices of heterogeneous consumers | 挪威 BEV 需求、属性与激励政策 | BLP 风格差异化需求 | 耐用品离散选择 + 运营成本/政策比较 | 围绕 BEV 的电池续航、充电便利、价格和补贴构造异质消费者选择模型，突出电动车属性本身的需求作用。 |
| BWI7CWGM | The Economics of Attribute-Based Regulation: Theory and Evidence from Fuel Economy Standards | 属性型监管、CAFE 与产品设计扭曲 | 标准 BLP 需求-供给 | 属性型监管与产品属性选择模型 | 不再只估计消费者对现有车型的选择，而是让监管规则 σ(a) 直接扭曲厂商对属性与能耗的联合设计。 |
| F8UTG3XW | Network Externality and Subsidy Structure in Two-Sided Markets: Evidence from Electric Vehicle Incentives | EV 双边市场、充电网络与补贴结构 | 标准 BLP 需求-供给 | EV 需求 + 充电网络部署的双边网络模型 | 把 EV 需求和充电站进入放进同一个双边网络框架，用以比较购车补贴和充电补贴的结构设计。 |
| FMISYR9Z | Fuel taxation, emissions policy, and competitive advantage in the diffusion of European diesel automobiles | 欧洲柴油扩散、燃油税与竞争优势 | 标准 BLP 需求-供给 | 标准 BLP 需求-供给框架 | 在多产品 Bertrand 汽车竞争里强调柴油/汽油发动机的属性、税差和厂商竞争优势如何共同驱动 diesel diffusion。 |
| HUZV45IT | Consumer Myopia in Vehicle Purchases: Evidence from a Natural Experiment | 车辆购买中的短视、自然实验与均衡效果 | BLP 邻近结构政策模型 | 带注意力/短视参数的结构需求 | 利用燃油经济性标签 restatement 的外生冲击识别消费者对未来燃料成本的低估，再看价格与市场均衡如何调整。 |
| I6ZAU5HX | Providing the Spark: Impact of financial incentives on battery electric vehicle adoption | BEV 购车激励与采用响应 | BLP 邻近结构政策模型 | 耐用品离散选择 + 运营成本/政策比较 | 围绕电动车激励的呈现形式、州级政策和技术新颖性来构造 EV 采用需求，而不是只套标准汽车 BLP。 |
| JDV2EEV6 | Better Lucky Than Rich? Welfare Analysis of Automobile Licence Allocations in Beijing and Shanghai | 牌照配置机制与汽车福利比较 | BLP 风格差异化需求 | BLP 风格差异化产品需求 | 把牌照稀缺和牌照获取机制嵌入购车选择，比较摇号、拍卖等牌照制度如何改变车型需求和福利。 |
| LXUZM7VX | What does an electric vehicle replace? | EV 替代关系与减排效果 | 标准 BLP 需求-供给 | 标准 BLP 需求-供给框架 | 把新车与二手车、燃油车与电动车放在统一随机系数效用里，直接回答“EV 到底替代了谁”。 |
| M5CH8LSF | Effectiveness of China's plug-in electric vehicle subsidy | 中国 PEV 补贴有效性与成本效果 | BLP 风格差异化需求 | 耐用品离散选择 + 运营成本/政策比较 | 围绕收入和年行驶里程异质性估计 PEV 选择模型，用以比较补贴拉动销量和减排的性价比。 |
| N5SE78G4 | Optimal policy and network effects for the deployment of zero emission vehicles | 零排放汽车部署的最优政策与网络效应 | BLP 邻近结构政策模型 | EV 需求 + 充电网络部署的双边网络模型 | 把政策设计问题直接放进 EV 与充电基础设施的网络反馈系统里，讨论哪种补贴组合最优。 |
| P5D5GNTW | The Evolution of Market Power in the U.S. Automobile Industry | 美国汽车业市场势力的长期演化 | 标准 BLP 需求-供给 | 标准 BLP 需求-供给框架 | 在标准汽车 BLP 上加入更丰富的 micro moments、second-choice data 和持续产品条件，用来追踪几十年 market power 的演进。 |
| RQSSQUXV | Carbon Taxes, Path Dependency, and Directed Technical Change: Evidence from the Auto Industry | 碳税、路径依赖与汽车定向技术变迁 | BLP 邻近结构政策模型 | 清洁/污染汽车束 + 定向技术变迁 | 把 clean / dirty vehicles、能源投入和创新方向放在同一理论结构里，重点从静态替代扩展到动态 innovation direction。 |
| UHH6VGYR | The Electric Vehicle Transition and the Economics of Banning Gasoline Vehicles | EV 转型与禁售燃油车 | BLP 邻近结构政策模型 | EV 转型/禁燃模型 | 通过校准 EV 与燃油车的替代弹性和转型路径，讨论 bans、cross-price elasticity 和技术进步如何共同影响长期均衡。 |
| X8Y7RF84 | The Role of Government in the Market for Electric Vehicles: Evidence from China | 中国 EV 市场中的政府角色 | BLP 邻近结构政策模型 | 耐用品离散选择 + 运营成本/政策比较 | 用 EV adoption demand 把财政补贴、非财政激励和地方政策工具分解开来，量化政府在起步期市场形成中的作用。 |
| ZGZYZSJQ | The Market for Electric Vehicles: Indirect Network Effects and Policy Design | EV 市场、间接网络效应与政策设计 | BLP 邻近结构政策模型 | EV 需求 + 充电网络部署的双边网络模型 | 把 EV 销量、存量和充电站数量联立成一个动态反馈系统，用 steady state 与过渡路径讨论政策设计。 |
| 96LPI5MZ | Greenhouse Gas Abatement Cost Curves of the Residential Heating Market: A Microeconomic Approach | 居民供暖系统、减排成本曲线与政策比较 | 标准 BLP 需求-供给 | 耐用品离散选择 + 运营成本/政策比较 | 把家庭供暖系统选择放进结构化离散选择，并把碳税与投资补贴的福利成本直接转成减排成本曲线。 |
| EPWJ8S9T | Consumer response to energy label policies: Evidence from the Brazilian energy label program | 家电能效标签与消费者响应 | BLP 风格差异化需求 | 耐用品离散选择 + 运营成本/政策比较 | 在耐用品选择里强调 operating costs 与标签信息如何影响异质家庭的选择与福利。 |
| JKYIT7SD | Hurdles and steps: Estimating demand for solar photovoltaics | 太阳能光伏采用、摩擦与政策组合 | BLP 邻近结构政策模型 | 太阳能采用的分阶段 / hurdle 结构需求 | 不从标准 share inversion 出发，而是把采用过程拆成多重 hurdle，解释 rebate、许可流程和地方营销活动如何共同作用。 |
| UNMC2I56 | Consumer myopia, imperfect competition and the energy efficiency gap: Evidence from the UK refrigerator market | 冰箱市场中的短视、竞争不完全与能效缺口 | 标准 BLP 需求-供给 | 带注意力/短视参数的结构需求 | 把 operating cost 的短视参数和 supply-side imperfect competition 放进同一个耐用品市场，从而分开比较“改偏好”和“改竞争”的政策效果。 |
| 2R3LE27E | The Welfare Effects of Peer Entry: The Case of Airbnb and the Accommodation Industry | Airbnb 进入、住宿市场结构与福利 | 标准 BLP 需求-供给 | 酒店固定供给 + Airbnb 弹性供给框架 | 在差异化住宿需求上加入“酒店固定供给 vs Airbnb 弹性 peer supply”的供给二元结构，让高峰期和容量约束成为模型核心。 |
| NY37LT4P | Market Entry, Fighting Brands, and Tacit Collusion: Evidence from the French Mobile Telecommunications Market | 法国移动通信进入、fighting brands 与 tacit collusion | 标准 BLP 需求-供给 | 通信市场 BLP + 产品线扩张与进入 | 在标准 BLP 需求外，加入零售/批发双层寡头竞争和 subsidiary brands 的产品线扩张决策，用来解释 entry 之后的 fighting brand 现象。 |
| S925QHZD | Equilibrium Effects of Food Labeling Policies | 食品警示标签、企业配方调整与均衡福利 | 标准 BLP 需求-供给 | 食品标签下的需求-供给均衡模型 | 需求侧引入消费者对营养成分的误信念和标签信号，供给侧引入配方 reformulation 选择，因此政策不是单纯的信息披露，而是均衡重配。 |

## 汽车、EV 与交通政策

### Better Lucky Than Rich? Welfare Analysis of Automobile Licence Allocations in Beijing and Shanghai (`JDV2EEV6`)

- 研究方向：牌照配置机制与汽车福利比较
- BLP 类型：BLP 风格差异化需求
- 这篇在问什么：Economists often favour market-based mechanisms over non-market based mechanisms to allocate scarce public resources on grounds of economic efficiency and revenue generation.

**这篇如何利用 BLP**
这篇论文的模型定位是“BLP-style differentiated-product demand”。 它使用的是“BLP 风格差异化产品需求”这一类结构框架。 在需求侧，全文表明作者在做结构化产品需求分析，但 OCR 证据不足以把需求形式精确钉死到某个 logit 变体。 在供给侧，供给侧并非完全缺席，作者至少把进入、定价或市场结构响应嵌进均衡框架。 识别与估计上，识别依赖工具变量、GMM 或其他矩条件来处理价格与产品属性的内生性。

**这篇相对标准 BLP 改了什么**
把牌照稀缺和牌照获取机制嵌入购车选择，比较摇号、拍卖等牌照制度如何改变车型需求和福利。

**文中模型骨架（按本文整理）**
```tex
u_{ijmt} = x_{jt}\beta_i - \alpha_i p_{jmt} + \xi_{jmt} + \varepsilon_{ijmt}

s_{jmt} = \int \frac{\exp(\delta_{jmt}+\mu_{ijmt})}{1+\sum_k \exp(\delta_{kmt}+\mu_{ikmt})} dF_i

\delta_{jmt} = x_{jt}\bar{\beta} - \bar{\alpha} p_{jmt} + \xi_{jmt}
```

**这个模型骨架在本文里怎么读**
这一类论文保留了 BLP 最关键的需求侧部分：消费者异质性、产品空间替代和价格响应。供给侧有时被简化、外生化，或者只在反事实阶段以较轻的方式处理。 放到这篇论文里，最关键的 paper-specific 改造是：把牌照稀缺和牌照获取机制嵌入购车选择，比较摇号、拍卖等牌照制度如何改变车型需求和福利。 因此它最终能回答的问题，不只是“消费者是否会替代”，还包括：模型的终点不是参数本身，而是福利、反事实和政策比较。

**OCR 原文模型片段**
```text
s to obtain the market demand. We focus on the mechanism of the model in this section and leave the discussion on model estimation and identification to the next section.

## 4.1. Utility function specification

Let m = {1,2,3,4} denote a market (i.e. Beijing, Nanjing, Shanghai, Tianjin) and a year-month by t from 2008 to 2012. Let i denote a household and j ∈ denote a model (i.e. vintage-nameplate) where J is the choice set. Household i’s utility from product j is a function of household demographics and product characteristics. A household chooses one product from a total of J models and an outside alternative in a given month. The outside alternative captures the decision of not purchasing any new vehicle in the current month. The indirect utility of household i from product j in market m at time t is defined as

$$
u _ { m t i j } = \bar { u } ( \mathfrak { p } _ { j } , \mathfrak { b } _ { m t i } , \mathrm { X } _ { j } , \xi _ { m t j } , \mathrm { y } _ { m t i } , Z _ { m t i } ) + \epsilon _ { m t i j } ,\tag{1}
$$

where the first term on the right, $\bar { u } ( . )$ , denotes the deterministic compon
```

```text
from the most preferred vehicle if the licence lasts as long as the vehicle (10–15 years).23

To estimate consumer surplus for different vehicles models, we set up and estimate a random coefficient discrete choice model of vehicle demand. In this section, we first specify the utility function, the basis of individual choices. We then discuss the aggregation process to obtain the market demand. We focus on the mechanism of the model in this section and leave the discussion on model estimation and identification to the next section.

## 4.1. Utility function specification

Let m = {1,2,3,4} denote a market (i.e. Beijing, Nanjing, Shanghai, Tianjin) and a year-month by t from 2008 to 2012. Let i denote a household and j ∈ denote a model (i.e. vintage-nameplate) where J is the choice set. Household i’s utility from product j is a function of household demographics and product characteristics. A household chooses one product from a total of J models and an outside alternative in a given month. The outside alternative captures the decision of not purchasing any new vehicle in the current month. The indirect utility of
```

**我对这篇模型的具体解释**
1. 先看研究对象：牌照配置机制与汽车福利比较。这决定了作者为什么需要结构模型而不是只做 reduced-form。
2. 再看需求侧：全文表明作者在做结构化产品需求分析，但 OCR 证据不足以把需求形式精确钉死到某个 logit 变体。
3. 再看供给/均衡：供给侧并非完全缺席，作者至少把进入、定价或市场结构响应嵌进均衡框架。
4. 真正的 paper-specific 改造是：把牌照稀缺和牌照获取机制嵌入购车选择，比较摇号、拍卖等牌照制度如何改变车型需求和福利。
5. 所以这篇模型最终服务于：模型的终点不是参数本身，而是福利、反事实和政策比较。

**主要发现与模型输出**
- Our analysis shows that different allocation mechanisms lead to dramatic differences in social welfare.
- A uniform-price auction would have generated nearly 20 billion Yuan to Beijing municipal government, more than covering all its subsidies to the local public transit system 7.

**模型锚点**
- estimation: `5. IDENTIFICATION AND ESTIMATION` (p.17) - 5. IDENTIFICATION AND ESTIMATION
- counterfactual: `7. WELFARE ANALYSIS` (p.28) - 7. WELFARE ANALYSIS The purpose of this section is to compare welfare consequences under the lottery and auction systems and we focus on 2012 for illustration. The comparison is performed on both allocative efficiency an
- conclusion: `8. CONCLUSION` (p.36) - 8. CONCLUSION Air pollution and traffic congestion are arguably two of the most pressing issues for China’s urban residents. To combat these problems, transit authorities in several major cities in China are implementing

---

### Carbon Taxes, Path Dependency, and Directed Technical Change: Evidence from the Auto Industry (`RQSSQUXV`)

- 研究方向：碳税、路径依赖与汽车定向技术变迁
- BLP 类型：BLP 邻近结构政策模型
- 这篇在问什么：Uses global firm-level patent data to show that higher fuel prices redirect automobile innovation toward cleaner technologies and that innovation is strongly path dependent.

**这篇如何利用 BLP**
这篇论文的模型定位是“BLP-adjacent structural policy model”。 它使用的是“清洁/污染汽车束 + 定向技术变迁”这一类结构框架。 在需求侧，全文表明作者在做结构化产品需求分析，但 OCR 证据不足以把需求形式精确钉死到某个 logit 变体。 在供给侧，供给侧较轻或被外生化，论文重心更偏需求恢复、替代矩阵和消费者/社会福利。 识别与估计上，识别依赖工具变量、GMM 或其他矩条件来处理价格与产品属性的内生性。

**这篇相对标准 BLP 改了什么**
把 clean / dirty vehicles、能源投入和创新方向放在同一理论结构里，重点从静态替代扩展到动态 innovation direction。

**文中模型骨架（按本文整理）**
```tex
U = C_0 + \Bigl[ \Bigl(\int_0^1 Y_{ci}^{(\sigma-1)/\sigma} di \Bigr)^{\frac{\sigma}{\sigma-1}\frac{\varepsilon-1}{\varepsilon}}
     + \Bigl(\int_0^1 Y_{di}^{(\sigma-1)/\sigma} di \Bigr)^{\frac{\sigma}{\sigma-1}\frac{\varepsilon-1}{\varepsilon}} \Bigr]^{\frac{\varepsilon}{\varepsilon-1}\frac{\beta-1}{\beta}}

Y_{ci} = \min(y_{ci}, \xi_{ci} e_{ci}), \quad
Y_{di} = \min(y_{di}, \xi_{di} e_{di})
```

**这个模型骨架在本文里怎么读**
这篇不是狭义的 BLP 车型需求，而是把 clean / dirty vehicle bundle、能源投入和创新方向放进结构模型。它关注的不是静态替代矩阵本身，而是碳税如何通过需求与创新的双重路径推动定向技术变迁。 放到这篇论文里，最关键的 paper-specific 改造是：把 clean / dirty vehicles、能源投入和创新方向放在同一理论结构里，重点从静态替代扩展到动态 innovation direction。 因此它最终能回答的问题，不只是“消费者是否会替代”，还包括：论文明确把模型用于税收、补贴、禁令、标签或进入政策的反事实分析。

**OCR 原文模型片段**
```text
n appendix A. We consider a one-period model of an economy in which consumers derive utility from an outside good and from motor vehicle services. To abstract from income effects, utility is quasi-linear with respect to the outside good $C _ { 0 }$ chosen as the numeraire .

ÞTo consume motor vehicle services, consumers need to buy cars and fuel call this a “dirty car bundle” or cars and electricity call this a ð Þ“clean car bundle” . Utility is then given by

$$
\begin{array} { c } { { U = C _ { 0 } + { \displaystyle { \frac { \beta } { \beta - 1 } } } \left\{ \left[ { \displaystyle { \int _ { 0 } ^ { 1 } Y _ { c i } ^ { ( \sigma - 1 ) / \sigma } d \dot { i } } } \right] ^ { [ \sigma / ( \sigma - 1 ) ] [ ( \varepsilon - 1 ) / \varepsilon ] } \right. } } \\ { { \left. + \left[ { \displaystyle { \int _ { 0 } ^ { 1 } Y _ { d i } ^ { ( \sigma - 1 ) / \sigma } d \dot { i } } } \right] ^ { [ \sigma / ( \sigma - 1 ) ] [ ( \varepsilon - 1 ) / \varepsilon ] } \right\} ^ { [ \varepsilon / ( \varepsilon - 1 ) ] [ ( \beta - 1 ) / \beta ] } , } } \end{array}
$$

where the consumption of variety i of clean cars together with
```

```text
_ { 0 }$ chosen as the numeraire .

ÞTo consume motor vehicle services, consumers need to buy cars and fuel call this a “dirty car bundle” or cars and electricity call this a ð Þ“clean car bundle” . Utility is then given by

$$
\begin{array} { c } { { U = C _ { 0 } + { \displaystyle { \frac { \beta } { \beta - 1 } } } \left\{ \left[ { \displaystyle { \int _ { 0 } ^ { 1 } Y _ { c i } ^ { ( \sigma - 1 ) / \sigma } d \dot { i } } } \right] ^ { [ \sigma / ( \sigma - 1 ) ] [ ( \varepsilon - 1 ) / \varepsilon ] } \right. } } \\ { { \left. + \left[ { \displaystyle { \int _ { 0 } ^ { 1 } Y _ { d i } ^ { ( \sigma - 1 ) / \sigma } d \dot { i } } } \right] ^ { [ \sigma / ( \sigma - 1 ) ] [ ( \varepsilon - 1 ) / \varepsilon ] } \right\} ^ { [ \varepsilon / ( \varepsilon - 1 ) ] [ ( \beta - 1 ) / \beta ] } , } } \end{array}
$$

where the consumption of variety i of clean cars together with the corresponding clean energy electricity is

$$
Y _ { c i } = \operatorname* { m i n } ( y _ { c i } , \xi _ { c i } e _ { c i } ) ,
$$

and the consumption of variety i of dirty cars together with the corresponding dirty energy fuel is
```

**我对这篇模型的具体解释**
1. 先看研究对象：碳税、路径依赖与汽车定向技术变迁。这决定了作者为什么需要结构模型而不是只做 reduced-form。
2. 再看需求侧：全文表明作者在做结构化产品需求分析，但 OCR 证据不足以把需求形式精确钉死到某个 logit 变体。
3. 再看供给/均衡：供给侧较轻或被外生化，论文重心更偏需求恢复、替代矩阵和消费者/社会福利。
4. 真正的 paper-specific 改造是：把 clean / dirty vehicles、能源投入和创新方向放在同一理论结构里，重点从静态替代扩展到动态 innovation direction。
5. 所以这篇模型最终服务于：论文明确把模型用于税收、补贴、禁令、标签或进入政策的反事实分析。

**主要发现与模型输出**
- Column 1 shows that the co-Þefficient on the tax-inclusive fuel price is positive and significant.

**模型锚点**
- results: `Main Results` (p.23) - Main Results Our main results are shown in table 3. Columns 1-3 use the number of clean patents a flow in a firm as the dependent variable and columns 4- 24 journal of political economy This content downloaded from 128.2

---

### Consumer Myopia in Vehicle Purchases: Evidence from a Natural Experiment (`HUZV45IT`)

- 研究方向：车辆购买中的短视、自然实验与均衡效果
- BLP 类型：BLP 邻近结构政策模型
- 这篇在问什么：A central question in the analysis of fuel economy policy is whether consumers are myopic with regards to future fuel costs.

**这篇如何利用 BLP**
这篇论文的模型定位是“BLP-adjacent structural policy model”。 它使用的是“带注意力/短视参数的结构需求”这一类结构框架。 在需求侧，全文表明作者在做结构化产品需求分析，但 OCR 证据不足以把需求形式精确钉死到某个 logit 变体。 在供给侧，供给侧是显式的：通常包含多产品定价、边际成本恢复、markup 变化和均衡反事实。 识别与估计上，识别主要靠制度冲击或自然实验，把外生变化灌进结构模型。

**这篇相对标准 BLP 改了什么**
利用燃油经济性标签 restatement 的外生冲击识别消费者对未来燃料成本的低估，再看价格与市场均衡如何调整。

**文中模型骨架（按本文整理）**
```tex
u_{ijt} = x_{jt}\beta_i - \alpha_i p_{jt} - \gamma_i \cdot \text{OperatingCost}_{jt} + \xi_{jt} + \varepsilon_{ijt},
\quad 0 < \gamma_i \le 1

\gamma_i < 1 \Rightarrow \text{consumers underweight future operating or fuel costs}
```

**这个模型骨架在本文里怎么读**
这里的核心改造是引入一个注意力或短视参数 γ，让未来运营成本在当期购买选择中被低估。论文通常再把这个需求侧缺陷与竞争不完全或供给反应结合起来做政策比较。 放到这篇论文里，最关键的 paper-specific 改造是：利用燃油经济性标签 restatement 的外生冲击识别消费者对未来燃料成本的低估，再看价格与市场均衡如何调整。 因此它最终能回答的问题，不只是“消费者是否会替代”，还包括：模型的终点不是参数本身，而是福利、反事实和政策比较。

**OCR 原文模型片段**
```text
thur van Benthem   
NBER Working Paper No. 25845   
May 2019   
JEL No. D12,L62,Q4

## ABSTRACT

A central question in the analysis of fuel-economy policy is whether consumers are myopic with regards to future fuel costs. We provide the first evidence on consumer valuation of fuel economy from a natural experiment. We examine the short-run equilibrium effects of an exogenous restatement of fuel-economy ratings that affected 1.6 million vehicles. Using the implied changes in willingness-to-pay, we find that consumers act myopically: consumers are indifferent between \$1 in discounted fuel costs and 15-38 cents in the vehicle purchase price when discounting at 4%. This myopia persists under a wide range of assumptions.

Kenneth Gillingham   
School of Forestry and Environmental Studies   
Yale University   
195 Prospect Street   
New Haven, CT 06511   
and NBER   
kenneth.gillingham@yale.edu   
Sébastien Houde   
Department of Management, Technology,   
and Economics   
Centre for Energy Policy and Economics   
ETH Zurich   
Zurichbergstrasse 18, 8092 Zurich   
shoude@ethz.ch   
Arthur van Benthem   
The Wharton Sc
```

```text
A central question in the analysis of fuel-economy policy is whether consumers are myopic with regards to future fuel costs. We provide the first evidence on consumer valuation of fuel economy from a natural experiment. We examine the short-run equilibrium effects of an exogenous restatement of fuel-economy ratings that affected 1.6 million vehicles. Using the implied changes in willingness-to-pay, we find that consumers act myopically: consumers are indifferent between \$1 in discounted fuel costs and 15-38 cents in the vehicle purchase price when discounting at 4%. This myopia persists under a wide range of assumptions.

Kenneth Gillingham   
School of Forestry and Environmental Studies   
Yale University   
195 Prospect Street   
New Haven, CT 06511   
and NBER   
kenneth.gillingham@yale.edu   
Sébastien Houde   
Department of Management, Technology,   
and Economics   
Centre for Energy Policy and Economics   
ETH Zurich   
Zurichbergstrasse 18, 8092 Zurich   
shoude@ethz.ch   
Arthur van Benthem   
The Wharton School   
University of Pennsylvania   
1354 Steinberg Hall - Dietrich Hall   
3620 Locust Walk
```

**我对这篇模型的具体解释**
1. 先看研究对象：车辆购买中的短视、自然实验与均衡效果。这决定了作者为什么需要结构模型而不是只做 reduced-form。
2. 再看需求侧：全文表明作者在做结构化产品需求分析，但 OCR 证据不足以把需求形式精确钉死到某个 logit 变体。
3. 再看供给/均衡：供给侧是显式的：通常包含多产品定价、边际成本恢复、markup 变化和均衡反事实。
4. 真正的 paper-specific 改造是：利用燃油经济性标签 restatement 的外生冲击识别消费者对未来燃料成本的低估，再看价格与市场均衡如何调整。
5. 所以这篇模型最终服务于：模型的终点不是参数本身，而是福利、反事实和政策比较。

**主要发现与模型输出**
- Using the implied changes in willingness to pay, we find that consumers act myopically: consumers are indifferent between $1.00 in discounted fuel costs and $0.

**模型锚点**
- counterfactual: `5 Implications for the Valuation of Fuel Economy` (p.12) - 5 Implications for the Valuation of Fuel Economy
- results: `4 The Equilibrium Effects of the Restatement` (p.7) - 4 The Equilibrium Effects of the Restatement
- conclusion: `6 Conclusions` (p.18) - 6 Conclusions This paper exploits an unexpected restatement in the EPA-rated fuel economy for thousands of vehicles. A highly desirable feature of this natural experiment is that the vehicles themselves are identical bef

---

### Consumer Valuation of Fuel Costs and Tax Policy: Evidence from the European Car Market (`5TWRWEP3`)

- 研究方向：燃料成本估值、里程异质性与汽车税制
- BLP 类型：标准 BLP 需求-供给
- 这篇在问什么：To what extent do car buyers undervalue future fuel costs, and what does this imply for tax policy?

**这篇如何利用 BLP**
这篇论文的模型定位是“canonical BLP demand-supply”。 它使用的是“带燃料成本与里程异质性的汽车 BLP”这一类结构框架。 在需求侧，全文表明作者在做结构化产品需求分析，但 OCR 证据不足以把需求形式精确钉死到某个 logit 变体。 在供给侧，供给侧较轻或被外生化，论文重心更偏需求恢复、替代矩阵和消费者/社会福利。 识别与估计上，识别依赖工具变量、GMM 或其他矩条件来处理价格与产品属性的内生性。

**这篇相对标准 BLP 改了什么**
把未来燃料成本显式写进效用，并用里程异质性来解释燃油税为何比产品税更能针对高里程消费者。

**文中模型骨架（按本文整理）**
```tex
u_{ijk} = x_{jk}\beta_i^x - \alpha_i \bigl(p_{jk} + \gamma G_{ijk}\bigr) + \xi_{jk} + \varepsilon_{ijk}

G_{ijk} = \text{PDV of expected fuel costs}(\text{mileage}_i,\text{fuel price},\text{fuel economy}_{jk})

s_{jk} = \int \Pr\{u_{ijk} \ge u_{i\ell}\ \forall \ell\} dF_i
```

**这个模型骨架在本文里怎么读**
标准 BLP 的关键改造是把燃料成本明确写进效用，并让它通过里程异质性进入消费者选择。这样模型不只解释车型替代，还能解释燃料税、产品税和能耗政策为什么会有不同的福利效果。 放到这篇论文里，最关键的 paper-specific 改造是：把未来燃料成本显式写进效用，并用里程异质性来解释燃油税为何比产品税更能针对高里程消费者。 因此它最终能回答的问题，不只是“消费者是否会替代”，还包括：模型的终点不是参数本身，而是福利、反事实和政策比较。

**OCR 原文模型片段**
```text
d, they pay the present discounted value of expected future fuel costs $G _ { i j k }$ . The conditional indirect utility of consumer i for car model j and engine variant k is

$$
u _ { i j k } = x _ { j k } \beta _ { i } ^ { x } - \alpha _ { i } ( p _ { j k } + \gamma G _ { i j k } ) + \xi _ { j k } + \varepsilon _ { i j k } ,\tag{1}
$$

where $x _ { j k }$ is a vector of observed car and engine characteristics and $\xi _ { j k }$ is an unobserved product characteristic. The vector $\beta _ { i } ^ { x }$ captures individual-specific valuations for the product characteristics, $\alpha _ { i }$ is the marginal utility of income, and $\varepsilon _ { i j k }$ is a remaining individual-specific valuation for car $j k$ , modeled as an extreme value (logit) random variable. The utility of the outside good is normalized to $u _ { i 0 0 } = \varepsilon _ { i 0 0 }$ The parameter $\gamma$ is Allcott and Wozny’s (2014) “attention weight” or “future valuation” parameter. $\operatorname { I f } \gamma = 1$ , consumers correctly trade-off the car’s purchase price $p _ { j k }$ against the present discounted value of future
```

```text
# Consumer Valuation of Fuel Costs and Tax Policy: Evidence from the European Car Market†

By Laura Grigolon, Mathias Reynaert, and Frank Verboven\*

To what extent do car buyers undervalue future fuel costs, and what does this imply for tax policy? To address both questions, we show it is crucial to account for consumer mileage heterogeneity. We use product-level data for a panel of European countries and exploit fuel cost variation by engine. Despite a modest undervaluation of fuel costs, fuel taxes are more effective in reducing fuel usage than product taxes. They also perform better in terms of welfare, even when usage demand is held fixed. The reason is that fuel taxes better target high mileage consumers to purchase fuel efficient cars. (JEL D12, H25, H31, L62, L71)

Governments are using a variety of policies to reducesenger cars. A central question in this debate is wheth $\mathrm { C O } _ { 2 }$ emissions from paser it is preferable to focus on fuel
```

**我对这篇模型的具体解释**
1. 先看研究对象：燃料成本估值、里程异质性与汽车税制。这决定了作者为什么需要结构模型而不是只做 reduced-form。
2. 再看需求侧：全文表明作者在做结构化产品需求分析，但 OCR 证据不足以把需求形式精确钉死到某个 logit 变体。
3. 再看供给/均衡：供给侧较轻或被外生化，论文重心更偏需求恢复、替代矩阵和消费者/社会福利。
4. 真正的 paper-specific 改造是：把未来燃料成本显式写进效用，并用里程异质性来解释燃油税为何比产品税更能针对高里程消费者。
5. 所以这篇模型最终服务于：模型的终点不是参数本身，而是福利、反事实和政策比较。

**主要发现与模型输出**
- To address both questions, we show it is crucial to account for consumer mileage heterogeneity.
- To what extent do car buyers undervalue future fuel costs, and what does this imply for tax policy?

**模型锚点**
- OCR 章节锚点较弱，建议回到 `D:/codex/tmp/blp_full_read_20260417/parsed_all/5TWRWEP3/5TWRWEP3.llm.md` 搜索 `utility`, `demand`, `profit`, `policy` 等关键词。

---

### Disentangling sources of vehicle emissions reduction in France: 2003-2008 (`9HUJHUTJ`)

- 研究方向：法国新车排放下降的来源分解
- BLP 类型：标准 BLP 需求-供给
- 这篇在问什么：We analyze the evolution of CO 2emissions of new vehicles sold in France between 2003 and 2008.

**这篇如何利用 BLP**
这篇论文的模型定位是“canonical BLP demand-supply”。 它使用的是“BLP 风格差异化产品需求”这一类结构框架。 在需求侧，需求侧更像嵌套 logit / 分层离散选择，保留了产品空间替代结构，但异质性比经典 BLP 更轻。 在供给侧，供给侧较轻或被外生化，论文重心更偏需求恢复、替代矩阵和消费者/社会福利。 识别与估计上，识别主要靠制度冲击或自然实验，把外生变化灌进结构模型。

**这篇相对标准 BLP 改了什么**
利用差异化汽车需求来分解排放下降是来自税制、柴油化、技术变化还是消费者替代，而不是只看平均排放变化。

**文中模型骨架（按本文整理）**
```tex
u_{ijmt} = x_{jt}\beta_i - \alpha_i p_{jmt} + \xi_{jmt} + \varepsilon_{ijmt}

s_{jmt} = \int \frac{\exp(\delta_{jmt}+\mu_{ijmt})}{1+\sum_k \exp(\delta_{kmt}+\mu_{ikmt})} dF_i

\delta_{jmt} = x_{jt}\bar{\beta} - \bar{\alpha} p_{jmt} + \xi_{jmt}
```

**这个模型骨架在本文里怎么读**
这一类论文保留了 BLP 最关键的需求侧部分：消费者异质性、产品空间替代和价格响应。供给侧有时被简化、外生化，或者只在反事实阶段以较轻的方式处理。 放到这篇论文里，最关键的 paper-specific 改造是：利用差异化汽车需求来分解排放下降是来自税制、柴油化、技术变化还是消费者替代，而不是只看平均排放变化。 因此它最终能回答的问题，不只是“消费者是否会替代”，还包括：论文明确把模型用于税收、补贴、禁令、标签或进入政策的反事实分析。

**OCR 原文模型片段**
```text
# Disentangling sources of vehicle emissions reduction in France: 2003–2008✩

![](images/5a65fa77bf5ab13db34d8ad5c69e835388cfa660970fc9cc62b9a4da63e1c1cb.jpg)

Xavier D’Haultfœuille a , Isis Durrmeyer b,∗ , Philippe Février c

a CREST (LMI), 15 Boulevard Gabriel Péri, 92245 Malakoff, France

b University of Mannheim, L7, 3-5 68131 Mannheim, Germany

c CREST (LEI), 15 Boulevard Gabriel Péri, 92245 Malakoff, France

## a r t i c l e i n f o

Article history:   
Received 18 September 2015   
Revised 3 May 2016   
Accepted 4 May 2016   
Available online 17 May 2016   
JEL classification:   
D12   
H23   
L62   
Q51

Keywords:   
Environmental policy   
Consumer preferences   
$\mathrm { C O _ { 2 } }$ emissions   
Automobiles

## a b s t r a c t

We analyze the evolution of $\mathrm { C O _ { 2 } }$ emissions of new vehicles sold in France between 2003 and 2008. We investigate in particular the effect of two policies introduced during that time: the energy label requ
```

```text
y label requirement, which went into effect in the end of 2005, and a feebate based on $\mathrm { C O _ { 2 } }$ emissions of new vehicles in 2008. We estimate a flexible model of demand for automobiles that incorporates consumers’ heterogeneity and valuation of vehicle $\mathrm { C O _ { 2 } }$ emissions. Our results show that there has been a shift in preferences towards low-emitting cars. Moreover, the timing of these changes is consistent with the introduction of the two policies. This suggests that the feebate had a crowding-in effect in addition to its price effect. Overall, the change in preferences accounts for 40% of the overall decrease in average $\mathrm { C O _ { 2 } }$ emissions of new cars in the period.

© 2016 Elsevier B.V. All rights reserved.

## 1. Introduction

In this paper, we study the evolution of carbon dioxide $\left( \mathrm { C O } _ { 2 } \right)$ emissions of new vehicles sold in France over the period 2003–2008. We seek to understand the 13% average decrease in new vehicle $\mathrm { C O _ { 2 } }$ emissions over this period, from 156 g/km in January 2003 to 136 g in December 2008.
```

**我对这篇模型的具体解释**
1. 先看研究对象：法国新车排放下降的来源分解。这决定了作者为什么需要结构模型而不是只做 reduced-form。
2. 再看需求侧：需求侧更像嵌套 logit / 分层离散选择，保留了产品空间替代结构，但异质性比经典 BLP 更轻。
3. 再看供给/均衡：供给侧较轻或被外生化，论文重心更偏需求恢复、替代矩阵和消费者/社会福利。
4. 真正的 paper-specific 改造是：利用差异化汽车需求来分解排放下降是来自税制、柴油化、技术变化还是消费者替代，而不是只看平均排放变化。
5. 所以这篇模型最终服务于：论文明确把模型用于税收、补贴、禁令、标签或进入政策的反事实分析。

**主要发现与模型输出**
- We show in another paper (see D’Haultfœuille et al., 2011) that such a cost was difficult to anticipate.
- This also implies that the optimal level of rebates and taxes for the different classes, in terms of social welfare, are lower than if individual’s preferences are not affected by the policy.
- We analyze the evolution of CO 2emissions of new vehicles sold in France between 2003 and 2008.

**模型锚点**
- estimation: `4. Estimation results` (p.14) - 4. Estimation results
- conclusion: `5. Conclusion` (p.30) - 5. Conclusion We have shown evidence that, in the French automobile market, consumers shifted their preferences for \mathrm { C O _ { 2 } } emissions between 2003 and 2008. This shift seems to be related to two environme

---

### Effectiveness of China's plug-in electric vehicle subsidy (`M5CH8LSF`)

- 研究方向：中国 PEV 补贴有效性与成本效果
- BLP 类型：BLP 风格差异化需求
- 这篇在问什么：In this paper, we explore the impact and cost-effectiveness of the Chinese PEV subsidy program.

**这篇如何利用 BLP**
这篇论文的模型定位是“BLP-style differentiated-product demand”。 它使用的是“耐用品离散选择 + 运营成本/政策比较”这一类结构框架。 在需求侧，需求侧是结构化离散选择/差异化产品需求系统，重点是恢复替代关系与价格弹性。 在供给侧，供给侧较轻或被外生化，论文重心更偏需求恢复、替代矩阵和消费者/社会福利。 识别与估计上，识别依赖工具变量、GMM 或其他矩条件来处理价格与产品属性的内生性。

**这篇相对标准 BLP 改了什么**
围绕收入和年行驶里程异质性估计 PEV 选择模型，用以比较补贴拉动销量和减排的性价比。

**文中模型骨架（按本文整理）**
```tex
u_{ijt} = x_{jt}\beta_i - \alpha_i p_{jt} - \kappa_i \cdot \text{OperatingCost}_{jt} + \xi_{jt} + \varepsilon_{ijt}

\Pr(j) = \frac{\exp(u_{ijt})}{1+\sum_k \exp(u_{ikt})}

\text{Policy counterfactuals compare taxes, subsidies, labels, or standards}
```

**这个模型骨架在本文里怎么读**
它保留了差异化耐用品选择的结构需求主线，把运营成本、标签或补贴等政策变量直接写进选择问题，再比较不同政策对采用、能耗和福利的影响。 放到这篇论文里，最关键的 paper-specific 改造是：围绕收入和年行驶里程异质性估计 PEV 选择模型，用以比较补贴拉动销量和减排的性价比。 因此它最终能回答的问题，不只是“消费者是否会替代”，还包括：模型的终点不是参数本身，而是福利、反事实和政策比较。

**OCR 原文模型片段**
```text
l plan for reducing local air pollution and greenhouse gas emissions from the light-duty vehicle sector. In this paper, we explore the impact and cost-effectiveness of the Chinese PEV subsidy program. In particular, a vehicle choice model is estimated using a large random sample of individual level, model year 2017 Chinese new vehicle purchases. The choice model is then used to predict PEV market share under alternative policies. Simulation results suggest that the 2.5% PEV market share of Chinese new vehicle sales in 2017 resulted in China‟s new vehicle fleet fuel economy improving by roughly 2%, reducing total gasoline consumption by 6.66 billion liters. However, the current PEV subsidy in China is expensive, costing \$1.90 per additional liter of gasoline saved. This is due to a large number of nonadditional PEV buyers, particularly high income consumers, who would have purchased the PEV regardless of the subsidy. Eliminating the subsidy for high income consumers and increasing it for low income consumers could result in a substantially lower cost per additional PEV (\$13,758 versus \$24,506). This would allow
```

```text
) are provided for each make-model to make the sample representative of the national new vehicle market.

To account for consumer heterogenity, the study aims to estimate separate choice models for low and high income consumer subgroups. The distinction in income groups is sought because previous studies on new vehicle consumers in other countries such as the U.S. have shown that preferences vary most by income (e.g., (DeShazo et al., 2017; Sheldon and Dua, 2018, 2019b). Appendix Table A3 including income interactions shows support for sample segmentation on income.

The disaggregate consumer-level J.D. Power survey data is aggregated into two subgroups corresponding to incomes of below and above RMB 16,000 (USD 2,368), the median monthly income for new vehicle buyers based on the J.D. Power survey data. The aggregation is done using the sales weights at the make-model level. Despite the random street intercept recruitment in J.D. Power survey data, it had no electric vehicle respondents.2 Given the insufficient J.D. Power data on PEV purchases, for PEV make-models, the sales distribution across the two subgroups
```

**我对这篇模型的具体解释**
1. 先看研究对象：中国 PEV 补贴有效性与成本效果。这决定了作者为什么需要结构模型而不是只做 reduced-form。
2. 再看需求侧：需求侧是结构化离散选择/差异化产品需求系统，重点是恢复替代关系与价格弹性。
3. 再看供给/均衡：供给侧较轻或被外生化，论文重心更偏需求恢复、替代矩阵和消费者/社会福利。
4. 真正的 paper-specific 改造是：围绕收入和年行驶里程异质性估计 PEV 选择模型，用以比较补贴拉动销量和减排的性价比。
5. 所以这篇模型最终服务于：模型的终点不是参数本身，而是福利、反事实和政策比较。

**主要发现与模型输出**
- Subsidies for promoting plug-in electric vehicle (PEV) adoption are a key component of China's overall plan for reducing local air pollution and greenhouse gas emissions from the light-duty vehicle sector.

**模型锚点**
- counterfactual: `Counterfactual Simulation Analysis` (p.7) - Counterfactual Simulation Analysis Table 4 compares the predicted counterfactual fleet if PEVs were unavailable for purchase in China to the current fleet with existing subsidies in China. Without PEVs, fleet fuel econom
- results: `RESULTS & DISCUSSION` (p.6) - RESULTS & DISCUSSION
- conclusion: `CONCLUSION` (p.10) - CONCLUSION Despite China‟s ambitious goal to have five million NEVs on the road by 2020, there is uncertainty over the future of the subsidy program. This paper seeks to shed light on the effectiveness of these subsidies

---

### Fiscal Policy and CO2 Emissions of New Passenger Cars in the EU (`99RBFASI`)

- 研究方向：欧盟汽车购买税、财政政策与排放强度
- BLP 类型：BLP 邻近结构政策模型
- 这篇在问什么：To what extent have national fiscal policies contributed to the decarbonisation of newly sold passenger cars?

**这篇如何利用 BLP**
这篇论文的模型定位是“BLP-adjacent structural policy model”。 它使用的是“两类汽车 / 税制比较模型”这一类结构框架。 在需求侧，全文表明作者在做结构化产品需求分析，但 OCR 证据不足以把需求形式精确钉死到某个 logit 变体。 在供给侧，供给侧是显式的：通常包含多产品定价、边际成本恢复、markup 变化和均衡反事实。 识别与估计上，识别依赖工具变量、GMM 或其他矩条件来处理价格与产品属性的内生性。

**这篇相对标准 BLP 改了什么**
用简化的两类车结构模型说明购买税、年税和未来成本如何共同影响车队构成与排放。

**文中模型骨架（按本文整理）**
```tex
\max_{q_1,q_2} \ u(q_1,q_2,m-x)
\quad \text{s.t.} \quad
p_1^c q_1 + p_2^c q_2 = x

p_i^c = \text{purchase price} + \text{registration tax} + \text{future operating costs}
```

**这个模型骨架在本文里怎么读**
这类模型更简单，重点不是完整的随机系数估计，而是用结构化的效用和预算约束来说明税制如何改变车队构成与排放强度。 放到这篇论文里，最关键的 paper-specific 改造是：用简化的两类车结构模型说明购买税、年税和未来成本如何共同影响车队构成与排放。 因此它最终能回答的问题，不只是“消费者是否会替代”，还包括：论文明确把模型用于税收、补贴、禁令、标签或进入政策的反事实分析。

**OCR 原文模型片段**
```text
3 Model

We illustrate the effect of vehicle purchase taxes on the average emission intensity with a simple model. We consider two car types. A representative consumer9 maximises (expected future) utility u dependent on the current purchase of cars, q _ { 1 } and q _ { 2 } , and income m net of purchase expenditures x:

where p _ { i } ^ { c } are costs per quantity, including registration taxes as well as future variable costs and annual taxes. The utility function satisfies the standard assumptions on continuity, differentiability, positive derivatives, and concavity. We also assume that both types are normal goods (increasing consumption with increasing income, decreasing consumption with increasing prices) and that the total budget for cars, x, increases in total income, m.

We do not model consumers’ care about the environmental performance of cars as such (see Achtnicht 2012 for an analysis along those lines), but focus on the effects of government instruments geared to direct consumers’ choices. We assume that the tax is fully shifted to consumers,10 so that the consumer price of cars is

where
```

```text
rage emission intensity with a simple model. We consider two car types. A representative consumer9 maximises (expected future) utility u dependent on the current purchase of cars, q _ { 1 } and q _ { 2 } , and income m net of purchase expenditures x:

where p _ { i } ^ { c } are costs per quantity, including registration taxes as well as future variable costs and annual taxes. The utility function satisfies the standard assumptions on continuity, differentiability, positive derivatives, and concavity. We also assume that both types are normal goods (increasing consumption with increasing income, decreasing consumption with increasing prices) and that the total budget for cars, x, increases in total income, m.

We do not model consumers’ care about the environmental performance of cars as such (see Achtnicht 2012 for an analysis along those lines), but focus on the effects of government instruments geared to direct consumers’ choices. We assume that the tax is fully shifted to consumers,10 so that the consumer price of cars is

where \tau _ { i } is a type-specific ad valorem tax and p _ { i } ^ { p } is the produ
```

**我对这篇模型的具体解释**
1. 先看研究对象：欧盟汽车购买税、财政政策与排放强度。这决定了作者为什么需要结构模型而不是只做 reduced-form。
2. 再看需求侧：全文表明作者在做结构化产品需求分析，但 OCR 证据不足以把需求形式精确钉死到某个 logit 变体。
3. 再看供给/均衡：供给侧是显式的：通常包含多产品定价、边际成本恢复、markup 变化和均衡反事实。
4. 真正的 paper-specific 改造是：用简化的两类车结构模型说明购买税、年税和未来成本如何共同影响车队构成与排放。
5. 所以这篇模型最终服务于：论文明确把模型用于税收、补贴、禁令、标签或进入政策的反事实分析。

**主要发现与模型输出**
- We find that for many countries the fiscal policies have become more sensitive to $$\hbox {CO}_{2}$$ emissions of new cars.
- We construct a simple model that generates predictions regarding the effect of fiscal policies on average $$\hbox {CO}_{2}$$ emissions of new cars, and then test the model empirically.

**模型锚点**
- model: `3 Model` (p.4) - 3 Model We illustrate the effect of vehicle purchase taxes on the average emission intensity with a simple model. We consider two car types. A representative consumer9 maximises (expected future) utility u dependent on t
- results: `6 Results` (p.12) - 6 Results
- conclusion: `7 Discussion` (p.19) - 7 Discussion We find empirical evidence that fiscal vehicle policies significantly affect emission intensities of new bought cars. A greater \mathrm { C O } _ { 2 } -sensitivity of registration taxes lead to the purchase

---

### Fuel taxation, emissions policy, and competitive advantage in the diffusion of European diesel automobiles (`FMISYR9Z`)

- 研究方向：欧洲柴油扩散、燃油税与竞争优势
- BLP 类型：标准 BLP 需求-供给
- 这篇在问什么：Economic integration agreements have significantly decreased import tariffs.

**这篇如何利用 BLP**
这篇论文的模型定位是“canonical BLP demand-supply”。 它使用的是“标准 BLP 需求-供给框架”这一类结构框架。 在需求侧，需求侧基本可以判定为随机系数离散选择，是最接近经典 BLP 的主干写法。 在供给侧，供给侧是显式的：通常包含多产品定价、边际成本恢复、markup 变化和均衡反事实。 识别与估计上，识别依赖工具变量、GMM 或其他矩条件来处理价格与产品属性的内生性。

**这篇相对标准 BLP 改了什么**
在多产品 Bertrand 汽车竞争里强调柴油/汽油发动机的属性、税差和厂商竞争优势如何共同驱动 diesel diffusion。

**文中模型骨架（按本文整理）**
```tex
u_{ijmt} = \delta_{jmt} + \mu_{ijmt} + \varepsilon_{ijmt},
\quad
\delta_{jmt} = x_{jt}\beta - \alpha p_{jmt} + \xi_{jmt}

s_{jmt} = \int \frac{\exp(\delta_{jmt}+\mu_{ijmt})}{1+\sum_k \exp(\delta_{kmt}+\mu_{ikmt})} dF_i

\pi_f = \sum_m \sum_{j \in J_f} (p_{jmt} - mc_{jmt}) M_{mt} s_{jmt},
\quad
p - mc = \Delta^{-1} s
```

**这个模型骨架在本文里怎么读**
核心是随机系数离散选择需求加多产品 Bertrand 定价。需求侧恢复替代矩阵，供给侧用一阶条件把价格、markup 和边际成本连起来，然后再做政策反事实或福利计算。 放到这篇论文里，最关键的 paper-specific 改造是：在多产品 Bertrand 汽车竞争里强调柴油/汽油发动机的属性、税差和厂商竞争优势如何共同驱动 diesel diffusion。 因此它最终能回答的问题，不只是“消费者是否会替代”，还包括：论文明确把模型用于税收、补贴、禁令、标签或进入政策的反事实分析。

**OCR 原文模型片段**
```text
be summarized as follows: consumer i derives an indirect utility from buying vehicle j at time t that depends on price and characteristics of the car:

$$
\begin{array} { l } { { u _ { i j t } = x _ { j i } \beta _ { i } + \alpha _ { i t } p _ { j t } + \xi _ { j t } + \epsilon _ { i j t } , } } \\ { { \mathrm { w h e r e } \quad i = 1 , \ldots , I _ { t } ; \quad j = 1 , \ldots , J _ { t } ; \quad t = \{ 1 9 9 1 , \ldots , 2 0 0 0 \} , } } \end{array}\tag{1}
$$

where we define a product j as model-engine type pair. In this Lancasterian approach, utility depends on the set of characteristics of the vehicle purchased, which includes a vector of $K$ observable characteristics $x _ { j t }$ as well as other characteristics, which are known to consumers and firms but remain unobservable for the econometrician, $\xi _ { j t }$ . Unobserved tastes of consumer i for vehicle $j , \epsilon _ { i j t } ,$ follow an i.i.d. multivariate type I extreme value distribution. Similar to Sweeting (2013), we assume the unobserved quality $\xi _ { j t }$ evolves according the following AR(1) process:

$$
\xi _ { j , t + 1 } = F _
```

```text
ice demand for horizontally differentiated products with heterogeneous preferences over observable and unobservable automobile characteristics. We add to this a model of oligopoly Bertrand-Nash price competition among multiproduct firms. The model delivers a set of structural equations which we use to recover the underlying demand and cost parameters.

 Demand. Demand can be summarized as follows: consumer i derives an indirect utility from buying vehicle j at time t that depends on price and characteristics of the car:

$$
\begin{array} { l } { { u _ { i j t } = x _ { j i } \beta _ { i } + \alpha _ { i t } p _ { j t } + \xi _ { j t } + \epsilon _ { i j t } , } } \\ { { \mathrm { w h e r e } \quad i = 1 , \ldots , I _ { t } ; \quad j = 1 , \ldots , J _ { t } ; \quad t = \{ 1 9 9 1 , \ldots , 2 0 0 0 \} , } } \end{array}\tag{1}
$$

where we define a product j as model-engine type pair. In this Lancasterian approach, utility depends on the set of characteristics of the vehicle purchased, which includes a vector of $K$ observable characteristics $x _ { j t }$ as well as other characteristics, which are known to con
```

**我对这篇模型的具体解释**
1. 先看研究对象：欧洲柴油扩散、燃油税与竞争优势。这决定了作者为什么需要结构模型而不是只做 reduced-form。
2. 再看需求侧：需求侧基本可以判定为随机系数离散选择，是最接近经典 BLP 的主干写法。
3. 再看供给/均衡：供给侧是显式的：通常包含多产品定价、边际成本恢复、markup 变化和均衡反事实。
4. 真正的 paper-specific 改造是：在多产品 Bertrand 汽车竞争里强调柴油/汽油发动机的属性、税差和厂商竞争优势如何共同驱动 diesel diffusion。
5. 所以这篇模型最终服务于：论文明确把模型用于税收、补贴、禁令、标签或进入政策的反事实分析。

**主要发现与模型输出**
- We show that (a) European fuel taxes and vehicle emissions policy favored diesel vehicles, a technology popular with European consumers but largely offered only by domestic automakers; (b) European automakers benefited from pro‐diesel fuel taxes and a lenient NO x emissions policy to earn significant profits from diesel cars; and (c) that both policies amounted to significant nontariff trade policies equivalent to an import tariff between two to three times the official rate 7.

**模型锚点**
- estimation: `5. Estimation` (p.11) - 5. Estimation We define the structural parameters of the model as \theta = [ \alpha , \beta , \gamma , \Sigma , \rho _ { \xi } , \sigma _ { \nu } ^ { 2 } ] and construct the demand-side structural error by creating quasi
- conclusion: `7. Concluding remarks` (p.26) - 7. Concluding remarks The goal in this article was to estimate the tariff-equivalence of two European domestic policies, which favored the domestic automobile industry. To do so, we estimated an equilibrium oligopoly mod

---

### How Much Do Consumers Value Fuel Economy and Performance? Evidence from Technology Adoption (`6Q55KN3G`)

- 研究方向：燃油经济性、性能与技术采用
- BLP 类型：BLP 邻近结构政策模型
- 这篇在问什么：This paper evaluates the welfare consequences of automakers forgoing performance increases to raise fuel economy as standards have tightened since 2012.

**这篇如何利用 BLP**
这篇论文的模型定位是“BLP-adjacent structural policy model”。 它使用的是“技术采用与均衡属性权衡模型”这一类结构框架。 在需求侧，全文表明作者在做结构化产品需求分析，但 OCR 证据不足以把需求形式精确钉死到某个 logit 变体。 在供给侧，供给侧是显式的：通常包含多产品定价、边际成本恢复、markup 变化和均衡反事实。 识别与估计上，识别依赖工具变量、GMM 或其他矩条件来处理价格与产品属性的内生性。

**这篇相对标准 BLP 改了什么**
不是标准 share inversion，而是从技术采用与价格均衡里恢复消费者对 fuel economy 与 performance 的权衡。

**文中模型骨架（按本文整理）**
```tex
\ln q_{jt} = \beta_f \ln(fc_{ijt}) + \beta_p \ln(perf_{jt}) + X_{ijt}\gamma + \xi_j + \nu_{ijt}

\text{Observed adoption and pricing reflect an equilibrium between consumer demand and manufacturer responses}
```

**这个模型骨架在本文里怎么读**
它并不总是把完整 BLP share inversion 写出来，但继承了 BLP 的核心关切：属性、价格、技术采用和供给反应是联动的，因此需要在均衡框架下解释消费者对性能与能效的权衡。 放到这篇论文里，最关键的 paper-specific 改造是：不是标准 share inversion，而是从技术采用与价格均衡里恢复消费者对 fuel economy 与 performance 的权衡。 因此它最终能回答的问题，不只是“消费者是否会替代”，还包括：模型的终点不是参数本身，而是福利、反事实和政策比较。

**OCR 原文模型片段**
```text
anufacturer adopts fuelsaving technology and increases the vehicle’s fuel economy. The higher fuel economy reduces fuel costs, causing the demand curve to shift to D _ { 2 } . The technology adoption increases marginal costs to M C _ { 2 } , which results in the equilibrium price of P _ { 2 } and equilibrium quantity of Q _ { 2 }

The consumer WTP for the fuel economy increase corresponds to the vertical shift of the demand curve, which is equal to the sum l _ { 1 } + l _ { 2 } . As explained in the next subsection, we use a regression of the vehicle’s equilibrium price on its fuel costs to identify the first part of the sum, l _ { 1 } \equiv P _ { 2 } - P _ { 1 } . We use a quantity regression to identify the equilibrium quantity effect Q _ { 2 } - Q _ { 1 } . The term l _ { 2 } depends on the equilibrium quantity change, as well as the slope of the demand curve. Therefore, to estimate WTP for fuel economy, we estimate the effects of fuel economy on the equilibrium price and quantity, and calculate WTP by assuming a particular slope of the demand curve. As Busse et al. (2013) note, an alternative approach would
```

```text
3.1 Empirical framework

Our empirical objective is to estimate consumer valuation for fuel economy and performance. We adapt the approach taken by Busse et al. (2013), which is to estimate separate reduced-form price and quantity regressions, and combine the results to estimate WTP. To illustrate this approach, we consider a hypothetical manufacturer that produces a single type of vehicle. For convenience, we conceive of a Bertrand model with heterogeneous products. (As we explain below, the empirical strategy does not depend on the underlying market structure.) We abstract from fuel economy and emissions standards for simplicity, and control for those standards in the empirical analysis as described below. The manufacturer faces a downward-sloping residual demand curve for that vehicle. We define the WTP for a fuel economy increase as the vertical shift of the demand curve caused by the fuel economy increase; WTP for a performance increase is defined similarly. The definition holds fixed all other attributes of the vehicle.

Figure 6 pr
```

**我对这篇模型的具体解释**
1. 先看研究对象：燃油经济性、性能与技术采用。这决定了作者为什么需要结构模型而不是只做 reduced-form。
2. 再看需求侧：全文表明作者在做结构化产品需求分析，但 OCR 证据不足以把需求形式精确钉死到某个 logit 变体。
3. 再看供给/均衡：供给侧是显式的：通常包含多产品定价、边际成本恢复、markup 变化和均衡反事实。
4. 真正的 paper-specific 改造是：不是标准 share inversion，而是从技术采用与价格均衡里恢复消费者对 fuel economy 与 performance 的权衡。
5. 所以这篇模型最终服务于：模型的终点不是参数本身，而是福利、反事实和政策比较。

**主要发现与模型输出**
- Using a unique data set and a novel approach to account for fuel economy and performance endogeneity, we find undervaluation of fuel cost savings and high valuation of performance.
- Key words: passenger vehicles, fuel economy standards, technology adoption, consumer welfare JEL classification numbers: D12, L11, L62, Q41 ∗Benjamin Leard (leard@rff.org) is a fellow at Resources for the Future (RFF).
- 1 5 Implications In this section we discuss the implications of our estimates for the effects of fuel economy and greenhouse gas emissions standards on consumer welfare.

**模型锚点**
- model: `3.1 Empirical framework` (p.11) - 3.1 Empirical framework Our empirical objective is to estimate consumer valuation for fuel economy and performance. We adapt the approach taken by Busse et al. (2013), which is to estimate separate reduced-form price and
- estimation: `3 Empirical Strategy` (p.11) - 3 Empirical Strategy
- counterfactual: `5 Implications` (p.24) - 5 Implications In this section we discuss the implications of our estimates for the effects of fuel economy and greenhouse gas emissions standards on consumer welfare. The approach is to consider small hypothetical chang
- conclusion: `6 Conclusion` (p.28) - 6 Conclusion If an energy efficiency gap exists for passenger vehicles, new vehicle fuel economy or greenhouse gas emissions standards would increase private welfare of new vehicle consumers and producers. NHTSA and EPA 

---

### Local Protectionism, Market Structure, and Social Welfare: China’s Automobile Market (`9X84A7QK`)

- 研究方向：中国汽车市场地方保护主义与福利
- BLP 类型：标准 BLP 需求-供给
- 这篇在问什么：This study documents the presence of local protectionism and quantifies its impacts on market competition and social welfare in the context of China’s automobile market.

**这篇如何利用 BLP**
这篇论文的模型定位是“canonical BLP demand-supply”。 它使用的是“标准 BLP 需求-供给框架”这一类结构框架。 在需求侧，需求侧是结构化离散选择/差异化产品需求系统，重点是恢复替代关系与价格弹性。 在供给侧，供给侧是显式的：通常包含多产品定价、边际成本恢复、markup 变化和均衡反事实。 识别与估计上，识别依赖工具变量、GMM 或其他矩条件来处理价格与产品属性的内生性。

**这篇相对标准 BLP 改了什么**
在标准汽车 BLP 里加入 province-of-origin / 本地品牌偏好与补贴扭曲，并在供给侧允许全国统一定价和税楔。

**文中模型骨架（按本文整理）**
```tex
u_{ijmt} = \delta_{jmt} + \mu_{ijmt} + \varepsilon_{ijmt},
\quad
\delta_{jmt} = x_{jt}\beta - \alpha p_{jmt} + \xi_{jmt}

s_{jmt} = \int \frac{\exp(\delta_{jmt}+\mu_{ijmt})}{1+\sum_k \exp(\delta_{kmt}+\mu_{ikmt})} dF_i

\pi_f = \sum_m \sum_{j \in J_f} (p_{jmt} - mc_{jmt}) M_{mt} s_{jmt},
\quad
p - mc = \Delta^{-1} s
```

**这个模型骨架在本文里怎么读**
核心是随机系数离散选择需求加多产品 Bertrand 定价。需求侧恢复替代矩阵，供给侧用一阶条件把价格、markup 和边际成本连起来，然后再做政策反事实或福利计算。 放到这篇论文里，最关键的 paper-specific 改造是：在标准汽车 BLP 里加入 province-of-origin / 本地品牌偏好与补贴扭曲，并在供给侧允许全国统一定价和税楔。 因此它最终能回答的问题，不只是“消费者是否会替代”，还包括：模型的终点不是参数本身，而是福利、反事实和政策比较。

**OCR 原文模型片段**
```text
5.2 Supply

We estimate the demand and supply equations separately. Our supply-side specification follows Berry et al. (1995) with a few minor modifications. First, instead of choosing the optimal price in every market, a firm chooses one national price for each model that it produces to maximize its total profits in a given year. National pricing is likely a reasonable approximation for the Chinese market because retail price maintenance is a common practice (Li et al., 2015). Second, taxes levied on automobile purchase is high in China and can account for as much as 50% of the final transaction price. This creates a sizeable wedge between the price paid by consumers and the sales revenue accrued to firms. We explicitly model how taxes affect firms’ profit function.

The annual national profit for firm f is (we suppress subscript t for simplicity):

28

where \mathcal { F } is the set of all products by firm f , { \mathfrak { p } } _ {
```

```text
This creates a sizeable wedge between the price paid by consumers and the sales revenue accrued to firms. We explicitly model how taxes affect firms’ profit function.

The annual national profit for firm f is (we suppress subscript t for simplicity):

28

where \mathcal { F } is the set of all products by firm f , { \mathfrak { p } } _ { j } ^ { 0 } is the manufacturer suggested retail price MSRP, \mathrm { T } _ { j } refers to total tax and is a function of the sales price, mc ; j is the marginal cost of product j , \mathbf { M } _ { m } is market size, measured by the number of households in market m. s _ { m j } is product j ^ { \circ } \mathrm { s } share in market m. { \bf M } _ { m } s _ { m j } is the number of automobile j sold in market m . In the second line, we use \mathrm { S } _ { j } to represent product j ^ { \circ } \mathbf { s } national sales. Here we make two simplifying assumptions on the marginal cost. First, the marginal cost for each model is constant across all markets and does not depend on the distance between where it is produced and where it is sold26. Second, the marginal cost is in
```

**我对这篇模型的具体解释**
1. 先看研究对象：中国汽车市场地方保护主义与福利。这决定了作者为什么需要结构模型而不是只做 reduced-form。
2. 再看需求侧：需求侧是结构化离散选择/差异化产品需求系统，重点是恢复替代关系与价格弹性。
3. 再看供给/均衡：供给侧是显式的：通常包含多产品定价、边际成本恢复、markup 变化和均衡反事实。
4. 真正的 paper-specific 改造是：在标准汽车 BLP 里加入 province-of-origin / 本地品牌偏好与补贴扭曲，并在供给侧允许全国统一定价和税楔。
5. 所以这篇模型最终服务于：模型的终点不是参数本身，而是福利、反事实和政策比较。

**主要发现与模型输出**
- This study documents the presence of local protectionism and quantifies its impacts on market competition and social welfare in the context of China’s automobile market.
- Through county border analysis, falsification tests, and a consumer survey, we uncover protectionist policies such as subsidies to local brands as the primary contributing factor to the observed home bias.

**模型锚点**
- model: `5.2 Supply` (p.28) - 5.2 Supply We estimate the demand and supply equations separately. Our supply-side specification follows Berry et al. (1995) with a few minor modifications. First, instead of choosing the optimal price in every market, a
- estimation: `5.3 Identification and Estimation` (p.30) - 5.3 Identification and Estimation Our discussion of identification focuses on two sets of key parameters: a) the price discounts \rho _ { 1 } , \rho _ { 2 } and \rho _ { 3 } that capture the extent of local protectionism
- counterfactual: `7.2 Welfare Analysis` (p.40) - 7.2 Welfare Analysis We first evaluate the welfare consequences of local protectionism on consumer surplus. To do so, we make two important assumptions: a) revenue neutrality of government subsidies, and b) all subsidies
- conclusion: `8 Conclusion` (p.46) - 8 Conclusion Based on the census of new passenger vehicle registrations from 2009 to 2011 in China, we provide strong evidence of local protectionism in China’s automobile market using a regression discontinuity design, 

---

### Network Externality and Subsidy Structure in Two-Sided Markets: Evidence from Electric Vehicle Incentives (`F8UTG3XW`)

- 研究方向：EV 双边市场、充电网络与补贴结构
- BLP 类型：标准 BLP 需求-供给
- 这篇在问什么：Published in volume 13, issue 4, pages 393-432 of American Economic Journal: Economic Policy, November 2021, Abstract: This paper uses new, large-scale vehicle registry data This paper uses new, large-scale vehicle registry data from Norway and a two-sided market framework to show non-neutrality of different subsidies and estimate their impact on electric vehicle adoption when network externalities are present.

**这篇如何利用 BLP**
这篇论文的模型定位是“canonical BLP demand-supply”。 它使用的是“EV 需求 + 充电网络部署的双边网络模型”这一类结构框架。 在需求侧，需求侧基本可以判定为随机系数离散选择，是最接近经典 BLP 的主干写法。 在供给侧，供给侧并非完全缺席，作者至少把进入、定价或市场结构响应嵌进均衡框架。 识别与估计上，识别依赖工具变量、GMM 或其他矩条件来处理价格与产品属性的内生性。

**这篇相对标准 BLP 改了什么**
把 EV 需求和充电站进入放进同一个双边网络框架，用以比较购车补贴和充电补贴的结构设计。

**文中模型骨架（按本文整理）**
```tex
q_t = q_t(N_t, p_t, x_t)

Q_t = \sum_{b \le t} q_b \, s_{t,b}

N_t = N_t(Q_t, z_t)
\quad \text{or} \quad
\pi^{station}_n = \text{entry profits}(Q_t, N_t, subsidy_t)
```

**这个模型骨架在本文里怎么读**
这里把 BLP 的汽车需求部分与充电站供给或进入方程联立起来，核心是正向反馈：车多了站更值得建，站多了车更容易卖。模型因此特别适合回答 EV 补贴与充电补贴应如何搭配。 放到这篇论文里，最关键的 paper-specific 改造是：把 EV 需求和充电站进入放进同一个双边网络框架，用以比较购车补贴和充电补贴的结构设计。 因此它最终能回答的问题，不只是“消费者是否会替代”，还包括：模型的终点不是参数本身，而是福利、反事实和政策比较。

**OCR 原文模型片段**
```text
nd all other stations’ profits in the market. The purchase decisions of consumers also affect station profits by changing the size of the market for electric charging.

A positive network externality arises in the context of electric vehicles due to complementarities between the (cumulative) sales of EVs and the available electric charging network. That is, if the number of stations increases for some exogenous reason, then demand for all-electric models increases. This leads to a further increase in the number of charging points, and so on. The positive feedback loop between new EV sales and charging station entry suggests that an otherwise small change on either side can lead to a large change in both electric vehicle purchases and charging station entry, which has important implications for government subsidies. Ignoring these network effects when estimating the impact of different electric vehicle policies would bias the results.

First, I model consumers’ vehicle purchasing decision by following the random coefficients discrete choice model of Berry et al. (1995). Then, I describe the charging station entry
```

```text
3 Empirical Framework

In the model, I consider the decisions of two types of economic agents: consumers and charging stations. Consumers wish to purchase a new car chosen from all available fuel types, while charging stations choose whether to enter the market for electric charging or not.15 In a simultaneous-move game, each period consumers and stations make their decisions based on complete knowledge of market conditions.

The timing of the game is as follows: (1) each period starts with a given number of vehicles of all fuel types already circulating in each market, (2) consumers decide whether to purchase a vehicle, (3) charging stations consider whether to enter the market and install charging equipment, (4) consumers choose their demand for charging and operating stations serving electric car drivers.16;17

14 I do not include the lagged and lead versions of the station subsidies for fast charging, as I did not find significant effects for the concurrent version.

15 In the current modeling framework, vehicle manufacturers’ profit maxim
```

**我对这篇模型的具体解释**
1. 先看研究对象：EV 双边市场、充电网络与补贴结构。这决定了作者为什么需要结构模型而不是只做 reduced-form。
2. 再看需求侧：需求侧基本可以判定为随机系数离散选择，是最接近经典 BLP 的主干写法。
3. 再看供给/均衡：供给侧并非完全缺席，作者至少把进入、定价或市场结构响应嵌进均衡框架。
4. 真正的 paper-specific 改造是：把 EV 需求和充电站进入放进同一个双边网络框架，用以比较购车补贴和充电补贴的结构设计。
5. 所以这篇模型最终服务于：模型的终点不是参数本身，而是福利、反事实和政策比较。

**主要发现与模型输出**
- Simultaneously, charging stations make an entry decision that is driven by their discounted stream of per-period profits and their sunk costs of entry.
- Network Externality and Subsidy Structure in Two-Sided Markets: Evidence from Electric Vehicle Incentives by Katalin Springel.

**模型锚点**
- model: `3 Empirical Framework` (p.17) - 3 Empirical Framework In the model, I consider the decisions of two types of economic agents: consumers and charging stations. Consumers wish to purchase a new car chosen from all available fuel types, while charging sta
- estimation: `3.4 Estimation Methodology` (p.28) - 3.4 Estimation Methodology The equilibrium for the model is defined by the number of operating charging stations N ^ { * } and the number of electric vehicle sales Q ^ { E V ^ { * } } that simultaneously satisfy the syst
- results: `4 Results` (p.29) - 4 Results The consumer demand for vehicles of all fuel type is derived from the indirect utility function shown in equation (3), while the station market entry is estimated from equation (10). Tables 3a and 3b display th
- conclusion: `6 Conclusion` (p.36) - 6 Conclusion There are a variety of opportunities to reduce greenhouse gas emissions from the transportation sector, such as improving fuel efficiency, reducing travel demand, improving driving practices, and switching t

---

### Optimal policy and network effects for the deployment of zero emission vehicles (`N5SE78G4`)

- 研究方向：零排放汽车部署的最优政策与网络效应
- BLP 类型：BLP 邻近结构政策模型
- 这篇在问什么：We analyze the impact of indirect network effects in the deployment of zero emission vehicles in a static partial equilibrium model.

**这篇如何利用 BLP**
这篇论文的模型定位是“BLP-adjacent structural policy model”。 它使用的是“EV 需求 + 充电网络部署的双边网络模型”这一类结构框架。 在需求侧，全文表明作者在做结构化产品需求分析，但 OCR 证据不足以把需求形式精确钉死到某个 logit 变体。 在供给侧，供给侧并非完全缺席，作者至少把进入、定价或市场结构响应嵌进均衡框架。 识别与估计上，识别依赖工具变量、GMM 或其他矩条件来处理价格与产品属性的内生性。

**这篇相对标准 BLP 改了什么**
把政策设计问题直接放进 EV 与充电基础设施的网络反馈系统里，讨论哪种补贴组合最优。

**文中模型骨架（按本文整理）**
```tex
q_t = q_t(N_t, p_t, x_t)

Q_t = \sum_{b \le t} q_b \, s_{t,b}

N_t = N_t(Q_t, z_t)
\quad \text{or} \quad
\pi^{station}_n = \text{entry profits}(Q_t, N_t, subsidy_t)
```

**这个模型骨架在本文里怎么读**
这里把 BLP 的汽车需求部分与充电站供给或进入方程联立起来，核心是正向反馈：车多了站更值得建，站多了车更容易卖。模型因此特别适合回答 EV 补贴与充电补贴应如何搭配。 放到这篇论文里，最关键的 paper-specific 改造是：把政策设计问题直接放进 EV 与充电基础设施的网络反馈系统里，讨论哪种补贴组合最优。 因此它最终能回答的问题，不只是“消费者是否会替代”，还包括：模型的终点不是参数本身，而是福利、反事实和政策比较。

**OCR 原文模型片段**
```text
quantity of fuel consumed is X.

The gross consumer surplus from consuming X vehicles with K refueling stations is S ( X , K ) = s ( X ) - \beta r ( K ) X . . The term s(X) is the utility from transportation and vehicle ownership, a positive, increasing and strictly concave function with s ( 0 ) = 0 , s ^ { \prime } ( X ) \geq 0 and s ^ { \prime \prime } ( X ) < 0 for X \geq 0 . The term \beta r ( K ) is the utility loss per vehicle associated with refueling, the cost to search and reach a refueling station. It is positive, decreasing and concave with r ( 0 ) = + \infty and r ^ { \prime } ( 0 ) = - \infty . For convenience the parameter \beta \geq 0 is referred to as the range anxiety factor.

Pollution, either climatic change or local air quality, from fossil fuel vehicles is not explicitly modeled but implicitly perfectly priced (at the Pigouvian level) and embedded into the willingness to pay s(X) for the new clean vehicle.

The total cost to produce X vehicles is C _ { V } ( X ) X . The unit production cost is decreasing with the total quantity produced : C _ { V } ^ { \prime } ( X ) \leq 0 , C _ { V } ^ { \p
```

```text
{ V } ^ { \prime } ( X ) \leq 0 , C _ { V } ^ { \prime \prime } ( X ) \geq 0 . . This will be simply referred as the scale effect; it integrates several phenomena (scale at such, supply chain effects, learning by doing) which we assume spills over from one firm to the other. We assume that it is relatively small: s ( X ) - C _ { V } ( X ) X is concave. Operating a refueling station incurs a fixed cost f , and a convex cost C _ { F } ( \boldsymbol { x } ) , to provide x units of fuel, with C _ { F } ( 0 ) = 0 , C _ { F } ^ { \prime } ( x ) > 0 and C _ { F } ^ { \prime \prime } ( x ) > 0 \mathrm { ~ f o r ~ } x \ge 0 . The strict convexity captures the capacity constraint of a refueling station.4
```

**我对这篇模型的具体解释**
1. 先看研究对象：零排放汽车部署的最优政策与网络效应。这决定了作者为什么需要结构模型而不是只做 reduced-form。
2. 再看需求侧：全文表明作者在做结构化产品需求分析，但 OCR 证据不足以把需求形式精确钉死到某个 logit 变体。
3. 再看供给/均衡：供给侧并非完全缺席，作者至少把进入、定价或市场结构响应嵌进均衡框架。
4. 真正的 paper-specific 改造是：把政策设计问题直接放进 EV 与充电基础设施的网络反馈系统里，讨论哪种补贴组合最优。
5. 所以这篇模型最终服务于：模型的终点不是参数本身，而是福利、反事实和政策比较。

**主要发现与模型输出**
- We also introduce the market power of vehicle producers and scale effects in the production function.
- We analyze the impact of indirect network effects in the deployment of zero emission vehicles in a static partial equilibrium model.

**模型锚点**
- model: `2.1. Framework` (p.2) - 2.1. Framework We consider two complementary goods: Vehicles and refueling stations. The total quantity of vehicles is X and the number of refueling stations K. The distance traveled per vehicle, and hence the quantity o
- counterfactual: `Optimal policy and network effects for the deployment of zero emission vehicles-` (p.0) - Optimal policy and network effects for the deployment of zero emission vehicles- Guy Meunier a,b,∗ , Jean-Pierre Ponssard b,c a INRA-UR1303 ALISS France b CREST - Ecole Polytechnique France c CNRS France
- conclusion: `7. Discussion, caveats, and extensions` (p.15) - 7. Discussion, caveats, and extensions Several important features of the transportation sector and electric mobility have not been considered in our model.

---

### Providing the Spark: Impact of financial incentives on battery electric vehicle adoption (`I6ZAU5HX`)

- 研究方向：BEV 购车激励与采用响应
- BLP 类型：BLP 邻近结构政策模型
- 这篇在问什么：To overcome adoption barriers and promote battery electric vehicles (BEVs) as an energy e cient consumer transportation option, a number of states o er subsidies to consumers for BEVs.

**这篇如何利用 BLP**
这篇论文的模型定位是“BLP-adjacent structural policy model”。 它使用的是“耐用品离散选择 + 运营成本/政策比较”这一类结构框架。 在需求侧，全文表明作者在做结构化产品需求分析，但 OCR 证据不足以把需求形式精确钉死到某个 logit 变体。 在供给侧，供给侧并非完全缺席，作者至少把进入、定价或市场结构响应嵌进均衡框架。 识别与估计上，识别主要靠制度冲击或自然实验，把外生变化灌进结构模型。

**这篇相对标准 BLP 改了什么**
围绕电动车激励的呈现形式、州级政策和技术新颖性来构造 EV 采用需求，而不是只套标准汽车 BLP。

**文中模型骨架（按本文整理）**
```tex
u_{ijt} = x_{jt}\beta_i - \alpha_i p_{jt} - \kappa_i \cdot \text{OperatingCost}_{jt} + \xi_{jt} + \varepsilon_{ijt}

\Pr(j) = \frac{\exp(u_{ijt})}{1+\sum_k \exp(u_{ikt})}

\text{Policy counterfactuals compare taxes, subsidies, labels, or standards}
```

**这个模型骨架在本文里怎么读**
它保留了差异化耐用品选择的结构需求主线，把运营成本、标签或补贴等政策变量直接写进选择问题，再比较不同政策对采用、能耗和福利的影响。 放到这篇论文里，最关键的 paper-specific 改造是：围绕电动车激励的呈现形式、州级政策和技术新颖性来构造 EV 采用需求，而不是只套标准汽车 BLP。 因此它最终能回答的问题，不只是“消费者是否会替代”，还包括：模型的终点不是参数本身，而是福利、反事实和政策比较。

**OCR 原文模型片段**
```text
## Journal Pre-proof

Providing the Spark: Impact of financial incentives on battery electric vehicle adoption

Bentley Clinton, Daniel Steinberg

![](images/4a80da726018137a68d6ee52b7b08c27270ee5a2491eaf2f465d5959933559cc.jpg)

PII: S0095-0696(18)30311-5

DOI: https://doi.org/10.1016/j.jeem.2019.102255

Reference: YJEEM 102255

To appear in: Journal of Environmental Economics and Management

Received Date: 28 January 2016

Revised Date: 30 June 2019

Accepted Date: 27 August 2019

Please cite this article as: Clinton, B., Steinberg, D., Providing the Spark: Impact of financial incentives on battery electric vehicle adoption, Journal of Environmental Economics and Management (2019), doi: https://doi.org/10.1016/j.jeem.2019.102255.

This is a PDF file of an article that has undergone enhancements after acceptance, such as the addition of a cover page and metadata, and formatting for readability, but it is not yet the definitive version of record. This version will undergo additional copyediting, typesetting and r
```

```text
## Journal Pre-proof

Providing the Spark: Impact of financial incentives on battery electric vehicle adoption

Bentley Clinton, Daniel Steinberg

![](images/4a80da726018137a68d6ee52b7b08c27270ee5a2491eaf2f465d5959933559cc.jpg)

PII: S0095-0696(18)30311-5

DOI: https://doi.org/10.1016/j.jeem.2019.102255

Reference: YJEEM 102255

To appear in: Journal of Environmental Economics and Management

Received Date: 28 January 2016

Revised Date: 30 June 2019

Accepted Date: 27 August 2019

Please cite this article as: Clinton, B., Steinberg, D., Providing the Spark: Impact of financial incentives on battery electric vehicle adoption, Journal of Environmental Economics and Management (2019), doi: https://doi.org/10.1016/j.jeem.2019.102255.

This is a PDF file of an article that has undergone enhancements after acceptance, such as the addition of a cover page and metadata, and formatting for readability, but it is not yet the definitive version of record. This version will undergo additional copyediting, typ
```

**我对这篇模型的具体解释**
1. 先看研究对象：BEV 购车激励与采用响应。这决定了作者为什么需要结构模型而不是只做 reduced-form。
2. 再看需求侧：全文表明作者在做结构化产品需求分析，但 OCR 证据不足以把需求形式精确钉死到某个 logit 变体。
3. 再看供给/均衡：供给侧并非完全缺席，作者至少把进入、定价或市场结构响应嵌进均衡框架。
4. 真正的 paper-specific 改造是：围绕电动车激励的呈现形式、州级政策和技术新颖性来构造 EV 采用需求，而不是只套标准汽车 BLP。
5. 所以这篇模型最终服务于：模型的终点不是参数本身，而是福利、反事实和政策比较。

**主要发现与模型输出**
- We find that incentives offered as direct purchase rebates generate increased levels of new BEV registrations at a rate of approximately 8 percent per thousand dollars of incentive offered.
- To overcome adoption barriers and promote battery electric vehicles (BEVs) as an energy e cient consumer transportation option, a number of states o er subsidies to consumers for BEVs.

**模型锚点**
- estimation: `4. Empirical strategy` (p.12) - 4. Empirical strategy Our empirical approach builds on that of Gallagher and Muehlegger (2011) with modifications that address differences in potential determinants of adoption for hybrids and BEVs. We employ a fixed-eff
- results: `5. Results` (p.14) - 5. Results
- conclusion: `7. Conclusions` (p.25) - 7. Conclusions The effectiveness of subsidies that target new vehicle technologies is critical to the design of cost-effective strategies to reduce transportation-sector emissions. We study the ability of state-level fin

---

### The Economics of Attribute-Based Regulation: Theory and Evidence from Fuel Economy Standards (`BWI7CWGM`)

- 研究方向：属性型监管、CAFE 与产品设计扭曲
- BLP 类型：标准 BLP 需求-供给
- 这篇在问什么：This paper analyzes "attribute-based regulations," in which regulatory compliance depends upon some secondary attribute that is not the intended target of the regulation.

**这篇如何利用 BLP**
这篇论文的模型定位是“canonical BLP demand-supply”。 它使用的是“属性型监管与产品属性选择模型”这一类结构框架。 在需求侧，需求侧是结构化离散选择/差异化产品需求系统，重点是恢复替代关系与价格弹性。 在供给侧，供给侧是显式的：通常包含多产品定价、边际成本恢复、markup 变化和均衡反事实。 识别与估计上，识别依赖工具变量、GMM 或其他矩条件来处理价格与产品属性的内生性。

**这篇相对标准 BLP 改了什么**
不再只估计消费者对现有车型的选择，而是让监管规则 σ(a) 直接扭曲厂商对属性与能耗的联合设计。

**文中模型骨架（按本文整理）**
```tex
U_n(a_n, e_n) = F_n(a_n, e_n) - C(a_n, e_n) + I_n + \lambda_n \bigl(e_n - \sigma(a_n)\bigr)

W = \sum_n \theta_n \bigl(F_n(a_n,e_n) - C(a_n,e_n) + I_n\bigr) + \phi \sum_n e_n

\sigma(a_n) \text{ sets an attribute-based standard / notch}
```

**这个模型骨架在本文里怎么读**
这不是标准 BLP 车型需求，而是把产品属性 a 和能耗/排放 e 的联合选择放进监管约束里。它借用了结构产业组织的精神：消费者/厂商优化、监管规则改变相对价格和边际激励，再映射到产品设计与福利。 放到这篇论文里，最关键的 paper-specific 改造是：不再只估计消费者对现有车型的选择，而是让监管规则 σ(a) 直接扭曲厂商对属性与能耗的联合设计。 因此它最终能回答的问题，不只是“消费者是否会替代”，还包括：模型的终点不是参数本身，而是福利、反事实和政策比较。

**OCR 原文模型片段**
```text
ves and the degree of marginal cost equalization that the ABR is able to achieve.

A second possibility is distribution. Attribute basing can achieve distributional goals when the planner wishes to shift welfare across consumers or producers based on the secondary attribute. In this case, the eficiency costs of ABR that are our focus represent the cost of achieving distributional goals. For example, size-based fuel-economy regulations can be rationalized as a way of shifting welfare between firms that sell small vehicles and those that sell large vehicles (perhaps in order to favor domestic producers and their consumers). Our final proposition demonstrates conditions under which second-best policies will include attribute basing to achieve redistribution.

In the second part of our paper, we develop two complementary empirical methods that use quasi-experimental policy variation to identify key parameters necessary for assessing the costs and benefits of attribute basing. To do so, we analyze Japanese fuel-economy regulations, under which firms making heavier cars are allowed to have lower fuel economy. The Japan
```

```text
_ { n }$ . In our terminology, e is the targeted characteristic; a is the secondary attribute.

We model an attribute-based regulation as a mandate that requires $e _ { n } \geq \sigma ( a _ { n } )$ . This mandate acts as a constraint on the consumer's optimization problem. When compliance trading is allowed, the mandate must be met by the market on average, but individual products can make up a compliance gap by purchasing credits. We generally work with a linear attribute-based regulation, which has $e _ { n } \geq { \hat { \sigma } } a _ { n } + \kappa .$ where $\hat { \sigma }$ and κ are constants. Where we work with a more general function $\sigma ( a )$ , we assume it is differentiable and includes a constant term κ. We call $\sigma ^ { \prime } ( a _ { n } )$ , which equals $\hat { \sigma }$ for linear policies, the "attribute slope."

We assume a perfectly competitive supply side with no fixed costs per variety. This means that consumers can choose any bundle of a and e and pay a price $P ( \boldsymbol { a } , \boldsymbol { e } )$ that is equal to the marginal cost of production $C ( \boldsymbol { a } ,
```

**我对这篇模型的具体解释**
1. 先看研究对象：属性型监管、CAFE 与产品设计扭曲。这决定了作者为什么需要结构模型而不是只做 reduced-form。
2. 再看需求侧：需求侧是结构化离散选择/差异化产品需求系统，重点是恢复替代关系与价格弹性。
3. 再看供给/均衡：供给侧是显式的：通常包含多产品定价、边际成本恢复、markup 变化和均衡反事实。
4. 真正的 paper-specific 改造是：不再只估计消费者对现有车型的选择，而是让监管规则 σ(a) 直接扭曲厂商对属性与能耗的联合设计。
5. 所以这篇模型最终服务于：模型的终点不是参数本身，而是福利、反事实和政策比较。

**主要发现与模型输出**
- The key drawback to attribute basing is that it creates distortions in the attribute, and we show that those distortions are greater when the attribute is more responsive to policy.
- Keywords: fuel-economy standards, energy efficiency, corrective taxation, notches, bunching analysis JEL: H23, Q48, Q58, L62 ©2015 Koichiro Ito and James M.

**模型锚点**
- estimation: `3.3 Estimation of Excess Bunching at Notches` (p.21) - 3.3 Estimation of Excess Bunching at Notches Econometric estimation of excess bunching in kinked or notched schedules is relatively new in the economics literature. Saez (2010) estimates the income elasticity of taxpayer
- counterfactual: `4.3 Counterfactual Policy Simulations` (p.39) - 4.3 Counterfactual Policy Simulations
- conclusion: `5 Conclusion` (p.43) - 5 Conclusion This paper shows that attribute-based regulation is an imperfect substitute for fat policies with compliance trading. The key drawback to attribute basing is that it creates distortions in the attribute, and

---

### The Electric Vehicle Transition and the Economics of Banning Gasoline Vehicles (`UHH6VGYR`)

- 研究方向：EV 转型与禁售燃油车
- BLP 类型：BLP 邻近结构政策模型
- 这篇在问什么：We analyze this transition with a dynamic model capturing falling costs of electric vehicles, decreasing pollution from electricity, and increasing vehicle substitutability.

**这篇如何利用 BLP**
这篇论文的模型定位是“BLP-adjacent structural policy model”。 它使用的是“EV 转型/禁燃模型”这一类结构框架。 在需求侧，全文表明作者在做结构化产品需求分析，但 OCR 证据不足以把需求形式精确钉死到某个 logit 变体。 在供给侧，供给侧是显式的：通常包含多产品定价、边际成本恢复、markup 变化和均衡反事实。 识别与估计上，识别依赖工具变量、GMM 或其他矩条件来处理价格与产品属性的内生性。

**这篇相对标准 BLP 改了什么**
通过校准 EV 与燃油车的替代弹性和转型路径，讨论 bans、cross-price elasticity 和技术进步如何共同影响长期均衡。

**文中模型骨架（按本文整理）**
```tex
\text{Consumers choose between gasoline vehicles } G \text{ and EVs } X

U(G,X) = \text{benefit from mobility, prices, and substitution curvature}

\epsilon_{Gp_X},\ \epsilon_{Xp_G},\ \text{or calibrated substitution parameters}
\Rightarrow \text{transition, ban, and welfare simulations}
```

**这个模型骨架在本文里怎么读**
这类论文不是标准 micro BLP 估计，而是把替代弹性、价格和技术演进校准进一个交通转型模型，用来回答禁售燃油车、过渡路径和补贴退出的长期效果。 放到这篇论文里，最关键的 paper-specific 改造是：通过校准 EV 与燃油车的替代弹性和转型路径，讨论 bans、cross-price elasticity 和技术进步如何共同影响长期均衡。 因此它最终能回答的问题，不只是“消费者是否会替代”，还包括：模型的终点不是参数本身，而是福利、反事实和政策比较。

**OCR 原文模型片段**
```text
2 Model

Consider a continuous time model in which society benefits from the stock of gasoline and/or electric vehicles. The benefit per unit of time in dollars is given by U ( G , X ) where G(t) denotes the stock of gasoline vehicles and X(t) the stock of electric vehicles at time t . ^ { 4 } Letting U _ { G } and U _ { X } denote the partial derivatives, we assume U is concave with U _ { G } > 0 and U _ { X } > 0 . { ^ 5 } The degree of substitutability between gasoline and electric vehicles plays an important role in determining the transition between them. Substitutability can be measured by either the cross-partial derivative U _ { G X } or a cross-price elasticity, and the use of these concepts is interchangeable in our model.

The stocks of gasoline and electric vehicles evolve over time by production of new vehicles and retirement of existing vehicles due to events such as accidents and mechanical failure. Let g ( t ) denote the production of gasoline vehicles and x ( t ) denote the production of electric vehicle
```

```text
2 Model

Consider a continuous time model in which society benefits from the stock of gasoline and/or electric vehicles. The benefit per unit of time in dollars is given by U ( G , X ) where G(t) denotes the stock of gasoline vehicles and X(t) the stock of electric vehicles at time t . ^ { 4 } Letting U _ { G } and U _ { X } denote the partial derivatives, we assume U is concave with U _ { G } > 0 and U _ { X } > 0 . { ^ 5 } The degree of substitutability between gasoline and electric vehicles plays an important role in determining the transition between them. Substitutability can be measured by either the cross-partial derivative U _ { G X } or a cross-price elasticity, and the use of these concepts is interchangeable in our model.

The stocks of gasoline and electric vehicles evolve over time by production of new vehicles and retirement of existing vehicles due to events such as accidents and mechanical failure. Let g ( t ) denote the production of gasoline vehicles and x ( t ) denote the production of electric vehicles at time t. The
```

**我对这篇模型的具体解释**
1. 先看研究对象：EV 转型与禁售燃油车。这决定了作者为什么需要结构模型而不是只做 reduced-form。
2. 再看需求侧：全文表明作者在做结构化产品需求分析，但 OCR 证据不足以把需求形式精确钉死到某个 logit 变体。
3. 再看供给/均衡：供给侧是显式的：通常包含多产品定价、边际成本恢复、markup 变化和均衡反事实。
4. 真正的 paper-specific 改造是：通过校准 EV 与燃油车的替代弹性和转型路径，讨论 bans、cross-price elasticity 和技术进步如何共同影响长期均衡。
5. 所以这篇模型最终服务于：模型的终点不是参数本身，而是福利、反事实和政策比较。

**主要发现与模型输出**
- We find that a gasoline vehicle production ban can reduce deadweight loss if the cross-price elasticity is such that ceasing gasoline vehicle production would be first best.
- Our calibration to the US market shows a transition from gasoline vehicles is not optimal at current substitutability: a gasoline vehicle production ban would have large deadweight loss.

**模型锚点**
- model: `2 Model` (p.5) - 2 Model Consider a continuous time model in which society benefits from the stock of gasoline and/or electric vehicles. The benefit per unit of time in dollars is given by U ( G , X ) where G(t) denotes the stock of gaso
- counterfactual: `4 Simulation Results` (p.18) - 4 Simulation Results We use the open-source program BOCOP (2017) to simulate numerical solutions to (1) and (8). BOCOP implements a local optimization method in which the optimal control problem is approximated by a fini
- conclusion: `5 Conclusion` (p.36) - 5 Conclusion This paper studies the transition from gasoline vehicles to electric vehicles using a theoretical model and numerical simulations calibrated to the U.S. market. The theoretical model shows that BAU electric 

---

### The Evolution of Market Power in the U.S. Automobile Industry (`P5D5GNTW`)

- 研究方向：美国汽车业市场势力的长期演化
- BLP 类型：标准 BLP 需求-供给
- 这篇在问什么：We estimate a demand model using product-level data on market shares, prices, and attributes, and consumer-level data on demographics, purchases, and stated second choices.

**这篇如何利用 BLP**
这篇论文的模型定位是“canonical BLP demand-supply”。 它使用的是“标准 BLP 需求-供给框架”这一类结构框架。 在需求侧，需求侧是结构化离散选择/差异化产品需求系统，重点是恢复替代关系与价格弹性。 在供给侧，供给侧是显式的：通常包含多产品定价、边际成本恢复、markup 变化和均衡反事实。 识别与估计上，识别依赖工具变量、GMM 或其他矩条件来处理价格与产品属性的内生性。

**这篇相对标准 BLP 改了什么**
在标准汽车 BLP 上加入更丰富的 micro moments、second-choice data 和持续产品条件，用来追踪几十年 market power 的演进。

**文中模型骨架（按本文整理）**
```tex
u_{ijmt} = \delta_{jmt} + \mu_{ijmt} + \varepsilon_{ijmt},
\quad
\delta_{jmt} = x_{jt}\beta - \alpha p_{jmt} + \xi_{jmt}

s_{jmt} = \int \frac{\exp(\delta_{jmt}+\mu_{ijmt})}{1+\sum_k \exp(\delta_{kmt}+\mu_{ikmt})} dF_i

\pi_f = \sum_m \sum_{j \in J_f} (p_{jmt} - mc_{jmt}) M_{mt} s_{jmt},
\quad
p - mc = \Delta^{-1} s
```

**这个模型骨架在本文里怎么读**
核心是随机系数离散选择需求加多产品 Bertrand 定价。需求侧恢复替代矩阵，供给侧用一阶条件把价格、markup 和边际成本连起来，然后再做政策反事实或福利计算。 放到这篇论文里，最关键的 paper-specific 改造是：在标准汽车 BLP 上加入更丰富的 micro moments、second-choice data 和持续产品条件，用来追踪几十年 market power 的演进。 因此它最终能回答的问题，不只是“消费者是否会替代”，还包括：模型的终点不是参数本身，而是福利、反事实和政策比较。

**OCR 原文模型片段**
```text
4 Model

Our framework is a differentiated product demand and oligopoly pricing model following Berry et al. (1995), which is standard in the industrial organization literature.

4These data were collected from Wards Automotive Yearbooks of the corresponding years.

9
```

```text
se features will be subsumed into a quality residual which summarizes all characteristics not captured by readily available data like horsepower and vehicle size.

## 4 Model

Our framework is a differentiated product demand and oligopoly pricing model following Berry et al. (1995), which is standard in the industrial organization literature.

## 4.1 Consumers

Consumer i makes a discrete choice among the $J _ { t }$ options in the set $\mathcal { J } _ { t }$ of car models available in year t and an outside “no-purchase” option (indexed 0), choosing the option that delivers the maximum conditional indirect utility.5

Utility is a linear index of a vector of vehicle attributes $\left( \mathbf { x } _ { j t } \right)$ , price $\left( p _ { j t } \right)$ , an unobserved vehicle specific term $( \xi _ { j t } )$ , and an idiosyncratic consumer-vehicle specific term $( \epsilon _ { i j t } )$

$$
u _ { i j t } = \beta _ { i t } { \bf x } _ { j t } + \alpha _ { i t } p _ { j t } + \xi _ { j t } + \epsilon _ { i j t }\tag{1}
$$

The index i denotes an individual in a given year. We specify and estimate parametric dist
```

**我对这篇模型的具体解释**
1. 先看研究对象：美国汽车业市场势力的长期演化。这决定了作者为什么需要结构模型而不是只做 reduced-form。
2. 再看需求侧：需求侧是结构化离散选择/差异化产品需求系统，重点是恢复替代关系与价格弹性。
3. 再看供给/均衡：供给侧是显式的：通常包含多产品定价、边际成本恢复、markup 变化和均衡反事实。
4. 真正的 paper-specific 改造是：在标准汽车 BLP 上加入更丰富的 micro moments、second-choice data 和持续产品条件，用来追踪几十年 market power 的演进。
5. 所以这篇模型最终服务于：模型的终点不是参数本身，而是福利、反事实和政策比较。

**主要发现与模型输出**
- Although real prices rose, we find that markups decreased substantially, and the fraction of total surplus accruing to consumers increased.
- We relate trends in consumer welfare and markups to trends in market structure and the composition of products.

**模型锚点**
- model: `4 Model` (p.8) - 4 Model Our framework is a differentiated product demand and oligopoly pricing model following Berry et al. (1995), which is standard in the industrial organization literature. 4These data were collected from Wards Autom
- estimation: `5 Estimation and Results` (p.11) - 5 Estimation and Results We estimate the model using GMM, closely following the procedures outlined by Petrin (2002) and Berry et al. (2004). Our estimation procedure is implemented in three steps. We briefly outline eac
- conclusion: `7 Conclusion` (p.26) - 7 Conclusion Antitrust policy has come under scrutiny in the U.S. in recent years. Critics argue that weak antitrust enforcement from the 1980’s onward has led to an increasingly tight grip of large firms over product ma

---

### The impact of car specifications, prices and incentives for battery electric vehicles in Norway: Choices of heterogeneous consumers (`B9VX97UN`)

- 研究方向：挪威 BEV 需求、属性与激励政策
- BLP 类型：BLP 风格差异化需求
- 这篇在问什么：Electric vehicles (EVs), specifically Battery EVs (BEVs), can offer significant energy and emission savings over internal combustion engine vehicles.

**这篇如何利用 BLP**
这篇论文的模型定位是“BLP-style differentiated-product demand”。 它使用的是“耐用品离散选择 + 运营成本/政策比较”这一类结构框架。 在需求侧，需求侧是结构化离散选择/差异化产品需求系统，重点是恢复替代关系与价格弹性。 在供给侧，供给侧较轻或被外生化，论文重心更偏需求恢复、替代矩阵和消费者/社会福利。 识别与估计上，识别依赖工具变量、GMM 或其他矩条件来处理价格与产品属性的内生性。

**这篇相对标准 BLP 改了什么**
围绕 BEV 的电池续航、充电便利、价格和补贴构造异质消费者选择模型，突出电动车属性本身的需求作用。

**文中模型骨架（按本文整理）**
```tex
u_{ijt} = x_{jt}\beta_i - \alpha_i p_{jt} - \kappa_i \cdot \text{OperatingCost}_{jt} + \xi_{jt} + \varepsilon_{ijt}

\Pr(j) = \frac{\exp(u_{ijt})}{1+\sum_k \exp(u_{ikt})}

\text{Policy counterfactuals compare taxes, subsidies, labels, or standards}
```

**这个模型骨架在本文里怎么读**
它保留了差异化耐用品选择的结构需求主线，把运营成本、标签或补贴等政策变量直接写进选择问题，再比较不同政策对采用、能耗和福利的影响。 放到这篇论文里，最关键的 paper-specific 改造是：围绕 BEV 的电池续航、充电便利、价格和补贴构造异质消费者选择模型，突出电动车属性本身的需求作用。 因此它最终能回答的问题，不只是“消费者是否会替代”，还包括：即便没有直接出现 counterfactual 关键词，这类 BLP 论文通常也把估计结果转成弹性、价格响应和福利含义。

**OCR 原文模型片段**
```text
3. Model and estimation

Our objective is to identify the impacts of car specifications and prices on BEV purchase by heterogeneous consumers and explore how the impacts vary with or without various municipal incentives. In this paper, we choose discrete choice models for two reasons: (i) personal preferences can be inferred from aggregate sales data, in a privacy-preserving manner; (ii) a choice model mimics consumers’ purchasing decisions by modeling their utilities. Individual utilities represent consumers’ preferences over various considerations while choosing different goods, and the utility concept is generally used in economics to reveal consumers’ willingness to pay. In this section, we discuss our methodology to estimate the impacts of vehicle attributes and incentives using discrete choice models. To make this paper self-contained, we start off by briefly reviewing a discrete choice model with the assumption that all consumers are homogeneous in Section 3.1. In Section 3.2, we work with a more realistic model where consumers have distinct pre
```

```text
3. Model and estimation

Our objective is to identify the impacts of car specifications and prices on BEV purchase by heterogeneous consumers and explore how the impacts vary with or without various municipal incentives. In this paper, we choose discrete choice models for two reasons: (i) personal preferences can be inferred from aggregate sales data, in a privacy-preserving manner; (ii) a choice model mimics consumers’ purchasing decisions by modeling their utilities. Individual utilities represent consumers’ preferences over various considerations while choosing different goods, and the utility concept is generally used in economics to reveal consumers’ willingness to pay. In this section, we discuss our methodology to estimate the impacts of vehicle attributes and incentives using discrete choice models. To make this paper self-contained, we start off by briefly reviewing a discrete choice model with the assumption that all consumers ar
```

**我对这篇模型的具体解释**
1. 先看研究对象：挪威 BEV 需求、属性与激励政策。这决定了作者为什么需要结构模型而不是只做 reduced-form。
2. 再看需求侧：需求侧是结构化离散选择/差异化产品需求系统，重点是恢复替代关系与价格弹性。
3. 再看供给/均衡：供给侧较轻或被外生化，论文重心更偏需求恢复、替代矩阵和消费者/社会福利。
4. 真正的 paper-specific 改造是：围绕 BEV 的电池续航、充电便利、价格和补贴构造异质消费者选择模型，突出电动车属性本身的需求作用。
5. 所以这篇模型最终服务于：即便没有直接出现 counterfactual 关键词，这类 BLP 论文通常也把估计结果转成弹性、价格响应和福利含义。

**主要发现与模型输出**
- From the results, we find that both groups have similar taste over BEV technology improvement, prices and incentives.
- Such knowledge will be helpful for decision makers to evaluate the cost and benefits in building a charging station network.

**模型锚点**
- model: `3. Model and estimation` (p.2) - 3. Model and estimation Our objective is to identify the impacts of car specifications and prices on BEV purchase by heterogeneous consumers and explore how the impacts vary with or without various municipal incentives. 
- estimation: `3.3. Estimation process` (p.5) - 3.3. Estimation process Since there is no analytical method to solve Eq. (6), we apply the traditional iterative method of the BLP model to estimate unknown coefficients (Berry et al., 1995; Li et al., 2011; Nevo, 2000).
- results: `5. Results` (p.8) - 5. Results This section discusses the results and policy implications.
- conclusion: `6. Conclusions and discussion` (p.13) - 6. Conclusions and discussion Norway has a long history of research and government incentives for BEVs, and it also has the largest BEV market of the world, on a per capita basis. Unlike many survey-based studies, we hav

---

### The Market for Electric Vehicles: Indirect Network Effects and Policy Design (`ZGZYZSJQ`)

- 研究方向：EV 市场、间接网络效应与政策设计
- BLP 类型：BLP 邻近结构政策模型
- 这篇在问什么：The market for plug-in electric vehicles (EVs) exhibits indirect network effects due to the interdependence between EV adoption and charging station investment.

**这篇如何利用 BLP**
这篇论文的模型定位是“BLP-adjacent structural policy model”。 它使用的是“EV 需求 + 充电网络部署的双边网络模型”这一类结构框架。 在需求侧，需求侧是结构化离散选择/差异化产品需求系统，重点是恢复替代关系与价格弹性。 在供给侧，供给侧并非完全缺席，作者至少把进入、定价或市场结构响应嵌进均衡框架。 识别与估计上，识别依赖工具变量、GMM 或其他矩条件来处理价格与产品属性的内生性。

**这篇相对标准 BLP 改了什么**
把 EV 销量、存量和充电站数量联立成一个动态反馈系统，用 steady state 与过渡路径讨论政策设计。

**文中模型骨架（按本文整理）**
```tex
q_t = q_t(N_t, p_t, x_t)

Q_t = \sum_{b \le t} q_b \, s_{t,b}

N_t = N_t(Q_t, z_t)
\quad \text{or} \quad
\pi^{station}_n = \text{entry profits}(Q_t, N_t, subsidy_t)
```

**这个模型骨架在本文里怎么读**
这里把 BLP 的汽车需求部分与充电站供给或进入方程联立起来，核心是正向反馈：车多了站更值得建，站多了车更容易卖。模型因此特别适合回答 EV 补贴与充电补贴应如何搭配。 放到这篇论文里，最关键的 paper-specific 改造是：把 EV 销量、存量和充电站数量联立成一个动态反馈系统，用 steady state 与过渡路径讨论政策设计。 因此它最终能回答的问题，不只是“消费者是否会替代”，还包括：模型的终点不是参数本身，而是福利、反事实和政策比较。

**OCR 原文模型片段**
```text
2.1. Model Setup and Properties

We assume that EV sales q _ { t } ( N _ { t } , p _ { t } , x _ { t } ) depends on the number of public charging stations in the market (Nt), the price of the EV \left( { { p } _ { t } } \right) , and other product characteristics combined \left( x _ { t } \right) that affect consumers’ choice, such as the fuel cost.14 The installed base of EVs is the cumulative sum of EV sales minus scrappage by the time t , denoted by Q _ { t } = \Sigma _ { b = 1 } ^ { t } q _ { b } { * } s _ { t , b } , where s _ { t ^ { \prime } b } is the survival rate at time t for EVs sold in time h. The number of charging stations that have been built N _ { t } ( Q _ { t } , z _ { t } ) depends on the EV market size \mathcal { Q } _ { t } and other variables combined z _ { t } that might affect the fixed cost of investment. To facilitate the illustration, we specify the following functions for EV demand and charging station deployment:

The EV demand equation arises from a discrete cho
```

```text
2.1. Model Setup and Properties

We assume that EV sales q _ { t } ( N _ { t } , p _ { t } , x _ { t } ) depends on the number of public charging stations in the market (Nt), the price of the EV \left( { { p } _ { t } } \right) , and other product characteristics combined \left( x _ { t } \right) that affect consumers’ choice, such as the fuel cost.14 The installed base of EVs is the cumulative sum of EV sales minus scrappage by the time t , denoted by Q _ { t } = \Sigma _ { b = 1 } ^ { t } q _ { b } { * } s _ { t , b } , where s _ { t ^ { \prime } b } is the survival rate at time t for EVs sold in time h. The number of charging stations that have been built N _ { t } ( Q _ { t } , z _ { t } ) depends on the EV market size \mathcal { Q } _ { t } and other variables combined z _ { t } that might affect the fixed cost of investment. To facilitate the illustration, we specify the following functions for EV demand and charging station deployment:

The EV demand equation arises from a discrete choice model of vehicle demand and follows closely the logit model using the market
```

**我对这篇模型的具体解释**
1. 先看研究对象：EV 市场、间接网络效应与政策设计。这决定了作者为什么需要结构模型而不是只做 reduced-form。
2. 再看需求侧：需求侧是结构化离散选择/差异化产品需求系统，重点是恢复替代关系与价格弹性。
3. 再看供给/均衡：供给侧并非完全缺席，作者至少把进入、定价或市场结构响应嵌进均衡框架。
4. 真正的 paper-specific 改造是：把 EV 销量、存量和充电站数量联立成一个动态反馈系统，用 steady state 与过渡路径讨论政策设计。
5. 所以这篇模型最终服务于：模型的终点不是参数本身，而是福利、反事实和政策比较。

**主要发现与模型输出**
- The market for plug-in electric vehicles (EVs) exhibits indirect network effects due to the interdependence between EV adoption and charging station investment.

**模型锚点**
- model: `2.1. Model Setup and Properties` (p.12) - 2.1. Model Setup and Properties We assume that EV sales q _ { t } ( N _ { t } , p _ { t } , x _ { t } ) depends on the number of public charging stations in the market (Nt), the price of the EV \left( { { p } _ { t } } \
- estimation: `4. ESTIMATION RESULTS` (p.23) - 4. ESTIMATION RESULTS We first present parameter estimates for equations (4) and (5). We then discuss the indirect network effects implied by these parameter estimates.
- counterfactual: `2.2. Implications on Policy Choices` (p.13) - 2.2. Implications on Policy Choices Now we conduct simulations to understand how feedback loops magnify policy shocks and their implications on policy choices. We fix p _ { t } , x _ { t } , and z _ { t } in equations (1
- conclusion: `6. CONCLUSION` (p.39) - 6. CONCLUSION This study first demonstrates through a stylized model that positive indirect network effects in both EV demand and charging station deployment give rise to feedback loops that amplify shocks to the system 

---

### The Role of Government in the Market for Electric Vehicles: Evidence from China (`X8Y7RF84`)

- 研究方向：中国 EV 市场中的政府角色
- BLP 类型：BLP 邻近结构政策模型
- 这篇在问什么：This paper is a product of the Office of the Chief Economist, Infrastructure Vice Presidency.

**这篇如何利用 BLP**
这篇论文的模型定位是“BLP-adjacent structural policy model”。 它使用的是“耐用品离散选择 + 运营成本/政策比较”这一类结构框架。 在需求侧，全文表明作者在做结构化产品需求分析，但 OCR 证据不足以把需求形式精确钉死到某个 logit 变体。 在供给侧，供给侧较轻或被外生化，论文重心更偏需求恢复、替代矩阵和消费者/社会福利。 识别与估计上，识别依赖工具变量、GMM 或其他矩条件来处理价格与产品属性的内生性。

**这篇相对标准 BLP 改了什么**
用 EV adoption demand 把财政补贴、非财政激励和地方政策工具分解开来，量化政府在起步期市场形成中的作用。

**文中模型骨架（按本文整理）**
```tex
u_{ijt} = x_{jt}\beta_i - \alpha_i p_{jt} - \kappa_i \cdot \text{OperatingCost}_{jt} + \xi_{jt} + \varepsilon_{ijt}

\Pr(j) = \frac{\exp(u_{ijt})}{1+\sum_k \exp(u_{ikt})}

\text{Policy counterfactuals compare taxes, subsidies, labels, or standards}
```

**这个模型骨架在本文里怎么读**
它保留了差异化耐用品选择的结构需求主线，把运营成本、标签或补贴等政策变量直接写进选择问题，再比较不同政策对采用、能耗和福利的影响。 放到这篇论文里，最关键的 paper-specific 改造是：用 EV adoption demand 把财政补贴、非财政激励和地方政策工具分解开来，量化政府在起步期市场形成中的作用。 因此它最终能回答的问题，不只是“消费者是否会替代”，还包括：模型的终点不是参数本身，而是福利、反事实和政策比较。

**OCR 原文模型片段**
```text
ket share of trim/choice k in market c and time t and $s _ { 0 m t }$ is the share of consumers who do not purchasing an EV (i.e., choose an outside option instead). This (linear) logit demand function is an aggregation of choices made by individuals with homogeneous consumer preference (Berry, 1994). Appendix Table A1 and A2 provides the estimates of the logit model. The implied price elasticity can be derived based on the price coefficient estimate in Appendix Table A1 as $\hat { \beta } _ { 1 } * p _ { k } * ( 1 - s _ { k } )$ or based on the estimate in Appendix Table A2 as ${ \hat { \beta } } _ { 1 } * ( 1 - s _ { k } )$ . The implied price elasticities are very similar between the two sets of tables since $s _ { j }$ is close to zero. In addition, the coefficient estimates on other variables are nearly identical as well.

It is important to note, with only EV models in our data, our analysis treats all other non-EV models to be in one category (i.e., the outside good). Limiting the choice set and the substitution pattern across choices could potentially impact the estimate of the price elasticity and policy
```

```text
9359

# The Role of Government in the Market for Electric Vehicles

Shanjun Li

Xianglei Zhu

Yiding Ma

Fan Zhang

Hui Zhou

Policy Research Working Paper 9359

## Abstract

To promote the development and diffusion of electric vehicles, central and local governments in many countries have adopted various incentive programs. This study examines the policy and market drivers behind the rapid development of the electric vehicle market in China, by far the largest one in the world. The analysis is based on the most comprehensive data on electric vehicle sales, local and central government incentive programs, and charging stations in 150 cities from 2015 to 2018. The study addresses the potential endogeneity of key variables, such as local policies and charging infrastructure, using the border regression

design and instrumental variable method. The analysis shows that central and local subsidies accounted for over half of the electric vehicles sold during the
```

**我对这篇模型的具体解释**
1. 先看研究对象：中国 EV 市场中的政府角色。这决定了作者为什么需要结构模型而不是只做 reduced-form。
2. 再看需求侧：全文表明作者在做结构化产品需求分析，但 OCR 证据不足以把需求形式精确钉死到某个 logit 变体。
3. 再看供给/均衡：供给侧较轻或被外生化，论文重心更偏需求恢复、替代矩阵和消费者/社会福利。
4. 真正的 paper-specific 改造是：用 EV adoption demand 把财政补贴、非财政激励和地方政策工具分解开来，量化政府在起步期市场形成中的作用。
5. 所以这篇模型最终服务于：模型的终点不是参数本身，而是福利、反事实和政策比较。

**主要发现与模型输出**
- We find that consumer subsidies for vehicle purchases accounted for more than half of EV sales in China.

**模型锚点**
- estimation: `3.2 Identification Strategy` (p.19) - 3.2 Identification Strategy We address the first two sources of endogeneity, unobserved product attributes and simultaneity using the instrumental variable method. For the third source of endogeneity, we use a cityborder
- counterfactual: `5 Policy Analysis` (p.27) - 5 Policy Analysis In this section, we conduct simulations to examine the role of the underlying driving factors behind the dramatic growth of China’s EV market. Based on the model estimates, we simulate the counterfactua
- conclusion: `6 Conclusion` (p.30) - 6 Conclusion This study provides to our knowledge the first empirical analysis on the underlying driving factors behind the rapid growth of the world’s largest EV market, China. The analysis is based on the most comprehe

---

### What does an electric vehicle replace? (`LXUZM7VX`)

- 研究方向：EV 替代关系与减排效果
- BLP 类型：标准 BLP 需求-供给
- 这篇在问什么：The emissions reductions from the adoption of a new transportation technology depend on the emissions from the new technology relative to those from the displaced technology.

**这篇如何利用 BLP**
这篇论文的模型定位是“canonical BLP demand-supply”。 它使用的是“标准 BLP 需求-供给框架”这一类结构框架。 在需求侧，需求侧基本可以判定为随机系数离散选择，是最接近经典 BLP 的主干写法。 在供给侧，供给侧较轻或被外生化，论文重心更偏需求恢复、替代矩阵和消费者/社会福利。 识别与估计上，识别依赖工具变量、GMM 或其他矩条件来处理价格与产品属性的内生性。

**这篇相对标准 BLP 改了什么**
把新车与二手车、燃油车与电动车放在统一随机系数效用里，直接回答“EV 到底替代了谁”。

**文中模型骨架（按本文整理）**
```tex
u_{ijmt} = \delta_{jmt} + \mu_{ijmt} + \varepsilon_{ijmt},
\quad
\delta_{jmt} = x_{jt}\beta - \alpha p_{jmt} + \xi_{jmt}

s_{jmt} = \int \frac{\exp(\delta_{jmt}+\mu_{ijmt})}{1+\sum_k \exp(\delta_{kmt}+\mu_{ikmt})} dF_i

\pi_f = \sum_m \sum_{j \in J_f} (p_{jmt} - mc_{jmt}) M_{mt} s_{jmt},
\quad
p - mc = \Delta^{-1} s
```

**这个模型骨架在本文里怎么读**
核心是随机系数离散选择需求加多产品 Bertrand 定价。需求侧恢复替代矩阵，供给侧用一阶条件把价格、markup 和边际成本连起来，然后再做政策反事实或福利计算。 放到这篇论文里，最关键的 paper-specific 改造是：把新车与二手车、燃油车与电动车放在统一随机系数效用里，直接回答“EV 到底替代了谁”。 因此它最终能回答的问题，不只是“消费者是否会替代”，还包括：模型的终点不是参数本身，而是福利、反事实和政策比较。

**OCR 原文模型片段**
```text
rs substitute among similarly priced vehicles, the EV substitutes are likely to be expensive new vehicles.

We define household i’s utility from purchasing vehicle model j as:

$$
u _ { i j } = \underbrace { \sum _ { k = 1 } ^ { K } x _ { j k } \overline { { \beta _ { k } } } - \alpha _ { 1 } l n p _ { j } + \xi _ { j } } _ { \delta _ { j } } + \underbrace { \alpha _ { 2 } \frac { l n p _ { j } } { Y _ { i } } + \sum _ { k r } x _ { j k } z _ { i r } \beta _ { k r } ^ { o } } _ { \mu _ { i j } } + \underbrace { \sum _ { k } x _ { j k } v _ { i k } \beta _ { k } ^ { u } } _ { \mu _ { i j } } + \varepsilon _ { i j } ,\tag{12}
$$

where $\delta _ { j }$ is the mean utility of vehicle model j which is constant across consumers in the same market. $x _ { j k }$ stands for the $k _ { t h }$ vehicle attribute for model j. We include horsepower, weight, gallons per mile,12 and some vehicle segment dummy variables as the observed vehicle attributes. Price $p _ { j }$ is the average transaction price observed from the survey data, which is constant for the same model by fuel type for all households buying a vehicle in the
```

```text
fuel type among different groups of consumers. Among gasoline buyers, 96.9 percent would consider another gasoline vehicle as a second choice, 2.9% percent would consider a hybrid vehicle model as an alternative, and only about 0.2 percent would consider either BEVs or PHEVs as substitutes. Gasoline vehicle buyers, who are the majority of new vehicle purchasers, are generally less interested in the EV technology. Hybrid vehicle buyers demonstrate a stronger preference of fuel economy, and 39.7 percent of them would consider another hybrid vehicle as an alternative choice. However, only 3 percent would consider EVs as second choices. Those consumers who purchase hybrid vehicles enjoy vehicles that save fuel cost but do not favor the plug-in feature of EVs. Both PHEV and BEV buyers show a strong interest into EVs: many of them are considering another EV as their second choices. However, 34.5 percent of PHEV buyers consider a hybrid vehicle as an alternative, and only 16.5 percent consider a BEV model. PHEV buyers are more willing to adopt the EV technology but are less interested in all-electric vehicles, probably
```

**我对这篇模型的具体解释**
1. 先看研究对象：EV 替代关系与减排效果。这决定了作者为什么需要结构模型而不是只做 reduced-form。
2. 再看需求侧：需求侧基本可以判定为随机系数离散选择，是最接近经典 BLP 的主干写法。
3. 再看供给/均衡：供给侧较轻或被外生化，论文重心更偏需求恢复、替代矩阵和消费者/社会福利。
4. 真正的 paper-specific 改造是：把新车与二手车、燃油车与电动车放在统一随机系数效用里，直接回答“EV 到底替代了谁”。
5. 所以这篇模型最终服务于：模型的终点不是参数本身，而是福利、反事实和政策比较。

**主要发现与模型输出**
- By simulating alternative subsidy designs, we find that a subsidy designed to provide greater incentives to low-income households would have been more cost effective and less regressive.
- The emissions reductions from the adoption of a new transportation technology depend on the emissions from the new technology relative to those from the displaced technology.

**模型锚点**
- estimation: `4.2. Identification` (p.8) - 4.2. Identification Consumer utility is composed of three parts: mean utility, observed heterogeneity, and unobserved heterogeneity. The linear parameters in the mean utility \overline { { \beta } } and \alpha _ { 1 } ar
- counterfactual: `6. Counterfactual analysis` (p.13) - 6. Counterfactual analysis In this section, we conduct simulations to examine the counterfactual vehicle fleet where we remove all EV models from the choice sets and where the EV subsidy were removed. The magnitude of th
- conclusion: `7. Discussion` (p.18) - 7. Discussion The results from our analysis come with several caveats. First, the estimates of the environmental benefits are relatively crude, as they do not incorporate spatial heterogeneity of the upstream emissions f

---

### Winners and Losers: the Distributional Effects of the French Feebate on the Automobile Market (`3XDZXLTP`)

- 研究方向：法国 feebate、汽车需求与分配效应
- BLP 类型：标准 BLP 需求-供给
- 这篇在问什么：Abstract I quantify the welfare and environmental gains and losses from a policy establishing an environmental tax/subsidy for new cars in France in 2008.

**这篇如何利用 BLP**
这篇论文的模型定位是“canonical BLP demand-supply”。 它使用的是“BLP 风格差异化产品需求”这一类结构框架。 在需求侧，需求侧基本可以判定为随机系数离散选择，是最接近经典 BLP 的主干写法。 在供给侧，供给侧是显式的：通常包含多产品定价、边际成本恢复、markup 变化和均衡反事实。 识别与估计上，识别依赖工具变量、GMM 或其他矩条件来处理价格与产品属性的内生性。

**这篇相对标准 BLP 改了什么**
在汽车需求里加入 municipality / demographic 异质性，再把 feebate 税补规则映射到不同地区与人群的福利分布上。

**文中模型骨架（按本文整理）**
```tex
u_{ijmt} = x_{jt}\beta_i - \alpha_i p_{jmt} + \xi_{jmt} + \varepsilon_{ijmt}

s_{jmt} = \int \frac{\exp(\delta_{jmt}+\mu_{ijmt})}{1+\sum_k \exp(\delta_{kmt}+\mu_{ikmt})} dF_i

\delta_{jmt} = x_{jt}\bar{\beta} - \bar{\alpha} p_{jmt} + \xi_{jmt}
```

**这个模型骨架在本文里怎么读**
这一类论文保留了 BLP 最关键的需求侧部分：消费者异质性、产品空间替代和价格响应。供给侧有时被简化、外生化，或者只在反事实阶段以较轻的方式处理。 放到这篇论文里，最关键的 paper-specific 改造是：在汽车需求里加入 municipality / demographic 异质性，再把 feebate 税补规则映射到不同地区与人群的福利分布上。 因此它最终能回答的问题，不只是“消费者是否会替代”，还包括：模型的终点不是参数本身，而是福利、反事实和政策比较。

**OCR 原文模型片段**
```text
3 Model

In this section, I present a model of demand and supply for new automobiles both under and in the absence of the feebate regulation. The model allows for heterogeneous preferences related to demographic characteristics. The demand is represented by a random coefficients logit model that is similar to the model used in Nurski and Verboven (2016). The supply model formalises the pricing strategies of car manufacturers, which are multi-product firms that compete with each other as in the standard model of Berry et al. (1995).

11

Table 2: Regression of the average characteristics of car purchases on the demographic characteristics of the municipality Note: The average price is in e100, rebate is in e10, and income is in e10,000. “%” stands for the percentage of households in each category. The household sizes and professional activities are in 10%. %Diesel is the share of diesel cars (in %). CO2 emissions are in g/km; CO, NOX and
```

```text
3 Model

In this section, I present a model of demand and supply for new automobiles both under and in the absence of the feebate regulation. The model allows for heterogeneous preferences related to demographic characteristics. The demand is represented by a random coefficients logit model that is similar to the model used in Nurski and Verboven (2016). The supply model formalises the pricing strategies of car manufacturers, which are multi-product firms that compete with each other as in the standard model of Berry et al. (1995).

11

Table 2: Regression of the average characteristics of car purchases on the demographic characteristics of the municipality Note: The average price is in e100, rebate is in e10, and income is in e10,000. “%” stands for the percentage of households in each category. The household sizes and professional activities are in 10%. %Diesel is the share of diesel cars (in %). CO2 emissions are in g/km; CO, NOX and HC emissions are in mg/km, and PM emissions are in mg/10 km. The reference categories are singles, retired and rural citi
```

**我对这篇模型的具体解释**
1. 先看研究对象：法国 feebate、汽车需求与分配效应。这决定了作者为什么需要结构模型而不是只做 reduced-form。
2. 再看需求侧：需求侧基本可以判定为随机系数离散选择，是最接近经典 BLP 的主干写法。
3. 再看供给/均衡：供给侧是显式的：通常包含多产品定价、边际成本恢复、markup 变化和均衡反事实。
4. 真正的 paper-specific 改造是：在汽车需求里加入 municipality / demographic 异质性，再把 feebate 税补规则映射到不同地区与人群的福利分布上。
5. 所以这篇模型最终服务于：模型的终点不是参数本身，而是福利、反事实和政策比较。

**主要发现与模型输出**
- Abstract I quantify the welfare and environmental gains and losses from a policy establishing an environmental tax/subsidy for new cars in France in 2008.

**模型锚点**
- model: `3 Model` (p.11) - 3 Model In this section, I present a model of demand and supply for new automobiles both under and in the absence of the feebate regulation. The model allows for heterogeneous preferences related to demographic character
- estimation: `3.4 Estimation` (p.15) - 3.4 Estimation I estimate the parameters of utility using the generalised method of moments. I use the standard aggregate demand and supply moments, as in Berry et al. (1995), complemented with micro-moments in the spiri
- conclusion: `3.5 Discussion` (p.17) - 3.5 Discussion The model is static and abstracts from the dynamic aspects related to the car purchase decision. Because a car is a durable good that is used for several years and can be sold on a second-hand car market, 

---


## 住宅能源、耐用品与绿色采用

### Consumer myopia, imperfect competition and the energy efficiency gap: Evidence from the UK refrigerator market (`UNMC2I56`)

- 研究方向：冰箱市场中的短视、竞争不完全与能效缺口
- BLP 类型：标准 BLP 需求-供给
- 这篇在问什么：The empirical literature on the energy efficiency gap concentrates on demand inefficiencies in the energy -using durables markets and finds evidence that consumers underestimate future energy costs when purchasing a new appliance.

**这篇如何利用 BLP**
这篇论文的模型定位是“canonical BLP demand-supply”。 它使用的是“带注意力/短视参数的结构需求”这一类结构框架。 在需求侧，需求侧更像嵌套 logit / 分层离散选择，保留了产品空间替代结构，但异质性比经典 BLP 更轻。 在供给侧，供给侧是显式的：通常包含多产品定价、边际成本恢复、markup 变化和均衡反事实。 识别与估计上，识别依赖工具变量、GMM 或其他矩条件来处理价格与产品属性的内生性。

**这篇相对标准 BLP 改了什么**
把 operating cost 的短视参数和 supply-side imperfect competition 放进同一个耐用品市场，从而分开比较“改偏好”和“改竞争”的政策效果。

**文中模型骨架（按本文整理）**
```tex
u_{ijt} = x_{jt}\beta_i - \alpha_i p_{jt} - \gamma_i \cdot \text{OperatingCost}_{jt} + \xi_{jt} + \varepsilon_{ijt},
\quad 0 < \gamma_i \le 1

\gamma_i < 1 \Rightarrow \text{consumers underweight future operating or fuel costs}
```

**这个模型骨架在本文里怎么读**
这里的核心改造是引入一个注意力或短视参数 γ，让未来运营成本在当期购买选择中被低估。论文通常再把这个需求侧缺陷与竞争不完全或供给反应结合起来做政策比较。 放到这篇论文里，最关键的 paper-specific 改造是：把 operating cost 的短视参数和 supply-side imperfect competition 放进同一个耐用品市场，从而分开比较“改偏好”和“改竞争”的政策效果。 因此它最终能回答的问题，不只是“消费者是否会替代”，还包括：模型的终点不是参数本身，而是福利、反事实和政策比较。

**OCR 原文模型片段**
```text
examine supply-side issues (see the literature review above) generally adopt a structural approach in which multi-product manufacturers compete à la Bertrand. In the context of a nested logit model, Berry (1994)
```

```text
3.2 Supply

In contrast to the demand equation, we adopt a reduced-form approach to assess the impact of imperfect competition on prices. Previous empirical contributions that examine supply-side issues (see the literature review above) generally adopt a structural approach in which multi-product manufacturers compete à la Bertrand. In the context of a nested logit model, Berry (1994)
```

**我对这篇模型的具体解释**
1. 先看研究对象：冰箱市场中的短视、竞争不完全与能效缺口。这决定了作者为什么需要结构模型而不是只做 reduced-form。
2. 再看需求侧：需求侧更像嵌套 logit / 分层离散选择，保留了产品空间替代结构，但异质性比经典 BLP 更轻。
3. 再看供给/均衡：供给侧是显式的：通常包含多产品定价、边际成本恢复、markup 变化和均衡反事实。
4. 真正的 paper-specific 改造是：把 operating cost 的短视参数和 supply-side imperfect competition 放进同一个耐用品市场，从而分开比较“改偏好”和“改竞争”的政策效果。
5. 所以这篇模型最终服务于：模型的终点不是参数本身，而是福利、反事实和政策比较。

**主要发现与模型输出**
- Using data on the UK refrigerator market (2002 -2007 ), we find that the average energy consumption of appliances sold during this period was only 7.2% higher than what would have been observed under a scenario with a perfectly competitive market and non-myopic consumers.
- One reason for this small gap is that market power actually reduces energy use The empirical literature on the energy efficiency gap concentrates on demand inefficiencies in the energy-using durables markets and finds evidence that consumers underestimate future energy costs when purchasing a new appliance.

**模型锚点**
- model: `3.2 Supply` (p.14) - 3.2 Supply In contrast to the demand equation, we adopt a reduced-form approach to assess the impact of imperfect competition on prices. Previous empirical contributions that examine supply-side issues (see the literatur
- estimation: `5. Estimation` (p.25) - 5. Estimation In this section, we specify the different equations and discuss identification issues.
- counterfactual: `7. Counterfactual simulations` (p.36) - 7. Counterfactual simulations In this section, we perform simulations to quantify the impact of the two identified market imperfections on energy consumption and consumer surplus. We analyze three counterfactual scenario
- results: `6. Results` (p.33) - 6. Results
- conclusion: `8. Conclusion` (p.42) - 8. Conclusion While the empirical literature on the energy efficiency gap in the residential sector has primarily focused on consumer behavior, this paper develops a comprehensive view of both demand-side and supply-side

---

### Consumer response to energy label policies: Evidence from the Brazilian energy label program (`EPWJ8S9T`)

- 研究方向：家电能效标签与消费者响应
- BLP 类型：BLP 风格差异化需求
- 这篇在问什么：Energy Policy xxx (xxxx) xxx Contents lists available at ScienceDirect Energy Policy journal homepage: www.elsevier.com/locate/enpol Consumer response to energy label policies: Evidence from the Brazilian energy label program✩ Cristian Husea, Claudio Lucindab,∗, Andre Ribeiro Cardosoc A R T I C L E I N F O 1.

**这篇如何利用 BLP**
这篇论文的模型定位是“BLP-style differentiated-product demand”。 它使用的是“耐用品离散选择 + 运营成本/政策比较”这一类结构框架。 在需求侧，需求侧基本可以判定为随机系数离散选择，是最接近经典 BLP 的主干写法。 在供给侧，供给侧并非完全缺席，作者至少把进入、定价或市场结构响应嵌进均衡框架。 识别与估计上，识别依赖工具变量、GMM 或其他矩条件来处理价格与产品属性的内生性。

**这篇相对标准 BLP 改了什么**
在耐用品选择里强调 operating costs 与标签信息如何影响异质家庭的选择与福利。

**文中模型骨架（按本文整理）**
```tex
u_{ijt} = x_{jt}\beta_i - \alpha_i p_{jt} - \kappa_i \cdot \text{OperatingCost}_{jt} + \xi_{jt} + \varepsilon_{ijt}

\Pr(j) = \frac{\exp(u_{ijt})}{1+\sum_k \exp(u_{ikt})}

\text{Policy counterfactuals compare taxes, subsidies, labels, or standards}
```

**这个模型骨架在本文里怎么读**
它保留了差异化耐用品选择的结构需求主线，把运营成本、标签或补贴等政策变量直接写进选择问题，再比较不同政策对采用、能耗和福利的影响。 放到这篇论文里，最关键的 paper-specific 改造是：在耐用品选择里强调 operating costs 与标签信息如何影响异质家庭的选择与福利。 因此它最终能回答的问题，不只是“消费者是否会替代”，还包括：论文明确把模型用于税收、补贴、禁令、标签或进入政策的反事实分析。

**OCR 原文模型片段**
```text
teristics – in particular lifetime expected operating costs – and interacting household demographics with product characteristics to control for endogeneity. Our choice model is a random coefficients logit model which accounts for consumer heterogeneity at the household level and can arbitrarily approximate any choice model (McFadden and Train, 2000). We allow for heterogeneity at the household level in both prices and operating costs. In fact, to more realistically conform with the institutional setting, where consumers knowingly face different choice environments, we will interact lifetime operating costs with period fixed-effects.

Contribution and related literature. This paper contributes to different strands of the literature. First, it contributes to the literature which examines the energy paradox (or energy efficiency gap). This literature goes back at least to Hausman (1979) and Dubin and McFadden (1984). Examples of papers quantifying the valuation of energy efficiency for appliances include Revelt and Train (1998) and Davis (2008), Davis et al. (2013) whereas Metcalf and Hassett (1999) examines the va
```

```text
which a household chooses the appliance that maximizes their conditional indirect utility taking into account a number of product characteristics – in particular lifetime expected operating costs – and interacting household demographics with product characteristics to control for endogeneity. Our choice model is a random coefficients logit model which accounts for consumer heterogeneity at the household level and can arbitrarily approximate any choice model (McFadden and Train, 2000). We allow for heterogeneity at the household level in both prices and operating costs. In fact, to more realistically conform with the institutional setting, where consumers knowingly face different choice environments, we will interact lifetime operating costs with period fixed-effects.

Contribution and related literature. This paper contributes to different strands of the literature. First, it contributes to the literature which examines the energy paradox (or energy efficiency gap). This literature goes back at least to Hausman (1979) and Dubin and McFadden (1984). Examples of papers quantifying the valuation of energy efficiency
```

**我对这篇模型的具体解释**
1. 先看研究对象：家电能效标签与消费者响应。这决定了作者为什么需要结构模型而不是只做 reduced-form。
2. 再看需求侧：需求侧基本可以判定为随机系数离散选择，是最接近经典 BLP 的主干写法。
3. 再看供给/均衡：供给侧并非完全缺席，作者至少把进入、定价或市场结构响应嵌进均衡框架。
4. 真正的 paper-specific 改造是：在耐用品选择里强调 operating costs 与标签信息如何影响异质家庭的选择与福利。
5. 所以这篇模型最终服务于：论文明确把模型用于税收、补贴、禁令、标签或进入政策的反事实分析。

**主要发现与模型输出**
- Energy Policy xxx (xxxx) xxx Contents lists available at ScienceDirect Energy Policy journal homepage: www.elsevier.com/locate/enpol Consumer response to energy label policies: Evidence from the Brazilian energy label program✩ Cristian Husea, Claudio Lucindab,∗, Andre Ribeiro Cardosoc A R T I C L E I N F O 5.

**模型锚点**
- estimation: `4. Empirical strategy` (p.4) - 4. Empirical strategy We specify a random coefficients logit model using householdlevel data. The starting point is a microeconomic model of rational behavior for individual households. Households buy one of the products
- results: `5. Results` (p.6) - 5. Results
- conclusion: `Conclusions and policy implications` (p.9) - Conclusions and policy implications This paper examines the effect of the PBE program, which mandated the adoption of (previously voluntarily adopted) energy labels. Using revealed preference data from a nationally repre

---

### Greenhouse Gas Abatement Cost Curves of the Residential Heating Market: A Microeconomic Approach (`96LPI5MZ`)

- 研究方向：居民供暖系统、减排成本曲线与政策比较
- BLP 类型：标准 BLP 需求-供给
- 这篇在问什么：In this paper, we develop a microeconomic approach to deduce greenhouse gas abatement cost curves of the residential heating sector.

**这篇如何利用 BLP**
这篇论文的模型定位是“canonical BLP demand-supply”。 它使用的是“耐用品离散选择 + 运营成本/政策比较”这一类结构框架。 在需求侧，需求侧是结构化离散选择/差异化产品需求系统，重点是恢复替代关系与价格弹性。 在供给侧，供给侧是显式的：通常包含多产品定价、边际成本恢复、markup 变化和均衡反事实。 识别与估计上，识别依赖工具变量、GMM 或其他矩条件来处理价格与产品属性的内生性。

**这篇相对标准 BLP 改了什么**
把家庭供暖系统选择放进结构化离散选择，并把碳税与投资补贴的福利成本直接转成减排成本曲线。

**文中模型骨架（按本文整理）**
```tex
u_{ijt} = x_{jt}\beta_i - \alpha_i p_{jt} - \kappa_i \cdot \text{OperatingCost}_{jt} + \xi_{jt} + \varepsilon_{ijt}

\Pr(j) = \frac{\exp(u_{ijt})}{1+\sum_k \exp(u_{ikt})}

\text{Policy counterfactuals compare taxes, subsidies, labels, or standards}
```

**这个模型骨架在本文里怎么读**
它保留了差异化耐用品选择的结构需求主线，把运营成本、标签或补贴等政策变量直接写进选择问题，再比较不同政策对采用、能耗和福利的影响。 放到这篇论文里，最关键的 paper-specific 改造是：把家庭供暖系统选择放进结构化离散选择，并把碳税与投资补贴的福利成本直接转成减排成本曲线。 因此它最终能回答的问题，不只是“消费者是否会替代”，还包括：模型的终点不是参数本身，而是福利、反事实和政策比较。

**OCR 原文模型片段**
```text
s are based on a microsimulation of private households’ investment decision for heating systems until 2030. The households’ investment behavior in the simulation is derived from a discrete choice estimation which allows investigating the welfare costs of different abatement policies in terms of the compensating variation and the excess burden. We simulate greenhouse gas abatements and welfare costs of carbon taxes and subsidies on heating system investments until 2030 to deduce abatement curves. Given utility maximizing households, our results suggest a carbon tax to be the welfare efficient policy. Assuming behavioral misperceptions instead, a subsidy on investments might have lower marginal greenhouse gas abatement costs than a carbon tax.

Keywords: Household behavior, discrete choice, Pigou, greenhouse gas abatement costs JEL classification: C35, C61, Q47, Q53, R21

ISSN: 1862 3808

## 1. Introduction and Background

The social costs of greenhouse gas emissions as a global externality are more and more spotlighted in the worldwide public discussion. Since the UNCED1 in Rio de Janeiro 1992, but latest since th
```

```text
Greenhouse Gas Abatement Cost Curves of the Residential Heating Market – a Microeconomic Approach.

AUTHORS Caroline Dieckhöner Harald Hecking

EWI Working Paper, No 12/16

Oktober 2012

Institute of Energy EconomicsInstitute Energy Economics at the University of Cologne (EWI)at of Cologne

Alte Wagenfabrik   
Vogelsanger Straße 321   
50827 Köln   
Germany

Tel.: +49 (0)221 277 29-100

Fax: +49 (0)221 277 29-400

www.ewi.uni-koeln.de

## CORRESPONDING AUTHOR

Caroline Dieckhöner

Institute of Energy Economics at the University of Cologne (EWI)

Tel: +49 (0)221 277 29-312

Fax: +49 (0)221 277 29-400

Caroline.Dieckhoener@ewi.uni-koeln.de

ISSN: 1862-3808

The responsibility for working papers lies solely with the authors. Any views expressed are those of the authors and do not necessarily represent those of the EWI.

# Greenhouse gas abatement cost curves of the residential heating market - a microeconomic approach

AUTHORS

Caroline Dieckhöner (EWI)
```

**我对这篇模型的具体解释**
1. 先看研究对象：居民供暖系统、减排成本曲线与政策比较。这决定了作者为什么需要结构模型而不是只做 reduced-form。
2. 再看需求侧：需求侧是结构化离散选择/差异化产品需求系统，重点是恢复替代关系与价格弹性。
3. 再看供给/均衡：供给侧是显式的：通常包含多产品定价、边际成本恢复、markup 变化和均衡反事实。
4. 真正的 paper-specific 改造是：把家庭供暖系统选择放进结构化离散选择，并把碳税与投资补贴的福利成本直接转成减排成本曲线。
5. 所以这篇模型最终服务于：模型的终点不是参数本身，而是福利、反事实和政策比较。

**主要发现与模型输出**
- We find that (i) welfare-based abatement costs are generally higher than pure technical equipment costs; (ii) given utility maximizing households a carbon tax is the most welfare-efficient policy and; (iii) if households are not utility maximizing, a subsidy on investments may have lower marginal greenhouse gas abatement costs than a carbon tax In this paper, we develop a microeconomic approach to deduce greenhouse gas abatement cost curves of the residential heating sector.
- 9 The compensating variation C V _ { n } is determined for each period y by an equation based on McFadden (1999) which is a generalization of the compensating variation of logit models introduced by Small and Rosen (1981).10 To determine the difference in consumer surpluses of the two scenarios with and without policy measures, we get: The amount of money that is needed to keep the original utility level and compensate for the additional costs C V _ { n } caused of the policy measures is then computed as follows: where c _ { n , j } ^ { \mathrm { p o l i c y } } indicates the respective total annual heating costs of household n with heating system j including a tax or subsidy and c _ { n , j } ^ { \mathrm { n o \ p o l i c y } } describes these costs without any policy measures.
- We investigate two policies: (i) a carbon tax and (ii) subsidies on heating system investments.

**模型锚点**
- counterfactual: `Welfare effects of different policies` (p.12) - Welfare effects of different policies The aggregated net utility in our model over all households that change their technology and install a new one in period (year) y \in { 2 0 1 0 } , . . . , 2030 is defined as follows
- results: `5. Results` (p.19) - 5. Results
- conclusion: `6. Conclusion` (p.26) - 6. Conclusion Analytically, we derive a welfare based greenhouse gas abatement curve, thereby taking into account household behavior and cost effects of policy measures. We implement the theory into the behavioral micros

---

### Hurdles and steps: Estimating demand for solar photovoltaics (`JKYIT7SD`)

- 研究方向：太阳能光伏采用、摩擦与政策组合
- BLP 类型：BLP 邻近结构政策模型
- 这篇在问什么：This paper estimates demand for residential solar photovoltaic (PV) systems using a new approach to address three empirical challenges that often arise with countdata: excess zeros, unobserved heterogeneity, and endogeneity of price.

**这篇如何利用 BLP**
这篇论文的模型定位是“BLP-adjacent structural policy model”。 它使用的是“太阳能采用的分阶段 / hurdle 结构需求”这一类结构框架。 在需求侧，全文表明作者在做结构化产品需求分析，但 OCR 证据不足以把需求形式精确钉死到某个 logit 变体。 在供给侧，供给侧较轻或被外生化，论文重心更偏需求恢复、替代矩阵和消费者/社会福利。 识别与估计上，识别依赖工具变量、GMM 或其他矩条件来处理价格与产品属性的内生性。

**这篇相对标准 BLP 改了什么**
不从标准 share inversion 出发，而是把采用过程拆成多重 hurdle，解释 rebate、许可流程和地方营销活动如何共同作用。

**文中模型骨架（按本文整理）**
```tex
\Pr(\text{adopt}_{it}) = \Pr(\text{clear hurdle 1}) \times \Pr(\text{clear hurdle 2}) \times \cdots

\text{Adoption depends on price, rebates, permitting frictions, and local programs}
```

**这个模型骨架在本文里怎么读**
这篇不是真正的 BLP 产品市场模型，而是把绿色技术采用拆成多个关卡。它仍然是结构需求思路：价格、制度摩擦和补贴共同决定采用概率，再用反事实比较政策组合。 放到这篇论文里，最关键的 paper-specific 改造是：不从标准 share inversion 出发，而是把采用过程拆成多重 hurdle，解释 rebate、许可流程和地方营销活动如何共同作用。 因此它最终能回答的问题，不只是“消费者是否会替代”，还包括：模型的终点不是参数本身，而是福利、反事实和政策比较。

**OCR 原文模型片段**
```text
s three empirical challenges that often arise with count data: excess zeros, unobserved heterogeneity, and endogeneity of price. Our results imply a price elasticity of demand for solar PV systems of −0-65. Counterfactual policy simulations indicate that reducing state financial incentives in half would have led to 9% fewer new installations in Connecticut in 2014. Calculations suggest a subsidy program cost of \$364/tCO2 assuming solar displaces natural gas. Our Poisson hurdle approach holds promise for modeling the demand for many new technologies.

Keywords. Count data, hurdle model, fixed effects, instrumental variables, Poisson, energy policy.

JEL classification. C33, C36, Q42, Q48.

## 1. Introduction

The market for rooftop solar photovoltaic (PV) systems has been growing rapidly around the world in the past decade. In the United States, there has been an increase in new installed capacity from under 500 MW in 2008 to over 4500 MW in 2013, along with a decrease in average (preincentive) PV system prices from over \$8/W in 2008 to just above \$4/W in 2013 (in 2014 dollars) (Barbose, Weaver, and Darghouth (
```

```text
nt data settings (e.g., Cameron and Trivedi (2013)). We estimate a hurdle model based on two data generating processes: a standard logit for whether a block group has at least one adoption and a zero-truncated Poisson that models the rate of adoptions conditional on a block group having an adoption. This hurdle model has a clear behavioral interpretation in our setting: the first installation in an area is a rare event, but once there are multiple installations, peer effects may begin to influence adoption and installers can focus marketing on the area, so we have a count process. In order to tackle unobserved heterogeneity and endogeneity of the price variable, we extend the hurdle model to accommodate fixed effects and instrumental variables.

At the basis of our approach is the conditional maximum likelihood (CMLE) estimator for fixed effects logit models introduced in a sequence of works by Rasch (1960, 1961), Andersen (1972), and Chamberlain (1980). Majo and van Soest (2011) show that this conditional maximum likelihood approach can also be applied to the zero-truncated Poisson framework and present an appli
```

**我对这篇模型的具体解释**
1. 先看研究对象：太阳能光伏采用、摩擦与政策组合。这决定了作者为什么需要结构模型而不是只做 reduced-form。
2. 再看需求侧：全文表明作者在做结构化产品需求分析，但 OCR 证据不足以把需求形式精确钉死到某个 logit 变体。
3. 再看供给/均衡：供给侧较轻或被外生化，论文重心更偏需求恢复、替代矩阵和消费者/社会福利。
4. 真正的 paper-specific 改造是：不从标准 share inversion 出发，而是把采用过程拆成多重 hurdle，解释 rebate、许可流程和地方营销活动如何共同作用。
5. 所以这篇模型最终服务于：模型的终点不是参数本身，而是福利、反事实和政策比较。

**主要发现与模型输出**
- We find that dropping incentives to Step 6 would have reduced the number of installations by 5% in 2014, while reducing incentives in half would have led to a 9% drop in installations in 2014.
- Other market failures, such as innovation market failures (van Benthem, Gillingham, and Sweeney (2008)), must be significant for the policy to be social welfare-improving.
- Calculations suggest a subsidy program cost of $364/tCO 2assuming solar displaces natural gas.

**模型锚点**
- counterfactual: `7. Policy analysis` (p.24) - 7. Policy analysis In this section, we highlight what our results imply for policies in the solar PV market in CT through a set of simple counterfactual simulations. We run three policy counterfactuals: a reduction in th
- results: `6. Results` (p.20) - 6. Results
- conclusion: `8. Conclusions` (p.28) - 8. Conclusions This study estimates the demand for solar PV systems using a new empirical approach: a Poisson hurdle model with fixed effects and instrumental variables. This approach allows us to tackle several key chal

---


## 平台、通信与服务市场结构

### Market Entry, Fighting Brands, and Tacit Collusion: Evidence from the French Mobile Telecommunications Market (`NY37LT4P`)

- 研究方向：法国移动通信进入、fighting brands 与 tacit collusion
- BLP 类型：标准 BLP 需求-供给
- 这篇在问什么：We study a major new entry in the French mobile telecommunications market, followed by the introduction of fighting brands by the three incumbents.

**这篇如何利用 BLP**
这篇论文的模型定位是“canonical BLP demand-supply”。 它使用的是“通信市场 BLP + 产品线扩张与进入”这一类结构框架。 在需求侧，全文表明作者在做结构化产品需求分析，但 OCR 证据不足以把需求形式精确钉死到某个 logit 变体。 在供给侧，供给侧并非完全缺席，作者至少把进入、定价或市场结构响应嵌进均衡框架。 识别与估计上，识别依赖工具变量、GMM 或其他矩条件来处理价格与产品属性的内生性。

**这篇相对标准 BLP 改了什么**
在标准 BLP 需求外，加入零售/批发双层寡头竞争和 subsidiary brands 的产品线扩张决策，用来解释 entry 之后的 fighting brand 现象。

**文中模型骨架（按本文整理）**
```tex
u_{ijt} = \alpha \log(y_{it} - p_j) + \beta_{it}' x_{jt} + \xi_{jt} + \varepsilon_{ijt}

s_{jt} = \int \frac{\exp(u_{ijt})}{1+\sum_k \exp(u_{ikt})} dF_i

\pi_f = \pi_f^{retail} + \pi_f^{wholesale}
\quad \text{with counterfactual product-line and entry decisions}
```

**这个模型骨架在本文里怎么读**
它把标准 BLP 需求搬到移动通信产品上，但进一步把零售、批发、进入和 fighting brand 决策并入同一个寡头环境，从而不只看价格竞争，还看 incumbents 为什么会主动扩张产品线来对冲 entry。 放到这篇论文里，最关键的 paper-specific 改造是：在标准 BLP 需求外，加入零售/批发双层寡头竞争和 subsidiary brands 的产品线扩张决策，用来解释 entry 之后的 fighting brand 现象。 因此它最终能回答的问题，不只是“消费者是否会替代”，还包括：论文明确把模型用于税收、补贴、禁令、标签或进入政策的反事实分析。

**OCR 原文模型片段**
```text
ese  sources  of  temporary  dynamics  but  
rather aims to control for them without taking a particular view.
Our model assumes that each consumer  i  receives indirect utility   u 
ijt
    from con-
suming mobile service product  j  among the set of  J   services available in market  t  
during  a  given  quarter.  The  market    t    refers  to  the  geographic  area  (region)  of  the  
consumer;  we  suppress  the  index  for  time  periods  to  simplify  the  notation.  Each  
mobile service product  j  is defined by tariff type (prepaid, postpaid, or forfait blo-
qué) and product brand (operator or subsidiary) following the structure of Table 3.
16
 
As BLP, we take the following specification for   u 
ijt
     :
(1)                                                       u 
ijt
     =     α log 
(
 y 
it
    −   p 
j
  
)
  +  β  
it
  ′      x 
jt
    +   ξ 
jt
    +   ε 
ijt
     ,
15 
A large literature has been devoted to estimating different types of  demand-side dynamics. Recent examples 
include Dubé, Hitsch, and Rossi (2009); Dubé, Hitsch, and Chintagunta (2010); Shcherbakov (2016); Weiergraeber 
(2
```

```text
2010).  Our  model  
does  not  attempt  to  distinguish  between  these  sources  of  temporary  dynamics  but  
rather aims to control for them without taking a particular view.
Our model assumes that each consumer  i  receives indirect utility   u 
ijt
    from con-
suming mobile service product  j  among the set of  J   services available in market  t  
during  a  given  quarter.  The  market    t    refers  to  the  geographic  area  (region)  of  the  
consumer;  we  suppress  the  index  for  time  periods  to  simplify  the  notation.  Each  
mobile service product  j  is defined by tariff type (prepaid, postpaid, or forfait blo-
qué) and product brand (operator or subsidiary) following the structure of Table 3.
16
 
As BLP, we take the following specification for   u 
ijt
     :
(1)                                                       u 
ijt
     =     α log 
(
 y 
it
    −   p 
j
  
)
  +  β  
it
  ′      x 
jt
    +   ξ 
jt
    +   ε 
ijt
     ,
15 
A large literature has been devoted to estimating different types of  demand-side dynamics. Recent examples 
include Dubé, Hitsch, and Rossi (2009); Dubé,
```

**我对这篇模型的具体解释**
1. 先看研究对象：法国移动通信进入、fighting brands 与 tacit collusion。这决定了作者为什么需要结构模型而不是只做 reduced-form。
2. 再看需求侧：全文表明作者在做结构化产品需求分析，但 OCR 证据不足以把需求形式精确钉死到某个 logit 变体。
3. 再看供给/均衡：供给侧并非完全缺席，作者至少把进入、定价或市场结构响应嵌进均衡框架。
4. 真正的 paper-specific 改造是：在标准 BLP 需求外，加入零售/批发双层寡头竞争和 subsidiary brands 的产品线扩张决策，用来解释 entry 之后的 fighting brand 现象。
5. 所以这篇模型最终服务于：论文明确把模型用于税收、补贴、禁令、标签或进入政策的反事实分析。

**主要发现与模型输出**
- Using an empirical oligopoly model, we find that the incumbents’ fighting brand strategies are difficult to rationalize as unilateral best responses.
- We study a major new entry in the French mobile telecommunications market, followed by the introduction of fighting brands by the three incumbents.

**模型锚点**
- OCR 章节锚点较弱，建议回到 `D:/codex/tmp/blp_full_read_20260417/parsed_all/NY37LT4P/NY37LT4P.llm.md` 搜索 `utility`, `demand`, `profit`, `policy` 等关键词。

---

### The Welfare Effects of Peer Entry: The Case of Airbnb and the Accommodation Industry (`2R3LE27E`)

- 研究方向：Airbnb 进入、住宿市场结构与福利
- BLP 类型：标准 BLP 需求-供给
- 这篇在问什么：We study the welfare effects of enabling peer supply through Airbnb in the accommodation industry.

**这篇如何利用 BLP**
这篇论文的模型定位是“canonical BLP demand-supply”。 它使用的是“酒店固定供给 + Airbnb 弹性供给框架”这一类结构框架。 在需求侧，需求侧是结构化离散选择/差异化产品需求系统，重点是恢复替代关系与价格弹性。 在供给侧，供给侧较轻或被外生化，论文重心更偏需求恢复、替代矩阵和消费者/社会福利。 识别与估计上，识别依赖工具变量、GMM 或其他矩条件来处理价格与产品属性的内生性。

**这篇相对标准 BLP 改了什么**
在差异化住宿需求上加入“酒店固定供给 vs Airbnb 弹性 peer supply”的供给二元结构，让高峰期和容量约束成为模型核心。

**文中模型骨架（按本文整理）**
```tex
u_{ijt} = \delta_{jt} + \mu_{ijt} + \varepsilon_{ijt}

\pi^{hotel}_f = \sum_t (p_{jt} - mc_{jt}) q_{jt}

\pi^{peer}_h = \sum_t (p_t - c_{ht}) \mathbf{1}\{p_t \ge c_{ht}\},
\quad
\text{peer supply is flexible and enters only when conditions are favorable}
```

**这个模型骨架在本文里怎么读**
需求侧仍然是差异化产品选择，但供给侧不再只是传统酒店的固定容量，而是加入了对价格和时间高度敏感的 peer hosts。模型因此能解释为什么 Airbnb 的福利效应集中在高峰时段和容量约束最强的城市。 放到这篇论文里，最关键的 paper-specific 改造是：在差异化住宿需求上加入“酒店固定供给 vs Airbnb 弹性 peer supply”的供给二元结构，让高峰期和容量约束成为模型核心。 因此它最终能回答的问题，不只是“消费者是否会替代”，还包括：模型的终点不是参数本身，而是福利、反事实和政策比较。

**OCR 原文模型片段**
```text
Consumer Demand

Consumers make a discrete choice between hotel tiers, Airbnb listing types, and an outside option for a given night. Consumer i has the following utility for room option j in market n:

For consumer i , \ \mu _ { i j n } represents a mean utility for accommodation j in market n inclusive of preference heterogeneity for the inside options. The price of an accommodation is denoted p _ { j n } , while \tau _ { j n } represents the percent difference between what the travelers pay and what the suppliers receive for accommodation j . . For hotels, \tau _ { j n } is simply the lodging tax rate. For Airbnb rooms, it is a combination of the Airbnb commission fee and the lodging tax rate if Airbnb collects it.21 Finally, \epsilon _ { i j n } is an idiosyncratic component with a type I extreme value distribution. We normalize the value of the outside option to 0 for all markets. This demand specification yields the following quan
```

```text
Consumer Demand

Consumers make a discrete choice between hotel tiers, Airbnb listing types, and an outside option for a given night. Consumer i has the following utility for room option j in market n:

For consumer i , \ \mu _ { i j n } represents a mean utility for accommodation j in market n inclusive of preference heterogeneity for the inside options. The price of an accommodation is denoted p _ { j n } , while \tau _ { j n } represents the percent difference between what the travelers pay and what the suppliers receive for accommodation j . . For hotels, \tau _ { j n } is simply the lodging tax rate. For Airbnb rooms, it is a combination of the Airbnb commission fee and the lodging tax rate if Airbnb collects it.21 Finally, \epsilon _ { i j n } is an idiosyncratic component with a type I extreme value distribution. We normalize the value of the outside option to 0 for all markets. This demand specification yields the following quantities for each accommodation type:

22

THE AMERICAN ECON
```

**我对这篇模型的具体解释**
1. 先看研究对象：Airbnb 进入、住宿市场结构与福利。这决定了作者为什么需要结构模型而不是只做 reduced-form。
2. 再看需求侧：需求侧是结构化离散选择/差异化产品需求系统，重点是恢复替代关系与价格弹性。
3. 再看供给/均衡：供给侧较轻或被外生化，论文重心更偏需求恢复、替代矩阵和消费者/社会福利。
4. 真正的 paper-specific 改造是：在差异化住宿需求上加入“酒店固定供给 vs Airbnb 弹性 peer supply”的供给二元结构，让高峰期和容量约束成为模型核心。
5. 所以这篇模型最终服务于：模型的终点不是参数本身，而是福利、反事实和政策比较。

**主要发现与模型输出**
- We study the welfare effects of enabling peer supply through Airbnb in the accommodation industry. We present a model of competition between flexible and dedicated sellers (peer hosts and hotels) who provide differentiated products.

**模型锚点**
- model: `Consumer Demand` (p.21) - Consumer Demand Consumers make a discrete choice between hotel tiers, Airbnb listing types, and an outside option for a given night. Consumer i has the following utility for room option j in market n: For consumer i , \ 

---


## 食品、标签与信息披露

### Equilibrium Effects of Food Labeling Policies (`S925QHZD`)

- 研究方向：食品警示标签、企业配方调整与均衡福利
- BLP 类型：标准 BLP 需求-供给
- 这篇在问什么：We study a regulation in Chile that mandates warning labels on products whose sugar or caloric concentration exceeds certain thresholds.

**这篇如何利用 BLP**
这篇论文的模型定位是“canonical BLP demand-supply”。 它使用的是“食品标签下的需求-供给均衡模型”这一类结构框架。 在需求侧，全文表明作者在做结构化产品需求分析，但 OCR 证据不足以把需求形式精确钉死到某个 logit 变体。 在供给侧，供给侧是显式的：通常包含多产品定价、边际成本恢复、markup 变化和均衡反事实。 识别与估计上，识别依赖工具变量、GMM 或其他矩条件来处理价格与产品属性的内生性。

**这篇相对标准 BLP 改了什么**
需求侧引入消费者对营养成分的误信念和标签信号，供给侧引入配方 reformulation 选择，因此政策不是单纯的信息披露，而是均衡重配。

**文中模型骨架（按本文整理）**
```tex
u_{ijt} = \delta_{ijt} - \alpha_i p_{jt} - w_{jt}\phi_i

E_{\pi_{ji}}[u_{ijt} \mid L_{jt}] = \delta_{ijt} - \alpha_i p_{jt} - E_{\pi_{ji}}[w_{jt} \mid L_{jt}] \phi_i

\pi_f = \sum_j \bigl(p_{jt} - c(w_{jt})\bigr) q_{jt},
\quad
f \text{ can reformulate } w_{jt}
```

**这个模型骨架在本文里怎么读**
需求侧把价格、口味和健康后果放进同一个效用函数，并允许消费者对真实营养成分有误信念；标签通过改变信念起作用。供给侧则允许企业同时调价格和营养成分，所以政策效果来自需求替代和供给重配两个通道。 放到这篇论文里，最关键的 paper-specific 改造是：需求侧引入消费者对营养成分的误信念和标签信号，供给侧引入配方 reformulation 选择，因此政策不是单纯的信息披露，而是均衡重配。 因此它最终能回答的问题，不只是“消费者是否会替代”，还包括：模型的终点不是参数本身，而是福利、反事实和政策比较。

**OCR 原文模型片段**
```text
re A.6, we show that results hold when we drop reformulated products.
17

product,p
jt
is its price in markett, andw
jt
is its vector of nutritional content.
25
We assume that the utility derived by individualiwhen purchasing productjcan be split into
three main components:
u
ijt
=δ
ijt
︸︷︷︸
experience/taste
−α
i
p
jt
︸
︷︷︸
price paid
−w
jt
φ
i
︸
︷︷︸
health consequences
(4)
whereδ
ijt
corresponds to the part of utility that comes from the experience of consuming product
jand is assumed to be observed by consumers when making the decision to buy the product.  It is
a function of all product characteristics, including taste
 ̄
δ
j
, and other individual- and product-level
demand shocks (e.g.  hunger relief, food craving, social status).
The second element in the utility function,α
i
p
jt
, corresponds to the disutility derived from paying
pricep
jt
for productj.  The parameterα
i
governs the price elasticity.
Finally,w
jt
φ
i
corresponds to the long-term health consequences of consuming unhealthy prod-
ucts.
26
We assume that consumers do not know the true nutritional content,w
jt
, but have beliefsπ
ji
about it.
```

```text
upply-side
responses can either offset or amplify the positive effects of food labels.  This paper studies the
equilibrium effectsof a regulation in Chile that mandates the use of warning labels on products
whose sugar or calorie concentration exceeds certain thresholds.  Using scanner data from Wal-
mart, we find an overall decrease in sugar and calorie intake of 9% and 7% after the policy.  To
reveal mechanisms, we zoom in on the breakfast cereal market.  On the demand side, we show
that consumers substitute from labeled to unlabeled products.  This effect is mostly driven by
products which, according to survey-based evidence, consumers mistakenly believed to be healthy.
On the supply side, we find substantial reformulation of products and bunching just below the
regulatory  thresholds.   We  develop  and  estimate  a  model  of  supply  and  demand  for  food  and
nutrients.  Consumers care about products’ price, taste, and nutritional content but have poorly
calibrated beliefs about nutrition.  Firms choose products’ prices and nutritional content to max-
imize profits.  We find that food labels increase cons
```

**我对这篇模型的具体解释**
1. 先看研究对象：食品警示标签、企业配方调整与均衡福利。这决定了作者为什么需要结构模型而不是只做 reduced-form。
2. 再看需求侧：全文表明作者在做结构化产品需求分析，但 OCR 证据不足以把需求形式精确钉死到某个 logit 变体。
3. 再看供给/均衡：供给侧是显式的：通常包含多产品定价、边际成本恢复、markup 变化和均衡反事实。
4. 真正的 paper-specific 改造是：需求侧引入消费者对营养成分的误信念和标签信号，供给侧引入配方 reformulation 选择，因此政策不是单纯的信息披露，而是均衡重配。
5. 所以这篇模型最终服务于：模型的终点不是参数本身，而是福利、反事实和政策比较。

**主要发现与模型输出**
- We show that consumers substitute from labeled to unlabeled products-a pattern mostly driven by products that consumers mistakenly believe to be healthy.
- We find that food labels increase consumer welfare by 1.8% of total expenditure, and that these effects are enhanced by firms' responses.
- We study a regulation in Chile that mandates warning labels on products whose sugar or caloric concentration exceeds certain thresholds.

**模型锚点**
- OCR 章节锚点较弱，建议回到 `D:/codex/tmp/blp_full_read_20260417/parsed_all/S925QHZD/S925QHZD.llm.md` 搜索 `utility`, `demand`, `profit`, `policy` 等关键词。

---
