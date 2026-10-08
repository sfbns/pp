---
title: "M1 基准 BLP 模型：工况重标如何进入随机系数需求系统"
subtitle: "从消费者效用最大化到可估计 GMM 系统的逐式推导（市场—年月—车型数据）"
date: "2026-10-08（第 3 版：按第 2 轮第三方审议修订）"
lang: zh-CN
---

# M1.0 本模型回答什么，以及与其他模型的关系

**一句话**：M1 是全课题的“共同需求核”。它从消费者在跨期预算约束下的效用最大化出发，推导出“车价 + 未来能源成本现值”构成的**广义价格**，把官方能耗/续航**标签**作为消费者形成能源成本与续航判断的信息输入放进广义价格与续航便利项，再按 BLP（1995）的随机系数 logit、Berry 反演、IV/GMM 与多产品 Bertrand 定价组成可估计系统。工况切换（NEDC→WLTC/CLTC）在 M1 中**不是政策虚拟变量**，而是对标签状态 $L_{jt}$ 的一次有日期的跳变；它对需求的作用必须经过“标签 → 主观能源成本/续航 → 效用 → **相对于所有其他选项的**效用变化 → 份额”这条结构链。

M1 直接回答用户的五个具体问题：

| 用户问题 | M1 的回答（详见所在小节） |
|---|---|
| 政策如何加入 BLP？放在效用的哪一部分？ | 进入广义价格中的“标签隐含能源成本” $\varphi_{d,c}K_{imt}L_{jt}$ 与 BEV 的续航便利项；不是自由系数的政策虚拟变量（§M1.4、§M1.8） |
| 用先前 $n$ 期油耗外推切换年的旧工况值再作差，以什么形式进入？ | 楔子 $W_j=L^{X}_{j}-\widehat L^{N}_{j}$ 定义标签跳变幅度、无改革反事实标签路径与预定工具；实际进入效用的是当期展示的标签 $L_{jt}$（§M1.8.2） |
| 燃油经济性/续航能否“单列一项”算边际效应？ | 可以且应当：它就是广义价格的能源成本项，系数与价格系数绑定；边际效应、弹性、支付意愿由 (M1.36)–(M1.39a) 给出（随机系数下为对类型分布的积分，需模拟计算）（§M1.9） |
| 口碑整体评分与分项评分如何构造？ | 分项是经验品质量的贝叶斯信号，按收缩后验均值进入；整体分是受限特例，可检验；能耗分项与车主实测进入信念（M2），不进口味项（§M1.6） |
| 新能源车的续航、电池如何进入？ | 由长途出行距离分布推出“续航缺口”$A_i(R)$，凸递减，与补能密度互为替代（§M1.5）；电池容量经续航进入、能量密度经质量—电耗—续航与补贴进入（§M1.7.2 注；详见 M4） |

**嵌套关系**：M1 用“比例信念”$B=\zeta_{d,c}L$ 得到在外部给定成本尺度下可识别的复合参数——标签成本估值率 $\varphi_{d,c}=\gamma_d\zeta_{d,c}$。M2 把信念推广为“标签 + 车主口碑”双信源贝叶斯后验；M3 把 $\varphi$ 分解为资本化率 $\gamma_d$ 与信念映射；M4 替代与电池；M5 异质性；M6 供给与创新；M7 反事实与福利。

**标注**：[O] 本轮对原页逐字核对的文献原式（BLP 1995 经项目核验底座逐式核对）；[O·卡] 文献卡片层（卡片记为原页核验、本轮未再开页）；[外] 外部已发表文献的结论（本地无精读卡）；[D] 本文推导；[P] 本项目设定；[I] 示例。记号沿用用户核验的 BLP 演练稿：$\delta$ 平均效用、$\mu$ 个体偏离、$\xi$ 未观测质量、$\Delta$ 定价矩阵、$\Delta^{-1}\tilde s$ 加价。

**记号表**（第 3 版统一，避免一符多义）：

| 符号 | 含义 | 符号 | 含义 |
|---|---|---|---|
| $c\in\lbrace N,X\rbrace$ | 工况制度（$N$=NEDC；$X$=新工况：燃油/混动/插混为 WLTC，纯电为中国工况） | $p_{jmt}$ | 消费者价（含税补，元） |
| $p^s_{jt}$ | 企业净收（不含增值税与消费税） | $\vartheta_{jt}$ | 税因子 $\partial p/\partial p^s$ |
| $t^v,\ t^{ct}_j,\ t^p_{jt}$ | 增值税、消费税（价外换算率）、购置税 | $\mathcal F_{jmt}$ | 车船税、牌照、保险等其他费用 |
| $L_{jt},\ T_{jm},\ B_{jt}$ | 标签、真实值、信念 | $W_j,\ w_j$ | 绝对楔子、相对楔子 |
| $K^{F}_{imt},\ K^{E}_{imt}$ | 燃油、电力成本尺度 | $\Lambda(r,\bar A)$ | 存活×里程衰减×贴现的年金因子 |
| $\zeta_{d,c}$ | 感知真实/标签比 | $\varphi_{d,c}=\gamma_d\zeta_{d,c}$ | 标签成本估值率 |
| $\gamma_d$ | 资本化率（M3） | $\kappa$ | 双信源标签精度权重（M2；M1 中等于 1） |
| $\mathcal C_{mt}$ | 补能密度 | $\chi(\mathcal C)$ | 补能调节函数 |
| $\mathrm{wt}_j$ | 整备质量 | $\mathbf d_i$ | 消费者人口特征 |
| $D^{day},\ D^{long}$ | 日行驶、长途单次距离 | $DR^{L}_{j\to k}$ | 标签转移率 |
| $\rho_\xi$ | $\xi$ 的 AR(1) 系数 | $\rho_{\mathrm{RRA}}$ | 相对风险厌恶系数 |
| $\tilde\Phi_{ij}\equiv\Phi_{ij}/\sigma_\varepsilon$ | 归一化服务流效用 | $N_{obs}$ | 观测数 |

---

# M1.1 数据结构、市场与时序

## M1.1.1 观测单位、产品层级与份额

观测单位为（产品 $j$，市场 $m$，月份 $t$）。**按用户数据，产品 $j$ 是“车型”**（同一车型的多个配置合并销量）；$m$ 为城市或省份（若只有全国数据则 $m$ 只有一个）；$d(j)\in\lbrace\mathrm I,\mathrm H,\mathrm P,\mathrm B\rbrace$ 依次为燃油车、油电混动、插电混动、纯电（同一车型的不同动力版本按动力拆为不同产品，若数据可拆）。$j=0$ 为外部选项（本月不购买新车）。

$$
s^{obs}_{jmt}=\frac{q_{jmt}}{M_{mt}},\qquad s^{obs}_{0mt}=1-\sum_{j\in\mathcal J_{mt}}s^{obs}_{jmt}>0. \tag{M1.1}
$$

$q_{jmt}$ 为终端销量（上险量优先；出厂量不是需求），$\mathcal J_{mt}$ 为实际在售集合，$M_{mt}$ 为潜在购买机会数。

**市场规模**[P]：参照 Li（2018）与 Ji 等（2026）“一半家庭为潜在新车买家”的做法 [O·卡]，令 $M_{mt}=\bar h\,\mathrm{HH}_{mt}/12$，基准 $\bar h=0.5$（每年一半家庭），敏感性 $\bar h\in\lbrace0.25,1\rbrace$。[I] 全国约 4.9 亿户、年零售约 2000 万辆时，基准下月度内部份额约 8%，外部份额约 0.92，远离 0；若取 $\bar h=0.07$，月度内部份额会高达约 0.58、峰月约 0.81，外部份额过小。须报告各 $(m,t)$ 的外部份额分布（最小值须明显大于 0），并展示 $\bar h$ 对弹性与福利的影响（Ji 等 2026 的市场规模稳健性显示部分系数变号 [O·卡]）。

**配置标签聚合到车型** [P]：标签按配置认证。车型层标签 $L_{jt}=\sum_{\ell\in j}\omega_{\ell jt}L_{\ell t}$，$\omega$ 为配置销量份额（若无配置销量，用在售配置的等权平均或主销配置，并作对比）。聚合引入测量误差 $e^{agg}_{jt}$，在推断中经全流程自助法传播；切换月若配置组合同时变化，须用固定配置篮子构造标签（只用切换前后都在售的配置）。**后果**：GRV（2018）赖以识别的“同车型不同发动机版本”变异在车型层数据中不可得，$\varphi$ 的识别改靠油价 × 标签的时变交互与同硬件跳变（§M1.11）。

## M1.1.2 时序（决定哪些变量是先决的）

1. 政府公布工况标准与法定时点。**不存在统一的“2021 年处理”**，须分别编码六种时钟：标准发布与实施日；新申请/已获型式批准车型的法定适用日；《公告》参数首次出现日；CCC 或目录换证日；**官方能耗标识启用日与作废日**；实际销售中首次出现新标签的月份。燃油车：GB/T 19233—2020（2021-01-01 实施）、GB 19578—2021（2021-07-01 实施），新申请型式批准车型 2021-07-01 起、已获批准车型 2023-01-01 前须满足新标准（此前允许并行与提前采用，属企业选择）；纯电：GB/T 18386.1—2021（2021-10-01 实施），过渡期可选 NEDC 或中国工况；混动与插混：GB/T 19753—2021（2021-10-01 实施），CCC 换版时钟（TC11-2021-01：新申请车型自决议发布起，既有获证车型自第 13 个月起）不同于燃油车；过渡期消费者能耗标识按车型实际采用的 NEDC、WLTC 或中国工况分别标注（装备中心〔2021〕290 号）。**第二次标签制度改革**：GB 22757.1—2023 与 GB 22757.2—2023 于 2024-07-01 实施，2024 年 7 月的联合通知把启用日定义为备案日、要求既有车型最迟 2024-09-01 前补备案并换标——这是与 2021 年工况转换相区分的标签格式改革（§M1.8.1）。消费者需求研究以“官方能耗标识启用日”为首选时钟 [O·卡：项目制度记忆]。
2. 企业观察需求冲击 $\xi$ 与成本冲击 $\omega$，在法定约束内选择认证与展示新标签的时点与价格。
3. 消费者在 $t$ 月观察价格、可观测特征、当期**展示**的标签 $L_{jt}$、截至 $t-1$ 的口碑 $Q_{j,t-1}$，作出购买选择。
4. 购车后真实能耗实现，车主发布口碑，成为以后消费者的信息。

---

# M1.2 消费者问题：从效用最大化到条件间接效用

## M1.2.1 跨期预算约束与 Fisher 分离 [D]

消费者 $i$ 面对完全资本市场（利率 $r$）。购买车型 $j$ 时，$a=0$ 期支付成交价 $p_{jmt}$，之后每期支付能源费用 $E_{ija}$。**以车辆整个使用寿命计**（存活概率 $S_a$ 刻画报废）。基准假设**持有至报废**（GRV 2018 式 (2) 以个体里程乘车辆寿命的做法 [O·卡]），或等价地“各任车主年里程相同”：此时整车寿命成本就是消费者面对的成本。若改用“完善二手车市场 + 里程异质”，首任车主的成本尺度须分段写为 $K^F_{imt}=\frac{\pi^F_{mt}}{100}\big[VKT_i\Lambda(r;1,H)+\overline{VKT}^{\,next}\Lambda(r;H+1,\bar A)\big]$（$\Lambda(r;a_1,a_2)=\sum_{a=a_1}^{a_2}S_av_a/(1+r)^a$，$H$ 为首任持有期），并相应改写外部选项（§M1.2.4 情形 B）；两种口径不可混用。现值预算约束为

$$
\sum_{a\ge0}\frac{\mathsf c_a}{(1+r)^a}=\mathcal W_i-p_{jmt}-\underbrace{\sum_{a=1}^{\bar A}\frac{S_a\,E_{ija}}{(1+r)^a}}_{\equiv PVE_{ij}}, \tag{M1.2}
$$

$\bar A$ 为最大车龄。完全资本市场下消费路径的最优安排与车辆选择可分离（Fisher 分离）。令 $\mathcal V_i(Y)$ 为给定财富 $Y$ 时最优安排消费的间接效用，$\Phi_{ij}$ 为车辆服务流效用现值：

$$
U_{ij}=\Phi_{ij}+\mathcal V_i\big(\mathcal W_i-p_{jmt}-PVE_{ij}\big). \tag{M1.3}
$$

（(M1.3) 要求车辆服务流与消费在效用中加性可分。能源费用含不确定性时，严格写法是期望效用；下式的一阶近似忽略风险项，风险扩展见 M2 §M2.9 的 CARA 确定性等价。）

## M1.2.2 准线性近似与收入边际效用 [D]

车辆终身成本 $TC_{ij}\equiv p_{jmt}+PVE_{ij}$ 相对终身财富较小，一阶展开：

$$
\mathcal V_i(\mathcal W_i-TC_{ij})=\mathcal V_i(\mathcal W_i)-\lambda_iTC_{ij}+O(TC_{ij}^2),\qquad \lambda_i\equiv\mathcal V_i'(\mathcal W_i)>0. \tag{M1.4}
$$

加入随机效用冲击 $\tilde\varepsilon_{ij}=\sigma_\varepsilon\varepsilon_{ij}$（$\varepsilon_{ij}$ 标准 I 型极值，独立同分布），以 $\sigma_\varepsilon$ 归一化尺度：

$$
u_{ij}\equiv\frac{U_{ij}+\tilde\varepsilon_{ij}}{\sigma_\varepsilon}\approx\frac{\Phi_{ij}+\mathcal V_i(\mathcal W_i)}{\sigma_\varepsilon}-\alpha_i\big(p_{jmt}+PVE_{ij}\big)+\varepsilon_{ij},\qquad \alpha_i\equiv\frac{\lambda_i}{\sigma_\varepsilon},\qquad \tilde\Phi_{ij}\equiv\frac{\Phi_{ij}}{\sigma_\varepsilon}. \tag{M1.5}
$$

**【参数定义 1：$\alpha_i$】** 价格系数 = 每元终身财富的效用（单位：$\varepsilon$ 尺度的效用/元；$\alpha_i>0$）。它**同时乘在购价与未来能源成本上**——这是预算约束“未来 1 元与今天 1 元可比”的含义，也是资本化率 $\gamma$ 能以“相对价格系数的比值”定义的根据。

## M1.2.3 收入异质性：$\alpha_i$ 的形式及其微观基础 [D]

BLP（1995）式 (2.7a) 用 $\alpha\log(y_i-p_j)$ [O]，对价格求导得 $-\alpha/(y_i-p_j)\approx-\alpha/y_i$。另一推导：若 $\mathcal V_i$ 为 CRRA（相对风险厌恶 $\rho_{\mathrm{RRA}}$），则 $\ln\lambda_i=\text{常数}-\rho_{\mathrm{RRA}}\ln\mathcal W_i$；若终身财富与收入成比例，则 $\partial\ln\alpha_i/\partial\ln y_i=-\rho_{\mathrm{RRA}}$。推广为

$$
\alpha_i=\exp\big(a_0+a_y\ln y_i+\sigma_p\nu_{ip}\big),\qquad \nu_{ip}\sim N(0,1),\qquad a_y=-\rho_{\mathrm{RRA}}. \tag{M1.6}
$$

$a_y=-1$ 对应 BLP 近似（对数效用）；BKL（2024）中国 EV 估计 $\alpha_2=-1.21\ (0.12)$ [O·卡]。对数正态保证 $\alpha_i>0$。（Ji 等 2026 的价格以 $\ln p$ 进入、系数为负对数正态，与本稿线性价格不同，只借鉴其收入交互形式 [O·卡]。）

## M1.2.4 外部选项：旧车能源成本与两种二手车市场假设 [D]

外部选项是“本月不买新车”：一部分消费者继续使用旧燃油车（置换型，$o_i=1$），一部分不拥车（首购型，$o_i=0$）。旧车能源成本怎样进入，取决于与 §M1.2.1 一致的二手车市场假设，**两种情形必须与新车成本尺度的口径配套**。

**情形 A（基准：持有至报废/旧车不经二手市场资本化）**：与 §M1.2.1 的基准口径一致。置换者若买新车，旧车报废或闲置；继续用旧车则承担其剩余能源成本：

$$
u_{i0}=\frac{\Phi_{i0}+\mathcal V_i(\mathcal W_i)}{\sigma_\varepsilon}-\alpha_i\,o_i\,\varphi^{0}\,K^{F,0}_{imt}\,\bar e_{0,m}+\varepsilon_{i0},\qquad K^{F,0}_{imt}=\frac{\pi^F_{mt}VKT_i\,\Lambda(r,\bar A_0)}{100}. \tag{M1.7}
$$

**情形 B（完善二手车市场）**：置换者以市场价 $P^u_{mt}$ 卖掉旧车，$P^u$ 已资本化边际二手买家的剩余能源成本 $\bar K^{F,0}_{mt}\bar e_{0,m}$；把对所有内部选项共同的 $\alpha_iP^u$ 移到外部选项一侧，只剩“自身成本偏离市场资本化成本”的部分：

$$
V^{B}_{i0}=\frac{\Phi_{i0}-\bar\Phi_0}{\sigma_\varepsilon}-\alpha_i\,o_i\,\varphi^{0}\big(K^{F,0}_{imt}-\bar K^{F,0}_{mt}\big)\bar e_{0,m}, \tag{M1.7b}
$$

其 $(m,t)$ 均值为零；此时新车的 $K^F$ 须用 §M1.2.1 的分段形式。

$\bar e_{0,m}$ 为市场 $m$ 在用旧车的真实油耗（外部给定，车主凭经验已知，不受工况改革影响——假设 A0），$\varphi^0$ 为旧车能源成本的估值率（旧车油耗已知、$\zeta=1$，故 $\varphi^0=\gamma_{\mathrm I}$）。情形 A 下位置归一化：

$$
V_{i0}=-\alpha_i\,o_i\,\varphi^{0}K^{F,0}_{imt}\bar e_{0,m},\qquad V_{ij}=\tilde\Phi_{ij}-\tilde\Phi_{i0}-\alpha_i\big(p_{jmt}+\widehat{PVE}_{ij}\big). \tag{M1.7a}
$$

**为什么不能省略**：外部选项的能源成本随油价与个体里程 $VKT_i$ 变化，时间不变的动力偏好 $\psi_{i,d}$ 吸收不了；动力×市场×月固定效应只吸收其 $(m,t)$ 均值，**个体偏离部分**改变各内部产品的买家构成。省略它会使“高里程消费者反而更倾向不买”（附录 M1.16 例 C：省略时 $\operatorname{corr}(K_i,P_{i0})=+0.33$，纳入后为 $-0.10$），并扭曲标签转移率（§M1.9）。Ji 等（2026）的福利稳健性同样把外部选项设为“继续开 5 年旧燃油车” [O·卡]。

**$\varphi^0$ 的识别与处理**：总份额对油价的反应是 $(m,t)$ 层变化，被 $\xi_{d,m,t}$ 全部吸收；$\varphi^0$ 只能经类型间异质性（油价变化通过 $\alpha_io_iK_i$ 的离散改变买家构成）识别，预期很弱。**基准把 $\varphi^0$ 固定于外部值**（$\gamma_{\mathrm I}=1$、GRV 的 0.91 [O·卡] 或 M3 的估计），报告敏感性。若自由估计 $\varphi^0$，它会在 M1 内分离 $\gamma_{\mathrm I}$ 与 $\zeta_{\mathrm I,c}=\varphi_{\mathrm I,c}/\varphi^0$——这条途径只靠函数形式与类型分布，本稿不依赖它（§M1.14）。**期限不对称**：新车按 $\bar A$ 年计、旧车按剩余 $\bar A_0$ 年计，$\bar A_0$ 之后的替换成本未入账，这是静态模型的近似，报告 $\bar A_0$ 的敏感性。尺度归一化 $\operatorname{Var}(\varepsilon)=\pi^2/6$ 使系数以 $\varepsilon$ 为单位，只有比值（支付意愿、估值率）有绝对含义。

## M1.2.5 完全信息、无行为偏差的基准 [D]

确知真实能耗、按市场利率贴现、充分注意时（略去与选择无关的常数）：

$$
u^{\ast}_{ij}=\tilde\Phi_{ij}-\alpha_i\big(p_{jmt}+PVE_{ij}\big)+\varepsilon_{ij}. \tag{M1.8}
$$

即 GRV（2018）式 (1) 在 $\gamma=1$ 的情形 [O·卡]（GRV 原式无残值项，与本文持有至报废的口径一致）。

---

# M1.3 生命周期能源成本：成本尺度 $K$ 的从零推导

## M1.3.1 燃油车与油电混动（ICE/HEV）[D]

车龄 $a$ 的能源费用 = 年行驶里程 × 每公里油耗 × 油价：

$$
E^{F}_{ija}=VKT_{i}v_a\cdot\frac{e^{F}_{jm}}{100}\cdot\pi^{F}_{m,t+a}, \tag{M1.9}
$$

$VKT_i$ 为首年年里程（km/年），$v_a$ 为里程随车龄的衰减（$v_1=1$），$e^{F}_{jm}$ 为真实道路油耗（L/100km），$\pi^{F}$ 为油价（元/L）。设油价期望为鞅（$E_t\pi_{m,t+a}=\pi_{mt}$；GRV 2018 [O·卡]，Anderson–Kellogg–Sallee 2013 经 GRV 卡转引 [外]）：

$$
PVE^{F}_{ij}=\underbrace{\frac{\pi^{F}_{mt}\,VKT_i\,\Lambda(r,\bar A)}{100}}_{\equiv K^{F}_{imt}}\;e^{F}_{jm},\qquad \Lambda(r,\bar A)\equiv\sum_{a=1}^{\bar A}\frac{S_a\,v_a}{(1+r)^a}. \tag{M1.10}
$$

**【参数定义 2：$K^F_{imt}$（燃油成本尺度）】** 单位：元/(L/100km)。由外部数据构造（油价、里程分布、存活与衰减曲线、利率），不是自由参数。外部选项用旧车剩余寿命 $\bar A_0$：$K^{F,0}_{imt}=\pi^F_{mt}VKT_i\Lambda(r,\bar A_0)/100$。量纲：$\pi$[元/L]×$VKT$[km/年]×$\Lambda$[年]÷100×$e$[L/100km] = 元。[I] $\pi=7.5$、$VKT=12000$、$r=5\%$、$\bar A=10$、$S_a=v_a=1$ 时 $\Lambda=7.72$，$K^F\approx6950$ 元；一辆 7.0 L/100km 的车标签上调 7.7%（约 0.54 L/100km），若被完全相信并完全资本化，约等于 3750 元现值。

**两个口径说明** [P]：（i）里程假设外生（不随油价反弹）；若引入里程的油价弹性 $\epsilon_{VKT}$，$K$ 对油价的反应小于比例，须在 $K$ 的构造中体现（§M1.11 的竞争解释）。（ii）调查中的里程分布通常以拥车/购车为条件，需映射到潜在买家总体（GRV 正文指向其在线附录 A.3 的映射，附录本地未读）。（iii）纯电电池衰减影响 $S_a$、$v_a$ 与续航，$\Lambda$ 可按动力设定；利率 $r$（车贷利率或存款利率）单列敏感性。

## M1.3.2 纯电（BEV）：有效电价与家充 [D]

$$
PVE^{E}_{ij}=K^{E}_{imt}\,e^{E}_{jm},\qquad
K^{E}_{imt}=\frac{\pi^{E}_{imt}\,VKT_i\,\Lambda(r,\bar A)}{100},\qquad
\pi^{E}_{imt}=h_i\,\pi^{home}_{mt}+(1-h_i)\,\pi^{pub}_{mt}, \tag{M1.11}
$$

$e^E$ 为插座端电耗（kWh/100km，含充电损耗），$h_i\in\lbrace0,1\rbrace$ 为是否有家充桩，$\pi^{home}$ 居民电价，$\pi^{pub}$ 公共快充电价含服务费。[I] 家充 0.55、公充 1.6 元/kWh 时，15 kWh/100km 的车十年现值约 7645 元与 22239 元——**家充可得性是巨大的异质性来源**（M5）。

## M1.3.3 插电混动（PHEV）：电驱里程份额 $UF$ 的推导 [D]

设有家充者每天从满电出发（$\tilde h_i=h_i\cdot f^{ch}_i$，$f^{ch}_i$ 为日充电概率），日行驶距离 $D^{day}_i\sim F^{day}_i$，前 $\min(D^{day},R)$ 公里用电：

$$
UF_i(R)=\tilde h_i\,\frac{E[\min(D^{day}_i,R)]}{E[D^{day}_i]},\qquad
\frac{\partial UF_i}{\partial R}=\tilde h_i\,\frac{\Pr(D^{day}_i>R)}{E[D^{day}_i]}\ge0, \tag{M1.12}
$$

（由 $\frac{d}{dR}\int_0^R(1-F^{day}(x))dx=\Pr(D^{day}>R)$。）一致性条件：$365\,E[D^{day}_i]=VKT_i$。每百公里费用与现值：

$$
\begin{aligned}
\pi^{P}_{ij}&=UF_i\big(\pi^{E}e^{E,CD}_{j}+\pi^{F}e^{F,CD}_{j}\big)+(1-UF_i)\,\pi^{F}e^{F,CS}_{j},\\
PVE^{P}_{ij}&=K^{F}_{imt}\big[UF_i\,e^{F,CD}_{j}+(1-UF_i)\,e^{F,CS}_{j}\big]+K^{E}_{imt}\,UF_i\,e^{E,CD}_{j}.
\end{aligned} \tag{M1.13}
$$

PHEV 的官方综合油耗是按标准 $UF^{c}$ 加权的复合值，与消费者自身的 $UF_i$ 不同；改革中 PHEV 综合油耗标签中位数上升约 59.3%、纯电续航中位数下降约 17.3%（本地同配置核对资产，引用前须按动力与指标复核）[P]。因此尽量用分项标签 $(L^{R,CD},L^{F,CS},L^{E,CD})$ 代入 (M1.13)；复合值与分项**不能同时**进入效用。

---

# M1.4 信息结构：标签、真实值、信念与 M1 的比例信念

## M1.4.1 三个永远分开的状态变量 [P]

对 $k\in\lbrace F,E,R\rbrace$：$L^{k}_{jt}$ 为 $t$ 月对消费者**展示**的标签（工况 $c(j,t)$）；$T^{k}_{jm}$ 为市场 $m$ 共同使用口径下的真实表现（工况切换本身不改变它）；$B^{k}_{ijmt}=E_i[T^{k}_{jm}\mid\mathcal I_{ijmt}]$ 为信念。**不默认 $L=T=B$；不把有名字的机制留在 $\xi$ 里再解释为认知。** 决策中出现的是信念：

$$
\widehat{PVE}^{F}_{ij}=E_i\big[K^{F}_{imt}T^{F}_{jm}\mid\mathcal I\big]=K^{F}_{imt}B^{F}_{ijmt}\quad(\text{$K$ 由公开油价与自身里程决定，与 $T$ 的主观不确定性独立}). \tag{M1.14}
$$

## M1.4.2 决策效用：资本化率与信念的乘积 [D]

允许决策时对未来能源成本赋予权重 $\gamma_d$。**基准含义**：在 M1.2 的完全资本市场与 Fisher 分离下，未来能源支出按市场利率完整资本化，充分理性的消费者 $\gamma_d=1$——即使其时间偏好是现时偏好的，因为车辆选择只通过财富现值影响预算集。$\gamma_d<1$ 需要偏离该基准：信贷约束（手到口）下的现时偏好、有限注意、或决策时使用高于市场利率的隐含贴现率；M3 推导这些微观基础及其不同的福利含义。M1 把 $\gamma_d$ 当作“as-if”决策权重：

$$
u^{D}_{ij}=\tilde\Phi_{ij}-\alpha_i\big(p_{jmt}+\gamma_{d}\,K_{imt}B_{ijmt}\big)+\varepsilon_{ij}. \tag{M1.15}
$$

**维持假设 A-$\gamma$**：$\gamma_d$ 不随所见标签的工况 $c$ 改变（M3 §M3.7 放松）。

**M1 的信息假设 A-M1（比例信念）**：

$$
B^{k}_{jt}=\zeta^{k}_{d,c}\,L^{k}_{jt},\qquad c=c(j,t)\in\lbrace N,X\rbrace. \tag{M1.16}
$$

**微观基础与理性预期锚点** [D]：若消费者认为在 $(d,c)$ 内真实能耗与标签之比与标签独立，$T_{jm}=\zeta^{true}_{d,c}L_{jt}\eta_{jm}$，$E[\eta_{jm}\mid L_{jt},d,c]=1$，则只看当期标签的消费者的条件期望为 $B_{jt}=E[T_{jm}\mid L_{jt},d,c]=\zeta_{d,c}L_{jt}$。该信息集下的理性预期值为 $\zeta^{RE}_{d,c}\equiv E[T/L\mid d,c]$（可用车主实测或道路测试数据外部构造，属外部矩，不由销量识别）；定义**信念校准指数** $\zeta_{d,c}/\zeta^{RE}_{d,c}$。若真实能耗不变且楔子与 $T/L^N$ 独立，$\zeta^{RE}_{d,X}/\zeta^{RE}_{d,N}=E[1/(1+w)]\approx1/(1+\bar w_d)$——因此 §M1.4.3 的基准 (b) 正是比例信念类中的理性预期基准，(a) 天真是偏离理性预期的基准。由此区分：**认证信息偏差收敛**＝$E\lvert\ln(T/L)\rvert$ 跨工况下降（标签本身的属性）；**信念校准改善**＝$\lvert\zeta_{d,c}/\zeta^{RE}_{d,c}-1\rvert$ 下降（消费者信念的属性）。

**【参数定义 3：$\zeta^k_{d,c}$（感知真实/标签比）】** 无量纲。$\zeta=1$ 照单全收；$\zeta=1.3$ 认为真实比标签高 30%。它是信念参数而非偏好参数。PHEV 的油、电标签共用一个 $\zeta^F_{\mathrm P,c}$ 是额外限制；$B$ 不随市场 $m$ 变而 $T_{jm}$ 随 $m$ 变（地区异质性见 M5）。代入 (M1.15)：

$$
u^{D}_{ij}=\tilde\Phi_{ij}-\alpha_i\Big(p_{jmt}+\varphi_{d,c}\,\underbrace{K_{imt}L_{jt}}_{\equiv G^{L}_{ijmt}}\Big)+\varepsilon_{ij},
\qquad \boxed{\varphi_{d,c}\equiv\gamma_d\,\zeta_{d,c}} \tag{M1.17}
$$

**【参数定义 4：$\varphi_{d,c}$（标签成本估值率）】** 由边际替代率定义：

$$
\varphi_{d,c}=\frac{\partial u^{D}_{ij}/\partial G^{L}_{ijmt}}{\partial u^{D}_{ij}/\partial p_{jmt}}. \tag{M1.18}
$$

含义：为抵消“标签隐含的生命周期能源成本”增加 1 元，消费者要求购价下降 $\varphi$ 元。$G^{L}=KL$ 称**标签隐含能源成本**。**$\varphi$ 只在外部给定的 $K$ 尺度（里程、利率、寿命、存活与衰减曲线）下识别**，误设会一比一进入 $\varphi$（与 GRV 中 $\gamma\rho$ 与里程尺度不可分同理 [O·卡]）；须报告 $r\times\bar A\times VKT$ 尺度的敏感性网格。$\varphi$ 是资本化率与信念映射的乘积，单凭标签变化无法拆开（M3 用第二信源拆开）。

## M1.4.3 三个信念基准（均为在 A-$\gamma$ 下的联合检验）[D]

令相对楔子 $w_j\equiv(L^{X}_j-\widehat L^{N}_j)/\widehat L^{N}_j$（全文统一为**相对**楔子；对数楔子另记 $\ln(1+w_j)$），$\bar w_d$ 为动力 $d$ 的平均楔子。

**(a) 天真表面值**：消费者未意识到工况换尺，$\zeta_{d,X}=\zeta_{d,N}$：

$$
H_0^{naive}:\ \varphi_{d,X}=\varphi_{d,N}. \tag{M1.19}
$$

**(b) 已知平均换算**：消费者按动力的平均换算系数整体换尺，平均楔子车型的信念不变：$\zeta_{d,X}(1+\bar w_d)=\zeta_{d,N}$，

$$
H_0^{avg}:\ \varphi_{d,X}\,(1+\bar w_d)=\varphi_{d,N}. \tag{M1.20}
$$

此时 $B_{post}/B_{pre}=(1+w_j)/(1+\bar w_d)$：偏离平均的楔子以表面值进入信念。在“只用当期标签”的信息集下，(b) 是比例信念类中的理性预期基准（上文微观基础）。这是比例信念的**机械推论**，不是“理性推断”的证明——消费者是否、以及在多大程度上把车型特有的楔子当作关于真实能耗的新信息，需要 M2 的贝叶斯信号结构（先验、精度）才能回答。

**(c) 真正的表示不变性**：若对每个车型新标签都是旧标签的已知一一映射，信息集不变，后验不变，**每个车型的效应都为零**（项目内核与构造协议对“表示不变性”的定义 [P]）：

$$
H_0^{RI}:\ B^{X}_{jt}=B^{N}_{jt}\ \ \forall j\quad\Longleftrightarrow\quad\varphi_{d,X}L^{X}_j=\varphi_{d,N}L^{N}_j\ \ \forall j. \tag{M1.20a}
$$

(M1.20a) 在比例信念下只有当所有车型楔子相同才能成立；楔子跨车型不同，正是官方换尺不自动满足表示不变性的原因。三个检验都以 A-$\gamma$ 为维持假设，因此是“信念 + 资本化不变”的联合检验。

---

# M1.5 续航与补能：续航缺口函数 $A_i(R)$ 的推导

## M1.5.1 从出行需要推出 [D]

消费者 $i$ 每年有 $n^{long}_i$ 次长途出行，单次距离 $D^{long}\sim F^{long}$（外部出行调查；与日行驶距离 $D^{day}$ 是不同的分布）。有效续航为 $R$ 时，单次“续航缺口”为 $(D^{long}-R)_+$。年期望缺口：

$$
A_i(R)=n^{long}_i\int_{R}^{\infty}\big(D-R\big)\,dF^{long}(D)=n^{long}_i\,E\big[(D^{long}-R)_+\big]. \tag{M1.21}
$$

由 Leibniz 法则（$g^{long}$ 为 $D^{long}$ 的密度）：

$$
A_i'(R)=-n^{long}_i\Pr(D^{long}>R)\le0,\qquad A_i''(R)=n^{long}_i\,g^{long}(R)\ge0. \tag{M1.22}
$$

## M1.5.2 进入效用与补能密度的替代关系 [P]+[D]

$$
-\eta_i\,\chi(\mathcal C_{mt})\,A_i\big(B^{R}_{ijmt}\big)\cdot\mathbf 1\lbrace d(j)=\mathrm B\rbrace,\qquad
\chi(\mathcal C)=\Big(\frac{\mathcal C}{\bar{\mathcal C}}\Big)^{-\varkappa},\ \varkappa\ge0, \tag{M1.23}
$$

**【参数定义 5：$\eta_i$、$\chi(\mathcal C)$】** $\eta_i$：每单位“年期望缺口公里数”所对应的终身效用损失（单位：效用/（km/年））；$\eta_i/\alpha_i$ 为其货币价值。$\chi(\mathcal C)$ 为补能密度 $\mathcal C_{mt}$ 的调节函数，$\chi(\bar{\mathcal C})=1$ 是尺度归一化，$\varkappa$ 为补能弹性。由 (M1.22)–(M1.23)：

$$
\frac{\partial u}{\partial R}=\eta_i\chi\,n^{long}_i\Pr(D^{long}>R)>0,\qquad
\frac{\partial^2u}{\partial R^2}=-\eta_i\chi\,n^{long}_i\,g^{long}(R)\le0, \tag{M1.24}
$$

$$
\frac{\partial^2u}{\partial R\,\partial\mathcal C}=\eta_i\,\chi'(\mathcal C)\,n^{long}_i\Pr(D^{long}>R)\le0\quad(\varkappa>0\ \text{时严格小于 0}). \tag{M1.24a}
$$

即续航边际效用为正且递减，**续航与补能网络互为替代**——与 Barwick 等（2026）上海车联网动态模型的发现一致 [O·卡]。PHEV 有发动机兜底，不设 $A$ 项，其纯电续航经 $UF$ 进入能源成本 (M1.13)。缺乏出行距离分布时可用 $\eta_i\ln B^R$（BKL 2024 的 $\log(\text{range})$ 写法 [O·卡]）作简约替代，二者只能选一。

**续航信念**：$B^R=\zeta^R_{d,c}L^R$，按动力分开（PHEV 新工况为 WLTC、BEV 为 CLTC）。在 $A(\cdot)$ 非线性、$F^{long}$ 以公里已知时，$\zeta^R_{d,N}$ 的水平原则上进入曲率；本文设 $\zeta^R_{\mathrm B,N}=1$（NEDC 续航按表面值），**这是识别假设而非无害归一化**，须报告 $\zeta^R_{\mathrm B,N}\in\lbrace0.7,0.8,1\rbrace$ 的敏感性，并只估计新工况的相对比 $\zeta^R_{\mathrm B,X}/\zeta^R_{\mathrm B,N}$。

---

# M1.6 口碑评分：整体评分与分项评分如何进入效用

## M1.6.1 经验品质量的贝叶斯信号模型 [D]

空间、动力、操控、舒适、外观、内饰、性价比等是**经验品属性**。设车型 $j$ 的经验质量 $q_{jk}\sim N(\bar q_k,\sigma^2_{qk})$，第 $n$ 位车主的分项评分 $r_{njk}=q_{jk}+e_{njk}$，$e_{njk}\sim N(0,\sigma^2_{ek})$ 独立。截至 $t-1$ 有 $n_{j,t-1}$ 条评论、样本均值 $\bar r_{jk,t-1}$。正态共轭后验均值：

$$
\widetilde Q^{k}_{j,t-1}\equiv E[q_{jk}\mid r]=\bar q_k+\underbrace{\frac{n_{j,t-1}\sigma^2_{qk}}{n_{j,t-1}\sigma^2_{qk}+\sigma^2_{ek}}}_{\text{收缩权重}\in(0,1)}\big(\bar r_{jk,t-1}-\bar q_k\big). \tag{M1.25}
$$

风险中性下质量进入效用为 $\sum_k\theta_k\widetilde Q^k_{j,t-1}$。**口碑应以收缩后验均值构造**，而非原始均分或“评分×条数”。先验参数 $(\bar q_k,\sigma^2_{qk},\sigma^2_{ek})$ 用经验贝叶斯估计，属生成变量。

**与可观测特征的重叠**：空间评分与尺寸、动力评分与功率相关；$\theta_k$ 度量的是**给定 $x$ 后的剩余经验质量**。可加入分项与人口特征的交互（如家庭规模 × 空间评分）以利用其异质估值。

## M1.6.2 整体评分 vs 分项评分 [D]

若平台整体分是分项加权和 $r^{all}_{nj}=\sum_k\omega_kr_{njk}+e^{all}_{nj}$，则**精确限制**为

$$
\sum_k\theta_k\widetilde Q^{k}=\theta\sum_k\omega_k\widetilde Q^{k}\quad\Longleftrightarrow\quad \theta_k=\theta\,\omega_k\ \ \forall k. \tag{M1.26}
$$

**近似条件**：只有各分项的信噪比（收缩权重）相同时，$\sum_k\omega_k\widetilde Q^k$ 才近似等于由整体分直接收缩得到的 $\widetilde Q^{all}$（数值例见附录 M1.16 例 B：两分项收缩权重 0.952 与 0.167 时，$\sum_k\omega_k\widetilde Q^k=0.168$，而由整体分收缩得到 $0.085$）。结论：（i）分项可得时用分项；（ii）只用整体分等价于施加 $\theta_k\propto\omega_k$ 并忽略信噪比差异，可用 Wald 检验；（iii）整体分与全部分项同时放入会近乎共线；（iv）平台整体分未必是分项的加权和，需核对平台规则；（v）品牌层口碑由品牌×年固定效应或品牌后验吸收。

## M1.6.3 能耗分项与车主实测油耗不进口味项 [D]

能耗分项与车主报告的实际油耗、实际续航是**关于 $T$ 的信号**，属于信念形成（M2 第二信源）。若放进 $\theta$，同一能源成本会经 $\gamma KB$ 与 $\theta_{energy}$ 计价两次。M1 中排除在 $\theta$ 之外（稳健性中可加入并解释为非货币的能耗满意度）。

## M1.6.4 动态内生性 [D]

评论累积依赖过去销量，而过去销量依赖持续的 $\xi$。若 $\xi$ 服从 AR(1)：$\xi_{jmt}=\rho_\xi\xi_{jm,t-1}+\nu_{jmt}$，则以准差分残差 $\nu_{jmt}=\xi_{jmt}-\rho_\xi\xi_{jm,t-1}$ 构造矩，并以 $\widetilde Q_{j,t-2}$ 及更深滞后作工具；同时控制车型上市月龄（生命周期效应与评论累积共线）。领先项检验：$\widetilde Q_{j,t+1}$ 不应预测 $t$ 期的 $\nu$。

---

# M1.7 完整效用、$\delta/\mu$ 分解与市场份额

## M1.7.1 标签隐含能源成本的统一写法 [D]

$$
G^{L}_{ijmt}=
\begin{cases}
K^{F}_{imt}L^{F}_{jt}, & d(j)\in\lbrace\mathrm I,\mathrm H\rbrace,\\[3pt]
K^{E}_{imt}L^{E}_{jt}, & d(j)=\mathrm B,\\[3pt]
K^{F}_{imt}\big[UF_i\,L^{F,CD}_{jt}+(1-UF_i)L^{F,CS}_{jt}\big]+K^{E}_{imt}UF_i\,L^{E,CD}_{jt}, & d(j)=\mathrm P,
\end{cases} \tag{M1.27}
$$

PHEV 的 $UF_i=UF_i(\zeta^R_{\mathrm P,c}L^{R,CD}_{jt})$ 由 (M1.12) 计算。

## M1.7.2 M1 的完整效用（基准规格）[P]

$$
\boxed{
\begin{aligned}
u_{ijmt}={}&\psi_{i,d(j)}+x_{jmt}'\beta_i+\sum_{k}\theta_k\widetilde Q^{k}_{j,t-1}
-\alpha_i\Big[p_{jmt}+\varphi_{d(j),c(j,t)}\,G^{L}_{ijmt}\Big]\\
&-\eta_i\,\chi(\mathcal C_{mt})\,A_i\big(\zeta^{R}_{\mathrm B,c}L^{R}_{jt}\big)\mathbf 1\lbrace d(j)=\mathrm B\rbrace+\xi_{jmt}+\varepsilon_{ijmt},\\
u_{i0mt}={}&-\alpha_i\,o_i\,\varphi^{0}\,K^{F,0}_{imt}\bar e_{0,m}+\varepsilon_{i0mt}.
\end{aligned}}
\tag{M1.28}
$$

外部选项的系数 $\varphi^0=\gamma_{\mathrm I}$（旧车真实油耗已知，$\zeta=1$），基准中固定于外部值（§M1.2.4）。随机系数：$\psi_{i,d}=\bar\psi_d+\sigma_d\nu_{id}$ 为对动力类型的非货币偏好（驾驶体验、环保态度、路权与牌照便利等不经能源成本与续航进入的部分）；$\beta_i=\bar\beta+\Pi\mathbf d_i+\Sigma\nu_i$（尺寸、功率/车重等）；$\alpha_i$ 见 (M1.6)；$K_{imt}$、$UF_i$、$h_i$、$o_i$ 随类型抽样而异；$\eta_i=\bar\eta$（异质性来自 $n^{long}_i$）。**电池变量**：容量 $C_j$ 不直接进入效用，经续航（$L^R$ 与真实续航）起作用；能量密度经“质量 → 电耗 → 续航”与补贴系数起作用（BKL 2024：容量只经续航进入需求 [O·卡]；工程链与补贴推导见 M4 §M4.5–M4.6）。

## M1.7.3 平均效用与个体偏离 [O]+[D]

按 BLP 式 (6.1) [O]：

$$
\begin{aligned}
\delta_{jmt}&=x_{jmt}'\bar\beta+\sum_k\theta_k\widetilde Q^{k}_{j,t-1}+\xi_{jmt}\quad(\bar\psi_d\ \text{被动力}\times\text{市场}\times\text{月固定效应吸收}),\\
\mu_{ijmt}&=\sigma_{d(j)}\nu_{id(j)}+x_{jmt}'(\Pi\mathbf d_i+\Sigma\nu_i)
-\alpha_i\big[p_{jmt}+\varphi_{d,c}G^{L}_{ijmt}\big]-\eta_i\chi(\mathcal C_{mt})A_i(\cdot)\mathbf 1\lbrace\mathrm B\rbrace .
\end{aligned} \tag{M1.29}
$$

价格与能源成本项整体放在 $\mu$（$\alpha_i$ 对数正态，无“均值 + 偏离”的可加分解；BKL 2024 同此写法 [O·卡]；BLP 原文价格通过 $\alpha\log(y-p)$ 进入非线性部分，故 $\xi_j=\delta_j-x_j\beta$ [O]）。$\theta_1=(\bar\beta,\theta,\text{固定效应})$；$\theta_2=(a_0,a_y,\sigma_p,\sigma_d,\Pi,\Sigma,\varphi_{d,c},\zeta^R_{\mathrm B,X},\bar\eta,\varkappa)$（$\varphi^0$ 基准固定）。**简约基准**：混动并入燃油车、跨动力共用 $\gamma$（只估 $\zeta$ 的比值）、$a_y$ 固定于外部值、$\varphi^0$ 固定；完整规格作扩展——聚合数据难以同时支撑全部非线性参数。

## M1.7.4 个体选择概率与市场份额 [O]

$$
P_{ijmt}=\frac{\exp(\delta_{jmt}+\mu_{ijmt})}{\exp(V_{i0mt})+\sum_{k\in\mathcal J_{mt}}\exp(\delta_{kmt}+\mu_{ikmt})},\qquad
s_{jmt}=\int P_{ijmt}\,dF_{mt}(i)\approx\frac1{NS}\sum_{i=1}^{NS}P_{ijmt}, \tag{M1.30}
$$

$V_{i0mt}$ 为 (M1.28) 中外部选项的确定部分（BLP 式 (6.6)(6.7)(6.10) 的推广 [O]）。类型 $i$ 的联合分布 $(y_i,VKT_i,h_i,f^{ch}_i,F^{day}_i,n^{long}_i,o_i,\nu_i)$ 须**联合**抽样（同一家庭调查的联合记录，或以 copula 连接边际分布），不能独立抽各边际（它决定替代模式）。所有抽样在估计与全部反事实中固定。**数据来源与降级方案**：收入—拥车联合分布可用家庭金融或追踪调查；里程、日行驶与长途分布可用全国出行调查或车联网数据；家充可用城市层私桩比例；只有边际分布时用独立 copula 并做相关性敏感性。

---

# M1.8 政策如何进入 BLP：标签跳变、楔子与反事实标签

## M1.8.1 标签状态方程 [P]

$$
L_{jt}=\big(1-S_{jt}\big)L^{N}_{jt}+S_{jt}L^{X}_{jt},\qquad S_{jt}=\mathbf 1\lbrace t\ge T^{show}_j\rbrace, \tag{M1.31}
$$

$T^{show}_j$ 为消费者实际看到新工况标签的首月（与法定资格日、认证日区分）。**混合展示月**（新旧标签并存）不能把平均标签代入效用（比例信念下 $\varphi_{d,c}$ 不再良定义）；基准做法是剔除过渡月（“甜甜圈”），稳健性中按消费者看到新标签的比例 $S_{jt}$ 对选择概率作混合 $S_{jt}P_{ij}(L^X)+(1-S_{jt})P_{ij}(L^N)$（逐车型近似）。

**两个标签时钟**：2024-07-01 实施的 GB 22757.1/.2—2023 改变了消费者标签格式（既有车型 2024-09-01 前换标），把展示状态扩展为 $(S^{cycle}_{jt},S^{format}_{jt})$——前者为工况切换，后者为标签格式改革；基准对 2024-07 至 2024-09 设甜甜圈，并对格式状态单独做稳健性。$T^{show}_j$ 的数据来源为工信部能耗标识备案系统的启用日与作废日。**插混的信息集**：按每一时期实际展示的字段构造信念——若某期只展示综合值，该期只能用综合值；字段结构本身的变化也是信息变化，此时 $\varphi_{\mathrm P,N}$ 与 $\varphi_{\mathrm P,X}$ 不再是同一映射下可比的参数。

## M1.8.2 用户的方法：用前 $n$ 期旧工况值外推切换年的旧工况标签 [P]+[D]

$$
\widehat L^{N}_{j,T_j}=\mathcal P\big(L^{N}_{j,T_j-1},\dots,L^{N}_{j,T_j-n};H_j\big),\qquad
W_j\equiv L^{X}_{j,T_j}-\widehat L^{N}_{j,T_j},\qquad
w_j\equiv\frac{W_j}{\widehat L^{N}_{j,T_j}}. \tag{M1.32}
$$

$H_j$ 为不随工况改变的硬件特征。最简单的 $\mathcal P$ 是“切换前最后一个 NEDC 值”（硬件不变时）；本地验证显示它与同配置双测值相关 0.8746、差值中位数 0、测量误差约占楔子方差 24.6%（可靠度 0.754），**验证只覆盖外推跨度 ≤1 年**[P，需复核原表]。楔子同时混有机械换算、工程适配、测试/披露楔子与测量误差四项（项目层四项分解 [P]），预定工具的作用是只保留由法定资格与改革前硬件决定的机械部分。

**楔子的三个用途**（不是另一个独立效用项）：（1）定义标签跳变；（2）构造无改革反事实 $L^{cf}_{jt}=\widehat L^{N}_{jt}$（M7 的 CF1）；（3）构造预定工具 $Z^{W}_{jt}=Elig^{law}_{jt}\times\bar K_{mt}\widehat W_j(H_{j,pre})$（§M1.10.3）。

## M1.8.3 切换时**本产品**效用的变化分解 [D]

同一消费者、同一硬件、同一价格、同一 $K$：

$$
\Delta u_{ij}=-\alpha_iK_{imt}\big[\varphi_{d,X}L^{X}_j-\varphi_{d,N}L^{N}_j\big]
=\underbrace{-\alpha_iK_{imt}\varphi_{d,X}W_j}_{\text{数值效应}}
\ \underbrace{-\ \alpha_iK_{imt}\big(\varphi_{d,X}-\varphi_{d,N}\big)L^{N}_j}_{\text{再估值效应}}. \tag{M1.33}
$$

（该分解依赖路径；另一写法为 $-\alpha_iK[\varphi_{d,N}W_j+(\varphi_{d,X}-\varphi_{d,N})L^X_j]$，报告两种或其平均。）两个基准下（用相对楔子 $W_j=w_jL^N_j$）：

$$
\Delta u_{ij}\big|_{naive}=-\alpha_iK_{imt}\varphi_{d,N}W_j,\qquad
\Delta u_{ij}\big|_{avg}=-\alpha_iK_{imt}\varphi_{d,N}L^{N}_j\,\frac{w_j-\bar w_d}{1+\bar w_d}. \tag{M1.34}
$$

## M1.8.4 份额怎样变化：必须看相对效用（对第 1 轮致命问题的修正）[D]

工况切换是同一动力内大量车型同时或交错重标的**市场层冲击**。由 $\partial P_{ij}/\partial u_{ij}=P_{ij}(1-P_{ij})$、$\partial P_{ij}/\partial u_{ik}=-P_{ij}P_{ik}$，份额的一阶变化为

$$
\boxed{\Delta s_{jmt}\approx\int P_{ij}\Big(\Delta u_{ij}-\sum_{k\in\mathcal J_{mt}}P_{ik}\,\Delta u_{ik}\Big)dF(i),\qquad \Delta u_{i0}=0,} \tag{M1.34a}
$$

$\Delta u_{ik}$ 包括所有同期重标的竞品（未重标产品与外部选项记 0），以及企业再定价带来的 $-\alpha_i\vartheta_k\Delta p^s_k$（§M1.12）。因此：

1. **份额上升的条件**是本产品效用变化高于“以选择概率加权（外部选项与未重标产品记 0）”的平均效用变化，**不是**本产品效用上升，更不是 $\varphi_{d,X}L^X_j<\varphi_{d,N}L^N_j$。
2. **天真基准下（零再估值）**，$\Delta u_{ij}=-\alpha_i\varphi K_iW_j$，$\Delta s_j\propto-\int\alpha_iK_iP_{ij}\big(W_j-\sum_kP_{ik}W_k\big)dF$：**楔子低于概率加权平均楔子的车型份额上升**。这是“没有任何再估值”的预测，不能被解读为“消费者相信新标签更真实”。（此简化式只在同一动力、共同 $\varphi$ 与 $K$ 时成立；跨动力须写 $\sum_kP_{ik}\Delta u_{ik}$。一阶式用于解释，定量预测须精确重解份额——插混楔子很大时一阶近似不可靠。）数值例（附录 M1.16 例 A：同质 logit，3 款 ICE + 1 款 BEV，天真信念，相对楔子 $(0.02,0.12,0.15,0)$）中，楔子最小的燃油车效用下降 $0.0252$，份额却从 $0.1950$ 升到 $0.2035$（外部份额 $0.22$）或从 $0.1050$ 升到 $0.1061$（外部份额 $0.58$）。
3. **再估值的证据**只能是：控制竞品同期重标与价格反馈之后，本产品的相对效用变化仍高于天真基准所预测的值——即在完整需求系统中估计 $\varphi_{d,X}\ne\varphi_{d,N}$，而不是看单个产品的份额符号。

**情景预测表**（**结构模型推出，非由共同成分直接识别**，依赖下述维持假设 A-FE；固定价格；燃油/混动楔子 $>0$、插混纯电续航下降；纯电续航楔子符号待核，两种符号分别给出；“组”为动力组份额）：

| 基准 | ICE/HEV 组 | 组内 | PHEV 组 | BEV 组 | 外部选项 |
|---|---|---|---|---|---|
| (a) 天真 | ↓ | 楔子低于加权平均者 ↑，高者 ↓ | ↓（降幅最大） | ↑（若 $w^R>0$）/ ↓（若 $w^R<0$） | ↑（内部平均效用下降） |
| (b) 已知平均换算 | ≈ | 偏离平均楔子者按偏离方向变化 | ≈ | ≈ | ≈ |
| (c) 表示不变 | 0 | 0 | 0 | 0 | 0 |
| (d) 再估值（燃油可信度上升、纯电下降） | ↑ | 视楔子分布 | ? | ↓ | ↓/? |

（“?”表示取决于参数；组层面方向由 M4 式 (M4.2) 计算。）

**维持假设 A-FE 与验证**：$\xi_{d,m,t}$ 吸收同动力同月的共同跳变，因此 $\varphi$ 只由同一动力内的相对变化（加交错时点）识别；表中组层面方向是把这样估出的 $\varphi$ 外推到共同成分上，维持假设 **A-FE**：$\xi_{d,m,t}$ 不含标签引起的成分，即共同成分与车型差异成分由同一 $\varphi_{d,c}$ 计价。验证：（i）用交错切换队列（2021-07 起新申请、2023-01 前既有车型）做组层面留出检验；（ii）把同一简约式算子 $R(\cdot)$ 作用于模型模拟数据，与 M0 事件研究系数比较：$\hat\beta^{model,cf}(\hat\theta)=R\big(q^{policy}(\hat\theta;\xi^{base})\big)-R\big(q^{no\,policy}(\hat\theta;\xi^{base})\big)$。纯电行还须计入中国工况下电耗标签 $L^E$ 的变化，不只是续航。

## M1.8.5 “单列一项”与“放进特征”：何时可识别 [D]

若在 (M1.28) 外再加政策项，分两种情形：

$$
\begin{aligned}
\text{(i)}\ \ &-\alpha_i\big(\varphi_dK_{imt}L_{jt}+b^{K}_dK_{imt}W_jS_{jt}\big):\ \ b^K_d\ \text{与}\ \varphi_{d,X}-\varphi_{d,N}\ \text{的分离依赖动力内楔子离散};\\
\text{(ii)}\ \ &-\alpha_i\varphi_dK_{imt}L_{jt}+b^{W}_dW_jS_{jt}:\ \ K\ \text{有变异时可识别}.
\end{aligned} \tag{M1.35}
$$

情形 (i)：切换后该项为 $-\alpha_iK[(\varphi_d+b^K)L^X-b^KL^N]$，与 M1 的 $-\alpha_iK\varphi_{d,X}L^X$ 在 $(KL^X,KL^N)$ 坐标中是不同的限制；$\operatorname{rank}[KL^X,\,KW]=2$ 当且仅当 $w_j$ 在动力内不是常数。实际楔子离散有限（同配置中位 7.7%、IQR 4.8%–11.4%），分离很弱，须报告缩放条件数，基准中不同时放开 $b^K_d$ 与 $\varphi_{d,X}-\varphi_{d,N}$。情形 (ii) 中不乘 $K$ 的 $b^W_d$ 度量**与能源成本无关的标签通道**（显著性、品牌信号、残值），它由 $K$ 的跨市场、跨时变异识别（$[K\cdot W,\,W]$ 在 $K$ 有变异时满秩），正是 §M1.14 预测 P3 的检验。不能再放“真实—标签差距”$T-L$ 作另一特征：真实值固定时 $\partial(T-L)=-\partial L$，是标签的镜像。

## M1.8.6 非信息的机械通道：必须进入价格或成本 [P]

- **新能源补贴**：BEV 为“续航档基础额 × 电池能量密度系数 × 电耗系数”；PHEV 为统一额（纯电续航门槛约 50 km）并有电耗相关要求（Ji 等 2026、BKL 2024 卡 [O·卡]）；2020 年起补贴前售价超过 30 万元的车型（换电车型除外）不享受补贴。若补贴按认证续航与电耗计算，切换会机械改变补贴额，进入消费者价 $p$（§M1.12）。
- **购置税与消费税**：燃油车购置税 10%（2022-06 至 2022-12 对 ≤2.0L 且 ≤30 万元减半），消费税按排量分档，新能源免征（有技术门槛）；资格变化进入 $\vartheta_j$ 与 $p$。
- **双积分**：WLTC 下燃油车实测油耗进入企业平均燃料消耗核算，改变有效边际成本（§M1.12、M6）。
- **2024 年标签格式改革**（GB 22757.1/.2—2023）是另一项同期信息变化（§M1.8.1）。

**2023 年 1 月同时是在产燃油车强制切换截止、购置税减半到期、中央补贴退出的月份**，2022 年 12 月还有提前购买；日历断点严重混杂，不能把该月的总体跳变归因于标签（M0 详述）。

---

# M1.9 边际效应、弹性与支付意愿（“单列”燃油经济性）

由 $\partial V_{ij}/\partial L_j=-\alpha_i\varphi_{d,c}K_{imt}$（ICE）：

$$
\frac{\partial s_{jmt}}{\partial L_{jt}}=-\int\alpha_i\varphi_{d,c}K_{imt}P_{ij}(1-P_{ij})\,dF<0,\qquad
\frac{\partial s_{kmt}}{\partial L_{jt}}=\int\alpha_i\varphi_{d,c}K_{imt}P_{ij}P_{ik}\,dF>0\ (k\neq j), \tag{M1.36}
$$

且 $\sum_{k\ne j}\partial s_k/\partial L_j+\partial s_0/\partial L_j=-\partial s_j/\partial L_j$（份额加总为 1；附录例 C 中转移率加总为 1.000000）。弹性与支付意愿：

$$
\epsilon^{L}_{jj}=\frac{L_{jt}}{s_{jmt}}\frac{\partial s_{jmt}}{\partial L_{jt}},\qquad
WTP_i(\Delta L=-1)=\frac{\partial V_{ij}/\partial L_j}{\partial V_{ij}/\partial p_j}=\frac{-\alpha_i\varphi K_{imt}}{-\alpha_i}=\varphi_{d,c}K_{imt}\ \text{（元）}. \tag{M1.37}
$$

**标签转移率**：

$$
DR^{L}_{j\to k}=\frac{\partial s_k/\partial L_j}{-\partial s_j/\partial L_j}
=\frac{\int\omega^{L}_{ij}P_{ij}P_{ik}\,dF}{\int\omega^{L}_{ij}P_{ij}(1-P_{ij})\,dF},\qquad \omega^{L}_{ij}=\alpha_i\varphi_{d,c}K_{imt},\qquad
\sum_{k\ne j}DR^{L}_{j\to k}+DR^{L}_{j\to0}=1. \tag{M1.38}
$$

与价格转移率（权重 $\alpha_i$）相比，标签转移率在**市场内**给高里程（$VKT_i$ 大）消费者更大权重；“高油价地区”权重更大是**跨市场**比较。外部选项含旧车能源成本时，高里程消费者更倾向置换，标签转移更偏向低能耗车型（附录 M1.16 例 C：外部份额都校准到 $0.5$ 时，含旧车油耗下 $\mathrm{corr}(K_i,P_{i0})=-0.10$，高里程者更倾向置换；省略旧车油耗时变为 $+0.33$，即高里程者反而更倾向“不买”，经济上说不通，并把标签转移率流向外部选项的部分从 $0.29$ 压到 $0.25$）——这再次说明 (M1.7) 不可省略。BEV 续航与 PHEV 纯电续航：

$$
\frac{\partial s_{jmt}}{\partial L^{R}_{jt}}=\int\eta_i\chi(\mathcal C_{mt})\,\zeta^R_{\mathrm B,c}\,n^{long}_i\Pr\big(D^{long}>\zeta^R_{\mathrm B,c}L^R_{jt}\big)\,P_{ij}(1-P_{ij})\,dF>0\quad(\mathrm{BEV}), \tag{M1.39}
$$

$$
\frac{\partial V_{ij}}{\partial L^{R,CD}_{j}}=-\alpha_i\varphi_{\mathrm P,c}\,\zeta^{R}_{\mathrm P,c}\Big[K^{F}_{imt}\big(L^{F,CD}_j-L^{F,CS}_j\big)+K^{E}_{imt}L^{E,CD}_j\Big]\frac{\partial UF_i}{\partial R}\quad(\mathrm{PHEV}). \tag{M1.39a}
$$

(M1.39a) 方括号在电驱比油驱便宜时为负，故纯电续航越长效用越高（项目层要求的 PHEV 链式项）。随机系数下这些边际效应都是对类型分布的积分，需模拟计算。

---

# M1.10 估计：反演、$\xi$ 结构、工具变量与 GMM

## M1.10.1 Berry 反演 [O]

给定 $\theta_2$，逐市场—月以 BLP 式 (6.8) 的收缩映射解 $s(\delta;\theta_2)=s^{obs}$ [O]：

$$
\delta^{h+1}_{mt}=\delta^{h}_{mt}+\ln s^{obs}_{mt}-\ln s_{mt}(\delta^{h}_{mt};\theta_2),\qquad \lVert\delta^{h+1}-\delta^{h}\rVert_\infty<10^{-12}. \tag{M1.40}
$$

外部选项确定部分 $V_{i0}\ne0$ 不影响收缩性质（它是给定 $\theta_2$ 时的已知项）。零销量：区分“未在售”（删去）与“在售零销量”（聚合到季度或用微观似然），不随意加小常数。

## M1.10.2 $\xi$ 的分解、固定效应与被吸收的对象 [P]

$$
\xi_{jmt}=\xi_{g(j)}+\xi_{b(j),y(t)}+\xi_{d(j),m,t}+\Delta\xi_{jmt}, \tag{M1.41}
$$

$\xi_g$ 车型谱系固定效应、$\xi_{b,y}$ 品牌×年、$\xi_{d,m,t}$ 动力×市场×月。**被吸收的对象**（只能靠交互项识别的参数）：

| 被吸收 | 由谁吸收 | 后果 |
|---|---|---|
| $\bar\psi_d$；动力共同政策（补贴退坡、限牌、充电网络主效应） | $\xi_{d,m,t}$ | 动力平均偏好不在 $\theta_1$ 中报告 |
| $K_{mt}$、$\mathcal C_{mt}$ 的主效应 | $\xi_{d,m,t}$ | $\varphi$ 只由 $K\times L_j$ 的产品间差异识别；$\varkappa$ 只由 $\chi(\mathcal C)\times A(R_j)$ 识别 |
| 同动力同月的标签共同跳变 | $\xi_{d,m,t}$ | 共同成分只能靠交错切换时点识别（M0） |
| 在 $(d,m,t)$ 层变化的工具（如同动力在售车型数） | $\xi_{d,m,t}$ | 残差方差为 0，必须改用产品层工具（下表） |
| 不随时间变化的车型质量、平均残值 | $\xi_g$ | 识别来自谱系内跨月变化 |

## M1.10.3 工具变量：逐条给出相关性、排除理由与威胁 [P]

| 内生对象 | 工具 | 相关性 | 排除限制与威胁 |
|---|---|---|---|
| 价格 $p$ | 钢价指数 $\pi^{steel}_t$ × 整备质量 $\mathrm{wt}_j$ | 车身材料成本随钢价变动，重车更敏感 | 重车（SUV）需求冲击若与钢价同步则失效；**整备质量缺失 60%–65%**（项目层），须补齐或改用尺寸代理 |
| 价格 $p$（BEV/PHEV） | 电池供应商 × 电池质量（BKL 2024 思路）；碳酸锂价格 $\pi^{Li}_t$ × 电池容量 $C_j$（谨慎） | 电池占电动车成本 30%–40% | 2021–2022 年锂价暴涨在很大程度上由中国新能源需求驱动，与容量相关的需求冲击可能相关；须论证或以供应商工具为主 |
| 价格 $p$（合资） | 汇率 × 外方国别 × 进口零部件比重 | 进口零部件成本随汇率变化 | 汇率与外方品牌形象冲击相关的威胁 |
| 价格 $p$ | BLP 竞争者特征和（同企业其他产品、其他企业产品，按动力×细分） | 近邻竞争越多，加价越低 | BLP 式 (5.8) 的经典论证 [O]；产品组合内生的威胁 |
| 价格与 $\sigma_d,\Sigma$ | **产品层**差异化工具：同细分、同价格带（±20%）内同动力竞品数（不含本企业）；特征空间距离小于一个标准差的竞品数（尺寸、功率、$\bar K_{mt}L_{jt}$、续航，按动力内计算；Gandhi–Houde 2019 的构造 [外]，本地经 Kaneko–Toyama 转引） | 局部竞争强度决定加价与替代 | 产品集合外生；用市场层 $\bar K_{mt}$ 而非个体 $K_{imt}$ |
| 标签项（切换后、展示时点内生时） | $Z^{W}_{jt}=Elig^{law}_{jt}\times\bar K_{mt}\widehat W_j(H_{j,pre})$ | 法定资格迫使切换，预测楔子决定跳变 | **可能是弱工具**（项目层：楔子对属性的 $R^2\approx0.30$），须报告 KP/SW；2023-01 截止与购置税减半到期重合、减半资格与排量相关，2022-12 提前购买进入 $\Delta\xi$——须剔除该窗口或单独建模 |

**标签项是“包含的外生变量”而非“排除的价格工具”**：标签直接进入效用，不能再拿它当价格工具（构造协议 §4.1 [P]）。

## M1.10.4 GMM、线性参数浓缩与 $\xi$ 的持续性 [O]+[D]

$$
g(\theta)=\frac1{N_{obs}}\sum_{jmt}Z_{jmt}\,\nu_{jmt}(\theta),\qquad
\widehat\theta=\arg\min_{\theta}\ g(\theta)'\,\mathbb W\,g(\theta), \tag{M1.42}
$$

基准 $\nu=\Delta\xi$；若 $\Delta\xi$ 持续（AR(1)），用准差分 $\nu_{jmt}=\Delta\xi_{jmt}-\rho_\xi\Delta\xi_{jm,t-1}$ 并把 $\rho_\xi$ 并入 $\theta_2$（§M1.6.4）。给定 $\theta_2$，$\delta=X_1\theta_1+\xi$ 对 $\theta_1$ 线性，浓缩：

$$
\widehat\theta_1(\theta_2)=\big(X_1'Z\mathbb WZ'X_1\big)^{-1}X_1'Z\mathbb WZ'\,\delta(\theta_2), \tag{M1.43}
$$

外层只对 $\theta_2$ 搜索（BLP 第 6.5 节 [O]）；AR(1) 准差分时，对准差分后的 $\delta$ 与 $X_1$ 应用 (M1.43)。两步 GMM，第二步用按谱系聚类的权重，并可用 Chamberlain 型近似最优工具提高随机系数精度（GRV 2018 采用 [O·卡]）。约束 $\varphi\ge0$、$\bar\eta\ge0$ 以 $\varphi=\exp(\tilde\varphi)$ 实现。**$a_y,\sigma_p$ 的识别**：成本移动项与市场收入分布的交互（如 $\pi^{steel}_t\times\mathrm{wt}_j\times\overline{\ln y}_{mt}$），以及若可得的汇总微观矩（各收入组在新车买家中的占比，Ji 等 2026 用 9 个此类矩 [O·卡]）；聚合数据下 $\sigma_p$ 常常弱识别——即使有车型—城市—月数据也如此（Li 2026 的 $\Sigma_\alpha=0.0010\ (0.8451)$ [O·卡]），可固定 $a_y$ 于外部值（$-1$ 或 BKL 的 $-1.21$）并做敏感性。

## M1.10.5 推断

按车型谱系聚类；标准误含模拟误差（BLP 式 (5.6) 的 $V_3$ [O]）；$K$、$\widehat L^N$、$\widetilde Q$、配置聚合标签均为生成变量，用“重抽谱系 → 重做外推、收缩与聚合 → 重估”的全流程自助法；有效政策冲击数有限，推断层级与冲击层级一致。

## M1.10.6 算法步骤

1. 固定抽样：每个 $(m,t)$ 抽 $NS=500\sim1000$ 个类型（Halton/Sobol），联合抽取 §M1.7.4 的类型向量，计算 $K^F,K^E,K^{F,0},UF_i,A_i(\cdot)$。
2. 给定 $\theta_2$ 算 $\mu_{ijmt}$ 与 $V_{i0mt}$。
3. 逐市场—月收缩映射得 $\delta$；浓缩 $\theta_1$；得 $\nu$，算 GMM 目标。
4. 外层优化（解析梯度、多初值），检查一阶与二阶条件。
5. 诊断（§M1.13）。$-\alpha_i\varphi K_iL_j$ 是“对数正态随机系数 × 外部抽样 × 产品特征”的三重乘积，标准 pyblp 公式不直接支持，建议自写内层，并用 pyblp 估计去掉该结构的嵌套简化版作交叉验证。

---

# M1.11 识别：参数—变异—矩登记表（含竞争解释、支持与秩）

**标签估值率的三组矩**（展示时点内生只污染利用跳变本身的前后对比；切换后同一产品内由油价时间变化带来的变异，只要油价波动与 $\nu$ 无关仍然有效，产品“何时进入新状态”的选择若只与 $\nu$ 的水平相关，会被产品×状态均值吸收）：

$$
\begin{aligned}
&E\Big[(K_{mt}-\bar K^{pre}_{jm})L^N_j\,\nu_{jmt}\,\mathbf 1\lbrace t<T_j\rbrace\Big]=0, &&\text{(M1.42a)}\\
&E\Big[(K_{mt}-\bar K^{post}_{jm})L^X_j\,\nu_{jmt}\,\mathbf 1\lbrace t\ge T_j\rbrace\Big]=0, &&\text{(M1.42b)}\\
&E\big[Z^W_{jt}\,\nu_{jmt}\big]=0. &&\text{(M1.42c)}
\end{aligned}
$$

(M1.42a) 识别 $\varphi_{d,N}$；(M1.42b)(M1.42c) 识别 $\varphi_{d,X}$，二者之间的过度识别检验就是“跳变是否外生”的检验。若担心 $L^X$ 本身因认证策略而内生，须单列并另给工具。

| 参数 | 识别变异 | 矩 | 主要竞争解释（rival） | 有效支持 | 局部秩检查 |
|---|---|---|---|---|---|
| $a_0,a_y,\sigma_p$ | 成本冲击引起的价格变化；成本 × 市场收入交互 | $E[Z^{cost}\nu]$、$E[Z^{cost}\overline{\ln y}\,\nu]$、汇总微观矩 | 成本冲击与需求冲击相关 | 各市场收入分布的跨市场/跨期差异 | $\partial g/\partial(a_y,\sigma_p)$ 缩放奇异值 |
| $\varphi_{d,N}$ | 改革前同一产品内油价时间变化 × 车型标签差异 | (M1.42a) | 油价经外部选项个体偏离、里程反弹、二手车价、收入影响需求 | 油价调整次数与幅度；车型标签离散 | 与 $a_y,\sigma_p$ 的联合秩 |
| $\varphi_{d,X}$ | 切换后同一产品内油价时间变化 × $L^X$；同硬件标签跳变（交错时点） | (M1.42b) 与 (M1.42c)；二者间的过度识别检验即“跳变是否外生”的检验 | 跳变与改款、补贴档位、税收资格捆绑；$L^X$ 因认证策略内生（须另给工具） | 严格同配置篮子；切换队列数 | KP/SW 弱工具统计 |
| $\varphi_{d,X}/\varphi_{d,N}$ | 同硬件跳变 × 楔子的跨产品差异（控制竞品重标与再定价） | 检验 (M1.19)–(M1.20a)；对 $K$ 的乘性误设不变，作主报告对象 | 竞品溢出、价格反馈（§M1.8.4） | 楔子跨车型离散 | — |
| $\varphi_{\mathrm B,N},\varphi_{\mathrm B,X}$ | 城市间与跨期的公共充电价格/服务费、分时电价调整、家充比例 × $L^E_j$；中国工况下 $L^E$ 的跳变（比值） | $E[(\bar K^E_{mt}L^E_{jt})\nu]$ | 城市口味（收入、拥堵、限牌）、补能密度、地方新能源政策 | 居民电价时间变异小 | 与 $\varkappa,\bar\eta$ 的联合秩 |
| $\varphi^{0}$（外部选项） | 仅类型间异质性（油价变化经 $\alpha_io_iK_i$ 的离散改变买家构成）；总份额对油价的反应被 $\xi_{d,m,t}$ 吸收 | 基准固定于外部值 | — | 组内变异很小 | 不在基准 $\theta_2$ 中 |
| $\sigma_d,\Sigma$ | 产品层差异化工具、新车型进入、竞品标签跳变 | 差异化工具矩 | 产品组合内生 | 车型进入/退出次数 | 缩放奇异值 |
| $\Pi$ | 跨城市人口分布差异（城市数据） | 人口 × 特征工具 | 城市层需求冲击 | 城市数与人口离散 | — |
| $\bar\eta,\varkappa,\zeta^R_{\mathrm B,X}$ | 同谱系不同电池版本的续航差（若车型层数据可拆）；补能密度跨城跨期变化 × 续航；CLTC 跳变 | 续航 × 补能交互矩 | BEV 自愿切换的选择性；同配置 BEV 证据很薄（6 款，约 45.7% 为同一数字写进两列 [P]） | 续航与补能的联合支持 | 曲率参数的 profile |
| $\theta_k$ | 谱系内口碑随评论累积的变化 | 准差分 $E[\widetilde Q_{t-2}\nu]$ | 营销活动同时影响评论与需求 | 评论数增长的车型间差异 | — |

**纯电与插混电力部分的退路**：(a) 施加 $\gamma_{\mathrm B}=\gamma_{\mathrm I}$（A-$\gamma$ 的跨动力版本，有支持时可检验），只估 $\zeta_{\mathrm B,X}/\zeta_{\mathrm B,N}$；(b) 或固定 $\varphi_{\mathrm B,N}$ 于外部值并报告敏感性。插混的 $\varphi_{\mathrm P,c}$ 同乘油、电两部分，其识别主要来自油价部分。

## M1.11.1 可检验的嵌套模型：按变异来源分开估值率（替代第 1 版的恒等式）[D]

在 M1 的比例信念下，“对油价的反应”与“对标签的反应”由同一个 $\varphi$ 决定——但这一点在 M1 **内部是恒等式**，不能当作检验。可检验的做法是写出按变异来源分开的嵌套模型：

$$
u_{ijmt}\supset-\alpha_i\Big[p_{jmt}+\varphi^{L}_{d,c}\,\bar K_{im}L_{jt}+\varphi^{K}_{d,c}\,\big(K_{imt}-\bar K_{im}\big)L_{jt}\Big],\qquad H_0:\ \varphi^{K}_{d,c}=\varphi^{L}_{d,c}, \tag{M1.44}
$$

$\bar K_{im}$ 用市场长期平均油价计算。车型（或谱系）固定效应下，$\bar K_{im}L_j$ 的时间不变部分被吸收，$\varphi^L$ 由**标签跳变**识别、$\varphi^K$ 由**油价变化**识别。若信念不是标签的比例函数（例如 M2 的双信源 $B=\kappa\zeta L+(1-\kappa)\widetilde O$），油价反应正比于整个信念 $B$，标签跳变反应正比于 $\kappa\zeta$；**当车主信源 $\widetilde O_j$ 与标签在固定效应残差上相关**（$\operatorname{Cov}(\tilde O_j,\tilde L_j)\ne0$）时，油价反应中的 $(1-\kappa)\widetilde O(K-\bar K)$ 部分载到 $\varphi^K$ 上，二者不等，$H_0$ 被拒绝；若二者无关，检验没有功效，**不拒绝 $H_0$ 不能作为比例信念成立的证据**。**但拒绝 $H_0$ 不自动支持双信源**：油价还经外部选项旧车成本（已在 (M1.7) 建模）、里程反弹（$K$ 对油价反应小于比例）、二手车价对油价的资本化、油价预期的均值回复等通道影响需求，这些都会使 $\varphi^K$ 偏离 $\varphi^L$。因此 (M1.44) 是“比例信念 + $K$ 构造正确”的联合检验；M2/M3 给出能区分这些解释的升级规格。

---

# M1.12 供给侧最小块（为 M6、M7 准备）

## M1.12.1 消费者价、企业净收与完整税补账户 [O·卡]+[D]

中国乘用车零售价含增值税（$t^v=13\%$）与消费税（按排量分档，新能源免征；以价外换算率记为 $t^{ct}_j$）；购置税以不含增值税价计征（燃油车 $t^p_j=10\%$ 或减半期 5%，新能源免征）。以企业净收 $p^s_j$（不含增值税与消费税）为企业选择变量，零售价 $P^{ret}_j=p^s_j(1+t^{ct}_j)(1+t^v)$，购置税 $t^p_jP^{ret}_j/(1+t^v)$，消费者价为

$$
\begin{aligned}
p_{jmt}&=p^{s}_{jt}\,(1+t^{ct}_j)\,(1+t^{v}+t^{p}_{jt})-sub_{jt}\cdot\mathbf 1\lbrace P^{ret}_{jt}\le\bar P^{sub}\rbrace-sub^{loc}_{jmt}+\mathcal F_{jmt},\\
\vartheta_{jt}&\equiv\frac{\partial p_{jmt}}{\partial p^s_{jt}}=(1+t^{ct}_j)(1+t^{v}+t^{p}_{jt})
\end{aligned} \tag{M1.45}
$$

（与 Ji 等 2026 的企业净价 $pr/[(1+t_v)(1+t_c)]$ 与 $\partial p/\partial pr=(1+t_v+t_t)/(1+t_v)$ 一致 [O·卡]；若消费税以价内税率 $t^{CT}$ 表示，则 $1+t^{ct}=1/(1-t^{CT})$。）$\mathcal F$ 为车船税、牌照费、保险等其他支出，$\bar P^{sub}=30$ 万元为补贴价格上限：$p(p^s)$ 在上限处不连续，FOC 须辅以离散偏离检查（企业可能聚集在上限以下）。经销商环节以“$p^s$ 含经销商毛利”的纵向结构假设处理，并做敏感性。

## M1.12.2 一阶条件与 $\Delta$ 矩阵方向 [O]+[D]

企业 $f$ 全国统一定价时 $\Pi_f=\sum_mM_{mt}\sum_{j\in\mathcal J_f}(p^s_{jt}-mc^{eff}_{jt})s_{jmt}(p)-F_f$。由链式法则 $\partial s_{km}/\partial p^s_j=\vartheta_{j}\,\partial s_{km}/\partial p_j$：

$$
\sum_{m}M_{mt}\Big[s_{jmt}+\sum_{k\in\mathcal J_f}\big(p^{s}_{kt}-mc^{eff}_{kt}\big)\vartheta_{jt}\frac{\partial s_{kmt}}{\partial p_{jt}}\Big]=0. \tag{M1.46}
$$

按 BLP 式 (3.4) 方向（第 $j$ 行是 $j$ 的价格 FOC，第 $k$ 列是 $k$ 的利润边际）：

$$
\Delta_{jk}=-O_{jk}\sum_mM_{mt}\,\vartheta_{jt}\,\frac{\partial s_{kmt}}{\partial p_{jt}},\qquad
\tilde s_j=\sum_mM_{mt}s_{jmt},\qquad
\boxed{p^{s}-mc^{eff}=\Delta^{-1}\tilde s}. \tag{M1.47}
$$

**方向不可互换**：即使对消费者价的需求雅可比 $\partial s/\partial p$ 在准线性下对称，只要同一企业内各产品的 $\vartheta_j$ 不同（燃油车含购置税与消费税、新能源免征），对企业净价的雅可比 $\vartheta_j\partial s_k/\partial p_j$ 就不对称，必须按 (3.4) 方向构造（附录 M1.16 例 D：4 产品 2 企业、燃油车含税而新能源免税，真实 $mc=[6,7,6.5,7.5]$；按 (3.4) 方向精确还原，转置方向最大误差 0.011）。$O_{jk}=\mathbf 1\lbrace f(j)=f(k)\rbrace$ 为基准；合资企业的利润分成以 $O_{jk}\in[0,1]$ 作 conduct 敏感性（“合资”标签本身不等于内部化权重）。需求导数按 BLP (6.9a)(6.9b)（已补回 (6.9b) 前置负号）[O]：本规格下 $\partial s_k/\partial p_j=\int\alpha_iP_{ij}P_{ik}dF>0$（$k\ne j$）。

## M1.12.3 有效边际成本 [P]

$mc^{eff}_{jt}=mc_{jt}-\lambda^{C}_f\,a^{C}_{jt}-\lambda^{N}_f\,a^{N}_{jt}$（$a$ 为每辆车对 CAFC/NEV 积分的边际贡献，$\lambda$ 为影子价格；推导见 M6 (M6.3)）。反推出的是 $mc^{eff}$ 而非纯制造成本；WLTC 同时改变燃油车实测油耗（标签侧）与第五阶段目标值（目标侧），$a^C$ 的变化取决于两侧，须按标准文本核算。反推出的 $mc^{eff}$ 在新能源积分价格高时可能为负，不能取对数：M1 的成本方程写为水平形式 $mc^{eff}_{jt}=w_{jt}'\gamma^{mc}+\omega_{jt}$，供给矩 $E[Z^S\omega]=0$（BLP 式 (3.1)(3.6) 的对数形式在此不适用 [O]），或把影子价格 $\lambda$ 作为待估参数（M6）。**M1 的基准估计只用需求矩**，供给矩作为扩展。

---

# M1.13 退化、嵌套与诊断

**精确退化**：

1. 令 $\sigma_d=0$、$\Pi=\Sigma=0$、$\sigma_p=0$、$a_y=0$，并令类型分布退化为预定代表类型 $z^\ast$（该类型保留自身的日行驶与长途距离分布，非线性输入 $UF$、$A$ 在 $z^\ast$ 处计算，而不是先对非线性输入取均值；M0 另需固定 $\zeta^R$ 与 $\chi$）⇒ 同质 logit，$\ln s_j-\ln s_0=V_j-V_0$ 有闭式反演，即 M0 的基础回归。
2. $\varphi_{d,X}=\varphi_{d,N}$ ⇒ 天真模型；$\varphi_{d,X}(1+\bar w_d)=\varphi_{d,N}$ ⇒ 已知平均换算模型。
3. M2 的双信源信念中令车主信源权重为 0 ⇒ 回到 M1 的比例信念。

**诊断清单**：（a）价格第一阶段与 Sanderson–Windmeijer F；（b）按单位缩放后的矩雅可比奇异值（$\varphi_{d,N},\varphi_{d,X},\varphi_{\mathrm B,c}$ 的联合秩）；（c）自价格弹性与加价率的合理性——以 Ji 等（2026）中国估计为参照（低收入组 $-3.85$、高收入组 $-2.46$、总体 $-2.88$ [O·卡]）；反推 $mc^{eff}$ 的合理性（新能源可能为负，须与积分价格对照）；（d）收缩映射收敛与积分节点加倍稳定性；（e）多初值；（f）嵌套检验 (M1.44)；（g）**样本内份额拟合由反演机械保证，不是验证**，需留出月份/城市预测与改革事件梯度的外部验证。

---

# M1.14 M1 的可检验预测与边界

- **P1（相对效应）**：同硬件、固定价格下，切换后车型 $j$ 的份额变化由 (M1.34a) 给出；天真基准下，楔子高于概率加权平均楔子的车型份额下降、低于者上升。检验对象是整个系统中的 $\varphi_{d,X}$ 与 $\varphi_{d,N}$，不是单个车型份额的符号。
- **P2（再估值）**：$\varphi_{d,X}/\varphi_{d,N}$ 与 $1$（天真）、$1/(1+\bar w_d)$（已知平均换算，比例信念类中的理性预期基准）比较；三者都以 A-$\gamma$ 为维持假设。比值对 $K$ 的乘性误设（$r$、$\bar A$、里程尺度）不变，而 $\varphi$ 的水平一比一受其影响，因此比值是主报告对象。
- **P3（成本通道）**：(M1.35)(ii) 中不乘 $K$ 的标签项 $b^W_d$ 显著，说明存在与能源成本无关的标签通道（显著性、品牌信号、残值）。
- **P4（替代去向）**：被标签冲击的车型份额主要流向特征相近、能耗更低的产品与外部选项，权重偏向高里程消费者 (M1.38)。组层面方向依赖维持假设 A-FE（§M1.8.4）。

**能回答**：标签变化在多大程度上被计价（$\varphi$，以 $K$ 尺度为条件）、新旧标签每单位估值是否变化、标签冲击下的替代去向、固定价格与重新定价下的份额变化。**不能单独回答**：消费者是否短视（$\gamma$）、标签信息权重多大——它们在 M1 中只以乘积出现，由 M2、M3 在约束下拆分。$\varphi^0$ 若自由估计，会在 M1 内分离 $\gamma_{\mathrm I}$ 与 $\zeta_{\mathrm I,c}$；这条途径只靠函数形式与类型分布，本稿不依赖它，因此仍把 $\gamma$ 视为 M1 不可识别。

---

# M1.15 来源说明与文献对接

[O] BLP（1995）式 (2.1)(2.2)(2.5)(2.7)(3.1)–(3.6)(4.1)(5.8)(6.1)–(6.10)，含 (6.9b) 前置负号与两处印刷笔误更正（项目核验底座）。
[O·卡] GRV（2018）式 (1)–(5)（式 (7) 仅文字层）：$\alpha_i(p+\gamma G)$、里程经验分布、$\gamma\rho$ 与里程尺度不可分；**Gillingham–Houde–van Benthem（2021）是同硬件重标的直接母本**（价格回归、估值 0.16–0.39、均值之比近似会高估、$\Delta WTP=\Delta P-P_0(\Delta Q/Q)/\eta_D$ 的条件换算），本稿 (M1.33)–(M1.35) 是其在 BLP 中的结构化推广，并补上竞品与价格反馈 (M1.34a)；**Reynaert–Sallee（2021）**的信念 $\tilde x=x-(1-\alpha)g$ 是“真值—标签凸组合”：$\zeta=1$ 时本稿比例信念与 RS 的 $\alpha=0$ 重合，一般 $\zeta$ 是对标签的比例校正、不在 RS 族内，两族由 M2 的双信源后验共同嵌套（M2 (M2.10)）；Barwick 等（2026）续航与充电替代；BKL（2024）对数正态价格系数（$\alpha_2=-1.21$）、容量只经续航进入、补贴门槛；Ji 等（2026）市场规模（一半家庭）、税楔子、补贴系数结构、外部选项“继续开旧车”、弹性参照；Li（2026）车型—城市—月数据下价格随机系数仍弱识别。
[O·卡：项目制度记忆] 标准与通知时点（§M1.1.2）。
[外] Anderson–Kellogg–Sallee（2013，经 GRV 卡转引）；Gandhi–Houde（2019，差异化工具，经 Kaneko–Toyama 转引）。
[D] (M1.2)–(M1.7b)、(M1.9)–(M1.13)、(M1.17)–(M1.24a)、(M1.25)–(M1.26)、(M1.33)–(M1.39a)、(M1.44)–(M1.47) 为本文推导。
[P] 比例信念 (M1.16)、续航缺口规格 (M1.23)、$\xi$ 结构 (M1.41)、工具组合、市场规模、配置聚合与有效边际成本为本项目设定，需数据检验。

---

# M1.16 附录：数值例参数与复现 [I]

三个数值例只用于说明符号与机制，不是估计结果；复现脚本 `tools/m1_examples.py`（numpy，固定随机种子）。

**例 A（相对效用，(M1.34a)）**：同质 logit，4 个内部产品 $\delta_j=0$，外部选项 $\delta_0$ 校准到 $s_0\in\lbrace 0.22,0.58\rbrace$；天真信念下 $\Delta u_j=-c\,w_j$，$c\equiv\alpha\varphi KL^N=1.26$，$w=(0.02,0.12,0.15,0)$（第 4 个为 BEV，不受燃油楔子影响）。结果：

| $s_0$ | $\Delta u_{1}$ | $\sum_kP_k\Delta u_k$ | ICE1 份额（精确） | 一阶近似 $\Delta s_1$ | BEV 份额 | 外部份额 |
|---|---|---|---|---|---|---|
| 0.22 | $-0.0252$ | $-0.0713$ | $0.1950\to0.2035$ | $+0.0090$（精确 $+0.0085$） | $0.1950\to0.2087$ | $0.2200\to0.2355$ |
| 0.58 | $-0.0252$ | $-0.0384$ | $0.1050\to0.1061$ | $+0.0014$（精确 $+0.0012$） | $0.1050\to0.1089$ | $0.5800\to0.6013$ |

**例 B（整体分 vs 分项，(M1.26)）**：两分项 $\omega=(0.5,0.5)$，先验方差 $\sigma^2_{qk}=0.04$，单条评论噪声方差 $\sigma^2_{ek}=(0.04,\,4.0)$，$n=20$，两分项样本均值偏离先验均值都为 $0.30$。分项收缩权重 $(0.952,\,0.167)$，$\sum_k\omega_k\widetilde Q^k=0.168$；把整体分 $r^{all}=\sum_k\omega_kr_k$ 当作单一信号收缩（先验方差 $\sum\omega_k^2\sigma^2_{qk}$、噪声方差 $\sum\omega_k^2\sigma^2_{ek}/n$），收缩权重 $0.284$，后验 $0.085$。信噪比不同的分项被整体分“平均掉”，这就是只用整体分的代价。

**例 C（标签转移率与外部选项能源成本，(M1.38)）**：$4\times10^5$ 个模拟消费者，$\ln VKT_i\sim N(\ln 12000,\,0.5^2)$，$\ln\alpha_i\sim N(\ln 0.10,\,0.3^2)$（每千元效用）；3 款 ICE，$L=(5.0,6.5,8.0)$ L/100km，$p=(140,120,100)$ 千元；$\pi^F=7.5$ 元/L，年金因子 $6$，$\varphi=0.8$，旧车油耗 $e_0=8.5$。两种外部选项设定下都用共同常数把平均外部份额校准到 $0.5$，扰动中间车型的标签。

| 外部选项 | $\mathrm{corr}(K_i,P_{i0})$ | 标签转移→最省油车 | 价格转移→最省油车 | 标签转移→外部 | 价格转移→外部 |
|---|---|---|---|---|---|
| 含旧车油耗 (M1.7) | $-0.098$ | $0.151$ | $0.110$ | $0.295$ | $0.296$ |
| $u_0=\varepsilon$（省略） | $+0.328$ | $0.107$ | $0.089$ | $0.251$ | $0.218$ |

两种设定下标签转移都比价格转移更偏向最省油车（高里程者权重大），但省略旧车油耗会让高里程者系统性地“更不买车”（相关系数变号），并改变流向外部选项的转移——外部选项设定直接影响替代格局与福利。

**例 D（供给侧 $\Delta$ 的方向，(M1.47)）**：同质 logit，$\alpha=0.5$，$\delta=(2.0,1.5,1.8,1.2)$；企业 1 拥有产品 1（燃油车）与 2（新能源），企业 2 拥有产品 3（燃油车）与 4（新能源）；税因子 $\vartheta=(1.13\times1.10\times1.05,\ 1.13,\ 1.13\times1.10\times1.03,\ 1.13)$（燃油车含购置税与消费税，新能源只含增值税）；真实 $mc=(6,7,6.5,7.5)$。由一阶条件解出均衡企业净价 $(7.655,8.893,8.138,9.346)$ 后：按 BLP (3.4) 方向构造 $\Delta_{jk}=-O_{jk}\vartheta_j\partial s_k/\partial p_j$，还原 $mc$ 的最大误差 $9\times10^{-16}$；按转置方向还原为 $(6.0067,6.9887,6.5033,7.4936)$，最大误差 0.011。税因子相同时两方向一致。

（第 2 版 §M1.2.4 曾引用的相关系数 $+0.056$ 来自第 1 轮审稿人自己的参数设定，第 3 版统一改用本附录例 C 的 $+0.33$。）

