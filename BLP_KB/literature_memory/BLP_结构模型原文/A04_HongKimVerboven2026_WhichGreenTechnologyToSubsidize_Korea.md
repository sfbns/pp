# A04 Which Green Technology to Subsidize? Evidence from Electric Vehicles in South Korea（应补贴哪种绿色技术？来自韩国电动汽车的证据）

## 1. 引用信息
- **英文题目**：Which Green Technology to Subsidize? Evidence from Electric Vehicles in South Korea
- **中译**：应补贴哪种绿色技术？来自韩国电动汽车的证据
- **作者（单位）**：Youngjin Hong（University of Michigan 经济系）；In Kyung Kim（Sogang University 西江大学经济系）；Frank Verboven（KU Leuven 经济系 & CEPR）。脚注说明三位作者贡献相同。
- **版本**：CEPR Discussion Paper DP21757（作者版）；封面日期 **September 2026**；文字层另有 arXiv:2607.14446v2 水印（PDF p1）。JEL：D12, H23, L62, Q58。关键词：electric vehicles; life-cycle GHG emissions; vehicle purchase subsidies; demand estimation; consumer mileage heterogeneity。
- **参考格式**
  - APA：Hong, Y., Kim, I. K., & Verboven, F. (2026). *Which green technology to subsidize? Evidence from electric vehicles in South Korea* (CEPR Discussion Paper No. DP21757). Centre for Economic Policy Research.
  - GB/T 7714：HONG Y, KIM I K, VERBOVEN F. Which green technology to subsidize? Evidence from electric vehicles in South Korea[R]. London: Centre for Economic Policy Research, 2026. CEPR Discussion Paper DP21757.
- **源 txt**：`scratchpad/txt3w/A04_HKV2026.txt`（4017 行；原 PDF `W07_Hong_2026_CEPR_author.pdf`，73 页）。**页码换算：印刷页 = PDF 页 − 1**（PDF p1 为封面/摘要）。下文页码一律写 **PDF 页**。
- **结构**：正文 §1–§7（PDF p2–34）；参考文献 PDF p35–38；附录 A 理论证明（p39–45）、B HEV/PHEV（p46）、C 数据（p47–49）、D 微观矩（p50–53）、E 排放核算（p54–57）、F 里程异质性（p58）、G 附表附图（p59–73）。
- **方法类型标签**：静态 RC logit（BLP）+ 收入除价 + 里程×燃料类型交互 + 微观矩（第二选择相关矩 + 分燃料里程矩）+ 多产品 Bertrand–Nash 供给（只用 FOC 反推 mc）+ 补贴转嫁矩阵（含需求曲率）+ 生命周期（GREET 式）排放核算 + 理论框架（diverted emissions / marginal abatement return）+ 预算中性反事实。

## 2. 一句话结论
“最干净”的技术不一定最值得补贴：在韩国现行电力结构（453 g CO2e/kWh）下，HEV 比 BEV 更能把需求从 ICEV（和高排放的旧车外部品）里拉走，所以把 2020–2023 年的 BEV 购置补贴预算（约 1.56 万亿韩元）**预算中性地改成统一 HEV 补贴，减排从 143.3 万吨增加到 210.4 万吨 CO2e（多 47%）**；电网碳强度要再降约 45%（约到葡萄牙 251 g/kWh）BEV 补贴才赶得上 HEV 补贴。另外，HEV 补贴给厂商和消费者带来的剩余也都更大。

## 3. 研究问题、背景与动机
- **核心问题**：政府在“最干净的前沿技术”（BEV）和“中间技术”（HEV）之间如何分配补贴？只按单车排放排序是否正确？（PDF p2–3）
- **机制**：补贴的减排效果 = 单车排放优势 + **能从高排放技术那里转走多少需求（diversion）**。中间技术更便宜、更符合当前偏好，可能转走更多 ICEV 需求；而 BEV 补贴主要导致 **BEV 内部的替代**，环境效益被削弱。
- **全球背景**（PDF p2）：BEV 普及低于政策目标（价格高、充电与电池安全顾虑、监管不确定；脚注 2：EU 2025 年 3 月允许 2025–2027 三年平均达标；美国最高 $7,500 的 BEV 联邦税抵免已被 One Big Beautiful Bill Act 取消，适用于 2025 年 10 月前登记的车）。HEV 政策支持少却增长更快：美国 2024 年 BEV 份额 7.8%、HEV 10.6%；德、法、意、英、日、韩、印的 HEV–BEV 差距更大；中国例外（BEV 近 30%）（图 G1）。
- **生命周期视角**：BEV 没有尾气排放，但发电碳强度高、电池生产排放高，所以 BEV 对 HEV 的生命周期优势可能被高估。韩国现行电力结构下，BEV 生命周期排放平均**比 ICEV 低 38%、比 HEV 低 15%**（PDF p3）。
- **韩国市场**（§3，PDF p10–14）：
  - 2023 年新乘用车约 149 万辆，户均车辆 1.13。表 1（2023 销量）：汽油 820,710；柴油 104,517；LPG 53,161；Hybrid（HEV+PHEV）390,893；BEV 115,756；HFCV 4,326；合计 1,489,363。其中现代汽车集团（Hyundai/Kia/Genesis）1,103,414，约占 75%。汽油占 55%，混动超过 25%（PHEV 不足 1 万辆），BEV 和柴油各约 7%。
  - HEV 份额从 2015 年 2.7% 升到 2023 年 23.1%（8 倍多）；BEV 2023 年只有 6.5%，比上年低 0.3 个百分点。柴油因 Dieselgate 和 CAFE 下滑（CAFE：2012 年 17 km/L、140 g/km → 2021 年 24.3 km/L、97 g/km，脚注 12）。
  - **政策**：NDC（2015-06）；2021-10 上调后的 NDC 要求交通部门 2030 年减排约 40%。2023 年充电桩预算 3,000 亿韩元（2.6 亿美元）。全文汇率为 1,000 KRW ≈ 0.86 USD。
  - **国家 BEV 补贴公式（2023）**：$[\text{attribute part}+\text{infrastructure part}+\text{innovation part}]\times\text{price multiplier}$。价格 < 5,700 万韩元时乘数为 1，5,700 万–8,500 万为 0.5，> 8,500 万为 0（多为德系车）。2023 年 36 个 BEV 车型中 25 个有补贴、11 个没有（表 G1）。地方补贴随省份和年份变化（这是识别变异的来源之一）。
  - 表 2（PDF p13，2020 不变价）：单车补贴从 2012 年 3,267 万降到 2023 年 706 万韩元；2015 年前补贴覆盖 ≥50% 车价，2022 年起 ≤15%；但 BEV 销量上升，总支出快速增长。全期合计：总补贴 2.54 万亿韩元、240,592 辆、单车 1,056 万、平均购置价 5,575 万、补贴占比 0.21。
  - **HEV 补贴**：2009 年起每辆 100 万韩元（不到车价 3%），2018 年减半，2019 年取消（PHEV 补贴 2021 年结束）。2012–2023 年 HEV 销量加权单车补贴只有 17 万韩元（147 美元），BEV 为 1,056 万（9,100 美元）。**税收抵免**：2012 年起 100 万–400 万韩元，BEV 约为 HEV 的 2–3 倍；HEV 抵免 2020 年起递减、2026 年取消，BEV 抵免至少稳定到 2026 年底。

## 4. 文献综述（方向 → 代表文献 → 本文推进）
1. **EV/HEV 需求激励**（PDF p4 脚注 4–5）
   - 早期 HEV：Chandra et al. 2010；Beresteanu & Li 2011；Gallagher & Muehlegger 2011；Sexton & Sexton 2014；Heutel & Muehlegger 2015；Gulati et al. 2017；Langford & Gillingham 2023（加州，灵活需求框架）。
   - BEV 采用：DeShazo et al. 2017；Clinton & Steinberg 2019；Muehlegger & Rapson 2022；Barwick, Kwon & Li 2024（=A09）。
   - 采用的异质性：Davis et al. 2025；Archsmith et al. 2022；Gillingham et al. 2023；Bushnell et al. 2022。
   - 排放含义：Holland et al. 2016；Xing, Leard & Li 2021（=A16）；Muehlegger & Rapson 2023；Fournel 2024；Allcott et al. 2024（=A17）。
   - 充电网络：Li et al. 2017（=A13）；Zhou & Li 2018；Li 2019；Springel 2021；Fournel 2024。
   - **本文推进**：已有文献都只评估“当时被认为最干净的单一技术”（早期 HEV，后来 BEV）。本文**比较两种技术补贴的相对效果**，并在理论上说明结果取决于单车减排和“从主流高排放技术转走的需求”两项。
2. **BEV 政策的环境效果与排放测量**（脚注 6，PDF p4–5）：Holland et al. 2016；Xing et al. 2021；Muehlegger & Rapson 2023；Guo & Xiao 2023；Meng et al. 2026；Fournel 2024；Allcott et al. 2024；Heid, Remmy & Reynaert 2025。Holland et al. 2016 发现，在美国各州之间，电网碳强度对环境收益差异的解释力远小于本地污染损害。**本文推进**：放到跨国、跨能源转型阶段的范围，碳强度变成关键变量，只有电网足够清洁时 BEV 补贴才优于 HEV 补贴。
3. **清洁/肮脏技术转型与定向技术进步**：Acemoglu et al. 2012, 2016；Papageorgiou et al. 2017（投入替代弹性、生产率差距）。**本文互补**：强调不完全竞争消费品市场里的**需求侧替代**。
4. **方法基础**：Berry 1994；BLP 1995；BLP 2004 与 Petrin 2002（微观矩）；Conlon & Gortmaker 2020（PyBLP）、2025（微观数据）；Grieco, Murry & Yurukoglu 2024（=A03）；Conlon & Mortimer 2021（diversion ratio 的权重）；Springel 2021（网络变量）；Ohashi & Toyama 2017（韩国弹性基准）。
5. **政治经济与产业/贸易政策**（结论部分）：Mani & Mukand 2007（政治家偏好“看得见”的公共品）；Barwick, Collison, Goldberg, Li & Wang 2026（=A18，收入中性的适度进口关税加国内 EV 生产补贴更优）。

## 5. 数据
- **主数据**：ConsumerInsight（韩国汽车营销研究公司），2012–2023 年、17 个省级行政区，按 brand × nameplate × model name × model year × fuel type × 属性组合给出年度登记量和销售收入。**价格 = 销售收入 / 登记量**，用 CPI（2020 = 100）平减。它包含经销商促销和选装件，所以比 MSRP 更接近成交价（PDF p14）。
- **净价**：BEV/HEV 价格减去总补贴（国家 + 地方）。两个假设：(i) 所有买家都申请并拿到了补贴；(ii) 各省年度补贴名额上限不约束（地方政府通常会在年中放宽或追加）。BEV 平均净价约 4,500 万韩元，比 HEV 高 22%、比汽油车高 54%。
- **品牌**：国内 6 个（Hyundai, Kia, KG Mobility, GM Korea, Renault Korea, Genesis），国外 7 个（Mercedes-Benz, BMW, VW, Audi, Toyota, Lexus, Tesla），合计占销量 93%。
- **变量**：每公里燃料成本 = 省-年燃料价格 / 燃料经济性（ICEV 用 km/L，BEV 用 km/kWh；油价来自 OPINET，充电价来自环境部）。马力、整备质量、BEV 续航来自 CARISYOU 和 Danawa。
- **产品 = brand × nameplate × fuel type**（如 Toyota–Camry–HEV）；**市场 = province × year**。样本内属性按登记量加权平均。
- **市场规模**：据 2014 年国家出行调查，换车周期约 6 年，所以取该省样本期平均乘用车保有量的 1/6。**外部品** = 买二手车或继续开现有车（公共交通不算外部品，而是通过里程体现，脚注 22）。
- **样本筛选**：删掉累计销量 < 100 的产品；剔除 PHEV、HFCV；剔除世宗市（缺可靠收入分布）。**最终 34,629 个产品-市场观测，366 个产品（BEV 40 个、HEV 34 个）**，16 省 × 12 年（=192 个市场，[D] 推算）。
- **表 3（销量加权属性，PDF p16）**

| 属性 | Gasoline | Diesel | LPG | HEV | BEV | All |
|---|---:|---:|---:|---:|---:|---:|
| 价格（百万 KRW） | 29.37 | 35.87 | 25.48 | 37.27 | 55.71 | 32.33 |
| 净价 | 29.37 | 35.87 | 25.48 | 37.10 | 45.14 | 32.11 |
| 每公里燃料成本（千 KRW/km） | 0.14 | 0.11 | 0.15 | 0.09 | 0.05 | 0.12 |
| 燃料经济性（km/L；BEV 为 km/kWh） | 12.53 | 13.27 | 9.28 | 16.84 | 5.16 | – |
| Size（m³） | 12.29 | 14.96 | 13.18 | 13.68 | 13.21 | 13.27 |
| Power（hp） | 168.14 | 180.73 | 152.50 | 218.47 | 233.57 | 176.61 |
| Weight（kg） | 1,371 | 1,775 | 1,474 | 1,629 | 1,824 | 1,528 |
| Accel（hp/kg） | 0.12 | 0.10 | 0.10 | 0.13 | 0.13 | 0.11 |
| 燃料周期排放（g CO2e/km） | 199.87 | 212.88 | 204.45 | 134.85 | 89.21 | 196.60 |
| 车辆周期排放（t CO2e，2020–23 售出） | 6.99 | 7.70 | 7.11 | 7.16 | 10.61 | 7.29 |
| 观测数 | 15,551 | 11,854 | 2,096 | 3,147 | 1,981 | 34,629 |

  - HEV 购置价比 BEV 低 33%，净价低 17.8%；HEV 的 16.8 km/L 在 ICEV 类中最高。BEV 的车辆周期排放比 HEV/ICEV 高 37.7%–51.7%（电池）。
  - 按持有 6 年、每年 12,000 km 计，HEV 约 17 t，与 BEV 相当；按 15 年（韩国平均车龄）计，BEV 26.7 t、HEV 31.4 t，只差 15%（PDF p16）。
- **补充数据**（PDF p15–17）
  - **排放**：每个产品-年的燃料周期排放；2020–2023 年售出产品的车辆周期排放（附录 E.1，见 §6.3）。
  - **BEV 补贴**：2020 年起有年-省-车型级数据（Zero-Emission Vehicle Integrated Portal）。县级差异用人口最多或 BEV 登记最多的县代替；2020 年以前用环境部文件和新闻。图 G4/G5 显示车型间、省份间差异很大。
  - **第二选择调查**：ConsumerInsight 2018 年和 2023 年调查（受访者近两年购买新车），剔除首选不在销售数据或没报第二选择的样本后，分别保留 **4,035 人和 4,145 人**。调查过度抽样 BEV 等小份额车型、少抽汽油和柴油车，用数据商提供的**逆抽样权重**纠正。
  - **里程**：韩国交通安全公团（KTSA）年检记录（新车 4 年后首检，之后每 2 年一次；货车等每年一次），字段包括检验年份、年里程、燃料类型、登记省份；用于矩的样本量 **69,707,543**（表 D1）。HEV 里程最高；BEV 里程在样本期快速上升；2021 年各类车里程都偏高（疫情）；大都市里程较低（表 G2，例如首尔平均 29.7 km/日、世宗 36.9）。
  - **收入**：KLIPS 家庭收入，按市场拟合对数正态分布，每个市场模拟 1,000 人。**充电桩**：韩国环境公团数据（2020–2023 年末存量；2020 年以前按安装年份回推）；网络变量 = ln(充电桩数) × BEV 虚拟变量（仿 Springel 2021）。
  - **各国电网排放因子**：Our World in Data 2022 年数据，用 World Bank 输配损耗调整（附录 C，表 C1 共 148 国；韩国 453 g/kWh、损耗 3.20%）。

## 6. 结构模型如何构建
### 6.1 需求侧（§5.1，PDF p18–19；据文字层重建）
- **间接效用**（式 6）：
$$u_{ijm}=x_{jm}\beta_i-\alpha_i p_{jm}+\xi_{jm}+\varepsilon_{ijm}$$
  - $p_{jm}$ 是**扣除补贴后的净价**（补贴通过净价进入效用）。
  - $x_{jm}$ 包括每公里成本（cost per km）、加速度（hp/kg）、尺寸、充电网络变量、上市/退市年份指示变量，以及**车型（nameplate）FE、省份 FE、燃料类型 × 年份 FE**。后者吸收随时间变化的燃料类型冲击，如 Dieselgate，以及 HEV/BEV 的非补贴优惠（停车费减免、专用车位）。
  - $\varepsilon_{ijm}$ 服从 i.i.d. 第一类极值分布。
- **异质性**（式 7）：
$$\alpha_i=\frac{\alpha}{y_i},\qquad \beta_{ik}=\beta_k+\pi_k\,\text{mileage}_i+\sigma_k v_{ik}$$
  - $y_i$ 为年收入，$\text{mileage}_i$ 为**日里程**，$v_{ik}\sim N(0,1)$。
  - $\pi_k\neq0$ 只用于 4 个燃料虚拟变量（diesel, gasoline, BEV, HEV；LPG 没有交互项），表示这四类燃料**相对外部品**的偏好随里程变化。
  - $\sigma_k\neq0$ 用于 4 个燃料虚拟变量、SUV 指示变量和每公里成本。
  - 非线性参数 $\theta=(\alpha,\{\pi_k\},\{\sigma_k\})$，共 1 + 4 + 6 = 11 个。
- **分解**（式 8）：
$$u_{ij}=\delta_j+\mu_{ij}+\varepsilon_{ij},\quad \delta_j=x_j\beta+\xi_j,\quad \mu_{ij}=-\frac{\alpha p_j}{y_i}+\sum_k(\pi_k\,\text{mileage}_i+\sigma_k v_{ik})x^{(2)}_{jk}$$
  - 价格只出现在 $\mu_{ij}$ 中（没有均值价格系数），所以 $\alpha$ 是非线性参数。
  - 燃料类型的均值偏好被燃料类型 × 年份 FE 吸收，所以表 4 中燃料类型这几行没有均值系数。
- **份额**（式 9）：外部品 $\delta_0=0$；$D=(\text{income},\text{mileage})$；假设 $D, v, \varepsilon$ 相互独立，且收入与里程独立（二者来自不同数据源）。
$$s_{ij}=\frac{\exp(\delta_j+\mu_{ij})}{1+\sum_{\ell\in\mathcal J}\exp(\delta_\ell+\mu_{i\ell})},\qquad s_j=\int_D\int_v s_{ij}\,dF(v)\,dF(D)$$
  - $F(v)$ 为正态分布，$F(D)$ 为经验分布。
- **基准模型**：logit 为 $\ln(s_{jm}/s_{0m})=x_{jm}\beta-\alpha p_{jm}/\bar y_m+\xi_{jm}$；嵌套 logit 再加 $\rho\ln s_{j|g}$，按 6 组分巢（gasoline, diesel, LPG, HEV, BEV, outside）（表 G3 注，PDF p61）。
- **燃料成本与排放如何进入**：每公里燃料成本作为属性进入效用（有随机系数 $\sigma$，但**没有与里程交互**）；里程通过燃料类型偏好进入效用。排放不进入效用，只在反事实中用于核算（见 6.3）。
- **嵌套/随机系数**：没有显式分巢，用燃料类型虚拟变量的随机系数（$\sigma_k$）近似“同燃料类型更接近替代品”（与 GV2014 的思路一致）。

### 6.2 供给侧（§6.1，PDF p23–24；附录 A.5，PDF p44–45）
- **利润**：$\Pi_f=\sum_{j\in\mathcal J_f}(p^G_j-mc_j)\,s_j(p)\,M$。其中 $p^G_j$ 为厂商定的毛价，消费者净价 $p_j=p^G_j-\tau_j$。
- **FOC**（式 13）：
$$p^G=mc-\big(\Omega\circ\nabla_p s(p)\big)^{-1}s(p),\qquad p^G=p+\tau$$
  - $\Omega$ 为（块对角）所有权矩阵，$\nabla_p s$ 为 $J\times J$ 份额对价格的导数矩阵。按 FOC 结构，其 $(j,k)$ 元应为 $\partial s_k/\partial p_j$（据文字层与 (31) 中转置推断）。
- **厂商**：按母公司定义。国内 4 家（Hyundai Motor Group, KG Mobility, GM Korea, Renault Korea），国外 5 家（Mercedes-Benz Group, BMW, VW Group, Toyota Group, Tesla）（脚注 26）。
- **成本**：边际成本为常数，在观测价格处由 (13) 反推。**没有估计成本函数，也没有供给侧矩**（GMM 只用需求矩和微观矩）。
- **补贴转嫁矩阵**（附录 A.5，据文字层重建，把握中高）：
  - 设 $B_{jg}=\mathbf 1\{j\in\mathcal J_g\}$，则 $p=p^G-B\tau$。
  - 记 $F(p,\tau)\equiv s(p)+\nabla(p)(p+B\tau-mc)=0$，其中 $\nabla(p)=\Omega\circ\nabla_p s(p)$。
  - 由隐函数定理：
$$\Theta\equiv-\frac{\partial p}{\partial\tau'}=\Big(\frac{\partial F}{\partial p'}\Big)^{-1}\frac{\partial F}{\partial\tau'},\quad \frac{\partial F}{\partial\tau'}=\nabla(p)B$$
$$\Big(\frac{\partial F}{\partial p'}\Big)_{jk}=\frac{\partial s_j}{\partial p_k}+\nabla(p)_{jk}+\sum_l\Omega_{jl}\frac{\partial^2 s_l}{\partial p_k\partial p_j}(p_l+(B\tau)_l-mc_l)$$
$$\Theta=\big[\nabla_p s(p)'+\nabla(p)+K(p,\tau)\big]^{-1}\nabla(p)B,\quad K_{jk}=\sum_l(p_l+(B\tau)_l-mc_l)\Omega_{jl}\frac{\partial^2 s_l}{\partial p_k\partial p_j}$$
  - 三项分别对应需求斜率、斜率 × 所有权、需求曲率。$\Theta_{j,g}$ 定义在**消费者净价**上：$\Theta=1$ 表示完全转嫁，$>1$ 表示过度转嫁（厂商还压低了毛价）。

### 6.3 均衡、排放与福利模块
- **均衡**：反事实下用 root solver 或定点算法解 (13)，得到价格、份额、销量和排放（PDF p24）。
- **个体期望排放**（式 14，PDF p24，据文字层重建，把握高）：
$$E^\tau_i=\sum_{j\in\mathcal J}\underbrace{\big(T\cdot m_i\cdot e^{FC}_j+e^{VC}_j\big)}_{e_{ij}}s^\tau_{ij}+e_{i0}\,s^\tau_{i0},\qquad e_{i0}=T^O\cdot m_i\cdot e^{FC}_0$$
  - $m_i$ 为年行驶里程（km），$T$ 为预期使用年限，$e^{FC}_j$ 为燃料周期排放（g/km），$e^{VC}_j$ 为车辆周期排放（生产、报废、回收）。
  - **外部品**：$e^{FC}_0$ 取本省“前 8 年、剔除最近 3 年”售出车辆的销量加权燃料周期排放（假设消费者不会在头三年换车；窗口具体是几年，原文表述有歧义，待核）；$e^{VC}_0=0$。
  - 基准设定 $T=T^O=15$ 年（韩国乘用车平均寿命，与 Allcott et al. 2024 一致）。
- **市场排放**（式 15、34）：$E^\tau_m=M_m\iint E^\tau_i\,dF(v)dF(D)\approx M_m\frac1N\sum_i E^\tau_i$。
- **分解**（式 35，附录 E.2）：
$$\Delta E_m=\Delta E_{m,FC}+\Delta E_{m,VC}+\Delta E_{m,outside}$$
$$\Delta E_{m,FC}=\frac{M_m}{N}\sum_i\sum_j T m_i e^{FC}_j\Delta\hat s_{ij},\quad \Delta E_{m,VC}=\frac{M_m}{N}\sum_i\sum_j e^{VC}_j\Delta\hat s_{ij},\quad \Delta E_{m,outside}=\frac{M_m}{N}\sum_i T^O m_i e^{FC}_0\Delta\hat s_{i0}$$
  - $\Delta E_{m,FC}$ 还可以按 ICEV/BEV/HEV 拆分。
- **排放测量**（附录 E.1，PDF p54–55）
  - **车辆周期**：用 Kelly et al. (2023) GREET 的美国轿车/SUV 分燃料类型估计。理由是两国化石能源发电占比相近（美国 2020 年 59.6%，韩国 2023 年 58.2%；表 E1：天然气 36.8/26.8、煤 22.8/31.4、核 20.3/30.7、可再生 19.4/8.4、其他 0.7/2.6）。BEV 按 200/300/400 英里续航线性插值：400 英里 BEV 的生产排放近 ICEV 两倍，200 英里 BEV 高 25%–32%。
  - **ICEV/HEV 燃料周期**：取车型-年官方尾气 CO2 的中位数，依次 ×1.14（ICCT：欧洲 2022 年实测比官方高约 14%）、×1.05（CO2 → CO2e）、÷0.86（tank-to-wheels 约占燃料周期 86%，Choi et al. 2020 给出 85.6%–86.7%）。例：2020 Camry HEV，93.5 × 1.14 × 1.05 = 111.92，÷ 0.86 = 130.14 g/km。
  - **BEV**：$e^{FC}_j=\text{emission factor (g CO}_2\text{e/kWh)}/\text{fuel economy}_j\text{ (km/kWh)}$，韩国 2022 年为 453。
  - 共 2,304 个产品-年组合；2012–2019 年有 61 个组合缺 CO2 数据，计算外部品排放时剔除。
  - 国际排放因子按损耗调整：$\text{factor}=\text{unadjusted}\times\frac{100}{100-\text{grid loss}(\%)}$。
- **福利**：只报告生产者剩余（按厂商）和消费者剩余（按收入五分位）的变化（表 9）。**没有**社会碳成本加总，也没有完整的社会福利函数。

### 6.4 识别
- **价格内生性**（PDF p20）：除非价格属性外，用两个成本移动工具变量，都**滞后一年**（成本冲击传导需要时间）：
  1. **进口关税率**：韩欧 FTA 使德系车关税在 2010–2016 年逐步下降，并因燃料类型和排量而异；日系 HEV 关税在 2020 年代初略降。
  2. **原材料价格 × 车重**：$(0.2\times\text{aluminum price}+\text{iron ore price})\times\text{weight}$（行业报告称造车用铁约为铝的 5 倍）。
- **第一阶段**（表 G4，PDF p62）：IV logit 中关税 0.037 (0.005)，原材料 × 重量 0.135 (0.127，单独不显著)；SW F = 26.29，R² = 0.955。嵌套 logit 中价格方程 SW F = 16.40；$\ln s_{j|g}$ 方程 SW F = 22.01，组内产品数 −0.006 (0.002)。嵌套参数的工具变量为“组内产品数”。
- **补贴变化作为变异来源**：净价包含补贴，国家补贴随属性和价格上限变化，地方补贴随省-年变化（图 G4/G5）。但文中**没有把补贴单独列为工具变量**，补贴提供的是净价的外生变异（这是我的解读，原文没有展开）。
- **$\{\pi_k\},\{\sigma_k\}$ 的识别靠微观矩**（附录 D）：
  - 第二选择调查：首选与次选属性的相关系数（BEV、HEV、diesel、gasoline、SUV 虚拟变量和每公里成本，分 2017–18 与 2022–23 两期，共 12 个矩）主要识别 $\sigma_k$。
  - KTSA 里程：各燃料类型平均日里程相对 LPG 的百分比差（BEV、HEV、diesel、gasoline，4 个矩）主要识别 $\pi_k$。这是 4 个矩对 4 个参数，表 D1 中拟合几乎完全精确。
- **正规化**：外部品 $\delta_0=0$；LPG 没有里程交互，作为里程矩的参照；价格系数按收入缩放。

### 6.5 估计算法与实现
- BLP 收缩映射反解 $\delta(\theta)$；每个市场 N = 1,000（收入 1,000 次抽样 × 里程 1,000 次抽样 × 1,000 个 scrambled Halton 抽样，逐个配对）。
- $\xi_j(\theta)=\delta_j(\theta)-x_j\hat\beta(\theta)$，$\hat\beta(\theta)$ 由线性 GMM 集中掉。
- 总体矩（式 10）：$G_1(\theta)=\frac{1}{N_p}\sum_{j,m}\xi_{jm}(\theta)Z_{jm}$。
- GMM（式 11–12）：$\hat\theta=\arg\min G(\theta)'WG(\theta)$，$G=[G_1;G_2]$，$W=\mathrm{diag}(W_1,W_2)$。
- 用 **PyBLP**（Conlon & Gortmaker 2020）实现；标准误按市场聚类。
- **观测端的微观统计量**（式 33）：
$$\frac{\sum_i w_i(x_{ij}-\bar x_j)(x_{ik}-\bar x_k)}{\sqrt{\sum_i w_i(x_{ij}-\bar x_j)^2}\sqrt{\sum_i w_i(x_{ik}-\bar x_k)^2}}$$
  - $w_i$ 为逆抽样权重；条件是首选和次选都是内部品。
- **模型端**：沿用 Conlon–Gortmaker 的 micro part 写法：
$$v_p(\theta)=\frac{\sum_{t}\sum_i\sum_j\sum_{k\neq j}w_{it}\,s_{ijkt}(\theta)\,w^d_{pijkt}\,v_{pijkt}}{\sum_t\sum_i\sum_j\sum_{k\neq j}w_{it}\,s_{ijkt}(\theta)\,w^d_{pijkt}}$$
  - $w_{it}=1/1000$，$w^d=\mathbf 1\{j,k\neq0\}$。
  - $v_1=x_jx_k$，$v_2=x_j$，$v_3=x_k$，$v_4=x_j^2$，$v_5=x_k^2$；相关系数 $f=(v_1-v_2v_3)/\big(\sqrt{v_4-v_2^2}\sqrt{v_5-v_3^2}\big)$。
- **里程矩**：$f=\big(\frac{v_1v_4}{v_2v_3}-1\big)\times100$，按文意等于 $\frac{E[m|BEV]-E[m|LPG]}{E[m|LPG]}\times100$。原文对 $v_1$–$v_4$ 的权重定义与此式组合起来不完全自洽，**待核**。
- **样本权重问题**（脚注 35）：理想做法是对每个 (i, j, k) 组合给不同的调查权重；实际拿不到，所以只在观测端用逆抽样权重纠偏，以缓解宏观数据与微观数据不相容（Conlon & Gortmaker 2025）。

### 6.6 理论框架、反事实与福利计算
- **基本设定**（§2.1，PDF p5–7）：三个产品 $j\in\{I,H,B\}$，市场规模 M，单位排放 $e_j$，且 $e_j<e_I$。能源转型早期可能 $e_H<e_B$，后期 $e_B<e_H$。
  - $E(\tau)=M\sum_k e_ks_k(p(\tau))$，$G(\tau)=M\sum_k\tau_ks_k(p(\tau))$；假设完全转嫁。
  - diversion ratio：$D_{j\to k}\equiv-\frac{\partial s_k/\partial p_j}{\partial s_j/\partial p_j}$。
  - **diverted emissions**：$e^D_j\equiv\sum_{k\neq j}D_{j\to k}e_k$，即边际消费者没有补贴时会产生的期望排放。
  - 式 (1)：$\frac{\partial E}{\partial\tau_j}=-M\sum_k e_k\frac{\partial s_k}{\partial p_j}=M(e^D_j-e_j)\frac{\partial s_j}{\partial p_j}$，所以当 $e^D_j-e_j>0$ 时补贴能减排。
- **命题 1**（式 2）：在零补贴基线下，“补贴 j、对 k 征税”能减排，当且仅当
$$-\frac{1}{s_j}\frac{\partial s_j}{\partial p_j}(e^D_j-e_j)>-\frac{1}{s_k}\frac{\partial s_k}{\partial p_k}(e^D_k-e_k)$$
  - 即“价格半弹性 × 净转移排放”更大的一方胜出。
  - 对称 logit 下，条件退化为 $e_j<e_k$，只比单车排放。
  - 若两者半弹性相同，条件为 $e_H-e_B<e^D_H-e^D_B$。
  - 附录 A.2，式 (22)：$e^D_H-e_H>e^D_B-e_B\iff\frac{2-D_{H\to I}}{2-D_{B\to I}}<\frac{e_I-e_H}{e_I-e_B}$。当 $e_H=e_B$ 时，只要 $D_{H\to I}>D_{B\to I}$，HEV 补贴就更有效。（推导用了 $\sum_{k\ne j}D_{j\to k}=1$，即三产品设定里没有外部品；已自行验算无误。）
- **预算中性一般条件**（附录 A.1）
  - $\partial G/\partial\tau_j=M\big[s_j-\sum_\ell\tau_\ell\,\partial s_\ell/\partial p_j\big]$，假设为正（式 16）。
  - 由隐函数 $d\tau_k/d\tau_j=-\frac{\partial G/\partial\tau_j}{\partial G/\partial\tau_k}$，$dE<0$ 当且仅当**边际减排回报（marginal abatement return, MAR）** 更高：
$$\frac{-\partial E/\partial\tau_j}{\partial G/\partial\tau_j}>\frac{-\partial E/\partial\tau_k}{\partial G/\partial\tau_k}\quad(20)$$
  - 有既有补贴时为式 (21)：分母变成 $s_j-\tau_j\partial s_j/\partial p_j-\tau_k\partial s_k/\partial p_j$。
- **命题 2**（§2.2，式 3–5，PDF p8；证明见 A.3）：推广到多产品、多燃料组、不完全竞争转嫁和异质里程。
  - $\mathcal J_g$ 为燃料组 g 的产品集，$S_g=\sum_{j\in\mathcal J_g}s_j$，$\Theta_{j,g}=-\partial p_j/\partial\tau_g$。
  - 个体层：$D_{ij\to k}=-\frac{\partial s_{ik}/\partial p_j}{\partial s_{ij}/\partial p_j}$，$e^D_{ij}=\sum_{k\ne j}D_{ij\to k}e_{ik}$。
  - 产品层：$e_j=\int\omega_{ij}e_{ij}dF(i)$，$e^D_j=\int\omega_{ij}e^D_{ij}dF(i)$，权重 $\omega_{ij}=\frac{\partial s_{ij}/\partial p_j}{\partial s_j/\partial p_j}$（价格敏感的消费者权重更大，类似 Conlon–Mortimer 2021 的 diversion 权重）。
  - 条件：
$$-\frac{1}{S_{g_1}}\sum_{g=1}^G\sum_{j\in\mathcal J_g}\Theta_{j,g_1}\frac{\partial s_j}{\partial p_j}(e^D_j-e_j)>-\frac{1}{S_{g_2}}\sum_{g=1}^G\sum_{j\in\mathcal J_g}\Theta_{j,g_2}\frac{\partial s_j}{\partial p_j}(e^D_j-e_j)$$
  - 若组内转嫁为 1、跨组转嫁为 0，条件只剩本组求和（脚注 9）。
  - 若高里程者减排空间更大，且价格更敏感，则加总的净转移排放会大于同质里程模型的预测（脚注 10）。
  - 含既有补贴的一般式为 (26)，分母为 $S_g+\tau_g\partial S_g/\partial\tau_g+\sum_{r\ne g}\tau_r\partial S_r/\partial\tau_g$（式 25）。
- **总效应**（附录 A.4，式 27–28）：
$$\Delta E_g(\bar G)=\int_0^{\bar G}\Big[\frac{-\partial E/\partial\tau_g}{\partial G/\partial\tau_g}\Big]_{\tau=\tau^g(G)}dG\equiv\int_0^{\bar G}MAR_g(G)\,dG$$
  - 比较两种政策，就是比较两条 MAR 曲线下的面积。命题 1/2 只比较截距（图 A1）。
- **反事实设计**（§6.1–6.2）：时期 2020–2023（HEV 补贴 2019 年已取消，期间只补贴 BEV）。
  - 情景 (i)：无补贴；情景 (ii)：把 BEV **直接购置补贴**的总预算改为**统一的 HEV 单车补贴**，校准到四年总支出约等于 BEV 预算。不含基础设施和税收抵免。
  - 分别比较 无补贴 → 现行 BEV 补贴，与 无补贴 → HEV 补贴。
  - 作者认为现行 BEV 补贴已含一定优化（按属性设计），所以估计的 HEV 相对优势是**下界**。
- **边际减排回报的实证版**：先在无补贴反事实价格处按 A.5 计算转嫁矩阵，再逐市场计算 MAR，按市场规模加权平均。2020–2023 年共 64 个市场，剔除 2 个（2021 忠南、2022 光州，矩阵病态不可逆），用 62 个。MAR 的倒数为边际减排成本 MAC。
- **电力碳强度反事实**（§6.3）：只把 BEV 的 $e^{FC}_j$ 换成其他 18 国（加世界平均）的排放因子；其他燃料的排放和车辆周期排放保持不变。

## 7. 估计结果
- **表 4（PDF p22；括号内为按市场聚类的稳健标准误）**

| 变量 | OLS logit | IV logit | RC1 α,β | RC1 σ | RC2 α,β | RC2 π | RC2 σ |
|---|---|---|---|---|---|---|---|
| Price/income | −0.406 (0.062) | −6.013 (0.739) | −12.864 (2.299) | | −14.569 (2.323) | | |
| Cost per km | −2.522 (0.090) | −0.668 (0.227) | −3.162 (0.388) | 1.557 (0.331) | −3.041 (0.357) | | 1.453 (0.341) |
| Acceleration | −0.271 (0.461) | 18.033 (2.659) | 10.636 (1.507) | | 11.460 (1.488) | | |
| Size | 0.324 (0.048) | 0.859 (0.134) | 1.082 (0.115) | | 1.147 (0.118) | | |
| Network | 0.032 (0.069) | 0.248 (0.069) | 0.362 (0.178) | | 0.213 (0.171) | | |
| Entry year | −0.623 (0.032) | −0.457 (0.041) | −0.367 (0.051) | | −0.345 (0.052) | | |
| Exit year | −1.707 (0.034) | −1.720 (0.041) | −1.975 (0.059) | | −2.043 (0.061) | | |
| BEV | | | | 4.992 (0.379) | | **7.423** (0.450) | 5.025 (0.376) |
| HEV | | | | 1.811 (0.114) | | **2.681** (0.108) | 1.778 (0.118) |
| Diesel | | | | 1.663 (0.125) | | **2.495** (0.128) | 1.722 (0.121) |
| Gasoline | | | | 1.830 (0.082) | | **−3.513** (0.118) | 1.568 (0.087) |
| SUV | | | | 3.514 (0.105) | | | 3.521 (0.105) |
| 自价格弹性中位数 | −0.371 | −5.490 | −5.588 | | −6.125 | | |
| 自价格弹性加权均值 | −0.291 | −4.302 | −5.377 | | −5.906 | | |

  - 列归属按文字层字符位置和正文描述重建，把握高：RC1 燃料行的数值是 $\sigma$；RC2 燃料行第一列是 $\pi$，第二列是 $\sigma$。
  - 解读：IV 使价格系数绝对值变大（符合预期）。所有 $\sigma$ 都显著，说明同燃料类型的车替代性更强。$\pi$ 表明里程越高，越看重 BEV、HEV、柴油车，越不看重汽油车。
  - 加入 $\pi$ 后，$\alpha,\beta,\sigma$ 基本不变。
  - 平均自价格弹性：RC1 −5.38，RC2 −5.91；对照 Ohashi & Toyama 2017（韩国 1996–2009）−5.32，GMY 2024（美国 1980–2018）−5.06。
- **嵌套 logit**（表 G3，PDF p61）：$\rho=0.677$ (0.063)，price/avg income −2.076 (0.411)，cost per km −0.145 (0.088)，acceleration 6.229，size 0.296，network 0.202，entry −0.148，exit −0.565；弹性中位数 −5.755，加权均值 −4.370。
- **分燃料自价格弹性**（表 G5A，加权均值）：BEV −6.18（P10–P90：−9.05 至 −4.49）、HEV −5.94、柴油 −6.40、汽油 −5.61、LPG −5.94，差别不明显。
- **交叉价格弹性**（表 G5B，未加权均值；行 = 产品燃料类型，列 = 被涨价的燃料类型）：

| 行\列 | BEV | HEV | Diesel | Gasoline | LPG |
|---|---:|---:|---:|---:|---:|
| BEV | 0.0374 | 0.0030 | 0.0012 | 0.0012 | 0.0018 |
| HEV | 0.0012 | 0.0273 | 0.0034 | 0.0026 | 0.0063 |
| Diesel | 0.0008 | 0.0041 | 0.0086 | 0.0019 | 0.0040 |
| Gasoline | 0.0006 | 0.0030 | 0.0021 | 0.0055 | 0.0040 |
| LPG | 0.0010 | 0.0064 | 0.0032 | 0.0032 | 0.0243 |

  - HEV 对汽油车价格的交叉弹性（0.0026）高于对 BEV 价格的交叉弹性（0.0012）。
- **表 5 燃料类型间 diversion ratio，2023 年**（PDF p23；行 → 列，先按燃料内销量加权，再对 16 个市场平均）：

| 从\到 | BEV | HEV | Diesel | Gasoline | LPG | Outside |
|---|---:|---:|---:|---:|---:|---:|
| BEV | 0.574 | 0.101 | 0.038 | 0.168 | 0.009 | 0.110 |
| HEV | 0.029 | 0.432 | 0.061 | 0.288 | 0.020 | 0.171 |
| Diesel | 0.034 | 0.194 | 0.290 | 0.340 | 0.026 | 0.116 |
| Gasoline | 0.017 | 0.098 | 0.038 | 0.639 | 0.015 | 0.193 |
| LPG | 0.023 | 0.178 | 0.078 | 0.442 | 0.043 | 0.236 |

  - HEV 涨价后，汽油车拿走 28.8% 的流失销量，BEV 只拿走 2.9%；汽油车涨价后，HEV 拿走 9.8%，BEV 只有 1.7%。
  - [D] 转向 ICEV（柴油 + 汽油 + LPG）的合计：从 HEV 出发 0.369，从 BEV 出发 0.215；转向外部品：HEV 0.171，BEV 0.110。
  - 这一格局在整个样本期都成立（图 G6，2018–2023）。
- **里程异质性**（PDF p23，图 G7）：低每公里成本车型（HEV、BEV、柴油）的份额随里程上升。2023 年 BEV 份额从日里程 20–40 km 组的 2.22% 翻倍到 60–80 km 组的 4.44%；汽油车份额随里程急剧下降。
- **微观矩拟合**（表 D1，PDF p53；观测 / 模拟）：
  - 每公里成本相关：0.551 / 0.472（2022–23），0.519 / 0.364（2017–18）。
  - BEV 相关：0.662 / 0.650，0.707 / 0.638。HEV：0.380 / 0.410，0.301 / 0.247。Diesel：0.382 / 0.330，0.568 / 0.519。Gasoline：0.453 / 0.474，0.558 / 0.509。SUV：0.540 / 0.590，0.655 / 0.618。
  - 里程相对 LPG 的百分比差：BEV +13.38、HEV +9.37、Diesel +6.00、Gasoline −19.69，模型几乎完全复现。

## 8. 反事实与政策结果
- **表 6 边际减排回报（零补贴基线，t CO2e / 百万 KRW，62 个市场按市场规模加权，PDF p26）**

| | BEV | HEV | Gasoline | Diesel | LPG |
|---|---:|---:|---:|---:|---:|
| Marginal abatement return | 1.402 | **1.671** | −0.355 | −1.006 | −0.939 |
| Own abatement return | 1.395 | 1.553 | −0.338 | −1.045 | −0.970 |
| Cross abatement return | 0.007 | 0.118 | −0.017 | 0.039 | 0.031 |

  - HEV 的 MAR 比 BEV 高约 20%。对应 MAC：BEV 0.713、HEV 0.598 百万韩元/吨（脚注 28）；[D] 约合 613 和 515 美元/吨。
  - 汽油、柴油、LPG 的 MAR 为负，说明应对它们征税，柴油和 LPG 尤甚。
  - 跨组回报很小，因为跨燃料类型的转嫁率低。市场层面分布见图 G8。
- **表 7 预算中性比较（2020–2023 累计，PDF p28）**

| | BEV 补贴 | HEV 补贴 |
|---|---:|---:|
| 单车补贴（百万 KRW，销量加权） | 8.646 | 1.943 |
| 总支出（万亿 KRW） | 1.563 | 1.565 |
| ΔBEV 销量 | +77,655 | −3,206 |
| ΔHEV | −15,026 | +177,697 |
| ΔGasoline | −28,244 | −92,213 |
| ΔDiesel | −13,793 | −31,708 |
| ΔLPG | −2,114 | −8,666 |
| ΔOutside | −18,478 | −41,903 |
| **总排放变化（千吨 CO2e）** | **−1,433** | **−2,104** |
| 燃料周期 | −942 | −572 |
| 　其中 ICEV | −1,930 | −5,208 |
| 　其中 BEV | +1,473 | −69 |
| 　其中 HEV | −485 | +4,705 |
| 车辆周期 | +381 | +289 |
| 外部品 | −871 | −1,821 |

  - HEV 补贴额小得多（HEV 销量大），但 HEV 销量增加约 17.8 万辆，BEV 补贴只让 BEV 增加约 7.8 万辆。
  - HEV 补贴使汽油车减少 9.2 万辆（BEV 补贴只减少 2.8 万），从外部品（旧 ICEV，排放最高）转走的也更多。
  - 总减排 2.10 Mt 对 1.43 Mt，**多 47%**（2,104/1,433 = 1.468）。
  - BEV 补贴的燃料周期减排更大（942 对 572），但车辆周期增排更多，外部品减排少得多（871 对 1,821）。
  - 燃料周期的数字是净值：HEV 补贴让 ICEV 燃料周期排放减少 5.2 Mt（约为外部品减排的 3 倍），同时新 HEV 增加 4.7 Mt。BEV 补贴只让 ICEV 减少 1.9 Mt。
  - **转嫁**（表 G6，2023）：HEV 补贴在所有车型上转嫁率都 > 1（1.07–1.38，例如 Elantra 1.38、Sonata 1.27、K5 1.30），厂商同时压低毛价。BEV 补贴的转嫁率在 0.71–1.15 之间：Genesis G80 0.71、GV70 0.75、GV60 0.76、Ioniq 5 N 0.77、EV9 0.80 偏低（毛价反而上涨）；Model Y 1.15。不合格的高价 BEV 毛价也小幅上涨。
  - [D] 由 Elantra、Sonata、Grandeur 反推，2023 年的 HEV 单车补贴约 1.63 百万 KRW，低于四年平均 1.943，说明“统一补贴”可能逐年校准，待核。
  - [D] 平均财政成本：BEV 约 1.09、HEV 约 0.74 百万韩元/吨（约 938 和 640 美元/吨）。这只是支出除以减排量，不是社会成本。
- **表 8 敏感性（千吨 CO2e，BEV 补贴 / HEV 补贴，PDF p29）**

| 情景 | BEV 补贴 | HEV 补贴 |
|---|---:|---:|
| 基准（RC2, 15 & 15 年，母公司所有权） | −1,433 | −2,104 |
| IV logit | −1,203 | **−1,105** |
| RC logit 1（同质里程） | −1,025 | −1,624 |
| 新车 15 年，外部品 9 年 | −1,084 | −1,376 |
| 新车与外部品都按 6 年 | −344 | −668 |
| 品牌级所有权 | −1,458 | −1,942 |
| 产品级所有权 | −1,453 | −1,877 |

  - **只有 IV logit 下 BEV 补贴略优**，正好对应理论中“对称 logit 只比单车排放”的结论。说明灵活的替代模式是本文结论的关键。
  - RC1 低估两种政策的减排，原因见附录 F：补贴主要吸引高里程消费者，HEV 补贴下日里程 40–60 km 组的 HEV 份额上升 2.1 个百分点，比 0–20 km 组（1.2 个百分点）高 76%，而同质里程模型捕捉不到这种构成变化。
  - 使用年限：15/9 年时 HEV 1.4 Mt 对 BEV 1.1 Mt；6/6 年时 668 对 344，按百分比 HEV 的优势更大。
  - 所有权结构几乎不影响结论：Toyota（HEV）、Tesla（BEV）的竞争约束限制了现代集团压低转嫁的动机。
- **电网碳强度**（§6.3，图 3、表 G7，PDF p31–32、p65；千吨 CO2e，BEV / HEV，括号内为 g/kWh）：

| 国家（g/kWh） | BEV 补贴 | HEV 补贴 |
|---|---:|---:|
| Norway（31） | 2,805 | 2,040 |
| France（85） | 2,629 | 2,048 |
| Brazil（122） | 2,509 | 2,054 |
| Denmark（213） | 2,213 | 2,068 |
| **Portugal（251）** | 2,089 | 2,073 |
| UK（274） | 2,015 | 2,077 |
| Peru（324） | 1,852 | 2,084 |
| Netherlands（339） | 1,803 | 2,087 |
| USA（430） | 1,507 | 2,101 |
| Germany（440） | 1,475 | 2,102 |
| **Korea（453）** | 1,433 | 2,104 |
| World（526） | 1,195 | 2,115 |
| Japan（542） | 1,143 | 2,118 |
| China（607） | 932 | 2,127 |
| Malaysia（649） | 795 | 2,134 |
| Philippines（667） | 737 | 2,137 |
| Indonesia（725） | 548 | 2,145 |
| Poland（778） | 376 | 2,153 |
| India（826） | 220 | 2,161 |
| **Kazakhstan（907）** | **−43**（反而增排） | 2,173 |

  - BEV 补贴的减排随排放因子线性下降（[D] 斜率约 −3.25 千吨每 g/kWh）；HEV 补贴的减排随排放因子略升（约 +0.15）。
  - 两条线约在葡萄牙水平（251 g/kWh，为韩国的 55%）相交，即韩国电网要**清洁 45%**；[D] 线性插值的交点约 256。
  - 中国水平下，BEV 补贴的减排不到 HEV 的一半（0.9 对 2.1 Mt）；印度和哈萨克斯坦水平下，BEV 补贴几乎不减排甚至增排。
- **表 9 剩余变化（十亿 KRW，PDF p33）**

| | BEV 补贴 | HEV 补贴 |
|---|---:|---:|
| 生产者剩余合计 | 292.5 | **1,024.3** |
| 现代汽车集团 | 291.7 | 1,111.4 |
| 其他国内厂商 | −12.4 | −66.0 |
| 德系 | −48.4 | −66.7 |
| Toyota 集团 | −5.8 | 52.7 |
| Tesla | 67.5 | −7.1 |
| 消费者剩余合计 | 971.5 | **1,253.4** |
| 收入最低 20% | 0.4 | −0.7 |
| 20–40% | 23.6 | 21.2 |
| 40–60% | 109.4 | 194.5 |
| 60–80% | 230.0 | 378.2 |
| 最高 20% | 608.1 | 660.2 |

  - 现代集团在 HEV 补贴下的利润增量约为 BEV 补贴下的 3.8 倍（原文说“nearly four times”），所以看不出短期产业政策理由。
  - 除最低两个收入组差别可忽略外，没有哪个收入组在 BEV 补贴下获益更多，所以分配理由也不成立。两种补贴的收益都集中在高收入组。
  - [D] CS + PS − 财政支出：BEV 约 −2,990 亿，HEV 约 +7,130 亿韩元（未计排放收益和财政影子成本；原文没有做这项加总）。
- **对政策偏向 BEV 的解释**（PDF p33–34）：
  1. 政治经济：前沿技术显眼，政治家看重可见度（Mani & Mukand 2007）。
  2. 长期产业政策：韩国自 2026 年 1 月明确把“支持国内 BEV 产业”列为目标。但若要促进创新和干中学，购置补贴未必是最合适的工具。
  3. 国际贸易战略：美欧限制中国 EV 并补贴本国生产；韩国也开始按对国内 BEV 供应链的贡献分配补贴，实际上削减了对 BYD 等中国车企的补贴。

## 9. 贡献
1. **理论**：提出 **diverted emissions** $e^D_j$ 和 **marginal abatement return** 框架。证明补贴效果取决于“半弹性 × 净转移排放 × 转嫁”，不只是单车排放；对称 logit 下退化为只比单车排放，这正是灵活替代模式重要的原因。框架推广到多产品、多燃料、不完全竞争转嫁和异质里程，权重 $\omega_{ij}$ 与 Conlon–Mortimer 的 diversion 权重同构；总效应等于 MAR 曲线下的面积。
2. **实证**：首次在一个结构模型里比较 HEV 与 BEV 补贴的相对效果。RC logit 结合韩国省-年产品数据、第二选择调查和 7,000 万条年检里程记录。发现 HEV 与 ICEV 的替代性远强于 BEV 与 ICEV。
3. **排放核算**：产品-年层面的生命周期排放（燃料周期 + 车辆周期 + 外部品旧车），并因个体里程而异。量化了高里程者的构成效应：忽略它会低估两种政策的减排。
4. **政策**：预算中性下，把补贴改给 HEV 可多减排 47%；给出 BEV 补贴占优所需的电网碳强度门槛（约 251 g/kWh，即清洁 45%），并做跨国对照。补贴还提高 PS 和 CS，削弱了“BEV 补贴有产业或分配理由”的说法。
5. **转嫁**：给出含需求曲率的多产品补贴转嫁矩阵解析式，并发现 HEV 补贴的转嫁率 > 1、BEV 补贴的转嫁率 < 1 到 > 1 不等。

## 10. 局限与稳健性
- **作者已做的稳健性**：IV logit、嵌套 logit、RC1 与 RC2 对比；使用年限（15/15、15/9、6/6）；所有权结构（母公司、品牌、产品）；电网碳强度（20 档）。HEV 优势只在 IV logit 下反转。
- **作者承认或隐含的限制**：
  - 只重新分配直接购置补贴，不含税收抵免和充电基础设施；现行 BEV 补贴有一定优化，所以结果是 HEV 优势的下界。
  - 假设人人都申请补贴，名额上限不约束。
  - 剔除了 PHEV、HFCV 和世宗市。
  - 车辆周期排放借用美国 GREET 数据。
  - 外部品车辆周期排放设为 0。
  - 电网反事实只改变 BEV 的燃料周期排放，不改变电价或需求。
- **结构上未建模的部分**：
  - 静态模型：没有耐用品动态、学习和网络效应的反馈（充电网络为外生变量）、二手车市场和报废、BEV 技术进步（作者在结论中把降低 BEV 价格、改进属性列为前提条件）。
  - 没有估计供给方程（不同时用供给矩）；边际成本为常数。
  - 没有社会碳成本和完整福利加总。
  - 里程与收入假设独立。
  - 里程是外生的，不受燃料成本反弹效应影响。
  - $\pi_k$ 只放在燃料虚拟变量上，没有和每公里成本交互（与 GRV2018 不同）。
- **数据与识别**：原材料 × 车重的第一阶段系数单独不显著；关税变异主要来自德系和日系进口车。2 个市场的转嫁矩阵病态被剔除。里程矩是 4 个矩对 4 个参数的恰好识别。
- **文字层问题**：图 1–3、A1、B2、C1、E1、F1、G1–G8 只有注释，没有数据；部分公式（如 (5)(21)(26)(32)）在文字层错位，已按上下文重建（见 §11）。

## 11. 公式说明（本篇无校正段；均据文字层重建）
| 式 | 内容 | 重建把握 |
|---|---|---|
| (1) | $\partial E/\partial\tau_j=-M\sum_ke_k\partial s_k/\partial p_j=M(e^D_j-e_j)\partial s_j/\partial p_j$ | 高（已自行推导验证） |
| $D_{j\to k}$, $e^D_j$ | $D_{j\to k}=-\frac{\partial s_k/\partial p_j}{\partial s_j/\partial p_j}$；$e^D_j=\sum_{k\ne j}D_{j\to k}e_k$ | 高 |
| (2) | $-\frac1{s_j}\frac{\partial s_j}{\partial p_j}(e^D_j-e_j)>-\frac1{s_k}\frac{\partial s_k}{\partial p_k}(e^D_k-e_k)$ | 高 |
| (3)(4) | $e_j=\int\omega_{ij}e_{ij}dF$，$e^D_j=\int\omega_{ij}e^D_{ij}dF$，$\omega_{ij}=\frac{\partial s_{ij}/\partial p_j}{\partial s_j/\partial p_j}$ | 高 |
| (5) | 见 6.6（$\Theta_{j,g}$ 加权、除以 $S_g$） | 中高（求和下标错位） |
| (6)(7)(8)(9) | 效用、$\alpha_i=\alpha/y_i$、$\beta_{ik}=\beta_k+\pi_k m_i+\sigma_kv_{ik}$、份额积分 | 高 |
| 反演 | $s_j=\frac1N\sum_i\frac{\exp(\delta_j+\mu_{ij}(\theta))}{1+\sum_\ell\exp(\delta_\ell+\mu_{i\ell}(\theta))}$ | 高 |
| (10)–(12) | $G_1=\frac1{N_p}\sum\xi Z$；$\min G'WG$，$W$ 块对角 | 高 |
| (13) | $p^G=mc-(\Omega\circ\nabla_ps)^{-1}s$，$p^G=p+\tau$ | 高（$\nabla_ps$ 的方向按 FOC 推断为 $\partial s_k/\partial p_j$） |
| (14)(15)(34)(35) | 个体排放、市场排放、三项分解 | 高 |
| (16)–(21) | 预算约束隐函数，MAR 比较 | 中高（(21) 分母按文字层拼接） |
| (22) | $\frac{2-D_{H\to I}}{2-D_{B\to I}}<\frac{e_I-e_H}{e_I-e_B}$ | 高（已自行推导验证） |
| (24)–(26) | 一般化 $-\partial E/\partial\tau_g$、$\partial G/\partial\tau_g$ | 中（下标 g 重用，文字层错位） |
| (27)(28) | $\Delta E_g(\bar G)=\int_0^{\bar G}MAR_g(G)dG$ | 高 |
| (29)–(32) | 转嫁矩阵 $\Theta=[\nabla_ps'+\nabla+K]^{-1}\nabla B$ | 中高（转置位置据 (31) 推断） |
| (33) | 加权相关系数 | 高 |
| 微观矩 $f(v)$ | 相关：$(v_1-v_2v_3)/\sqrt{(v_4-v_2^2)(v_5-v_3^2)}$；里程：$(v_1v_4/(v_2v_3)-1)\times100$ | 相关式高；里程式中 $v$ 的定义待核 |
| BEV 燃料周期 | $e^{FC}_j=\text{EF}/\text{km per kWh}$ | 高 |
| 损耗调整 | $\text{EF}=\text{EF}^{raw}\times100/(100-\text{loss}\%)$ | 高 |
| ICEV/HEV 燃料周期 | $e^{FC}=\text{median CO}_2\times1.14\times1.05/0.86$ | 高 |
| logit/NL | $\ln(s_j/s_0)=x\beta-\alpha p/\bar y+[\rho\ln s_{j\mid g}]+\xi$ | 高 |

## 12. 可复用要点与关联文献
- **可复用要点**
  - **“diverted emissions + MAR”评估框架**：任何“补贴哪种绿色技术”的问题（BEV/PHEV/HEV、热泵/燃气、光伏/储能）都可以套用。MAR = $-\partial E/\partial\tau\,/\,\partial G/\partial\tau$，预算中性下比较 MAR 曲线下的面积。中国 NEV 场景可以直接比较 BEV、PHEV、HEV 补贴，并接入各省电网排放因子。
  - **把个体里程作为“偏好 + 排放”双重异质性**：里程既进入燃料类型偏好（$\pi_k$），又进入个体排放 $T m_i e^{FC}_j$；排放加总的权重用 $\omega_{ij}$。
  - **微观矩组合**：第二选择相关矩（逆抽样权重纠偏）识别 $\sigma$；分燃料平均里程相对参照组的百分比差识别 $\pi$；都可在 PyBLP 中实现。
  - **成本移动工具变量**：FTA 关税下降、原材料价格 × 车重，均滞后一年；嵌套 logit 用组内产品数。
  - **补贴转嫁矩阵解析式**（含曲率项 K）以及“净价转嫁 > 1”的过度转嫁现象。
  - **生命周期排放的工程化流程**：GREET 车辆周期按续航插值；官方 CO2 × 1.14 × 1.05 / 0.86；电网排放因子按损耗调整；外部品用当地旧车队的历史平均。
  - **反事实矩阵**：模型（logit/RC1/RC2）× 使用年限 × 所有权 × 电网强度。
- **与包内文献的关系**
  - **A01 BLP1995 / A02 Petrin2002 / M01 Conlon–Gortmaker**：方法底座（收缩映射、微观矩、PyBLP），本文都有引用。A03 GMY2024 提供第二选择矩的范式，也是弹性对照（−5.06 对本文 −5.91）。
  - **A05 GRV2018**（Grigolon, Reynaert & Verboven，同一位 Verboven）：本文**未引用**，但思路一脉相承，都用里程异质性刻画燃料成本、燃料类型选择和税收政策。区别在于：GRV 把里程乘进生命周期燃料成本，用以识别燃料成本低估；HKV 让里程与燃料类型虚拟变量交互，并把里程用于个体排放核算。每公里成本只有随机系数，没有与里程交互。
  - **A07 GV2014**（NL 还是 RC，本文未引用）：本文同时估计按燃料类型分巢的 NL（ρ = 0.677）和带燃料类型随机系数的 RC，并用后者近似分巢替代。本文结果表明，同质 logit 会把结论翻转到 BEV，与 GV2014“替代模式决定政策结论”的主张一致。
  - **A08 Durrmeyer2022**（法国 feebate 的分配效应，本文未引用）：本文表 9 按收入五分位报告 CS，两种补贴的收益都集中在高收入组，可与 Durrmeyer 的分配分析对照。
  - **A09 BKL2024**（基于属性的补贴与市场力，本文引用）：同样关注补贴设计和不完全竞争下的转嫁。韩国 BEV 补贴本身也基于属性并设价格上限；本文用所有权敏感性检验市场力。
  - **A16 XLL2021**（EV 替代了什么，本文引用）：XLL 发现 EV 主要替代节能车，减排被高估。本文的 $e^D_j$ 把这一思想正式写成 diversion ratio 加权的转移排放，并发现 BEV 主要替代 BEV（0.574）和 HEV（0.101）。
  - **A17 Allcott et al. 2024**：15 年使用年限、全面排放核算，被引用。**A18 Barwick et al. 2026**：EV 关税加补贴，在结论中引用。**A13 Li et al. 2017**：充电网络效应，被引用。**A10 Remmy** 未引用；Heid–Remmy–Reynaert 2025（EV 与电价的互补市场）被引用。**A20 Ji et al.**（中国 NEV 补贴 BLP，本文未引用）：可与本文的韩国结论对照，中国电网 607 g/kWh 下 BEV 补贴的效果不到 HEV 的一半。
