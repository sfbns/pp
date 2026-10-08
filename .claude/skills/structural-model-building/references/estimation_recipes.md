# 结构模型估计配方（BLP 以外）

BLP 的估计（嵌套不动点、Berry 反演、近似最优工具、微观矩、pyblp）见 `blp-model-building/references/estimation_algorithm_and_code.md`。本文件给动态离散选择、GMM 推断、模拟矩、两步法与校准的最小配方，第 7 节再给进入、动态博弈、拍卖、生产函数与加价、匹配、量化空间六类模型族各一条路由级配方。
第1–6节中实际受检的教学环节由 `python D:\codex\.codex-home\skills\structural-model-building\scripts\structural_selftest.py` 用小例子复现（T1–T9 当前17条检查；包含新增优化器成功、梯度及失败分支检查；历史12项不是当前覆盖量）。
文献于2026-10-07经Crossref核对题名、年份与期刊（`D:\blp-structural-skill-config\work_20261007\crossref_canonical_output.txt` 与 `D:\blp-structural-skill-config\work_20261007\crossref_round3_output.txt`）；该历史检查仅为元数据。2026-10-08补核McFadden/Pakes–Pollard、Hansen/Hotz–Miller/Magnac–Thesmar/GPV/Choo–Siow/Weyl–Fabinger的指定原刊目标页，记录分别在项目 evaluations/round03_preflight 和 round02/skills_evidence/general；不是整篇通读或其它经典原典全部已核。标 `[D]` 的仍是标准/独立推导，应用须回对应版本与条件，未核范围不升级。

2026-10-08新增独立条件回归：`D:\codex\.codex-home\skills\structural-model-building\scripts\primitive_conditions_selftest.py` 实际检验成本曲率可推翻无条件转嫁界，以及光滑无偏模拟器方差可高于1+1/S；它是另三条合成检查（两种成本/conduct规格的转嫁与一个光滑模拟方差反例），不把主脚本17条改称20条，也不认证经验识别。
本机可读的教学代码骨架在 `D:\codex\research-memory\BLP_structural_models_memory_skills_configs_2026-08-24\07_structural_model_code\src\econ_model_agent\structural\`（`dynamic_discrete_choice.py`、`gmm.py`、`blp.py` 里的 `SMMEstimator`），不是生产级估计器。

---

## 0. 任何结构估计开工前的三件事

1. **参数—变异—矩—反事实账本**：每个原语写清动它的变异、对应的矩、标签（直接观测 · 已识别 · 集合识别 · 校准 · 借用 · 归一化 · 只在反事实中出现），以及它进入哪个反事实（用户专家包 structural_professor 记忆第 1、4 节，`D:\codex\economics_theory_agent_complete_gpt55_xhigh\kb\08_hypothesis_packaging_45\agent_memories\structural_professor.md`）。
2. **随机抽样固定**：模拟用的抽样在参数之间与情景之间都固定（common random numbers），否则目标函数不光滑、反事实差分里混进模拟噪声。
3. **校准用过的事实不能再当验证**：同一个事实既拿来调参又拿来宣传"样本外吻合"，是该记忆第 7 节否决清单第 4 条。

## 1. GMM 推断

- **两步有效 GMM**：第一步用单位阵或 `(Z'Z)^{-1}` 得一致估计，第二步用残差构造 `Ŝ`、取 `W = Ŝ^{-1}`。本机 `gmm.py` 的 `GMMEstimator.two_step_fit` 与 `gmm_sandwich_standard_errors` 实现了这两步与夹心方差。
- **过度识别检验**（Hansen 1982 *Econometrica*）`[D]`：有效权重下 `J = N·ĝ'Ŵĝ → χ²(L − K)`，L 是矩个数，K 是参数个数。**J 拒绝说明矩之间不一致**（工具无效或模型设定错）；**J 不拒绝不证明工具有效**，只说明这组矩彼此没有冲突。自检 T4：工具有效时拒绝率 4.7%，有一个工具进入误差项时拒绝率 100%。
- **弱识别**：报第一阶段强度（线性部分报 Kleibergen–Paap 一类统计量，Kaneko & Toyama 2025 报 18.290，卡 `D:\fuel-econ-lit-2026\cards\P10_Kaneko_Toyama_2025_精读卡.md`）、矩 Jacobian 的秩与条件数、profile objective 是否平坦；弱识别时用对弱工具稳健的推断，不要只报 Wald 置信区间。

## 2. 模拟矩（SMM）与模拟误差

- **方差放大** `[D]`（McFadden 1989；Pakes & Pollard 1989，均 *Econometrica*）：模拟矩的残差等于数据残差减去模拟误差，二者独立，方差相加。每个观测用 S 个独立抽样、抽样在观测之间独立时：若模拟误差的方差恰为数据残差方差的 1/S（频率模拟器，或按数据同一结构模拟 S 倍样本再对矩），估计量渐近方差是精确矩 GMM 的 `(1 + 1/S)` 倍；仅“光滑”不保证模拟方差更小。一般GMM设D=∂g/∂θ′、固定对称权重W、H=D′WD、Ω_g=lim Var(sqrt(N) ĝ)，则sqrt(N)(θhat−θ0)的渐近协方差V=H^{-1}D′W Ω_g W D H^{-1}，估计量方差近似V/N、标准误为其对角元平方根；独立设计下Ω_g=Ω_data+Ω_sim/S，数据与模拟相关时还须减去相应交叉协方差及转置，共享抽样须计跨观测相关。只有特定Rao–Blackwell条件化/方差缩减设计才保证相对给定原模拟器弱降低；不能把它当通用低于(1+1/S)的规则。比例同方差特例下**方差乘1+1/S，标准误乘sqrt(1+1/S)**。自检 T3 是线性特例：S = 2 时模拟得 1.488，理论值 1.5。
- **BLP 也有这一项**：BLP (1995) 式 (5.6) 的渐近方差含模拟误差分量 `V_3`（`blp-model-building/references/blp1995_verified_equations.md` 第三节，原页已核）。
- **本机骨架的缺口**：`blp.py` 的 `SMMEstimator` 没有做模拟误差的方差放大，用它报标准误时按实际模拟设计估Ω_sim及相关项，只有满足上一段比例条件才乘(1+1/S)；可采用与抽样/模拟设计一致的全流程bootstrap。
- 权重矩阵同样两步构造；模拟次数要足够大到让 `1/S` 相对 1 可以忽略，或者如实报放大后的标准误。

## 3. 动态离散选择（DDC）

**模型** `[D]`：状态 x、行动 a，流量效用 `u(x, a; θ) + ε_a`，ε 服从 i.i.d. I 型极值，贴现因子 β，转移 `F(x'|x, a)`。积分价值函数 `V(x) = log Σ_a exp(u(x,a;θ) + β E[V(x')|x,a]) + γ_Euler`，选择概率是 logit 形式的条件选择概率（CCP）。

**两种估计法**
- **嵌套不动点**（Rust 1987）：对每个 θ 在内层把 V 迭代到收敛（它是模为 β 的收缩），外层对 CCP 做最大似然。自检 T2：β = 0.95 已知时，从 2 万个模拟决策还原 (θ1, θ2) = (0.254, 3.04)，真值 (0.25, 3)。本机 `dynamic_discrete_choice.py` 的 `DynamicDiscreteChoiceSolver.solve / log_likelihood / simulate` 实现了值迭代、对数似然与模拟。
- **CCP 法**（Hotz & Miller 1993 *REStud*）：先从数据非参数估 CCP，用它反推条件价值之差，避免每个 θ 都解一次动态规划；代价是第一步 CCP 的估计误差要进推断（全流程 bootstrap）。
  最小配方 `[D]`：第一步用灵活 logit（状态的多项式）估 `P̂(a|x)`，访问少的状态靠平滑而不是频率；第二步对每个 θ 只解一次线性方程给策略 P̂ 估值，`V = (I − βF^{P̂})^{-1} Σ_a P̂_a ∘ (u_a(θ) + γ_Euler − log P̂_a)`，其中 `F^{P̂} = Σ_a P̂_a ∘ F_a` 是 P̂ 下的状态转移、`γ_Euler − log P̂_a` 是 I 型极值冲击在"选了 a"条件下的期望；再由 `v_a = u_a + βF_a V` 得到隐含 CCP `Ψ(θ; P̂)`，最大化伪似然 `Σ_t log Ψ_{a_t}(x_t; θ, P̂)`。在 Ψ 与 P̂ 之间反复迭代是 Aguirregabiria & Mira (2002, Econometrica 70(4):1519–1543, DOI 10.1111/1468-0262.00340) 的单主体 NPL；2007 年论文是动态博弈扩展，不是此处单主体方法的原始出处。自检 T7a 验证 `Ψ(θ_0; P_0) = P_0`（真值处的不动点），T7b 用两步 CCP 从同一批 2 万个模拟决策还原 (0.254, 3.04)，与 NFXP 一致。
- 两种方法外层都用导数法（BFGS 等），不要用 Nelder-Mead，理由与 BLP 相同（见 `blp-model-building/references/estimation_algorithm_and_code.md` 第 0.4 节）。

**识别**
- **贴现因子与流量效用（连同参照选项的归一化）一般不能同时非参数识别**（Magnac & Thesmar 2002 *Econometrica*）。做法二选一：事先固定 β 并做敏感性；或找只影响未来、不影响当期效用的排除变量（Abbring & Daljord 2020 *Quantitative Economics*）。
- 理性预期下，可观测状态的转移可以在第一阶段直接从数据估出；用主观信念时，贴现与信念会混在一起。
- Chou–Derdenger的正例须按版本和限制阅读：本轮直接核的是2022年7月早期稿 `D:\auto-demand-lit-2026-09\pdf\J07_ucr2022.pdf`（SHA256 `5bb47da11b97e9ab6e103b61e72f39e42ce21dbf5ee9844bce3a95980a3a7ef3`），不是把该稿假设编号直接认证为2025刊本。PDF17的Assumptions1–3保留I型极值/序列独立冲击、Markov与条件独立、同价格敏感度消费者的共同条件信念；放松的是“主观条件转移等于数据转移”的理性预期，不是允许任意信念。PDF22–23的β恢复还依赖已恢复的CCP/其它原语、Eξ=0、固定异质类型下的平稳/遍历与连续性，以及至少两组非退化矩关系；需正确处理非随机退出。PDF25的直觉不取消这些限制。不能据此说仅有一般市场车型月份额即可同时自由识别贴现和任意主观过程。目标页核读，不是全文/刊本全假设核验；具体页图和自有条件反例见项目 `memos/round06_source_scope.md`。
- 单元测试：β = 0 时动态模型必须退化成静态 logit（自检 T1）。

## 4. 两步法估计的博弈与进入模型

- 动态博弈两步法（Bajari, Benkard & Levin 2007；Aguirregabiria & Mira 2007，均 *Econometrica*）`[D]`：第一步非参数估策略或 CCP，第二步用均衡条件估原语。推断要把第一步的估计误差带进去（对两步整体 bootstrap）。
- 多重均衡：数据通常只显示被选中的那个均衡；反事实必须写明均衡选择规则，否则结果不唯一。静态进入博弈在多重均衡下可以改用矩不等式给参数的界（Ciliberto & Tamer 2009 *Econometrica*）。

## 5. 校准、借用与集合识别的参数

- 校准值保留来源与合理区间；借用的弹性保留原研究的样本与定义；二者都不能叫"已识别"（structural_professor 记忆第 7 节否决清单第 3 条）。
- 福利稳健性按顺序做：先变动经验上弱的参数，再变函数形式与形状，再变市场边界与闭合，最后变分配权重与转移；决策符号在可行集里不变时报稳健距离或界（同一份记忆 Action F；例见 Kang & Vasserman 2025 AER 卡 `D:\codex\economics_theory_agent_complete_gpt55_xhigh\kb\08_hypothesis_packaging_45\cards\batch_c\p0075.md`）。

## 6. 机制分解与受限基准的两条数值事实

- Shapley 分摊在通道有交互时仍满足"各通道贡献之和 = 全开减全关"（自检 T5），但它只分配已分别识别的机制，见 `identification_and_claim_ladder.md` 第 4 节。
- 受限基准必须把类型分布退化到一个预定代表类型；先把个体变量取均值再代入的 `G(E[ω])` 与异质模型的 `E[G(ω)]` 不同（自检 T6a），不能参加"方差归零回到基准"的等价测试。正确的嵌套是同一个模型、同一组抽样，类型 `ω = ω*·exp(σz)`，σ = 0 时恰好等于基准 `G(ω*)`，σ 变小时差距按 σ² 收缩（自检 T6b），见 `when_and_which_model.md` 第 4 节。

## 7. 其他模型族的最小配方

每条只写到"识别变异、估计、最常见的失败"三栏，是路由级配方，全部标 `[D]`：2026-10-07曾只有元数据核对；当前部分经典原典已有首段列明的指定页审计。它们不是整篇读完或该族生产实现，具体版本/假设/推断仍按逐项来源台账核对；未审部分不升级。

| 模型族 | 识别变异 | 估计 | 最常见的失败 |
|---|---|---|---|
| 静态进入（Bresnahan & Reiss 1991 *JPE*） | 市场规模在市场之间的外生差异 | 有序 probit：观测到 N 家企业，当且仅当第 N 家进入有利可图而第 N+1 家不划算，由此估出容纳 N 家所需的市场规模门槛 `S_N`。人均门槛之比 `(S_{N+1}/(N+1))/(S_N/N)` 大于 1 说明新进入者压低了利润率，趋于 1 说明竞争强度不再随企业数变化 | 企业异质时，均衡下的企业组合不唯一；改用 Ciliberto & Tamer (2009) 的矩不等式给参数的界 |
| 动态博弈（Bajari, Benkard & Levin 2007；Aguirregabiria & Mira 2007） | 需求、成本与竞争者数这些状态随时间的变化 | 第一步从数据估策略函数或 CCP 与状态转移；第二步 BBL 用前向模拟算出观测策略与扰动策略的价值，以"观测策略的价值不低于任何单方扰动"构造最小距离目标；Aguirregabiria–Mira 在 CCP 与参数之间迭代伪似然（NPL） | 第一步的估计误差与有限样本偏误传入第二步；数据混有多个均衡时第一步就不一致；未观测的市场异质性 |
| 一价拍卖（Guerre, Perrigne & Vuong 2000 *Econometrica*） | 出价分布本身：对称独立私人价值、风险中性下，均衡出价是估值的严格增函数，一阶条件给出逆映射 | `v = b + G(b)/[(I−1)g(b)]`，G、g 是出价的分布与核密度，I 是投标人数；两步得到估值分布。自检 T8 从模拟出价还原估值，内部区间平均误差 0.0016 | 未观测的拍卖异质性会让出价看似关联；进入内生（只有估值高的人来投）；保留价与支撑边界处的核估计偏误 |
| 生产函数与加价（Olley & Pakes 1996；Levinsohn & Petrin 2003 *REStud*；Ackerberg, Caves & Frazer 2015；De Loecker & Warzynski 2012 *AER*） | 投入选择的时序：资本在上期决定，可变投入在生产率实现后选择；生产率服从马尔可夫过程 | 第一步用代理变量（投资或中间投入）把生产率写成可观测量的函数，剥掉测量误差；第二步用生产率创新与事先决定的投入正交，例如 `E[ξ_t·(k_t, l_{t−1})] = 0`（ACF 把劳动系数也移到第二步，因为第一步里劳动与代理函数共线）。加价 = 可变投入的产出弹性 ÷ 该投入支出占收入的份额，份额用去掉第一步误差的产出算。自检 T9 在常弹性需求下验证这个比值等于 P/MC | 产出用收入代替数量时价格混进"生产率"，比值法给出的加价几乎不含信息（Bond, Hashemi, Kaplan & Zoch 2021 *Journal of Monetary Economics*）；所谓可变投入其实有调整成本时，一阶条件不成立 |
| 匹配（Choo & Siow 2006 *JPE*） | 各类型已匹配与未匹配的人数 | 路由级标准推导，非本轮原式认证：两侧独立I型极值误差且两侧尺度均归一为1、可转移效用时，总匹配剩余 `Φ_ij = log(μ_ij² / (μ_i0·μ_0j))`；μ_ij为匹配对数量（不是对数），μ_i0、μ_0j为单身数量。共同尺度σ时右端乘σ；不能把归一化效用量直接叫货币收益 | 单一截面只识别双方合计的收益，分不开两边各自偏好；不等尺度、相关误差或其他分布需重新推导。本机仅有首段所列指定原页审计，不是整篇原文/全定理核验，用于论文前逐式回源 |
| 量化空间（Allen & Arkolakis 2014 *QJE*） | 区位间的人口、工资与贸易或通勤流；贸易成本的地理差异 | 用均衡条件把观测的人口与工资反解成各地的生产率与舒适度（模型恰好拟合观测分布），再做反事实；贸易弹性与集聚、拥挤参数通常借自外部估计或用准实验另估 | 反解出的基本面与数据一一对应，样本内拟合不能当验证；均衡是否唯一取决于集聚与拥挤参数的相对大小，具体条件回原文核对 |

动态离散选择的配方在第 3 节；本机有精读卡的实例见 `when_and_which_model.md` 第 3 节对应行（采购进入 p0028、空间 p0097、生产法与需求法加价对照 J03）。
