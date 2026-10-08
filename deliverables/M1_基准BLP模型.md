---
title: "M1 基准 BLP 模型：工况重标如何进入随机系数需求系统"
subtitle: "从消费者效用最大化到可估计 GMM 系统的逐式推导（市场—年月—车型数据）"
date: "2026-10-08（第 1 版，待第三方审议）"
lang: zh-CN
---

# M1.0 本模型回答什么，以及与其他模型的关系

**一句话**：M1 是全课题的“共同需求核”。它从消费者在跨期预算约束下的效用最大化出发，推导出“车价 + 未来能源成本现值”构成的**广义价格**，把官方能耗/续航**标签**作为消费者形成能源成本与续航判断的信息输入放进广义价格与续航便利项，再按 BLP（1995）的随机系数 logit、Berry 反演、IV/GMM 与多产品 Bertrand 定价组成可估计系统。工况切换（NEDC→WLTC/CLTC）在 M1 中**不是一个政策虚拟变量**，而是对标签状态 $L_{jt}$ 的一次有日期的跳变；它对需求的作用必须经过“标签 → 主观能源成本/续航 → 效用 → 份额”这条结构链。

M1 直接回答用户的五个具体问题：

| 用户问题 | M1 的回答（详见所在小节） |
|---|---|
| 政策如何加入 BLP？放在效用的哪一部分？ | 进入广义价格中的“标签隐含能源成本” $\varphi_{d,s}K_{imt}L_{jt}$ 与 BEV 的续航便利项；不是自由系数的政策虚拟变量（§M1.4、§M1.8） |
| 用先前 $n$ 期油耗外推切换年的旧工况值再作差，以什么形式进入？ | 楔子 $W_j=L^{X}_{j}-\widehat L^{N}_{j}$ 定义标签跳变幅度、无改革反事实标签路径与预定工具变量；实际进入效用的是当期展示的标签 $L_{jt}$（§M1.8.2） |
| 燃油经济性/续航能否“单列一项”算边际效应？ | 可以且应当：它就是广义价格的能源成本项，系数与价格系数绑定，边际效应、弹性、支付意愿均有闭式（§M1.9） |
| 口碑整体评分与分项评分如何构造？ | 分项是经验品质量的贝叶斯信号，按收缩后验均值进入；整体分只是分项加权和的受限特例，可检验；能耗分项与车主实测油耗进入信念（M2），不进口味项（§M1.6） |
| 新能源车的续航如何进入？ | 由出行距离分布推出“续航缺口”函数 $A_i(R)$，凸递减，与补能密度互为替代（§M1.5）；电池容量与能量密度经工程链进入（M4） |

**与后续模型的嵌套关系**：M1 用“比例信念”$B=\zeta_{d,s}L$ 得到可识别的复合参数——标签成本估值率 $\varphi_{d,s}=\gamma_d\zeta_{d,s}$。M2（机制一：认证可信度）把信念推广为“标签 + 车主口碑”双信源贝叶斯后验；M3（机制二：短视/资本化）把 $\varphi$ 分解为资本化率 $\gamma_d$ 与信念映射；M4 处理跨动力替代与电池；M5 异质性；M6 供给与创新；M7 反事实与福利。每个升级都给出“回到 M1 的精确参数限制”。

**标注约定**：[O] 文献原式（已对原页或已核卡片）；[D] 本文从所述假设推导；[P] 本项目设定（需识别或校准）；[I] 仅示例。记号沿用用户核验过的 BLP 演练稿：$\delta$ 平均效用、$\mu$ 个体偏离、$\xi$ 未观测质量、$\Delta$ 定价矩阵、$\Delta^{-1}s$ 加价。

---

# M1.1 数据结构、市场与时序

## M1.1.1 观测单位与份额

观测单位为（产品 $j$，市场 $m$，月份 $t$）。$j$ 是“车型—动力版本/配置”（标签按配置认证）；$m$ 是城市或省份（若只有全国数据则 $m$ 只有一个）；$d(j)\in\lbrace \mathrm{I},\mathrm{H},\mathrm{P},\mathrm{B}\rbrace$ 依次为燃油车（ICE）、油电混动（HEV）、插电混动（PHEV）、纯电（BEV）。$j=0$ 为外部选项（本月不购买新车，含继续使用旧车或不拥车）。

$$
s^{obs}_{jmt}=\frac{q_{jmt}}{M_{mt}},\qquad s^{obs}_{0mt}=1-\sum_{j\in\mathcal J_{mt}}s^{obs}_{jmt}>0. \tag{M1.1}
$$

$q_{jmt}$ 为终端销量（上险量优先；出厂量不是需求），$\mathcal J_{mt}$ 为该市场该月**实际在售**的产品集合，$M_{mt}$ 为潜在购买机会数。[P] 建议 $M_{mt}=H_{mt}\times\bar h$：$H_{mt}$ 为家庭户数，$\bar h$ 为月度购车机会率（例如年换购/首购率 7% 折月），并对 $\bar h$ 做敏感性。$M$ 决定外部份额，进而决定总需求弹性与福利零点；不能用当月总销量当 $M$（否则 $s_0\equiv0$，见 micro_foundations §2(d)）。

## M1.1.2 时序（决定哪些变量是“先决”的）

1. 政府公布工况标准与法定时点（ICE/PHEV 新车型 2021-07-01 起、在产车型 2023-01-01 前须满足 GB 19578—2021；BEV 按 GB/T 18386.1—2021 可自愿切换）。
2. 企业观察需求冲击 $\xi$ 与成本冲击 $\omega$，在法定约束内选择认证与展示新标签的时点、价格（M6 讨论属性与创新）。
3. 消费者在 $t$ 月观察价格 $p_{jmt}$、可观测特征 $x_{jmt}$、当期**展示**的标签 $L_{jt}$、截至 $t-1$ 的口碑 $Q_{j,t-1}$，作出购买选择。
4. 购车后真实能耗 $T$ 实现，车主发布口碑，成为以后消费者的信息。

时序 3–4 意味着：$Q_{j,t-1}$ 相对 $t$ 月选择是先决的；$L_{jt}$ 在硬件不变时由工况规则决定，但展示时点由企业选择——这是识别中最需防范的内生性（§M1.10.3）。

---

# M1.2 消费者问题：从效用最大化到条件间接效用

## M1.2.1 跨期预算约束与 Fisher 分离 [D]

消费者 $i$ 在 $t$ 月面对完全资本市场（利率 $r$）。若购买车型 $j$：$\tau=0$ 期支付成交价 $p_{jmt}$；$\tau=1,\dots,H$ 期支付能源费用 $E_{ij\tau}$；$\tau=H$ 期获得残值 $RV_{ij}$。合成商品消费流为 $c_\tau$。现值预算约束为

$$
\sum_{\tau=0}^{H}\frac{c_\tau}{(1+r)^\tau}
=\mathcal W_i-p_{jmt}-\underbrace{\sum_{\tau=1}^{H}\frac{E_{ij\tau}}{(1+r)^\tau}}_{\equiv PVE_{ij}}
+\underbrace{\frac{RV_{ij}}{(1+r)^H}}_{\equiv PVR_{ij}}, \tag{M1.2}
$$

$\mathcal W_i$ 为终身财富现值。完全资本市场下，消费时间路径的最优安排与车辆选择**可分离**（Fisher 分离）：车辆选择只通过右端的“可用于消费的财富现值” $Y_{ij}=\mathcal W_i-p_{jmt}-PVE_{ij}+PVR_{ij}$ 影响消费效用。令 $\mathcal V_i(Y)$ 为给定财富 $Y$ 时最优安排消费所得的间接效用，$\Phi_{ij}$ 为拥有车型 $j$ 的服务流效用现值，则

$$
U_{ij}=\Phi_{ij}+\mathcal V_i\big(\mathcal W_i-p_{jmt}-PVE_{ij}+PVR_{ij}\big). \tag{M1.3}
$$

## M1.2.2 准线性近似与“收入边际效用” [D]

车辆的终身净成本 $c_{ij}\equiv p_{jmt}+PVE_{ij}-PVR_{ij}$ 相对终身财富 $\mathcal W_i$ 较小。对 $\mathcal V_i$ 在 $\mathcal W_i$ 处一阶展开：

$$
\mathcal V_i(\mathcal W_i-c_{ij})=\mathcal V_i(\mathcal W_i)-\lambda_i c_{ij}+O(c_{ij}^2),\qquad \lambda_i\equiv\mathcal V_i'(\mathcal W_i)>0. \tag{M1.4}
$$

$\lambda_i$ 是**终身财富的边际效用**（即“钱的边际效用”）。这正是 Small–Rosen 福利公式要求的条件：$\lambda_i$ 不随所考虑的车辆选择而变。加入随机效用冲击 $\tilde\varepsilon_{ij}=\sigma_\varepsilon\varepsilon_{ij}$（$\varepsilon_{ij}$ 为标准 I 型极值，独立同分布），并以 $\sigma_\varepsilon$ 归一化尺度：

$$
u_{ij}=\frac{U_{ij}}{\sigma_\varepsilon}
=\frac{\Phi_{ij}}{\sigma_\varepsilon}+\frac{\mathcal V_i(\mathcal W_i)}{\sigma_\varepsilon}
-\alpha_i\big(p_{jmt}+PVE_{ij}-PVR_{ij}\big)+\varepsilon_{ij},
\qquad \alpha_i\equiv\frac{\lambda_i}{\sigma_\varepsilon}. \tag{M1.5}
$$

**【参数定义 1：$\alpha_i$】** 价格系数 = 每元终身财富的效用（以 $\varepsilon$ 的尺度度量）。单位：效用/元；符号：$\alpha_i>0$。经济含义：消费者 $i$ 的收入边际效用；**它同时乘在购价和未来能源成本上**——这是“未来 1 元与今天 1 元可比”的预算约束含义，也是后面资本化率 $\gamma$ 能以“相对价格系数的比值”定义的根据。

## M1.2.3 收入异质性：从 BLP 的 Cobb–Douglas 规格推出 $\alpha_i$ 的形式 [D]

BLP（1995）式 (2.7a) 用 $\alpha\log(y_i-p_j)$ [O]。对价格求导得 $\partial u/\partial p=-\alpha/(y_i-p_j)\approx-\alpha/y_i$。即价格敏感度近似与收入成反比。推广为

$$
\alpha_i=\exp\big(a_0+a_y\ln y_i+\sigma_p\nu_{ip}\big),\qquad \nu_{ip}\sim N(0,1), \tag{M1.6}
$$

$a_y=-1$ 对应 BLP 的近似；对数正态保证 $\alpha_i>0$，避免正态抽样出现“喜欢涨价”的消费者（BKL 2024、Ji 等 2026 的中国汽车 BLP 均用此形式 [O·卡]）。$y_i$ 抽自市场 $m$ 的外部收入分布。

## M1.2.4 外部选项与两个归一化 [O]+[D]

外部选项效用 $u_{i0}=\Phi_{i0}/\sigma_\varepsilon+\mathcal V_i(\mathcal W_i)/\sigma_\varepsilon-\alpha_iPVE_{i0}+\varepsilon_{i0}$（继续使用旧车的服务与能耗）。份额只依赖效用差，故从所有选项减去外部选项的确定性部分：

$$
V_{i0}\equiv0,\qquad \mathcal V_i(\mathcal W_i)\ \text{在所有选项中抵消}. \tag{M1.7}
$$

两个后果：（i）所有“新车相对不买”的共同吸引力由带随机系数的内部常数 $\psi_{i,d}$ 吸收（BLP p.849 脚注 [O]）；（ii）**假设 A0**：工况改革不改变外部选项的效用（旧车的标签不变、车主凭驾驶经验已知旧车真实油耗）。尺度归一化 $\operatorname{Var}(\varepsilon)=\pi^2/6$ 使所有系数以 $\varepsilon$ 为单位，只有比值（支付意愿、资本化率）有绝对含义。

## M1.2.5 完全信息、无行为偏差的基准 [D]

若消费者确知真实能耗、按市场利率贴现且无注意偏差，则（略去与选择无关的常数）

$$
u^{*}_{ij}=\Phi_{ij}-\alpha_i\big(p_{jmt}+PVE_{ij}-PVR_{ij}\big)+\varepsilon_{ij}. \tag{M1.8}
$$

这就是 GRV（2018）式 (1) 中 $\gamma=1$ 的情形 [O]。后面所有“偏离”（信念、资本化）都相对 (M1.8) 定义。

---

# M1.3 生命周期能源成本：成本尺度 $K$ 的从零推导

## M1.3.1 燃油车与油电混动（ICE/HEV）[D]

第 $\tau$ 年能源费用 = 存活概率 × 年行驶里程 × 每公里油耗 × 油价：

$$
E^{F}_{ij\tau}=S_\tau\cdot VKT_{i}v_\tau\cdot\frac{e^{F}_{jm}}{100}\cdot\pi^{F}_{m,t+\tau}, \tag{M1.9}
$$

$S_\tau$ 为车龄 $\tau$ 仍在使用的概率，$VKT_i$ 为消费者 $i$ 的首年年里程（km/年），$v_\tau$ 为里程随车龄的衰减曲线（$v_1=1$），$e^F_{jm}$ 为真实道路油耗（L/100km，可随市场的气候、拥堵、地形而变），$\pi^F$ 为油价（元/L）。设油价期望为鞅（$E_t\pi_{m,t+\tau}=\pi_{mt}$，GRV 2018 与 Anderson–Kellogg–Sallee 2013 的设定 [O·卡]），则

$$
PVE^{F}_{ij}=\underbrace{\frac{\pi^{F}_{mt}\,VKT_i\,\Lambda(r,H)}{100}}_{\equiv K^{F}_{imt}}\;e^{F}_{jm},
\qquad \Lambda(r,H)\equiv\sum_{\tau=1}^{H}\frac{S_\tau v_\tau}{(1+r)^\tau}. \tag{M1.10}
$$

**【参数定义 2：$K^F_{imt}$（燃油成本尺度）】** 单位：元/(L/100km)，即“真实油耗每高 1 L/100km，生命周期能源成本现值增加多少元”。它由外部数据（油价、里程分布、存活曲线、利率）构造，不是自由参数。量纲核验：$\pi$[元/L]×$VKT$[km/年]×$\Lambda$[年]÷100 × $e$[L/100km] = 元。[I] 例：$\pi=7.5$、$VKT=12000$、$r=5\%$、$H=10$、$S_\tau=v_\tau=1$ 时 $\Lambda=7.72$，$K^F\approx6948$ 元；ICE 标签上调 7.7%（约 0.54 L/100km）若被完全相信并完全资本化，约等于 3750 元现值。

## M1.3.2 纯电（BEV）：有效电价与家充 [D]

$$
PVE^{E}_{ij}=K^{E}_{imt}\,e^{E}_{jm},\qquad
K^{E}_{imt}=\frac{\pi^{E}_{imt}\,VKT_i\,\Lambda(r,H)}{100},\qquad
\pi^{E}_{imt}=h_i\,\pi^{home}_{mt}+(1-h_i)\,\pi^{pub}_{mt}, \tag{M1.11}
$$

$e^E$ 为插座端电耗（kWh/100km，包含充电损耗；若数据为电池端须除以充电效率），$h_i\in\lbrace0,1\rbrace$ 为是否有家充桩（按城市有固定车位/家充比例抽样），$\pi^{home}$ 为居民电价，$\pi^{pub}$ 为公共快充电价含服务费。[I] 家充 0.55 元/kWh 与公充 1.6 元/kWh 时，15 kWh/100km 的车十年现值约 7600 元与 22200 元——**家充可得性本身就是巨大的异质性来源**（M5）。

## M1.3.3 插电混动（PHEV）：电驱里程份额 $UF$ 的推导 [D]

设消费者每天以概率 $\tilde h_i$ 从满电出发，日行驶距离 $D_i\sim F_{D,i}$；前 $\min(D_i,R)$ 公里用电（$R$ 为纯电续航），其余用油。电驱里程占比（utility factor）为

$$
UF_i(R)=\tilde h_i\,\frac{E[\min(D_i,R)]}{E[D_i]},\qquad
\frac{\partial UF_i}{\partial R}=\tilde h_i\,\frac{\Pr(D_i>R)}{E[D_i]}\ge0. \tag{M1.12}
$$

（导数由 $\frac{d}{dR}E[\min(D,R)]=\frac{d}{dR}\int_0^R(1-F_D(x))\,dx=\Pr(D>R)$ 得到。）每百公里能源费用与现值为

$$
\begin{aligned}
c^{P}_{ij}&=UF_i\big(\pi^{E}e^{E,CD}_{j}+\pi^{F}e^{F,CD}_{j}\big)+(1-UF_i)\,\pi^{F}e^{F,CS}_{j},\\
PVE^{P}_{ij}&=K^{F}_{imt}\big[UF_i\,e^{F,CD}_{j}+(1-UF_i)\,e^{F,CS}_{j}\big]+K^{E}_{imt}\,UF_i\,e^{E,CD}_{j},
\end{aligned} \tag{M1.13}
$$

CD 为电量消耗模式（可能同时耗少量油），CS 为电量保持模式（发动机发电所耗燃油已含在 $e^{F,CS}$ 中，不重复加电）。

**PHEV 标签的特殊性**：PHEV 的官方“综合油耗”是按工况规定的标准 $UF^{c}$ 加权的复合值，消费者自己的 $UF_i$ 与 $UF^c$ 不同。2021 年改革中 PHEV 综合油耗标签中位数上升约 59.3%、纯电续航中位数下降约 17.3%（本地同配置核对资产，需按动力与指标分别复核后引用）[P]。因此 PHEV 不应只用复合标签，而应尽量用分项标签 $(L^{R,CD},L^{F,CS},L^{E,CD})$ 代入 (M1.13)；只有复合值时作为近似并报告偏误方向。复合值与分项**不能同时**进入效用（会重复计价）。

## M1.3.4 残值（M1 中的处理）

$PVR_{ij}=(1+r)^{-H}E_t[RV_{ij}]$。残值可能依赖标签（二手车买家也看标签，BEV 续航标签影响保值率，P11/P12 卡），这是独立于能源成本的第二条渠道。M1 中以车型谱系固定效应与品牌×年固定效应吸收其平均水平；“标签→残值”的渠道放在 M8 作为扩展机制，不在 M1 中与能源成本重复计价。

---

# M1.4 信息结构：标签、真实值、信念与 M1 的比例信念

## M1.4.1 三个永远分开的状态变量 [P]

对指标 $k\in\lbrace F,E,R\rbrace$（油耗 L/100km、电耗 kWh/100km、续航 km）：

- $L^{k}_{jt}$：$t$ 月对消费者**展示**的官方标签值（工况 $c\in\lbrace N,W,C\rbrace$ 分别为 NEDC、WLTC、CLTC）；
- $T^{k}_{jm}$：市场 $m$ 共同使用口径下的**真实**道路表现（由硬件与使用环境决定，工况切换本身不改变它）；
- $B^{k}_{ijmt}=E_i[T^{k}_{jm}\mid\mathcal I_{ijmt}]$：消费者的**信念**（基于其信息集的主观期望）。

**绝不默认 $L=T=B$；也不把有名字的机制留在 $\xi$ 里再把 $\xi$ 解释为消费者认知。** 消费者看不到 $T$，所以决策中出现的是 $B$：

$$
\widehat{PVE}^{F}_{ij}=E_i\big[K^{F}_{imt}T^{F}_{jm}\mid\mathcal I\big]=K^{F}_{imt}B^{F}_{ijmt}
\quad(\text{$K$ 由公开油价与自身里程决定、与 $T$ 的主观不确定性独立}). \tag{M1.14}
$$

## M1.4.2 决策效用：资本化率与信念的乘积 [D]

允许消费者在决策时对未来能源成本赋予权重 $\gamma_d$（M3 将从现时偏好、有限注意、隐含贴现率三种理论分别推出它）：

$$
u^{D}_{ij}=\Phi_{ij}-\alpha_i\big(p_{jmt}+\gamma_{d}\,K_{imt}B_{ijmt}\big)+\varepsilon_{ij}. \tag{M1.15}
$$

**M1 的信息假设（A-M1，比例信念）**：消费者把标签按动力类型与标签所属工况的比例换算为真实预期：

$$
B^{k}_{jt}=\zeta^{k}_{d,s}\,L^{k}_{jt},\qquad s=s(j,t)\in\lbrace0,1\rbrace, \tag{M1.16}
$$

$s=0$ 表示展示的是旧工况（NEDC）标签，$s=1$ 表示新工况（WLTC/CLTC）标签。

**【参数定义 3：$\zeta^k_{d,s}$（感知真实/标签比）】** 无量纲。$\zeta=1$：照单全收；$\zeta=1.3$：消费者认为真实油耗比标签高 30%。它是信念参数而非偏好参数。代入 (M1.15)：

$$
u^{D}_{ij}=\Phi_{ij}-\alpha_i\Big(p_{jmt}+\varphi_{d,s}\,\underbrace{K_{imt}L_{jt}}_{\equiv G^{L}_{ijmt}}\Big)+\varepsilon_{ij},
\qquad \boxed{\varphi_{d,s}\equiv\gamma_d\,\zeta_{d,s}} \tag{M1.17}
$$

**【参数定义 4：$\varphi_{d,s}$（标签成本估值率）】** 由边际替代率定义：

$$
\varphi_{d,s}=\frac{\partial u^{D}_{ij}/\partial G^{L}_{ijmt}}{\partial u^{D}_{ij}/\partial p_{jmt}}. \tag{M1.18}
$$

含义：为抵消“标签隐含的生命周期能源成本”增加 1 元，消费者要求购价下降 $\varphi$ 元。无量纲；$\varphi>0$。$G^{L}_{ijmt}=K_{imt}L_{jt}$ 是“若把标签当真实值，生命周期能源成本现值是多少元”，称**标签隐含能源成本**。**$\varphi$ 是 M1 唯一能由市场数据稳健识别的能源估值参数**：它是资本化率 $\gamma$ 与信念映射 $\zeta$ 的乘积，单凭标签变化无法拆开（M3 用第二信源拆开）。这避免了“看到需求下降就说消费者不短视”的跳跃：需求下降只说明 $\varphi>0$。

## M1.4.3 两个可检验的信念基准 [D]

令 $w_j\equiv(L^{X}_j-L^{N}_j)/L^{N}_j$ 为同一硬件新旧工况的相对楔子，$\bar w_d$ 为动力 $d$ 的平均楔子（$X$ 为新工况）。

**(a) 天真表面值（naive face value）**：消费者没有意识到工况换了尺子，$\zeta_{d,1}=\zeta_{d,0}$，于是

$$
H_0^{naive}:\ \varphi_{d,1}=\varphi_{d,0}. \tag{M1.19}
$$

**(b) 表示不变性（representation invariance）**：消费者完全理解两种工况的平均换算，平均楔子的车型信念不变：$\zeta_{d,1}L^{X}_j=\zeta_{d,0}L^{N}_j$ 对 $w_j=\bar w_d$ 成立，故 $\zeta_{d,1}=\zeta_{d,0}/(1+\bar w_d)$，

$$
H_0^{RI}:\ \varphi_{d,1}\,(1+\bar w_d)=\varphi_{d,0}. \tag{M1.20}
$$

在 (b) 下车型 $j$ 的信念变化为 $B_{post}/B_{pre}=(1+w_j)/(1+\bar w_d)$：**只有高于平均的楔子才让消费者推断该车真实油耗更高**。这是有经济含义的：若新工况更接近真实驾驶，楔子大说明该车旧标签被 NEDC“美化”得更多，理性消费者据此下调对它的评价。(a)、(b) 都可被数据拒绝；拒绝二者正是 M2（可信度机制）登场的理由。

---

# M1.5 续航与补能：续航缺口函数 $A_i(R)$ 的推导

## M1.5.1 从出行需要推出 [D]

消费者 $i$ 每年有 $f_i$ 次长距离出行，单次距离 $D\sim F_{D}$（外部出行调查）。若有效续航为 $R$，单次出行的“续航缺口”为 $(D-R)_+$（需中途补能或改用其他交通的公里数）。年期望缺口为

$$
A_i(R)=f_i\int_{R}^{\infty}(D-R)\,dF_D(D)=f_i\,E\big[(D-R)_+\big]. \tag{M1.21}
$$

由 Leibniz 法则：

$$
A_i'(R)=-f_i\Pr(D>R)\le0,\qquad A_i''(R)=f_i\,g_D(R)\ge0. \tag{M1.22}
$$

即续航越长缺口越小，但边际改善递减（凸递减）。

## M1.5.2 进入效用与补能密度的替代关系 [P]+[D]

$$
-\eta_i\,\chi(N_{mt})\,A_i\big(B^{R}_{ijmt}\big)\cdot\mathbf 1\lbrace d(j)=\mathrm B\rbrace,\qquad \chi'(N)<0,\ \chi(\bar N)=1, \tag{M1.23}
$$

**【参数定义 5：$\eta_i$（续航缺口负效用）】** 每公里年期望缺口的效用损失；$\eta_i/\alpha_i$ 为其货币价值（元/公里缺口）。$\chi(N)$ 为补能密度 $N_{mt}$（每万人或每平方公里公共充电桩）的调节函数，$\chi(\bar N)=1$ 是尺度归一化（否则 $\eta$ 与 $\chi$ 的水平不能同时识别）。由 (M1.22)–(M1.23)：

$$
\frac{\partial u}{\partial R}=\eta_i\chi f_i\Pr(D>R)>0,\qquad
\frac{\partial^2u}{\partial R^2}=-\eta_i\chi f_ig_D(R)\le0,\qquad
\frac{\partial^2u}{\partial R\,\partial N}=\eta_i\chi'(N)f_i\Pr(D>R)<0. \tag{M1.24}
$$

第三式表明**续航与补能网络互为替代**：充电越方便，多 1 公里续航越不值钱——与 Barwick 等（2026，上海车联网动态模型）“续航与充电可得性互为替代、都边际递减”的发现一致 [O·卡]。PHEV 有发动机兜底，不设 $A$ 项，其纯电续航经 $UF$ 进入能源成本 (M1.13)。

M1 中续航信念同样用比例形式 $B^R=\zeta^R_{s}L^R$，并以 $\zeta^R_0=1$ 归一化（NEDC 续航按表面值），只估计新工况的相对比 $\zeta^R_1$。若缺乏出行距离分布，可用 $\eta_i\ln B^R$ 作简约替代（同样凸递减），**二者只能选一，不能叠加**。

---

# M1.6 口碑评分：整体评分与分项评分如何进入效用

## M1.6.1 经验品质量的贝叶斯信号模型 [D]

汽车的空间、动力、操控、舒适、外观、内饰、性价比等是**经验品属性**：购前难以完全观察。设车型 $j$ 的真实经验质量向量 $q_j=(q_{j1},\dots,q_{jK})$，先验 $q_{jk}\sim N(\bar q_k,\sigma^2_{qk})$。第 $n$ 位车主的分项评分 $r_{njk}=q_{jk}+e_{njk}$，$e_{njk}\sim N(0,\sigma^2_{ek})$ 独立。截至 $t-1$ 有 $n_{j,t-1}$ 条评论，样本均值 $\bar r_{jk,t-1}$。正态共轭后验均值为

$$
\widetilde Q^{k}_{j,t-1}\equiv E[q_{jk}\mid r]=\bar q_k+\underbrace{\frac{n_{j,t-1}\sigma^2_{qk}}{n_{j,t-1}\sigma^2_{qk}+\sigma^2_{ek}}}_{\text{收缩权重}\in(0,1)}\big(\bar r_{jk,t-1}-\bar q_k\big). \tag{M1.25}
$$

风险中性下质量进入效用为 $\sum_k\theta_k\widetilde Q^k_{j,t-1}$。评论越多，后验越接近样本均值；评论越少，越向类别均值收缩。**这回答了“口碑应当如何构造”：用收缩后验均值，而不是原始均分，更不是“评分×条数”。**

## M1.6.2 整体评分 vs 分项评分：一个可检验的限制 [D]

若平台整体分是分项的加权和 $r^{all}_{nj}=\sum_k\omega_kr_{njk}+e^{all}_{nj}$，则

$$
\sum_k\theta_k\widetilde Q^{k}=\theta\sum_k\omega_k\widetilde Q^{k}\approx\theta\,\widetilde Q^{all}
\quad\Longleftrightarrow\quad \theta_k=\theta\,\omega_k\ \ \forall k. \tag{M1.26}
$$

结论：（i）分项可得时用分项（更一般）；（ii）只用整体分等价于施加 $\theta_k\propto\omega_k$，可用 Wald 检验；（iii）**整体分与全部分项同时放入会近乎完全共线**，系数无经济含义；（iv）品牌整体口碑是跨车型共同信号，用品牌×年固定效应或品牌层面后验吸收。

## M1.6.3 能耗分项与车主实测油耗不进口味项 [D]

“油耗/电耗”分项与车主报告的实际油耗、实际续航是**关于 $T$ 的信号**，属于信念形成（M2 的第二信源），而不是独立的口味。若把它放进 $\theta$，同一能源成本会经 $\gamma K B$ 与 $\theta_{energy}$ 计价两次。M1 中将其排除在 $\theta$ 之外（稳健性中可加入并解释为“非货币的能耗满意度”）。

## M1.6.4 内生性与选择 [D]

评分反映了部分原本藏在 $\xi$ 中的质量，把它显式化后，剩余 $\xi$ 仍可能与评分相关（持续性质量）。处理：（a）用 $t-1$ 期之前的评论（先决）；（b）谱系固定效应吸收不随时间变化的质量，识别来自谱系内评分随评论累积的变化；（c）领先项检验（$\widetilde Q_{j,t+1}$ 不应预测 $t$ 期份额残差）；（d）评论者是已购车主，评论选择性只影响信号含义，不改变“消费者在决策时看到它”的事实。

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

PHEV 的 $UF_i=UF_i(\zeta^R_sL^{R,CD}_{jt})$ 由 (M1.12) 计算。

## M1.7.2 M1 的完整效用（基准规格）[P]

$$
\boxed{
\begin{aligned}
u_{ijmt}={}&\psi_{i,d(j)}+x_{jmt}'\beta_i+\sum_{k}\theta_k\widetilde Q^{k}_{j,t-1}
-\alpha_i\Big[p_{jmt}+\varphi_{d(j),s(j,t)}\,G^{L}_{ijmt}\Big]\\
&-\eta_i\,\chi(N_{mt})\,A_i\big(\zeta^{R}_{s}L^{R}_{jt}\big)\mathbf 1\lbrace d(j)=\mathrm B\rbrace+\xi_{jmt}+\varepsilon_{ijmt},
\qquad u_{i0mt}=\varepsilon_{i0mt}.
\end{aligned}}
\tag{M1.28}
$$

随机系数：$\psi_{i,d}=\bar\psi_d+\sigma_d\nu_{id}$（动力类型偏好，捕捉“同动力内更强替代”）；$\beta_i=\bar\beta+\Pi D_i+\Sigma\nu_i$（对尺寸、功率/车重等的观测与未观测异质性，$D_i$ 为人口特征抽样）；$\alpha_i$ 见 (M1.6)；$K_{imt}$ 与 $UF_i$、$h_i$ 随里程、家充抽样而异；$\eta_i=\bar\eta$（M1 中同质，异质性来自 $f_i$ 与 $A_i$）。

## M1.7.3 平均效用与个体偏离 [O]+[D]

按 BLP 式 (6.1) [O] 的结构：

$$
\begin{aligned}
\delta_{jmt}&=\bar\psi_{d(j)}+x_{jmt}'\bar\beta+\sum_k\theta_k\widetilde Q^{k}_{j,t-1}+\xi_{jmt},\\
\mu_{ijmt}&=\sigma_{d(j)}\nu_{id(j)}+x_{jmt}'(\Pi D_i+\Sigma\nu_i)
-\alpha_i\big[p_{jmt}+\varphi_{d,s}G^{L}_{ijmt}\big]-\eta_i\chi(N_{mt})A_i(\zeta^{R}_sL^R_{jt})\mathbf 1\lbrace\mathrm B\rbrace .
\end{aligned} \tag{M1.29}
$$

因为 $\alpha_i$ 为对数正态、无“均值 + 偏离”的可加分解，价格与能源成本项**整体放在 $\mu$**（与 BKL 2024、Ji 等 2026 的写法一致；也与 BLP 原文“价格通过 $\alpha\log(y-p)$ 进入非线性部分，故 $\xi_j=\delta_j-x_j\beta$”一致 [O]）。线性参数 $\theta_1=(\bar\psi,\bar\beta,\theta,\text{固定效应})$；非线性参数 $\theta_2=(a_0,a_y,\sigma_p,\sigma_d,\Pi,\Sigma,\varphi_{d,s},\zeta^R_1,\bar\eta,\chi(\cdot)\text{参数})$。

## M1.7.4 个体选择概率与市场份额 [O]

$$
P_{ijmt}=\frac{\exp(\delta_{jmt}+\mu_{ijmt})}{1+\sum_{k\in\mathcal J_{mt}}\exp(\delta_{kmt}+\mu_{ikmt})},\qquad
s_{jmt}=\int P_{ijmt}\,dF_{mt}(\nu,D,VKT,h)\approx\frac1{NS}\sum_{i=1}^{NS}P_{ijmt}. \tag{M1.30}
$$

即 BLP 式 (6.6)(6.7)(6.10) [O]。所有抽样（收入、里程、家充、日行驶距离、$\nu$）**在估计与全部反事实中固定**（共同随机数）。

---

# M1.8 政策如何进入 BLP：标签跳变、楔子与反事实标签

## M1.8.1 标签状态方程 [P]

$$
L_{jt}=\big(1-S_{jt}\big)L^{N}_{jt}+S_{jt}L^{X}_{jt},\qquad S_{jt}=\mathbf 1\lbrace t\ge T^{show}_j\rbrace, \tag{M1.31}
$$

$T^{show}_j$ 是消费者实际看到新工况标签的首月（与法定资格日 $T^{law}_j$、认证日 $T^{cert}_j$ 区分）。混合展示可令 $S_{jt}\in[0,1]$ 为新标签展示比例。

## M1.8.2 用户的方法：用前 $n$ 期旧工况值外推切换年的旧工况标签 [P]+[D]

对切换时硬件不变的配置，其切换年不存在官方 NEDC 值。用户的方法是用该配置切换前 $n$ 期的 NEDC 值预测同一技术状态下的 NEDC 值：

$$
\widehat L^{N}_{j,T_j}=f\big(L^{N}_{j,T_j-1},\dots,L^{N}_{j,T_j-n};H_j\big),\qquad
W_j\equiv L^{X}_{j,T_j}-\widehat L^{N}_{j,T_j},\qquad
w_j\equiv\ln L^{X}_{j,T_j}-\ln\widehat L^{N}_{j,T_j}. \tag{M1.32}
$$

$H_j$ 为不随工况改变的硬件特征（排量、整备质量、变速器、电池容量）。最简单的 $f$ 是“切换前最后一个 NEDC 值”（硬件不变时）；本地验证显示它与同配置双测值相关 0.8746、差值中位数为 0、测量误差约占楔子方差 24.6%（可靠度 0.754）[P，需复核原表]。

**楔子在 M1 中的三个用途**（它不是另一个独立的效用项）：

1. **定义标签跳变**：实际进入效用的是 $L_{jt}$；对硬件不变的配置，$L_{jt}$ 在 $T^{show}_j$ 处跳变 $W_j$。
2. **构造无改革反事实**：$L^{cf}_{jt}=\widehat L^{N}_{jt}$（M7 的反事实 CF1）。
3. **构造预定工具变量**：$Z^{W}_{jt}=Elig^{law}_{jt}\times K_{mt}\widehat W_j(H_{j,pre})$（§M1.10.3），用法定资格与改革前硬件预测的楔子处理“企业选择展示时点”的内生性。

## M1.8.3 切换时的效用变化分解 [D]

同一消费者、同一硬件、同一价格、同一 $K$，由 (M1.28)：

$$
\Delta u_{ij}=-\alpha_iK_{imt}\big[\varphi_{d,1}L^{X}_j-\varphi_{d,0}L^{N}_j\big]
=\underbrace{-\alpha_iK_{imt}\varphi_{d,1}W_j}_{\text{数值效应}}
\ \underbrace{-\ \alpha_iK_{imt}\big(\varphi_{d,1}-\varphi_{d,0}\big)L^{N}_j}_{\text{再估值效应}}. \tag{M1.33}
$$

“数值效应”是新数字本身（按新估值率计价）；“再估值效应”是消费者对每单位标签的信念/估值改变。两个基准下：

$$
\Delta u_{ij}\big|_{naive}=-\alpha_iK_{imt}\varphi_{d,0}W_j,\qquad
\Delta u_{ij}\big|_{RI}=-\alpha_iK_{imt}\varphi_{d,0}L^{N}_j\,\frac{w_j-\bar w_d}{1+\bar w_d}\quad(W_j=w_jL^N_j). \tag{M1.34}
$$

**这正面回答了“油耗数值提高反而需求增加”是否可能**：在 M1 内只有当 $\varphi_{d,1}L^X_j<\varphi_{d,0}L^N_j$，即再估值效应为正且超过数值效应时才可能——这要求消费者对新标签每单位的信念换算显著下降（相信新标签“更真实、不用再自行加价”）。这一条件的经济含义与识别由 M2 展开；M1 只提供检验：估计 $\varphi_{d,1}/\varphi_{d,0}$ 并与 $1$（天真）和 $1/(1+\bar w_d)$（表示不变）比较。

## M1.8.4 “单列一项”与“放进特征”：等价与重复计价 [D]

若在 (M1.28) 之外再加一个自由系数的政策项 $\tau_dW_jS_{jt}$：由 (M1.31)，$L_{jt}$ 已经包含 $W_jS_{jt}$，故

$$
-\alpha_i\varphi_dK L_{jt}+\tau_dW_jS_{jt}
=-\alpha_i\varphi_dK L^{N}_j-\big(\alpha_i\varphi_dK-\tau_d\big)W_jS_{jt}. \tag{M1.35}
$$

$\tau_d$ 只是在吸收“再估值”与任何直接效应，与分工况的 $\varphi_{d,s}$ 不能同时自由识别。**规则**：要么用结构写法（分工况 $\varphi_{d,s}$），要么用 M0 的简约写法（只放楔子），不能二者都自由。同理，不能再放“真实—标签差距”$T-L$ 作为另一特征：真实值固定时 $\partial(T-L)=-\partial L$，它是标签的镜像，两者系数无法区分“数值效应”与“信任效应”。

## M1.8.5 非信息的机械通道：必须进入价格或成本 [P]

工况切换还会经制度规则机械地改变价格与成本，这些**不是信息效应**，必须显式放进 $p$ 或 $mc$：

- 新能源补贴：2017–2022 年中央补贴 = 续航档基础额 × 电池能量密度系数 × 电耗系数（Ji 等 2026 卡）[O·卡]；若补贴按所在工况的认证续航与电耗计算，切换会改变补贴额，进入消费者净价 $p_{jmt}=(1+\tau_{jt})p^{s}_{jmt}-sub_{jt}$。
- 购置税：燃油车 10%（2022-06 至 2022-12 对 ≤2.0L 且 ≤30 万元减半），新能源免征且有技术门槛；资格变化进入 $\tau_{jt}$。
- 双积分（CAFC 与 NEV 积分）：WLTC 下燃油车实测油耗上升直接改变企业积分账户，进入有效边际成本（M6）。

**2023 年 1 月同时是在产燃油车强制切换截止、购置税减半到期、中央补贴退出的月份**，日历断点严重混杂，不能把该月的总体跳变归因于标签（M0 详述）。

---

# M1.9 边际效应、弹性与支付意愿（“单列”燃油经济性）

由 $\partial P_{ij}/\partial V_{ij}=P_{ij}(1-P_{ij})$、$\partial P_{ik}/\partial V_{ij}=-P_{ij}P_{ik}$ 与 $\partial V_{ij}/\partial L_j=-\alpha_i\varphi_{d,s}K_{imt}$（ICE）：

$$
\frac{\partial s_{jmt}}{\partial L_{jt}}=-\int\alpha_i\varphi_{d,s}K_{imt}P_{ij}(1-P_{ij})\,dF<0,\qquad
\frac{\partial s_{kmt}}{\partial L_{jt}}=\int\alpha_i\varphi_{d,s}K_{imt}P_{ij}P_{ik}\,dF>0\ (k\neq j). \tag{M1.36}
$$

核验：$\sum_{k\ne j}\partial s_k/\partial L_j+\partial s_0/\partial L_j=-\partial s_j/\partial L_j$（份额加总恒为 1）。弹性与支付意愿：

$$
\epsilon^{L}_{jj}=\frac{L_{jt}}{s_{jmt}}\frac{\partial s_{jmt}}{\partial L_{jt}},\qquad
WTP_i(\Delta L=-1)=-\frac{\partial V_{ij}/\partial L_j}{\partial V_{ij}/\partial p_j}=\varphi_{d,s}K_{imt}\ \text{（元）}. \tag{M1.37}
$$

**标签转移率（label diversion）**：$j$ 的标签变差时流失的份额去向

$$
D^{L}_{j\to k}=\frac{\partial s_k/\partial L_j}{-\partial s_j/\partial L_j}
=\frac{\int w_{ij}P_{ij}P_{ik}\,dF}{\int w_{ij}P_{ij}(1-P_{ij})\,dF},\qquad w_{ij}=\alpha_i\varphi_{d,s}K_{imt},\qquad
\sum_{k\ne j}D^{L}_{j\to k}+D^{L}_{j\to0}=1. \tag{M1.38}
$$

与价格转移率（权重 $w_{ij}=\alpha_i$）相比，标签转移率给**高里程、高油价地区**的消费者更大权重——他们更可能转向低油耗燃油车、HEV 或电动车。这一差异是 M4 讨论跨动力替代的核心。BEV 续航：

$$
\frac{\partial s_{jmt}}{\partial L^{R}_{jt}}=\int\eta_i\chi(N_{mt})\zeta^R_sf_i\Pr\big(D>\zeta^R_sL^R_{jt}\big)P_{ij}(1-P_{ij})\,dF>0,\qquad
WTP_i(+1\text{km})=\frac{\eta_i\chi\zeta^R_sf_i\Pr(D>\zeta^R_sL^R)}{\alpha_i}. \tag{M1.39}
$$

---

# M1.10 估计：反演、$\xi$ 结构、工具变量与 GMM

## M1.10.1 Berry 反演 [O]

给定 $\theta_2$，在每个市场—月解 $s(\delta;\theta_2)=s^{obs}$，用 BLP 式 (6.8) 的收缩映射 [O]：

$$
\delta^{h+1}_{mt}=\delta^{h}_{mt}+\ln s^{obs}_{mt}-\ln s_{mt}(\delta^{h}_{mt};\theta_2),\qquad \lVert\delta^{h+1}-\delta^{h}\rVert_\infty<10^{-12}. \tag{M1.40}
$$

BLP 附录 I 证明其模小于 1、不动点唯一 [O]。零销量不能直接代入对数：先区分“未在售”（从 $\mathcal J_{mt}$ 删去）与“在售但零销量”（聚合到季度或用微观似然处理），不能随意加小常数。

## M1.10.2 $\xi$ 的分解与固定效应 [P]

$$
\xi_{jmt}=\xi_{g(j)}+\xi_{b(j),y(t)}+\xi_{d(j),m,t}+\Delta\xi_{jmt}, \tag{M1.41}
$$

$\xi_g$：车型谱系固定效应（吸收不随时间变化的质量、平均残值、品牌形象）；$\xi_{b,y}$：品牌×年；$\xi_{d,m,t}$：动力×市场×月（吸收各动力共同的政策、限牌、补贴退坡、充电网络、季节）。于是**识别来自谱系内跨月变化与同动力同月内跨产品差异**：标签跳变、油价/电价 × 标签的交互、口碑更新、价格中的成本冲击。注意 $\xi_{d,m,t}$ 会吸收同动力同月的共同跳变，因此“标签的共同成分”只能靠交错切换时点识别（M0）。

## M1.10.3 工具变量：逐条给出相关性与排除理由 [P]

| 内生对象 | 工具 | 相关性 | 排除限制与威胁 |
|---|---|---|---|
| 价格 $p$ | 钢价指数$_t$ × 整备质量$_j$ | 车身材料成本随钢价变动，重车更敏感 | 钢价不直接改变消费者对某车的偏好；威胁：钢价与宏观需求同步（由 $\xi_{d,m,t}$ 吸收） |
| 价格 $p$（BEV/PHEV） | 碳酸锂或电芯价格指数$_t$ × 电池容量$_j$ | 电池占电动车成本 30–40%，容量越大成本暴露越大 | 锂价是全球供给冲击；威胁：容量是企业选择（M4/M6 处理容量内生） |
| 价格 $p$（合资） | 日元/欧元/韩元汇率$_t$ × 外方国别$_b$ × 进口零部件比重 | 进口零部件成本随汇率变化 | 汇率不直接改变中国消费者偏好；威胁：汇率与外方品牌形象冲击相关 |
| 价格 $p$ | BLP 竞争者特征和：同企业其他产品、其他企业产品的特征和（按动力×细分） | 近邻竞争越多，加价越低 | BLP 式 (5.8) 的经典论证 [O]；威胁：产品组合内生 |
| 价格与随机系数 | 差异化工具（Gandhi–Houde）：特征空间中距离 $j$ 小于一个标准差的竞品数（尺寸、功率、$G^L$、续航） | 局部竞争强度决定加价与替代 | 以产品集合外生为前提；对 $\sigma$ 的识别尤其重要 |
| $\sigma_d$ | 同动力在售车型数、新上市车型数 | 选择集变化改变近邻替代 | 进入时点需外生于当月 $\Delta\xi$ |
| 标签项 $KL_{jt}$（展示时点内生时） | $Z^{W}_{jt}=Elig^{law}_{jt}\times K_{mt}\widehat W_j(H_{j,pre})$ | 法定资格迫使切换，预测楔子决定跳变幅度 | 用法定截止而非企业实际选择；威胁：资格与补贴、税收资格机械相关（须同时控制） |

**标签项是“包含的外生变量”而非“排除的价格工具”**：标签直接进入效用，不能再拿它当价格工具（构造协议 §4.1 [P]）。

## M1.10.4 GMM 目标函数与线性参数浓缩 [O]+[D]

$$
g_N(\theta)=\frac1{N}\sum_{jmt}Z_{jmt}\,\Delta\xi_{jmt}(\theta),\qquad
\widehat\theta=\arg\min_{\theta}\ g_N(\theta)'\,\mathbb W\,g_N(\theta). \tag{M1.42}
$$

给定 $\theta_2$，$\delta(\theta_2)$ 已由反演得到，$\delta=X_1\theta_1+\xi$ 对 $\theta_1$ 线性，可浓缩：

$$
\widehat\theta_1(\theta_2)=\big(X_1'Z\mathbb WZ'X_1\big)^{-1}X_1'Z\mathbb WZ'\,\delta(\theta_2), \tag{M1.43}
$$

外层只对 $\theta_2$ 数值搜索（BLP 第 6.5 节 [O]）。两步 GMM：第一步 $\mathbb W=(Z'Z)^{-1}$，第二步用残差构造的异方差（按谱系聚类）权重，并可用 Chamberlain/BLP 近似最优工具提高随机系数精度（GRV 2018、Reynaert–Verboven 2014 [O·卡]）。约束：$\varphi_{d,s}\ge0$、$\bar\eta\ge0$ 以参数变换（$\varphi=\exp(\tilde\varphi)$）实现。

## M1.10.5 推断

（i）按车型谱系聚类（同一认证配置在城市与月份的复制行不是独立样本）；（ii）标准误含模拟误差（BLP 式 (5.6) 的 $V_3$ [O]）；（iii）$K$（外部里程分布）、$\widehat L^N$（外推）、$\widetilde Q$（收缩）均为生成变量，用“重抽谱系 → 重做外推与收缩 → 重估”的全流程自助法；（iv）全国共同改革的有效冲击数有限，推断层级要与冲击层级一致。

## M1.10.6 算法步骤（可直接编码）

1. 固定抽样：每个 $(m,t)$ 抽 $NS=500\sim1000$ 个类型（Halton/Sobol），每个类型含 $(y_i,VKT_i,h_i,F_{D,i},\nu_i)$，计算 $K^F_{imt}$、$K^E_{imt}$、$UF_i$、$A_i(\cdot)$ 所需的分布量。
2. 外层给定 $\theta_2$：算 $\mu_{ijmt}$（含 $\varphi_{d,s}G^L$、续航项）。
3. 内层：逐市场—月收缩映射 (M1.40) 得 $\delta$。
4. 浓缩 $\theta_1$ (M1.43)，得 $\Delta\xi$，算 GMM 目标 (M1.42)。
5. 外层优化（Knitro/L-BFGS-B，解析梯度，50 组初值），检查一阶与二阶条件。
6. 诊断（§M1.13）。由于 $-\alpha_i\varphi K_iL_j$ 是“对数正态随机系数 × 外部抽样 × 产品特征”的三重乘积，标准 pyblp 公式不直接支持；建议自写内层（numpy/JAX），并用 pyblp 估计去掉该结构的嵌套简化版作交叉验证。

---

# M1.11 识别：参数—变异—矩登记表

| 参数 | 经济含义 | 识别它的变异 | 对应矩 | 失败时如何降级 |
|---|---|---|---|---|
| $a_0,a_y,\sigma_p$ | 收入边际效用及其收入梯度 | 成本冲击引起的价格变化；跨市场收入分布差异 | $E[Z^{cost}\Delta\xi]=0$ | 价格异质性不显著时令 $\sigma_p=0$ |
| $\varphi_{d,0}$ | 旧标签成本估值率 | 改革前：谱系内不同发动机版本的标签差 × 油价/里程（GRV 型变异） | $E[(KL)\Delta\xi]=0$（包含外生变量） | 报告分动力的复合 $\varphi$ |
| $\varphi_{d,1}$ | 新标签成本估值率 | 改革后同类变异 + 同硬件标签跳变（交错时点） | 同上 + $E[Z^W\Delta\xi]=0$ | 若跳变与改款捆绑，限于严格同配置样本 |
| $\varphi_{d,1}/\varphi_{d,0}$ | 再估值（信念换算变化） | 同硬件跳变 × 楔子的跨产品差异 | 检验 (M1.19)(M1.20) | 只报“与天真/表示不变一致或拒绝” |
| $\sigma_d$ | 同动力内相关偏好 | 选择集变化、新车型进入、各动力份额随时间变化 | 差异化工具矩 | 退回固定动力偏好 + 嵌套 logit 作对照 |
| $\Pi,\Sigma$ | 人口与未观测口味异质性 | 跨城市人口分布差异（城市数据）；产品组合变化 | 人口 × 特征工具 | 仅全国数据时少设随机系数 |
| $\bar\eta,\zeta^R_1$ | 续航缺口负效用、新工况续航换算 | 同谱系不同电池版本的续航差；补能密度跨城跨期变化；CLTC 切换跳变 | 续航 × 补能交互矩 | 改用 $\eta\ln R$ 简约式 |
| $\theta_k$ | 经验质量的边际效用 | 谱系内口碑随评论累积的变化 | $E[\widetilde Q\Delta\xi]=0$（先决性） | 只用整体分（受限式 (M1.26)） |

**一个关键的过度识别检验（通向 M3）**：在 M1 的比例信念下，油价变化（改变 $K$）与标签变化（改变 $L$）都通过同一个乘积 $KL$ 进入，因此“对油价的反应”与“对标签的反应”必须给出同一个 $\varphi_{d,s}$：

$$
\frac{\partial u/\partial K}{L}=\frac{\partial u/\partial L}{K}=-\alpha_i\varphi_{d,s}. \tag{M1.44}
$$

若数据拒绝 (M1.44)——例如油价反应显著大于标签反应——说明消费者的信念不是标签的比例函数，而是含有与标签无关的成分（车主口碑、经验），正是 M2/M3 双信源模型的入口：油价反应度量“对信念的资本化”，标签反应度量“资本化 × 对标签的信任”。

---

# M1.12 供给侧最小块（为 M6、M7 准备）

## M1.12.1 消费者价、企业净收与税补楔子 [O]+[D]

$p^{c}_{jmt}=(1+\tau_{jt})p^{s}_{jt}-sub_{jt}$：$p^s$ 为企业净收（不含购置税），$\tau$ 为购置税率，$sub$ 为补贴。企业 $f$ 在全国统一定价时：

$$
\Pi_f=\sum_{m}M_{mt}\sum_{j\in\mathcal J_f}\big(p^{s}_{jt}-mc^{eff}_{jt}\big)s_{jmt}(p^c)-F_f. \tag{M1.45}
$$

## M1.12.2 一阶条件与 $\Delta$ 矩阵方向 [O]+[D]

由链式法则 $\partial s_{km}/\partial p^s_j=(1+\tau_j)\,\partial s_{km}/\partial p^c_j$，内点 FOC 为

$$
\sum_{m}M_{mt}\Big[s_{jmt}+\sum_{k\in\mathcal J_f}\big(p^{s}_{kt}-mc^{eff}_{kt}\big)(1+\tau_{jt})\frac{\partial s_{kmt}}{\partial p^{c}_{jt}}\Big]=0. \tag{M1.46}
$$

定义（BLP 式 (3.4) 方向：第 $j$ 行是 $j$ 的价格 FOC，第 $k$ 列是 $k$ 的利润边际）

$$
\Delta_{jk}=-O_{jk}\sum_mM_{mt}(1+\tau_{jt})\frac{\partial s_{kmt}}{\partial p^{c}_{jt}},\qquad
\tilde s_j=\sum_mM_{mt}s_{jmt},\qquad
\boxed{p^{s}-mc^{eff}=\Delta^{-1}\tilde s}. \tag{M1.47}
$$

$O_{jk}=\mathbf 1\lbrace f(j)=f(k)\rbrace$ 为基准；合资企业的利润分成可用 $O_{jk}\in[0,1]$ 作 conduct 敏感性（“合资”标签本身不等于内部化权重）。需求导数按 BLP (6.9a)(6.9b)（已补回 (6.9b) 前置负号）[O]：在本规格下 $\partial s_k/\partial p^c_j=\int\alpha_iP_{ij}P_{ik}\,dF>0$（$k\neq j$），$\partial s_j/\partial p^c_j=-\int\alpha_iP_{ij}(1-P_{ij})\,dF<0$。准线性下需求雅可比对称，两种 $\Delta$ 方向一致；若改用收入效应规格则必须按 (3.4) 方向（见 micro_foundations §7(c)）。

## M1.12.3 有效边际成本 [P]

$mc^{eff}_{jt}=mc_{jt}+v^{CAFC}_t\,a^{CAFC}_{jt}-v^{NEV}_t\,a^{NEV}_{jt}$：$a$ 为每辆车消耗/产生的积分，$v$ 为积分影子价格。反推出的是 $mc^{eff}$ 而不是纯制造成本；WLTC 改变燃油车的 $a^{CAFC}$，因此改革同时是需求冲击与合规成本冲击（推导见 M6）。成本方程 $\ln mc_{jt}=w_{jt}'\gamma^c+\omega_{jt}$ 给供给矩 $E[Z^S\omega]=0$（BLP 式 (3.1)(3.6) [O]）。

---

# M1.13 退化、嵌套与诊断

**精确退化**（每一步只放松一个限制）：

1. $\sigma_d=0,\ \Pi=\Sigma=0,\ \sigma_p=0,\ a_y=0,\ VKT_i=\overline{VKT}_m,\ h_i=\bar h_m$ ⇒ 同质 logit，$\ln s_j-\ln s_0=\delta_j+\mu_j$ 有闭式，即 M0 的基础回归 (M0.6)。
2. $\varphi_{d,1}=\varphi_{d,0}$ ⇒ 天真表面值模型；$\varphi_{d,1}(1+\bar w_d)=\varphi_{d,0}$ ⇒ 表示不变模型。
3. M2 的双信源信念中令车主信源权重为 0、感知偏差为常数比例 ⇒ 回到 M1 的比例信念（见 M2）。

**诊断清单**：（a）价格第一阶段与 Sanderson–Windmeijer F；（b）矩雅可比按单位缩放后的奇异值与条件数（$\varphi_{d,0},\varphi_{d,1}$ 的联合秩）；（c）自价格弹性应在 $-3$ 至 $-8$、加价率 10%–35% 合理区间，反推 $mc^{eff}>0$；（d）收缩映射收敛与积分节点加倍稳定性；（e）多初值；（f）$\varphi$ 的跨识别源一致性检验 (M1.44)；（g）**样本内份额拟合由反演机械保证，不是验证**，需留出月份/城市预测与改革事件梯度的外部验证。

---

# M1.14 M1 的可检验预测与边界

**可检验预测**：

- P1（数值效应）：同硬件、同价格下，楔子 $W_j$ 越大，切换后份额相对下降越多，幅度为 $-\int\alpha_iK_i\varphi_{d,1}P_{ij}(1-P_{ij})dF\cdot W_j$。
- P2（再估值）：$\varphi_{d,1}/\varphi_{d,0}$ 与 $1$、$1/(1+\bar w_d)$ 的比较区分“天真”与“表示不变”。
- P3（里程梯度）：标签效应随 $K$（油价、里程）增强——若完全不随 $K$ 变化，说明标签响应不是经由能源成本，而是另一种通道（显著性、品牌信号）。
- P4（替代去向）：被标签冲击的车型份额主要流向特征相近、能耗更低的产品与外部选项，权重偏向高里程消费者 (M1.38)。

**M1 能回答**：标签变化在多大程度上被计价（$\varphi$）、新旧标签每单位的估值是否变化、标签冲击下的替代去向、固定价格与重新定价下的份额变化。

**M1 不能单独回答**：消费者是否短视（$\gamma$）、是否信任标签（信念权重）——它们在 M1 中只以乘积出现；这正是 M2、M3 的任务。

---

# M1.15 来源说明

[O] BLP（1995）式 (2.1)(2.2)(2.5)(2.7)(3.1)–(3.6)(4.1)(5.8)(6.1)–(6.10)，含 (6.9b) 前置负号与两处印刷笔误更正（项目核验底座 `blp1995_verified_equations.md`）；GRV（2018）式 (1)–(7)（$\alpha_i(p+\gamma G)$、里程经验分布、$\gamma\rho$ 识别）；Gillingham–Houde–van Benthem（2021）同硬件重标与估值参数；Reynaert–Sallee（2021）感知/真实属性分离；Barwick 等（2026）续航焦虑与充电替代；BKL（2024）、Ji 等（2026）中国汽车 BLP 的对数正态价格系数与补贴结构（卡片层 [O·卡]）。
[D] (M1.2)–(M1.5)、(M1.9)–(M1.13)、(M1.17)–(M1.24)、(M1.25)–(M1.26)、(M1.33)–(M1.39)、(M1.44)、(M1.46)–(M1.47) 为本文从所述假设推导。
[P] 比例信念 (M1.16)、续航缺口规格 (M1.23)、$\xi$ 结构 (M1.41)、工具变量组合、有效边际成本为本项目设定，需数据检验。
