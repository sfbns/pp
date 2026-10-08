# A06 Demand Estimation with Flexible Income Effect: An Application to Pass-Through and Merger Analysis（具有灵活收入效应的需求估计：在转嫁率与合并分析中的应用）

> 精读依据：全文 txt 第 1–2893 行逐页通读（PDF 第 1–48 页；印刷页 = PDF 页 + 185）。公式以 txt 页末【公式校正】段及总表“### A06 KanekoToyama2025”节为准；(1)–(10) 已对照原页图（PDF p7–p9），(11) 起各式**未经看图校正**，由文字层重排，存疑处已标注。txt 只含正文，**Online Appendix A–H 不在 txt 中**（收入分布构造、税制细节、逐点形状约束、连续性数值例、UPP 推导、租赁价格、CV 计算等细节均未读到）。

---

## 1. 引用信息

- **英文题目**：Demand Estimation with Flexible Income Effect: An Application to Pass-Through and Merger Analysis
- **中文译名**：具有灵活收入效应的需求估计：在转嫁率与合并分析中的应用
- **作者与单位**：Shuhei Kaneko（Department of Economics, University of California, Santa Barbara）；Yuta Toyama（Graduate School of Economics, Waseda University）
- **期刊**：The Journal of Industrial Economics, Vol. LXXIII (73), No. 1, March 2025, pp. 186–232（PDF p48 页眉印 233，为 Supporting Information 页）。共同编辑 Panle Barwick。Open Access（CC BY-NC），© 2024。
- **DOI**：10.1111/joie.12406（由页边水印 URL `onlinelibrary.wiley.com/doi/10.1111/joie.12406` 得到）
- **旧标题**：“Flexible Demand Estimation with Nonparametric Income Effect: An Application to Pass-through and Merger Analysis”
- **资助/致谢**：Waseda University Grant（2021C-421, 2022C-585, 2024C-676）、JSPS KAKENHI 22K13398；日本汽车数据由 Komei Fujita、Naoki Wakamori 提供；税、补贴与租赁价格数据由 Tatsuya Abe 协助构造。
- **APA**：Kaneko, S., & Toyama, Y. (2025). Demand estimation with flexible income effect: An application to pass-through and merger analysis. *The Journal of Industrial Economics, 73*(1), 186–232. https://doi.org/10.1111/joie.12406
- **GB/T 7714**：KANEKO S, TOYAMA Y. Demand estimation with flexible income effect: an application to pass-through and merger analysis[J]. The Journal of Industrial Economics, 2025, 73(1): 186-232. DOI:10.1111/joie.12406.
- **源 txt**：`scratchpad/txt3w/A06_KanekoToyama2025.txt`（PyMuPDF 文字层；原 PDF `P10_Kaneko2024_JIE.pdf`）；**页码换算：印刷页 = PDF 页 + 185**；核对页图仅有 `A06_p07/p08/p09(.png)` 及 p09 放大图。
- **方法类型标签**：半参数离散选择需求（semiparametric discrete choice）｜非参数收入效应 $f(y-p)$｜筛函数近似（Bernstein polynomial sieve）+ 单调形状约束（shape restriction）｜sieve GMM + BLP 嵌套不动点（NFP）｜显式预算约束（choice set）｜多产品 Bertrand–Nash 供给｜从价税/从量税/补贴楔子｜转嫁率（pass-through）｜合并模拟 + UPP｜补偿变动 CV（Dagsvik–Karlström）｜蒙特卡洛｜日本新车市场 2006–2013｜Eco-car Subsidy（feebate）。

## 2. 一句话结论

把 logit 需求中的收入效应项 $f(y_i-p_j)$ 设为只需弱递增的非参数函数，用带单调约束的 Bernstein 筛函数嵌入 BLP NFP 做 sieve GMM，用于日本汽车市场时发现：$f$ 明显非线性且凹；生态车补贴的平均转嫁率为 1.194（过度转嫁），而线性 logit 只有 0.991 且受上界 1 约束；丰田–本田假想合并的涨价幅度（+2.7%/+7.3%）远高于线性 logit（+0.6%/+1.4%），也高于参数化收入效应模型（+1.9%/+5.3%）。说明需求曲率要灵活估计。

## 3. 研究问题、背景与动机

- **核心问题**：差异化产品需求的**曲率**（二阶导）决定成本/税收转嫁率（Weyl & Fabinger 2013）和合并的价格效应（Farrell & Shapiro 2010：合并价格效应在一阶上等于机会成本上升的转嫁；Crooke et al. 1999：弹性相同但曲率不同的需求，模拟出的合并结果可能差别很大）。参数化需求会预先限定曲率（PDF p1–p2, p11–p12）。
- **准线性的局限**：$V_{ij}=\alpha(y_i-p_j)+\dots$ 中收入在比较备选项时相互抵消，需求与收入无关；简单 logit 的自价格弹性 $|\eta_{jj}|=\alpha p_j(1-s_j)$ 随价格线性上升（Nevo 2000b），越贵的车弹性越大；需求在价格上始终 log-concave，所以转嫁率 < 1（PDF p10–p11, p29）。
- **对数形式的局限**：BLP 的 $\alpha\ln(y_i-p_j)$，或 BLP(1999) 的一阶近似 $\alpha p_j/y_i$，虽然引入了收入异质性，但函数形式本身仍会限制曲率和转嫁率（PDF p9, p11）。
- **预算约束被忽视**：已有文献多数不处理 $y_i\ge p_j$ 的约束，在准线性下它无影响；Xiao et al. (2017)、Pesendorfer et al. (2023) 讨论了遗漏预算约束带来的偏误。本文把预算约束显式写进选择集（PDF p9）。
- **计量难点**：非/半参数估计在内生性下面临 ill-posed inverse problem（Horowitz 2014），估计不精确。借鉴 Chetverikov & Wilhelm (2017)，用效用最大化推出的单调性作为形状约束来提高精度（PDF p3）。
- **应用**：日本新车市场（2006–2013），两个反事实：(i) 2009 年起的生态车补贴（Eco-car Subsidy，feebate）的转嫁与福利；(ii) Toyota–Honda 假想合并（PDF p3–p4, p23）。

## 4. 文献综述（方向 → 代表文献 → 本文推进）

| 方向 | 代表文献（原文所列） | 本文推进 |
|---|---|---|
| 非/半参数需求（同质品） | Blundell et al. (2012 QE; 2017 REStat，Slutsky 约束)；Blundell, Chen & Kristensen (2007) | 扩展到差异化产品的离散选择 |
| 非参数离散选择（个体数据） | Bhattacharya (2015 Ecta，非参数福利)；Tebaldi, Torgovitsky & Yang (2019，加州医保) | 只用**市场层面加总数据**（BLP 路线） |
| 最接近文献 | Griffith, Nesheim & O'Connell (2018 QE)：灵活的**参数化**收入效应，英国人造黄油，饱和脂肪税，个体数据 | 方法上：非参数 + 形状约束的 sieve，证明约束显著提高精度；数据上：只用加总数据；用 IV 处理价格内生性；应用到汽车的转嫁与合并 |
| 参数化非线性收入效应 | Herriges & Kling (1999)、Morey et al. (2003)（个体数据，脚注 5） | 非参数化 |
| 完全非参数差异化需求 | Compiani (2021/2022 QE)；Berry & Haile (2014)：反需求为 2J 维函数（脚注 6） | 只对一维对象 $f(\cdot)$ 做非参数，适用于产品很多的市场 |
| 半参数 BLP | Wang (2022 JoE, Sieve BLP)：非参数估计随机系数分布 | 放松的是收入效应的函数形式 |
| 灵活曲率的参数模型 | Birchall, Mohapatra & Verboven (2023)：Box-Cox，放松单位需求（承 Björnerstedt & Verboven 2016），早餐谷物；Miravete, Seim & Thurk (2023)：单位需求下对收入效应取 Box-Cox 一阶近似 | 适用于**单位需求的耐用品**；$f$ 完全非参数；显式预算约束和效用最大化，可以做福利分析 |
| 转嫁的实证 | Nakamura & Zerom (2010)、Goldberg & Hellerstein (2013)、Fabra & Reguant (2014)、Hollenbeck & Uetake (2021)；理论 Weyl & Fabinger (2013) | 用供给侧模拟说明灵活曲率对税/补贴转嫁很关键；允许转嫁率 > 1 |
| 横向合并模拟 | Nevo (2000a)；脚注 7：Peters (2006) 航空、Fan (2013) 报纸、Houde (2012) 加油站、Gowrisankaran et al. (2015) 医院、Miller & Weinberg (2017) 啤酒、Ohashi & Toyama (2017) 汽车、Björnerstedt & Verboven (2016) 药品；Crooke et al. (1999)；UPP：Farrell & Shapiro (2010)、Jaffe & Weyl (2013)、Miller et al. (2016) | 在反垄断分析中提供曲率灵活的替代模型 |
| 筛估计与推断 | Chen (2007) sieve；Chetverikov & Wilhelm (2017) 单调 NPIV；Chetverikov, Kim & Wilhelm (2018) 工具矩阵；Chen & Pouzo (2015) 广义残差自助；Chen & Qiu (2016)、Chen, Christensen & Kankanala (2023) 筛阶数选择 | 证明形状约束在**不可分（non-separable）**模型中同样有效 |
| 收入效应下的福利 | McFadden (1999)；Dagsvik & Karlström (2005)；Small & Rosen (1981) | 半参数模型用 Dagsvik–Karlström 计算 CV |
| 离散-连续选择（排除） | Dubin & McFadden (1984)、Newey (2007)（脚注 8） | 本文加性可分，排除这一类；作者列为未来方向 |

## 5. 数据

- **市场与时期**：日本新车市场，**2006–2013 年**的年度数据；市场 $t$ = 年份（$T=8$）；车型×年份的非平衡面板，**1,322 个观测**（2006–2008 年 495 个，2009–2013 年 827 个，表 V）（PDF p23–p26）。
- **来源**（脚注 24–25）：车型目录与标价来自 CarView! 网站；普通车与小型车（standard/compact）登记量来自日本汽车经销商协会 *Annual Report of New Car Registrations*；轻自动车（minicar）来自日本轻自动车协会（zenkeijikyo）；进口车只有销量前 20 的车型，来自日本汽车进口商协会（JAIA）；市场规模 = 日本家庭总数（总务省 Basic Resident Register）。
- **份额**：$s_{jt}$ = 新车登记量 / 家庭总数；$s_{0t}=1-\sum_{j\in J_t}s_{jt}$。
- **特征 $X_{jt}$**：HP/WT（马力/车重）、Size（车身尺寸）、MPG（由 km/L 换算：$mpg=(fe/1.60934)\times3.78541$，脚注 26）、AT/CVT 哑变量；另有 minicar、foreign、hybrid 哑变量（minicar：长 ≤3.4 m、宽 ≤1.48 m、高 ≤2.0 m、排量 ≤660 cc，脚注 27）。
- **有效价格**（式 22，PDF p25）：
$$p^e_{jt}=(1+\rho_{jt})p_{jt}+T_{jt}-ES_{jt}$$
  $\rho_{jt}$ 为从价税率，含消费税（样本期 5%）；$T_{jt}$ 为从量税；$ES_{jt}$ 为生态车补贴。所有价格与税按 **2015 年 CPI** 平减；汇率按 100 JPY/USD。税制细节见 Online Appendix C（txt 未含）。
- **生态车补贴（Eco-car Subsidy, ES）**（表 IV，PDF p26）：

| | Phase 1 | Phase 2 |
|---|---|---|
| 时期 | 2009.4–2010.9 | 2011.12–2013.1 |
| 普通车 | JPY 100,000 | JPY 100,000 |
| 轻自动车 | JPY 50,000 | JPY 70,000 |
| 条件 | 比 2010 年燃油标准高 15% | 达到 2015 年燃油标准（= 2010 标准的 125%） |

  第一阶段另有报废超过 13 年旧车可领更高补贴的选项（脚注 29，Kitano 2022），本文从略（脚注 39）。
- **描述统计（表 V，PDF p26）**：2006–08 年对 2009–13 年：$\ln(s_{jt}/s_{0t})$ 均值 −8.446 / −8.860；$p^e$ 均值 2.731 / 2.772 百万日元（SD 1.966 / 1.973；最小 0.780 / 0.771；最大 12.870 / 13.946）；总税额均值 0.186 / 0.144 百万日元；ES 均值 0 / 0.019 百万日元（最大 0.104）；HP/WT 0.099 / 0.099；MPG 34.595 / 37.142；Size 7.485 / 7.520；AT/CVT 0.978 / 0.987；minicar 0.202 / 0.198；hybrid 0.008 / 0.042。正文称总税负下降约 24%，2009–2013 年平均 ES 为 JPY 19,000；MPG 有改善，其他特征变化不大。Online Appendix 表 A1 显示补贴使有效价格下降、税使其上升。
- **收入分布**：假设每年家庭实际收入 $y_{it}\sim LN(\mu_t,\sigma_t^2)$，用《国民生活基础调查》（Comprehensive Survey of Living Conditions）逐年估计 $(\mu_t,\sigma_t)$（Online Appendix B，txt 未含）；用 Halton 序列抽 1,000 个消费者（PDF p30）。**没有微观选择数据**，异质性只来自收入分布。

## 6. 结构模型如何构建

### 6.1 需求侧

**(1) 效用最大化**（McFadden 1981 的离散 + 连续选择，PDF p7，看图校正）：
$$\max_{(\mathbf m,j)\in\mathbb R^{d_m}_{+}\times\mathbf J}U(\mathbf m,j)\quad\text{s.t.}\quad \mathbf P_{\mathbf m}'\mathbf m+p_j\le y_i$$
$\mathbf m$ 为 $d_m$ 维连续选择的其他商品，$\mathbf J=\{0,1,\dots,J\}$，$j=0$ 为外部选项，$p_0=0$。

**(2) 条件间接效用**：
$$V(\mathbf P_{\mathbf m},y-p_j,j)\equiv\max_{\mathbf m\in\mathbb R^{d_m}_{+}}U(\mathbf m,j)\quad\text{s.t.}\quad\mathbf P_{\mathbf m}'\mathbf m\le y_i-p_j$$
标准性质：① 对 $(\mathbf P_m,y-p_j)$ 零次齐次；② 对 $y-p_j$ 递增；③ 关于 $\mathbf P_m$ 的单调性（文字层错乱，标准性质为对价格非增，待核）；④ 拟凸。作者用这些性质推出形状约束。

**(3)–(4) 加性可分**：
$$U(\mathbf m,j)=v(j)+u(\mathbf m)\ \Rightarrow\ V(\mathbf P_{\mathbf m},y-p_j,j)=v(j)+\tilde V(\mathbf P_{\mathbf m},y-p_j)$$
差异化品带来的效用与其他商品无关，大多数离散选择模型都隐含这一假设（脚注 8：因此排除 Dubin–McFadden 式的离散-连续耦合）。连续品按计价物处理，$\mathbf P_m$ 视为价格指数，$\tilde V=u\big((y-p_j)/P^m\big)$；$y$ 和 $p$ 都用价格指数平减。**定义收入效应项** $f(y-p_j)\equiv\tilde V(P^m,y-p_j)$，**只要求弱递增**，并在估计中施加（PDF p8）。

**(5)–(6) 差异化品效用**：
$$v_{ij}=\beta'X_j+\xi_j+\varepsilon_{ij},\ j=1,\dots,J;\qquad v_{i0}=\varepsilon_{i0}$$
$\varepsilon$ 服从 IID Type-I 极值分布。

**(7) 条件间接效用**（核心设定）：
$$V_{ij}=\begin{cases}f(y_i-p_j)+\beta'X_j+\xi_j+\varepsilon_{ij}, & j=1,\dots,J\\ f(y_i)+\varepsilon_{i0}, & j=0\end{cases}$$
- **准线性特例**：$V_{ij}=\alpha(y_i-p_j)+\beta'X_j+\xi_j+\varepsilon_{ij}$，收入在比较中抵消（脚注 9 还提到 Nevo 2001 的 $\alpha_i=g(z_i)$ 人口特征交互）。
- **BLP 特例**：$V_{ij}=\alpha\ln(y_i-p_j)+\beta'X_j+\xi_j+\varepsilon_{ij}$；脚注 10：按 Berry et al. (1999)，$\alpha\log(y_i-p_j)$ 可一阶近似为 $\alpha\,p_j/y_i$。
- 本文：除递增外不对 $f$ 施加任何参数形式。

**(8) 预算约束决定个人选择集**（PDF p9，看图校正）：
$$\mathbf J_{it}=\{0\}\cup\{j\in\{1,\dots,J_t\}:\ y_{it}-p_{jt}\ge0\}$$
**(9)** $\max_{j\in\mathbf J_{it}}V_{ijt}$。

**(10) 个体选择概率**（看图校正；**原页分母最后一项印作 $\xi_{jt}$，应为 $\xi_{kt}$**）：
$$s_{ijt}(y_{it})=\frac{\mathbf 1\{y_{it}\ge p_{jt}\}\exp\big(f(y_{it}-p_{jt})+\beta'X_{jt}+\xi_{jt}\big)}{\exp(f(y_{it}))+\sum_{k=1}^{J_t}\mathbf 1\{y_{it}\ge p_{kt}\}\exp\big(f(y_{it}-p_{kt})+\beta'X_{kt}+\xi_{kt}\big)}$$

**(11) 市场份额与需求**（PDF p10，未看图）：
$$s_{jt}=\int s_{ijt}(y_{it})\,dG_t(y_{it}),\qquad q_{jt}=N_t\times s_{jt}$$
基准模型里，异质性**只来自收入 $y_{it}$**；脚注 11：可加入随机系数 $u_{ijt}=f(y_{it}-p_{jt})+\beta_i'X_{jt}+\xi_{jt}+\varepsilon_{ijt}$，$\beta_i\sim N(\beta,\Sigma)$。

**价格弹性**（PDF p10，文字层重排）：
- 准线性 logit，式 (12)：$\eta_{jj}=-\alpha p_j(1-s_j)$，$\eta_{jk}=\alpha p_k s_k\ (k\ne j)$。
- 本文模型，式 (13)：
$$\eta_{jk}=\frac{\partial q_j}{\partial p_k}\frac{p_k}{q_j}=\begin{cases}-\dfrac{p_j}{s_j}\displaystyle\int f'(y_i-p_j)\,s_{ij}(1-s_{ij})\,dG(y_i), & k=j\\[2mm] \dfrac{p_k}{s_j}\displaystyle\int f'(y_i-p_k)\,s_{ij}s_{ik}\,dG(y_i), & k\ne j\end{cases}$$
  价格敏感度 $f'(y_i-p_j)$ 既随收入变化，也随价格水平本身变化，这比随机系数 logit（Nevo 2000b）多一层灵活性。脚注 12：$f$ 也会影响交叉弹性，价格敏感的消费者更偏向便宜产品，替代模式因此随价格不同而不同。
- **需求二阶导**（脚注 37，PDF p34）：
$$\frac{\partial^2 s_j}{\partial p_j^2}=\int\Big\{s_{ij}(1-s_{ij})(1-2s_{ij})\,[f'(y_i-p_j)]^2+s_{ij}(1-s_{ij})\,f''(y_i-p_j)\Big\}dG(y_i)$$
  参数化随机系数模型（$\alpha p/y$）中 $f''=0$；本文中曲率取决于灵活估计的 $f''$。
- **曲率指标**（Mrázová & Neary 2017；Miravete et al. 2023，PDF p33）：$\rho_j=\dfrac{q_j\,\partial^2q_j/\partial p_j^2}{(\partial q_j/\partial p_j)^2}$。

### 6.2 供给侧（VI(i)，PDF p34–p35）

- 多产品厂商 Bertrand–Nash 价格竞争（BLP；Nevo 2001），边际成本为常数。厂商定的是出厂价/标价 $p_{jt}$，消费者面对的是有效价格 $p^e_{jt}$。
- **(28) 利润**：$\pi_{ft}=\sum_{j\in J_{ft}}(p_{jt}-mc_{jt})\,q_{jt}(\mathbf p^e_t)$。
- **(29) FOC**（文字层错乱；以下按与 (30) 一致的形式重写，待看图核）：
$$\frac{\partial\pi_{ft}}{\partial p_{jt}}=q_{jt}(\mathbf p^e_t)+(1+\rho_{jt})\sum_{l\in J_{ft}}(p_{lt}-mc_{lt})\frac{\partial q_{lt}}{\partial p^e_{jt}}=0,\quad\forall j\in J_{ft}$$
- **(30) 矩阵形式**：
$$\tilde{\mathbf q}_t(\mathbf p^e_t)-D_t(\mathbf p^e_t)(\mathbf p_t-\mathbf{mc}_t)=0,\quad \tilde{\mathbf q}_t=\Big(\tfrac{q_{1t}}{1+\rho_{1t}},\dots,\tfrac{q_{J_tt}}{1+\rho_{J_tt}}\Big)',\quad D_t=\Omega_t\odot S(\mathbf p^e_t)$$
  $\Omega_t$ 为所有权矩阵（同一厂商为 1）；**$S$ 的 $(i,j)$ 元素 $=-\partial q_{jt}/\partial p^e_{it}$**，与 BLP 的 $\Delta_{jr}=-\partial s_r/\partial p_j$ 方向一致。收入效应下 Jacobian 不对称，方向不能写反（见 M01 卡提示）。从价税楔子以 $1/(1+\rho)$ 进入 $\tilde q$。
- **成本反推**：用需求估计算出 $S$，再由 (30) 解出 $\mathbf{mc}_t=\mathbf p_t-D_t^{-1}\tilde{\mathbf q}_t$（由 (30) 推得）。
- **均衡求解**：Morrow & Skerlos (2011) 定点算法（与 pyBLP 相同，脚注 38）。

### 6.3 均衡与其他模块（转嫁、合并、UPP）

- **转嫁率**（PDF p36）：$PTR_{jt}=\dfrac{p^{e\prime}_{jt}-p^e_{jt}}{ES_{jt}}$，$p^{e\prime}$ 为取消补贴（$ES_{jt}=0$）后重新求解的均衡有效价格（只对 $ES>0$ 的合格车型有意义，由定义推断）。有效价格变化率：$100\times(p^{e\prime}_{jt}-p^e_{jt})/p^{e\prime}_{jt}$。
- **Weyl–Fabinger 判据**（PDF p11）：在对称寡头或垄断下，转嫁率 < 1 当且仅当需求 log-concave，即 $d^2\log q(p)/dp^2<0$。准线性 logit 一定 log-concave。用上面的曲率 $\rho_j$ 表示：线性 logit 的 $\rho_j\le1$。
- **合并**：把 Toyota、Honda 产品在 $\Omega_t$ 中设为同一所有者，用估计出的 mc（**不考虑效率提升**）求新均衡（PDF p39）。
- **UPP**（式 31，Farrell & Shapiro 2010；Miller et al. 2016；推导见 Online Appendix F，PDF p41，文字层重排）：厂商 A 的产品为 $\{1,\dots,J_A\}$，厂商 B 的为 $\{J_A+1,\dots,J_A+J_B\}$，
$$\mathbf{UPP}_A=-\Big[\frac{\partial q_c}{\partial p_r}\Big]_{r,c\in A}^{-1}\Big[\frac{\partial q_c}{\partial p_r}\Big]_{r\in A,\,c\in B}(\mathbf p_B-\mathbf{mc}_B)$$
  （两个矩阵的行对应 $p_r$，列对应 $q_c$）。前两项的乘积是 A→B 的分流比矩阵，再乘 B 的加成，就是合并带来的机会成本。在合并前价格处计算。
- **脚注 14**（两家单产品厂商合并后厂商 1 的 FOC；文字层有两个 “−1” 上标，排版存疑）：$p_1+(\partial q_1/\partial p_1)^{-1}q_1=c_1+D_{12}(p_2-c_2)$，其中 $D_{12}=-\partial q_2/\partial q_1$ 为分流比，右侧第二项是机会成本。

### 6.4 识别

- **原文没有给出形式化的识别定理**，识别依靠以下几点：
  1. **条件矩**（式 17）：$E[\xi_{jt}\mid Z_{jt}]=0$，$Z_{jt}=(X_{jt},W_{jt})$。
  2. **水平归一化**：$f$ 加上常数 $C$ 会在 (10) 中消掉，所以设 $\pi_0=0\Rightarrow f(0)=0$（PDF p13–p14）。实证用逆 Bernstein，靠 $\lim_{x\to0}f=-\infty$ 定位，与 $f(0)=0$ 不能同时成立（脚注 44）。
  3. **形状约束**（弱递增）缓解 ill-posed inverse 问题，与惩罚项作用类似（脚注 18）。
  4. **$f$ 的形状靠什么识别（本卡解读）**：同一年里，外生收入分布 $G_t$ 中不同收入的消费者面对同一价格，$y-p$ 有差异；车型之间价格有差异，用税基工具变量处理其内生性；$(\mu_t,\sigma_t)$ 与税/补贴逐年变化。只有市场份额数据，没有微观选择数据，这是它和 Petrin (A02)、Griffith et al. (2018) 的区别。
- **价格工具变量**（PDF p27–p28，参照 Konishi & Zhao 2017、Kitano 2022）：
  - $w_{1,jt}=\sum_{k\in J_f,k\ne j}\text{Tax}_{kt}$（同厂其他车型的税额之和）；$w_{2,jt}=\sum_{k\notin J_f}\text{Tax}_{kt}$（竞争对手车型的税额之和）。$\text{Tax}$ = 重量税 + 汽车税；**取得税随价格变化、是内生的，故不计入**。
  - 相关性：厂商定价时考虑税率；第一阶段见表 VI。外生性：沿用 Eizenberg (2014) 的假设，厂商在推出车型前观察不到 $\xi_{jt}$；控制 mini/foreign/hybrid 等与减税、补贴资格相关的车型类别哑变量。产品特征视为外生（脚注 33；内生特征可参考 Barwick et al. 2024，即 A09）。
  - 脚注 32：差分工具变量（Gandhi & Houde 2019）也试过；传统 BLP 工具变量的第一阶段明显更弱，结果未报告（与 Konishi & Zhao 2017 附录 D 一致）。
  - 半参数模型的工具矩阵：$p(w)=(1,w_1,w_2,w_1^2,w_2^2,w_1^3,w_2^3)$，再加上 $p(w)$ 与 $X_{jt}$ 的张量积（PDF p29）。

### 6.5 估计算法与实现细节

**筛函数近似（III(i)，PDF p13）**：K 阶 Bernstein 多项式
$$f(x)\approx B_K(x)=\sum_{k=0}^{K}\pi_k b^K_k(x)\equiv\psi_K(x)'\Pi,\qquad b^K_k(x)=\binom{K}{k}x^k(1-x)^{K-k}\quad(14)\text{–}(15)$$
$$B_K'(x)=K\sum_{k=0}^{K-1}(\pi_{k+1}-\pi_k)\,b^{K-1}_k(x)$$
- **单调约束**：$\pi_k\le\pi_{k+1}$（充分但非必要，脚注 16）；另一种做法是在网格点上约束导数为正（Online Appendix D），结果相近但计算时间长得多。
- **归一化**：$\pi_0=0\Rightarrow f(0)=0$。
- **标准化**（脚注 15）：$z_{max}=\max_{i,j,t}\{y_{it}-p_{jt}\}$，$z_{min}=\min_{i,j,t}\{y_{it}-p_{jt}\mid y_{it}-p_{jt}>0\}$，文字层为 $z_{ijt}\equiv\frac{y_{it}-p_{jt}}{z_{max}-z_{min}}$（原文如此；严格映射到 [0,1] 通常还要减去 $z_{min}$，待核）。无预算约束的版本中 $z_{min}=\min\{y-p\}$，可以为负（脚注 45）。

**sieve 份额方程（式 16，PDF p14，未看图）**：把 (10) 中的 $f$ 换成 $\psi_K(\cdot)'\Pi$ 后对 $G_t$ 积分。文字层显示分母求和项中印成了 $\mathbf 1\{y_{it}\ge p_{jt}\}$ 和 $\xi_{jt}$，与 (10) 是同类笔误，应为 $p_{kt}$、$\xi_{kt}$（未看图，待核）。参数 $\theta=(\beta,\Pi)$。

**sieve GMM（PDF p14–p15）**：
- (18) 无条件矩：$E[\xi_{jt}(\theta)\,p_b(X_{jt},W_{jt})]=0,\ b=1,\dots,B$，$\{p_b\}$ 当 $B\to\infty$ 时能逼近任意平方可积函数。脚注 17：等价于用单位权重矩阵、以级数估计条件期望的 sieve 最小距离。
- (19) 目标函数：$\xi(\beta,\Pi)'\tilde P(\tilde P'\tilde P)^{-}\tilde P'\xi(\beta,\Pi)$，$\tilde P=[P,\ P\otimes X]$，$P=(p(W_{11}),\dots,p(W_{J_TT}))'$（按 Chetverikov, Kim & Wilhelm 2018）。
- 不加高阶导数惩罚项（脚注 18）：一是惩罚要选调参；二是单调约束已有类似作用（Chetverikov & Wilhelm 2017 附录 B.3）。

**NFP 三步**（给定 $\Pi$）：① 用 BLP 收缩映射求 $\delta_{jt}=\beta'X_{jt}+\xi_{jt}$（容差 **1E-12**，脚注 19）；② 把 $\delta$ 对 $X$ 做线性回归得到 $\hat\beta$ 和残差 $\xi$（“concentration out”，Nevo 2001；线性 GMM）；③ 计算 (19)。**只对 $\Pi$ 做非线性优化**，所以 $\delta$ 中可以放大量协变量和固定效应（厂商 FE、年份 FE）。MC 中用 **Knitro** 的约束最小化（脚注 22）。

**推断**：$\beta$ 与 $f$ 的置信区间用 Chen & Pouzo (2015) Theorem 5.2 的广义残差自助法，**200 次 bootstrap**（PDF p16, p31）。

**随机系数扩展（III(ii)(a)）**：把随机系数的标准差和 $\Pi$ 一起作为非线性参数，需要差分工具变量（Gandhi & Houde 2019）提供额外矩。实证未采用（见 §10）。

**实证规格（V(iii)，式 24–25，PDF p29–p30）**：
$$V_{ijt}=f(y_{it}-p^e_{jt})+\beta'X_{jt}+\theta_{f(j)}+\theta_t+\xi_{jt}+\varepsilon_{ijt}\ (j\ge1),\qquad V_{i0t}=f(y_{it})+\varepsilon_{i0t}$$
- **逆 Bernstein 近似**（文字层重排：“inverse of a Bernstein polynomial”，且 $\lim_{x\to0}f=-\infty$，PDF p29、p43 均未看图）：
$$f(y-p)=\frac{-1}{\sum_{k=1}^{K}\pi_k\,b^K_k(y-p)},\qquad K=4,\qquad \pi_k\le\pi_{k+1}\ (k=1,\dots,K-1)$$
  依据：$k\ge1$ 的基函数在 0 处为 0，所以分母 → 0，$f\to-\infty$；分母递增且为正时，$-1/B$ 也递增（本卡推理）。
- **为什么用逆形式**：预算指示函数 $\mathbf 1\{p_{jt}\le y_{it}\}$ 使个体概率在 $p_{jt}=y_{it}$ 处不连续；用有限个模拟消费者近似加总需求时，加总需求会有很多不连续点。估计时价格是给定协变量，问题不大，但求解 Bertrand 均衡时数值上不稳定（脚注 35：作者早期用不连续模型，模拟结果不可靠）。施加 $\lim_{p\to y}f(y-p)=-\infty$ 后，价格趋近收入时 $s_{ij}\to0$，需求连续（数值例见 Online Appendix E）。
- 积分：每年 1,000 个 Halton 消费者，取自估计的 $LN(\mu_t,\sigma_t^2)$。
- **筛阶数**：没有数据驱动的方法（Chen & Qiu 2016 指出理论指导有限；Chen, Christensen & Kankanala 2023 的方法不覆盖本模型）；Online Appendix 图 A1 显示 K=3、4、5 的自价格弹性相近（脚注 34）。

**参数化对照模型**：
- 线性 logit，式 (23)：$\ln(s_{jt}/s_{0t})=\alpha p^e_{jt}+\beta'X_{jt}+\theta_{f(j)}+\theta_t+\xi_{jt}$（对应准线性 $f=\alpha(y-p)$ 且**不加预算约束**；脚注 31：即使准线性，只要有预算约束就会产生消费者异质性，不能再用 Berry 1994 的线性回归）。
- 参数化收入效应（“parametric BLP / parametric random coefficient”），式 (26)–(27)：$V_{ijt}=\frac{\alpha}{y_i}p^e_{jt}+\beta'X_{jt}+\theta_{f(j)}+\theta_t+\xi_{jt}+\varepsilon_{ijt}$，$V_{i0t}=\varepsilon_{i0t}$；与 BLP(1995/1999) 相同，是 $\alpha\log(y-p)$ 的一阶近似。

### 6.6 反事实与福利计算

- **生态车补贴的转嫁**：令所有 $ES_{jt}=0$，用 (30) 重新求均衡，比较有效价格（PDF p35–p36）。
- **生产者剩余与税收**（脚注 40）：$PS_t=\sum_{f\in F}\sum_{j\in J_{ft}}(p_{jt}-mc_{jt})q_{jt}(\mathbf p^e_t)$；$TR_t=\sum_f\sum_{j}(p_{jt}\rho_{jt}+T_{jt}-ES_{jt})q_{jt}(\mathbf p^e_t)$。
- **消费者剩余**：线性 logit 与参数化随机系数模型用 Small & Rosen (1981) 的 log-sum 公式（参数模型对每个收入水平的消费者分别计算再加总，脚注 41；原文未写出式子）。半参数模型有收入效应，log-sum 不适用，改用 Dagsvik & Karlström (2005) 的**补偿变动 CV**，逐个体计算后加总（Online Appendix H，txt 未含；脚注 42）。
- **合并**：改 $\Omega_t$ → 求新均衡 → 比较价格、UPP、CS/利润/税收/总福利（2006–2013 年平均）。
- **稳健性**：(i) 用租赁价格（Abe 2023；Bento et al. 2009 的思路；Online Appendix G）重新估计并模拟；(ii) 去掉预算约束：(32)–(33)，用普通 Bernstein，K=4。

## 7. 估计结果

**线性 logit（表 VI，PDF p28；N=1,322；均含年份 FE、厂商 FE、minicar 与 hybrid 哑变量；括号内为稳健标准误）**：

| | (1) OLS | (2) IV 差分 | (3) IV 税基 | (4) IV 两者 |
|---|---:|---:|---:|---:|
| 有效价格 $p^e$ | −0.402 (0.030) | −0.646 (0.119) | **−0.929 (0.153)** | −0.703 (0.105) |
| HP/WT | 5.898 (1.578) | 13.598 (3.830) | 22.550 (4.853) | 15.424 (3.429) |
| MPG | 0.105 (0.006) | 0.100 (0.007) | 0.093 (0.007) | 0.098 (0.007) |
| Car size | 1.686 (0.115) | 1.976 (0.163) | 2.314 (0.189) | 2.045 (0.148) |
| AT/CVT | 0.257 (0.385) | 0.437 (0.385) | 0.647 (0.399) | 0.480 (0.385) |
| Kleibergen–Paap F | NA | 21.650 | 18.290 | 16.316 |
| Hansen J | NA | 25.702 | **2.614** | 30.986 |

- OLS 的价格系数偏向 0；第 (3) 列（税基工具变量）的 KP F 较高、J 统计量很低，因此选为半参数模型的工具变量，并作为模拟中线性 logit 的参数（PDF p29）。
- 派生 [D]（本卡推算，非原文）：按 (12)，在均值价格约 2.77 百万日元、$s\approx0$ 处，线性 logit 的 $|\eta_{jj}|\approx0.929\times2.77\approx2.6$。

**半参数模型**：
- **$\hat f(y-p)$（图 7，PDF p31）**：明显**非线性且凹**；低收入家庭购车后可支配收入的边际效用更高。图中 $y-p$ 范围为 0.5–10 百万日元，95% 置信带基于 200 次 bootstrap。正文未给 $\pi_k$ 的数值。
- **线性参数（表 VII，PDF p31；N=1,322；含 minicar、hybrid 哑变量和年份、厂商 FE，未报告）**：

| | 估计值 | 95% CI |
|---|---:|---|
| Constant | −25.147 | [−27.587, −21.078] |
| HP/WT | 21.315 | [10.744, 33.838] |
| MPG | 0.077 | [0.042, 0.098] |
| Car size | 2.508 | [1.877, 3.324] |
| AT/CVT | 0.269 | [−0.676, 1.531] |

  原文称点估计与简单 logit 可比，“HP/WT 约为表 VI 第 (3) 列的 1.5 倍”。但表中 21.315 对 22.550，**数字不支持这一说法**；与第 (2) 列 13.598 之比约 1.57（待核，见 §11）。半参数模型的置信区间更宽，说明灵活估计收入效应会降低其他参数的精度，这是一个需要权衡的地方。
- **自价格弹性（图 8，PDF p32）**：简单 logit 中弹性与价格呈线性关系；半参数模型中两者是非线性关系，**在 2–10 百万日元区间内弹性大致不变**。因此 logit **低估便宜车（如轻自动车）的弹性，高估豪华车的弹性**。参数化 BLP（$\alpha p/y$）的整体形态接近半参数模型，但在相同价格下，半参数模型的弹性**异质性更大**。正文未报告弹性数值，只有图。
- **曲率（图 9，PDF p33–p34）**：线性 logit 的曲率**以 1 为上界并集中在 1 附近**（log-concave）；参数化收入效应和半参数模型都有异质性，半参数模型最大，原因是其曲率依赖灵活估计的 $f''$。

## 8. 反事实 / 政策结果

**(a) 生态车补贴转嫁（表 VIII，PDF p36）**：

| $PTR_{jt}$ | Mean | SD | p25 | Median | p75 |
|---|---:|---:|---:|---:|---:|
| 半参数 | **1.194** | 0.080 | 1.140 | 1.174 | 1.252 |
| 参数化收入效应 | 1.196 | 0.046 | 1.166 | 1.194 | 1.229 |
| 线性 logit | 0.991 | 0.009 | 0.980 | 0.993 | 0.999 |

| 有效价格变化 % | Mean | SD | p25 | Median | p75 |
|---|---:|---:|---:|---:|---:|
| 半参数 | −5.968% | 2.434% | 3.997% | 5.701% | 7.532% |
| 参数化收入效应 | −5.940% | 2.287% | 4.068% | 5.832% | 7.232% |
| 线性 logit | −4.928% | 1,788%（应为 1.788%） | 3.500% | 4.852% | 5.932% |

- 均值为负、分位数为正，表内符号不一致（原表如此）。表 XIV/XV 把同一组数印成负的分位数，即 −4.00/−5.70/−7.53。
- 半参数与参数化收入效应模型的平均转嫁率相近（1.194 对 1.196），都出现**过度转嫁**；线性 logit 为 0.991 且不超过 1，与 Weyl–Fabinger 的结论一致：log-concave 需求只能不完全转嫁。
- **异质性（图 10，PDF p37；只画有效价格 < 8 百万日元的车型）**：半参数模型中**便宜车转嫁率更高，贵车更低**，与图 9 的曲率格局一致；参数模型的异质性较小。

**(b) 补贴的福利效应（表 IX，PDF p38；单位：十亿日元）**：

| 规格 | 项目 | 2009 | 2010 | 2012 | 平均 |
|---|---|---:|---:|---:|---:|
| 半参数 | CS | 302.2 | 406.4 | 571.7 | **426.8** |
| | Profit | 97.9 | 129.5 | 174.5 | 134.0 |
| | Tax revenue | −143.4 | −197.4 | −274.4 | −205.1 |
| | Total | 256.7 | 338.6 | 471.8 | **355.7** |
| 参数化收入效应 | CS | 179.6 | 250.2 | 344.1 | 258.0 |
| | Profit | 101.8 | 136.6 | 187.1 | 141.8 |
| | Tax revenue | −136.7 | −188.3 | −261.2 | −195.4 |
| | Total | 144.7 | 198.5 | 269.9 | 204.4 |
| 线性 logit | CS | 153.0 | 211.5 | 293.7 | 219.4 |
| | Profit | 138.9 | 191.7 | 263.7 | 198.1 |
| | Tax revenue | −144.2 | −198.1 | −277.5 | −206.6 |
| | Total | 147.7 | 205.1 | 279.9 | 210.9 |

- 三种规格下补贴都**提高总福利**，且**消费者剩余增量超过财政支出**。作者的解释是补贴缓解了市场势力造成的既有扭曲（Buchanan 1969；Fowlie et al. 2016）。半参数模型的 CS 与总福利最大，平均分别约为参数模型的 1.65 倍（426.8/258.0）和 1.74 倍（355.7/204.4），由表算出。各行加总已核对：CS + Profit + Tax = Total。

**(c) CV 分布（表 X，PDF p38；单位：日元）**：

| | Mean | SD | p10 | p25 | Median | p75 | p90 |
|---|---:|---:|---:|---:|---:|---:|---:|
| 半参数 2009 | 5,715 | 11,705 | 0 | 0 | 6 | 3,280 | 26,511 |
| 半参数 2010 | 7,616 | 15,822 | 0 | 0 | 14 | 4,202 | 34,570 |
| 半参数 2012 | 10,554 | 20,189 | 0 | 0 | 28 | 8,024 | 50,137 |
| 参数 2009 | 3,397 | 7,302 | 0 | 8 | 229 | 2,525 | 11,375 |
| 参数 2010 | 4,689 | 10,390 | 0 | 13 | 301 | 3,280 | 15,390 |
| 参数 2012 | 6,351 | 12,442 | 1 | 27 | 605 | 5,667 | 22,124 |
| 线性 logit 2009/2010/2012 | 2,893 / 3,963 / 5,423 | NA | | | | | |

- 线性 logit 没有异质性；另两种模型的 SD 很大。logit 的 CV 落在半参数模型分布的中位数与 p75 之间。**图 11（2012 年，横轴为 log10(CV+1)）**：参数模型的 CV 分布右偏，半参数模型的是**双峰**，说明分析政策的分配效应时，收入效应要灵活设定（PDF p39）。

**(d) Toyota–Honda 合并（表 XI，PDF p40）**：观测有效价格：Toyota 均值 2.76（SD 2.01，中位数 2.18）百万日元，Honda 2.51（SD 1.27，中位数 2.33）。

| 有效价格变化 | Toyota 均值（SD；p25/中位/p75） | Honda 均值（SD；p25/中位/p75） |
|---|---|---|
| 半参数 | **2.68%**（0.60%；2.38/2.74/3.08） | **7.30%**（0.86%；6.78/7.46/7.93） |
| 参数化收入效应 | 1.87%（0.33%；1.74/1.94/2.10） | 5.32%（0.51%；4.99/5.51/5.71） |
| 线性 logit | 0.59%（0.25%；0.42/0.57/0.74） | 1.37%（0.62%；0.91/1.23/1.82） |

**UPP（表 XII，PDF p41；单位：万日元）**：

| | Toyota 均值（SD；p25/中位/p75） | Honda 均值（SD；p25/中位/p75） |
|---|---|---|
| 半参数 | 4.96（1.32；3.99/4.77/5.89） | 13.05（5.32；8.30/12.71/16.40） |
| 参数化收入效应 | 3.48（1.14；2.67/3.24/4.16） | 9.82（4.44；6.01/9.43/12.55） |
| 线性 logit | 1.21（0.15；1.15/1.18/1.38） | 2.61（0.28；2.52/2.72/2.88） |

- **机制**：线性 logit 的 UPP 最低、转嫁率也最低，所以合并效应最小。半参数与参数模型的平均转嫁率相近，但半参数模型的 **UPP 更大**，所以合并效应更大。
- **合并的福利效应（表 XIII，2006–2013 年平均，十亿日元）**：

| | 半参数 | 参数化收入效应 | 线性 logit |
|---|---:|---:|---:|
| CS | −240.1 | −108.9 | −33.8 |
| Profit | 35.9 | 21.9 | 1.6 |
| Tax revenue | −11.8 | −12.9 | −2.2 |
| Total welfare | **−216.0** | −99.9 | −34.4 |

## 9. 贡献

1. **方法**：提出一个半参数离散选择需求框架，从效用最大化（离散 + 连续选择，加性可分）推出收入效应项 $f(y-p)$，把它当作只需弱递增的一维非参数对象；准线性和 BLP 的对数形式都是它的特例。
2. **估计**：把 Bernstein 筛近似 + 系数单调约束嵌入 BLP NFP，做 sieve GMM。$\beta$ 可以 concentrate out，只需对 $\Pi$ 做非线性搜索，计算负担接近标准 BLP。用 Chen–Pouzo 自助法做推断。
3. **形状约束的价值**：MC 显示在**不可分模型**中，单调约束也能大幅降低 $f$ 的 MISE 和 $\beta_0$ 的 RMSE，把 Chetverikov & Wilhelm (2017) 的结论从可分模型推广到不可分模型。
4. **预算约束**：显式写进选择集 (8)，并用逆 Bernstein（$\lim f=-\infty$）保证需求连续，使供给侧均衡可以数值求解。这一点是方法上的细节，在实践中很关键。
5. **实证**：日本汽车数据中 $f$ 非线性且凹；补贴出现过度转嫁（约 1.19）；合并效应明显大于参数模型；CV 分布呈双峰，说明分配效应与参数模型不同。这些结果表明需求曲率需要灵活估计。

## 10. 局限与稳健性

**蒙特卡洛（IV，PDF p16–p23）**：
- **DGP（式 20–21）**：$J_t=100$，$T=10$；$V_{ijt}=\beta_0+\beta_1x_{jt}+\xi_{jt}+f(y_{it}-p_{jt})+\varepsilon_{ijt}$，$V_{i0t}=f(y_{it})+\varepsilon_{i0t}$；$x\sim U(0,1)$，$\xi\sim N(0,0.1^2)$；$p_{jt}=0.2+0.3x_{jt}+w_{jt}+\xi_{jt}$，$w\sim U(0,1)$ 为成本转移变量（价格由边际成本竞争性决定，不含 Bertrand，脚注 21）；收入 $y\sim LN(0,0.25^2)$（原文写作 $y_{jt}$，应为 $y_{it}$）；1,000 个 Halton 抽样；$y-p$ 的支撑约为 [−1.5, 2.5]；$\beta_0=-5$，$\beta_1=3$。
- **三个 DGP**：DGP1 $f(a)=\sinh^{-1}(a)$；DGP2 $f(a)=\ln2+\ln(|a-1|+1)\,\mathrm{sgn}(a-1)$，在 $a=1$ 处不可导，$a\in[0,1]$ 上凸、$a\ge1$ 上凹，标准化后约在第 40 百分位处二阶导变号；DGP3 $f(a)=a$，即参数模型设定正确。DGP2 的文字层排版错乱，按 $f(0)=0$ 和凹凸描述核对后一致。
- **实现**：K=3、4、5；工具 $p(w)=(1,w,\dots,w^{K-1})'$ 及其与 $x$ 的乘积；参数模型用 $(1,w)$；$NS=100$ 次重复；$MISE=\frac1{NS}\sum_r\int_0^1(f(z)-\hat f_r(z))^2dz$，用 Monte Carlo 积分；Bias 与 RMSE 的公式在文字层里没有根号，待核。

| MISE of $f$ | DGP1 无SR / 有SR | DGP2 无SR / 有SR | DGP3 无SR / 有SR |
|---|---|---|---|
| K=3 | 0.0268 / **0.0025** | 0.0289 / 0.0039 | 0.0356 / 0.0044 |
| K=4 | 0.0142 / 0.0050 | 0.0192 / 0.0046 | 0.0207 / 0.0065 |
| K=5 | 0.1075 / 0.0069 | 0.0526 / 0.0049 | 0.0615 / 0.0066 |
| 参数 $\alpha(y-p)$ | 0.0099 | **0.0018** | **0.0002** |

- $\beta_0$ 的 RMSE（无 SR → 有 SR，K=3/4/5）：DGP1 0.1032/0.0838/0.1557 → 0.0249/0.0405/0.0482（参数 0.0097）；DGP2 0.1053/0.1033/0.1198 → 0.0315/0.0390/0.0440（参数 0.0091）；DGP3 0.1140/0.0981/0.1249 → 0.0376/0.0496/0.0519（参数 0.0105）。
- $\beta_0$ 的 Bias（无 SR；有 SR；参数）：DGP1 K3 0.0058；−0.0043；0.0074｜K4 −0.0072；0.0078｜K5 0.0143；−0.0024。DGP2 K3 −0.0375；−0.0184；−0.0253｜K4 −0.0070；−0.0219｜K5 0.0238；−0.0185。DGP3 K3 −0.0123；0.0038；0.0010｜K4 0.0098；−0.0050｜K5 0.0085；−0.0036。
- $\beta_1$：各方法的 RMSE 都在 0.011–0.014 之间，差别很小，个别格子 SR 略差（如 DGP1 K=5：0.0128 对 0.0123；DGP3 K=3：0.0121 对 0.0116）。Bias 的绝对值都 ≤ 0.0026。
- **结论**：形状约束显著降低 MISE 和 $\beta_0$ 的 RMSE，置信带在支撑端点附近收紧（图 1–3）。DGP1 中非参数 + SR 优于设定错误的参数模型（图 4）。DGP2 接近线性，参数模型的设定偏误很小，其 MISE 反而更低，非参数的置信区间也更宽（图 5）。DGP3 中参数模型正确，明显更优（图 6）。这就是灵活性与效率之间的权衡。

**实证稳健性（VII）**：
- **租赁价格（表 XIV，PDF p42）**：PTR 均值 1.194（SD 0.074；1.141/1.181/1.239），与基准的 1.194（SD 0.080）几乎一样；有效价格变化 −5.97%（SD 2.47%；−3.97/−5.72/−7.30）。
- **去掉预算约束（表 XV，PDF p44）**：PTR 均值 **1.105**（SD 0.081；1.041/1.075/1.157），价格变化 −5.36%（SD 1.69%；−4.05/−5.17/−6.15）。基准模型的 PTR 略高，但形态相似，**仍然过度转嫁**。去掉预算约束后不需要逆 Bernstein，需求本身就连续，代价是不符合效用最大化、无法做一致的福利分析，且可能有偏（Pesendorfer et al. 2023）。
- **其他**：筛阶数 K=3/4/5 的弹性相似（图 A1）；逐点导数约束与系数约束结果相近（Online Appendix D）。

**局限**：
1. 基准模型里异质性只来自收入，**没有对特征的随机系数**。替代模式仍接近 logit（IIA 只在同一收入层内被打破）。脚注 36：尝试过用差分工具变量估计特征随机系数，但 $\sigma$ 不精确且接近 0，可能因为只有 $T=8$ 个市场。
2. 没有数据驱动的筛阶数选择（K=4 是设定的）。
3. 逆 Bernstein 规定 $\lim f=-\infty$，与 MC 中 $f(0)=0$ 的归一化不能兼容，所以**没有对实证所用的逆形式做 MC**（脚注 44，结果“可应要求提供”）。
4. 预算约束用年收入对整车有效价格，忽略了贷款和储蓄（用租赁价格部分缓解）。
5. 产品特征和产品选择视为外生（Eizenberg 型假设）；只用年度数据，补贴实际从年中开始执行；忽略报废补贴（脚注 39）；合并不考虑效率提升；补贴分析是方法演示，“并非对日本 feebate 的完整评估”。
6. 半参数模型的线性参数置信区间更宽，精度有损失。
7. 加性可分排除了离散-连续耦合（Dubin–McFadden 类）。

## 11. 公式校正与笔误提示

1. **(10)（PDF p9，已看图）**：分母求和中最后一项原印 $\xi_{jt}$，**应为 $\xi_{kt}$**。
2. **(16)（PDF p14，未看图）**：文字层显示分母求和内为 $\mathbf 1\{y_{it}\ge p_{jt}\}$ 和 $\xi_{jt}$，与 (10) 是同类笔误，应为 $p_{kt}$、$\xi_{kt}$，待看图核。
3. **(33)（PDF p43，未看图）**：分母同样印成 $\xi_{jt}$，应为 $\xi_{kt}$；其后正文“non-zero even when $p_{jt}<y_{it}$（budget constraint violated）”中的不等号应为 $p_{jt}>y_{it}$；该处指示函数写成 $\mathbf 1\{y>p\}$，与 (10) 的 $\ge$ 不一致。
4. **(29) FOC（PDF p35）**：文字层错乱，§6.2 按与 (30) 一致的形式重写；$S_{ij}=-\partial q_j/\partial p^e_i$，属于 BLP 方向。
5. **逆 Bernstein 式（PDF p29, p43）**：由文字层重构为 $f=-1/\sum_{k=1}^K\pi_kb^K_k$，待看图核。
6. **脚注 14**：文字层有两个 “−1” 上标，分流比项的写法待核。
7. **脚注 15**：标准化式为 $(y-p)/(z_{max}-z_{min})$，未减 $z_{min}$，原文如此，待核。
8. **MC 中的 RMSE**：文字层未见根号；收入记作 $y_{jt}$，应为 $y_{it}$。
9. **表 VIII 面板 B**：均值为负、分位数为正，符号不一致；线性 logit 的 SD 印作 “1,788%”，应为 1.788%。表 XIV/XV 中分位数为负，但 p25 = −4.00 大于 p75 = −7.53，相当于按绝对值排序。
10. **正文与表不符**：说 HP/WT “约为表 VI 第 (3) 列的 1.5 倍”，实际 21.315 对 22.550；“总税负下降约 24%”，按表 V 两期均值 0.186 → 0.144 算约 −22.6%，口径可能不同。
11. **小笔误**：V(ii) 中 “AC/CVT” 应为 AT/CVT；正文引 “Compiani [2021]”，参考文献列为 2022 QE；图 8 与图 9 的图例颜色/形状描述不一致（图 8 称 BLP 为 red diamond，图 9 称 logit 为 green diamond、参数模型为 red square）。
12. **符号约定**：(23) 中价格系数 $\alpha$ 估计为负（−0.929），而 §II 的 $f=\alpha(y-p)$ 中 $\alpha>0$，两处符号约定相反。(26) 的 $\alpha/y_i$ 同样应为负值。复用时要统一。

## 12. 可复用要点与关联文献

**可复用要点**：
- **规格模板**：$V_{ij}=f(y_i-p_j)+\beta'X_j+\xi_j+\varepsilon_{ij}$，$V_{i0}=f(y_i)+\varepsilon_{i0}$，选择集 $\{j:y_i\ge p_j\}$。$f$ 线性即准线性 logit，$f=\alpha\ln$ 即 BLP(1995)，一阶近似 $\alpha p/y$ 即 BLP(1999)。
- **实现配方**：Bernstein 基 + $\pi_k\le\pi_{k+1}$（线性不等式约束，可用 Knitro）+ $\pi_0=0$；$\delta$ 用收缩映射（1E-12）；$\beta$ 与固定效应 concentrate out；只对 $\Pi$ 做非线性搜索；工具矩阵 $\tilde P=[P,P\otimes X]$，$P$ 为工具变量的多项式基；推断用 Chen–Pouzo 广义残差自助法（200 次）。
- **供给侧注意**：(a) 有预算约束时要保证 $\lim_{p\to y}f=-\infty$，否则 Bertrand 均衡难以求解。BLP 的 $\ln(y-p)$ 本来就满足这一点（本卡解读）。(b) 存在从价税时，FOC 中份额要除以 $(1+\rho)$，Jacobian 对有效价格求导，$S_{ij}=-\partial q_j/\partial p^e_i$。
- **诊断**：报告曲率 $\rho_j=q_j q_j''/(q_j')^2$ 的分布。线性 logit 的 $\rho\le1$，转嫁率必然 ≤ 1，这是规格本身造成的，不能当作经验发现。
- **福利**：有收入效应时不能用 log-sum，要用 Dagsvik–Karlström 的 CV，并报告 CV 分布（分位数和直方图）。
- **工具变量**：日本的车重税和汽车税（不含随价格变化的取得税）按同厂/对手求和，F≈18，J≈2.6（参照 Konishi & Zhao 2017；Kitano 2022）。

**与其他卡的关系**：
- **A01 BLP (1995)**：BLP 的 $\alpha\ln(y_i-p_j)$ 是本文 $f$ 的参数特例；本文说明这类函数形式会限制曲率和转嫁率。BLP 的供给方向 $\Delta_{jr}=-\partial s_r/\partial p_j$ 与本文 (30) 中的 $S$ 一致；本文另外加入税收楔子 $(1+\rho)$。参数对照模型 (26) 就是 BLP(1999) 的 $\alpha p/y$。
- **A02 Petrin (2002)**：Petrin 按收入组设分段的价格系数 $(\alpha_1,\alpha_2,\alpha_3)$，并用微观矩识别。本文的价格敏感度 $f'(y-p)$ 随收入和价格连续变化，只用市场份额数据加外部收入分布，没有微观矩。如果有 CEX 类微观矩，可以与本文的 sieve 结合来提高 $f$ 的精度（本卡建议）。
- **M01 Conlon–Gortmaker (pyBLP)**：本文用的 Morrow–Skerlos 定点算法来自 pyBLP。M01 卡提示：收入效应规格的 Jacobian 不对称，$\Delta$ 必须按 BLP 方向构造。本文 $S_{ij}=-\partial q_j/\partial p^e_i$ 正好是这个方向。预算指示函数 + 非参数 $f$ 很可能需要自己写代码（本卡判断）。
- **A03 GMY (2024)**：同样是汽车市场、价格敏感度随收入变化的结构模型，研究市场势力的演变。本文提醒，加成和转嫁对收入效应的函数形式敏感。
- **A05 GRV (2018)、A08 Durrmeyer (2022)、A09 BKL (2024)**：都涉及汽车税、补贴、feebate 及其转嫁或分配效应。本文的 CV 双峰分布和过度转嫁结论可以作为比较基准；A09 研究内生产品属性，也就是本文脚注 33 引用的 Barwick et al. (2024)。
- **A07 Grigolon–Verboven (2014)**：嵌套 logit 与随机系数 logit 在替代模式上的比较。本文的灵活性在曲率维度，而不在替代模式维度，两者可以互补。
- **原文外部关联**：Griffith, Nesheim & O'Connell (2018)；Miravete, Seim & Thurk (2023)；Birchall, Mohapatra & Verboven (2023)；Konishi & Zhao (2017)；Kitano (2022)；Ohashi & Toyama (2017)；Weyl & Fabinger (2013)；Pesendorfer, Schiraldi & Silva-Junior (2023)。
