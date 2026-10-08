# M2 第三方审稿报告（第 2 轮）：机制一「认证信息偏差收敛与标签精度权重」（第 2 版）

- 审稿人：blp_referee（独立第三方，全新上下文；与作者同配置）
- 日期：2026-10-08（UTC 21:37 完成验算）
- 审议对象：`deliverables/M2_机制一_认证可信度.md`（git `72b54eb`，SHA256 `23914fe25ec6c7a91bfa91bbe4e1ce513a291c3a414ae9754910b42d2ce9464d`）；复现脚本 `tools/m2_examples.py`（SHA256 `67d4b4a4e26cb677c3693d9ab49a60587166f7e7b543f81db277ebe9fe6c74d0`）。审稿过程中未修改任何被审文件。
- 背景（不评分）：`deliverables/M1_基准BLP模型.md`（记号来源）；交叉核对时还查阅了 `M3`、`M7` 中引用 M2 的段落。

## 0. 加载清单与独立性声明

**实际打开的文件**：`.claude/agents/blp-referee.md`（评分细则与致命项规则）；`blp-model-building/SKILL.md`、`references/构造与组合协议.md`（D04 C×I、D09 I×W）、`references/模块集成图.md`、`references/technical/micro_foundations.md`、`references/technical/project_china_driving_cycle.md`；`blp-project-professor/SKILL.md`、`references/five-paper-kernel.md`、`references/constructive-model-design.md`（两源失效、CARA、表示不变性）、`references/model-formula-ledger.md`（V6-M01/M02）；`structural-model-building/SKILL.md`、`references/identification_and_claim_ladder.md`、`references/mechanism_construction_and_theory.md`；`economics-expert-reviewer/SKILL.md`、`references/review-standard.md`、`references/evidence-boundaries.md`；`top-journal-hypothesis-packaging/SKILL.md`、`references/orchestration-contract.md`；文献卡 A15（Reynaert–Sallee 2021，含 §6.1 信念式公式校正、§7(3) 离散度图 4）、A14（GHVB 2021，§6、§10 信任讨论）、A05（GRV 2018，油耗变量口径）；`MEMORY/00_断点记忆_CHECKPOINT.md` 的 A 节（逐字）。

**独立性**：未阅读作者自评、采纳说明或目标分数。按委托要求，先完成本轮全部独立核验与打分，之后才阅读第 1 轮报告 `reviews/M2_review_round1.md` 做逐条核对（第 7 节）；分数只依据当前稿件。scratchpad 中其他会话留下的脚本与文件未被使用，本报告全部数值来自本轮自写脚本（第 8 节）。

---

## 1. 总体评价

**一句话贡献**：M2 把“工况切换缩小真实—标称差距”拆成两层——客观层的同口径误差变化（认证信息偏差收敛），和消费者层的双信源贝叶斯信念 $B=\kappa\zeta L+(1-\kappa)\widetilde O$——再经广义价格中的 $\gamma KB$ 进入 M1 的随机系数需求，并给出份额的系统条件、需求不降的容许楔子以及识别约束。

**第 2 版的主要进步（经本轮实际验证）**：

1. 原语统一。比例信号 $\zeta L=T+\upsilon$ 贯穿全文，与 M1 的 $B=\zeta L$ 精确嵌套。表示不变基准 (M2.11a) 与 M1 (M1.34) 同形，阈值 (M2.16) 来自被估计的同一模型。
2. 代数全部正确。(M2.3)(M2.4)(M2.7)–(M2.11a)(M2.16)–(M2.18)(M2.21)–(M2.23)(M2.25) 均用 sympy 逐式核对通过；数值例 A–G 全部复现。(M2.14) 的线性化在异质 $K_i$、动力间 $\gamma_d$ 不同的随机系数 logit 中与精确份额变化吻合，(M2.15) 正确预测了每个产品份额变化的符号（第 8 节 §8.3）。
3. 新增的鞅性质命题 M2.0 正确且有洞见：理性预期下动力平均信念不变，“可信度红利”在平均意义上只能来自过度怀疑被纠正、新的轻信或二阶通道。这是对用户“油耗变高、需求反而上升”这一问题最有理论含量的回答。
4. 命名纪律到位。$\kappa$ 称标签精度权重，$\zeta-1$ 称感知偏差率；红利分为纠偏型与轻信型，并写明“红利 ≠ 福利”；“欺诈”只留给有证据的故意误报。gaming 主要表现为系统平移，这一点与 A15 卡（图 4：离散度不升）核对一致。GHVB §10 的加法/比例不信任讨论引用准确。
5. 识别部分诚实：给出约化系数与结构参数的计数（4 对 5），说明 M2-A 机械地施加了已知平均换算，交代固定效应残差化后剩余的变异来源与失效情形，处理生成变量推断与 $\kappa=1$ 的边界检验。

**仍未达标的核心问题**（详见第 4 节）：

1. **基准规格 M2-A 的一个未被认识的机械性质**：校准 $\widehat\zeta_{d,c}=\sum\bar O/\sum L^c$ 使校准样本上的动力平均信念变化恒等于 $\Delta\kappa_d(\overline{\bar O}-\overline{\widetilde O})\approx0$。无论 $\kappa$ 怎样变，M2-A 都**不能**产生动力层面的可信度红利或折价，而这正是用户问题的核心。文中“红利只能经 $\Delta\kappa$ 体现”和“$\gamma_{d,N}=\gamma_{d,X}$ 检验维持假设 A-$\gamma$”两处说过头了：后者是 A-$\gamma$ 与校准的联合检验。
2. **纯电（和插混）续航渠道没有进入可估规格和识别**：(M2.24) 与 §M2.10 只覆盖能源成本项；系统条件 (M2.14) 也只含 $\varpi\Delta B$。BEV 的 $\zeta^R,\kappa^R/\hat\tau^R,\Omega^R,\eta$ 如何识别没有讨论，而 P-M2-7（纯电反向）是主要预测之一。
3. **两处经济学结论缺条件**：(i)“纠偏型改善体验效用”在 $\gamma<1$ 时不成立（次优：过度怀疑部分抵消了低资本化），与 M7 自己的 CF5 论证矛盾；(ii) 风险溢价通道在 M1 的终身财富 CRRA 微观基础下量级约为 $10^{-4}$ L/100km，比信念效应小三个数量级，却被列为“需求上升”的渠道之一，没有给出量级。
4. **第二信源有效性检验的设计偏差**：锚定检验 (M2.5) 用当月新增评论时，评论流混有切换前的购车者，$\pi^A=\rho^A\cdot s^{post}$ 被衰减，检验偏向接受“车主实测独立”。M2-B 中 $v_j$ 只随评论数 $n$ 变化，与车型生命周期、热度、标签显著性衰减混淆；$\sigma_b^2$ 不能由单一平台识别。
5. **一处文献归属不实**：M2-C(ii) 把 $B=\widetilde O$（信念等于车主实测）称为“GHVB/GRV 式消费者知道真实能耗”。实际上 GRV 用官方油耗评级，GHVB 正是利用消费者对官方评级变化的反应，二者都对应 $B=L$。

---

## 2. 八维度得分表

| 维度 | 满分 | 得分 | 扣分理由（对应第 4 节必须修改项） |
|---|---:|---:|---|
| 经济学基础与原语（偏好、预算、时序、信息集） | 15 | 12 | 贝叶斯两步更新、客观/主观参数分离、鞅性质、期望缺口的凸性与 CARA 推导都从原语推出，质量高。扣分：纠偏型“改善体验效用”未加 $\gamma<1$ 的次优条件，且与 M7 矛盾（R2-3）；风险溢价通道在 M1 微观基础下量级可忽略，却作为符号反转的候选渠道，未做量级核算（R2-4）；车主报告共同偏差 $E[b]=0$ 是未说明的关键原语假设（S3）；插混把后验均值代入凹函数 $UF$，与 §M2.8.2 自己的 Jensen 论证不一致（R2-10） |
| 数学推导正确（逐步可验证、符号/单位/方向） | 20 | 18 | 全部展示式代数经 sympy 核验无误，单位一致（$W^{\ast\ast\ast}$ 中 $\Delta p/(\gamma\bar K^w)$ 为 L/100km）。扣分：(M2.5) 写 $\pi^A=\rho^A$，在评论流混合队列时不成立（R2-5）；命题 M2.2 与 (M2.15) 的“当且仅当”只在一阶线性化下成立（R2-8）；(M2.11) 自称“与顺序无关”，实为两层嵌套的 Shapley（Owen 型），与对称三因子 Shapley 相差 $\Delta\kappa\Delta\zeta\Delta L/12$（R2-8）；“比值的均值”应为“均值之比”（R2-8） |
| BLP/结构模型一致性（份额、反演、IV/GMM、正规化、outside） | 15 | 12 | 广义价格位置正确，不重复计价；外部选项不受重标影响；(M2.14) 与 M1 (M1.34a) 一致并经数值验证；IV/先决性/准差分与 M1 衔接。扣分：BEV/PHEV 续航渠道未进入 (M2.24)，系统条件只含能源成本项，续航部分与 M1 的嵌套条件（$\Omega^R\to0$）未写明（R2-2）；M2-A 的 $\kappa_{d,c}$ 是对贝叶斯 $\kappa_{jc}$ 的加总，异质性造成的“积之均值 ≠ 均值之积”偏误未讨论（S10）；插混 $\varpi$ 的定义不适用（S11） |
| 新参数的经济学构造与含义 | 10 | 9 | $\kappa$、$\zeta$、$\hat\tau^2$、$\rho^A$、$\mathcal R$ 都有经济学定义、量纲与可解释符号，命名不越级。扣分：$\hat\tau^{R2}_c$ 记号与路径标签 R2 冲突；BEV 段与 §M2.6.4 表残留“理性换算”（M1/M2.4 已改为“已知平均换算”）；P-M2-3 把机械换算称作“可信度渠道”（R2-9、S8） |
| 识别论证（变异、排除、秩、rival、falsifier） | 15 | 10 | 计数、约束、残差化支持、失效情形、生成变量推断与边界检验都写到了。扣分：M2-A 机械地消除动力平均信念变化而未被认识，“红利只能经 $\Delta\kappa$ 体现”误导（R2-1）；过度识别检验其实是联合检验，被说成检验 A-$\gamma$（R2-1，数值反例 0.6000 对 0.6277）；锚定检验衰减且有选择性发帖问题（R2-5）；M2-B 的 $v(n)$ 与生命周期混淆，$\sigma_b^2$ 不可识别（R2-6）；BEV 续航参数的识别完全缺失（R2-2） |
| 文献一致性与来源标注（不冒称原式） | 10 | 8 | RS 信念式与“gaming 主要是整体平移”核对 A15 卡一致；GHVB §10 引用准确；Frankel–Kartik、KOS 2007、Jin–Leslie、Nelson、Darby–Karni、Dranove–Jin、Blackwell 都是真实且贴切的理论锚点；[O·卡] 未冒称原式。扣分：M2-C(ii)“GHVB/GRV 式消费者知道真实能耗”归属不实（R2-7）；P-M2-3 使用“纯电 46 组中位数为 0”样本，未提项目记忆中的数据警示（R2-9）；来源账本漏列 (M2.2)，(M2.1) 正文标 [D]、账本标 [P]（S8） |
| 回应用户问题与数据适配（市场—月—车型数据） | 10 | 9 | 用户要求的两部分（切换对差距的影响；差距收敛经信念进入 BLP）、“信任还是欺诈”的命名、双向替代、“上浮多少需求不减”都有正面回答；数据需求（车型—月销量 + 口碑车主实测 + 评论数与购车时间）与用户的市场层数据相容。扣分：容许上浮只给单车型阈值，没有给动力组层面的阈值，续航（BEV/PHEV）也没有对应阈值（S4） |
| LaTeX 规范与可读性 | 5 | 4 | xelatex 编译通过，19 页；只有一处 0.116pt 表格溢出，无缺字；框式、underbrace、aligned、`\dfrac` 均正确。扣分：§M2.4 的列表项“3./4.”紧接段落，被并入段落正文（PDF 第 8 页可见）；行内数学用 `*`（$W^\ast$、$W^{\ast\ast}$），违反 CLAUDE.md §3；$\hat\tau^{R2}$ 有歧义（S8） |
| **合计** | **100** | **82** | 未触发致命项 |

---

## 3. 致命项

逐条核查 `blp-referee.md` 的五类致命项：

1. **导数方向或符号错误导致结论反转**：未发现。$\partial\kappa/\partial\hat\tau^2<0$、$\partial v/\partial n<0$、$\partial\bar A/\partial B^R=-n\Pr(D>T^R)$、$\partial\bar A/\partial\sqrt{\Omega}=nE_D[\phi]$、(M2.14) 交叉项正号、(M2.23) 不等式方向均经符号与有限差分核验。
2. **把校准/假设说成已识别**：M2-A 在表中列为“额外约束 + 可识别对象”，属于条件识别，表述诚实。但“$\gamma_{d,N}=\gamma_{d,X}$ 检验维持假设 A-$\gamma$”把联合检验说成单一假设的检验，属措辞越级（R2-1），程度未到致命。
3. **福利公式在其不适用条件下使用**：M2 未使用 logsum 福利式。“纠偏型改善体验效用”是缺条件的福利陈述（R2-3），不是公式误用，不构成致命项。
4. **份额/反演/FOC 核心式错误**：无。(M2.14) 经数值核验。
5. **完全不回应用户核心问题**：未发生。

**结论：本轮未触发致命项。**

---

## 4. 必须修改项（按后果排序）

### R2-1【M2-A 基准：机械地消除动力平均信念变化；两处识别表述说过头】

**位置**：§M2.10.2 表 M2-A 行（“红利只能经 $\Delta\kappa$ 体现”“$\gamma_{d,N}=\gamma_{d,X}$ 是可检验的过度识别限制（检验维持假设 A-$\gamma$）”）；§M2.6.4 表“纠偏型或轻信型红利 → 平均下降 → 新能源 → 燃油”一行在 M2-A 下的可得性。

**问题 (a)：M2-A 下动力平均信念变化恒约为 0。** 校准 $\widehat\zeta_{d,c}\equiv\sum_j\bar O_j/\sum_jL^c_j$ 意味着在校准样本上 $\widehat\zeta_{d,c}\,\overline{L^c}=\overline{\bar O}$ 恒成立。对 (M2.8) 在动力 $d$ 内取样本平均：

$$
\frac1{J_d}\sum_{j\in d}\Delta B_j=\kappa_{d,X}\widehat\zeta_{d,X}\overline{L^X}-\kappa_{d,N}\widehat\zeta_{d,N}\overline{L^N}-\Delta\kappa_d\,\overline{\widetilde O}=\Delta\kappa_d\big(\overline{\bar O}-\overline{\widetilde O}\big)\approx0 .
$$

$\widetilde O$ 是 $\bar O$ 向以特征为中心的先验收缩的结果，两者样本均值几乎相同。数值验证（§8.4）：$\kappa$ 由 0.3 升到 0.9，平均 $\Delta B=+0.0036$（车型间标准差 0.51），与恒等式右边逐位相等。因此 M2-A 只能产生**动力内再分配**（以及经选择概率加权的二阶效应），不能产生用户问题核心所在的动力层面“可信度红利/折价”。“红利只能经 $\Delta\kappa$ 体现”须改为：“M2-A 下动力平均红利恒为 $\Delta\kappa_d(\overline{\bar O}-\overline{\widetilde O})\approx0$；$\Delta\kappa$ 只在动力内把信念从标签隐含值低于口碑的车型移向高于口碑的车型”。

**问题 (b)：过度识别检验是联合检验。** 若消费者实为天真（$\zeta_X=\zeta_N$）而 $\gamma$ 不变，M2-A 以 $\widehat\zeta_X=\widehat\zeta_N/(1+\bar w)$ 校准，会得到

$$
\hat\gamma_{d,X}=\gamma\big(1+\kappa_{d,X}\bar w_d\big)\neq\hat\gamma_{d,N}=\gamma .
$$

数值例：$\gamma=0.6$、$\kappa_X=0.6$、$\bar w=0.077$，得 $\hat\gamma_X=0.6277$（§8.4）。所以拒绝 $\gamma_{d,N}=\gamma_{d,X}$ 既可能是 A-$\gamma$ 不成立，也可能是校准（已知平均换算）、$E[b]=0$ 或锚定假设不成立。

**修改方案**：
1. 在 M2-A 行写出上面的恒等式，把 M2-A 定位为“动力内再分配规格”；把检验改称“A-$\gamma$ 与 $\zeta$ 校准、$E[b]=0$ 的联合检验”。
2. 增加两个**单边校准**规格。二者在 A-$\gamma$ 下恰好识别（4 个约化系数对 4 个参数），能直接检验用户关心的两条红利路径：
   - **M2-A′（只校准 NEDC，$\zeta_{d,N}=\widehat\zeta_{d,N}$，$\zeta_{d,X}$ 自由）**：$\gamma=\varphi^L_N/\widehat\zeta_N+\varphi^O_N$，$\kappa_N=(\varphi^L_N/\widehat\zeta_N)/\gamma$，$\kappa_X=1-\varphi^O_X/\gamma$，$\zeta_X=\varphi^L_X/(\gamma\kappa_X)$。用于检验天真（$\zeta_X=\widehat\zeta_N$）、已知平均换算（$\zeta_X=\widehat\zeta_N/(1+\bar w^L)$）与轻信（$\zeta_X<\widehat\zeta_X$）。
   - **M2-A″（只校准新工况，$\zeta_{d,X}=\widehat\zeta_{d,X}$，$\zeta_{d,N}$ 自由）**：对称求解，用于检验 NEDC 时代的过度怀疑（$\zeta_N>\widehat\zeta_N$），即纠偏型红利。
3. 在 §M2.6.4 表中注明每一行由哪个规格识别：天真/已知平均换算/轻信用 M2-A′，纠偏用 M2-A″，精度结构用 M2-B；M2-A 本身只识别组内重排。

**修复失败时仍成立的结论**：M2-A 下关于组内再分配（楔子高于/低于平均、精度梯度）的结论仍然有效；动力层面红利只能作为情景报告。

### R2-2【纯电（及插混）续航渠道未进入可估规格、系统条件与识别】

**位置**：(M2.24)、§M2.10 全节、(M2.14)–(M2.15)、§M2.7、§M2.12。

**问题**：
- (a) §M2.8 推导了 BEV 的贝叶斯期望缺口 $\bar A_i(B^R,\Omega^R)$，但可估规格 (M2.24) 只含 $\varphi^LKL+\varphi^OK\widetilde O$。$\zeta^R_{\mathrm B,X}$、$\kappa^R_c$（或 $\hat\tau^R_c$）、$\Omega^R$、$\eta$、$\varkappa$ 的变异来源、矩、约束与失效情形都没有给出。纯电能源成本又因 $K^E$ 几乎不随时间变化而弱识别（失效情形 (a)），结果 M2 对纯电实际上没有任何识别路径，而 P-M2-7（纯电反向）是主要预测之一。
- (b) 系统条件 (M2.14) 只含 $-\varpi_{ik}\Delta B_k$。BEV 重标主要改变续航，(M2.14)–(M2.15) 对 BEV 是不完整的。
- (c) 与 M1 的嵌套：M1 的 $A_i(\zeta^RL^R)$ 只在 $\Omega^R\to0$ 时恢复。在贝叶斯结构中这对应 $\hat\tau^R\to0$，并自动给出 $\kappa^R=1$。M2-A 中若 $\kappa^R$ 作自由参数，$\Omega^R=(1-\kappa^R)v^R_j$ 还需要车主续航数据的 $v^R_j$，文中未说明。
- (d) 用户也问到续航“上浮/下降多少需求不减”，文中没有续航版阈值。

**修改方案**：
1. 把效用变化写成一般式，并直接代入 M1 (M1.34a)：

$$
\Delta u_{ik}=-\varpi_{ik}\Delta B_k+\mathbf 1\lbrace d(k)=\mathrm B\rbrace\,\eta_i\chi(N_{mt})\,n^{long}_i\Big[\Pr\nolimits_i\big(D^{long}>T^R_k\big)\Delta B^R_k-E_D\big[\phi(z_{ik})\big]\Delta\sqrt{\Omega^R_k}\Big]+\mathbf 1\lbrace d(k)=\mathrm P\rbrace\,\Delta u^{UF}_{ik},
$$

$$
\Delta s_{jmt}\approx\int P_{ij}\Big(\Delta u_{ij}-\sum_kP_{ik}\Delta u_{ik}\Big)dF .
$$

2. 新增“§M2.10.x 续航信念的可估规格与识别”。可用变异：CLTC 跳变 × 补能密度 $N_{mt}$ 的跨城跨期变化；长途出行分布 $n^{long}$ 的跨市场差异；同谱系不同电池版本；按地区与季节的车主续航实测。约束：沿用 M1 的 $\zeta^R_{\mathrm B,N}=1$ 识别假设，或校准 $\hat\tau^R$。失效情形：BEV 自愿切换的选择性；同配置证据只有 6 款且约 45.7% 为同一数字写进两列。若无法识别，P-M2-7 应明确降为“情景/敏感性”。
3. 给出续航版的自身中性阈值：由 $\Pr(D>T^R)\,\Delta B^R_j(W^R)=E_D[\phi]\,\Delta\sqrt{\Omega^R_j}$ 解 $W^{R\ast}_j$，并给出插混纯电续航下降时的对应式。

### R2-3【“纠偏型改善体验效用”缺 $\gamma<1$ 的次优条件，与 M7 矛盾】

**位置**：§M2.5 末段（“两类红利都降低信念、提高需求，但福利含义相反：纠偏型改善体验效用……”）。

**问题**：M7 §M7.2 的体验效用以 $\gamma=1$、真实 $T$ 为规范，M7 的 CF5 也明确写道：“若只纠正信念而保留 $\gamma<1$，增益可能为负：当消费者原本高估能耗（怀疑过度）而又低资本化时，两种偏差相互抵消”。M2.5 的无条件陈述与此矛盾。数值验证（§8.4 V5，两车 + 外部选项）：$\gamma=1$ 时把 $\zeta$ 从 1.45 纠正到 1.30，体验福利 $2.2216\to2.2629$（改善）；$\gamma=0.6$ 时 $2.1046\to2.0424$（恶化）。

**修改方案**：改为条件陈述。以 $\kappa=1$ 的单维情形为例，标签隐含成本的决策权重为 $\gamma\zeta$，规范权重为 $\zeta^0$，成本权重扭曲为 $|\gamma\zeta-\zeta^0|$。纠正过度怀疑（$\zeta_N\to\zeta^0$）在二次近似下改善体验效用的条件是

$$
|\gamma\zeta_N-\zeta^0|>(1-\gamma)\zeta^0\iff\zeta_N>\frac{(2-\gamma)\,\zeta^0}{\gamma}\quad(\text{当}\ \gamma\zeta_N>\zeta^0);\qquad \gamma\zeta_N\le\zeta^0\ \text{时纠正必然恶化}.
$$

$\gamma=1$ 时条件退化为 $\zeta_N>\zeta^0$，恒成立。精确阈值需数值求解：$\gamma=0.6$ 时近似式给出 3.03，数值解为 2.68；$\gamma=0.8$ 时分别为 1.95 与 1.86（§8.6）。正文写“纠偏型在 $\gamma=1$ 时改善体验效用；$\gamma<1$ 时符号取决于 $\gamma\zeta$ 相对 $\zeta^0$ 的位置，见 M7 CF5/CF6 的联合报告”。

### R2-4【风险溢价通道的量级：在 M1 的微观基础下可忽略】

**位置**：§M2.9（M2.22）–（M2.23）；§M2.6.3 第 4 条“二阶通道：后验方差下降带来的风险溢价下降”；§M2.3.5 第 1 条。

**问题**：§M2.9 从 M1 的终身财富间接效用 $\mathcal V_i$ 推出 $\mathcal R_i=-\mathcal V_i''/\mathcal V_i'$。M1 (M1.6) 的 CRRA 设定给出 $\mathcal R_i=\rho_c/\mathcal W_i$。取 $\rho_c=2$、$\mathcal W=2\times10^6$ 元，$\mathcal R=10^{-6}$/元；按例 G 的后验方差变化 $\Delta\Omega=-0.069$（L/100km）²，$K=6950$：

$$
\tfrac{\mathcal R}{2}K(-\Delta\Omega)\approx2.4\times10^{-4}\ \text{L/100km},
$$

而文中各例的 $|\Delta B|$ 在 0.07–0.5 之间。要抵消 $\Delta B=+0.05$，需要 $\mathcal R\approx2.1\times10^{-4}$/元，即 $\rho_c\approx416$（§8.4 V4）。即使改为按年收入的窄框架（$\rho_c=2$、年收入 $10^5$ 元），该项也只有约 0.005 L/100km。这符合 Arrow–Pratt 的小风险逻辑：风险溢价是二阶小量。

**修改方案**：在 §M2.9 加一段量级核算。明确货币成本风险溢价**不能**合理解释燃油车需求的符号反转，只作完整性说明。把真正有量级的二阶通道写成：(i) BEV 期望缺口的凸性（非货币，例 F 中后验标准差 0→60 km 时缺口从 20 升到 35 km）；(ii) logsum 凸性带来的信息期权价值（见 S1）。同步修改 §M2.6.3 第 4 条与 §M2.3.5 第 1 条的措辞。

### R2-5【锚定检验 (M2.5)：评论流混合购车队列导致衰减；选择性发帖】

**位置**：§M2.2.1 (M2.5) 及其后各条。

**问题**：(M2.5) 用“当月新增评论”的均值，写 $\pi^A=\rho^A$。但切换后第 $t$ 月发表的评论中，有一部分来自切换前购车、看到的是 NEDC 标签的车主。若该月评论者中切换后购车者占 $s^{post}_{jt}$，则

$$
\pi^A=\rho^A\cdot s^{post}_{jt}\quad(\text{当 } s^{post}_{jt}\ \text{不随}\ j\ \text{变化时}),
$$

检验被衰减向 0（§8.4 V6：$\rho^A=0.3$、$s^{post}=0.3$ 时 $\pi^A=0.09$），偏向接受“车主实测独立于标签”这一关键假设。另外，若车主是否发帖取决于相对所见标签的“失望”，即 $T-\zeta L^{c(n)}$，评论数 $n_j$ 与 $\upsilon^N$ 相关，会同时污染 (M2.6) 的跨制度方差差分和 M2-B 的 $v_j$。

**修改方案**：
1. 主检验改为文中已提及的**队列检验**：按评论记录的购车时间，比较同硬件下切换前后购车者的报告；回归元写成 $\ln(1+w_j)\cdot\mathbf 1\lbrace t^{buy}_n\ge T^{show}_j\rbrace$。
2. 若只能用评论流，回归元改为 $S_{jt}\,s^{post}_{jt}\ln(1+w_j)$。
3. 报告 $\rho^A$ 的最小可检测效应（检验功效）。
4. 增加“发帖率检验”：切换后评论数增量是否随 $w_j$ 变化。

### R2-6【M2-B：$v_j$ 只随 $n$ 变——生命周期/热度/显著性 rival；$\sigma_b^2$ 不可识别】

**位置**：§M2.10.2 M2-B 行、(M2.25)、§M2.10.3 第 4 条、P-M2-2。

**问题**：$v_j=v(n_{j,t-1};\sigma_0,\sigma_b,\sigma_e)$，$\kappa$ 的全部变异来自累计评论数 $n$。$n$ 随车型上市月龄与热度机械增长，因此“标签权重随 $n$ 下降”与以下 rival 难以区分：标签显著性或广告随车龄衰减；买家构成从早期采用者转向主流；其他信息源（媒体、口口相传）随车龄累积，相当于 $v_j$ 有测量误差。先决不等于外生，交互项的斜率异质性需要单独论证。此外，$v_\infty$ 与 $v_j$ 依赖 $\sigma_b^2$，而 §M2.2.2 自己承认 $\sigma_b^2$ 的水平需要第二个独立车主数据源。因此 M2-B 中 $(\gamma,\hat\tau^2)$ 的识别是以假定的 $\sigma_b^2$ 为条件的。

**修改方案**：
1. 控制“车龄 × $K\cdot L$”“车龄 × $K\cdot\widetilde O$”交互，利用同车龄不同热度车型之间的 $n$ 差异。
2. 用 (M2.25) 的结构做判别：贝叶斯精度渠道预测 $\varphi^L/\varphi^O=\zeta v_j/\hat\tau^2$ 随 $n$ 下降，即**比值**改变；整体成本注意随车龄衰减的 rival 预测 $\varphi^L,\varphi^O$ 同比例变化，比值不变（与 M3 §M3.7 的表一致）。
3. 报告 $\sigma_b^2$ 网格（及其隐含的 $\kappa_\infty$）下的 $(\gamma,\hat\tau^2,\zeta)$。

### R2-7【文献归属：M2-C(ii)“GHVB/GRV 式消费者知道真实能耗”不实】

**位置**：§M2.10.2 表 M2-C 行。

**问题**：GRV 的燃油成本用的是 JATO 数据中的油耗 $e_{jk}$（L/100km；A05 卡第 75、121 行）。A15 卡第 88–90 行写明，RS 与 GRV 使用同一 JATO 来源，其中的油耗是官方评级（车辆按“品牌 × 车型 × 燃料 × 官方油耗”定义）。因此 GRV 对应 $B=L$。GHVB（A14 卡 §3、§6.2）的识别恰恰来自消费者对官方 EPA 评级变化的反应（车辆不变），也是 $B=L$。RS（A15 卡 §6.2(1)）假设 gaming 出现前信念“平均正确”，但同样用官方评级计算。三篇都没有把信念设为车主实测的真实能耗。

**修改方案**：M2-C(i)“$\zeta=1,\kappa=1$”才是 GRV/GHVB 的惯例，应如此标注。M2-C(ii) $B=\widetilde O$ 改称本项目设定的“经验信念基准”[P]；若要挂靠文献，可对应 RS 的 $\alpha=1$（完全识破，$\tilde x=x$）情形 [O·卡 A15]。

### R2-8【等式与命题的精确性】

**位置**：命题 M2.2、(M2.15) 框式；(M2.11) 前的说明；§M2.2.2。

- (a) (M2.14) 是一阶近似（“≈”），由它推出的 (M2.15) 与命题 M2.2 的“当且仅当”只在**一阶线性化下**成立，须写明。数值上，在本轮的随机系数例子中线性化与精确份额变化的符号一致，相对误差约 2%（§8.3）。
- (b) (M2.11) 是两层嵌套的 Shapley：先在 $\kappa$ 与 $\ell$ 之间对称，再在 $\ell$ 内的 $\zeta$ 与 $L$ 之间对称（Owen 型）。它不是 $(\kappa,\zeta,L)$ 的对称三因子 Shapley。例如数值效应项：

$$
\phi^{Shapley}_L-\bar\kappa\bar\zeta W=\tfrac1{12}\,\Delta\kappa\,\Delta\zeta\,\Delta L\quad(\text{sympy 核验，§8.2}).
$$

应把“与顺序无关”改为“在给定分组层级下与顺序无关”，或另报对称三因子 Shapley。
- (c) §M2.2.2“系统比率用比值的均值估计 $\widehat\zeta=\sum\bar O/\sum L$”：公式正确，因为在 $E[\upsilon^0\mid T]=0$ 下均值之比是一致估计（§8.5：1.297，真值 1.30；比值的均值为 1.306，有偏），但文字应为“均值之比”。GHVB 对两者的区分正是项目文献的重点。
- (d) “相对可信度（$0<\Delta B_j<\widetilde{\Delta B}_{-j}$）”所举的“燃油车切换期间未切换的纯电车”$\Delta B_j=0$，应写 $0\le\Delta B_j$。

### R2-9【P-M2-3 零楔子切换者：数据依据与命名】

**位置**：§M2.12 预测表 P-M2-3。

**问题**：
1. 文中称“纯电 46 组中位数为 0 的配对可用”。项目记忆记录：该历史 46 车型样本“不能认证原设计”（跨口径楔子标准差 0.218）；同配置纯电双测数据中约 45.7% 的配对是“同一数字写进两列”。记录为 0 的楔子可能只是字段复制，消费者并未看到新口径标签，也就不构成“切换”。
2. 楔子为 0 时，已知平均换算预测 $\Delta B_j=-\kappa\zeta_NL^N_j\bar w_d/(1+\bar w_d)<0$。这是**机械换算**效应，而文中其他地方明确不把它称为“可信度”，此处却把它归入“可信度渠道（$\Delta\zeta,\Delta\kappa$）”。

**修改方案**：
1. 要求核验零楔子切换者确实对消费者展示了新口径标签（用 `label_visible_from` 时钟），并剔除字段复制。
2. 预测改写为三分：天真为 0；已知平均换算为 $-\kappa\zeta_NL^N\bar w/(1+\bar w)$；精度变化通过第③项 $(\kappa_X-\kappa_N)(\ell-\widetilde O)$。即零楔子切换者用于识别**比率再估值**，而不是笼统的“可信度”。

### R2-10【插混：$UF$ 的后验均值代入与 §M2.8.2 自相矛盾；分项清单与 M1 不一致】

**位置**：§M2.8.4。

**问题**：$UF_i(R)$ 关于 $R$ 是凹函数（M1.12）。“以 $UF_i(B^{R,CD})$ 组合”把后验均值代入非线性函数，正是 §M2.8.2 对 BEV 批评的做法。后验方差会降低期望电驱份额、提高期望油费（§8.5：$UF(E[R])=0.766$，$E[UF(R)]=0.754$）。另外，分项清单列 $(L^{F,CS},L^{E,CD},L^{R,CD})$，而 M1 (M1.13)/(M1.27) 还用到 $L^{F,CD}$。

**修改方案**：改用 $E[UF_i(T^{R,CD})\mid\mathcal I]$（正态或对数正态下有闭式，或用数值积分），并写出相应的方差渠道（方向与 BEV 相同：精度下降降低效用）。分项清单与 M1 统一。

---

## 5. 建议项

- **S1（理性预期下的信息期权价值，建议提升为正式命题）**：鞅性质只说平均信念不变。但 logsum 关于效用是凸的，理性预期下更精确的标签使信念在车型间更分散，动力组的期望包容值 $E[IV_d]$ 上升，组份额二阶上升。本轮模拟：组包容值 $-2.7372\to-2.7162$，组份额相对上升 0.44%，选择加权平均信念 $7.356\to7.305$（§8.5）。这是唯一与理性预期和 Blackwell 都相容的“标签变差、组需求上升”渠道，双向替代都适用。目前只以“logit 凸性”一笔带过，建议在 §M2.6.3 与 §M2.6.4 表中列为独立一行，并写出 $\Delta S_d\approx\frac{\partial S_d}{\partial IV_d}\big(E[IV_d^X]-E[IV_d^N]\big)$。
- **S2**：“已知平均换算下平均信念不变”只在 $\bar w_d$ 取**标签加权**平均时成立。若取简单平均且楔子与标签水平相关，平均 $\Delta B$ 不为 0（模拟 +0.017 L/100km，§8.5）。建议明确 $\bar w_d\equiv\sum L^N_jw_j/\sum L^N_j$，这也与 M2-A 的 $\widehat\zeta$ 一致。
- **S3**：明确写出 $E[b_j]=0$ 假设。平台层面的共同报告偏差 $\bar b$（车主城市构成、驾驶工况、记录口径）会按比例抬高 $\widehat\zeta_{d,c}$ 的水平，跨制度比值 $\widehat\zeta_X/\widehat\zeta_N$ 则稳健。建议用加油卡类数据校正，或报告敏感性。
- **S4**：用户的问题“上浮多少需求才不会减少”更可能指动力组需求。建议把 (M2.14) 对动力组求和，给出“动力组份额中性的统一楔子”，并给出续航版本（见 R2-2）。
- **S5**：$\kappa=1$ 的边界检验应在 $(\gamma,\varphi^O\ge0)$ 参数化下进行（$\varphi^O=0\iff\kappa=1$）。在 $\kappa=\mathrm{logit}^{-1}(k)$ 参数化下，边界位于无穷远。
- **S6**：标签误差可能与技术相关（启停、CVT、混动对工况的优化），即 $E[\upsilon\mid x]\ne0$。可以允许 $\zeta_{d,c}$ 按细分或技术变化，或把技术放进先验均值。
- **S7**：§M2.3.1“自身驾驶风格对所有车型共同，在车型比较中抵消”只在可加时成立（§M2.9(ii) 已写明）。比例型驾驶风格 $\theta_i$ 会像里程一样缩放成本差，应并入 $K_i$。
- **S8（排版与记号）**：
  - $\hat\tau^{R2}_c$ 改为 $(\hat\tau^R_c)^2$，避免与路径标签 R2 冲突；
  - §M2.6.4 表与 §M2.8.3 的“理性换算”改为“已知平均换算”；
  - 行内数学的 `*` 改为 `\ast` 或 `\star`（CLAUDE.md §3）；
  - §M2.4 中“3.”“4.”前加空行，使其恢复为列表；
  - 来源账本补列 (M2.2)，统一 (M2.1) 的 [D]/[P] 标注；
  - 按 CLAUDE.md 要求逐个展示式标注来源。
- **S9**：检验切换后评论率是否随 $w_j$ 变化，用于检测选择性发帖。
- **S10**：M2-A 中的 $\kappa_{d,c}$ 是 $\kappa_{jc}$ 的某种加权平均。由于 $E[\kappa\zeta L]\ne\bar\kappa\zeta E[L]$（GHVB 关于均值之比的警示），建议说明加权方式并做异质性稳健性。
- **S11**：插混的 $\varpi$ 是多分项的，(M2.14) 的 $\varpi_{ik}=\alpha_i\gamma K$ 不适用，应写出分项向量形式。
- **S12**：§M2.10.4 引用的残差化方差份额（0.7%/0.01%）与条件数（3.1→21.3）来自第 1 轮审稿模拟。建议把相应代码并入 `tools/m2_examples.py`。本轮用简化设计复现得 0.77%（§8.5），量级一致。

---

## 6. 逐式核验摘要

| 式/命题 | 结论 | 备注 |
|---|---|---|
| (M2.1)(M2.2) | ✓ | 定义与 MSE 分解正确；(M2.2) 未进来源账本 |
| (M2.3) | ✓ | sympy；数值 $\Gamma^X=0.2071$、收敛 30.98%；BEV 带符号差距的前提已补 |
| (M2.4) | ✓ | $D>0$、$D<0$ 两种情形与续航式均正确 |
| (M2.5) | ⚠ | 符号已改正；$\pi^A=\rho^A$ 只在纯队列时成立（R2-5） |
| (M2.6) | ✓/⚠ | 方差分解正确；跨制度差分要求 $\mathrm{Cov}(b+\bar e,\upsilon^X-\upsilon^N)=0$（R2-5） |
| (M2.7)–(M2.9) | ✓ | 后验、$\Omega=\kappa\hat\tau^2=(1-\kappa)v$、两个比较静态、下界 $v_\infty=\sigma_0^2\sigma_b^2/(\sigma_0^2+\sigma_b^2)$ |
| (M2.10) | ✓ | 两种 RS 对应均成立；(a) 是实现值层面的对应（$v_j>0$ 时 $\widetilde O_j=T_j$ 只是巧合） |
| (M2.10a) 命题 M2.0 | ✓ | 迭代期望律；模拟平均 $\Delta B=-0.0003$，$\mathrm{Var}(B)$ 与 $\mathrm{Var}(T)-E\Omega$ 一致 |
| (M2.11)(M2.11a) | ✓/⚠ | 恒等式正确；“与顺序无关”须限定为嵌套层级（R2-8） |
| 命题 M2.1 | ✓ | 比例形式下的表示不变性正确 |
| (M2.12) | ✓ | 近似条件已写明 |
| (M2.13) | ✓ | 与 M1 嵌套 |
| (M2.14)(M2.15) | ✓/⚠ | 线性化与精确结果吻合，符号预测全对；“当且仅当”为一阶；未含续航（R2-2） |
| 命题 M2.2 | ✓/⚠ | R1–R3 与相对可信度齐全；一阶限定 |
| (M2.16)–(M2.18) | ✓ | 闭式、特例与价格项均正确，单位一致 |
| (M2.19)–(M2.21) | ✓ | 闭式与两个导数经符号推导与有限差分验证（对数正态 $D$：$-0.564564$ 对 $-0.564564$，$0.119612$ 对 $0.119612$） |
| (M2.22)(M2.23) | ✓/⚠ | 代数正确；量级可忽略（R2-4） |
| (M2.24)(M2.25) | ✓/⚠ | 映射正确；M2-A 平均恒等式、联合检验与 M2-B 的 rival（R2-1、R2-6） |
| 命题 M2.3 | ✓ | Blackwell 的限定恰当 |

---

## 7. 对上一轮（第 1 轮）意见的逐条核对

| 第 1 轮必须修改项 | 第 2 版处理 | 判定 | 依据与残留 |
|---|---|---|---|
| M1 (M2.5) 锚定解释符号与检验设计 | 改为同硬件样本中 $\ln\bar O^{flow}$ 对 $S\ln(1+w)$ 回归，原假设 $\pi^A=0$；更正“$<-1$”的方向；增加队列检验；改用原始均值 | **已解决**（符号与设计） | 新残留：评论流混合队列使 $\pi^A$ 衰减（R2-5） |
| M2 统一加法/比例原语 | 全文统一为比例信号；(M2.11) 三项分解、R1–R3、$W^\ast$、表示不变基准 (M2.11a) 全部重推；给出 $\mathrm{Var}(L\mid T)=\hat\tau^2/\zeta^2$；说明截距映射 | **已解决** | sympy 逐式核验通过 |
| M3 系统条件、第三条路径、命题 M2.2 | 给出 (M2.14)(M2.15) 与同质 logit 特例；四类渠道；R3 已补；命题改为“充要 + 充分路径”；区分 $K^F/K^E$；新增跨动力流向表 | **已解决** | 残留：“当且仅当”为一阶（R2-8）；系统条件未含续航（R2-2） |
| M4(a) M2-A 校准施加表示不变性；过度识别检验 | 写明“机械地施加了已知平均换算”、R1 不可检验；列出 $\gamma_N=\gamma_X$ 检验 | **部分解决** | 检验被说成检验 A-$\gamma$，实为联合检验；M2-A 机械消除动力平均信念变化这一更强的性质未被认识（R2-1） |
| M4(b) $\widetilde O$、$n_j$ 的外生性/工具 | 工程预测真实能耗作 $\bar K\widetilde O$ 的工具；$n_{j,t-1}$ 先决；更深滞后作稳健性 | **部分解决** | 领先项检验未明写；$n$ 与生命周期、热度的 rival 未处理（R2-6） |
| M4(c) 残差化支持、奇异值与条件数、评论层级 | §M2.10.4 列出剩余变异来源、报告要求，引用第 1 轮模拟数，说明谱系级评论被吸收 | **已解决**（作为报告要求） | 建议把模拟代码并入复现脚本（S12） |
| M4(d) “全部识别”降级；补失效情形 | 改为“函数形式条件下的识别”；失效 (a)–(d) 齐全 | **已解决** | — |
| M4(e) “尖锐识别”降级 | 改为同配置样本与 $Z^W$ 下的条件识别，列出威胁 | **已解决** | — |
| M5 命名（$\hat\beta$、$\kappa$、红利两型、红利 ≠ 福利） | $\zeta-1$ 称感知偏差率，只在 $\zeta=\zeta^0$ 时称理性；引用 Frankel–Kartik；$\kappa$ 称标签精度权重；纠偏/轻信两型与 $CAL$；命题 M2.3 加 $\gamma\ne1$ 限定 | **已解决** | 新残留：“纠偏型改善体验效用”无条件，与命题 M2.3(ii) 和 M7 CF5 矛盾（R2-3）；“理性换算”残留（S8） |
| M6 BEV 期望损失、理性揭示与过度反应、冬季损失归属 | (M2.20)(M2.21) 闭式与均值/方差两渠道；与 CARA 不重复计价；区分理性换算与过度反应；冬季损失归入 $Q_m$ | **已解决**（理论层） | 新残留：未进入可估规格与识别（R2-2） |
| M7 PHEV 与 M1 一致 | 删除复合标签差距，改用分项，$UF_i$ 为类型层面的量 | **已解决** | 新残留：$UF(B)$ 代入违背 Jensen；分项清单缺 $L^{F,CD}$（R2-10） |
| M8 文献（RS 双对应、gaming 归属、记号） | (M2.10) 并列两种对应并说明 (b) 更贴近 RS；gaming 主要进入 $\zeta^0$；记号冲突已改 | **已解决** | 新问题：M2-C(ii) 归属不实（R2-7） |
| M9 符号冲突 | $V/\Omega$、$m/\widetilde O$、$\eta/\upsilon$、弃用 $\beta$、$a\to\varphi^L,\varphi^O$、CARA 改用 $\mathcal R$、$\tau^2$ 与 $\hat\tau^2$ 分开、固定效应改用 $\iota$ | **基本解决** | 残留：$\hat\tau^{R2}$ 与路径 R2 冲突；R 同时用于续航上标、路径标签与 $\mathcal R$（S8） |
| M10 前提条件补全 | (M2.4) 两种情形；续航 $g^{R,N}\ge0$；(M2.3) $\Gamma^{R,N}\ge0$；“$\kappa\uparrow\Rightarrow\Omega\downarrow$”限定为由 $\hat\tau^2$ 驱动；价格项改用边际买者加权的 $\bar K^w_j$ | **已解决** | — |

**第 1 轮建议项的采纳情况**：
- 已采纳：1 零楔子检验（P-M2-3，但见 R2-9 的数据警示）；2 $K$ 梯度（P-M2-4）；5 特征条件先验；6 联合更新（作为稳健性）；7 Shapley；8 $\bar\chi^2$ 边界；9 理论锚点；10 原始均值；11 A-$\gamma$ 作维持假设（但过度识别检验被说过头）；12 跨动力汇总表；13 估计约束；14 CARA 从 $\mathcal V$ 推出；15 目标 $T$ 的情景定义。
- 部分采纳：3 学习动态（P-M2-6 只作预测，未建模）。
- 未采纳：4 $\kappa$ 异质性（仅提到“有效阅读条数”）。

**总体判断**：第 1 轮的 10 项必须修改中，8 项已解决，2 项部分解决（M4(a)(b)）。第 2 版的修订还引入或暴露了 R2-1 至 R2-10 中的新问题，其中 R2-1（M2-A 平均恒等式）与 R2-2（续航识别）最重要。

---

## 8. 验算记录（代码与输出）

环境：Python 3（`python3 -I`），sympy 1.14.0，numpy 2.5.3，scipy 1.18.1；pandoc 3.1.3 + XeLaTeX。脚本位于本会话 scratchpad `m2r2/`：`verify_m2_r2.py`、`verify_m2_r2_b.py`、`verify_m2_r2_c.py`、`verify_m2_r2_d.py`、`report_repro.py`。

### 8.1 作者复现脚本

命令：`python3 -I tools/m2_examples.py`（退出码 0）。输出与正文一致：例 A 的两行 $\kappa$ 表（0.891…0.000；0.891…0.620）；例 B 六种情形的三项之和与直接计算逐位相同（+0.4204、0、+0.0900、−0.0750、−0.0900、−0.5159）；例 C 标签隐含偏差 +1.050→+0.324、0→−0.860；例 D 份额 (0.3084,0.2525,0.1871,0.1386)→(0.3165,0.2038,0.1510,0.1808)，份额加权平均 $\Delta B=0.3563$；例 E $W^\ast=0.4562$，$\widetilde{\Delta B}_{-1}=0.3813$，$W^{\ast\ast}=0.9827$；例 F 20.000/21.666/27.912/35.254；例 G 平均 $\Delta B=-0.0005$、下降占比 0.501、标准差 0.920→0.957，过度怀疑时 −0.3925、0.844。

### 8.2 符号核验（`verify_m2_r2.py` 第 1 部分）

```
M2.3 Gamma_X form: True ; M2.3 relative convergence: True
M2.4 dMSE: True ; M2.4 range dMSE: True
M2.8 Omega = kappa*tau^2: True ; = (1-kappa)v: True ; posterior mean form: True
M2.9 dkappa/dtau2: True ; M2.9 dv/dn: True ; lower bound v_inf: sigma0**2*sigma_b**2/(sigma0**2 + sigma_b**2)
M2.10(a) alpha=1-kappa: True ; M2.10(b) zeta=1+alpha*g/L: True
M2.11 three-term identity: True ; M2.11a: True
3-factor Shapley 'L' term minus nested numeric term: -(LN - LX)*(k_N - k_X)*(z_N - z_X)/12
M2.16: True ; known-average & const kappa -> wbar*LN: True ; M2.18: True
M2.21 dpsi/dx = Phi: True ; dpsi/dsigma = phi: True
M2.23 (corrected test, verify_m2_r2_b.py B1): True ; CARA-normal CE: True
M2.25 1/phiO linear in v: True ; phiL/phiO: True ; M2-A elasticity dln gamma/dln zhat = -kappa: True
```

注：第 1 部分脚本中 (M2.23) 的首次检验写错了符号（属本人测试式错误），已在 `verify_m2_r2_b.py` B1 中改正，结果为 True。(M2.23) 原式正确。

### 8.3 (M2.14) 线性化与精确份额变化（异质 $K_i$、$\alpha_i$，ICE 与 BEV 的 $\gamma_d$ 不同）

```
linear (M2.14): [-0.00026  -0.000395  0.000105 -0.000252  0.000443  0.000358]
exact         : [-0.000258 -0.000386  0.000106 -0.000248  0.000434  0.000351]
sign agreement: True
dB_j < dB~_-j  : [False False  True False  True  True]  vs exact share up: [False False  True False  True  True]
```

### 8.4 本轮新发现的复现（`report_repro.py`，退出码 0）

```python
import itertools, numpy as np, sympy as sp
# [V1] three-term decomposition is exact, but it is a NESTED Shapley; symmetric 3-factor Shapley differs
kN,kX,zN,zX,LN,LX,O=sp.symbols('k_N k_X z_N z_X L_N L_X O')
f=lambda k,z,L: k*z*L+(1-k)*O
dec=(kN+kX)/2*(zN+zX)/2*(LX-LN)+(kN+kX)/2*(zX-zN)*(LN+LX)/2+(kX-kN)*((zN*LN+zX*LX)/2-O)
print("V1 identity:", sp.simplify(f(kX,zX,LX)-f(kN,zN,LN)-dec)==0)
s,e={'k':kN,'z':zN,'L':LN},{'k':kX,'z':zX,'L':LX}; phiL=0
for o in itertools.permutations('kzL'):
    c=dict(s)
    for q in o:
        b=f(c['k'],c['z'],c['L']); c[q]=e[q]
        if q=='L': phiL+=(f(c['k'],c['z'],c['L'])-b)/6
print("V1 Shapley_L - nested term1 =", sp.factor(phiL-(kN+kX)/2*(zN+zX)/2*(LX-LN)))
# [V2] M2-A calibration forces mean dB = dkappa*(mean Obar - mean Otil) ~ 0
r=np.random.default_rng(99); J=300; T=r.normal(8,1,J); n=r.integers(5,400,J)
sO2=.25+2.25/n; v=1/(1+1/sO2); Ob=T+.5*r.standard_normal(J)+1.5/np.sqrt(n)*r.standard_normal(J)
Ot=v*(8+Ob/sO2); w=np.clip(r.normal(.077,.03,J),0,None); L0=(T+.6*r.standard_normal(J))/1.3; L1=(1+w)*L0
z0,z1=Ob.sum()/L0.sum(),Ob.sum()/L1.sum()
for a,b in [(.5,.65),(.3,.9)]:
    dB=b*z1*L1+(1-b)*Ot-a*z0*L0-(1-a)*Ot
    print(f"V2 kappa {a}->{b}: mean dB={dB.mean():+.4f}, identity={(b-a)*(Ob.mean()-Ot.mean()):+.4f}, sd={dB.std():.3f}")
# [V3] M2-A over-identification test gamma_N=gamma_X is joint: naive consumers, constant gamma
g,k0,k1,z,wb=.6,.5,.6,1.3,.077
gN=g*k0*z/z+g*(1-k0); gX=g*k1*z/(z/(1+wb))+g*(1-k1)
print(f"V3 gamma_N={gN:.4f}, gamma_X={gX:.4f}  (=gamma*(1+kappa_X*wbar)={g*(1+k1*wb):.4f})")
# [V4] CARA risk-premium magnitude under CRRA over lifetime wealth (M1.6)
R=2/2e6; K=6950; dOm=0.0839-0.1530
print(f"V4 (R/2)K(-dOmega)={R/2*K*(-dOm):.1e} L/100km; R needed for dB=0.05: {2*.05/(K*-dOm):.1e}/yuan -> rho_c={2*.05/(K*-dOm)*2e6:.0f}")
# [V5] correcting over-skepticism with gamma<1 can lower experienced welfare
Tt=np.array([6.,9.]); Ll=Tt/1.3; xi=np.array([8.,9.2])
def Wexp(gm,zt):
    V=xi-gm*zt*Ll; e=np.r_[1,np.exp(V)]; P=e/e.sum(); return np.log(e.sum())+(P[1:]*((xi-Tt)-V)).sum()
for gm in (1.,.6): print(f"V5 gamma={gm}: W(zeta=1.45)={Wexp(gm,1.45):.4f}  W(zeta=1.30)={Wexp(gm,1.30):.4f}")
# [V6] anchoring regression with mixed purchase cohorts: pi^A = rho^A * share_post
print("V6", [(sp_, .3*sp_) for sp_ in (1.,.6,.3)])
```

输出：

```
V1 identity: True
V1 Shapley_L - nested term1 = -(L_N - L_X)*(k_N - k_X)*(z_N - z_X)/12
V2 kappa 0.5->0.65: mean dB=+0.0009, identity=+0.0009, sd=0.187
V2 kappa 0.3->0.9: mean dB=+0.0036, identity=+0.0036, sd=0.512
V3 gamma_N=0.6000, gamma_X=0.6277  (=gamma*(1+kappa_X*wbar)=0.6277)
V4 (R/2)K(-dOmega)=2.4e-04 L/100km; R needed for dB=0.05: 2.1e-04/yuan -> rho_c=416
V5 gamma=1.0: W(zeta=1.45)=2.2216  W(zeta=1.30)=2.2629
V5 gamma=0.6: W(zeta=1.45)=2.1046  W(zeta=1.30)=2.0424
V6 [(1.0, 0.3), (0.6, 0.18), (0.3, 0.09)]
```

### 8.5 其他数值核验（`verify_m2_r2.py` 第 4、7、9、10 部分；`verify_m2_r2_b.py`）

```
[鞅性质, 40 万车型] E[dB] = -0.0003; Var(B): 0.847 -> 0.917; Var(T)-E[Omega]: 0.847 -> 0.916
[信息期权价值] mean group IV: -2.7372 -> -2.7162; choice-weighted mean belief: 7.3563 -> 7.3048
[组份额, 外部份额较大] const=-1.0: ICE group share 0.7794 -> 0.7828 (rel. +0.44%)
[PHEV Jensen] UF(E[R]) = 0.7657; E[UF(R)] = 0.7543
[zeta^0 估计量] sum(O)/sum(L) = 1.2970; mean(O/L) = 1.3060; true 1.3
[残差化支持] residual variance share of K*L (产品FE+时间FE, 油价sd 10%): 0.7652%
[(M2.21) 有限差分, 对数正态 D] dA/dB -0.564564 vs -Pr(D>T) -0.564564; dA/dsd 0.119612 vs E_D[phi] 0.119612; MC Pr(D>T)=0.565074
[已知平均换算, 楔子与标签相关] mean dB (简单平均 wbar) = +0.0173; (标签加权 wbar) = +0.00000
```

### 8.6 纠偏型福利阈值（`verify_m2_r2_d.py`）

```
gamma=0.6: numerical threshold zeta_N* = [2.682]; closed-form (2-gamma)*z0/gamma = 3.033
gamma=0.8: numerical threshold zeta_N* = [1.856]; closed-form (2-gamma)*z0/gamma = 1.950
gamma=1.0: numerical threshold zeta_N* = [];      closed-form (2-gamma)*z0/gamma = 1.300（纠正恒改善）
```

### 8.7 LaTeX 编译与目检

- `bash tools/build_pdf.sh deliverables/M2_机制一_认证可信度.md <scratchpad>/review_M2_r2.pdf`：成功，19 页。
- `bash tools/check_overfull.sh`：3 处 `Overfull \hbox (0.11597pt too wide)`，均在 §M2.4 例 B 的 7 列表格内，可忽略；无 Missing character，无未定义命令；警告仅为 mathtools/unicode-math 加载顺序与 hyperref 重跑提示。
- `pdftoppm` 目检第 8、12、13、14、15 页：(M2.11) 框式与 underbrace、(M2.16) 框式、(M2.17)(M2.18)、(M2.20)(M2.21)、(M2.22) aligned、M2.10.2 长表格（含 `\dfrac`）都正确渲染。可见缺陷：第 8 页“3. 真表示不变 / 4. 精度变化”并入段落正文；(M2.24) 的式号因行宽换行；第 14 页长表格前有较大空白（longtable 分页，仅属美观问题）。
- GitHub 渲染风险：行内数学 `$W^*=0$……$W^*=\bar w_dL^N_j$……$W^*$` 与同段的 `**不存在**` 共存。不识别数学的 CommonMark 解析（pandoc `-f commonmark` 测试）会把 `*` 解析成强调；识别数学时正常。CLAUDE.md §3 要求避免 `*`。

---

**审稿结论**：第 2 版在原语统一、系统条件、命名纪律与 BEV 期望缺口上有实质进步，代数全部正确，未触发致命项。仍需修改的是：基准规格 M2-A 机械地消除动力平均红利、过度识别检验被说成单一假设检验、续航渠道没有识别路径、纠偏型福利陈述缺次优条件、风险溢价通道量级可忽略、锚定检验衰减，以及一处文献归属不实。按细则打分：82。

SCORE: 82
