# 汽车行业 BLP 与结构模型论文：原文 txt、公式校正与原文 PDF 位置对照

2026-10-08 整理。本包收 24 篇汽车行业结构模型论文（另加 1 份工作论文版作对照），都是近期构建 BLP 与结构模型 skill 时读过、且本机有原文 PDF 的文献。
每篇一个 txt，内容是原文 PDF 的逐页文字（机器抽取的英文原文，不是译文）。其中 15 份（14 篇论文与 GHvB 的工作论文版）的核心模型公式已对照原页图逐式转写为 LaTeX，附在 txt 对应页的末尾。
本文件给出每篇 txt 对应的原文 PDF 绝对路径、PDF 页码与印刷（期刊）页码的换算、每条校正公式在原文中的位置和校正后的公式。

## 一、怎么用

1. txt 中每页以 `===== [PDF 第 n 页｜印刷第 m 页] =====` 开头。PDF 页码 n 可直接在原 PDF 阅读器里跳页，印刷页码 m 对应论文页眉或页脚印的页码。
2. 带校正的页末有一段 `【公式校正｜对照原页图逐式转写，LaTeX】`。正文里同一个公式的机器抽取版本常常错位或乱码，引用时以校正段为准。
3. 核对方式分三种。「本轮看图」指本次打包时重新渲染原页并逐式核对；「既有看图核验」或「沿用 09-25 看图核验」指此前已用同一批原页图核过，本次沿用；「派生 [D]」不是原文印刷式，而是由原文数字或标准推导得出，已注明来源。
4. 未校正的论文和未列出的公式，正文为机器抽取，请以原 PDF 为准。
5. `核对页图\` 文件夹是核对时用的原页截图，文件名为 `<编号>_p<PDF页>.png`，带 `_<起>-<止>` 后缀的是放大的局部。
6. 本文件的公式用 `$...$` 与 `$$...$$` 书写，用支持数学公式的 Markdown 阅读器（Typora、VS Code、Obsidian 等）打开即可渲染。

## 二、总表

| 编号 | 文献 | 分组 | txt 文件 | 原文 PDF（本机绝对路径） | 页数 | 页码换算 | 公式校正条数 | 文本来源 |
|---|---|---|---|---|---:|---|---:|---|
| A01 | Berry, Levinsohn & Pakes (1995). Automobile Prices in Market Equilibrium. Econometrica 63(4): 841-890. | 底层 | `txt\A01_BLP1995.txt` | `D:\codex\blp.pdf` | 58 | 印刷（期刊）页码 = PDF 页码 + 839 | 27 | PDF 文字层 |
| A02 | Petrin (2002). Quantifying the Benefits of New Products: The Case of the Minivan. Journal of Political Economy 110(4): 705-729. 本地为工作论文版 | 需求侧 | `txt\A02_Petrin2002.txt` | `D:\codex\research-memory\pdfs\Z47HEXTA_Petrin_2002.pdf` | 52 | 印刷页码 = PDF 页码 − 2（前 2 页为封面或前置页） | 8 | RapidOCR 识别 |
| A03 | Grieco, Murry & Yurukoglu (2024). The Evolution of Market Power in the U.S. Automobile Industry. Quarterly Journal of Economics 139(2): 1201-1253. 本地为作者版（2023-03-09） | 需求侧 | `txt\A03_GMY2024.txt` | `D:\auto-demand-lit-2026-09\原文PDF\J03_Grieco_2024_QJE_author.pdf` | 67 | 印刷页码与 PDF 页码相同 | 8 | PDF 文字层 |
| A04 | Hong, Kim & Verboven (2026). Which Green Technology to Subsidize? Evidence from Electric Vehicles in South Korea. CEPR Discussion Paper DP21757（作者版） | 需求侧 | `txt\A04_HKV2026.txt` | `D:\auto-demand-lit-2026-09\原文PDF\W07_Hong_2026_CEPR_author.pdf` | 73 | 印刷页码 = PDF 页码 − 1（前 1 页为封面或前置页） | 0 | PDF 文字层 |
| A05 | Grigolon, Reynaert & Verboven (2018). Consumer Valuation of Fuel Costs and Tax Policy: Evidence from the European Car Market. AEJ: Economic Policy 10(3): 193-225. | 需求侧 | `txt\A05_GRV2018.txt` | `D:\codex\output\blp_bundle_20261007\package\02_five_BLP_recommendations\R01_GRV2018\original.pdf` | 33 | 印刷（期刊）页码 = PDF 页码 + 192 | 5 | PDF 文字层 |
| A06 | Kaneko & Toyama (2025). Demand Estimation with Flexible Income Effect: An Application to Pass-Through and Merger Analysis. Journal of Industrial Economics 73(1): 186-232. | 需求侧 | `txt\A06_KanekoToyama2025.txt` | `D:\codex\output\blp_bundle_20261007\package\01_existing_fuel_batch\original_pdfs\P10_Kaneko2024_JIE.pdf` | 48 | 印刷（期刊）页码 = PDF 页码 + 185 | 8 | PDF 文字层 |
| A07 | Grigolon & Verboven (2014). Nested Logit or Random Coefficients Logit? A Comparison of Alternative Discrete Choice Models of Product Differentiation. Review of Economics and Statistics 96(5): 916-935. | 需求侧 | `txt\A07_GrigolonVerboven2014.txt` | `C:\Users\于舒奕\Downloads\Nested_Logit_or_Random_Coefficients_Logit__A_Comparison_of_Alternative_Discrete_Choice_Models_of_Product_Differentiation.pdf` | 20 | 印刷（期刊）页码 = PDF 页码 + 915 | 0 | PDF 文字层 |
| A08 | Durrmeyer (2022). Winners and Losers: The Distributional Effects of the French Feebate on the Automobile Market. Economic Journal 132(644): 1414-1448. | 需求侧 | `txt\A08_Durrmeyer2022.txt` | `C:\Users\于舒奕\Downloads\Winners_and_Losers__the_Distributional_Effects_of_the_French_Feebate_on_the_Automobile_Market.pdf` | 35 | 印刷（期刊）页码 = PDF 页码 + 1413 | 0 | PDF 文字层 |
| A09 | Barwick, Kwon & Li (2024). Attribute-Based Subsidies and Market Power: An Application to Electric Vehicles. NBER Working Paper w32264 (March 2024). | 供给侧 | `txt\A09_BKL2024.txt` | `D:\codex\output\blp_bundle_20261007\package\01_existing_fuel_batch\original_pdfs\P02_w32264.pdf` | 57 | 印刷页码 = PDF 页码 − 2（前 2 页为封面或前置页） | 9 | PDF 文字层 |
| A10 | Remmy (2026). Adjustable Product Attributes, Indirect Network Effects, and Subsidy Design: The Case of Electric Vehicles. AEJ: Economic Policy 18(2): 107-140. 本地为作者版 | 供给侧 | `txt\A10_Remmy2026.txt` | `D:\auto-demand-lit-2026-09\原文PDF\J01_Remmy_2026_AEJEP_author.pdf` | 58 | 印刷页码与 PDF 页码相同 | 7 | PDF 文字层 |
| A11 | Alé-Chilet, Chen, Li & Reynaert (2026). Colluding Against Environmental Regulation. Review of Economic Studies 93(1): 35-71. | 供给侧 | `txt\A11_AleChilet2026.txt` | `D:\auto-demand-lit-2026-09\原文PDF\J10_AleChilet_2026_REStud_journal.pdf` | 37 | 印刷（期刊）页码 = PDF 页码 + 34 | 11 | PDF 文字层 |
| A12 | Reynaert (2021). Abatement Strategies and the Cost of Environmental Regulation: Emission Standards on the European Car Market. Review of Economic Studies 88(1): 454-488. | 供给侧 | `txt\A12_Reynaert2021.txt` | `D:\codex\research-memory\deep-reading\blp40s_20260403\pdfs\29_dzvnrcum.pdf` | 35 | 印刷页码与 PDF 页码相同 | 0 | PDF 文字层 |
| A13 | Li, Tong, Xing & Zhou (2017). The Market for Electric Vehicles: Indirect Network Effects and Policy Design. JAERE 4(1): 89-133. | 网络效应 | `txt\A13_LiTongXingZhou2017.txt` | `D:\codex\research-memory\pdfs\blp_1995_citing_2026-03-21\Li_Tong_Xing_Zhou_2017_Market_for_Electric_Vehicles_mirror.pdf` | 45 | 印刷（期刊）页码 = PDF 页码 + 88 | 0 | PDF 文字层 |
| A14 | Gillingham, Houde & van Benthem (2021). Consumer Myopia in Vehicle Purchases: Evidence from a Natural Experiment. AEJ: Economic Policy 13(3): 207-238. | 标签与信念 | `txt\A14_GHvB2021.txt` | `D:\codex\output\blp_bundle_20261007\package\01_existing_fuel_batch\original_pdfs\P15_Gillingham2021_Myopia.pdf` | 32 | 印刷（期刊）页码 = PDF 页码 + 206 | 3 | PDF 文字层 |
| A14b | Gillingham, Houde & van Benthem (2019). Consumer Myopia in Vehicle Purchases: Evidence from a Natural Experiment. NBER Working Paper w25845（A14 的工作论文版，含表 D.1 与脚注 26） | 标签与信念 | `txt\A14b_GHvB2019WP.txt` | `C:\Users\于舒奕\Downloads\w25845.pdf` | 56 | 印刷页码 = PDF 页码 − 2（前 2 页为封面或前置页） | 2 | PDF 文字层 |
| A15 | Reynaert & Sallee (2021). Who Benefits When Firms Game Corrective Policies? AEJ: Economic Policy 13(1): 372-412. | 标签与信念 | `txt\A15_ReynaertSallee2021.txt` | `D:\codex\output\blp_bundle_20261007\package\02_five_BLP_recommendations\R02_Reynaert_Sallee2021\original.pdf` | 41 | 印刷（期刊）页码 = PDF 页码 + 371 | 1 | PDF 文字层 |
| A16 | Xing, Leard & Li (2021). What Does an Electric Vehicle Replace? Journal of Environmental Economics and Management 107: 102432. | 替代 | `txt\A16_XingLeardLi2021.txt` | `D:\codex\output\blp_bundle_20261007\package\02_five_BLP_recommendations\R04_Xing_Leard_Li2021\original.pdf` | 33 | 印刷页码与 PDF 页码相同 | 5 | PDF 文字层 |
| A17 | Allcott, Kane, Maydanchik, Shapiro & Tintelnot (2024, 2026 修订). The Effects of "Buy American": Electric Vehicles and the Inflation Reduction Act. NBER Working Paper w33032. | 替代 | `txt\A17_Allcott2026.txt` | `D:\codex\output\blp_bundle_20261007\package\01_existing_fuel_batch\original_pdfs\P08_w33032.pdf` | 107 | 印刷页码 = PDF 页码 − 2（前 2 页为封面或前置页） | 0 | PDF 文字层 |
| A18 | Barwick, Collison, Goldberg, Li & Wang (2026). From Trade War to Green Transition: Optimal Electric Vehicle Tariffs with Revenue-Funded Subsidies. NBER Working Paper w35334. | 替代 | `txt\A18_BCGLW2026.txt` | `D:\auto-demand-lit-2026-09\原文PDF\W01_Barwick_2026_NBER_NBERwp.pdf` | 85 | 印刷页码 = PDF 页码 − 2（前 2 页为封面或前置页） | 0 | PDF 文字层 |
| A19 | Heeney, Knittel & Mandia (2026). Tariffs, Global Value Chains, and the Incidence of Protection: Evidence from US Automobiles. NBER Working Paper w35023. | 供给侧 | `txt\A19_HKM2026.txt` | `D:\auto-demand-lit-2026-09\原文PDF\W02_Heeney_2026_NBER_NBERwp.pdf` | 57 | 印刷页码 = PDF 页码 − 2（前 2 页为封面或前置页） | 0 | PDF 文字层 |
| A20 | Ji, Wang, Zheng & Fan (2026). 中国新能源汽车补贴的 BLP 评估（人口特征交互）. JAERE 13(1). | 需求侧 | `txt\A20_Ji2026.txt` | `D:\blp-lit-recommend-20261002\package_20261008\03_人口特征交互_Ji2026_JAERE\Ji2026_原文.pdf` | 40 | 印刷页码与 PDF 页码相同 | 6 | PDF 文字层 |
| A21 | Barwick, Kwon, Li & Zahur (2025). Drive Down the Cost: Learning by Doing and Government Policies in the Global EV Battery Industry. NBER Working Paper w33378 (Revised Aug 2025). | 供给侧 | `txt\A21_BKLZ2025.txt` | `D:\codex\output\blp_bundle_20261007\package\01_existing_fuel_batch\original_pdfs\P01_w33378.pdf` | 72 | 印刷页码 = PDF 页码 − 2（前 2 页为封面或前置页） | 6 | PDF 文字层 |
| A22 | Chou & Derdenger (2025). CCP Estimation of Dynamic Discrete Choice Demand Models with Segment Level Data and Continuous Unobserved Heterogeneity. Marketing Science 44(5): 1163-1187. 本地为作者版 | 动态 | `txt\A22_ChouDerdenger2025.txt` | `D:\auto-demand-lit-2026-09\原文PDF\J07_Chou_2025_MKSC_author.pdf` | 59 | 印刷页码与 PDF 页码相同 | 0 | PDF 文字层 |
| A23 | Barwick et al. (2026). Range Anxiety. NBER Working Paper w34871. | 动态 | `txt\A23_RangeAnxiety2026.txt` | `D:\auto-demand-lit-2026-09\原文PDF\W03_Barwick_2026_NBER_NBERwp.pdf` | 68 | 印刷页码 = PDF 页码 − 2（前 2 页为封面或前置页） | 0 | PDF 文字层 |
| M01 | Conlon & Gortmaker (2020). Best Practices for Differentiated Products Demand Estimation with PyBLP. RAND Journal of Economics 51(4): 1108-1161. | 方法底座 | `txt\M01_ConlonGortmaker2020.txt` | `D:\codex\research-memory\deep-reading\blp40s_20260403\pdfs\30_bfp23mj2.pdf` | 54 | 印刷页码与 PDF 页码相同 | 9 | PDF 文字层 |

## 三、原文笔误与记号不一（本次核对中发现）

各条都已在对应 txt 的校正段写明原印刷式与正确写法，照抄原文前请先看这一节。

- **A01 BLP1995，PDF 第 26 页，(6.9b)**　原页有前置负号；原页印作 $f_j(\nu,\xi,\dots)$ 与 $[\partial\mu_{ij}/\partial p_q]$，两处为原文笔误，应为 $\delta$ 与 $\partial\mu_{iq}/\partial p_q$
- **A01 BLP1995，PDF 第 28 页，(6.13)**　原页即如此印刷，缺归一因子。原文写明求和对被接受的 $\nu$ 进行，若 ns 指被接受的抽样数，无偏式为 $\frac{1}{ns}\sum_{i=1}^{ns}\frac{\bar s(\theta',P_0)}{\bar f(\nu_i,\theta')}f_j(\nu_i,\theta)$；若改为固定提议抽样数 N，则为 $\frac{1}{N}\sum_{\text{accepted}}f_j(\nu_i,\theta)/\bar f(\nu_i,\theta')$。两种计数不可混用
- **A02 Petrin2002，PDF 第 12 页，（收入组价格系数）**　$\bar y_1,\bar y_2$ 把美国人口按收入三等分。第 7.1 节（PDF 第 17 页）把这三个参数记作 $(\alpha_1,\alpha_2,\alpha_3)$，低收入组写作 $y_i<\bar y_1$，原文前后记号不一
- **A03 GMY2024，PDF 第 12 页，(6)**　原页印作 $s_{jt}+\sum_{k\in\mathscr J^m_t}(p_{jt}-c_{jt})\,\partial s_{jt}/\partial p_{kt}=0$，下标写反，为作者版笔误；上式为与 BLP (3.3) 一致的正确写法
- **A03 GMY2024，PDF 第 18 页，(7)**　原页如此；按字面 ds/dp<0 时右端为负，弹性须取绝对值，即 $(p-mc)/p=-\frac{s}{p}\big/\frac{ds}{dp}$（单产品厂商情形）
- **A03 GMY2024，PDF 第 23 页，(8)**　原页如此。本文 $\alpha_{it}<0$，按字面 $1/\alpha_{it}$ 会使补偿变化为负，钱度量应除以 $-\alpha_{it}$（即 $|\alpha_{it}|$）。其后 $\widetilde{CS}_t=\frac{1}{T}\sum_{v=0}^{T}CS_t(\gamma_v)$，v 从 0 到 T 共 T+1 项，与 1/T 不一致，按文意为对 39 个年份的 $\gamma$ 取平均
- **A06 KanekoToyama2025，PDF 第 9 页，(10)**　原页分母最后一项印作 $\xi_{jt}$，应为 $\xi_{kt}$（求和下标为 k），排印笔误
- **A10 Remmy2026，PDF 第 14 页，(2)**　原页如此。正文说利润是各州利润的加权和，式中却没有对 m 求和；(3)(4) 中有 $\sum_m\phi_{mt}$，按文意 (2) 应含 $\sum_m$。$\lambda_{jt}$ 为补贴，厂商收到 $p_{jt}+\lambda_{jt}$
- **A10 Remmy2026，PDF 第 15 页，(7)**　原页如此。由 (6) 直接得到的是 $\rho\pi_{m,t+1}=F_{mt}-\rho F_{m,t+1}$，即左侧与 $Q^{EV}$ 应为 t+1 期；原式时序下标不一致，使用时按入场年份统一。其后设 $\vartheta(d_{mt})=(\kappa d_{mt})^{\iota}$
- **A11 AleChilet2026，PDF 第 21 页，(13)**　原页印作 $\boldsymbol{mc}=\boldsymbol p+(\Omega\odot S(\boldsymbol a,\boldsymbol p))^{-1}\boldsymbol s$。在原文自己的定义 $S_{jh}=-\partial s_h/\partial p_j$ 下，$(\Omega\odot S)^{-1}s$ 是正的加价，加号是笔误，照抄会得到 mc>p；上式为正确写法，等价于 $\boldsymbol p+(\Omega\odot J^{\top})^{-1}\boldsymbol s$（$J_{jh}=\partial s_j/\partial p_h$）
- **A14b GHvB2019WP，PDF 第 50 页，脚注 26（原印刷）**　原页确实如此印刷。该式与同文表 D.1 不一致：按此式各格都约等于 294，而表 D.1 从 −9 到 597。判断为原文笔误，不要照抄
- **A15 ReynaertSallee2021，PDF 第 18 页，（未编号，信念设定）**　x 为真实油耗（坏属性），m 为卖方发出的信息即官方标称值，g 为博弈（gaming）量。$\alpha=1$ 时买方完全识破，$\alpha=0$ 时完全被骗。原页式中写作 $\tilde x_t$（带下标 t），正文称 $\tilde x$，下标疑为排印残留。其前：$\beta=(p_f+\tau)\times k$，全信息需求 $D(f)=D(p+\beta x)$，感知 $\tilde f=p+\beta\tilde x$；成本 c(x) 满足 c'<0,c''>0，博弈成本 h(g) 满足 h'>0,h''>0；规制 $m=x-g\le\sigma$
- **A20 Ji2026，PDF 第 12 页，(5)**　原文随后写 $\theta_2=(\alpha_1,\alpha_2,\alpha_p,\sigma_k)$，其中 $\alpha_p$ 与式 (2) 的 $\sigma_p$ 记号不一，按 (2) 应为 $\sigma_p$
- **A21 BKLZ2025，PDF 第 13 页，(2)**　$\phi_{jct}$ 为中央政府消费者补贴。原文此处写 consumer i in county c，全文其余处为 country c，county 疑为笔误
- **A21 BKLZ2025，PDF 第 20 页，(7)**　BK 为电池容量（kWh），$E_{bt}=\sum_{s<t}\sum_c\sum_{j\in\mathscr I\{I_{bcs}=1\}}q_{jcs}$ 为供应商累计产量（干中学），学习率 $1-2^{\gamma_E}$；CH 为电池化学类型，PK 为工厂产能。同页 $mk^{b}_{jct}=\frac{\lambda^b}{1-\lambda^b}\overline{mk}^{b}_{jct}$；正文把非电池成本写作 $mc^{c}_{jct}$，与 (1) 的 $mc^{v}_{jct}$ 记号不一

## 四、逐篇公式位置与校正后的公式

### A01 BLP1995

Berry, Levinsohn & Pakes (1995). Automobile Prices in Market Equilibrium. Econometrica 63(4): 841-890.

原文 PDF：`D:\codex\blp.pdf`　txt：`txt\A01_BLP1995.txt`

| 式号 | PDF 页 | 印刷页 | 核对方式 |
|---|---:|---:|---|
| (2.1) | 7 | 846 | 既有看图核验 |
| (2.2) | 7 | 846 | 既有看图核验 |
| (2.3) | 7 | 846 | 既有看图核验 |
| (2.4) | 7 | 846 | 既有看图核验 |
| (2.5) | 9 | 848 | 本轮看图 |
| (2.6) | 9 | 848 | 本轮看图 |
| (2.7a) | 10 | 849 | 本轮看图 |
| (2.7b) | 10 | 849 | 本轮看图 |
| (3.1) | 14 | 853 | 本轮看图 |
| (3.2) | 14 | 853 | 本轮看图 |
| (3.3) | 14 | 853 | 本轮看图 |
| (3.4) | 14 | 853 | 本轮看图 |
| （未编号） | 15 | 854 | 既有看图核验 |
| (3.5) | 15 | 854 | 既有看图核验 |
| (3.6) | 15 | 854 | 既有看图核验 |
| (4.1) | 15 | 854 | 既有看图核验 |
| (5.8) | 22 | 861 | 既有看图核验 |
| (6.2)–(6.5) | 25 | 864 | 既有看图核验 |
| (6.6) | 26 | 865 | 既有看图核验 |
| (6.7) | 26 | 865 | 既有看图核验 |
| (6.8) | 26 | 865 | 既有看图核验 |
| (6.9a) | 26 | 865 | 既有看图核验 |
| (6.9b) | 26 | 865 | 既有看图核验（2026-10-07 重开原页） |
| (6.10) | 27 | 866 | 本轮看图 |
| (6.11) | 27 | 866 | 本轮看图 |
| (6.12) | 27 | 866 | 本轮看图 |
| (6.13) | 28 | 867 | 本轮看图 |

**(2.1)**（PDF 第 7 页）

$$
A_j(x,p,\xi;\theta)=\{\zeta:\ U(\zeta,p_j,x_j,\xi_j;\theta)\ \ge\ U(\zeta,p_r,x_r,\xi_r;\theta),\ r=0,\dots,J\}
$$

说明：r=0 为 outside good

**(2.2)**（PDF 第 7 页）

$$
s_j(x,p,\xi;\theta)=\int_{\zeta\in A_j}P_0(d\zeta)
$$

说明：市场需求量为 $M s_j$

**(2.3)**（PDF 第 7 页）

$$
U(\zeta_i,p_j,x_j,\xi_j;\theta)=x_j\beta-\alpha p_j+\xi_j+\epsilon_{ij}\equiv\delta_j+\epsilon_{ij}
$$

**(2.4)**（PDF 第 7 页）

$$
s_j=\int_{\epsilon}\prod_{q\ne j}P(\delta_j-\delta_q+\epsilon)\,P(d\epsilon)
$$

说明：logit 下替代只取决于份额，见原文 p.847

**(2.5)**（PDF 第 9 页）

$$
U(\zeta_i,p_j,x_j,\xi_j;\theta)=x_j\bar\beta-\alpha p_j+\xi_j+\sum_k\sigma_k x_{jk}\nu_{ik}+\epsilon_{ij}
$$

说明：其后 $\delta_j=x_j\bar\beta-\alpha p_j+\xi_j$，$\mu_{ij}=\sum_k\sigma_k x_{jk}\nu_{ik}+\epsilon_{ij}$

**(2.6)**（PDF 第 9 页）

$$
U(\zeta_i,p_j,x_j,\xi_j;\theta)=(y_i-p_j)^{\alpha}\,G(x_j,\xi_j,\nu_i)\,e^{\epsilon(i,j)}
$$

说明：文字层未识别出式号

**(2.7a)**（PDF 第 10 页）

$$
u_{ij}=\alpha\log(y_i-p_j)+x_j\bar\beta+\xi_j+\sum_k\sigma_k x_{jk}\nu_{ik}+\epsilon_{ij},\quad j=1,\dots,J
$$

**(2.7b)**（PDF 第 10 页）

$$
u_{i0}=\alpha\log(y_i)+\xi_0+\sigma_0\nu_{i0}+\epsilon_{i0}
$$

说明：其后 $\nu_i=(y_i,\nu_{i1},\dots,\nu_{iK})$

**(3.1)**（PDF 第 14 页）

$$
\ln(mc_j)=w_j\gamma+\omega_j
$$

**(3.2)**（PDF 第 14 页）

$$
\Pi_f=\sum_{j\in\mathcal F_f}(p_j-mc_j)\,M\,s_j(p,x,\xi;\theta)
$$

**(3.3)**（PDF 第 14 页）

$$
s_j(p,x,\xi;\theta)+\sum_{r\in\mathcal F_f}(p_r-mc_r)\,\frac{\partial s_r(p,x,\xi;\theta)}{\partial p_j}=0
$$

**(3.4)**（PDF 第 14 页）

$$
\Delta_{jr}=\begin{cases}-\dfrac{\partial s_r}{\partial p_j}, & r\text{ 与 }j\text{ 同厂}\\[4pt] 0, & \text{否则}\end{cases}
$$

说明：行 = j 的价格 FOC，列 = r；若代码存 $J_{jr}=\partial s_j/\partial p_r$，则 $\Delta=-(H\odot J^{\top})$

**（未编号）**（PDF 第 15 页）

$$
s(p,x,\xi;\theta)-\Delta(p,x,\xi;\theta)\,[p-mc]=0\ \Rightarrow\ p=mc+\Delta(p,x,\xi;\theta)^{-1}s(p,x,\xi;\theta)
$$

**(3.5)**（PDF 第 15 页）

$$
b(p,x,\xi;\theta)\equiv\Delta(p,x,\xi;\theta)^{-1}s(p,x,\xi;\theta)
$$

**(3.6)**（PDF 第 15 页）

$$
\ln\big(p-b(p,x,\xi;\theta)\big)=w\gamma+\omega
$$

**(4.1)**（PDF 第 15 页）

$$
E[\xi_j(\theta_0)\mid z]=E[\omega_j(\theta_0)\mid z]=0,\qquad z_j=[x_j,w_j],\ z=[z_1,\dots,z_J]
$$

说明：价格与数量不进条件集

**(5.8)**（PDF 第 22 页）

$$
\Big\{\,z_{jk},\ \sum_{r\ne j,\ r\in\mathcal F_f}z_{rk},\ \sum_{r\notin\mathcal F_f}z_{rk}\,\Big\}
$$

说明：对每个特征 k 取自身、同厂其他产品之和、对手产品之和，即 BLP 工具的原型

**(6.2)–(6.5)**（PDF 第 25 页）

$$
s_j=\frac{e^{\delta_j}}{1+\sum_{q}e^{\delta_q}},\qquad \ln s_j-\ln s_0=\delta_j,\qquad \xi_j=\ln s^n_j-\ln s^n_0-x_j\beta+\alpha p_j
$$

说明：logit 特例；此处只核了公式内容，未逐个对应式号

**(6.6)**（PDF 第 26 页）

$$
f_j(\nu_i,\delta,p,x,\theta)=\frac{\exp(\delta_j+\mu_{ij})}{1+\sum_r\exp(\delta_r+\mu_{ir})}
$$

**(6.7)**（PDF 第 26 页）

$$
s_j=\int f_j\big(\nu_i,\delta(x,p,\xi),p,x,\theta\big)\,P_0(d\nu)
$$

**(6.8)**（PDF 第 26 页）

$$
T(s,\theta,P)[\delta]_j=\delta_j+\ln(s_j)-\ln\big[s_j(p,x,\delta,P;\theta)\big]
$$

说明：收缩映射；反演后 $\xi_j(\theta,s,P)=\delta_j(\theta,s,P)-x_j\beta$（完整规格价格在非线性部分，不出现 $+\alpha p_j$）

**(6.9a)**（PDF 第 26 页）

$$
\frac{\partial s_j}{\partial p_j}=\int f_j(1-f_j)\left[\frac{\partial\mu_{ij}}{\partial p_j}\right]P_0(d\nu)
$$

**(6.9b)**（PDF 第 26 页）

$$
\frac{\partial s_j}{\partial p_q}=-\int f_j\,f_q\left[\frac{\partial\mu_{iq}}{\partial p_q}\right]P_0(d\nu),\quad q\ne j
$$

说明：原页有前置负号；原页印作 $f_j(\nu,\xi,\dots)$ 与 $[\partial\mu_{ij}/\partial p_q]$，两处为原文笔误，应为 $\delta$ 与 $\partial\mu_{iq}/\partial p_q$

**(6.10)**（PDF 第 27 页）

$$
s_j(p,x,\xi,\theta,P_{ns})\equiv\frac{1}{ns}\sum_{i=1}^{ns}f_j(\nu_i,\delta,p,x,\theta)
$$

**(6.11)**（PDF 第 27 页）

$$
s_j(\theta,P_0)=\int\left[\frac{f_j(\nu,\theta)}{h(\nu,\theta)}\,p_0(\nu)\,h(\nu,\theta)\right]d\nu\equiv\int f_{hj}(\nu,\theta)\,P_{hj}(d\nu,\theta)\equiv s_j(\theta,P_{hj})
$$

说明：$P_{hj}(d\nu,\theta)\equiv h(\nu,\theta)d\nu$，$f_{hj}(\nu,\theta)\equiv[f_j(\nu,\theta)p_0(\nu)]/h(\nu,\theta)$

**(6.12)**（PDF 第 27 页）

$$
P^{*}_{hj}(d\nu,\theta)=\big[f_j(\nu,\theta)\,p_0(\nu)\,d\nu\big]\big/s_j(\theta,P_0)
$$

**(6.13)**（PDF 第 28 页）

$$
s_j\big[\theta,P^{*}_{h}(\theta')_{ns}\big]=\sum_{i=1}^{ns}\frac{\bar s(\theta',P_0)}{\bar f(\nu_i,\theta')}\,f_j(\nu_i,\theta)\quad\text{（求和只对被接受的抽样）}
$$

说明：原页即如此印刷，缺归一因子。原文写明求和对被接受的 $\nu$ 进行，若 ns 指被接受的抽样数，无偏式为 $\frac{1}{ns}\sum_{i=1}^{ns}\frac{\bar s(\theta',P_0)}{\bar f(\nu_i,\theta')}f_j(\nu_i,\theta)$；若改为固定提议抽样数 N，则为 $\frac{1}{N}\sum_{\text{accepted}}f_j(\nu_i,\theta)/\bar f(\nu_i,\theta')$。两种计数不可混用

### A02 Petrin2002

Petrin (2002). Quantifying the Benefits of New Products: The Case of the Minivan. Journal of Political Economy 110(4): 705-729. 本地为工作论文版

原文 PDF：`D:\codex\research-memory\pdfs\Z47HEXTA_Petrin_2002.pdf`　txt：`txt\A02_Petrin2002.txt`

| 式号 | PDF 页 | 印刷页 | 核对方式 |
|---|---:|---:|---|
| （效用，印刷 p.10） | 12 | 10 | 本轮看图 |
| （收入组价格系数） | 12 | 10 | 本轮看图 |
| （家庭规模交互，印刷 p.11） | 13 | 11 | 本轮看图 |
| （选择概率与份额） | 13 | 11 | 本轮看图 |
| (5.1) | 14 | 12 | 本轮看图 |
| （微观矩一，印刷 p.15） | 17 | 15 | 本轮看图 |
| （微观矩二，印刷 p.16） | 18 | 16 | 本轮看图 |
| （BLP 矩） | 18 | 16 | 本轮看图 |

**（效用，印刷 p.10）**（PDF 第 12 页）

$$
u_{ij}=\alpha_i\ln(y_i-p_j)+X_j\beta+\sum_k\gamma_k\nu_{ik}x_{jk}+\xi_j+\epsilon_{ij}
$$

**（收入组价格系数）**（PDF 第 12 页）

$$
\alpha_i=\begin{cases}\alpha_0 & y_i\le\bar y_1\\ \alpha_1 & \bar y_1\le y_i<\bar y_2\\ \alpha_2 & y_i\ge\bar y_2\end{cases},\qquad \gamma_{ik}=\gamma_k\nu_{ik}
$$

说明：$\bar y_1,\bar y_2$ 把美国人口按收入三等分。第 7.1 节（PDF 第 17 页）把这三个参数记作 $(\alpha_1,\alpha_2,\alpha_3)$，低收入组写作 $y_i<\bar y_1$，原文前后记号不一

**（家庭规模交互，印刷 p.11）**（PDF 第 13 页）

$$
\gamma_{i,mi}=\gamma_{mi}\ln(fs_i)\,\nu_{if},\qquad \gamma_{i,sw}=\gamma_{sw}\ln(fs_i)\,\nu_{if}
$$

说明：mi 为厢式旅行车（minivan），sw 为旅行车；$\nu_{if}$ 为对家庭用车的共同特异口味

**（选择概率与份额）**（PDF 第 13 页）

$$
Pr(j\mid X,i)=\frac{e^{\alpha_i\ln(y_i-p_j)+X_j\beta+\sum_k\gamma_k\nu_{ik}x_{jk}+\xi_j}}{\sum_l e^{\alpha_i\ln(y_i-p_l)+X_l\beta+\sum_k\gamma_k\nu_{ik}x_{lk}+\xi_l}},\qquad s_j=\int_i Pr(j\mid X,i)\,P(di)=\int_i\frac{e^{\delta_j+\mu_{ij}}}{\sum_l e^{\delta_l+\mu_{il}}}P(di)
$$

说明：$(y_i,fs_i)$ 联合分布取自 CEX；未观测口味用 K 个独立、在 95% 处截断的 $\chi^2(3)$

**(5.1)**（PDF 第 14 页）

$$
\ln(mc_j)=W_j\tau+\omega_j
$$

说明：其后 $\Pi_f=M\sum_{j\in J_f}(p_j-mc_j)\,s_j(p,X;\theta)$，$q_j(p,X;\theta)=M\,s_j(p,X;\theta)$，多产品 Bertrand-Nash

**（微观矩一，印刷 p.15）**（PDF 第 17 页）

$$
E\big[\{i\text{ 购新车}\}\mid\{y_i<\bar y_1\}\big],\quad E\big[\{i\text{ 购新车}\}\mid\{\bar y_1\le y_i<\bar y_2\}\big],\quad E\big[\{i\text{ 购新车}\}\mid\{y_i\ge\bar y_2\}\big]
$$

说明：按收入组的购车概率，识别收入效应参数

**（微观矩二，印刷 p.16）**（PDF 第 18 页）

$$
E\big[fs_i\mid\{i\text{ 购 minivan}\}\big],\ E\big[fs_i\mid\{i\text{ 购 station wagon}\}\big],\ E\big[fs_i\mid\{i\text{ 购 SUV}\}\big],\ E\big[fs_i\mid\{i\text{ 购 full-size van}\}\big]
$$

说明：另有四个矩：四类家庭用车买家户主年龄在 30 至 60 岁的概率。共 11 个微观矩

**（BLP 矩）**（PDF 第 18 页）

$$
s_j(\delta(\theta),\theta)-\mathbf s_j=0,\ j=0,1,\dots,J;\qquad E[\xi_j(\theta_0)\mid(X,W)]=E[\omega_j(\theta_0)\mid(X,W)]=0
$$

### A03 GMY2024

Grieco, Murry & Yurukoglu (2024). The Evolution of Market Power in the U.S. Automobile Industry. Quarterly Journal of Economics 139(2): 1201-1253. 本地为作者版（2023-03-09）

原文 PDF：`D:\auto-demand-lit-2026-09\原文PDF\J03_Grieco_2024_QJE_author.pdf`　txt：`txt\A03_GMY2024.txt`

| 式号 | PDF 页 | 印刷页 | 核对方式 |
|---|---:|---:|---|
| (1) | 10 | 10 | 本轮看图 |
| (2) | 10 | 10 | 本轮看图 |
| (3) | 11 | 11 | 本轮看图 |
| (4) | 11 | 11 | 本轮看图 |
| (5) | 12 | 12 | 本轮看图 |
| (6) | 12 | 12 | 本轮看图（放大核对） |
| (7) | 18 | 18 | 本轮看图 |
| (8) | 23 | 23 | 本轮看图 |

**(1)**（PDF 第 10 页）

$$
u_{ijt}=\beta_{it}\mathbf x_{jt}+\alpha_{it}p_{jt}+\xi_{jt}+\epsilon_{ijt}
$$

说明：outside：$u_{i0t}=\gamma_t+\epsilon_{i0t}$；$\xi_{jt}=\tau_t+\tilde\xi_{jt}$，$E[\tilde\xi_{jt}\mid\mathbf z_{jt}]=0$

**(2)**（PDF 第 10 页）

$$
\forall j\in\mathscr C_t:\ E[\xi_{jt}-\xi_{jt-1}]=E\big[(\tau_t-\tau_{t-1})+(\tilde\xi_{jt}-\tilde\xi_{jt-1})\big]=0
$$

说明：$\mathscr C_t$ 为未改款的持续车型；归一化 $\tau_0=0$

**(3)**（PDF 第 11 页）

$$
\alpha_{it}=\bar\alpha+\sum_h\alpha_h D^h_{it}
$$

**(4)**（PDF 第 11 页）

$$
\beta_{ik}=\bar\beta_k+\sum_h\beta_{kh}D^h_{it}+\sigma_k\nu_{ik}
$$

说明：$D_{it}$ 的分布取自 CPS，$\nu_{ik}$ 独立标准正态

**(5)**（PDF 第 12 页）

$$
s_{jt}=\int_i\frac{\exp(\beta_{it}\mathbf x_{jt}+\alpha_{it}p_{jt}+\xi_{jt})}{\exp(\gamma_t)+\sum_{l\in\mathscr J_t}\exp(\beta_{it}\mathbf x_{lt}+\alpha_{it}p_{lt}+\xi_{lt})}\,dF(i)
$$

**(6)**（PDF 第 12 页）

$$
s_{jt}+\sum_{k\in\mathscr J^m_t}(p_{kt}-c_{kt})\,\frac{\partial s_{kt}}{\partial p_{jt}}=0
$$

说明：原页印作 $s_{jt}+\sum_{k\in\mathscr J^m_t}(p_{jt}-c_{jt})\,\partial s_{jt}/\partial p_{kt}=0$，下标写反，为作者版笔误；上式为与 BLP (3.3) 一致的正确写法

**(7)**（PDF 第 18 页）

$$
\frac{p-mc}{p}=\frac{1}{\text{elas}}=\frac{s}{p}\times\frac{1}{ds/dp}
$$

说明：原页如此；按字面 ds/dp<0 时右端为负，弹性须取绝对值，即 $(p-mc)/p=-\frac{s}{p}\big/\frac{ds}{dp}$（单产品厂商情形）

**(8)**（PDF 第 23 页）

$$
CS_t(\gamma)=\int_i\frac{1}{\alpha_{it}}\left[\log\Big(\exp(\gamma)+\sum_{j\in\mathscr J_t}\exp\big(\beta_{it}\mathbf x_{jt}+\alpha_{it}p^{(\gamma)}_{jt}+\xi_{jt}\big)\Big)-\gamma\right]dF_t(i)
$$

说明：原页如此。本文 $\alpha_{it}<0$，按字面 $1/\alpha_{it}$ 会使补偿变化为负，钱度量应除以 $-\alpha_{it}$（即 $|\alpha_{it}|$）。其后 $\widetilde{CS}_t=\frac{1}{T}\sum_{v=0}^{T}CS_t(\gamma_v)$，v 从 0 到 T 共 T+1 项，与 1/T 不一致，按文意为对 39 个年份的 $\gamma$ 取平均

### A05 GRV2018

Grigolon, Reynaert & Verboven (2018). Consumer Valuation of Fuel Costs and Tax Policy: Evidence from the European Car Market. AEJ: Economic Policy 10(3): 193-225.

原文 PDF：`D:\codex\output\blp_bundle_20261007\package\02_five_BLP_recommendations\R01_GRV2018\original.pdf`　txt：`txt\A05_GRV2018.txt`

| 式号 | PDF 页 | 印刷页 | 核对方式 |
|---|---:|---:|---|
| (1) | 6 | 198 | 本轮看图 |
| (2) | 7 | 199 | 本轮看图 |
| (3) | 8 | 200 | 本轮看图 |
| (4) | 8 | 200 | 本轮看图 |
| (5) | 8 | 200 | 本轮看图 |

**(1)**（PDF 第 6 页）

$$
u_{ijk}=x_{jk}\beta^{x}_i-\alpha_i\big(p_{jk}+\gamma\,G_{ijk}\big)+\xi_{jk}+\varepsilon_{ijk}
$$

说明：j 为车型、k 为发动机版本；$\alpha_i$ 为收入的边际效用

**(2)**（PDF 第 7 页）

$$
G_{ijk}=E\Big[\sum_{s=1}^{S}(1+r)^{-s}\,\beta^{m}_i\,e_{jk}\,g_{ks}\Big]
$$

说明：$outside u_{i00}=\varepsilon_{i00}$；$\gamma$ 为 Allcott–Wozny 的注意权重或未来估值参数，$\gamma=1$ 正确权衡，$\gamma<1$ 低估未来；$g_{ks}$ 为 s 期燃油价格（欧元/升）

**(3)**（PDF 第 8 页）

$$
G_{ijk}=\rho\,\beta^{m}_i\,e_{jk}\,g_k
$$

说明：假设油价随机游走，$E[g_{ks}]=g_k$

**(4)**（PDF 第 8 页）

$$
\rho\equiv\sum_{s=1}^{S}(1+r)^{-s}=\frac1r\Big[1-(1+r)^{-S}\Big]
$$

说明：资本化系数，取值于 [0,S]

**(5)**（PDF 第 8 页）

$$
u_{ijk}=x_{jk}\beta^{x}_i-\alpha_i\big(p_{jk}+\gamma\rho\,\beta^{m}_i e_{jk}g_k\big)+\xi_{jk}+\varepsilon_{ijk}
$$

说明：$\gamma$ 与 $\rho$ 不能与里程尺度分开识别，用里程经验分布作先验，识别的是 $\gamma\rho$

### A06 KanekoToyama2025

Kaneko & Toyama (2025). Demand Estimation with Flexible Income Effect: An Application to Pass-Through and Merger Analysis. Journal of Industrial Economics 73(1): 186-232.

原文 PDF：`D:\codex\output\blp_bundle_20261007\package\01_existing_fuel_batch\original_pdfs\P10_Kaneko2024_JIE.pdf`　txt：`txt\A06_KanekoToyama2025.txt`

| 式号 | PDF 页 | 印刷页 | 核对方式 |
|---|---:|---:|---|
| (1) | 7 | 192 | 本轮看图 |
| (2) | 7 | 192 | 本轮看图 |
| (3) | 7 | 192 | 本轮看图 |
| (4) | 7 | 192 | 本轮看图 |
| (5)–(6) | 8 | 193 | 本轮看图 |
| (7) | 8 | 193 | 本轮看图 |
| (8) | 9 | 194 | 本轮看图 |
| (10) | 9 | 194 | 本轮看图（放大核对） |

**(1)**（PDF 第 7 页）

$$
\max_{(\mathbf m,j)\in\mathbb R^{d_m}_{+}\times\mathbf J}U(\mathbf m,j)\quad\text{s.t.}\quad \mathbf P_{\mathbf m}'\mathbf m+p_j\le y_i
$$

说明：$\mathbf m$ 为连续选择的其他商品，j=0 为不购买（$p_0=0$）

**(2)**（PDF 第 7 页）

$$
V(\mathbf P_{\mathbf m},y-p_j,j)\equiv\max_{\mathbf m\in\mathbb R^{d_m}_{+}}U(\mathbf m,j)\quad\text{s.t.}\quad\mathbf P_{\mathbf m}'\mathbf m\le y_i-p_j
$$

说明：条件间接效用：对 $(\mathbf P_{\mathbf m},y-p_j)$ 零次齐次，对 $y-p_j$ 递增

**(3)**（PDF 第 7 页）

$$
U(\mathbf m,j)=v(j)+u(\mathbf m)
$$

**(4)**（PDF 第 7 页）

$$
V(\mathbf P_{\mathbf m},y-p_j,j)=v(j)+\tilde V(\mathbf P_{\mathbf m},y-p_j)
$$

说明：其后以计价物处理：$\tilde V(P^m,y-p_j)=u\big((y-p_j)/P^m\big)$，记 $f(y-p_j)\equiv\tilde V(P^m,y-p_j)$，只要求弱递增

**(5)–(6)**（PDF 第 8 页）

$$
v_{ij}=\beta'X_j+\xi_j+\varepsilon_{ij},\ j=1,\dots,J;\qquad v_{i0}=\varepsilon_{i0}
$$

**(7)**（PDF 第 8 页）

$$
V_{ij}=\begin{cases}f(y_i-p_j)+\beta'X_j+\xi_j+\varepsilon_{ij}, & j=1,\dots,J\\ f(y_i)+\varepsilon_{i0}, & j=0\end{cases}
$$

说明：准线性特例 $V_{ij}=\alpha(y_i-p_j)+\beta'X_j+\xi_j+\varepsilon_{ij}$；BLP 特例 $V_{ij}=\alpha\ln(y_i-p_j)+\beta'X_j+\xi_j+\varepsilon_{ij}$

**(8)**（PDF 第 9 页）

$$
\mathbf J_{it}=\{0\}\cup\{j\in\{1,\dots,J_t\}:\ y_{it}-p_{jt}\ge0\}
$$

说明：预算约束决定个人选择集

**(10)**（PDF 第 9 页）

$$
s_{ijt}(y_{it})=\frac{\mathbf 1\{y_{it}\ge p_{jt}\}\exp\big(f(y_{it}-p_{jt})+\beta'X_{jt}+\xi_{jt}\big)}{\exp(f(y_{it}))+\sum_{k=1}^{J_t}\mathbf 1\{y_{it}\ge p_{kt}\}\exp\big(f(y_{it}-p_{kt})+\beta'X_{kt}+\xi_{kt}\big)}
$$

说明：原页分母最后一项印作 $\xi_{jt}$，应为 $\xi_{kt}$（求和下标为 k），排印笔误

### A09 BKL2024

Barwick, Kwon & Li (2024). Attribute-Based Subsidies and Market Power: An Application to Electric Vehicles. NBER Working Paper w32264 (March 2024).

原文 PDF：`D:\codex\output\blp_bundle_20261007\package\01_existing_fuel_batch\original_pdfs\P02_w32264.pdf`　txt：`txt\A09_BKL2024.txt`

| 式号 | PDF 页 | 印刷页 | 核对方式 |
|---|---:|---:|---|
| (8) | 20 | 18 | 本轮看图 |
| (9) | 22 | 20 | 本轮看图 |
| (10) | 22 | 20 | 本轮看图 |
| （固定成本，未编号） | 22 | 20 | 本轮看图 |
| （拉格朗日函数，未编号） | 23 | 21 | 本轮看图 |
| (11) | 23 | 21 | 本轮看图 |
| (12) | 23 | 21 | 本轮看图 |
| (13) | 23 | 21 | 本轮看图 |
| (14) | 26 | 24 | 本轮看图 |

**(8)**（PDF 第 20 页）

$$
u_{ijmt}=-\alpha_i(\tilde P_{jmt}-b_{jmt})+x_{jmt}\beta_i+\xi_{jmt}+\varepsilon_{ijmt}
$$

说明：$outside u_{i0mt}=0$；$\beta_{ik}=\bar\beta_k+\sigma_k\nu_{ik}$；$\alpha_i=\exp(\alpha_1+\alpha_2\log(y_{im})+\sigma_p\nu_{ip})$；$b_{jmt}$ 为中央与地方补贴

**(9)**（PDF 第 22 页）

$$
D_j(k_j,w_j)=\eta_k k_j+\eta_w w_j+\kappa_j
$$

说明：续航技术前沿：续航 D 对电池容量 k 与净车重 w 线性；$\kappa_j$ 含电机效率、风阻等；用全部工信部送检车型（含未上市）单独估计

**(10)**（PDF 第 22 页）

$$
mc_j(k_j,w_j)=\mathbb 1\{EV_j\}\cdot\rho^{t}\gamma_k\,k_j+\gamma_w\,w_j+G_j'\gamma_g+\omega_j
$$

说明：$\rho^t$ 为每 kWh 电池成本的逐年下降（$\rho=0.9$ 即每年降 10%），是 $\rho$ 的 t 次方而非下标

**（固定成本，未编号）**（PDF 第 22 页）

$$
\frac{\partial FC_j}{\partial k_j}=\phi_k+FE+\nu^k_j,\qquad \frac{\partial FC_j}{\partial w_j}=\phi_w+FE+\nu^w_j
$$

说明：沿 Fan (2013)

**（拉格朗日函数，未编号）**（PDF 第 23 页）

$$
\mathscr L_f=\sum_{j\in J_f}\pi_j(\boldsymbol P,\boldsymbol k,\boldsymbol w,\boldsymbol b)-\sum_{j\in J_f}FC(k_j,w_j)+\sum_{j\in J_f}\lambda_j\big[D_j(k_j,w_j)-D_c\big]
$$

说明：$\lambda_j$ 为放松续航约束的影子价值，$D_j=D_c$（卡在补贴门槛）时为正，否则为零

**(11)**（PDF 第 23 页）

$$
\text{价格：}\ Q_j+\sum_{l\in J_f}(P_l-mc_l)\frac{\partial Q_l}{\partial P_j}=0,\ \forall j
$$

**(12)**（PDF 第 23 页）

$$
\text{电池容量：}\ \sum_{l\in J_f}(P_l-mc_l)\frac{\partial Q_l}{\partial k_j}=\underbrace{\rho^{t}\gamma_k}_{\partial mc_j/\partial k_j}Q_j-\lambda_j\underbrace{\eta_k}_{\partial D_j/\partial k_j}+\underbrace{\phi_k+FE+\nu^k_j}_{\partial FC_j/\partial k_j},\ \forall j
$$

**(13)**（PDF 第 23 页）

$$
\text{车重：}\ \sum_{l\in J_f}(P_l-mc_l)\frac{\partial Q_l}{\partial w_j}=\underbrace{\gamma_w}_{\partial mc_j/\partial w_j}Q_j-\lambda_j\underbrace{\eta_w}_{\partial D_j/\partial w_j}+\underbrace{\phi_w+FE+\nu^w_j}_{\partial FC_j/\partial w_j},\ \forall j
$$

**(14)**（PDF 第 26 页）

$$
E[\omega_j\mid W_j]=0,\qquad E[\nu^k_j\mid W_j]=0,\qquad E[\nu^w_j\mid W_j]=0
$$

说明：$\lambda_j$ 不可观测，作者两种处理：加松弛参数 $E[\lambda_j\mid W_j]$，或设 $\lambda_j\simeq\zeta\,Q_j$（$\lambda_j>0$ 时）；成本参数 $(\rho,\gamma,\phi,\zeta)$ 用 (10)(12)(13) 联合 GMM

### A10 Remmy2026

Remmy (2026). Adjustable Product Attributes, Indirect Network Effects, and Subsidy Design: The Case of Electric Vehicles. AEJ: Economic Policy 18(2): 107-140. 本地为作者版

原文 PDF：`D:\auto-demand-lit-2026-09\原文PDF\J01_Remmy_2026_AEJEP_author.pdf`　txt：`txt\A10_Remmy2026.txt`

| 式号 | PDF 页 | 印刷页 | 核对方式 |
|---|---:|---:|---|
| (1) | 12 | 12 | 本轮看图 |
| (2) | 14 | 14 | 本轮看图 |
| (3) | 14 | 14 | 本轮看图 |
| (4) | 14 | 14 | 本轮看图 |
| (5) | 15 | 15 | 本轮看图 |
| (6) | 15 | 15 | 本轮看图 |
| (7) | 15 | 15 | 本轮看图 |

**(1)**（PDF 第 12 页）

$$
u_{ijmt}=\underbrace{\beta^{b}_iBEV_j+\beta^{p}_iPHEV_j+\beta^{r}_ir_{jt}+\beta^{d}\log(d_{jmt})}_{\text{仅电动车}}\ \underbrace{-\,\alpha\frac{p_{jt}}{y_{imt}}+x_{jmt}\beta^{x}_i+\xi_{jmt}+\varepsilon_{ijmt}}_{\text{全部车型}}
$$

说明：市场为州 m × 年 t；$r_{jt}$ 为续航，$d_{jmt}$ 为充电站数，价格以 p/y 进入

**(2)**（PDF 第 14 页）

$$
\max_{p,r}\ \pi_{ft}\equiv\sum_{j\in\mathcal J_{ft}}\big(p_{jt}+\lambda_{jt}-mc_{jt}(r_{jt},w_{jt};\theta_s)\big)\,s_{jmt}(p,r,d,x,\xi;\sigma)\,\mathcal M_{mt}
$$

说明：原页如此。正文说利润是各州利润的加权和，式中却没有对 m 求和；(3)(4) 中有 $\sum_m\phi_{mt}$，按文意 (2) 应含 $\sum_m$。$\lambda_{jt}$ 为补贴，厂商收到 $p_{jt}+\lambda_{jt}$

**(3)**（PDF 第 14 页）

$$
\frac{\partial\pi_{ft}}{\partial p_{jt}}=\sum_m\phi_{mt}\Big\{s_{jmt}+\sum_{k\in\mathcal J_{ft}}\big(p_{kt}+\lambda_{kt}-mc_{kt}\big)\frac{\partial s_{kmt}}{\partial p_{jt}}\Big\}=0
$$

说明：$\phi_{mt}=\mathcal M_{mt}/\sum_{m'}\mathcal M_{m't}$

**(4)**（PDF 第 14 页）

$$
\frac{\partial\pi_{ft}}{\partial r_{jt}}=\sum_m\phi_{mt}\Big\{-\frac{\partial mc_{jt}}{\partial r_{jt}}s_{jmt}+\sum_{k\in\mathcal J_{ft}}\big(p_{kt}+\lambda_{kt}-mc_{kt}\big)\frac{\partial s_{kmt}}{\partial r_{jt}}\Big\}=0
$$

说明：续航的一阶条件：加价被续航成本挤压（集约边际）对比续航带来的需求（扩展边际）与对自家其他产品的蚕食

**(5)**（PDF 第 15 页）

$$
\pi_{mt}=Q^{EV}_{mt}\,\underbrace{\frac{\mathcal D(p^{e}(d_{mt}))\,(p^{e}-c^{e})}{d_{mt}}}_{\equiv\vartheta(d_{mt})}
$$

说明：充电站进入（沿 Springel 2021）；$Q^{EV}$ 为在用电动车存量

**(6)**（PDF 第 15 页）

$$
-F_{mt}+\rho\pi_{m,t+1}+\rho^2\pi_{m,t+2}+\dots=-\rho F_{m,t+1}+\rho^2\pi_{m,t+2}+\rho^3\pi_{m,t+3}+\dots
$$

说明：自由进入：t 期与 t+1 期进入无差异。原文称 $\rho$ 为 discount rate，按式中用法它是贴现因子

**(7)**（PDF 第 15 页）

$$
\log(\vartheta(d_{mt}))=-\log(\rho)-\log(Q^{EV}_{mt})+\log\big(F_{mt}-\rho F_{m,t+1}\big)
$$

说明：原页如此。由 (6) 直接得到的是 $\rho\pi_{m,t+1}=F_{mt}-\rho F_{m,t+1}$，即左侧与 $Q^{EV}$ 应为 t+1 期；原式时序下标不一致，使用时按入场年份统一。其后设 $\vartheta(d_{mt})=(\kappa d_{mt})^{\iota}$

### A11 AleChilet2026

Alé-Chilet, Chen, Li & Reynaert (2026). Colluding Against Environmental Regulation. Review of Economic Studies 93(1): 35-71.

原文 PDF：`D:\auto-demand-lit-2026-09\原文PDF\J10_AleChilet_2026_REStud_journal.pdf`　txt：`txt\A11_AleChilet2026.txt`

| 式号 | PDF 页 | 印刷页 | 核对方式 |
|---|---:|---:|---|
| (1) | 6 | 40 | 本轮看图 |
| (2) | 6 | 40 | 本轮看图 |
| (3) | 6 | 40 | 本轮看图 |
| (4) | 7 | 41 | 本轮看图 |
| (7) | 18 | 52 | 本轮看图 |
| (8) | 18 | 52 | 本轮看图 |
| (9) | 18 | 52 | 本轮看图 |
| (13) | 21 | 55 | 本轮看图 |
| (14) | 21 | 55 | 本轮看图 |
| (15) | 21 | 55 | 本轮看图 |
| (16) | 21 | 55 | 本轮看图 |

**(1)**（PDF 第 6 页）

$$
\pi_f(\boldsymbol a^J)-\mathbb EK_f(\boldsymbol a^J)-\mathbb EA_f(\boldsymbol a^J)\ \ge\ \pi_f(\boldsymbol a^N)-\mathbb EK_f(\boldsymbol a^N)
$$

说明：参与约束；$\mathbb EK_f(\boldsymbol a)\equiv P_f(\boldsymbol a)K_f(\boldsymbol a)$ 为预期违规罚金，$\mathbb EA_f$ 为预期反垄断罚金

**(2)**（PDF 第 6 页）

$$
\pi_f(\boldsymbol a^N)-\mathbb EK_f(\boldsymbol a^N)\ \ge\ \pi_f(a^J_f,\boldsymbol a^N_{-f})-\mathbb EK_f(a^J_f,\boldsymbol a^N_{-f})
$$

说明：非合作均衡的定义

**(3)**（PDF 第 6 页）

$$
\mathbb EK_f(a^J_f,\boldsymbol a^N_{-f})-\mathbb EK_f(\boldsymbol a^J)\ \ge\ \pi_f(a^J_f,\boldsymbol a^N_{-f})-\pi_f(\boldsymbol a^J)
$$

说明：命题 1

**(4)**（PDF 第 7 页）

$$
\pi_f(\boldsymbol a^J)-\mathbb EK_f(\boldsymbol a^J)-\mathbb EA_f(\boldsymbol a^J)\ \ge\ \pi_f(a^J_f,\boldsymbol a^N_{-f})-\mathbb EK_f(a^J_f,\boldsymbol a^N_{-f})
$$

**(7)**（PDF 第 18 页）

$$
U_{ij}=\delta_j+\mu_{ij}+\bar\varepsilon_{ij}
$$

说明：$outside u_{i0}=\bar\varepsilon_{i0}$；$\bar\varepsilon_{ij}$ 按 Cardell (1997) 的嵌套 logit 分布，十个车身尺寸组 $c=0,\dots,9$

**(8)**（PDF 第 18 页）

$$
\delta_j=\alpha p_j+x_j(a_j)\beta+\xi_j
$$

说明：减排选择 $a_j$（尿素罐容积）经后备箱空间等特征 $x_j(a_j)$ 进入效用

**(9)**（PDF 第 18 页）

$$
\mu_{ij}=\sigma_p p_j\nu_{ip}+\sum_k\sigma_k x_{jk}(a_{jk})\nu_{ik}
$$

说明：$\nu_{ip},\nu_{ik}$ 为标准正态

**(13)**（PDF 第 21 页）

$$
\boldsymbol{mc}=\boldsymbol p-\big(\Omega\odot S(\boldsymbol a,\boldsymbol p)\big)^{-1}\boldsymbol s,\qquad S_{jh}=-\frac{\partial s_h(\boldsymbol a,\boldsymbol p)}{\partial p_j}
$$

说明：原页印作 $\boldsymbol{mc}=\boldsymbol p+(\Omega\odot S(\boldsymbol a,\boldsymbol p))^{-1}\boldsymbol s$。在原文自己的定义 $S_{jh}=-\partial s_h/\partial p_j$ 下，$(\Omega\odot S)^{-1}s$ 是正的加价，加号是笔误，照抄会得到 mc>p；上式为正确写法，等价于 $\boldsymbol p+(\Omega\odot J^{\top})^{-1}\boldsymbol s$（$J_{jh}=\partial s_j/\partial p_h$）

**(14)**（PDF 第 21 页）

$$
mc_j=\eta_x x_j+\eta_a a_j+\eta_{wg}\,a_j\,WG_j+\omega_j
$$

说明：$WG_j$ 为工作组（合谋）成员虚拟变量

**(15)**（PDF 第 21 页）

$$
\mathbb EK_f(a^J_f,\boldsymbol a^N_{-f})\ \ge\ \mathbb E\pi_f(a^J_f,\boldsymbol a^N_{-f})-\mathbb E\pi_f(\boldsymbol a^N)+\mathbb EK_f(\boldsymbol a^N)
$$

说明：单方低减排时预期罚金的下界

**(16)**（PDF 第 21 页）

$$
\mathbb EK_f(\boldsymbol a^J)+\mathbb EA_f(\boldsymbol a^J)\ \le\ \mathbb E\pi_f(\boldsymbol a^J)-\mathbb E\pi_f(\boldsymbol a^N)+\mathbb EK_f(\boldsymbol a^N)
$$

说明：合谋方案下预期罚金的上界

### A14 GHvB2021

Gillingham, Houde & van Benthem (2021). Consumer Myopia in Vehicle Purchases: Evidence from a Natural Experiment. AEJ: Economic Policy 13(3): 207-238.

原文 PDF：`D:\codex\output\blp_bundle_20261007\package\01_existing_fuel_batch\original_pdfs\P15_Gillingham2021_Myopia.pdf`　txt：`txt\A14_GHvB2021.txt`

| 式号 | PDF 页 | 印刷页 | 核对方式 |
|---|---:|---:|---|
| (1) | 7 | 213 | 本轮看图 |
| (2) | 16 | 222 | 本轮看图 |
| （表 7 的换算，派生） | 23 | 229 | 派生 [D] |

**(1)**（PDF 第 7 页）

$$
Price_{jrt}=\beta\,\mathbf 1(\text{Post Restatement})_t\times\mathbf 1(\text{Affected Model})_j+\rho_{t\times Class_j}+\mu_{t\times Make_j}+\eta_r\times\mathbf 1(\text{Post Restatement})_t+\eta_r+\omega_j+\epsilon_{jrt}
$$

说明：Price 取对数或水平；j 为 VIN10，r 为 DMA，t 为年月；重标在 2012 年 11 月。表 2 第 (6) 列水平值 −294（91）

**(2)**（PDF 第 16 页）

$$
Price_{jrt}=\gamma\,\Delta G_{jt}+\rho_{t\times Class_j}+\mu_{t\times Make_j}+\eta_r\times\mathbf 1(\text{Post Restatement})_t+\eta_r+\omega_j+\epsilon_{jrt}
$$

说明：$\Delta G_{jt}$ 为重标引起的贴现生命周期燃油成本变化（非受影响车型与重标前为 0）。销量不调整时 $\gamma=-1$ 为完全估值；表 6（PDF 第 18 页）4% 贴现率下 2011–2012 年款 −0.39、2013 年款 −0.16

**（表 7 的换算，派生）**（PDF 第 23 页）

$$
\Delta WTP=\Delta P-P_0\,\frac{\Delta Q/Q}{\eta_D},\qquad \Delta P=-294,\ P_0=24{,}500
$$

说明：期刊正文未印此式（原式在本地没有的在线附录 D.3）。该式由表 7 六个格子反推，能复现 498/600、335/355、90/−12（表中报的是 $-\Delta WTP$）；它与 NBER 工作论文版脚注 26 的 $\Delta P+\Delta P\times\Delta Q/\eta_D$ 不同，后者见 A14b

### A14b GHvB2019WP

Gillingham, Houde & van Benthem (2019). Consumer Myopia in Vehicle Purchases: Evidence from a Natural Experiment. NBER Working Paper w25845（A14 的工作论文版，含表 D.1 与脚注 26）

原文 PDF：`C:\Users\于舒奕\Downloads\w25845.pdf`　txt：`txt\A14b_GHvB2019WP.txt`

| 式号 | PDF 页 | 印刷页 | 核对方式 |
|---|---:|---:|---|
| 脚注 26（原印刷） | 50 | 48 | 本轮看图 |
| 表 D.1（原印刷） | 52 | 50 | 本轮看图 |

**脚注 26（原印刷）**（PDF 第 50 页）

$$
\text{total WTP}=\Delta P+\Delta P\times\frac{\Delta Q}{\eta_D}
$$

说明：原页确实如此印刷。该式与同文表 D.1 不一致：按此式各格都约等于 294，而表 D.1 从 −9 到 597。判断为原文笔误，不要照抄

**表 D.1（原印刷）**（PDF 第 52 页）

$$
\Delta Q/Q=-5\%:\ 496/597;\quad -1\%:\ 334/355;\quad 0:\ 294/294;\quad +1\%:\ 254/233;\quad +5\%:\ 92/-9\qquad(\eta_D=-6\,/\,-4)
$$

说明：表注写所用价格为改革前 24,500，但十个格子恰好由 $\Delta WTP=\Delta P-P_1(\Delta Q/Q)/\eta_D$、$P_1=24{,}500-294=24{,}206$ 复现（误差 ≤1 美元）；期刊版表 7 则用 $P_0=24{,}500$。两版价格水平不同，不能混用

### A15 ReynaertSallee2021

Reynaert & Sallee (2021). Who Benefits When Firms Game Corrective Policies? AEJ: Economic Policy 13(1): 372-412.

原文 PDF：`D:\codex\output\blp_bundle_20261007\package\02_five_BLP_recommendations\R02_Reynaert_Sallee2021\original.pdf`　txt：`txt\A15_ReynaertSallee2021.txt`

| 式号 | PDF 页 | 印刷页 | 核对方式 |
|---|---:|---:|---|
| （未编号，信念设定） | 18 | 389 | 本轮看图（放大核对） |

**（未编号，信念设定）**（PDF 第 18 页）

$$
g=x-m,\qquad \tilde x_t=\alpha x+(1-\alpha)(x-g)=x-(1-\alpha)g
$$

说明：x 为真实油耗（坏属性），m 为卖方发出的信息即官方标称值，g 为博弈（gaming）量。$\alpha=1$ 时买方完全识破，$\alpha=0$ 时完全被骗。原页式中写作 $\tilde x_t$（带下标 t），正文称 $\tilde x$，下标疑为排印残留。其前：$\beta=(p_f+\tau)\times k$，全信息需求 $D(f)=D(p+\beta x)$，感知 $\tilde f=p+\beta\tilde x$；成本 c(x) 满足 c'<0,c''>0，博弈成本 h(g) 满足 h'>0,h''>0；规制 $m=x-g\le\sigma$

### A16 XingLeardLi2021

Xing, Leard & Li (2021). What Does an Electric Vehicle Replace? Journal of Environmental Economics and Management 107: 102432.

原文 PDF：`D:\codex\output\blp_bundle_20261007\package\02_five_BLP_recommendations\R04_Xing_Leard_Li2021\original.pdf`　txt：`txt\A16_XingLeardLi2021.txt`

| 式号 | PDF 页 | 印刷页 | 核对方式 |
|---|---:|---:|---|
| (12) | 8 | 8 | 本轮看图 |
| (13) | 9 | 9 | 本轮看图 |
| (14) | 9 | 9 | 本轮看图 |
| (15) | 9 | 9 | 本轮看图 |
| (10)–(11) | 8 | 8 | 本轮看图 |

**(12)**（PDF 第 8 页）

$$
u_{ij}=\underbrace{\sum_{k=1}^{K}x_{jk}\bar\beta_k-\alpha_1\ln p_j+\xi_j}_{\delta_j}+\underbrace{\alpha_2\frac{\ln p_j}{Y_i}+\sum_{kr}x_{jk}z_{ir}\beta^{o}_{kr}+\sum_k x_{jk}\nu_{ik}\beta^{u}_k}_{\mu_{ij}}+\varepsilon_{ij}
$$

说明：$Y_i$ 为收入，$z_{ir}$ 为其他人口特征，$\nu_{ik}$ 标准正态

**(13)**（PDF 第 9 页）

$$
P_{ijh}=\int\frac{\exp[\delta_j(\theta)+\mu_{ij}(\theta)]}{\sum_g\exp[\delta_g(\theta)+\mu_{ig}(\theta)]}\cdot\frac{\exp[\delta_h(\theta)+\mu_{ih}(\theta)]}{\sum_{g\ne j}\exp[\delta_g(\theta)+\mu_{ig}(\theta)]}\,f(\nu)\,d\nu
$$

说明：首选 j、次选 h 的联合概率：两个概率在同一个 $\nu$ 下相乘后再积分，不能等于两个边际积分之积

**(14)**（PDF 第 9 页）

$$
\ln L=\sum_{i=1}^{N}\ln R_i,\qquad \ln R_i=\ln P_{ijh}
$$

说明：最大似然估计非线性参数

**(15)**（PDF 第 9 页）

$$
\delta^{t}_j(\theta,S)=\delta^{t-1}_j(\theta,S)+\ln(S_j)-\ln\big(\hat S_j(\theta,\delta^{t-1}(\theta,S))\big)
$$

说明：内层容差 1E-15；反演后 $\delta_j=-\alpha_1\ln p_j+\sum_k x_{jk}\bar\beta_k+\xi_j$，再用 BLP 型工具估线性参数

**(10)–(11)**（PDF 第 8 页）

$$
\frac{dN}{ds'}=\frac{q_1(p^{0}_1)}{q_1(p_1)}\,\epsilon_1,\qquad \left.\frac{dN}{ds'}\right|_{p^0_1=p_1}=\epsilon_1
$$

说明：补贴的非新增购买与 EV 自价格弹性 $\epsilon_1$ 成正比（第 3 节理论部分）

### A20 Ji2026

Ji, Wang, Zheng & Fan (2026). 中国新能源汽车补贴的 BLP 评估（人口特征交互）. JAERE 13(1).

原文 PDF：`D:\blp-lit-recommend-20261002\package_20261008\03_人口特征交互_Ji2026_JAERE\Ji2026_原文.pdf`　txt：`txt\A20_Ji2026.txt`

| 式号 | PDF 页 | 印刷页 | 核对方式 |
|---|---:|---:|---|
| (1) | 10 | 10 | 沿用 09-25 看图核验 |
| (2) | 11 | 11 | 本轮看图 |
| (3) | 11 | 11 | 本轮看图 |
| (4) | 12 | 12 | 本轮看图 |
| (5) | 12 | 12 | 本轮看图 |
| (6) | 13 | 13 | 沿用 09-25 看图核验 |

**(1)**（PDF 第 10 页）

$$
u_{ijt}=\alpha_{it}\ln(p_{jt})+\sum_{k=1}^{K}x_{jkt}\beta_{ikt}+\xi_{jt}+\epsilon_{ijt}
$$

说明：$p_{jt}$ 为税、补贴、强制保险调整后的有效消费者价格；$outside u_{i0t}=\epsilon_{i0t}$

**(2)**（PDF 第 11 页）

$$
\alpha_{it}=-e^{\alpha_1+\alpha_2\ln(y_{it})+\sigma_p\nu_{ipt}}
$$

**(3)**（PDF 第 11 页）

$$
\begin{cases}\beta_{ikt}=\bar\beta_k+\sigma_k\nu_{ikt}\\ \xi_{jt}=\gamma_1\zeta_{bev\text{-}dummy}t+\gamma_2\zeta_{phev\text{-}dummy}t+\gamma_3\zeta_{ev\text{-}dummy}\log(\text{EDR/Weight})+\gamma_4\zeta_{suv\text{-}dummy}+\gamma_5\zeta_{mpv\text{-}dummy}+\gamma_6\zeta_{year\text{-}FE}+\gamma_7\zeta_{quarter\text{-}FE}+\gamma_8\zeta_{firm\text{-}FE}+\Delta\xi_{jt}\end{cases}
$$

说明：$\nu_{ikt}\sim N(0,I_K)$

**(4)**（PDF 第 12 页）

$$
u_{ijt}(\theta)=\delta_{jt}(\theta_1)+\mu_{ijt}(\theta_2)+\epsilon_{ijt}
$$

**(5)**（PDF 第 12 页）

$$
\delta_{jt}(\theta_1)=\sum_{k=1}^{K}x_{jkt}\bar\beta_k+\xi_{jt},\qquad \mu_{ijt}(\theta_2)=\alpha_{it}\ln(p_{jt})+\sum_{k=1}^{K}x_{jkt}(\sigma_k\nu_{ikt})
$$

说明：原文随后写 $\theta_2=(\alpha_1,\alpha_2,\alpha_p,\sigma_k)$，其中 $\alpha_p$ 与式 (2) 的 $\sigma_p$ 记号不一，按 (2) 应为 $\sigma_p$

**(6)**（PDF 第 13 页）

$$
s_{jt}(\theta_1,\theta_2)=\int\frac{e^{\delta_{jt}+\mu_{ijt}}}{1+\sum_{k=1}^{J_t}e^{\delta_{kt}+\mu_{ikt}}}\,dP(\nu)
$$

### A21 BKLZ2025

Barwick, Kwon, Li & Zahur (2025). Drive Down the Cost: Learning by Doing and Government Policies in the Global EV Battery Industry. NBER Working Paper w33378 (Revised Aug 2025).

原文 PDF：`D:\codex\output\blp_bundle_20261007\package\01_existing_fuel_batch\original_pdfs\P01_w33378.pdf`　txt：`txt\A21_BKLZ2025.txt`

| 式号 | PDF 页 | 印刷页 | 核对方式 |
|---|---:|---:|---|
| (1) | 13 | 11 | 本轮看图 |
| (2) | 13 | 11 | 本轮看图 |
| （整车利润与 (3)） | 14 | 12 | 本轮看图 |
| （纳什乘积与 (4)） | 15 | 13 | 本轮看图 |
| （价格系数） | 18 | 16 | 本轮看图 |
| (7) | 20 | 18 | 本轮看图 |

**(1)**（PDF 第 13 页）

$$
p_{jct}=\underbrace{mc^{b}_{jct}}_{\text{电池成本}}+\underbrace{mc^{v}_{jct}}_{\text{非电池成本}}+\underbrace{mk^{b}_{jct}}_{\text{电池加价}}+\underbrace{mk^{v}_{jct}}_{\text{整车加价}}
$$

**(2)**（PDF 第 13 页）

$$
U_{ijct}=\alpha_i(p_{jct}-\phi_{jct})+\mathbf X_{jct}\boldsymbol\beta_i+\xi_{jct}+\varepsilon_{ijct}
$$

说明：$\phi_{jct}$ 为中央政府消费者补贴。原文此处写 consumer i in county c，全文其余处为 country c，county 疑为笔误

**（整车利润与 (3)）**（PDF 第 14 页）

$$
\pi^{v}(\mathbf p)=\sum_{j\in\Omega_v}(p_j-\tau_j-mc^{v}_j)\,q_j(\mathbf p,\phi);\qquad q_j+\sum_{k\in\Omega_v}\underbrace{(p_k-\tau_k-mc^{v}_k)}_{mk^{v}_k}\frac{\partial q_k}{\partial p_j}=0\ \ (3)
$$

说明：$\tau_j$ 为电池价格；脚注 11：合资企业与其中方母公司视为不同厂商

**（纳什乘积与 (4)）**（PDF 第 15 页）

$$
NP_j(\tau_j,\tau_{-j})=(\pi^{v}-d^{v})^{(1-\lambda^{b})}(\pi^{b}-d^{b})^{\lambda^{b}};\qquad (1-\lambda^{b})(\pi^{b}-d^{b})\frac{\partial\pi^{v}}{\partial\tau_j}+\lambda^{b}(\pi^{v}-d^{v})\frac{\partial\pi^{b}}{\partial\tau_j}=0\ \ (4)
$$

说明：$\pi^{b}(\tau)=\sum_{j\in\Omega_b}(\tau_j-mc^{b}_j)q_j(\mathbf p,\phi)$，$\lambda^b\in(0,1)$ 为电池供应商的议价权重；脚注 14：电池化学体系与能量密度可因车型而异

**（价格系数）**（PDF 第 18 页）

$$
\alpha_i=\alpha_1+\frac{\alpha_{c(i)}}{y_i}+\sigma_p\nu^{p}_i
$$

说明：按人均收入把国家分四组，$\alpha_{c(i)}$ 随组变化；前瞻版纳什乘积把 $\pi^{b}-d^{b}$ 换成 $V^{b}-D^{b}$

**(7)**（PDF 第 20 页）

$$
mc^{b}_{jct}=BK_{bjct}\Big(\underbrace{\gamma_0E_{bt}^{\gamma_E}+CH_{bjct}\gamma_1+PK_{bt}\gamma_2+\eta\, t}_{\text{每 kWh 成本}}\Big)
$$

说明：BK 为电池容量（kWh），$E_{bt}=\sum_{s<t}\sum_c\sum_{j\in\mathscr I\{I_{bcs}=1\}}q_{jcs}$ 为供应商累计产量（干中学），学习率 $1-2^{\gamma_E}$；CH 为电池化学类型，PK 为工厂产能。同页 $mk^{b}_{jct}=\frac{\lambda^b}{1-\lambda^b}\overline{mk}^{b}_{jct}$；正文把非电池成本写作 $mc^{c}_{jct}$，与 (1) 的 $mc^{v}_{jct}$ 记号不一

### M01 ConlonGortmaker2020

Conlon & Gortmaker (2020). Best Practices for Differentiated Products Demand Estimation with PyBLP. RAND Journal of Economics 51(4): 1108-1161.

原文 PDF：`D:\codex\research-memory\deep-reading\blp40s_20260403\pdfs\30_bfp23mj2.pdf`　txt：`txt\M01_ConlonGortmaker2020.txt`

| 式号 | PDF 页 | 印刷页 | 核对方式 |
|---|---:|---:|---|
| (2) | 5 | 5 | 本轮看图 |
| (3) | 5 | 5 | 本轮看图 |
| (4) | 5 | 5 | 本轮看图 |
| （标量 FOC 与 (5)） | 5 | 5 | 本轮看图 |
| (6) | 6 | 6 | 本轮看图 |
| (7) | 6 | 6 | 本轮看图 |
| (8) | 6 | 6 | 本轮看图 |
| (26) | 19 | 19 | 本轮看图 |
| (27) | 19 | 19 | 本轮看图 |

**(2)**（PDF 第 5 页）

$$
d_{ijt}=\begin{cases}1 & U_{ijt}>U_{ikt}\ \forall k\ne j\\ 0 & \text{otherwise}\end{cases},\qquad s_{jt}=\int d_{ijt}(\boldsymbol\delta_t,\boldsymbol\mu_{it})\,d\boldsymbol\mu_{it}\,d\boldsymbol\epsilon_{it}
$$

说明：$outside U_{i0t}=\epsilon_{i0t}$

**(3)**（PDF 第 5 页）

$$
s_{jt}(\boldsymbol\delta_t,\tilde\theta_2)=\int\frac{\exp(\delta_{jt}+\mu_{ijt})}{\sum_{k\in J_t}\exp(\delta_{kt}+\mu_{ikt})}\,f(\boldsymbol\mu_{it}\mid\tilde\theta_2)\,d\boldsymbol\mu_{it}
$$

说明：其后 $\boldsymbol\delta_t\equiv D_t^{-1}(\boldsymbol{\mathcal S}_t,\tilde\theta_2)$；脚注 10：logit 时 $D^{-1}=\log s_{jt}-\log s_{0t}$，嵌套 logit 时 $D^{-1}=\log s_{jt}-\log s_{0t}-\rho\log s_{j|ht}$

**(4)**（PDF 第 5 页）

$$
\delta_{jt}(\boldsymbol{\mathcal S}_t,\tilde\theta_2)=[x_{jt},v_{jt}]\beta-\alpha p_{jt}+\xi_{jt}
$$

说明：矩条件 $E[\xi_{jt}Z^D_{jt}]=0$

**（标量 FOC 与 (5)）**（PDF 第 5 页）

$$
s_{jt}(\boldsymbol p_t)+\sum_{k\in J_{ft}}\frac{\partial s_{kt}}{\partial p_{jt}}(\boldsymbol p_t)\,(p_{kt}-c_{kt})=0;\qquad \boldsymbol s_t(\boldsymbol p_t)=\Delta_t(\boldsymbol p_t)(\boldsymbol p_t-\boldsymbol c_t),\quad \underbrace{\Delta_t(\boldsymbol p_t)^{-1}\boldsymbol s_t(\boldsymbol p_t)}_{\boldsymbol\eta_t(\boldsymbol p_t,\boldsymbol s_t,\theta_2)}=\boldsymbol p_t-\boldsymbol c_t\ \ (5)
$$

**(6)**（PDF 第 6 页）

$$
\Delta_t(\boldsymbol p_t)\equiv-\mathcal H_t\odot\frac{\partial\boldsymbol s_t}{\partial\boldsymbol p_t}(\boldsymbol p_t),\qquad (j,k)\text{ 元为 }\partial s_{jt}/\partial p_{kt}
$$

说明：注意：按 $(j,k)=\partial s_{jt}/\partial p_{kt}$ 拼成的 $\Delta$ 与上式标量 FOC（用 $\partial s_{kt}/\partial p_{jt}$）差一次转置，与 BLP (3.4) 的 $\Delta_{jr}=-\partial s_r/\partial p_j$ 也差一次转置。只有需求 Jacobian 对称（准线性价格的混合 logit）时两者相同；收入效应规格下须按 BLP 方向实现

**(7)**（PDF 第 6 页）

$$
f_{MC}\big(p_{jt}-\eta_{jt}(\theta_2)\big)=f_{MC}(c_{jt})=x_{jt}\gamma_1+w_{jt}\gamma_2+\omega_{jt}
$$

说明：$c_{jt}=p_{jt}-\eta_{jt}(\theta_2)$；矩条件 $E[\omega_{jt}Z^S_{jt}]=0$；$f_{MC}$ 常取恒等或对数

**(8)**（PDF 第 6 页）

$$
g(\theta)=\begin{bmatrix}g_D(\theta)\\ g_S(\theta)\end{bmatrix}=\begin{bmatrix}\frac1N\sum_{j,t}\xi_{jt}Z^D_{jt}\\ \frac1N\sum_{j,t}\omega_{jt}Z^S_{jt}\end{bmatrix},\qquad \min_\theta\ q(\theta)\equiv g(\theta)'Wg(\theta)
$$

说明：$\theta=[\beta,\alpha,\tilde\theta_2,\gamma]$

**(26)**（PDF 第 19 页）

$$
\frac{\partial\boldsymbol s_t}{\partial\boldsymbol p_t}(\boldsymbol p_t)=\Lambda_t(\boldsymbol p_t)-\Gamma_t(\boldsymbol p_t),\quad \Lambda_{jj,t}=\int\alpha_i s_{ijt}(\boldsymbol\mu_{it})f(\boldsymbol\mu_{it}\mid\tilde\theta_2)d\boldsymbol\mu_{it},\quad \Gamma_{jk,t}=\int\alpha_i s_{ijt}(\boldsymbol\mu_{it})s_{ikt}(\boldsymbol\mu_{it})f(\boldsymbol\mu_{it}\mid\tilde\theta_2)d\boldsymbol\mu_{it}
$$

说明：此处 $\alpha_i=\partial u_{ijt}/\partial p_{jt}$（价格的边际负效用，取负值），与 (4) 中 $-\alpha p$ 的写法相反；同文 p.8 脚注 17 又取正号。照搬前先统一符号

**(27)**（PDF 第 19 页）

$$
\boldsymbol p_t\leftarrow\boldsymbol c_t+\boldsymbol\zeta_t(\boldsymbol p_t),\qquad \boldsymbol\zeta_t(\boldsymbol p_t)=\Lambda_t(\boldsymbol p_t)^{-1}\big[\mathcal H^{*}_t\odot\Gamma_t(\boldsymbol p_t)\big](\boldsymbol p_t-\boldsymbol c_t)-\Lambda_t(\boldsymbol p_t)^{-1}\boldsymbol s_t(\boldsymbol p_t)
$$

说明：Morrow–Skerlos 定点，作者称比牛顿类方法快 3–12 倍；停止规则 $\|\Lambda(\boldsymbol p_t)(\boldsymbol p_t-\boldsymbol c_t-\boldsymbol\zeta_t(\boldsymbol p_t))\|_\infty<\text{tol}$（脚注 65）；logit 时 $\Lambda_{jj,t}=\alpha s_{jt}$（脚注 64）

## 五、近期读过但未收入的文献

| 文献 | 未收入原因 | 可用的本机材料 |
|---|---|---|
| Lu (2023)，生命周期燃油成本与里程分布 | 本机没有原文 PDF | 精读卡 `D:\codex\output\blp_driving_cycle_structural_research_20260824\iteration3_new_papers_20260824\03_pass1_cards\lu_2023_vehicle_use_heterogeneity_pass1_card.md` |
| Springel (2021) AEJ: Economic Policy，充电网络双边市场 | 本机没有原文 PDF | 卡片 `D:\codex\economics_theory_agent_complete_gpt55_xhigh\kb\04_literature\structural_papers\17-network-externality-and-subsidy-structure-in-two-sided-markets-evidence-from-electric-vehicle-incentives.md` |
| Li (2026) Energy Economics，非对称短视的随机系数 logit | 本次未在本机检索到原文 PDF | 核验记录 `D:\blp-structural-skill-config\VERIFICATION_LEDGER.md` C1–C2 |
| Miller & Weinberg (2017) Econometrica | 啤酒行业，不属汽车 | 卡片 `D:\codex\output\blp_driving_cycle_structural_research_20260824\iteration3_new_papers_20260824\03_pass1_cards\miller_weinberg_2017.md` |
| Hu 等 (2025) REStat | 本机只有摘要 | 卡片 `D:\auto-demand-lit-2026-09\cards\J04.json` |

## 六、局限

1. txt 正文是机器抽取。PDF 文字层干净的论文，正文文字可靠，但公式、表格和脚注常被拆散；Petrin (2002) 的正文是 OCR 结果，希腊字母常被误识。
2. 公式校正只覆盖核心模型式（效用、份额、反演、供给一阶条件、成本与矩条件，以及与工况项目最相关的扩展式），不是全文逐式校正；另有 10 篇未做校正，见总表中校正条数为 0 的各篇。
3. 多篇本机只有作者版或工作论文版（GMY 2024、Remmy 2026、Chou–Derdenger 2025、Petrin 2002 等），页码与正式刊不同；作者版里的笔误在正式刊中是否已改正未核。
4. Reynaert (2021) 与 Conlon–Gortmaker (2020) 是早期在线版，页码从 1 起，与正式刊页码不同。