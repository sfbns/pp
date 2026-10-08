---
name: blp-model-building
description: 从零搭建、估计、审计一个 BLP 型差异化产品需求—供给结构模型，并按文献的做法改造它。触发词包括「BLP」「随机系数 logit」「份额反演」「Berry inversion」「markup 反推」「micro moments」「第二选择」「pyblp」「跨产品替代/diversion」「结构反事实与福利」「BLP 怎么改造」「内生属性」「网络效应」「资本化/短视」，以及汽车/EV/能效标签/工况重标类政策问题。三块底座：BLP 的微观经济学原理、文献改造谱系（改哪个原语、机制怎样搭、要什么理论、怎样估计）、估计最佳实践；公式逐页对 BLP(1995) 与 Conlon–Gortmaker(2020) 原页核验，项目口径以 2026-09-20 纠错台账为准。
metadata:
  type: skill
  provenance: BLP(1995) Econometrica 原页核验 + Conlon & Gortmaker(2020) RAND 原页核验 + 本机 28 篇 BLP 语料、40 篇深读包、燃油经济性 17 篇、需求侧结构模型 49 篇、BLP 改造篇 6 篇 + 工况重标项目 iter1–iter5 与 09-20 纠错台账
  updated: 2026-10-07（并入 08-26 至 10-07 结论；新增 micro_foundations、extension_genealogy；估计文件加第 0、7 节）
  companion: structural-model-building, econ-research-craft, economics-expert-reviewer, econ-empirical-research
---

# BLP 模型构建

中国工况项目先加载 `references/current-project-adapter.md`，恢复本轮输入、政策时钟、纠错优先级与未完成评审；历史PASS不认证当前版本。

一句话：**BLP 不是"更复杂的 logit"，而是一整套把市场份额翻译回结构原语、再用来做替代、均衡和福利反事实的流程。**
主线：异质消费者效用 → 聚合份额 → 份额反演出 δ 与 ξ → IV/GMM 识别 → 多产品 Nash 定价反推 markup 与 mc → 反事实与福利。

## 三块必读（按顺序）

| 要回答的问题 | 读哪里 |
|---|---|
| BLP 每一块在经济学上是什么：特征空间、离散选择与归一化、logit 为什么不够、随机系数怎样生成替代、ξ 与内生性、反演为什么是钥匙、多产品 Bertrand 怎样不靠成本数据估成本、Small–Rosen 福利、每个参数靠什么变异识别 | `references/micro_foundations.md` |
| 文献怎样改造 BLP：十二个原语坐标系；Petrin、Grieco 等、Hong–Kim–Verboven、GRV、Kaneko–Toyama、RCNL、Barwick–Kwon–Li、Remmy、Alé-Chilet 等、Reynaert、Miller–Weinberg、网络效应、GHvB 等逐篇拆成"改了哪个原语 · 机制写法 · 所需理论 · 识别 · 估计 · 边界"；八种机制构建模式；改造后算法每一环改什么 | `references/extension_genealogy.md` |
| 最后怎样估计：NFXP 步骤、容差 1E-14 至 1E-12、SQUAREM、多起点与一阶二阶条件、积分规则、Morrow–Skerlos 定价固定点、近似最优工具与差异化工具、微观矩怎样堆叠；五个改造配方（生命周期成本、第二选择、信念增广、续航不便、内生属性） | `references/estimation_algorithm_and_code.md` 第 0 节与第 7 节 |
| 能直接跑的代码：数值自检（8 组 19 项，只需 numpy）与 pyblp 最小示例（Nevo 数据：随机系数 + 人口交互、收敛诊断、弹性、加价、成本、转移率、消费者剩余、近似最优工具、微观矩接口；`--show-bound-trap` 演示 σ 默认下界怎样卡住参数），均已在本机跑通 | `scripts/blp_selftest.py`；`scripts/pyblp_minimal_example.py`（用 `D:\blp-structural-skill-config\work_20261007\venv_pyblp\Scripts\python.exe` 运行） |

## 用之前先回答三个问题

如果这三个有任何一个答不上来，先别写效用函数。

1. **为什么 reduced-form 不够？** 只有当你要的对象是**替代矩阵、均衡传导或福利重分配**时，结构层才值这个代价。要的只是平均处理效应，就别上 BLP。
2. **outside option 和市场规模 `M` 是什么？** 只观察到新车购买者内部份额，你估的是**条件需求**，算不出"不买/买二手/继续持有/公共交通"这些边界上的替代与福利。
3. **哪个对象内生？** 价格、政策诱发的工程属性、充电网络、进入退出、暴露强度——名字必须先点出来，识别策略才有靶子。

想加机制时多问一句：**这个机制落在哪个原语上**（效用里的货币项、异质性分布、误差结构、选择集、信念、厂商的第二个选择、网络外部性、规制约束）？`extension_genealogy.md` 第 1 节的坐标系给出每个原语谁改过、怎么估。

## 七步实操流程

1. 选定需求特征 `x_j`、成本特征 `w_j`、厂商归属 `F_f`，定义市场与 outside；
2. 给定消费者异质性分布 `P_0`（收入用外部数据喂进去，不要凭空假设）；
3. 猜一组非线性参数 `(α, σ)`；
4. 用收缩映射从观测份额反演 `δ`：`δ ← δ + ln s^obs − ln s^model`，容差按份额对数差的上确界 1E-14 至 1E-12；
5. 由 `δ` 得 `ξ`，再由需求导数构造 `Δ`、算 markup `Δ^{-1}s`、反推成本冲击 `ω`；
6. 用 `ξ, ω` 和工具变量构造 GMM 矩条件（有微观数据就堆叠微观矩）；
7. 更新参数直到矩条件接近 0。只有条件于非线性参数后实际线性进入需求/成本矩的参数块才可 concentrate out；`γ` 是否属于该块取决于具体效用设定。随机资本化、信念交互或非线性成本中的 `γ` 必须留在非线性搜索中，不按符号名分类。

逐式定义、符号与单位见 `references/blp1995_verified_equations.md`；**该文件标了本机 walkthrough 的一处漏负号（2026-10-07 已在 8 份副本中修正）和原文自身三处笔误，动手前必读。**

## 八条最常犯的错（本机语料反复出现）

1. **交叉价格导数漏负号。** BLP (6.9b) 前面有负号，且求导对象是**被调价那个备选项**的效用指数。写成 `∂μ_ij/∂p_q` 会得零，写掉负号会让 Δ 非对角元反号，markup 与 mc 全错。
2. **矩阵方向。** `Δ_jr = −∂s_r/∂p_j`（行 = j 的价格 FOC，列 = r 的 margin）。代码若把 Jacobian 存成 `J_jk = ∂s_j/∂p_k`，则 `Δ = −(H ⊙ Jᵀ)`。Conlon & Gortmaker (2020) 式 (6) 不转置，只在需求 Jacobian 对称时（准线性价格）与 BLP 等价；收入规格 `α log(y−p)` 下必须按 BLP 方向。上线前用有限差分逐元核。
3. **照抄原文的符号约定与笔误。** 价格系数：BLP 的线性价格起始示例写 `−αp, α>0`，原实证规格却用 `α log(y−p)`，不能混称；Conlon & Gortmaker 式 (26) 的 `α_i = ∂u/∂p < 0`，而同文 p.8 脚注 17 的 `α_i` 取正号；Barwick–Kwon–Li 正文与表 3 说明也不一致。加价：Alé-Chilet 等式 (13) 在 `S_jh = −∂s_h/∂p_j` 的定义下印成 `mc = p + (Ω⊙S)^{-1}s`，正确是减号。GHvB 来源边界：2019工作稿脚注26确实印 `ΔP + ΔP·ΔQ/η_D` [O·目标页]，但与其TableD.1不一致只支持[D] suspected-typo诊断，未核作者勘误或唯一修复。`ΔWTP ≈ ΔP − P_0·(ΔQ/Q)/η_D` 是局部平行需求/相应供给条件下的[D]换算，不是已核正式在线附录D.3原式；`Loss=−signed ΔWTP` 是声明的符号归一。正式Table7以改革前P0=24,500、工作稿TableD.1以推断的改革后P1=24,206重算，不能把P1写成工作稿改革前P0。工作稿D.1的负斜率 `γ_src=−θ/δ` 与D.4正比率 `v=θ/δ` 必须显式区分；细节和未核项以 `extension_genealogy.md` B1为准。照搬任何公式前先统一约定，再用 `scripts/blp_selftest.py` 跑一遍。
4. **把机制塞进 ξ。** `ξ` 是消费者和厂商看得见、计量学家看不见的产品质量。短视、注意、信任、续航焦虑、绿色偏好属于**异质偏好或信念层**，塞进 ξ 之后再把 ξ 解释成消费者认知，是循环论证。
5. **把非线性个体变量先取均值再代入当"基准"。** `G(E[ω]) ≠ E[G(ω)]`。真正嵌套的基准是把**消费者类型分布退化到一个预定代表类型**，取均值的版本只能叫 `mean-index Logit approximation`。
6. **用平均系数比冒充平均比率。** `E[γ/α] ≠ E[γ]/E[α]`。资本化率、WTP、福利货币化都要**逐消费者/逐抽样**算完再聚合；GHvB 本应用的"均值之比"近似估计曾提高一倍以上；工作稿D.4只是说明聚合次序不能互换，偏误符号/幅度不是普遍定理，也不单独识别心理机制。
7. **把文献数字或已撤回的命题搬进项目。** 续航曲率、残值改斜率、连续楔子替代对照组、P18 解决无对照组、5.58%/200 km/0.65 等，2026-09-20 纠错台账已撤回或禁止移植，清单在 `extension_genealogy.md` 第 9 节。
8. **把校准嵌套 logit 当作估计的 RC-BLP。** 需求侧 RC-BLP 可只有异质效用、聚合份额反演与内生性/GMM 识别，不强制包含供给。只有称为 BLP 需求—供给模型时才另要求多产品定价 FOC 与成本反推；Allcott 等的 IRA 校准嵌套 logit 不能据此冒充估计的 RC-BLP。

## 识别：逐参数登记，不许打包

聚合份额通常只识别**复合响应**。上表之前，对每个非线性参数登记五栏：变化来源 · 排除变量或微观矩 · 有效支持 · 主要 rival channel · 矩 Jacobian 局部秩。

- 价格 IV **不会自动**识别标签注意或未来成本资本化；
- 非线性参数必须有有效变化和足够矩条件，使矩 Jacobian 对所估参数局部满列秩；不是机械地给每个参数配一个不同 IV。"BLP-style instrument" 的名字不证明排除限制；差异化工具/近似最优工具仍须论证有效性，并报告弱识别诊断；
- 不可遗漏政策楔子的直接效用路径后把它当excluded price IV；完整建模后的条件排除、可分离成本分量、相关性和联合秩须另证，不是放入标签就自动有效（见identification_and_micro_moments.md §2）；
- 条件需求 ≠ 完整需求（Berry & Haile 2024）：能识别价格弹性，不等于能识别改标签、改属性的效应。

微观矩优先级、抽样权重写法、第一—第二选择模板见 `references/identification_and_micro_moments.md`。核心事实：**人口—选择矩可加强观测异质性 Π 的识别；Σ 能否识别取决于聚合市场特征、价格、份额、有效工具和矩条件的联合变化与局部秩。** 第二选择或选择集变化有帮助但不是识别 Σ 的必要条件；禁止反向宣称没有这类数据就不能估计标准 BLP 随机系数。 第二选择数据等于观察"删掉第一选择"的反事实集合，对替代模式价值最高。

## 供给、反事实、福利

- 静态多产品 Bertrand 只给"固定价格需求效应"与"maintained Bertrand 下的价格反馈"两件事。它**不识别**广告、认证操纵、工程属性或产品进入——那些要各自的 FOC、成本函数与额外工具（`extension_genealogy.md` S1–S4）。
- 均衡价格用 Morrow–Skerlos 的 ζ 固定点比直接迭代稳；两种都没有唯一性定理。
- 反事实先登记状态向量（改什么、固定什么），所有场景共用同一组随机抽样，`ξ` 固定为预定基准质量。
- 通道非线性交互，逐一关闭有顺序依赖，用 Shapley 分摊；但 **Shapley 只能分配已经分别识别的机制**，把复合项 `γ·a·ϑ` 算成三个"因果贡献率"是假的。
- 福利：B0/B2 用逐抽样 `logsum/α_i`（Small–Rosen 的成立条件见 `micro_foundations.md` 第 8 节）；nested/RCNL 必须换成对应的 nested-GEV surplus；有收入效应时逐个体根求 CV/EV；标签或质量变化**不由选择概率非参数点识别**，要并列"参数点估计 / 弱可分敏感性 / 界或不可识别"三层；信念有误时决策福利与体验福利分开。
详见 `references/supply_welfare_counterfactual.md`。

## 数值与验收

必过项：先跑 `scripts/blp_selftest.py` 确认公式没抄错 · 每个市场 Berry 反演收敛并记录 sup norm · 固定 common random draws · 多起点、多优化器得到相近目标值 · 解处一阶条件与二阶条件都满足 · 解析梯度与有限差分一致 · `∂s_j/∂p_j<0` 且交叉导数非负（无网络效应或互补项时；有间接网络效应的模型可以出现负交叉弹性）· markup 与 mc 经济上合理 · `α, γ, κ` 保证为正（用相关对数正态块，不要事后截断正态抽样）· 矩 Jacobian 秩与 profile objective · 生成变量（映射楔子、信念校准、市场规模、微观矩、模拟份额）全部进全流程 bootstrap。
单元测试清单与代码入口见 `references/estimation_algorithm_and_code.md`。

## 本机资产与调用顺序

`references/corpus_and_verification.md` 给出资产层级的确切路径、已失效路径、08-25 以后新增的语料、以及**语料分类标签的已知错误**（28 篇里 4 篇跨构建不一致，其中 `I6ZAU5HX` 索引写 canonical 而其卡片写 reduced-form DID）。
规矩：**索引字段不构成证明**。语料里的 APA 串一律缺卷期页，进正文前走 `econ-empirical-research` 补齐。`econ-research-craft` 的检索索引已于 2026-10-07 重建并收入全部 BLP 语料，查具体论文或项目判决可用 `python D:\codex\.codex-home\skills\econ-research-craft\scripts\find_reference.py --query "<问题>" --corpus blp-skill,struct-skill,blp-iter-cards,blp-papers,blp-fulltext`（语料标签表见该 skill 的 `references/retrieval-workflow.md`）。

## 用户当前项目

中国 NEDC→WLTC/CLTC 工况重标 × 跨动力替代。**先读 `references/project_china_driving_cycle.md` 第 14–20 节**（08-26 至 10-07 的研究架构、数据事实、制度事实、识别出路、机制检验特征与关键路径），凡与旧节冲突处以这几节与 `D:\codex\research-memory\fuel_econ_lit_2026_refresh_20260920\MEMORY_MAP.md` 为准；再读 `D:\codex\output\blp_driving_cycle_structural_research_20260824\00_DURABLE_TASK_BRIEF.md`。

## 输出纪律

- 每条展示公式打 `[O]/[D]/[P]/[I]` 标签并进逐式账本（见 `structural-model-building` 的 ledger 协议）；引用本机精读卡里已原页核验、本轮未再开页的式子标 `[O·卡]`。
- 报告证据层级：`fulltext-grounded` / `manual close reading` / `equation-proof-level manual review`，三者不得合并成一句"全部精读过"。
- 缺市场规模、outside share、成交价、产品级销量或必需微观矩时，**明说最强可辩护版本是什么、缺哪一块数据卡住了下一层**，不要用复杂数值替代缺失的数据变异。
