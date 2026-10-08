# M01 Best Practices for Differentiated Products Demand Estimation with PyBLP（用 PyBLP 估计差异化产品需求的最佳实践）

> 记忆卡 ID：M01｜分组：方法底座｜精读方式：子代理按 txt 第 1–3215 行逐页通读（PDF 第 1–54 页，含附录 A、B，参考文献与在线附录目录）。
> 公式以 txt 页末【公式校正】段与总表（(2)(3)(4)(5)(6)(7)(8)(26)(27) 共 9 条，均已看图）为准；另本卡对照核对页图 p07、p08、p09、p12 重读了 (9)–(15)、(21)(22)。其余公式按文字层重建，把握程度见第 11 节。
> 旋转排版的大表（表 4、5、6、B2、B3）文字层被打散，本卡按“列从右到左、行从上到下”的规律重排，并与表 B1 的交叉值核对；无法唯一确定处标“（文字层错乱，待核）”。凡本卡自行推算的数字标 [D]。

## 1. 引用信息
- **英文题目**：Best Practices for Differentiated Products Demand Estimation with PyBLP
- **中译**：用 PyBLP 估计差异化产品需求的最佳实践
- **作者（单位）**：Christopher Conlon（New York University, Stern School of Business）；Jeff Gortmaker（Harvard University）。致谢中编辑为 Marc Rysman，研究助理 Daniel Stackman。
- **期刊**：*The RAND Journal of Economics*, 2020, 51(4): 1108–1161。DOI 10.1111/1756-2171.12352（txt 未给出 DOI，凭记忆填写，待核）。
- **版本说明**：本地为 RAND **早期在线版**（页眉 “Vol. 00, No. 00, xxxx 2020, pp. 1–54”），页码从 1 起，与正式刊不同。若正式刊排版不变，正式刊页码 = 本地页码 + 1107 [D]（54 页对应 1108–1161）。
- **APA**：Conlon, C., & Gortmaker, J. (2020). Best practices for differentiated products demand estimation with PyBLP. *The RAND Journal of Economics, 51*(4), 1108–1161. https://doi.org/10.1111/1756-2171.12352
- **GB/T 7714**：CONLON C, GORTMAKER J. Best practices for differentiated products demand estimation with PyBLP[J]. The RAND Journal of Economics, 2020, 51(4): 1108-1161.
- **源 txt**：`scratchpad/txt3w/M01_ConlonGortmaker2020.txt`（超长行已折行），共 54 页，**印刷页 = PDF 页**。核对页图仅有 p05–p09、p12、p19。
- **结构**：§1 引言（p1–4，表 1 记号 p4）；§2 模型与估计（p4–9：需求、供给、估计量、NFXP 算法 1、嵌套 logit 与 RCNL）；§3 算法改进（p9–19：多维固定效应、份额反演、优化、数值技巧、积分、定价均衡）；§4 供需联合：最优工具与过度识别约束（p19–24，算法 2）；§5 蒙特卡洛（p24–36，表 2–6、图 1–4）；§6 复现（p36–43，表 7–8、图 5–7）；§7 结论（p44）；附录 A 推导（p44–46）；附录 B 附表附图（p46–50：表 B1–B3、图 B1）；参考文献（p50–53）；在线附录目录（p53–54，图 OA1–OA18、表 OA1–OA18，**txt 无内容**）。
- **方法类型标签**：METHOD｜BLP 随机系数 logit / 嵌套 logit / RCNL｜NFXP（嵌套不动点）｜SQUAREM 加速收缩、Levenberg–Marquardt｜集中掉线性参数（含高维固定效应吸收）｜解析梯度（含供给侧）｜数值积分（pMC、Halton、MLHS、重要性抽样、Gauss–Hermite 积规则、稀疏网格）｜差异化 IV、可行近似最优工具｜供需联合 GMM 与过度识别检验｜Morrow–Skerlos 定价不动点｜蒙特卡洛 + 复现（Nevo 2000b 谷物、BLP 1995/1999 汽车、Knittel–Metaxoglou 2014）｜软件 PyBLP。

## 2. 一句话结论
把近年 BLP 估计的数值与计量改进合并成一套默认设置，写进开源 Python 包 PyBLP。蒙特卡洛和复现表明，按最佳实践估计时，**多个局部极小在识别良好的问题中很少见**；小样本表现可以很好，**“近似最优工具 + 设定正确的供给侧”时偏误基本消失**。最佳实践清单：
1. **内层反演**：SQUAREM 加速收缩（或 Jacobian 型的 LM），L∞ 容差 1E-14（建议区间 1E-14 至 1E-12），log-sum-exp 防溢出；
2. **外层优化**：解析梯度 + 参数盒约束 + 紧容差；优先 Knitro Interior/Direct，其次 SciPy 的 BFGS 类（L-BFGS-B）；不用 Nelder-Mead；多初值、多优化器互查，并检查一阶、二阶条件；
3. **积分**：随机系数少时用高阶 Gauss–Hermite 积规则；维数高时用稀疏网格或加扰 Halton；估计后用大量节点检验积分误差；
4. **工具**：第一阶段用差异化 IV（Gandhi–Houde，含“预期价格”），第二阶段（厂商行为已知时）换成可行近似最优工具（“approximate” 版即可）；
5. **供给侧**：设定正确时加入供给矩收益很大，成本移动变量越弱收益越大；设定错误（如真实为完全竞争）会让 α 有偏，可用 (32) 式检验；
6. **反事实定价**：用 Morrow–Skerlos 的 ζ-markup 不动点 (27)，不用朴素迭代 $p\leftarrow c+\eta(p)$；
7. **多维固定效应**：吸收（MAP 等）而不是加哑变量。

## 3. 研究问题、背景与动机
- **BLP 模型的两面**：本质是从观测份额到平均效用的非线性变量替换；替换后只剩线性 IV（仅需求）或两方程线性 IV（供需）。难点是替换的参数 $\theta_2$ 未知，目标函数是**模拟/近似的、非凸的**，只能迭代求解，没有收敛到全局最优的保证（p2）。
- **文献中的数值困境**：Knittel & Metaxoglou (2014) 发现大量局部极小，弹性、福利随初值和优化器大幅变化；Dubé, Fox & Su (2012) 指出内层容差过松导致误差传递，并提出 MPEC；Armstrong (2016) 认为产品数增多而无强成本移动变量时，BLP 工具变弱。担心研究者为算得快而牺牲模型丰富度（p2）。
- **缺少标准实现**：几乎每个研究者自写代码、各有调整，复现困难，也难以比较各种改进（p2）。
- **本文目标**：(1) 梳理 BLP 估计各环节（解不动点、优化、积分、解反事实均衡）的最佳实践；(2) 提供通用、可扩展的开源实现 PyBLP（`pip install pyblp`，文档 pyblp.readthedocs.io；依赖 NumPy、SciPy、SymPy、Patsy，以及吸收高维固定效应的 PyHDFE；可从 MATLAB（py 命令）、Julia（PyCall）、R（reticulate）调用，p2 脚注 1–3）；(3) 新结果：便于供需联合并吸收固定效应的问题写法；突出过度识别约束的最优工具表达式。
- **不讨论**：MPEC（Dubé–Fox–Su 2012；Conlon 2017 推广到广义经验似然）、Lee–Seo (2015) 近似估计量、Hong–Li–Li 的 Laplace 型估计量、Salanié–Wolak (2019) 线性 IV 近似估计量（适合找初值）、纯特征模型（Berry–Pakes 2007）、微观矩（Petrin 2002；BLP 2004a）。脚注 6：PyBLP 支持纯特征模型的近似与常见微观矩，但本文不评估其计量表现（p3–4）。

## 4. 文献综述（方向 → 代表文献 → 本文推进）
| 方向 | 代表文献 | 本文推进 |
|---|---|---|
| BLP 框架与应用 | BLP (1995, 1999, 2004a)；Berry (1994)；Nevo (2000a,b, 2001)；Petrin (2002)；Fan (2013)；Lee (2013)；Ho–Pakes (2014)；Bayer–Ferreira–McMillan (2007)；Nielson (2017) | 统一实现，默认采用最佳实践 |
| 识别 | Berry–Haile (2014)；Fox et al. (2012)；Berry–Linton–Pakes (2004b) | 用最优工具式子把排除约束、跨方程约束写明（与 Berry–Haile 平行） |
| 数值稳定性 | Knittel–Metaxoglou (2014)；Dubé–Fox–Su (2012)；Skrainka (2012a,b)；Judd–Skrainka (2011)；Brunner et al. (2017) | 复现并消除 K–M 的离散：紧容差 + 求积 |
| 收缩加速 | Reynaerts–Varadhan–Nash (2012)；Varadhan–Roland (2008) SQUAREM；DF-SANE；MINPACK（Powell、LM） | 系统比较，推荐 SQUAREM 或 LM |
| 最优工具 | Amemiya (1977)；Chamberlain (1987)；BLP (1995, 1999)；Reynaert–Verboven (2014) | 供需两组工具分开，模型**过度识别**；与 R–V 的恰好识别写法不同 |
| 差异化 IV | Gandhi–Houde (2019)（Local、Quadratic） | 蒙特卡洛确认其优于“特征之和” BLP 工具 |
| 积分 | Halton (1960)；Train (2000, 2009)；Bhat (2001)；Owen (1997, 2017)；Hess–Train–Polak (2006) MLHS；Heiss–Winschel (2008) 稀疏网格；Judd–Skrainka (2011) 单项式求积；Freyberger (2015) | 比较积分误差与参数表现 |
| 定价均衡 | Morrow–Skerlos (2010, 2011)；Caplin–Nalebuff (1991)；Konovalov–Sandor (2010)；Armstrong (2016)（朴素迭代出现循环） | 把 ζ-markup 不动点引入 IO，并用它构造最优工具 |
| 高维固定效应 | Correia (2016)（ivreghdfe）；Guimarães–Portugal (2010)；Fong–Saunders (2011) LSMR；Somaini–Wolak (2016) | 供需联合下仍可吸收固定效应 |
| RCNL | Brenkers–Verboven (2006)；Grigolon–Verboven (2014)；Miller–Weinberg (2017)；Conlon–Rao (2017)；Miravete–Seim–Thurk (2018) | 阻尼收缩 (15)，比较算法 |
| 厂商行为 | Bresnahan (1982)；Miller–Weinberg (2017) $\mathcal H_t(\kappa)$；Backus–Conlon–Sinkinson (2020)；Villas-Boas (2007)；Bonnet–Dubois (2010) | 供给矩的过度识别检验 (32) |

## 5. 数据
1. **蒙特卡洛设计（§5，p24–26）**：大致仿照 Armstrong (2016)，但**先抽效用与成本，再解出均衡价格和份额**（脚注 74：不解均衡则加价不内生，很多 BLP 工具的相关性条件不成立）。
   - 每种设定 1000 个合成数据集；$T=20$ 个市场；每市场厂商数 $F_t\in\{2,5,10\}$ 随机，每厂商产品数 $J_{ft}\in\{3,4,5\}$ 随机；样本量一般 $200<N<600$。
   - $(\xi_{jt},\omega_{jt})$ 为零均值二元正态，$\sigma_\xi^2=\sigma_\omega^2=0.2$，$\sigma_{\xi\omega}=0.1$。
   - 需求线性特征 $[1,x_{jt},p_{jt}]$；供给特征 $[1,x_{jt},w_{jt}]$；$x_{jt},w_{jt}\sim U(0,1)$；异质性 $\mu_{ijt}=\sigma_x x_{jt}\nu_{it}$，$\nu_{it}\sim N(0,1)$，每市场 1000 个个体。
   - 真值：$[\beta_0,\beta_x,\alpha]=[-7,6,-1]$，$\sigma_x=3$，外部品份额一般 $0.8<s_{0t}<0.9$；$[\gamma_0,\gamma_x,\gamma_w]=[2,1,0.2]$，线性边际成本 $c_{jt}=[1,x_{jt},w_{jt}]\gamma+\omega_{jt}$；基准下 $\mathrm{Corr}(p_{jt},w_{jt})\approx0.2$，**成本移动工具偏弱**。
   - 三个变体：**Simple**（基准）；**Complex**（价格加随机系数 $\sigma_p=0.2$，非线性特征为 $[x,p]$）；**RCNL**（加嵌套参数 $\rho=0.5$，每厂商的产品随机分入 $H=2$ 个组）。
   - 用均衡价格份额求解器 (27) 生成 $(p,s)$；计算在 NYU HPC 集群上完成（脚注 80）。
2. **Nevo (2000b) 谷物“假数据”（§6，p39）**：含可观测人口特征（income、income²、age、child）、不可观测异质性和产品固定效应；$J=24$ 个产品（p9）；原始工具随数据提供，原文为一步 GMM、2SLS 权重 $(Z'Z)^{-1}$（脚注 95）；数据随 PyBLP 分发。
3. **BLP (1995, 1999) 汽车数据（§6，p40）**：无人口交互、无产品固定效应，但有供给侧，价格系数随收入变化。数据取自 Andrews–Gentzkow–Shapiro (2017) 的复现包（脚注 98）。按 BLP (1999) 把 $\log(y_i-p_j)$ 换成一阶线性近似 $p_j/y_i$，否则有个体 $p_j>y_i$。原文部分配置（如抽样）未随数据提供。
4. **Knittel–Metaxoglou (2014) 复现（p40–43）**：Nevo 配置 + BLP 问题的仅需求版本；50 个随机初值 × 多个优化器（Knitro 与 SciPy 共 7 种配置，图 7 注）。
5. **固定效应模拟（表 3 注）**：Simple 设定下令 $T=6^4$、$F_t=J_f=6$，得 $N=6^6=46{,}656$ 个产品（文字层为 “T = 64”“N = 66”，上标被压平；$T=6^4=1296$ 为 [D]），按产品序号 $n$ 的 mod/div 运算分配 1–3 维固定效应，FE 取自标准均匀分布；100 次模拟取中位数。

## 6. 模型与算法如何构建
### 6.1 模型
**记号（表 1，p4）**：$j$ 产品，$t$ 市场，$i$ 个体，$f$ 厂商，$h$ 嵌套组。参数分三块：$\theta_1$（$K_1$ 维线性需求参数，去掉 FE 后记 $\beta$）；$\theta_2$（$K_2$ 维非线性公共参数，含价格系数 $\alpha$、嵌套参数 $\rho$ 与异质性参数 $\tilde\theta_2$）；$\theta_3$（$K_3$ 维线性供给参数，去掉 FE 后记 $\gamma$）。$\mathcal H_t$ 为持股/所有权矩阵，$\Delta_t$ 为厂商内需求导数矩阵，$\eta_{jt}$ 为多产品 Bertrand 加价，$Z$ 工具，$W$ 权重，$g$ 样本矩，$q$ 目标函数。

**需求**（(1)–(3)，p4–5）：
$$U_{ijt}=\delta_{jt}+\mu_{ijt}+\epsilon_{ijt},\qquad U_{i0t}=\epsilon_{i0t}$$
$$d_{ijt}=\begin{cases}1 & U_{ijt}>U_{ikt}\ \forall k\ne j\\ 0 & \text{otherwise}\end{cases},\qquad s_{jt}=\int d_{ijt}(\boldsymbol\delta_t,\boldsymbol\mu_{it})\,d\boldsymbol\mu_{it}\,d\boldsymbol\epsilon_{it}$$
$$s_{jt}(\boldsymbol\delta_t,\tilde\theta_2)=\int\frac{\exp(\delta_{jt}+\mu_{ijt})}{\sum_{k\in J_t}\exp(\delta_{kt}+\mu_{ikt})}\,f(\boldsymbol\mu_{it}\mid\tilde\theta_2)\,d\boldsymbol\mu_{it}\qquad(3)$$
- **反演**：$\boldsymbol\delta_t\equiv D_t^{-1}(\boldsymbol{\mathcal S}_t,\tilde\theta_2)$，每个市场 $J_t$ 个方程、$J_t$ 个未知数。
- **解析反演（脚注 10、p9）**：logit：$D_t^{-1}=\log s_{jt}-\log s_{0t}$；嵌套 logit（Berry 1994）：$\delta_{jt}=\log\mathcal S_{jt}-\log\mathcal S_{0t}-\rho\log\mathcal S_{j|ht}$，$\mathcal S_{j|ht}$ 为组内份额。
- **线性部分**（(4)，p5）：
$$\delta_{jt}(\boldsymbol{\mathcal S}_t,\tilde\theta_2)=[x_{jt},v_{jt}]\beta-\alpha p_{jt}+\xi_{jt},\qquad E[\xi_{jt}Z^D_{jt}]=0$$
  $v_{jt}$ 为排除在供给外的需求移动变量；$Z^D$ 含 $x_{jt},v_{jt}$。McFadden–Train (2000)：任何 RUM 都可由足够基的混合 logit 近似（脚注 9）。

**供给**（(5)(6)，p5–6）：多产品厂商在每个市场同时定价，
$$s_{jt}(\boldsymbol p_t)+\sum_{k\in J_{ft}}\frac{\partial s_{kt}}{\partial p_{jt}}(\boldsymbol p_t)\,(p_{kt}-c_{kt})=0$$
$$\boldsymbol s_t(\boldsymbol p_t)=\Delta_t(\boldsymbol p_t)(\boldsymbol p_t-\boldsymbol c_t),\qquad \underbrace{\Delta_t(\boldsymbol p_t)^{-1}\boldsymbol s_t(\boldsymbol p_t)}_{\boldsymbol\eta_t(\boldsymbol p_t,\boldsymbol s_t,\theta_2)}=\boldsymbol p_t-\boldsymbol c_t\qquad(5)$$
$$\Delta_t(\boldsymbol p_t)\equiv-\mathcal H_t\odot\frac{\partial\boldsymbol s_t}{\partial\boldsymbol p_t}(\boldsymbol p_t),\qquad (j,k)\text{ 元为 }\partial s_{jt}/\partial p_{kt}\qquad(6)$$
- $\mathcal H_t$ 的 $(j,k)$ 元在 $j,k$ 同属某厂商时为 1（脚注 11）；可换成单产品寡头、垄断、或参数化的 $\mathcal H_t(\kappa)$（Miller–Weinberg 2017；Backus–Conlon–Sinkinson 2020 用 PyBLP 检验行为）。
- **⚠ 转置（总表校正）**：按 $(j,k)=\partial s_{jt}/\partial p_{kt}$ 拼的 $\Delta$ 与上面的标量 FOC（用 $\partial s_{kt}/\partial p_{jt}$）差一次转置，与 BLP (3.4) 的 $\Delta_{jr}=-\partial s_r/\partial p_j$ 也差一次转置。**编码时一律按 BLP 方向**：$\Delta^{\rm BLP}=-\mathcal H_t\odot(\partial\boldsymbol s_t/\partial\boldsymbol p_t)^{\top}$，$\boldsymbol\eta_t=(\Delta^{\rm BLP})^{-1}\boldsymbol s_t$。只有每个消费者对各产品的价格边际效用相同（准线性价格混合 logit），Jacobian 才对称、两种写法一致；$\alpha\ln(y_i-p_j)$ 等收入效应规格下不对称，必须按 BLP 方向实现。
- **边际成本**（(7)，p6）：
$$f_{MC}\big(p_{jt}-\eta_{jt}(\theta_2)\big)=f_{MC}(c_{jt})=x_{jt}\gamma_1+w_{jt}\gamma_2+\omega_{jt},\qquad E[\omega_{jt}Z^S_{jt}]=0$$
  $f_{MC}$ 常取恒等，也可取 $\log$（保证 mc 为正，脚注 12）；$w_{jt}$ 为排除在需求外的成本移动变量。可让 mc 依赖产量（附录 A.3，见 6.5）。
- **堆叠 GMM**（(8)，p6）：
$$g(\theta)=\begin{bmatrix}g_D(\theta)\\ g_S(\theta)\end{bmatrix}=\begin{bmatrix}\frac1N\sum_{j,t}\xi_{jt}Z^D_{jt}\\ \frac1N\sum_{j,t}\omega_{jt}Z^S_{jt}\end{bmatrix},\qquad \min_\theta\ q(\theta)\equiv g(\theta)'Wg(\theta),\quad \theta=[\beta,\alpha,\tilde\theta_2,\gamma]$$
  脚注 13：部分文献把目标乘以 $N^2$（Nevo 2000b 写 $q=\xi'Z_DWZ_D'\xi$）；本文不缩放。脚注 42：**PyBLP 默认乘以 $N$**，两步 GMM 后目标值即 Hansen J 统计量。
- **完整程序 (9)（p7，已看图）**：在 (8) 外加 $\xi_{jt}=\delta_{jt}-[x_{jt},v_{jt}]\beta+\alpha p_{jt}$，$\omega_{jt}=f_{MC}(p_{jt}-\eta_{jt})-[x_{jt},w_{jt}]\gamma$，$\boldsymbol\eta_t=\Delta_t(\theta_2)^{-1}\boldsymbol s_t$，$\mathcal S_{jt}=s_{jt}(\boldsymbol\delta_t,\theta_2)$。每个 $\theta_2$ 参数至少需要一个排除工具（脚注 14：$D^{-1}$ 依赖全市场的内生份额）。要解两次：第一次得一致的 $W$，第二次得有效 GMM。
- **仅需求程序 (10)**：去掉 $g_S$、$\omega$、$\eta$；用户不给供给侧时 PyBLP 即估此式。不加供给侧的理由：$f_{MC}$ 或行为 $\mathcal H_t$ 可能设错（共谋、Cournot、双重加价等，脚注 15）。

**RCNL**（(14)(15)，p8–9，已看图）：$\theta_2\equiv[\alpha,\rho,\tilde\theta_2]$，$U_{ijt}=\delta_{jt}+\mu_{ijt}(\tilde\theta_2)+\epsilon_{ijt}(\rho)$，
$$s_{jt}(\boldsymbol\delta_t,\theta_2)=\int\frac{\exp[(\delta_{jt}+\mu_{ijt})/(1-\rho)]}{\exp[IV_{iht}/(1-\rho)]}\cdot\frac{\exp IV_{iht}}{1+\sum_{h\in H}\exp IV_{iht}}\,f(\boldsymbol\mu_{it}\mid\tilde\theta_2)\,d\boldsymbol\mu_{it},\quad IV_{iht}=(1-\rho)\log\sum_{j\in J_{ht}}\exp\Big(\frac{\delta_{jt}+\mu_{ijt}}{1-\rho}\Big)\qquad(14)$$
$$\boldsymbol\delta_t\leftarrow\boldsymbol\delta_t+(1-\rho)\big[\log\boldsymbol{\mathcal S}_t-\log\boldsymbol s_t(\boldsymbol\delta_t,\theta_2)\big]\qquad(15)$$
未阻尼的 BLP 收缩在 RCNL 下不再是压缩映射，须乘 $(1-\rho)$ 阻尼；$\rho\to1$ 时收敛可任意变慢（脚注 21）。脚注 19：$\rho$ 可按组 $\rho_h$ 变化，PyBLP 两种都支持。脚注 20：(15) 与 Grigolon–Verboven (2014) 不完全一致，因后者有小排版错误。

### 6.2 估计算法
**算法 1：嵌套不动点（NFXP，p8，已看图）**。对每个 $\theta_2$：
1. (a) 每个市场解 $\mathcal S_{jt}=s_{jt}(\boldsymbol\delta_t,\theta_2)$，得 $\hat{\boldsymbol\delta}_t(\theta_2)$；
2. (b) 用 $\hat{\boldsymbol\delta}_t$ 构造 $J_t\times J_t$ 的 $\Delta_t(\boldsymbol p_t,\hat{\boldsymbol\delta}_t(\theta_2),\theta_2)$（注意转置）；
3. (c) 解 $J_t\times J_t$ 线性方程组得 $\hat{\boldsymbol\eta}_t(\theta_2)=\Delta_t^{-1}\boldsymbol{\mathcal S}_t$；
4. (d) 堆叠后用线性 IV-GMM 求 $[\hat\theta_1(\theta_2),\hat\theta_3(\theta_2)]$。**本文写法把 $\alpha p$ 放到左边**：
$$\hat\delta_{jt}(\boldsymbol{\mathcal S}_t,\theta_2)+\alpha p_{jt}=[x_{jt},v_{jt}]\beta+\xi_{jt},\qquad f_{MC}(p_{jt}-\hat\eta_{jt}(\theta_2))=[x_{jt},w_{jt}]\gamma+\omega_{jt}\qquad(11)$$
5. (e) 残差 $\hat\xi_{jt}(\theta_2)=\hat\delta_{jt}(\theta_2)-[x_{jt},v_{jt}]\hat\beta(\theta_2)+\alpha p_{jt}$，$\hat\omega_{jt}(\theta_2)=\hat c_{jt}(\theta_2)-[x_{jt},w_{jt}]\hat\gamma(\theta_2)$（(12)）；
6. (f) 堆叠矩 $g(\theta_2)=\big[\frac1N\sum\hat\xi_{jt}Z^D_{jt};\ \frac1N\sum\hat\omega_{jt}Z^S_{jt}\big]$（(13)）；
7. (g) $q(\theta_2)=g(\theta_2)'Wg(\theta_2)$。
- 关键：加价 $\eta_{jt}$ 只依赖 $\theta_2$（脚注 17：$\partial s_{kt}/\partial p_{jt}=-\int\alpha_i s_{ikt}[1(j=k)-s_{ijt}]f(\boldsymbol\mu_{it},\alpha_i\mid\theta_2)d\boldsymbol\mu_{it}$，只依赖含 $\alpha$ 的 $\theta_2$），因此 $\alpha p$ 可移到左边，供需可以一起集中掉线性参数。
- 优点：只对 $K_2$ 个非线性参数搜索，Hessian 仅 $K_2\times K_2$；线性参数（含大量 FE）“几乎免费”；(a)–(c) 可按市场并行，(a) 之外都很便宜。缺点：目标是 $\theta_2$ 的复杂隐函数，有异质性就非凸，难度随 $K_2$ 快速上升。

**集中掉线性参数（附录 A.1，(A1)–(A5)）**：
$$Y^D_{jt}\equiv\hat\delta_{jt}(\theta_2)+\alpha p_{jt}=X^D_{jt}\beta+\xi_{jt},\qquad Y^S_{jt}\equiv p_{jt}-\hat\eta_{jt}(\theta_2)=X^S_{jt}\gamma+\omega_{jt}$$
$$\begin{bmatrix}Y_D\\Y_S\end{bmatrix}=\begin{bmatrix}X_D&0\\0&X_S\end{bmatrix}\begin{bmatrix}\beta\\\gamma\end{bmatrix}+\begin{bmatrix}\xi\\\omega\end{bmatrix}\ (2N\times1),\qquad \mathcal Y=\tfrac1N\begin{bmatrix}Z_D'&0\\0&Z_S'\end{bmatrix}\begin{bmatrix}Y_D\\Y_S\end{bmatrix},\ \mathcal X=\tfrac1N\begin{bmatrix}Z_D'X_D&0\\0&Z_S'X_S\end{bmatrix}$$
$$\begin{bmatrix}\hat\beta(\theta_2)\\\hat\gamma(\theta_2)\end{bmatrix}=(\mathcal X'W\mathcal X)^{-1}\mathcal X'W\mathcal Y\qquad(A5)$$
$M=M_D+M_S$ 个矩，用与整体问题相同的 $M\times M$ 权重 $W$。脚注 102：除非假设 $\mathrm{Cov}(\xi,\omega)=0$，否则不能分两条方程各自回归。（文中 (Y^S) 用 $p-\hat\eta$，对应 $f_{MC}$ 为恒等；一般情形为 $f_{MC}(p-\hat\eta)$。）

**多维固定效应吸收（§3，p9–10，(16)）**：例如 Nevo 的 $\delta_{jt}=[x,v]\beta-\alpha p_{jt}+\xi_j+\Delta\xi_{jt}$。Nielsen 周度 UPC-门店数据中 $J_t>3500$，约 $T=500$ 周（2006–2016），100 家店的店-周 FE 约 50,000 个，UPC-店 FE 可达 100,000 以上。做法：
- 写成 (16) 的线性 IV 后，单维 FE 用组内去均值；两维 FE 用交替投影（MAP）迭代去均值，两维不相关时一次即可，相关时迭代很多次；LSDV 要求逆 $(J+T)\times(J+T)$ 矩阵，内存不可行。
- **BLP 的特殊之处**：$X$ 不变，可**只残差化一次**；左边 $Y$（$\hat\delta+\alpha p$ 与 $\hat c$）随 $\theta_2$ 变，每次都要残差化。PyBLP 支持多种 MAP 加速、LSMR（Fong–Saunders 2011）、两维 FE 的 Somaini–Wolak (2016)（脚注 24）。

**内层：解份额方程（p10–13）**：
- 按市场解 $T$ 个 $J_t$ 维系统（而非 $N$ 维），可并行（脚注 25：MPEC 的稀疏性来自同一事实）。
- **停止规则 (18)**：$\|\log\mathcal S_{jt}-\log s_{jt}(\boldsymbol\delta_t,\theta_2)\|_\infty\le\epsilon_{tol}$，**推荐 1E-14 至 1E-12**（双精度机器精度约 1E-16）；太松则误差传入估计（Dubé–Fox–Su 2012；Lee–Seo 2016），太紧可能永远达不到。
- **牛顿型 (19)**：$\boldsymbol\delta^{h+1}_t\leftarrow\boldsymbol\delta^h_t-\lambda\,\Psi_t^{-1}(\boldsymbol\delta^h_t,\theta_2)\,\boldsymbol s_t(\boldsymbol\delta^h_t,\theta_2)$，$\Psi_t=\partial\boldsymbol s_t/\partial\boldsymbol\delta_t$；实际解线性方程 $\Psi_t(\boldsymbol\delta^{h+1}_t-\boldsymbol\delta^h_t)=-\boldsymbol s_t(\boldsymbol\delta^h_t,\theta_2)$ 更快（脚注 27）。（本卡注：残差应为 $\boldsymbol s_t(\boldsymbol\delta)-\boldsymbol{\mathcal S}_t$，原式省略了 $-\boldsymbol{\mathcal S}_t$。）$\Psi$ 元素 $\partial s_{jt}/\partial\delta_{kt}=\int[1(j=k)s_{ijt}-s_{ijt}s_{ikt}]f\,d\boldsymbol\mu$（脚注 30）；主要成本是算 $J_t^2$ 个积分，而非求逆（$J_t=1{,}000$ 时求逆也容易）。外部品份额为正时 $\Psi$ 严格对角占优、非奇异（脚注 28）。
- **Levenberg–Marquardt（推荐的 Jacobian 法）**：最小化 $\sum_j[\mathcal S_{jt}-s_{jt}(\boldsymbol\delta_t,\theta_2)]^2$，更新 $\boldsymbol\delta^h_t+\boldsymbol x_t$，
$$[\Psi_t'\Psi_t+\lambda\,\mathrm{diag}(\Psi_t'\Psi_t)]\,\boldsymbol x_t=\Psi_t'[\boldsymbol{\mathcal S}_t-\boldsymbol s_t(\boldsymbol\delta_t,\theta_2)]\qquad(20)$$
  （右边文字层为 “Ψ_t[S_t′ − s_t]”，按标准 LM 写作 $\Psi_t'$，p11 无页图，待核。）$\lambda=0$ 为高斯–牛顿步，$\lambda$ 大时沿梯度方向；对角项保证近奇异时仍可逆。实现：`scipy.optimize.root` 的 `lm` 选项（MINPACK 的 LMDER，脚注 29、81）。
- **BLP 收缩 (21)（已看图）**：$f:\ \boldsymbol\delta^{h+1}_t\leftarrow\boldsymbol\delta^h_t+\log\boldsymbol{\mathcal S}_t-\log\boldsymbol s_t(\boldsymbol\delta^h_t,\tilde\theta_2)$。线性收敛，速率正比于 $L/(1-L)$，Lipschitz 常数 $L(\tilde\theta_2)=\max_{\boldsymbol\delta_t}\|I_{J_t}-\partial\log\boldsymbol s_t/\partial\boldsymbol\delta_t\|_\infty<1$。脚注 32（本文新推导）：$\partial\log\boldsymbol s_t/\partial\boldsymbol\delta_t=I_{J_t}-\mathrm{diag}^{-1}(\boldsymbol s_t)\Gamma_t(\tilde\theta_2)$，其中这里 $\Gamma_{jkt}=\int s_{ijt}s_{ikt}f\,d\boldsymbol\mu$（不含 $\alpha_i$，与 (26) 的 $\Gamma$ 不同）；故 $L=\max_{\boldsymbol\delta}[\max_j s_{jt}^{-1}\sum_k|\Gamma_{jkt}|]$，粗略近似 $\max_j\sum_k|s_{kt}|\cdot|\mathrm{Corr}(s_{ijt},s_{ikt})|<1-s_{0t}$。**外部品份额越小，$L$ 越大，迭代越多。**
- **SQUAREM 加速 (22)（已看图）**：
$$\boldsymbol\delta^{h+1}_t\leftarrow\boldsymbol\delta^h_t-2\alpha^h\boldsymbol r^h+(\alpha^h)^2\boldsymbol v^h,\quad \alpha^h=\frac{(\boldsymbol v^h)'\boldsymbol r^h}{(\boldsymbol v^h)'\boldsymbol v^h},\quad \boldsymbol r^h=f(\boldsymbol\delta^h_t)-\boldsymbol\delta^h_t,\quad \boldsymbol v^h=f(f(\boldsymbol\delta^h_t))-2f(\boldsymbol\delta^h_t)+\boldsymbol\delta^h_t$$
  （$\alpha^h$ 为步长，不是价格系数。）一般比直接迭代快 3–6 倍；步数接近牛顿法，但不算 Jacobian，所需量都是迭代中本来就要算的；**理论上无收敛保证**（不再是压缩）。PyBLP 含 R 包 SQUAREM 的 Python 移植（脚注 34）。DF-SANE（$\boldsymbol\delta^{h+1}\leftarrow\boldsymbol\delta^h-\alpha^hf(\boldsymbol\delta^h)$）表现相近但略慢、略不稳。结论：SQUAREM 是最快最稳的加速不动点法；LM 可靠性相近、速度略好，但依问题而定。

**外层：优化（p13–14、35–36）**：
- 问题非凸（无随机系数时全局凸，脚注 35）：Hessian 不必半正定，任何算法都不保证在有限时间内找到全局最小。必须核查一阶条件（梯度接近 0）和二阶条件（Hessian 特征值全正）；有界约束时用投影梯度和约化 Hessian（脚注 36）。**PyBLP 默认报告两者。**
- 支持 SciPy 全部优化器与商业的 Knitro，也可接任何 Python 函数（文档中有网格暴力搜索的“自定义”例子，脚注 37）。**不推荐 Nelder-Mead**（Dubé–Fox–Su 2012、Knittel–Metaxoglou 2014 及本文均发现导数法更快更稳，脚注 38）。
- **解析梯度**：对任意用户模型（含供给矩、FE）都算解析梯度（脚注 39：文献中找不到供需联合估计用解析梯度的先例，因 $\partial\eta/\partial\theta_2$ 很复杂）。脚注 40：自动微分有前景，但交给 AD 库会削弱对数值错误的处理。
- **盒约束** $\theta_2^{(\ell)}\in[\underline\theta_2^{(\ell)},\bar\theta_2^{(\ell)}]$：如需求向下倾斜、随机系数方差非负且有界；能防止大随机系数引发的数值问题。脚注 41：因优化的是协方差的 Cholesky 根 $LL'=\Sigma$，目标关于 0 对称，$g(\sigma)=g(-\sigma)$，非负约束不是必需。
- **终止容差**：软件默认值常偏松，$N$ 大时对目标尺度敏感的终止条件更糟；若提前终止要换配置。脚注 77：MATLAB 求解器报告绝对容差，SciPy 报告相对容差，数值不可直接比较。
- **推荐顺序**：有 Knitro 先试 Interior/Direct（缺点是收费，脚注 43），再试 BFGS 类（最好带约束，如 L-BFGS-B）；对 NFXP 来说，**盒约束、解析梯度、紧容差比选哪个求解器更重要**（PyBLP 默认都已设置）。商业求解器对 MPEC 可能更有优势（脚注 44）。

**数值问题与技巧（p14–15）**：
- logit 分母 $\sum_j\exp(\delta_{jt}+\mu_{ijt})$ 中数量级差异大（如 $\exp(-5)\approx0.0067$ 与 $\exp(30)>10^{13}$）会丢精度（IEEE-754 双精度约 15 位有效数字）；$\exp(800)$ 会溢出，导致 $s_{jt}\to1$、其他 $\to0$，反演失败（脚注 45）。
- 对策：盒约束限制随机系数；按市场计算、避免超大求和；Kahan 求和（Python `math.fsum`）太慢不默认；扩展精度（`pyblp.options.dtype` 设为 `numpy.longdouble`，多数 Unix 上是 128 位 long double）更慢且不改善统计表现，但份额极小或产品极多时可能有用（脚注 47）。
- **默认采用防溢出的 log-sum-exp**：$\mathrm{LSE}(x)=\log\sum_k\exp x_k=a+\log\sum_k\exp(x_k-a)$，$a=\max\{0,\max_kx_k\}$；额外成本可忽略。它不防下溢；$W$ 或 $\Delta_t$ 可能近奇异。PyBLP 遇数值错误时用“合理”替代（上一轮迭代的值或 Moore–Penrose 伪逆）并给出警告（脚注 48）。
- 常见“技巧”收效甚微：用 $\exp(\delta)$ 迭代（现代 CPU 上 $\exp$ 很快，十亿次不到 1 秒）；用上一个 $\theta_2$ 的 $\delta$ 作热启动（SQUAREM、LM 对初值不敏感）；Nevo (2000b) 与 K–M 的“全市场堆叠累加和”向量化不如按市场并行，且 $T\to\infty$ 时丢精度。

### 6.3 工具变量
**表 2 工具集（p25）**：
- $Z^{\rm Own}_{jt}=\{1,x_{jt},w_{jt},x^2_{jt},w^2_{jt},x_{jt}w_{jt}\}$（自身特征的全部二次交互，可视为逼近最优 IV 的筛基，脚注 79）；
- $Z^{\rm Sums}_{jt}=\{Z^{\rm Own},\ \sum_{k\in J_{ft}\setminus\{j\}}1,\ \sum_{k\notin J_{ft}}1,\ \sum_{k\in J_{ft}\setminus\{j\}}x_{kt},\ \sum_{k\notin J_{ft}}x_{kt}\}$（BLP 工具：同厂其他产品与对手产品分开）；
- $Z^{\rm Local}_{jt}=\{Z^{\rm Own},\ \sum_{k\in J_{ft}\setminus\{j\}}1(|d_{jkt}|<\mathrm{SD}(d)),\ \sum_{k\notin J_{ft}}1(|d_{jkt}|<\mathrm{SD}(d))\}$（差异化 IV 局部版：一个标准差内的产品个数）；
- $Z^{\rm Quad}_{jt}=\{Z^{\rm Own},\ \sum_{k\in J_{ft}\setminus\{j\}}d^2_{jkt},\ \sum_{k\notin J_{ft}}d^2_{jkt}\}$（二次版：距离平方和）；
- $d_{jkt}=x_{kt}-x_{jt}$，对 $x_{jt}$ 中每个特征计算，SD 在所有市场的产品对上合并计算（表注文字层写作 “$d_{kt}-d_{jt}$”，应为 $x$ 的差）。
- **Complex** 额外加入“预期价格” $E[p_{jt}\mid Z_t]$ 作为一个 $x$：价格对全部外生变量（含上述工具）线性回归的拟合值（Gandhi–Houde）；**RCNL** 额外加入同市场同组产品数（Berry 1994；Gandhi–Houde）。
- 这些工具意在与内生加价 $\eta_{jt}(\theta_2,\boldsymbol x_t,\boldsymbol w_t)$ 及 $D_t^{-1}(\mathcal S_t,\theta_2)$ 相关，二者都依赖全市场产品特征。

**最优工具推导（§4，p19–21；(28)–(31) 文字层严重错乱，PDF p20 无核对页图，以下按可辨部分重建，待核）**：
- 条件矩 $E[\xi_{jt}\mid Z^D_{jt}]=0$、$E[\omega_{jt}\mid Z^S_{jt}]=0$；渐近方差依赖 $D'\Omega^{-1}D$，$D=E[(\partial\xi_{jt}/\partial\theta,\ \partial\omega_{jt}/\partial\theta)\mid Z_t]$，$\Omega=E[(\xi_{jt},\omega_{jt})'(\xi_{jt},\omega_{jt})\mid Z_t]$（p19 已看图）。Chamberlain (1987)：最优工具为每个观测的期望 Jacobian 贡献 $E[D_{jt}(Z_t)\Omega_{jt}^{-1}\mid Z_t]$；因对 $(\xi,\omega)$ 的期望无闭式，称“近似”。
- (28)：$D_{jt}$ 为 $(K_1+K_2+K_3)\times2$：$\beta$ 行为 $[-x_{jt},0]$、$[-v_{jt},0]$；$\alpha$ 行与 $\tilde\theta_2$ 行为 $[\partial\xi_{jt}/\partial\cdot,\ \partial\omega_{jt}/\partial\cdot]$；$\gamma$ 行为 $[0,-x_{jt}]$、$[0,-w_{jt}]$。$\Omega_t=\begin{bmatrix}\sigma^2_\xi&\sigma_{\xi\omega}\\\sigma_{\xi\omega}&\sigma^2_\omega\end{bmatrix}$（脚注 66：蒙特卡洛假设 $(\xi,\omega)$ 跨 $j,t$ 独立同分布，异方差、聚类可直接推广）。
- (29)：$D_{jt}\Omega_t^{-1}=\frac{1}{\sigma^2_\xi\sigma^2_\omega-\sigma^2_{\xi\omega}}\begin{bmatrix}-\sigma^2_\omega x_{jt}&\sigma_{\xi\omega}x_{jt}\\-\sigma^2_\omega v_{jt}&\sigma_{\xi\omega}v_{jt}\\\sigma^2_\omega\frac{\partial\xi_{jt}}{\partial\alpha}-\sigma_{\xi\omega}\frac{\partial\omega_{jt}}{\partial\alpha}&\sigma^2_\xi\frac{\partial\omega_{jt}}{\partial\alpha}-\sigma_{\xi\omega}\frac{\partial\xi_{jt}}{\partial\alpha}\\\sigma^2_\omega\frac{\partial\xi_{jt}}{\partial\tilde\theta_2}-\sigma_{\xi\omega}\frac{\partial\omega_{jt}}{\partial\tilde\theta_2}&\sigma^2_\xi\frac{\partial\omega_{jt}}{\partial\tilde\theta_2}-\sigma_{\xi\omega}\frac{\partial\xi_{jt}}{\partial\tilde\theta_2}\\\sigma_{\xi\omega}x_{jt}&-\sigma^2_\xi x_{jt}\\\sigma_{\xi\omega}w_{jt}&-\sigma^2_\xi w_{jt}\end{bmatrix}$
- (30)：每列第 1 与第 5 个元素都是 $x_{jt}$ 的线性函数（共线），用 0/1 矩阵 $\Theta$ 作 Hadamard 积，把第 1 列的第 5 元（供给块的 $x$）和第 2 列的第 1 元（需求块的 $x$）置 0。
- (31)：$Z^{\rm Opt,D}_{jt}\equiv E[(D_{jt}(Z_t)\Omega_t^{-1}\odot\Theta)_{\cdot1}\mid Z_t]$，维数 $K_1+K_2+(K_3-K_x)$；$Z^{\rm Opt,S}_{jt}\equiv E[(D_{jt}(Z_t)\Omega_t^{-1}\odot\Theta)_{\cdot2}\mid Z_t]$，维数 $K_2+K_3+(K_1-K_x)$（$K_x$ 为共同外生特征 $x$ 的维数）。线性部分的最优工具只是按协方差缩放的外生变量；$\theta_2$ 的最优工具是数据的非线性函数，且**供需两侧不同**（脚注 68：仅在刀刃情形下相同；$Z^D$ 与 $Z^S$ 因排除变量不同而永远不应相同）。
- **识别计数**：$K_3-K_x$ 个成本移动 $w$（排除在需求外）+ $K_1-K_x$ 个需求移动 $v$（排除在供给外）给出排除约束；加上跨方程约束，共 $2(K-K_x)$ 个约束、$K$ 个参数，即 $K-2K_x$ 个过度识别约束；其中额外的 $K_2$ 个来自每个 $\theta_2$（含 $\alpha$）都有两条约束。
- **Remark 1**：排除约束来自“进入另一条方程的东西”；$w$ 为需求提供关于 $\theta_2$（含 $\alpha$）的过度识别约束，$v$ 为供给提供关于 $\theta_2$（与加价）的约束；两侧的连接是内生加价 $\eta_{jt}(\theta_2,\xi_t,\omega_t)$，故 $(\partial\xi/\partial\theta_2,\partial\omega/\partial\theta_2)$ 型工具被称作数量移动或加价移动变量。Backus–Conlon–Sinkinson (2020) 用 (30) 检验厂商行为（脚注 69）。
- **Remark 2（与 Reynaert–Verboven 2014 的差别）**：R–V 似乎把 (29) 按行求和并去掉第 1 或第 3 行，得 $K=K_1+K_2+K_3$ 个工具，恰好识别；因堆叠 $(\xi_t,\omega_t)$，实际有 $2N$ 个观测，相当于施加 $E[\xi Z^D]+E[\omega Z^S]=0$，而非分别施加两组矩。R–V 主设定也不是供需联合（脚注 70）。
- **Remark 3（半参数基替代）**：Newey (1990)、Ai–Chen (2003)、Donald–Imbens–Newey (2009) 的筛基 $E[\xi A(Z_t)]=0$ 有维数灾难和“多矩”问题（Newey–Smith 2004；脚注 71：多项式基 $(1,x^2,x^3,x^4)$ 高度相关）；Gandhi–Houde 的差分二阶多项式基性质较好。

**算法 2：可行近似最优 IV（BLP 1999 配方，p23）**。得到初始估计 $\hat\theta=[\hat\beta,\hat\alpha,\hat{\tilde\theta}_2,\hat\gamma]$ 后，对每个市场：
1. 由 $(\hat\xi_{jt},\hat\omega_{jt})$ 的协方差得 $\Omega_{jt}^{-1}$ 的初始估计（可独立同分布或按任意层级聚类）；
2. 按下列选项之一抽 $J_t\times2$ 的结构误差 $(\xi^*_t,\omega^*_t)$；
3. 算 $\hat Y^S_{jt}=\hat c_{jt}=[x_{jt},w_{jt}]\hat\gamma+\omega^*_{jt}$ 与效用外生部分 $\hat Y^D_{jt}=[x_{jt},v_{jt}]\hat\beta+\xi^*_{jt}$；
4. 用 (27) 的 ζ-markup 法解均衡 $(\hat{\boldsymbol p}_t,\hat{\boldsymbol s}_t)$（不涉及任何内生量）；
5. 把 $(\hat{\boldsymbol p}_t,\hat{\boldsymbol s}_t,\boldsymbol x_t,\boldsymbol w_t)$ 当数据，求 $\hat\xi_t$、$\hat\omega_t$；
6. 用附录 A.2 的解析公式算 $\partial\hat\xi_{jt}/\partial\theta_2$、$\partial\hat\omega_{jt}/\partial\theta_2$ 与 $\hat D_{jt}$；
7. 对多次抽样平均，得 $E[\hat D_{jt}\mid Z_t]$。
- 三种抽样选项（PyBLP 都提供）：(a) **approximate**：用期望 $(0,0)$ 代替（BLP 1999 的做法），仅当 $(\xi,\omega)$ 很小时近似好；(b) **asymptotic**：从 $N(0,\hat\Omega)$ 抽；(c) **empirical**：从 $(\hat\xi,\hat\omega)$ 联合经验分布中抽，需可交换性假设。
- 可行性来自快速均衡求解器：大问题几分钟，BLP (1995) 或 Nevo (2000b) 这类小问题几秒；**“approximate” 与更贵的选项表现一样好**；PyBLP 中只需图 6 最后两行代码。
- 局限：要有生成 $(\xi^*,\omega^*)$ 的方法和其协方差估计；$2J_t$ 维积分在偏态分布下难近似；依赖供给侧设定正确（真实为共谋时会出问题）。脚注 73：R–V 在完全竞争假设下算 $E[p\mid Z]=E[c\mid Z]=[x,w]\gamma+\hat\omega$；Gandhi–Houde 用回归得 $\hat p$ 来构造 $d_{jkt}=\hat p_{kt}-\hat p_{jt}$。
- **仅需求时**：失去跨方程约束，但保留 $w$ 带来的 $K_3-K_x$ 个需求排除约束；无 mc 模型、不能解均衡，用户提供 $E[\boldsymbol p_t\mid Z^D_t]$ 或由 PyBLP 第一阶段回归构造；第 4 步变为在预期价格处算份额，最优 IV 的价值取决于第一阶段对价格的解释力。

### 6.4 数值积分
- **三种写法 (23a)–(23c)**：直接对 $f(\boldsymbol\mu_{it}\mid\tilde\theta_2)$ 抽样；对 $K_2$ 维标准正态 $\phi(\nu)$ 积分，再用协方差的 Cholesky 根 $L(\tilde\theta_2)$ 变成相关正态（$\tilde\nu_{it}=L\nu_{it}$，$\mu_{ijt}=\sum_k x^{(k)}_{jt}\tilde\nu^{(k)}_{it}$）；在 $[0,1]^{K_2}$ 上积分并用逆 CDF 变换。积分对象有界、光滑、$C^\infty$（导数有界见 Iaria–Wang 2019）。**PyBLP 默认用 (23b)**：固定抽样、随 $\theta_2$ 只做缩放，避免目标函数“抖动”（脚注 51）。支持正态与对数正态（脚注 49）。
- **求积近似 (24)**：$s_{jt}(\boldsymbol\delta_t,\theta_2)\approx\sum_{i\in I_t}w_{it}\,s_{ijt}(\boldsymbol\delta_t,\boldsymbol\mu_{it}(\nu_{it},\theta_2))$。
- **pMC**：$w_{it}=1/I_t$；误差 $\epsilon^{pMC}_{I_t}\xrightarrow{d}N(0,V(s_{jt})/I_t)$，$V(s_{jt})=\int[s_{ijt}-s_{jt}]^2f\,d\boldsymbol\mu<1$；无维数灾难，但以 $O(I_t^{-1/2})$ 慢速下降（偏误修正与标准误调整见 Freyberger 2015）。
- **qMC**（Halton 等低差异序列）：$O(I_t^{-1}(\log I_t)^{K_2})$；Owen (1997) 加扰后对光滑被积函数可达 $O(I_t^{-3/2}(\log I_t)^{K_2})$；还要求 $2^{K_2}<I_t$（文字层为 “2K2 < It”，按上标压平推断）。**PyBLP 默认按 Owen (2017) 加扰 Halton，并在每个维度丢弃前 1000 个点**（脚注 55），各维用不同素数（2, 3, …，图 1 注）。
- **方差缩减**：MLHS（把超立方体切成小块，每块内 pMC 抽样）；对偶抽样 $\phi(\nu)=\phi(-\nu)$。**重要性抽样**：BLP (1995) 从 $q_t(\nu)=\phi(\nu)\cdot\frac{1-s_{i0t}(\boldsymbol\delta_t,\nu,\tilde\theta_2)}{1-\mathcal S_{0t}}$ 抽（多抽外部品份额小的消费者），$\theta_2$、$\delta_t$ 用一致估计代入，拒绝抽样实现，PyBLP 已实现（脚注 57）；自适应重要性抽样（Heiss 2010；Brunner 2017）须随 $\theta_2$ 更新权重，PyBLP 未实现（脚注 56）。
- **高斯求积**：Gauss–Hermite 适合正态；嵌套规则可复用低阶节点；覆盖尾部更好，但可能产生极大值引起溢出（脚注 59：个体 $s_{ijt}\to1$）。积规则维数灾难：一维需 $I_t$ 个节点，$d$ 维需 $I_t^d$。单项式求积（Judd–Skrainka 2011）与稀疏网格（Heiss–Winschel 2008）常有**负权重**，估计或分解异质性（尤其反事实）时可能出问题。
- **推荐**：低维用高阶积规则；高维用 Halton，尤其稀疏网格。蒙特卡洛基准用“精确积分 17 次及以下多项式”的 Gauss–Hermite 积规则：一维 $(17+1)/2=9$ 个节点，二维 $9^2=81$ 个（脚注 76）。估计后应按图 1 的程序自检：用远多于估计时可行的节点精确算 $\delta_t=D_t^{-1}(\mathcal S_t,\theta_2)$，再比较各规则在可行节点数下的 $\|\mathcal S_t-s_t(\delta_t,\theta_2;I_t)\|_2$（PyBLP 有现成的估计后方法，脚注 88）。

### 6.5 供给侧与联合估计、反事实定价
- **估计时**只需对 $\Delta_t(\boldsymbol p_t,\mathcal H_t)$ 求逆得 $\boldsymbol\eta_t$，进而 $c_{jt}=p_{jt}-\eta_{jt}(\theta_2)$。供给边际成本函数可为线性或对数。蒙特卡洛估计供给侧时约束 $\alpha\le-0.001$，因为 $\alpha=0$ 时 $\Delta_t$ 奇异（脚注 78）。
- **反事实**（合并、成本变化）：解 $J_t$ 维非线性方程 $\boldsymbol p_t=\boldsymbol c_t+\boldsymbol\eta_t(\boldsymbol p_t,\mathcal H^*_t)$（(25)）。牛顿法需要需求 Hessian 与张量积；有限差分 Jacobian 又慢又不可取（脚注 62；Knittel–Metaxoglou 不更新 $\boldsymbol s_t(\boldsymbol p_t)$，回避了完整求解）。最常见的直接迭代 $\boldsymbol p_t\leftarrow\boldsymbol c_t+\boldsymbol\eta_t(\boldsymbol p_t,\mathcal H^*_t)$ 不是压缩；Armstrong (2016) 发现它有时不收敛或循环，本文在类似实验中复现了 1–5% 的失败率。“民间”阻尼 $\boldsymbol p\leftarrow\rho\boldsymbol p+(1-\rho)[\boldsymbol c+\boldsymbol\eta^*]$ 更慢更稳但无收敛理论（脚注 63）。存在唯一性超出本文范围（脚注 61）。
- **Morrow–Skerlos (2011) ζ-markup 不动点（(26)(27)，p19，已看图）**：
$$\frac{\partial\boldsymbol s_t}{\partial\boldsymbol p_t}(\boldsymbol p_t)=\Lambda_t(\boldsymbol p_t)-\Gamma_t(\boldsymbol p_t),\quad \Lambda_{jj,t}=\int\alpha_i s_{ijt}(\boldsymbol\mu_{it})f(\boldsymbol\mu_{it}\mid\tilde\theta_2)d\boldsymbol\mu_{it},\quad \Gamma_{jk,t}=\int\alpha_i s_{ijt}(\boldsymbol\mu_{it})s_{ikt}(\boldsymbol\mu_{it})f(\boldsymbol\mu_{it}\mid\tilde\theta_2)d\boldsymbol\mu_{it}$$
$$\boldsymbol p_t\leftarrow\boldsymbol c_t+\boldsymbol\zeta_t(\boldsymbol p_t),\qquad \boldsymbol\zeta_t(\boldsymbol p_t)=\Lambda_t(\boldsymbol p_t)^{-1}\big[\mathcal H^{*}_t\odot\Gamma_t(\boldsymbol p_t)\big](\boldsymbol p_t-\boldsymbol c_t)-\Lambda_t(\boldsymbol p_t)^{-1}\boldsymbol s_t(\boldsymbol p_t)\qquad(27)$$
  - $\Lambda_t$ 对角、$\Gamma_t$ 稠密；**此处 $\alpha_i=\partial u_{ijt}/\partial p_{jt}$ 为价格的边际负效用，取负值**，与 (4) 中 $-\alpha p$ 的写法相反（见第 11 节）。logit 时 $\Lambda_{jj,t}=\alpha s_{jt}$（脚注 64），类似“按自身份额缩放每个方程”的民间做法（Skrainka 2012a）。
  - (27) 与 (25) 是不同的不动点，只在静止点重合；比牛顿类方法**快 3–12 倍**，且可靠地找到均衡。
  - **停止规则（脚注 65）**：$\|\Lambda(\boldsymbol p_t)(\boldsymbol p_t-\boldsymbol c_t-\boldsymbol\zeta_t(\boldsymbol p_t))\|_\infty<\text{tol}$，即“数值同时平稳条件”。
  - 编码：$\Gamma$ 在每个消费者价格边际效用跨产品相同的情形下对称；若 $\partial u_{ij}/\partial p_j$ 随 $j$ 变（如 $\ln(y_i-p_j)$），需自行推导对应分解，且 FOC 方向按 BLP。
- **能快速解均衡 → 可构造可行最优工具**（算法 2 第 4 步）。
- **产量依赖的边际成本（附录 A.3）**：BLP (1995) 设 $\log(p_{jt}-\eta_{jt}(\theta_2))=\log c_{jt}=[x_{jt},w_{jt}]\gamma+\gamma_q\log q_{jt}+\omega_{jt}$。$\log q_{jt}$ 内生，不能放入 $Z^S$，且增加所需工具数（BLP 工具作为数量移动变量应有相关性）。若厂商内部化“多卖一单位改变 mc”，FOC 变为 $s_{jt}+\sum_{k\in J_{ft}}\frac{\partial s_{kt}}{\partial p_{jt}}\big(p_{kt}-c_{kt}-M_ts_{kt}\frac{\partial c_{kt}}{\partial q_{kt}}\big)=0$；对数–对数时化为 $s_{jt}+\sum_k\frac{\partial s_{kt}}{\partial p_{jt}}(p_{kt}-c_{kt}(1+\gamma_q))=0$，即隐含 mc 同比例放大 $(1+\gamma_q)$。现有文献（BLP 1995, 1999）在 FOC 中把 mc 当常数，只在回收 $\gamma$ 时加 $\log q$ 项；内部化可能破坏唯一性，尤其规模报酬递增 $\gamma_q<0$ 时（脚注 106）。

### 6.6 解析梯度、检验与估计后计算接口
- **梯度（附录 A.2）**：$\nabla q(\theta_2)=2G(\theta_2)'Wg(\theta_2)$，$G(\theta_2)=\frac1N\begin{bmatrix}Z_D'&0\\0&Z_S'\end{bmatrix}\begin{bmatrix}\partial\xi/\partial\theta_2\\\partial\omega/\partial\theta_2\end{bmatrix}$（$M\times K_2$）；(A6) $\begin{bmatrix}\partial\xi/\partial\theta_2\\\partial\omega/\partial\theta_2\end{bmatrix}=\begin{bmatrix}\partial\delta/\partial\theta_2\\-f'_{MC}(\cdot)\,\partial\eta/\partial\theta_2\end{bmatrix}$，$f'_{MC}=1$（线性）或 $1/c_{jt}$（对数）。（本卡注：因 $\alpha\in\theta_2$ 且 $Y^D=\delta+\alpha p$，对 $\alpha$ 的导数还含 $p_{jt}$ 项；文字层未显示，待核。）
  - 需求块按市场分块（隐函数定理）：$\frac{\partial\boldsymbol\delta_t}{\partial\theta_2}=-\Big(\frac{\partial\boldsymbol s_t}{\partial\boldsymbol\delta_t}\Big)^{-1}\frac{\partial\boldsymbol s_t}{\partial\theta_2}$（$J_t\times K_2$）；可逆性由外部品份额为正时的对角占优保证，份额很小时仍可能出数值问题（脚注 104）。
  - 供给块（对 $\theta_2$ 中某元素 $\theta_\ell$，$\boldsymbol s_t$ 为数据不依赖参数，脚注 105）：$\frac{\partial\boldsymbol\eta_t}{\partial\theta_\ell}=-\Delta_t^{-1}\frac{\partial\Delta_t}{\partial\theta_\ell}\boldsymbol\eta_t-\Delta_t^{-1}\Big(\frac{\partial\Delta_t}{\partial\boldsymbol\xi_t}\frac{\partial\boldsymbol\xi_t}{\partial\theta_\ell}\Big)\boldsymbol\eta_t$，其中 $\partial\Delta_t/\partial\boldsymbol\xi_t$ 为 $J_t\times J_t\times J_t$ 张量；$\omega_t$ 与 $\eta_t$ 既直接依赖 $\theta_2$，又经 $\xi_t$ 间接依赖。
  - 脚注 103（Armona、Stackman 指出）：集中掉线性参数后 (A6) 的等式在优化中不成立，$\partial L/\partial\theta_2=(I-X(\tilde X'W\tilde X)^{-1}\tilde X'WZ')\partial R/\partial\theta_2\ne\partial R/\partial\theta_2$；但由正交性 $\nabla q\propto\frac{\partial L'}{\partial\theta_2}ZWZ'L=\frac{\partial R'}{\partial\theta_2}ZWZ'L$，**计算梯度时用 (A6) 没问题**。
- **供给矩检验 (32)**（Hausman 式，Newey 1985）：先估供需全模型得 $\hat\theta$，再只用需求矩与最优仅需求权重 $W_D$ 重估得 $\hat\theta_D$，
$$LR=N\big[g(\hat\theta)'Wg(\hat\theta)-g_D(\hat\theta_D)'W_Dg_D(\hat\theta_D)\big]\sim\chi^2_{K-K_x}$$
  PyBLP 也支持 LM（Score）与 Wald 版本。蒙特卡洛中通常能拒绝设错的行为假设，不拒绝设对的（Remark 4）。
- **微观矩、合并、弹性、福利**：PyBLP 支持常见形式的微观矩（Petrin 2002；BLP 2004a），但本文不评估（脚注 6）；估计后方法计算弹性、加价、合并价格效应、福利等（图 5、6 注）；在线附录报告标准误、弹性、合并效应、福利的蒙特卡洛表现（表 OA7–OA15，txt 无内容）。

## 7. 蒙特卡洛结果（§5 与附录 B）
**通用设定（p25–26）**：SQUAREM、L∞ 容差 1E-14、收缩评估上限 1000；log-sum-exp；第一步 GMM 从 logit（或嵌套 logit）解起步，第二步从第一步的 $\hat\delta_t$ 起步。L-BFGS-B + 解析梯度，L∞ 投影梯度容差 1E-5，主迭代上限 1000。初值在真值上下 50% 的均匀分布中抽 3 次，保留目标最小者。盒约束为真值上下 1000%，例外：$\sigma_x\ge0$、$\sigma_p\ge0$、$\rho\in[0,0.95]$、估供给侧时 $\alpha\le-0.001$。最优 IV 用 $Z^{\rm Sums}$ 一步 GMM 的估计构造（approximate 版）；有供给侧时预期价格由 (27) 解出，无供给侧时由价格对全部外生变量回归。报告参数估计的中位偏误与中位绝对误差（MAE）。

**表 3 固定效应吸收（p26；一步 GMM，100 次模拟中位数）**：
| 维数 | 水平 | 吸收 | 秒 | MB |
|---|---|---|---:|---:|
| 1 | 216 | 否 / 是 | 56 / 20 | 721 / 39 |
| 2 | 216×216 | 否 / 是 | 112 / 25 | 1414 / 43 |
| 2 | 36×1296 | 否 / 是 | 330 / 25 | 2498 / 43 |
| 3 | 36×36×36 | 否 / 是 | 46 / 24 | 375 / 47 |
- 吸收使内存降低一到两个数量级，速度最多约 10 倍（36×1296 为 13.2 倍 [D]）；两维中一维远大于另一维时收益最大；即便只吸收 216 个一维 FE 也大幅省时省内存。

**表 4 不动点算法（p28–29；100 次模拟中位数、示例问题 10 次相同运行；每行：平均毫秒 / 平均收缩评估次数 / 收敛率）**。各块内行序：Iteration（L∞ 绝对）、DF-SANE（L∞ 绝对）、SQUAREM（L∞ 绝对）、SQUAREM（L2 相对）、Powell（L2 相对，需 Jacobian）、LM（L2 相对，需 Jacobian）。
| 问题（中位 $s_{0t}$） | Iteration | DF-SANE | SQUAREM L∞ | SQUAREM L2 | Powell | LM |
|---|---|---|---|---|---|---|
| Simple $\beta_0=-7$（0.91） | 5.95/41.85/100% | 3.43/16.27/100% | 2.56/15.94/100% | 2.75/15.26/100% | 3.48/16.33/28.56% | 2.31/8.91/100% |
| Simple $\beta_0=-1$（0.27） | 29.35/212.09/100% | 7.10/35.28/100% | 5.40/34.58/100% | 5.73/33.91/100% | 3.67/17.21/11.38% | 2.35/8.92/100% |
| Complex $\beta_0=-7$（0.91） | 8.35/45.02/100% | 4.52/17.67/100% | 3.32/16.14/100% | 3.50/15.50/100% | 4.03/14.89/32.29% | 2.85/8.98/100% |
| Complex $\beta_0=-1$（0.28） | 39.35/216.80/100% | 8.92/36.23/100% | 7.03/34.75/100% | 7.51/34.09/100% | 4.80/17.70/9.71% | 2.90/8.93/100% |
| RCNL $\rho=0.5$（0.92） | 21.63/93.40/100% | 9.62/32.30/100% | 8.45/33.49/100% | 8.53/31.33/100% | 4.67/14.44/60.65% | 3.27/8.89/100% |
| RCNL $\rho=0.8$（0.92） | 58.01/250.34/100% | 16.30/55.50/99.92% | 14.04/55.54/100% | 13.95/51.70/100% | 6.48/20.16/61.48% | 3.62/9.64/100% |
| Nevo 示例（0.54） | 12.95/86.64/100% | 5.50/25.40/100% | 4.05/24.06/100% | 4.26/22.80/100% | 3.84/17.06/29.20% | 2.62/9.34/100% |
| BLP 示例（0.89） | 152.72/203.04/100% | 34.93/42.37/100% | 31.54/40.61/100% | 31.43/39.38/100% | 26.40/19.31/9.34% | 17.64/8.71/100% |
- p28 部分与表 B1 交叉值一致（SQUAREM L∞：Simple 2.56/15.94、Complex 3.32/16.14、RCNL 8.45/33.49、Nevo 4.05/24.06、BLP 31.54/40.61）。**p29 的毫秒列文字层错乱**：RCNL $\rho=0.8$ 的 SQUAREM/Powell/LM 与 Nevo 各行毫秒是按“每次评估耗时”与 B1 交叉值推断的排列（13.95 与 12.95 的归属尤其不确定），评估次数与收敛率列清楚。
- 结论：$s_{0t}$ 从 0.91 降到 0.27，直接迭代的次数约增 5 倍（41.85→212.09，5.07 倍 [D]）；Jacobian 法不受 Lipschitz 常数影响；SQUAREM 次数只增约 110%（文中数；15.94→34.58 为 +117% [D]）。Powell 在 1E-14 的紧容差下常失败，不推荐。DF-SANE 明显好于直接迭代，但不如 SQUAREM 与 LM。SQUAREM 把迭代次数减少 3–8 倍而单次成本基本不变，在含供给侧的 BLP 示例上尤佳。LM 单次成本高但次数少，外部品份额小时最多比直接迭代快 10 倍，有时与 SQUAREM 相当；RCNL（$\rho\to1$ 收缩变慢）时 LM 提速尤其大。LM 好于 Reynaerts 等报告的拟牛顿法，可能因 MINPACK 的 LMDER 对差初值更稳健（脚注 83）。Broyden、Anderson 等 SciPy 求根法太慢太不稳，不报告（脚注 81）。

**表 B1 不动点技巧（p46；SQUAREM、绝对 L∞ 1E-14；毫秒 / 评估次数，收敛率均为 100.00%）**：
| 问题（$s_{0t}$） | LSE+δ+$\delta^0$ | 无LSE+δ | LSE+exp(δ) | 无LSE+exp(δ) | LSE+δ+热启动 $\delta^{n-1}$ |
|---|---|---|---|---|---|
| Simple（0.91） | 2.56/15.94 | 1.66/15.94 | 2.57/15.94 | 1.66/15.94 | 1.78/13.93 |
| Complex（0.91） | 3.32/16.14 | 2.32/16.15 | 3.33/16.16 | 2.34/16.15 | 2.74/14.74 |
| RCNL（0.92） | 8.45/33.49 | 6.06/33.49 | 8.24/33.49 | 6.09/33.50 | 6.37/27.32 |
| Nevo（0.54） | 4.05/24.06 | 2.67/24.06 | 4.07/24.06 | 2.69/24.06 | 3.10/18.27 |
| BLP（0.89） | 31.54/40.61 | 26.97/40.69 | 31.64/40.61 | 26.57/40.69 | 29.08/37.95 |
- 用 SQUAREM 后其他技巧收益不大；热启动减少 10–20% 迭代，值得考虑，但会让同一 $\theta$ 的目标值随上一轮 $\theta^{n-1}$ 略变，仍建议 1E-14 紧容差（脚注 84）；LSE 成本较低，并降低溢出导致反演失败的可能，推荐。

**图 1 积分误差（p30–31；份额 RMSE，100 个市场中位数，对数刻度）**：随 $K_2$ 增加同步增加节点 $I_t=4^{K_2}$（与精确积分 7 次多项式的积规则同规模；文字层为 “4K2”），各随机系数方差设为 $1/K_2$ 使效用分布不变；用 100 万个 pMC 抽样精确算 $\delta_t$。结论：同节点数下求积最好；随 $I_t$ 增大维数灾难使其他方法相对改善；非求积方法中加扰 Halton 最好（尤其随机系数多时），MLHS 与重要性抽样平平（脚注 87：外部品份额大且常数项有随机系数时重要性抽样略好，对误差度量敏感，且在 $\theta_2$ 估计值而非真值处做会更差）。**$K_2>5$ 时稀疏网格精度与积规则相近，节点不到其 10%。**

**表 B2 积分方法对参数估计的影响（p47–48；1000 次模拟；approximate 最优 IV）**。行序：MC（$I_t=100$）、MC（1000）、MLHS（1000）、Halton（1000）、Importance（1000）、Product rule（$9^{K_2}$：Simple/RCNL 为 9，Complex 为 81；文字层为 “91”“92”，按脚注 76 的上标压平推断）。
| 设定 | 秒 | α 偏误 | σx 偏误 | σp/ρ 偏误 | α MAE | σx MAE | σp/ρ MAE |
|---|---|---|---|---|---|---|---|
| Simple 无供给 | 1.0/3.1/3.2/3.2/21.6/0.8 | 0.233/0.198/0.188/0.186/0.181/0.189 | −0.691/−0.132/−0.051/−0.050/0.018/−0.039 | — | 0.298/0.251/0.241/0.241/0.242/0.245 | 0.691/0.191/0.167/0.165/0.169/0.169 | — |
| Simple 有供给 | 2.7/8.8/8.8/9.2/27.2/2.2 | 0.113/0.021/0.020/0.020/−0.001/0.015 | −0.705/−0.102/−0.015/−0.015/0.065/0.003 | — | 0.243/0.180/0.172/0.170/0.176/0.172 | 0.705/0.182/0.162/0.162/0.181/0.172 | — |
| Complex 无供给 | 1.9/5.3/5.1/5.7/28.3/1.6 | 0.304/0.193/0.191/0.141/0.180/0.172 | −0.776/−0.190/−0.103/−0.120/−0.017/−0.088 | σp：−0.091/−0.012/−0.018/0.033/−0.028/−0.011 | 0.317/0.253/0.254/0.241/0.254/0.250 | 0.778/0.223/0.182/0.190/0.173/0.177 | σp：0.110/0.098/0.102/0.121/0.108/0.169 |
| Complex 有供给 | 5.2/15.0/15.2/17.1/38.6/4.7 | 0.114/0.029/0.015/−0.025/−0.050/−0.020 | −0.702/−0.126/−0.051/−0.053/0.071/−0.029 | σp：−0.137/−0.040/−0.050/0.024/−0.020/0.004 | 0.250/0.194/0.195/0.194/0.208/0.195 | 0.713/0.204/0.171/0.162/0.190/0.171 | σp：0.141/0.106/0.146/0.127/0.112/0.169 |
| RCNL 无供给 | 5.7/18.9/19.0/19.9/40.2/4.3 | 0.236/0.182/0.177/0.174/0.086/0.176 | −0.645/−0.131/−0.026/−0.024/0.854/−0.017 | ρ：0.046/0.001/−0.007/−0.008/−0.110/−0.007 | 0.268/0.219/0.216/0.214/0.241/0.214 | 0.645/0.182/0.160/0.155/0.854/0.153 | ρ：0.051/0.022/0.021/0.021/0.110/0.021 |
| RCNL 有供给 | 12.5/45.8/45.8/47.6/66.0/9.3 | 0.072/0.020/0.008/0.010/−0.071/0.002 | −0.573/−0.096/−0.005/−0.008/0.862/−0.001 | ρ：0.046/0.007/0.000/0.000/−0.099/0.000 | 0.124/0.112/0.109/0.109/0.130/0.109 | 0.573/0.156/0.138/0.139/0.863/0.139 | ρ：0.048/0.019/0.017/0.017/0.099/0.018 |
- 真值：α=−1，σx=3，σp=0.2，ρ=0.5。文中结论：与积规则相比，**10 倍的 pMC/MLHS/Halton/重要性抽样才达到相近精度，耗时 3–20 倍**。100 个 pMC 抽样使 σx 严重下偏（约 −0.6 至 −0.8）；RCNL 下重要性抽样使 σx 上偏约 0.85。注意 Complex 的 σp MAE 上积规则（0.169）并不最优（按文字层顺序，待核）。

**表 5 工具与供给矩（p32；1000 次模拟；积规则 17 次；行序 Own/Sums/Local/Quadratic/Optimal）**：
| 设定 | 秒 | α 偏误 | σx 偏误 | σp/ρ 偏误 | α MAE | σx MAE | σp/ρ MAE |
|---|---|---|---|---|---|---|---|
| Simple 无供给 | 0.6/0.6/0.6/0.6/0.8 | 0.126/0.224/0.181/0.206/0.218 | −0.045/−0.076/−0.056/−0.085/−0.049 | — | 0.238/0.257/0.242/0.263/0.250 | 0.257/0.208/0.235/0.239/0.174 | — |
| Simple 有供给 | 1.4/1.5/1.4/1.4/2.2 | 0.021/0.054/0.035/0.047/0.005 | 0.006/−0.020/−0.006/−0.022/0.012 | — | 0.226/0.193/0.207/0.217/0.170 | 0.250/0.196/0.229/0.237/0.171 | — |
| Complex 无供给 | 1.1/1.1/1.0/1.0/1.6 | −0.025/0.225/0.184/0.200/0.191 | 0.000/−0.132/−0.107/−0.117/−0.119 | σp：−0.200/−0.057/−0.085/−0.198/0.001 | 0.381/0.263/0.274/0.299/0.274 | 0.272/0.217/0.236/0.243/0.195 | σp：0.200/0.200/0.200/0.200/0.200 |
| Complex 有供给 | 3.9/3.3/3.4/3.5/4.9 | −0.213/0.018/−0.043/−0.028/−0.024 | 0.060/−0.104/−0.078/−0.067/−0.036 | σp：0.208/0.052/0.135/0.116/−0.002 | 0.325/0.203/0.216/0.237/0.193 | 0.263/0.207/0.225/0.227/0.171 | σp：0.208/0.180/0.200/0.200/0.191 |
| RCNL 无供给 | 5.1/3.4/3.4/3.4/4.3 | 0.423/0.222/0.216/0.211/0.217 | −1.235/−0.187/−0.194/−0.231/−0.031 | ρ：0.199/0.013/0.016/0.018/−0.008 | 0.463/0.237/0.247/0.252/0.230 | 1.393/0.300/0.324/0.354/0.155 | ρ：0.218/0.034/0.039/0.042/0.021 |
| RCNL 有供给 | 9.7/7.0/7.1/7.1/10.0 | 0.205/0.047/0.038/0.036/0.008 | −0.955/−0.154/−0.148/−0.169/−0.003 | ρ：0.162/0.018/0.020/0.022/0.002 | 0.301/0.148/0.172/0.168/0.111 | 1.201/0.275/0.298/0.330/0.136 | ρ：0.189/0.034/0.039/0.042/0.017 |
- 旋转表重排，行序依据“秒”列（Optimal 最慢、有供给更慢）判断，p32 无页图，待核。真值同上。α 偏误为正表示估计值偏向 0（需求估得偏不弹性）[D]。
- 结论：多数设定下**近似最优 IV 最好**（与 Reynaert–Verboven 一致）；差异化 IV 优于“特征之和”（与 Gandhi–Houde 一致）；加入设定正确的供给矩对多数工具集显著改善（Own 除外）；**最优 IV + 供给侧时偏误基本消失**（α 偏误 Simple 0.005、Complex −0.024、RCNL 0.008），随机系数的 MAE 大幅下降——这与 R–V“有最优 IV 后供给侧作用有限”不同（R–V 的成本移动变量强，本文基准 $\mathrm{Corr}(p,w)\approx0.2$ 偏弱，脚注 89）。收益也传导到平均弹性、合并价格效应等（在线附录）。
- 注：表 5 Optimal 行与表 B2/B3 的积规则/Approximate 行数值接近但不完全相同（如 Simple 无供给 α 偏误 0.218 对 0.189），文中未说明原因。

**表 B3 最优 IV 的三种构造（p49；行序 Approximate/Asymptotic/Empirical）**：
| 设定 | 秒 | α 偏误 | σx 偏误 | σp/ρ 偏误 | α MAE | σx MAE | σp/ρ MAE |
|---|---|---|---|---|---|---|---|
| Simple 无供给 | 0.8/4.8/4.8 | 0.189/0.189/0.188 | −0.039/−0.038/−0.035 | — | 0.245/0.245/0.245 | 0.169/0.169/0.168 | — |
| Simple 有供给 | 2.2/18.1/18.2 | 0.015/0.021/0.026 | 0.003/0.003/0.007 | — | 0.172/0.192/0.181 | 0.172/0.172/0.171 | — |
| Complex 无供给 | 1.6/6.5/6.5 | 0.172/0.177/0.171 | −0.088/−0.084/−0.085 | σp：−0.011/−0.008/−0.012 | 0.250/0.251/0.246 | 0.177/0.175/0.175 | σp：0.169/0.165/0.168 |
| Complex 有供给 | 4.7/29.7/29.5 | −0.020/（0.001、−0.008，顺序待核） | −0.029/−0.085/−0.074 | σp：0.004/−0.029/−0.016 | 0.195/0.210/0.211 | 0.171/0.209/0.199 | σp：0.169/0.168/0.168 |
| RCNL 无供给 | 4.3/9.4/9.6 | 0.176/0.175/0.173 | −0.017/−0.022/−0.020 | ρ：−0.007/−0.007/−0.007 | 0.214/0.214/0.215 | 0.153/0.153/0.151 | ρ：0.021/0.021/0.021 |
| RCNL 有供给 | 9.3/46.4/46.2 | 0.002/0.010/0.011 | −0.001/0.005/−0.004 | ρ：0.000/−0.000/−0.000 | 0.109/0.113/0.113 | 0.139/0.142/0.145 | ρ：0.018/0.018/0.017 |
- Approximate 行与表 B2 积规则行逐项一致（交叉验证了重排）。结论：估计对构造方法不敏感，Approximate 最便宜（耗时约为另两者的 1/2 至 1/8 [D]）且不差。

**图 2 工具强度与设定错误（p33）**：令 $\gamma_w$ 从 0 到 1 变化（1000 次模拟中位偏误，approximate 最优 IV）。成本移动变量很弱（$\mathrm{Corr}(p,w)\approx0.05$）时，仅需求估计的 α 偏误和方差都上升（与 Armstrong 2016 一致）；**加入设定正确的供给约束（配最优 IV）可消除偏误并大幅降方差**，印证 BLP (1995) 的“民间说法”。脚注 91：Berry–Haile 提示无成本移动变量时可能非参数不可识别；本例 $\gamma_x>0$，价格的“第一阶段”仍非平凡。下图：数据按完全竞争生成、估计时假设 Bertrand 多产品寡头——**设错的供给侧比不加供给侧更糟**，使 α 有偏。图 B1：仅用需求矩估计时，按 BLP (1999) 配方（即使行为设错）构造最优 IV，也优于用第一阶段线性回归算 $E[p\mid Z]$。

**图 3 剖面 GMM 目标（p34–35；Simple，100 次模拟中位数）**：固定 α 或 σx、对其他参数再优化。最优 IV 与供给矩使目标在最小值附近更陡（弱识别即目标变平，Stock–Wright 2000），最小值更接近 0，从而 (32) 的 LR 检验能拒绝设错的供给、不拒绝设对的。**推荐**：第一阶段用差异化 IV（含某种“预期价格”），若厂商行为已知，第二阶段用可行最优 IV；随机系数多时尤其应使用最优 IV。

**图 4 问题规模（p35–36）**：市场数 T 增加，α 与 σx 的偏误和效率都改善；T 小且无供给矩时 α 偏误可观；**T>100 时有无供给约束的表现相近**；仅需求时 T=40 大致足以得到“合理”估计。计算时间约随 T 线性增长，随产品数约按 $\sqrt{J_t}$ 增长，供需联合时增长快于 $J_t$。与 Armstrong (2016) 不同，$J_t$ 增大时估计量反而更好，归因于：每厂商产品数跨市场变化、使用可行最优 IV、部分设定含供给矩。

**表 6 优化算法（p37–38；1000 次模拟；approximate 最优 IV；积规则 17 次；终止容差 1E-5）**。每块行序：Knitro Interior/Direct、SciPy L-BFGS-B、BFGS、TNC、Nelder-Mead；前三者用 $\|\nabla q\|_\infty$ 终止，TNC 与 Nelder-Mead 用参数变化 $\|\theta_2^n-\theta_2^{n-1}\|_\infty$ 终止；仅 Nelder-Mead 无梯度。列：收敛率 / Hessian 半正定比例 / 中位秒 / 中位评估次数 / 第一步 GMM 中位 $q$ / 中位 $\|\nabla q\|_\infty$。
| 设定（$|\theta_2|$） | Interior/Direct | L-BFGS-B | BFGS | TNC | Nelder-Mead |
|---|---|---|---|---|---|
| Simple 无供给（1） | 100%/100%/0.2/4/1.10E-08/8.30E-07 | 100%/100%/0.2/4/8.19E-09/7.28E-07 | 100%/100%/0.6/11/1.58E-08/1.03E-06 | 99.9%/99.8%/0.6/10/3.89E-24/9.61E-15 | 66.5%/100%/19.6/115/1.08E-24/4.70E-15 |
| Simple 有供给（2） | 100%/100%/0.6/5/2.17E-06/3.54E-06 | 100%/100%/0.4/4/2.18E-06/3.32E-06 | 100%/100%/2.0/11/2.61E-06/5.26E-06 | 99.8%/100%/2.2/18/2.15E-06/5.12E-11 | 53.3%/100%/31.7/251/2.14E-06/9.69E-13 |
| Complex 无供给（3） | 100%/96.9%/0.7/6/1.92E-07/4.11E-06 | 100%/93.6%/0.4/6/1.83E-07/3.59E-06 | 100%/96.5%/1.9/26/2.25E-07/5.14E-06 | 100%/86.9%/1.8/20/5.08E-20/1.61E-12 | 54.0%/74.6%/30.1/275/1.18E-24/1.39E-14 |
| Complex 有供给（4） | 100%/93.7%/1.9/9/3.20E-06/6.11E-06 | 100%/94.1%/1.4/9/3.12E-06/5.57E-06 | 100%/94.2%/4.6/28/3.19E-06/6.36E-06 | 99.5%/99.5%/5.7/31/2.87E-06/4.02E-10 | 45.5%/99.5%/64.6/480/2.80E-06/1.83E-12 |
| RCNL 无供给（2） | 100%/100%/1.7/10/1.67E-08/5.72E-06 | 100%/99.9%/1.9/11/1.52E-09/1.47E-06 | 100%/100%/4.3/25/2.64E-09/1.95E-06 | 100%/99.6%/4.1/22/3.56E-19/1.16E-11 | 56.4%/98.7%/60.5/243/1.27E-25/2.53E-14 |
| RCNL 有供给（3） | 100%/100%/3.4/13/2.83E-06/9.95E-06 | 100%/100%/3.2/12/2.66E-06/3.85E-06 | 100%/100%/9.3/37/2.73E-06/4.41E-06 | 100%/100%/7.2/24/2.95E-06/2.24E-09 | 39.0%/100%/115.2/423/2.93E-06/4.60E-12 |
- 旋转表重排：“收敛率”与“PSD Hessian”两列的归属按表头词序判断（收敛率列使导数法 ≥99.5%，与正文“超过 99% 收敛”一致）；PSD 低于 100% 只出现在 Complex（推测与 $\sigma_p$ 常落在下界 0、目标关于 0 对称有关 [推测]），与正文“收敛 = 梯度近 0 且 Hessian 半正定”的定义略有出入，待核。仅需求问题用最优 IV 时恰好识别，$q$ 理论上为 0，故参数终止的 TNC/NM 的 $q$ 可达 1E-20 量级。
- 结论：除 Nelder-Mead 外，各优化器都能可靠地找到满足一、二阶条件的最优点；**首选 Knitro Interior/Direct 与 SciPy 的 BFGS 类**（速度与可靠性最佳）。与 Knittel–Metaxoglou 相反：所有导数法超过 99% 的运行收敛到局部极小。作者提醒：模拟问题简单、维数低；数值改进可能已解决部分优化问题；**强工具 + 小数值误差 → 陡峭光滑的目标 → 易优化**。建议：盒约束、梯度法、紧容差、多优化器与多初值互查。

## 8. 复现结果（§6）
**表 7 Nevo (2000b) 复现（p41；括号内为标准误）**。列：原文发表值｜复现｜更紧容差（BFGS 梯度 L∞ 从 1E-4 收紧到 1E-5）｜最佳实践（紧容差 + 仅需求的 approximate 最优 IV）。
| 参数 | Published | Replication | Tighter Tolerance | Best Practices |
|---|---|---|---|---|
| 均值：Price | −32.433 (7.743) | −32.404 (7.729) | −62.729 (14.803) | −27.489 (4.383) |
| 标准差：Price | 1.848 (1.075) | 1.851 (1.070) | 3.313 (1.340) | 2.910 (0.669) |
| 标准差：Constant | 0.377 (0.129) | 0.376 (0.129) | 0.558 (0.163) | 0.196 (0.085) |
| 标准差：Sugar | 0.004 (0.012) | 0.003 (0.012) | 0.006 (0.014) | 0.028 (0.008) |
| 标准差：Mushy | 0.081 (0.205) | 0.080 (0.204) | 0.093 (0.185) | 0.324 (0.110) |
| Price × income | 16.598 (172.334) | 16.457 (172.237) | 588.318 (270.441) | 15.957 (98.164) |
| Price × income² | −0.659 (8.955) | −0.655 (8.951) | −30.192 (14.101) | −1.282 (5.119) |
| Price × child | 11.625 (5.207) | 11.543 (5.166) | 11.054 (4.123) | 4.551 (2.405) |
| Constant × income | 3.089 (1.213) | 3.100 (1.203) | 2.292 (1.209) | 6.253 (0.541) |
| Constant × age | 1.186 (1.016) | 1.172 (1.001) | 1.284 (0.631) | 0.162 (0.207) |
| Sugar × income | −0.193 (0.005) | −0.193 (0.045) | −0.385 (0.121) | −0.289 (0.037) |
| Sugar × age | 0.029 (0.036) | 0.030 (0.036) | 0.052 (0.026) | 0.046 (0.014) |
| Mushy × income | 1.468 (0.697) | 1.462 (0.693) | 0.748 (0.802) | 0.998 (0.303) |
| Mushy × age | −1.514 (1.103) | −1.502 (1.091) | −1.353 (0.667) | −0.523 (0.188) |
| 平均自价格弹性 | — | −3.700 | −3.618 | −3.685 |
| 平均加价 | — | 0.360 | 0.364 | 0.363 |
| GMM 目标 | 6.60E-03 | 6.61E-03 | 2.02E-03 | 2.03E-04 |
| 乘以 N 的 GMM 目标 | 1.49E+01 | 1.49E+01 | 4.56E+00 | 4.59E-01 |
- 弹性与加价三列几乎相同，尽管 Price×income 项（数据中近乎共线）的估计差异很大。脚注 96：Nevo 原代码容差过松众所周知；收紧后 $Nq(\hat\theta)=4.56$，与 Dubé–Fox–Su (2012) 的 MPEC 结果完全相同。Sugar×income 的发表值标准误 0.005 与复现 0.045 相差一个数量级（照抄，可能是原文笔误，待核）。由两行之比推得 $N\approx2.26\times10^3$ [D]。

**表 8 BLP (1995, 1999) 复现（p42；括号内为按车型聚类的标准误）**。列：原文发表值｜复现（原文的特征之和 BLP 工具 + 重要性抽样积分）｜最佳实践（每市场 10,000 个加扰 Halton 抽样 + approximate 最优 IV）。
| 参数 | Published | Replication | Best Practices |
|---|---|---|---|
| 均值：Constant | −7.061 (0.941) | −7.284 (2.807) | −6.679 (1.304) |
| 均值：HP/weight | 2.883 (2.019) | 3.460 (1.415) | 2.774 (0.833) |
| 均值：Air | 1.521 (0.891) | −0.999 (2.101) | 0.572 (0.349) |
| 均值：MP$ | −0.122 (0.320) | 0.421 (0.250) | 0.340 (0.098) |
| 均值：Size | 3.460 (0.610) | 4.178 (0.658) | 3.920 (0.322) |
| 标准差：Constant | 3.612 (1.485) | 2.025 (6.065) | 2.962 (1.637) |
| 标准差：HP/weight | 4.628 (1.885) | 6.101 (2.200) | 1.388 (2.107) |
| 标准差：Air | 1.818 (1.695) | 3.956 (2.110) | 1.424 (0.435) |
| 标准差：MP$ | 1.050 (0.272) | 0.254 (0.549) | 0.072 (1.002) |
| 标准差：Size | 2.056 (0.585) | 1.908 (1.108) | 0.231 (3.837) |
| 价格项 ln(y−p) | 43.501 (6.427) | 44.842 (9.216) | 45.898 (11.748) |
| 供给：Constant | 0.952 (0.194) | 2.760 (0.116) | 2.785 (0.104) |
| 供给：ln(HP/weight) | 0.477 (0.056) | 0.897 (0.072) | 0.731 (0.071) |
| 供给：Air | 0.619 (0.038) | 0.423 (0.087) | 0.528 (0.040) |
| 供给：ln(MPG) | −0.415 (0.055) | −0.525 (0.073) | −0.651 (0.071) |
| 供给：ln(size) | −0.046 (0.081) | −0.261 (0.210) | −0.472 (0.125) |
| 供给：Trend | 0.019 (0.002) | 0.027 (0.003) | 0.018 (0.002) |
| 平均自价格弹性 | — | −3.928 | −3.461 |
| 平均加价 | — | 0.316 | 0.346 |
| GMM 目标 | — | 2.24E-01 | 1.06E-01 |
| 乘以 N 的 GMM 目标 | — | 4.97E+02 | 2.36E+02 |
- 表中价格项仍标作 $\ln(y-p)$，但实际估计按 BLP (1999) 用 $p_j/y_i$ 近似（脚注 98）。估计大体相近；最佳实践显示偏好异质性稍小，需求稍不弹性、加价稍高。Published 列已在 A01 卡与 BLP (1995) 表 IV 逐一核对一致。由两行之比推得 $N\approx2.22\times10^3$ [D]。
- 代码（图 5 Python 写 Nevo；图 6 通过 R 的 reticulate 写 BLP，最后两行把最优工具结果转为新问题再求解）在文字层中缺失。

**Knittel–Metaxoglou (2014) 复现（p40–43，图 7）**：Nevo 配置 + BLP 仅需求版本，50 个随机初值 × 7 种 Knitro/SciPy 优化配置。
- K–M 对参数变化和目标变化都用 1E-3 容差，目标容差尤其导致提前终止；本文用 L∞ 梯度与参数容差 1E-1 **复现出**估计值、目标值、弹性的离散（脚注 100）。
- 收紧到 L∞ 梯度与参数容差 1E-4（脚注 101）即可**消除 Nevo 问题的全部离散**；BLP 仅需求版本还需把每市场 50 个 pMC 抽样换成精确积分 11 次多项式的 Gauss–Hermite 积规则，离散才全部消失（与 Brunner et al. 2017 关于模拟误差的发现一致）。K–M 在线附录也报告收紧容差能消除 Nevo 的离散但不能消除 BLP 的。
- 图 7：中位产品自价格弹性的直方图，最佳实践下跨优化器与初值基本无离散；**正确配置后，开源或商业优化器的选择对 NFXP 不重要**。

## 9. 贡献
1. **统一、开源、可扩展的实现 PyBLP**：最佳实践设为默认；支持 logit、嵌套 logit、BLP、RCNL、多维 FE、供给侧、微观矩、纯特征近似、最优 IV、合并模拟等；可从多语言调用，便于复现。
2. **问题写法的新结果**：把 $\alpha p$ 移到左边，使供需联合 + 高维 FE 吸收可行（算法 1、附录 A.1）；首次给出供需联合估计的**解析梯度**（附录 A.2）。
3. **最优工具的新表达式**：供需两侧工具不同、模型过度识别，明确排除约束（$w$、$v$）和跨方程约束的来源；与 Reynaert–Verboven (2014) 的恰好识别写法区分。
4. **新的数值结论**：Lipschitz 常数的简单推导（脚注 32）；log-sum-exp 引入 BLP；Morrow–Skerlos 定价不动点引入 IO 并用于构造最优 IV。
5. **改写文献结论**：局部极小在识别良好的问题中罕见（推翻 Knittel–Metaxoglou 的悲观结论）；“最优 IV + 正确供给侧”下小样本表现很好，成本移动变量弱时供给侧价值最大（不同于 Reynaert–Verboven，也缓和 Armstrong 2016 的担忧）；BLP 估计量的有限样本表现可能比以前认为的好。

## 10. 局限与稳健性
- 不讨论 MPEC、近似估计量、纯特征模型、微观矩的计量性质（只在 PyBLP 中支持）。
- 蒙特卡洛简单、低维（$K_2\le4$），可跑数千次；优化器表现好可能部分源于此；结论依赖设计（产品数跨市场变化、弱成本移动变量 $\mathrm{Corr}\approx0.2$）。成本移动变量很强或 $(\xi,\omega)$ 方差很小时，几乎任何工具都表现良好（脚注 75）。
- 最优 IV 与供给矩的收益依赖**供给侧设定正确**（$f_{MC}$、$\mathcal H_t$）；设错比不加更糟。需要生成 $(\xi^*,\omega^*)$ 的分布假设；高偏态时 $2J_t$ 维积分难近似。
- 积分结论依情境而定，应估计后自检；重要性抽样在估计值处可能更差。
- SQUAREM 无收敛保证；Morrow–Skerlos 法与均衡存在唯一性未证；数值问题（下溢、近奇异）仍可能发生。
- 表 5 与 B2/B3 中“最优 IV + 积规则”行数字不完全一致，原因未交代；在线附录（标准误、弹性、合并、福利的表现）不在本地文本中。

## 11. 公式校正与笔误提示
1. **(6) Δ 的转置**（总表，p6 已看图）：正文写明 (6) 中导数矩阵的 $(j,k)$ 元为 $\partial s_{jt}/\partial p_{kt}$，由此拼成的 $\Delta$ 与 p5 标量 FOC（$\partial s_{kt}/\partial p_{jt}$）差一次转置，与 BLP (3.4) $\Delta_{jr}=-\partial s_r/\partial p_j$ 也差一次转置。准线性价格混合 logit 的 Jacobian 对称，二者一致；**收入效应规格（如 $\ln(y_i-p_j)$、灵活收入效应）下须按 BLP 方向实现** $\Delta=-\mathcal H\odot(\partial s/\partial p)^\top$。
2. **α 符号约定**（总表，p19 已看图）：(4)(9)(11)(12) 写 $-\alpha p$（即 $\alpha>0$ 为负效用），脚注 17（p8）也按 $\alpha_i>0$ 写 $\partial s_{kt}/\partial p_{jt}=-\int\alpha_i s_{ikt}[1(j=k)-s_{ijt}]$；(26) 却定义 $\alpha_i=\partial u_{ijt}/\partial p_{jt}$（取负值）。**蒙特卡洛与 PyBLP 实际按“价格系数本身”报告**：真值 $\alpha=-1$、约束 $\alpha\le-0.001$、表 7 均值 Price $=-32.433$。编码时统一：若效用写 $+\alpha p$（$\alpha<0$），则 (11) 左边应为 $\hat\delta-\alpha p$，(26) 的 $\Lambda,\Gamma$ 直接用 $\alpha_i<0$。
3. **脚注 64**：logit 时 $\Lambda_{jj,t}=\alpha s_{jt}$（同样按 $\alpha=\partial u/\partial p<0$）。**脚注 65**：ζ 迭代停止规则 $\|\Lambda(\boldsymbol p_t)(\boldsymbol p_t-\boldsymbol c_t-\boldsymbol\zeta_t(\boldsymbol p_t))\|_\infty<\text{tol}$。
4. **两个 Γ**：脚注 32 的 $\Gamma_t(\tilde\theta_2)$（$\int s_{ij}s_{ik}$，用于 $\partial\log s/\partial\delta$）与 (26) 的 $\Gamma_t$（含 $\alpha_i$）不是同一个对象。
5. **(19)**：牛顿步的残差写成 $\boldsymbol s_t(\boldsymbol\delta^h)$，应为 $\boldsymbol s_t(\boldsymbol\delta^h)-\boldsymbol{\mathcal S}_t$（脚注 27 同）。**(20)**：右边文字层为 “$\Psi_t[\mathcal S_t'-s_t]$”，标准 LM 为 $\Psi_t'[\mathcal S_t-s_t]$（p11 无页图，待核）。
6. **(15)**：作者称与 Grigolon–Verboven (2014) 不完全一致是后者的小排版错误（脚注 20）。
7. **(28)–(31)**：文字层严重错乱、无页图，本卡按可辨部分重建（见 6.3），待对照原 PDF p20。
8. **(32)**：自由度 $K-K_x$ 照原文；与前文“$K-2K_x$ 个过度识别约束”的计数不同（检验的是供给矩带来的额外约束），保留原文。
9. **(A6)**：对 $\alpha$ 的导数应含 $p_{jt}$ 项（因 $Y^D=\delta+\alpha p$），文字层未显示，待核；脚注 103 说明集中参数后用 (A6) 算梯度仍正确。
10. **上标压平**：文字层 “T = 64”“N = 66”“92 = 81”“It = 4K2”“2K2 < It”“exp(30) > 1013” 分别应为 $6^4$、$6^6$、$9^2$、$4^{K_2}$、$2^{K_2}$、$10^{13}$。
11. **表 2 注**：$d_{jkt}=d_{kt}-d_{jt}$ 应为 $x_{kt}-x_{jt}$；表注 “$Z^{\rm Opt,D}$ and $Z^{\rm Opt,D}$” 第二个应为 $Z^{\rm Opt,S}$。
12. **表 8 价格项标签**：仍写 $\ln(y-p)$，实际用 $p/y$ 近似（脚注 98）。**表 7**：Sugar×income 发表值 SE 0.005 疑为原文笔误。

## 12. 可复用要点与关联文献
**推荐默认值清单（可直接写进代码配置）**：
- 内层：SQUAREM（或 LM），收敛判据 $\|\log\mathcal S-\log s\|_\infty\le$ 1E-14（可放到 1E-12），收缩评估上限 1000；起点用 logit/嵌套 logit 解析解，第二步用第一步 $\hat\delta$；RCNL 用阻尼 (15)，$\rho$ 接近 1 时改用 LM。
- 份额计算：按市场、log-sum-exp（$a=\max\{0,\max_kx_k\}$）；必要时 `longdouble`。
- 外层：解析梯度；盒约束（随机系数标准差 ≥0 且有界；有供给侧时价格系数 ≤ −0.001；$\rho\in[0,0.95]$）；L∞（投影）梯度容差 1E-5 或更紧；Knitro Interior/Direct 或 L-BFGS-B；多初值（如真值/初估 ±50%）与多优化器互查；报告梯度范数与 Hessian 特征值；对 Cholesky 根参数化。
- 积分：$K_2$ 小时用 Gauss–Hermite 积规则（17 次：每维 9 节点）；$K_2$ 大（>5）用稀疏网格或加扰 Halton（Owen 加扰、各维丢前 1000 点）；固定抽样只做缩放；估计后用大量节点检验积分误差。
- 工具：第一阶段差异化 IV（Local 或 Quadratic；含预期价格；RCNL 加同组产品数）；第二阶段 approximate 最优 IV（有供给侧用 (27) 解均衡价格；仅需求用价格对外生变量回归）。
- 供给：$\Delta$ 按 BLP 方向构造；$f_{MC}$ 线性或对数；用 (32) 的 LR（或 LM/Wald）检验行为假设。
- 固定效应：吸收（MAP/LSMR/Somaini–Wolak），$X$ 只残差化一次。
- 反事实：Morrow–Skerlos ζ 不动点，停止规则用脚注 65。
- 权重矩阵：两步 GMM；PyBLP 目标乘 N，等于 Hansen J。

**PyBLP 用法示意**（**非本文 txt 内容**：图 5/6 代码在文字层缺失，以下据 PyBLP 文档的常见写法整理，参数名以所装版本文档为准）：
```python
import numpy as np, pandas as pd, pyblp
# X1 线性（固定效应用 absorb 吸收，不再写常数项）、X2 随机系数、X3 成本
# product_data 需含 market_ids、firm_ids、shares、prices 及 demand_instruments*/supply_instruments* 列
X1 = pyblp.Formulation('0 + prices + x', absorb='C(product_ids)')
X2 = pyblp.Formulation('0 + x + prices')
X3 = pyblp.Formulation('1 + x + w')
integration = pyblp.Integration('product', size=9)       # 或 'grid'（稀疏网格）/ 'halton'
problem = pyblp.Problem((X1, X2, X3), product_data, integration=integration, costs_type='linear')
results = problem.solve(
    sigma=np.diag([1.0, 0.1]), sigma_bounds=(np.zeros((2, 2)), np.diag([10.0, 10.0])),
    optimization=pyblp.Optimization('l-bfgs-b', {'gtol': 1e-5}),
    iteration=pyblp.Iteration('squarem', {'atol': 1e-14}),
    method='2s')                                           # 价格系数在 PyBLP 中按“系数本身”（负值）报告
iv = results.compute_optimal_instruments(method='approximate')   # 算法 2
results2 = iv.to_problem().solve(sigma=results.sigma, method='2s')
E = results2.compute_elasticities(); mc = results2.compute_costs()
p_merger = results2.compute_prices(firm_ids=merged_firm_ids, costs=mc)   # ζ-markup 不动点
```
- 差异化 IV 构造：`pyblp.build_differentiation_instruments(formulation, product_data, version='local'|'quadratic')`；BLP 工具：`pyblp.build_blp_instruments(...)`；模拟数据：`pyblp.Simulation(...).replace_endogenous()`（均据文档，非本文）。

**关联文献（本包）**：
- **A01 BLP (1995)**：本文表 8 复现其表 IV（Published 列已逐一核对一致）；本文把 $\ln(y-p)$ 换成 $p/y$；BLP (3.4) 的 $\Delta$ 方向是编码基准；BLP 的重要性抽样、最优工具配方（BLP 1999）、产量依赖 mc 都在本文被重新实现或讨论。
- **A02 Petrin (2002)**：微观矩的代表；PyBLP 支持 Petrin 式与 BLP (2004a) 式微观矩，但本文不评估其表现。微观数据的系统处理见 Conlon–Gortmaker (2025, JoE，据 A04/A19 卡，非本文)。
- **A03 GMY (2024)**：其 FOC 下标问题与本文 (6) 转置同源，实现时统一按 BLP 方向；反事实可用 Morrow–Skerlos 定点。
- **A04 HKV (2026)**：用 PyBLP 实现（据 A04 卡：标准误按市场聚类、沿用 Conlon–Gortmaker 的 micro part 写法）。
- **A06 Kaneko–Toyama (2025)**：灵活收入效应下 Jacobian 不对称，正是第 11 节第 1 条要防的情形；其使用 pyBLP 的 Morrow–Skerlos 算法（据 A06 卡）。
- **A07 Grigolon–Verboven (2014)**：RCNL 的来源；本文 (15) 阻尼收缩引用并修正其排版错误；$\rho\to1$ 时收敛变慢，LM 更合适。
- **A11 Ale-Chilet 等 (2026)**：脚注 36 明确遵循本文最佳实践（Knitro、解析梯度、容差 1e−12、近似最优工具、多初值、检查一二阶条件，据 A11 卡）。
- **A19 Heeney–Knittel–Mandia (2026)**、A08、A09、A10：引用 PyBLP 或采用差异化 IV、严格容差等实践。
- 方法外部文献：Dubé–Fox–Su (2012) MPEC 与内层误差；Knittel–Metaxoglou (2014)；Reynaert–Verboven (2014) 最优工具；Gandhi–Houde (2019) 差异化 IV；Armstrong (2016) 大市场渐近与弱工具；Berry–Haile (2014) 识别；Morrow–Skerlos (2011) 定价不动点；Varadhan–Roland (2008) SQUAREM；Heiss–Winschel (2008) 稀疏网格；Owen (2017) 加扰 Halton；Correia (2016) 高维 FE。
