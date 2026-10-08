# A00 包3 说明：汽车 BLP 结构模型原文 txt、公式校正与原文 PDF 位置对照

## 1. 来源与用途
- 源文件：Z3 `汽车BLP结构模型_原文txt_公式校正_20261008.zip` → `00_原文PDF位置与公式校正对照.md`（1197 行，2026-10-08 整理）+ `txt/` 25 个 txt + `核对页图/` 76 张原页截图。
- 收 24 篇汽车行业结构模型论文 + 1 份工作论文版（A14b）对照；每篇一个 txt，为原文 PDF 逐页文字（机器抽取英文原文，非译文）。
- 其中 15 份（14 篇 + GHvB 工作论文版）的核心模型公式已对照原页图逐式转写为 LaTeX，附在 txt 对应页末 `【公式校正｜对照原页图逐式转写，LaTeX】`；**引用公式以校正段为准**（正文机器抽取版常错位乱码）。
- txt 每页以 `===== [PDF 第 n 页｜印刷第 m 页] =====` 开头；核对方式：「本轮看图」「既有看图核验/沿用 09-25 看图核验」「派生 [D]」（由原文数字推导，非原印刷式）。
- 未校正论文（校正条数 0）：A04、A07、A08、A12、A13、A17、A18、A19、A22、A23；其公式以原 PDF 为准。

## 2. 总表（编号｜文献｜分组｜页数｜页码换算｜校正条数｜文本来源）
| 编号 | 文献 | 分组 | 页数 | 页码换算 | 校正 | 来源 |
|---|---|---|---:|---|---:|---|
| A01 | Berry, Levinsohn & Pakes (1995) Automobile Prices in Market Equilibrium. Econometrica 63(4): 841-890 | 底层 | 58 | 印刷 = PDF + 839 | 27 | JSTOR OCR 文字层 |
| A02 | Petrin (2002) Quantifying the Benefits of New Products: The Case of the Minivan. JPE 110(4): 705-729（本地工作论文版） | 需求侧 | 52 | 印刷 = PDF − 2 | 8 | RapidOCR |
| A03 | Grieco, Murry & Yurukoglu (2024) The Evolution of Market Power in the U.S. Automobile Industry. QJE 139(2): 1201-1253（作者版 2023-03-09） | 需求侧 | 67 | 相同 | 8 | 文字层 |
| A04 | Hong, Kim & Verboven (2026) Which Green Technology to Subsidize? Evidence from EVs in South Korea. CEPR DP21757 | 需求侧 | 73 | 印刷 = PDF − 1 | 0 | 文字层 |
| A05 | Grigolon, Reynaert & Verboven (2018) Consumer Valuation of Fuel Costs and Tax Policy. AEJ: Policy 10(3): 193-225 | 需求侧 | 33 | 印刷 = PDF + 192 | 5 | 文字层 |
| A06 | Kaneko & Toyama (2025) Demand Estimation with Flexible Income Effect. JIE 73(1): 186-232 | 需求侧 | 48 | 印刷 = PDF + 185 | 8 | 文字层 |
| A07 | Grigolon & Verboven (2014) Nested Logit or Random Coefficients Logit? REStat 96(5): 916-935 | 需求侧 | 20 | 印刷 = PDF + 915 | 0 | 文字层 |
| A08 | Durrmeyer (2022) Winners and Losers: Distributional Effects of the French Feebate. EJ 132(644): 1414-1448 | 需求侧 | 35 | 印刷 = PDF + 1413 | 0 | 文字层 |
| A09 | Barwick, Kwon & Li (2024) Attribute-Based Subsidies and Market Power: EVs. NBER w32264 | 供给侧 | 57 | 印刷 = PDF − 2 | 9 | 文字层 |
| A10 | Remmy (2026) Adjustable Product Attributes, Indirect Network Effects, and Subsidy Design. AEJ: Policy 18(2): 107-140（作者版） | 供给侧 | 58 | 相同 | 7 | 文字层 |
| A11 | Alé-Chilet, Chen, Li & Reynaert (2026) Colluding Against Environmental Regulation. REStud 93(1): 35-71 | 供给侧 | 37 | 印刷 = PDF + 34 | 11 | 文字层 |
| A12 | Reynaert (2021) Abatement Strategies and the Cost of Environmental Regulation. REStud 88(1): 454-488（早期在线版） | 供给侧 | 35 | 相同 | 0 | 文字层 |
| A13 | Li, Tong, Xing & Zhou (2017) The Market for Electric Vehicles: Indirect Network Effects and Policy Design. JAERE 4(1): 89-133 | 网络效应 | 45 | 印刷 = PDF + 88 | 0 | 文字层 |
| A14 | Gillingham, Houde & van Benthem (2021) Consumer Myopia in Vehicle Purchases. AEJ: Policy 13(3): 207-238 | 标签与信念 | 32 | 印刷 = PDF + 206 | 3 | 文字层 |
| A14b | 同上 NBER w25845 (2019) 工作论文版（含表 D.1、脚注 26） | 标签与信念 | 56 | 印刷 = PDF − 2 | 2 | 文字层 |
| A15 | Reynaert & Sallee (2021) Who Benefits When Firms Game Corrective Policies? AEJ: Policy 13(1): 372-412 | 标签与信念 | 41 | 印刷 = PDF + 371 | 1 | 文字层 |
| A16 | Xing, Leard & Li (2021) What Does an Electric Vehicle Replace? JEEM 107: 102432 | 替代 | 33 | 相同 | 5 | 文字层 |
| A17 | Allcott, Kane, Maydanchik, Shapiro & Tintelnot (2024/2026) The Effects of "Buy American": EVs and the IRA. NBER w33032 | 替代 | 107 | 印刷 = PDF − 2 | 0 | 文字层 |
| A18 | Barwick, Collison, Goldberg, Li & Wang (2026) From Trade War to Green Transition: Optimal EV Tariffs with Revenue-Funded Subsidies. NBER w35334 | 替代 | 85 | 印刷 = PDF − 2 | 0 | 文字层 |
| A19 | Heeney, Knittel & Mandia (2026) Tariffs, Global Value Chains, and the Incidence of Protection: US Automobiles. NBER w35023 | 供给侧 | 57 | 印刷 = PDF − 2 | 0 | 文字层 |
| A20 | Ji, Wang, Zheng & Fan (2026) 中国新能源汽车补贴 BLP 评估（人口特征交互）. JAERE 13(1) | 需求侧 | 40 | 相同 | 6 | 文字层 |
| A21 | Barwick, Kwon, Li & Zahur (2025) Drive Down the Cost: Learning by Doing and Government Policies in the Global EV Battery Industry. NBER w33378 | 供给侧 | 72 | 印刷 = PDF − 2 | 6 | 文字层 |
| A22 | Chou & Derdenger (2025) CCP Estimation of Dynamic Discrete Choice Demand Models with Segment Level Data. Marketing Science 44(5): 1163-1187（**注：txt 实为 2022 年 7 月工作论文版，题为 “Dynamic Discrete Choice Demand Estimation Leveraging Overlapping Groups of Consumers”，数字可能与正式刊不同**——主会话复核发现） | 动态 | 59 | 相同 | 0 | 文字层 |
| A23 | Barwick, Li & Xia (2026) Range Anxiety. NBER w34871（作者据 txt 首页：Panle Jia Barwick、Shanjun Li、Tianli Xia） | 动态 | 68 | 印刷 = PDF − 2 | 0 | 文字层 |
| M01 | Conlon & Gortmaker (2020) Best Practices for Differentiated Products Demand Estimation with PyBLP. RAND 51(4): 1108-1161（早期在线版） | 方法底座 | 54 | 相同 | 9 | 文字层 |

## 3. 原文笔误与记号不一（照抄原文前必看）
- **A01 BLP1995 (6.9b)**（PDF p26）：交叉导数 $\partial s_j/\partial p_q=-\int f_j f_q[\partial\mu_{iq}/\partial p_q]P_0(d\nu)$；原页印 $f_j(\nu,\xi,\dots)$ 与 $\partial\mu_{ij}/\partial p_q$，应为 $\delta$ 与 $\partial\mu_{iq}/\partial p_q$。
- **A01 (6.13)**（p28）：重要性抽样式缺归一因子；若 ns=被接受抽样数，无偏式 $\frac{1}{ns}\sum_i\frac{\bar s(\theta',P_0)}{\bar f(\nu_i,\theta')}f_j(\nu_i,\theta)$；若固定提议抽样数 N，则 $\frac1N\sum_{accepted}f_j/\bar f$；两种计数不可混用。
- **A02 Petrin**（p12）：收入三组价格系数原记 $(\alpha_0,\alpha_1,\alpha_2)$，7.1 节记 $(\alpha_1,\alpha_2,\alpha_3)$，低收入组边界 ≤ 与 < 不一。
- **A03 GMY (6)**：作者版 FOC 下标写反，正确为 $s_{jt}+\sum_{k\in\mathscr J^m_t}(p_{kt}-c_{kt})\partial s_{kt}/\partial p_{jt}=0$。
- **A03 (7)**：Lerner 式需取弹性绝对值 $(p-mc)/p=-\frac{s}{p}/\frac{ds}{dp}$。
- **A03 (8)**：$\alpha_{it}<0$，CS 应除以 $|\alpha_{it}|$；$\widetilde{CS}_t=\frac1T\sum_{v=0}^{T}$ 项数不一致，按文意为对 39 个年份的 $\gamma$ 取平均。
- **A06 Kaneko–Toyama (10)**：分母最后一项 $\xi_{jt}$ 应为 $\xi_{kt}$。
- **A10 Remmy (2)**：利润式缺 $\sum_m$（(3)(4) 有 $\sum_m\phi_{mt}$）；(7) 时序下标不一致，由 (6) 得 $\rho\pi_{m,t+1}=F_{mt}-\rho F_{m,t+1}$。
- **A11 Alé-Chilet (13)**：原印 $mc=p+(\Omega\odot S)^{-1}s$，加号为笔误，正确 $mc=p-(\Omega\odot S)^{-1}s$，$S_{jh}=-\partial s_h/\partial p_j$；等价于 $p+(\Omega\odot J^\top)^{-1}s$，$J_{jh}=\partial s_j/\partial p_h$。
- **A14b GHvB WP 脚注 26**：$\text{total WTP}=\Delta P+\Delta P\times\Delta Q/\eta_D$ 与表 D.1 不一致（按此式各格≈294，表中 −9 至 597），原文笔误；表 D.1 实由 $\Delta WTP=\Delta P-P_1(\Delta Q/Q)/\eta_D$，$P_1=24{,}206$ 复现；期刊版表 7 用 $P_0=24{,}500$。
- **A15 Reynaert–Sallee**：信念 $\tilde x=\alpha x+(1-\alpha)(x-g)=x-(1-\alpha)g$，原页 $\tilde x_t$ 下标疑为残留。
- **A20 Ji (5)**：$\theta_2$ 中 $\alpha_p$ 应为 $\sigma_p$。
- **A21 BKLZ (2)**：county 应为 country；(7) 正文非电池成本 $mc^c$ 与 (1) $mc^v$ 记号不一。
- **M01 Conlon–Gortmaker (6)**：按 $(j,k)=\partial s_{jt}/\partial p_{kt}$ 拼成的 $\Delta$ 与标量 FOC 差一次转置，与 BLP (3.4) $\Delta_{jr}=-\partial s_r/\partial p_j$ 也差一次转置；只有需求 Jacobian 对称（准线性价格混合 logit）时相同，**收入效应规格须按 BLP 方向实现**；(26) 中 $\alpha_i$ 取负值，与 (4) 中 $-\alpha p$ 写法相反，照搬前统一符号。

## 4. 通用 BLP 骨架（来自校正段，跨文献共用）
- 需求：$u_{ijt}=\delta_{jt}+\mu_{ijt}+\epsilon_{ijt}$，$\delta_{jt}=x_{jt}\bar\beta-\alpha p_{jt}+\xi_{jt}$，$\mu_{ijt}=\sum_k\sigma_kx_{jkt}\nu_{ik}$（+人口特征交互）；份额 $s_{jt}=\int\frac{e^{\delta_{jt}+\mu_{ijt}}}{1+\sum_k e^{\delta_{kt}+\mu_{ikt}}}dP(\nu)$。
- 反演（收缩映射，BLP 6.8）：$\delta^{h+1}=\delta^h+\ln s^{obs}-\ln s(\delta^h,\theta_2)$；logit：$\delta=\ln s_j-\ln s_0$；嵌套 logit：$\delta=\ln s_j-\ln s_0-\rho\ln s_{j|h}$。
- 供给（BLP 3.3–3.6）：$s_j+\sum_{r\in\mathcal F_f}(p_r-mc_r)\partial s_r/\partial p_j=0$；$p=mc+\Delta^{-1}s$，$\Delta_{jr}=-\partial s_r/\partial p_j$（同厂）；$\ln(p-b)=w\gamma+\omega$。
- 矩：$E[\xi\mid z]=E[\omega\mid z]=0$；BLP 工具（5.8）：每个特征取自身、同厂其他产品之和、对手产品之和；GMM：$\min g(\theta)'Wg(\theta)$，$g=[\frac1N\sum\xi Z^D;\frac1N\sum\omega Z^S]$。
- 反事实定价：Morrow–Skerlos 定点 $p\leftarrow c+\zeta(p)$，$\zeta=\Lambda^{-1}[\mathcal H\odot\Gamma](p-c)-\Lambda^{-1}s$（M01 (27)）。

## 5. 近期读过但未收入的文献（无原文 PDF）
- Lu (2023) 生命周期燃油成本与里程分布；Springel (2021) AEJ: Policy 充电网络双边市场；Li (2026) Energy Economics 非对称短视随机系数 logit；Miller & Weinberg (2017) Econometrica（啤酒）；Hu 等 (2025) REStat（仅摘要）。

## 6. 局限（原文件第六节）
1. txt 为机器抽取，公式表格脚注常拆散；Petrin (2002) 为 OCR，希腊字母常误识。
2. 公式校正只覆盖核心模型式，不是全文逐式；10 篇未校正。
3. 多篇只有作者版/工作论文版（GMY 2024、Remmy 2026、Chou–Derdenger 2025、Petrin 2002 等），页码与正式刊不同。
4. Reynaert (2021)、Conlon–Gortmaker (2020) 为早期在线版，页码从 1 起。
