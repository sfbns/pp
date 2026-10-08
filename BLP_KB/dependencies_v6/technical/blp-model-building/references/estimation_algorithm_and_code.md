# 估计算法、数值实施与本机代码

## 0. 标准 BLP 怎样估：嵌套不动点与最佳实践

主来源：Conlon & Gortmaker (2020). Best practices for differentiated products demand estimation with PyBLP. *RAND Journal of Economics*, 51(4), 1108–1161（卷期页与 DOI `10.1111/1756-2171.12352` 于 2026-10-07 经 Crossref 核实；本地 PDF 是 early view 版，页码 1–54，下文页码按本地版）。全文 `D:\codex\research-memory\deep-reading\blp40s_20260403\fulltext\30_bfp23mj2.fulltext.txt`，带公式的 p.5、6、7、8、9、12、19 已渲染原页核过（图在 `D:\blp-structural-skill-config\work_20261007\pageimg\`）；容差、优化器、积分、工具变量等文字叙述按文字层核对，所以只有公式条目标 `[O]`。

### 0.1 估计量 `[O]`（p.6–7 式 (8)–(10)）
`θ = [β, α, θ̃₂, γ]`，堆叠需求与供给矩 `g(θ) = [ (1/N)Σ ξ_jt Z^D_jt ; (1/N)Σ ω_jt Z^S_jt ]`，最小化 `q(θ) = g'Wg`。要解两次：先得一致估计构造 W，再得有效 GMM。
只估需求时去掉供给块。**不估供给的正当理由**：不知道或不愿假定边际成本函数形式与厂商行为（p.7）。

### 0.2 嵌套不动点算法 `[O]`（p.8 Algorithm 1，式 (11)–(13)）
对每个 θ₂ 的猜测：
1. 每个市场解 `S_jt = s_jt(δ_t, θ₂)` 得 `δ̂_t(θ₂)`（内层）；
2. 用 `δ̂_t` 构造 `Δ_t`，解线性方程得加价 `η̂_t = Δ_t^{-1} S_t`；
3. 线性 IV-GMM 集中出线性参数：`δ̂_jt + αp_jt = [x, v]β + ξ`，`f_MC(p − η̂) = [x, w]γ + ω`（式 (11)，α 移到左边是作者与多数应用的不同处）；
4. 构造残差、堆叠矩、算 `q(θ₂)`。
**为什么这样拆**：非线性搜索只在 K₂ 个参数上，Hessian 只有 K₂×K₂；大量线性参数（含产品、市场固定效应）几乎免费；第 1–2 步可按市场并行。**代价**：所有参数都是 θ₂ 的隐函数，一旦有异质性，目标函数非凸（p.8）。没有随机系数时问题全局凸（p.13 脚注 35）。

### 0.3 内层：反演怎样解得又快又准
- **容差**：用份额对数差的上确界范数 `‖log S − log s(δ,θ₂)‖_∞ ≤ ε_tol`，作者取 1E-14 至 1E-12（双精度机器精度约 1E-16）；太松会把数值误差传进估计，太紧会永远达不到（p.11）。
- **收缩速度** `[O]`（p.12 式 (21) 与脚注 32）：线性收敛，速率与 Lipschitz 常数 `L(θ₂) = max‖I − ∂log s/∂δ‖_∞` 有关；Dubé, Fox & Su (2012) 的模拟显示**外部选项份额越小，L 越大，收敛越慢**。脚注 32 给了粗略界 `max_j Σ_k s_kt·|Corr(s_ijt, s_ikt)| < 1 − s_0t`，直观上外部选项份额就是收缩的"安全边际"。
- **加速**：SQUAREM（Varadhan & Roland 2008）比直接迭代快 3–6 倍，代价是失去收缩保证（p.12）。
- **小技巧**：对 `exp(δ)` 迭代；用上一个 θ₂ 的 δ 作起点（p.15）。

### 0.4 外层：优化器与收敛判断
- 非凸问题没有任何优化器能保证找到全局最小。**多起点、多优化器，并在解处同时验一阶条件（梯度近零）与二阶条件（Hessian 特征值全正）**（p.13）。
- 不推荐 Nelder-Mead：Dubé, Fox & Su (2012) 与 Knittel & Metaxoglou (2014) 都发现导数法更快更稳（p.13 脚注 38）。
- 推荐先试 Knitro Interior/Direct，再试带参数界的 L-BFGS-B；**比选哪个求解器更要紧的是：参数界、解析梯度、足够紧的终止容差**（p.14）。默认终止容差常太松，N 大时更糟。
- 随机系数优化的是协方差的 Cholesky 根，目标函数关于 σ 的符号对称，所以非负约束不是必需（p.13 脚注 41）。这个对称性要求积分节点对称（例如 Gauss-Hermite 或对称化的抽样）；每个市场只用固定的少量抽样且抽样不对称时 `g(σ) ≠ g(−σ)`，对角元的符号会影响估计。pyblp 在支持边界的优化器（如 L-BFGS-B）下**默认把 σ 的对角元限制为非负**（pyblp 1.2.0 `Problem.solve` 的 `sigma_bounds` 说明）；在 Nevo 数据上这会把糖分的 σ 卡在 0，目标函数 4.7214，而不设界的 BFGS 得 4.5615、σ_sugar = −0.0058。用带界优化器时要么显式放开 `sigma_bounds`，要么报告哪些参数落在边界上（`scripts/pyblp_minimal_example.py --show-bound-trap` 复现这一点）。

### 0.5 数值积分
低维用高阶乘积规则（Gauss-Hermite）；高维 Halton 序列与 sparse grid 扩展性最好（p.16–18）。作者复现 BLP (1995) 只估需求时的困难，换成能精确积分 11 次以下多项式的 Gauss-Hermite 乘积规则、替代每市场 50 个伪蒙特卡洛抽样就消除了（p.43 脚注）。

### 0.6 均衡价格怎样求 `[O]`（p.19 式 (26)(27)）
直接迭代 `p ← c + η(p)` 不是收缩，Armstrong (2016) 的模拟会循环，作者复现 1%–5% 失败（p.18）。用 Morrow & Skerlos (2011)：`∂s/∂p = Λ − Γ`，`p ← c + ζ(p)`，`ζ = Λ^{-1}[H ⊙ Γ](p − c) − Λ^{-1}s`；以 `‖Λ(p)(p − c − ζ(p))‖_∞` 小于容差为止。比 Newton 类快 3–12 倍且可靠。★ 该式里 `α_i ≡ ∂u_ijt/∂p_jt` 为负，与本 skill 其余部分 `−αp, α>0` 的约定相反，照搬前统一符号（见 `micro_foundations.md` 7(d)）。

### 0.7 工具变量：从 BLP 工具到近似最优工具
- 识别应检查所估模型的矩 Jacobian 局部满列秩、排除限制与支持，不是按每个参数分配不同工具；原文的必要维数讨论不能替代该检查（Conlon–Gortmaker p.7 脚注14）。
- **近似最优工具**（Chamberlain 1987）`E[D_jt Ω_jt^{-1} | Z_t]`，D 是结构误差对参数的 Jacobian（p.19）。作者的版本让供需两侧各有工具，因而有 K₂ 个过度识别约束；排除限制要在"另一条方程里出现的东西"上找，只进成本的 w 给需求提供关于 θ₂（含 α）的信息，只进需求的 v 给供给提供关于加价的信息（p.21 Remark 1）。Reynaert & Verboven (2014) 的版本相当于只施加 `E[ξZ^D] + E[ωZ^S] = 0`（Remark 2）。
- **差异化工具**（Gandhi & Houde 2019）：产品特征差 `d_jkt = x_kt − x_jt` 的二阶多项式基（Remark 3）。
- 结论：近似最优工具配上设定正确的供给侧"价值极大，几乎总应使用"；在此条件下 BLP 估计量的有限样本表现比以往认为的好（p.44）。

### 0.8 加入微观矩时改什么（Conlon & Gortmaker, *Journal of Econometrics*, Article 105926，本机卡 `D:\codex\output\blp_driving_cycle_structural_research_20260824\iteration3_new_papers_20260824\03_pass1_cards\conlon_gortmaker_micro_pyblp.md`）`[O·卡]`
- 每个微观数据集是条件于全部聚合数据的独立调查，按已知入样概率 `w_dijt` 抽样；每个统计量是 micro parts 的平滑函数，模型对应量是按入样概率加权的条件期望（式 (17)）。
- 估计量 `ĝ = [ĝ_A ; ĝ_M]`，`ĝ_M = f(v̄) − f(v(θ))`（式 (18)）；两类样本条件独立时最优权重块对角，但**必须按估计协方差加权，不能随意同权**。
- 同一调查拆成"所有买家"与"某类买家"不能当两个独立数据集；兼容性可疑的矩先在不用它们的模型下估计，再做 Wald 检验（式 (22)）。
- 第二选择：`s_ijkt = s_ijt · s_ik(−j)t`。人口—选择矩主要识别 Π；选择集/第二选择改善识别，但缺少它们不等于Σ不可识别；依聚合有效变化与矩Jacobian检验。
- 用 Salanié–Wolak 二阶近似回归做识别诊断与起始值（式 (8)），不当最终估计。

## 1. 模型阶梯（务必按顺序，并保证真正嵌套）

| 层 | 模型 | 新释放的内容 | 必须不变的内容 |
|---|---|---|---|
| B0 | 受限结构 Logit | 消费者类型分布退化到预定代表类型 `ω*` | 效用变量、政策暴露、市场、工具、outside |
| B1 | 事前可辩护候选树的 nested Logit（可选） | 预定分组的残余相关 | 同上；焦点或非焦点均不自带合法性；不能只因焦点是动力而预设nest，有独立替代证据时可作候选并检验限制 |
| B2 | RC / micro BLP（主模型） | 价格、成本、不便、类别与品味的连续异质性 | 同一效用对象与政策矩 |
| B3 | RCNL（可选） | 经验证后仍存在的分组相关 | B2 的连续异质性全部保留 |

**B0 的正确定义**：`F^{B0} = Dirac_{ω*}`，`Π = 0`，`L = 0`，`μ_ij = 0`，并在**同一个**非线性成本/不便函数里评价该代表类型。
**错误定义**：先把 `Ĝ_i`、`RI_i`、注意/信任取市场均值再代入。非线性下 `G(E[ω]) ≠ E[G(ω)]`，这只能叫 `mean-index Logit approximation`，不能参加"B2 方差归零回到 B0"的等价测试。

B0 的份额与反演有封闭形式：`log s_j − log s_0 = δ_j`。B1：`log s_j − log s_0 = δ_j + ρ log s_{j|g}`，`0 ≤ ρ < 1`，`s_{j|g}` 是内生均衡份额，**必须配工具**（within-nest share 不是自己的工具变量）。

## 2. 反演与求解

- 标准 BLP：`δ^{h+1} = δ^h + log s^obs − log s^model(δ^h; θ_2)`。
- **RCNL 的阻尼反演**：`δ^{h+1} = δ^h + λ_c[log s^obs − log s^model(δ^h)]`，`0 < λ_c ≤ 1 − ρ`。
  ★ Grigolon–Verboven 附录里把 `(1−ρ)` 只放在 model log share 前面的印刷式，**直接当迭代不保持 `s^model = s^obs`**。实现必须对**完整 log-share 差值**阻尼，并同时检查 share residual 与 fixed-point residual。两层 nest 须满足 `0 ≤ ρ₂ ≤ ρ₁ < 1`。
- 只对**每个 inside 份额和 outside share 都严格为正**的市场用标准 Berry 反演。对"可得但样本份额为零"的产品，预先选择并论证：更粗市场聚合 / 显式测量误差或删失份额模型 / 个体选择似然。**不得随便给份额加 ε。**
- reduced-form 的基期 roster 可以把退出后销量记零；BLP 的市场集合 `J_mt` 则按可售集排除退出产品。两者不能混用。

## 3. 保证符号的参数化

需要为正的系数（价格 `α_i`、未来成本 `γ_id`、不便 `κ_i`）用**相关对数正态块**：
```
[log α_i, log γ_i1, …, log κ_i]' = a_0 + Π_a z_i + L_a ν_i,   ν_i ~ N(0,I)
```
`L_a L_a'` 允许这几个系数相关。可正可负的属性/类别/品味偏好另用线性正态块。
**不要用"线性正态抽样 + 事后截断"**——那会同时破坏分布形状和梯度。
若用对数正态，比较"完全资本化"基准时应比较 `E[χ_i]` 或其分位数与 1，**不能把对数均值参数直接与 1 比**。

## 4. 数值验收清单

- 每个市场的收缩映射收敛，记录 sup norm
- 固定 / common random draws；跨情景共用，独立抽样再验绝对误差
- 多起点优化得到相近目标值与参数
- 解析梯度与有限差分一致
- `∂s_j/∂p_j < 0`，交叉导数非负（只适用于没有网络效应或互补项的需求；Remmy 2026 这类间接网络效应模型会出现负的交叉弹性，此时改查符号是否与模型里的网络项一致）
- Jacobian / 所有权矩阵方向逐元有限差分核对（`Δ = −(Jᵀ⊙H)`）；Conlon & Gortmaker 式 (6) 不转置，只在 Jacobian 对称（准线性价格）时与 BLP (3.4) 等价，收入规格下按 BLP 方向
- 价格系数符号约定统一：BLP 写 `−αp, α>0`，Conlon & Gortmaker 式 (26) 的 `α_i = ∂u/∂p < 0`，Barwick–Kwon–Li 正文与表 3 说明也不一致
- markup 与边际成本经济上合理，`p ≥ mc`
- 生命周期成本：`/100` 换算、同币值基期、持有联合期望、实际/名义折现配套、转售终值处理一致
- 矩 Jacobian 秩、弱识别诊断、profile objective
- 生成变量（映射楔子、真实道路映射、信念校准、market size、micro moments、模拟份额）全部进全流程 bootstrap 或影响函数

## 5. 模型单元测试（跑得通才算实现正确）

1. B2 类型分布退化到同一 `ω*` 时数值回到 B0（mean-index 版本不参加此测试）
2. RCNL 的 `ρ=0` 回到 RC/BLP，且反演同时满足 share residual 与 fixed-point residual
3. 完全相同的反事实状态 ⇒ 零份额差、零 CV/EV、零经验福利差
4. 单独提高某产品价格 ⇒ own share 下降、所需 `CV^req` 非负
5. 单独提高不利属性（如显示能耗）⇒ 在正系数下效用下降；提高有利属性 ⇒ 上升
6. 注意或信任为 0 时，纯标签变化不改变信念通道
7. 统一参数化后做等权资本化：若效用为 `−α_i(p+γ_iG)`，无量纲比率应为 `γ_i^cf=1`；若另记成本斜率为 `−η_iG`，则 `η_i^cf=α_i`。不能把斜率和资本化比率混称γ。信念、真实属性与其他偏好固定。
8. 产品 IV 矩与 micro moments 使用各自样本与权重，堆叠 Jacobian 达到所需 rank
9. 组 diversion 以源组 share loss 为分母、含 outside，对冲击权重敏感
10. 转移矩阵含 outside、每行和为 1，并与独立重抽 / coupling bounds 比较
11. 固定价格反事实不调用供给求解器；重新定价基线能回放观测价格
12. 逐抽样 `1/α_i` 的决策 surplus 与错误的平均 `ᾱ` 版本**分别输出**（用来演示差别）
13. 选择集扩张且其他不变时决策 surplus 不下降
14. `M_mt · s_jmt` 与销量单位一致，`w_imt` 归一
15. 社会福利各账户逐项守恒；关闭任一未建部门时不输出伪总额

## 6. 本机代码

生产级首选 **pyblp**（Conlon & Gortmaker 2020, *RAND* 51(4), 1108–1161，2026-10-07 Crossref 核实），micro moments 用其官方框架。

**历史两个主脚本；本轮另补归一与买家抽样反例**（2026-10-07 在本机跑通）：
- `D:\codex\.codex-home\skills\blp-model-building\scripts\blp_selftest.py`：只需 numpy，8 组 19 项数值自检（(6.9b) 负号与下标、两种 Δ 方向、logit 加价、GHvB 期刊表 7 与工作论文表 D.1、Alé-Chilet 符号、logsum、续航缺口导数、均值之比），全部通过时打印 ALL PASS，覆盖该脚本列出的19项，不代表上文15条生产验收全部已实现。改公式后先跑对应测试。
- `D:\codex\.codex-home\skills\blp-model-building\scripts\pyblp_minimal_example.py`：pyblp 1.2.0 自带 Nevo 数据上的随机系数 + 人口交互估计、弹性、加价、成本、转移率、消费者剩余、近似最优工具重估、一个微观矩的接口写法。运行用隔离虚拟环境 `D:\blp-structural-skill-config\work_20261007\venv_pyblp\Scripts\python.exe`（装有 pyblp 1.2.0 与 pandas）。优化器用不设界的 BFGS（gtol 1E-5，pyblp 教程对 Nevo 的设定），并打印收敛诊断，诊断不过就报 CHECKS FAILED。本机实跑结果（2026-10-07）：目标函数 4.5615，价格系数 −62.73，投影梯度范数 5.6E-06，约化 Hessian 特征值最小 3.2E-05（全为正，是局部极小），σ 对角元 (0.558, 3.313, −0.006, 0.093)；首个市场平均自弹性 −4.21，平均勒纳指数 0.364，自导数为负、交叉导数非负、加价为正；近似最优工具重估后价格系数 −31.40（工具个数等于参数个数，恰好识别，目标函数为 0）。加 `--show-bound-trap` 再用 L-BFGS-B 跑一遍：糖分的 σ 卡在下界 0，目标函数 4.7214，价格系数 −60.18。
- pyblp 的两个约定：`compute_markups` 返回勒纳指数 (p−c)/p，不是加价额；`compute_demand_jacobians` 的 (j,k) 元是 ∂s_j/∂p_k，自己拿它拼 Δ 时按 BLP (3.4) 转置。

本机自建骨架（教学/诊断/报告脚手架用，不是生产估计器）：
`D:\codex\research-memory\BLP_structural_models_memory_skills_configs_2026-08-24\07_structural_model_code\src\econ_model_agent\structural\`
> 注意：`D:\codex\econ-model-agent\src\` 已被删，代码只在上面这个解包目录里。

`blp.py` 提供的对象：
- `BLPConfig`（market_id / product_id / share / price / product_characteristics / demand_instruments / random_coefficients / firm_id）
- `BLPModelSkeleton`：`describe_model` / `moment_conditions` / `python_code` / `counterfactual_interface`
- `BLPContractionSolver`：`solve`、`predict_shares`、份额合法性校验
- `SimpleLogitDemandEstimator` → `BLPDemandResults`：IV-GMM 简单 logit、`elasticities`、`simulate_price_counterfactual`、消费者剩余变化、补贴向量
- `MicroMoment`、`RandomCoefficientsDemandEstimator` → `RandomCoefficientsDemandResults`：模拟随机系数非线性 GMM + 可选微观矩
- `SupplySideBertrandSolver`：`recover_marginal_costs`、`solve_equilibrium_prices`、`_derivative_matrix`、`_ownership_matrix`
- `SMMEstimator`、`gmm_sandwich_standard_errors`、`OptimizerDiagnostics`
同目录另有 `dynamic_discrete_choice.py`（有限状态 DDC 值迭代/选择概率/似然/模拟）、`gmm.py`、`mle.py`、`counterfactual.py`。
测试：`07_structural_model_code\tests\test_blp.py`、`test_structural_optimizers.py`；示例 `examples\03_blp_demand_skeleton.py`。

## 7. 改造后的估计配方（与 `extension_genealogy.md` 第 7 节配套）

下面五个配方按工况重标项目最可能用到的顺序排列，每个都写清"多了什么、在哪一环加、靠什么识别"。公式是本项目扩展，标 `[P]`；所借文献的原式见 `extension_genealogy.md`。

**配方 1 生命周期运营成本 + 里程异质性**（借 D4 GRV 2018、D5 Lu 2023、D3 Hong–Kim–Verboven）`[P]`
- 效用写 `−α_i (p_j + γ_{i,d(j)} G_ij)`，`G_ij = Σ_τ S_τ KM_iτ E[P_fuel] FC_j /(100(1+r)^τ)`；里程 `KM_i` 从外部经验分布抽样并与价格敏感度一起进 μ。
- 内层不变；外层识别的是 `αγ·ρ` 这类复合系数，ρ 由预先登记的折现率、年限、存活率算出。**比值逐抽样算再聚合**，不能用平均系数相除（GHvB 本应用的近似估计曾提高一倍以上；这不是普遍同号/同幅度偏误，且须先区分工作稿D.1负斜率与D.4正比率，见extension_genealogy B1）。
- 识别：与 ξ 正交的运营成本变化（同车型不同配置、跨地区能源价格）；里程分布钉尺度；若有"哪类里程者买哪类车"的微观矩更好（Lu 2023 缺这一块）。

**配方 2 第二选择与人口微观矩**（借 D1、D2、D3、`identification_and_micro_moments.md` 第 3 节）
- 每次 θ₂ 猜测：反演 δ → 用同一组抽样算模型的微观统计量（第二选择要在删掉第一选择的集合上重算概率）→ 线性集中 β → 堆叠 `[g_A; g_M]`。
- 新车买家样本不仅把P_ij除以P_iB，还须用dF_B=P_iB*dF/s_B重权类型，或直接用总体联合概率除s_B；并复制调查入样机制（见identification_and_micro_moments第3节）；权重矩阵按估计协方差构造。
- 诊断：先用 Salanié–Wolak 近似回归看 Σ 与 Π 有没有可识别的变化。

**配方 3 信念增广（标签权重）**（项目 [P]，台账 03 第 2–3 节）
- 主观运营成本 `PVOC_hat_ij = ω_ij PVOC(L_j) + (1 − ω_ij) PVOC(B_ij)`，`0 ≤ ω ≤ 1`；ω 进 μ 的方式须预先说明（全体共同、按类型、随抽样）。
- 当标签与先验没有独立变化、先验未知且资本化未受约束时，聚合份额通常只约束ω与资本化的复合响应；这不是聚合数据的一般不可能定理，独立变化和已知先验可能改变秩。此时主表只能叫"复合标签权重"；分开需补足使矩Jacobian局部满列秩的独立限制/变异，例如标签阅读、工况识别、换算测试或随机信息解释微观矩；也可为外部已知先验与独立aggregate变异，不能一概规定调查/实验是唯一方法（台账 04 第 4 节）。
- 单元测试：ω = 0 时纯标签变化不改变选择概率；新旧标签存在已知一一映射且消费者用两种标签形成相同后验时，纯换标尺不应改变选择（表示不变性基准，台账 03 式 (3a)）。

**配方 4 续航不便的微观基础**（项目 [P]，台账 03 第 5 节）
- `A_i(R) = E[(D_i − R)_+]`，`A_i′(R) = −Pr(D_i > R)`，`A_i″(R) = f_{D_i}(R) ≥ 0`；效用中 `−κ_i A_i(R̂_ij, N_mt)`，因此续航边际效用为正且递减，曲率来自出行需求分布，**不需要也不应引 Kaneko–Toyama**。
- 实现：对每个模拟消费者抽出行距离分布（或用 W03 那类使用侧动态模型给出的货币化量级作外部校准），数值积分 `A_i`；κ 用相关对数正态块保证非负。
- 识别：续航 × 长途频率 × 充电条件的变化；行程分布右尾与家充数据作微观矩。

**配方 5 内生属性（有数据门槛的扩展）**（借 S1 Barwick–Kwon–Li、S2 Remmy）
- 供给侧在价格 FOC 之外加属性 FOC，影子价格 λ 的处理（共同参数或与销量成比例）须预先登记；技术前沿用包含未上市车型的外部测试数据另估。
- 估计：边际成本方程、属性 FOC 残差的条件矩与需求矩联合 GMM；反事实同时解价格与属性。
- 门槛：属性成本移动项、工程前沿数据、足够多的属性变化；缺任一项就停在"冻结属性、只允许重新定价"，并在报告里写明这一层被数据卡住。
