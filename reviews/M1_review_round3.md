---
title: "M1 基准 BLP 模型：第三方审稿报告（第 3 轮）"
date: "2026-10-09"
lang: zh-CN
---

# 0 审稿信息

- **审议对象**：`deliverables/M1_基准BLP模型.md`（第 3 版，745 行；(M1.1)–(M1.47)，另含 (M1.7a)(M1.7b)(M1.20a)(M1.24a)(M1.34a)(M1.39a)(M1.42a)–(M1.42c)）。
- **审稿人**：blp_referee（独立第三方，全新上下文）。流程：先独立逐式审查、验算并给分，**分数在 2026-10-09 03:34:55 UTC 锁定为 87**（锁定记录在审稿人 scratchpad），之后才读第 2 轮报告做逐条核对。没有读作者自评或目标分。评分只依据当前稿件，未参考上一轮分数。
- **结论**：**小到中等修改（minor–major revision）**，**无致命项**。核心计算部分（相对效用份额变化、Berry 反演、价格进入 $\mu$ 时的 $\xi$、IV/GMM 浓缩、税楔子下 $\Delta$ 的方向）全部经符号与数值验证正确；第 2 轮的 12 个必须修改项中 10 项已解决，2 项部分解决。剩余问题集中在四处：（1）§M1.11 把一个联合检验写成了“跳变外生”的检验，主报告比值 $\varphi_{d,X}/\varphi_{d,N}$ 由哪组矩识别没有讲清楚；（2）外部选项缺少按置换/首购区分的结构，例 C 的符号结论依赖两条没有写出的设定；（3）理性预期锚点只是近似；（4）价格变量（指导价还是成交价）没有交代。另有记号与来源标注的小问题。
- **总分：87 / 100**。

## 0.1 实际显式加载（Read）的文件

1. 评分细则：`.claude/agents/blp-referee.md`（八维度与致命项规则）。
2. 技能：`blp-model-building/SKILL.md`、`references/构造与组合协议.md`、`references/模块集成图.md`、`references/technical/blp1995_verified_equations.md`、`micro_foundations.md`、`supply_welfare_counterfactual.md`、`project_china_driving_cycle.md`；`blp-project-professor/SKILL.md`、`references/five-paper-kernel.md`、`constructive-model-design.md`、`model-formula-ledger.md`；`structural-model-building/SKILL.md`、`references/identification_and_claim_ladder.md`、`mechanism_construction_and_theory.md`；`economics-expert-reviewer/SKILL.md`、`references/review-standard.md`；`top-journal-hypothesis-packaging/SKILL.md`。
3. 文献卡核对（`BLP_KB/literature_memory/BLP_结构模型原文/`）：A05 GRV2018（式 (1)–(5)，$\gamma\rho$ 与里程尺度不可分，$\gamma=0.91$，在线附录 A.3，车型内发动机变异，Chamberlain 最优工具）；A09 BKL2024（$\alpha_i=\exp(\alpha_1+\alpha_2\log y+\sigma_p\nu)$，$\alpha_2=-1.21\,(0.12)$，价格全在 $\mu$，容量只经续航，$\log(\text{range})$，PHEV 50 km 门槛）；A14 GHVB2021（0.16–0.39，均值之比高估，$\Delta WTP$ 换算为卡片派生式）；A15 RS2021（$\tilde x=x-(1-\alpha)g$）；A20 Ji 等 2026（一半家庭、季度 /8，税楔子两式，9 个微观矩，$\ln p$，弹性 −3.85/−2.46/−2.88，福利中“开 5 年旧燃油车”，spec 3 变号）；A23 Barwick 等 2026（上海车联网使用侧动态模型，续航与充电互为替代）。Li（2026）的 $\Sigma_\alpha$ 依据项目记忆 `project_china_driving_cycle.md` 第 10 节与 claim ladder 第 9 节。
4. 制度时点：`BLP_KB/dependencies_v6/project/national_model_sales_identification_memory.md`（GB/T 19233—2020、GB 19578—2021、GB/T 18386.1—2021、GB/T 19753—2021、装备中心〔2021〕132/197/290 号、TC11-2021-01、GB 22757.1/.2—2023 与 2024-07-22 联合通知）；`dependencies_v6/project/BLP研究框架与完整推导.md` 与 `technical/blp-model-building/references/current-project-adapter.md`（工信厅联通装〔2024〕43 号把启用日期定义为备案日期）。
5. 用户原始要求：`MEMORY/00_断点记忆_CHECKPOINT.md` A 节（A1–A5 逐字）。按“市场—年月—车型聚合数据（非家庭调查）”与“政策 = NEDC→WLTC（纯电为中国工况）”判断数据适配。

## 0.2 实际运行（全部 `python3 -I`）

`tools/m1_examples.py`（输出与附录逐格一致）；本轮自写 7 个验算脚本（第 8 节）；`tools/build_pdf.sh`（成功，24 页）；`tools/check_overfull.sh`（只有 3 处 0.116pt 表格对齐溢出）；`pdftoppm` 目检第 12–14、19–22 页；源文件的 GitHub 写法扫描。

---

# 1 总体评价

**长处。** 第 3 版是一份完成度很高、纪律很严的基准模型推导。

- 经济学链条完整：跨期预算 → Fisher 分离（写明了服务流与消费可分）→ 准线性一阶近似 → EV1 尺度归一化 → 由 CRRA 推出 $a_y=-\rho_{\mathrm{RRA}}$。
- 生命周期能源成本 $K$ 从里程、衰减、存活、贴现与油价鞅逐项构造，量纲与数字全对。二手车市场的两种口径（持有至报废 / 完善转售加分段 $K$）明确分开，不再混用。
- PHEV 的 $UF$ 与 BEV 的续航缺口 $A(R)$ 都从出行距离分布推出，导数与曲率正确。
- 比例信念有了微观基础和“认证信息偏差收敛 / 信念校准改善”的可操作区分。
- 政策进入方式清楚：工况切换是标签状态的跳变，楔子只承担三种用途。(M1.34a) 的相对效用规则配有情景表与可复现数值例。
- 识别表五栏齐全，补上了 BEV 能源成本估值率，$\varphi^0$ 改为外部固定。三组矩、A-FE 维持假设与同一简约算子的验证都写进去了。
- 供给侧的税账户与 $\Delta$ 方向正确，并用例 D 演示了“税因子不同则方向不可互换”。
- 2024 年标签格式改革作为第二时钟编码，PHEV 按实际展示字段构造信息集，来源标注总体诚实（[外]、“附录本地未读”、“经 GRV 卡转引”）。

**主要剩余问题（按后果排序）。**

1. **识别逻辑（MF1）**：§M1.11 说 (M1.42b) 与 (M1.42c) 之间的过度识别检验“就是跳变是否外生的检验”。但同一稿件的 §M1.11.1 已经推出：只要信念不是标签的比例函数，或 $K$ 构造有误，油价识别的 $\varphi^K$ 与跳变识别的 $\varphi^L$ 就不相等。所以这是**联合检验**。主报告对象 $\varphi_{d,X}/\varphi_{d,N}$ 的识别来源也不确定：表中写“同硬件跳变”，而 (M1.42a) 用油价识别 $\varphi_{d,N}$。若混用两种来源，在 M2 型信念下会把“天真”误读为“强烈再估值”。验算：在展示时点完全外生的双信源模拟中，油价识别的 $\varphi_X=0.944$，跳变识别为 $0.559$；混合比值 $0.565$，油价比值 $0.954$，而真值是标签部分天真（跳变比值为 1）。
2. **外部选项结构（MF2）**：(M1.7a) 归一化后，$\tilde\Phi_{i0}$ 因置换（$o_i=1$）与首购（$o_i=0$）而不同，但 (M1.28) 的内部效用不随 $o_i$ 变，等于隐含限制“留旧车与无车的服务流相同”。里程只经能源成本进入，首购者仍有“高里程者更不买车”的问题。例 C 的“纳入后 $\operatorname{corr}=-0.10$”依赖两条没有写出的设定：全部消费者都是置换者，旧车年金因子等于新车的 6（与正文 $\bar A_0<\bar A$ 矛盾）。改成 50% 置换者，相关为 $+0.095$；令 $\Lambda_0=4$，即使全部是置换者也为 $+0.106$。
3. **理性预期锚点（MF3）**：新工况下 $L^X=L^N(1+w_j)$。楔子跨车型离散时，$T/L^X$ 与 $L^X$ 不再均值独立，RE 信念对标签的弹性为 $b_d=s^2_L/(s^2_L+s^2_w)<1$。所以“(b) 正是比例信念类中的理性预期基准”只是一阶近似。ICE 楔子离散下误差约 5%；PHEV 型离散下弹性只有 0.5，比例类根本装不下 RE 信念。
4. **价格变量（MF4）**：没有交代 $p$ 是指导价还是成交价。中国终端优惠大且随需求冲击变化，这影响 $\alpha$、加价与“再定价”通道。
5. 记号仍有一符多义（$\omega$ 四义、$\nu$ 两义、$w$ 两义、$S$ 两义），与文首“避免一符多义”的声明不符（MF5）；若干来源与制度事实标注（MF6）；三处措辞越级（MF7）。

这些问题都可以在一轮内修好，不需要重做模型。MF1–MF3 是理论与识别层面的实质修改，修好后基准模型可以达到 90 分以上。

---

# 2 八维度得分

| 维度 | 满分 | 得分 | 扣分理由 |
|---|---:|---:|---|
| 经济学基础与原语（偏好、预算、时序、信息集） | 15 | **13** | 推导链完整，二手车两口径分开，时钟与信息集完整。扣分：外部选项缺置换/首购专属项与里程相关的拥车价值，首购者的里程分选在经济上说不通（MF2，−1）；RE 锚点只是近似，新工况下 RE 信念不是比例函数（MF3，−0.5）；月度静态模型的跨期替代（提前购买、推迟购买）只靠甜甜圈处理，没有写成竞争解释（−0.5） |
| 数学推导正确（逐步可验证、符号/单位/方向） | 20 | **18** | 约 30 个式子经 sympy 与数值验证无误（第 8 节）。扣分：“(b) 正是 RE 基准”写成恒等，实为近似（−0.5）；(M1.7b) 把货币转售价与效用相减，单位与“均值为零”只近似成立（−0.5）；例 C 的参数（$o_i\equiv1$、$\Lambda_0=\Lambda$）与正文不一致却用来支持实质论断（−0.5）；准差分残差在 §M1.6.4 为 $\xi-\rho\xi_{-1}$、在 (M1.42) 为 $\Delta\xi-\rho\Delta\xi_{-1}$，前后不一（−0.5） |
| BLP/结构模型一致性（份额、反演、IV/GMM、正规化、outside） | 15 | **13.5** | $\delta/\mu/\xi$ 分解、$V_{i0}\ne0$ 下的收缩映射、价格进入 $\mu$ 时 $\xi=\delta-x\beta$、标签是包含的外生变量、浓缩、AR(1) 准差分、$\Delta$ 方向与税因子、水平形式的 $mc^{eff}$ 都正确。扣分：(M1.7a) 与 (M1.28) 之间丢掉了 $\tilde\Phi_{i0}$ 对 $o_i$ 的依赖（MF2，−1）；配置标签线性加权后进入非线性效用，属于 mean-index 近似，只当作测量误差处理（−0.5） |
| 新参数的经济学构造与含义 | 10 | **9** | $\alpha_i,K,\zeta,\varphi$（用边际替代率定义）、$\eta,\chi,\varkappa,UF,A,\theta_k,\psi_{i,d},\varphi^0,\vartheta$ 都有定义、单位与符号。扣分：$b^W_d$ 的“残值”解释与 $K$ 结构冲突（MF7）；“信念校准指数”在 M1 中只有跨工况比值可识别、水平不可识别，未说明（−1，合计） |
| 识别论证（变异、排除、秩、rival、falsifier） | 15 | **12** | 登记表、固定效应吸收表、A-FE、$\varphi^0$ 与 $\zeta^R_{\mathrm B,N}$ 的诚实处理、(M1.35) 的秩条件、(M1.44) 的功效条件都很好。扣分：过度识别检验被解释成单一的“跳变外生”检验，主比值的识别来源不定，混用会误读（MF1，−2）；P3 的“说明”在 $K$ 可能误设时越级（MF7，−0.5）；替代去向（P4）依赖外部选项结构（MF2，−0.5） |
| 文献一致性与来源标注（不冒称原式） | 10 | **8.5** | BLP [O] 各式与核验底座一致；GRV、GHVB、RS、BKL、Ji 等、Barwick 等、Li（2026）的数字与卡片逐一相符；[外] 与“附录本地未读”使用得当。扣分：Li（2018）本地无卡却标 [O·卡]；30 万元补贴上限（含换电例外）无来源；TC11-2021-01 只挂在混动下，实际也管 BEV；GHVB 的 $\Delta WTP$ 式在卡片中是派生式 [D]，却列在 [O·卡] 下；§M1.7.4 标题标 [O]，而展示式是推广（MF6，合计 −1.5） |
| 回应用户问题与数据适配（市场—月—车型） | 10 | **9** | 用户的五个子问题逐一回答（政策进入效用的位置、$n$ 期外推作差、单列边际效应、口碑整体与分项、电池容量与能量密度），两方向替代、市场—月—车型数据都处理了。扣分：价格变量未交代（MF4，−0.5）；情景表 PHEV“降幅最大”没有推导支持（MF7，−0.5） |
| LaTeX 规范与可读性 | 5 | **4** | 编译无错、无缺字，只有 3 处 0.116pt 表格溢出；没有 `\{`、`*`、表内裸 `\|`；`$$` 块前后有空行；PDF 目检正常。扣分：一符多义仍多（MF5，−1） |
| **合计** | **100** | **87** | 无致命项，无上限约束 |

---

# 3 致命项

**无。** 逐条对照细则：

- **导数方向或符号错误导致结论反转**：未发现。(M1.22)(M1.24)(M1.24a)(M1.12)(M1.33)(M1.34)(M1.34a)(M1.36)–(M1.39a)(M1.45)–(M1.47) 全部经符号或数值验证。
- **把校准/假设说成已识别**：未发现。$\varphi^0$ 外部固定，$\zeta^R_{\mathrm B,N}=1$ 写明是识别假设，$\gamma$ 声明不可识别。MF1 是把联合检验说成单一检验，属于检验解释越级，不是把假设冒充识别，所以不判致命，但必须修改。
- **福利公式误用**：M1 不计算福利。
- **份额/反演/FOC 核心式错误**：无。
- **不回应用户核心问题**：否。

---

# 4 逐式核验清单

| 式号 | 结论 | 说明（验算编号见第 8 节） |
|---|---|---|
| (M1.1) | 通过 | $\bar h=0.5$：月内部份额 0.082；$\bar h=0.07$：0.583（V2） |
| (M1.2)–(M1.3) | 通过 | 写明了可加可分；持有至报废与分段 $K$ 两口径正确 |
| (M1.4)–(M1.6) | 通过 | 一阶展开、尺度归一化、$a_y=-\rho_{\mathrm{RRA}}$；BKL $\alpha_2=-1.21$ 与卡一致 |
| (M1.7)/(M1.7a) | **问题** | 归一化后丢掉 $\tilde\Phi_{i0}$ 对 $o_i$ 的依赖；缺首购者的替代出行成本（MF2，V5–V7） |
| (M1.7b) | 近似 | 货币转售价与效用相减；均值为零只在边际买家 $K$ 等于置换者按 $\alpha$ 加权的均值时成立（S1） |
| (M1.8) | 通过 | 标 [O·卡]，与 §M1.15 一致 |
| (M1.9)–(M1.11) | 通过 | $\Lambda=7.7217$，$K^F=6949.6$，0.539 L/100km → 3746 元；家充/公充 7645/22239 元（V2） |
| (M1.12)–(M1.13) | 通过 | sympy：指数日距离下 $UF'(R)=\tilde h\Pr(D>R)/E[D]$（V1） |
| (M1.14)–(M1.18) | 通过 | MRS $=\varphi$ |
| (M1.16) 微观基础 | **近似** | 新工况下 RE 信念弹性 $b<1$，比例信念只在 $s^2_w/s^2_L\to0$ 时为 RE（MF3，V3、V8） |
| (M1.19)–(M1.20a) | 通过 | $B_{post}/B_{pre}=(1+w)/(1+\bar w)$；$E[1/(1+w)]-1/(1+\bar w)=1.9\times10^{-3}$（ICE 楔子，V2） |
| (M1.21)–(M1.24a) | 通过 | sympy：$A'=-n\Pr(D>R)$，$A''=ng(R)$，$\partial^2u/\partial R\partial\mathcal C<0$（V1） |
| (M1.25)–(M1.26) | 通过 | 例 B 逐数复核（R0） |
| (M1.27)–(M1.30) | 通过；外部选项见 MF2 | — |
| (M1.31)–(M1.32) | 通过 | 混合展示用选择概率加权正确；$S_{jt}$ 同时作指示与比例（MF5） |
| (M1.33)–(M1.34) | 通过 | sympy：两种路径分解、天真与已知平均换算残差为 0（V1） |
| (M1.34a) | 通过 | 例 A 精确值与一阶近似复核（R0） |
| (M1.35) | 通过 | 秩条件 $\operatorname{rank}[KL^X,KW]=2\iff w_j$ 非常数，正确 |
| (M1.36)–(M1.39a) | 通过 | 加总恒等；(M1.39a) sympy 链式项正确（V1） |
| (M1.40)–(M1.43) | 通过 | 收缩映射在 $V_{i0}\ne0$ 下成立；浓缩式标准 |
| (M1.42a)–(M1.42c) 及其后一句 | **问题** | 过度识别是联合检验；主比值的识别来源须固定（MF1，V4） |
| (M1.44) | 通过 | 功效条件与“拒绝不自动支持双信源”都已写明；V4 复现 $\varphi^K>\varphi^L$ |
| (M1.45) | 通过 | sympy：$p$ 的因式分解与 $\vartheta=(1+t^{ct})(1+t^v+t^p)$ 精确，与 Ji 等两式一致（V1） |
| (M1.46)–(M1.47) | 通过 | 例 D：(3.4) 方向还原误差 $8.9\times10^{-16}$，转置方向 0.0113（R0） |

---

# 5 必须修改项

## MF1【过度识别检验是联合检验；主报告比值 $\varphi_{d,X}/\varphi_{d,N}$ 的识别来源必须固定】

**位置**：§M1.11 第 608–618 行（(M1.42a)–(M1.42c) 及“(M1.42a) 识别 $\varphi_{d,N}$；(M1.42b)(M1.42c) 识别 $\varphi_{d,X}$，二者之间的过度识别检验就是‘跳变是否外生’的检验”）；第 624–625 行（表中 $\varphi_{d,X}$ 与 $\varphi_{d,X}/\varphi_{d,N}$ 两行）；§M1.14 P2（第 701 行）；与 §M1.11.1 (M1.44) 的关系。

**问题。**

(a) (M1.42b) 用切换后同一产品内的油价变化识别 $\varphi_{d,X}$，记为 $\varphi^{K}_{d,X}$；(M1.42c) 用预测跳变识别，记为 $\varphi^{L}_{d,X}$。§M1.11.1 自己证明了：双信源信念 $B=\kappa\zeta L+(1-\kappa)\widetilde O$ 下

$$
\varphi^{K}_{d,c}=\gamma_d\Big[\kappa\zeta_{d,c}+(1-\kappa)\,b_{\widetilde O\mid L,c}\Big],\qquad
\varphi^{L}_{d,c}=\gamma_d\,\kappa\,\zeta_{d,c},
$$

其中 $b_{\widetilde O\mid L,c}$ 是固定效应残差上 $\widetilde O_j$ 对 $L^c_j$ 的投影系数。里程反弹、二手车价资本化油价、油价均值回复也会让 $\varphi^K\ne\varphi^L$。因此第 618 行的检验不是“跳变是否外生”，而是

$$
H_0^{J}:\ \Big\lbrace E\big[Z^W_{jt}\nu_{jmt}\big]=0\Big\rbrace\ \cap\ \Big\lbrace \varphi^{K}_{d,X}=\varphi^{L}_{d,X}\Big\rbrace .
$$

拒绝它不能读成“跳变内生”。这条论断来自第 2 轮报告 MF3 的建议措辞，第 3 版照搬了；本轮认为它过强。

(b) 表中主报告对象 $\varphi_{d,X}/\varphi_{d,N}$ 写“同硬件跳变 × 楔子的跨产品差异”，但按 (M1.42a)，$\varphi_{d,N}$ 来自油价。混用得到的是 $\varphi^L_{d,X}/\varphi^K_{d,N}$，它既不是 $\zeta_X/\zeta_N$，也不是 (M1.19)–(M1.20a) 中的任何基准。验算 V4：展示时点完全外生，标签部分天真（$\zeta_X=\zeta_N$），$\gamma=0.9$，$\kappa=0.6$。结果：

| 识别来源 | 估计 |
|---|---|
| 油价，改革前，$\varphi^K_N$ | 0.990 |
| 油价，改革后，$\varphi^K_X$ | 0.944 |
| 跳变，$\varphi^L$ | 0.559（真值 $\gamma\kappa=0.540$） |

混合比值 $0.565$ 会被读成“强烈再估值”（低于已知平均换算基准 $1/(1+\bar w)\approx0.93$）；油价比值 $R^K=0.954$ 看起来像“部分平均换算”；跳变比值 $R^L=1$ 才对应真值。三个比值回答三个不同问题。

**修改。**

1. 第 618 行改为：“(M1.42b) 与 (M1.42c) 之间的过度识别检验是联合检验，原假设为 {展示时点与 $Z^W$ 外生} ∩ {$\varphi^{K}_{d,X}=\varphi^{L}_{d,X}$}；只有在比例信念与 $K$ 构造正确（即 (M1.44) 的 $H_0$）的维持假设下，它才是展示时点外生性的检验。”
2. 定义两个比值并分别报告，不得混用来源：

$$
R^{K}_{d}\equiv\frac{\varphi^{K}_{d,X}}{\varphi^{K}_{d,N}}\quad\text{（(M1.42a)(M1.42b)）},\qquad
R^{L}_{d}\equiv\frac{\varphi^{L}_{d,X}}{\varphi^{L}_{d,N}}\quad\text{（同硬件跳变）} .
$$

   $R^L$ 只靠跳变就能识别：同一产品切换时

$$
\Delta u_{ij}=-\alpha_iK_{imt}\Big[\varphi^{L}_{d,X}W_j+\big(\varphi^{L}_{d,X}-\varphi^{L}_{d,N}\big)L^{N}_j\Big],\qquad
\operatorname{rank}\big[KW,\ KL^{N}\big]=2\iff w_j\ \text{在动力内非常数},
$$

   与 (M1.35)(i) 同一秩条件，须报告缩放条件数。
3. 建议以 $R^L$ 作为“标签再估值”的主报告对象，它直接回应 GHVB 式同硬件重标设计。$R^K$ 作为“油价成本通道”对象。二者之差 $R^K-R^L$ 正是 (M1.44) 型诊断。在表中把 (M1.44) 写成上述联合检验的分解：先检验 $\varphi^K=\varphi^L$（以改革前或不受跳变影响的子样本为主），再解释 J 统计量。
4. P2 相应改写：比较的是 $R^L_d$ 与 1、$1/(1+\bar w_d)$ 的关系（注意 MF3 的近似）。$R^L$ 对 $K$ 的常数乘性误设不变，这一点仍然成立。

## MF2【外部选项：缺置换/首购专属项与里程相关的出行价值；例 C 的符号依赖未声明设定】

**位置**：(M1.7a)（第 135 行）与 (M1.28) 末行（第 374 行）；§M1.2.4“为什么不能省略”（第 138 行）；§M1.9 第 522 行；附录例 C（第 733–740 行）；§M1.14 P4。

**问题。**

(a) **归一化丢项**。(M1.7a) 写 $V_{ij}=\tilde\Phi_{ij}-\tilde\Phi_{i0}-\alpha_i(\cdots)$。置换者的 $\tilde\Phi_{i0}$ 是旧车服务流，首购者的 $\tilde\Phi_{i0}$ 是无车状态，二者不同。(M1.28) 把 $\tilde\Phi_{ij}-\tilde\Phi_{i0}$ 映射成 $\psi_{i,d}+x'\beta_i+\cdots$，这些项都不随 $o_i$ 变，等于隐含假设“留旧车与无车的服务流相同”。

(b) **首购者的里程分选**。$VKT_i$ 只经能源成本进入。对首购者，高里程只提高所有内部选项的成本，而外部选项（无车）不受影响，所以模型仍然推出“高里程者更不买车”。稿件把这一病症只归因于“省略旧车能源成本”，但首购者身上它依然存在。

(c) **例 C 的设定没有写出且与正文矛盾**。脚本 `tools/m1_examples.py` 中：(i) 全部消费者都是置换者（$o_i\equiv1$，附录未写）；(ii) 旧车年金因子取 6，与新车相同，与 §M1.2.4“旧车按剩余 $\bar A_0$ 年计”相矛盾。验算 V5–V6：

| 设定 | $\operatorname{corr}(K_i,P_{i0})$ |
|---|---|
| 全置换，$\Lambda_0=6$（稿件） | $-0.098$ |
| 50% 置换，$\Lambda_0=6$ | $+0.095$ |
| 全置换，$\Lambda_0=4$ | $+0.106$ |
| 全置换，$\Lambda_0=3$ | $+0.181$ |

所以第 138 行“纳入后为 $-0.10$”以及 (M1.7) 作为药方的论证都不稳健。标签转移流向外部选项的份额在这些设定下也在 0.21 到 0.30 之间变化，直接影响 P4 与 M7 的福利。

**修改（从同一预算约束推出，不新增自由口味参数）。**

1. 对首购者，“本月不买新车”意味着要用替代出行方式（公交、网约车、出租车）完成出行，付出货币加时间成本 $c^{alt}_{mt}$（元/km，城市层外部数据）。外部选项写为

$$
u_{i0mt}=\psi^{o}o_i-\alpha_i\Big[o_i\,\varphi^{0}K^{F,0}_{imt}\bar e_{0,m}+(1-o_i)\,\varphi^{alt}\,\underbrace{c^{alt}_{mt}\,VKT_i\,\Lambda(r,\bar A)}_{\text{替代出行的现值成本}}\Big]+\varepsilon_{i0mt},
\qquad \psi^{o}\equiv\frac{\Phi^{keep}_{i0}-\Phi^{none}_{i0}}{\sigma_\varepsilon}.
$$

   $\psi^o$ 是“留旧车相对无车”的服务流差（效用单位）；$\varphi^{alt}$ 基准取 1 或与 $\varphi^0$ 绑定。验算 V7：50% 置换、$c^{alt}=0.6$ 元/km 时，$\operatorname{corr}(K,P_0)$ 由 $+0.095$ 变为 $-0.158$，分选恢复合理。
2. 简约替代：在全部内部选项中加 $\psi^{v}\ln(VKT_i/\overline{VKT})$（拥车服务价值随出行需要上升）。二者只能选一，不能重复计价。
3. **识别**：$\psi^o$ 由跨市场置换比例（千户保有量）的变化，或“新车买家中置换购买占比”的汇总微观矩识别。$c^{alt}$ 外部给定。用买家条件里程分布作微观矩，检验或约束里程分选（同一调查也用于 §M1.3.1 (ii) 的里程映射）：

$$
g^{VKT}(\theta)=\overline{\ln VKT}^{\,\mathrm{buyers,data}}-\frac{\int\ln VKT_i\,\big(1-P_{i0}(\theta)\big)\,dF(i)}{\int\big(1-P_{i0}(\theta)\big)\,dF(i)} .
$$

4. 例 C 改用调查给出的置换比例与 $\Lambda_0<\Lambda$，在附录写明全部参数（含 $o_i$ 与 $\Lambda_0$），并报告转移率对 $(o\text{ 比例},\Lambda_0,c^{alt})$ 的敏感性。第 138 行改为“外部选项的类型结构直接影响买家构成与标签转移”，不再把单一相关系数的符号当结论。

## MF3【理性预期锚点只是近似：新工况下 RE 信念不是标签的比例函数】

**位置**：§M1.4.2“微观基础与理性预期锚点”（第 232 行）；§M1.4.3 (b) 后一段（第 265 行）；§M1.14 P2（第 701 行）。

**问题。** 微观基础要求在每个工况制度内 $E[\eta\mid L,d,c]=1$，即 $T/L$ 与 $L$ 均值独立。改革前若成立，改革后 $L^X=L^N(1+w_j)$；当 $w_j$ 跨车型离散且与 $T/L^N$、$L^N$ 独立时，$T/L^X=(T/L^N)/(1+w_j)$ 与 $L^X$ **不再**均值独立：标签高部分是因为楔子大。设 $\ln L^N\sim N(\cdot,s^2_L)$、$\ln(1+w)\sim N(\cdot,s^2_w)$ 相互独立，则

$$
\frac{\partial E\big[\ln T\mid \ln L^X\big]}{\partial \ln L^X}=b_d\equiv\frac{s^2_{L,d}}{s^2_{L,d}+s^2_{w,d}}<1,\qquad
\frac{\partial E\big[\ln T\mid \ln L^N\big]}{\partial \ln L^N}=1 .
$$

验算 V3、V8：

| 楔子离散 | RE 弹性 $b$ | $E[T/L^X\mid L^X]$ 跨十分位极差/均值 |
|---|---|---|
| ICE 型（$s_L=0.2$，$s_w=0.045$） | 0.952 | 3.5% |
| PHEV 型（$s_w=0.2$） | 0.500 | 55% |

所以“(b) 正是比例信念类中的理性预期基准”只在 $s^2_w/s^2_L\to0$ 时成立。对 PHEV 分项标签（楔子很大且离散），比例类装不下 RE 信念。

**修改。**

1. 第 232、265 行改为“(b) 是比例信念类对 RE 的一阶近似，误差阶为 $s^2_w/s^2_L$”，并按动力报告 $s_w/s_L$（用同配置双测资产）。PHEV 不称 (b) 为 RE 基准。
2. 给出 RE 的锐利预测，并作为扩展规格：对数线性信念

$$
B_{jt}=\zeta_{d,c}\,L_{jt}^{\,b_{d,c}},\qquad b_{d,N}=1,\qquad b^{RE}_{d,X}=\frac{s^2_{L,d}}{s^2_{L,d}+s^2_{w,d}},
$$

   在只看当期标签的 RE 下，横截面上标签差异的计价在改革后按 $b_{d,X}$ 衰减。这是一个可检验的、与“天真”（$b_{d,X}=1$）不同的预测。$b$ 的识别来自改革后横截面标签差异与 $K$ 的交互，与 MF1 的 $R^L$ 分开报告。
3. 顺带说明：在 A-$\gamma$ 下，M1 只能识别信念校准指数的**跨工况比值**

$$
\frac{\zeta_{d,X}/\zeta^{RE}_{d,X}}{\zeta_{d,N}/\zeta^{RE}_{d,N}}=\frac{R_d}{\zeta^{RE}_{d,X}/\zeta^{RE}_{d,N}},
$$

   水平 $\lvert\zeta_{d,c}/\zeta^{RE}_{d,c}-1\rvert$ 需要 $\gamma$，留给 M3。第 232 行定义的“信念校准改善”应注明这一识别边界。

## MF4【价格变量：指导价、成交价与终端优惠】

**位置**：§M1.1.1（第 55 行）、§M1.2.1（第 74 行“成交价”）、§M1.12.1（第 651 行起）、§M1.8.4 的再定价项、§M1.10.3。

**问题。** 稿件把 $p_{jmt}$ 定义为含税补的消费者价，但没有交代数据中的价格是厂商指导价还是终端成交价。中国终端优惠幅度大、随车龄与竞争变化（2023 年价格战尤甚），并且对需求冲击 $\xi$ 有反应：畅销车优惠少，滞销车优惠多。只用指导价时，测量误差与 $\xi$ 相关，会使 $\alpha$、(M1.47) 的加价与 $mc^{eff}$ 以及切换时的“再定价”通道（$-\alpha_i\vartheta_k\Delta p^s_k$）全部偏误。改标时企业可能调整优惠而非指导价。项目记忆也把“一致口径成交价”列为缺口。

**修改。**

1. 写明价格来源与口径。优先使用终端成交价（含优惠）。
2. 若只有指导价，写出 $p^{obs}_{jmt}=p_{jmt}+d_{jmt}$（$d$ 为未观测优惠），说明价格进入 $\mu$ 且 $\alpha_i$ 异质时 $d$ 不能被 $\xi$ 线性吸收。需求侧只解释为对标价的反应。供给块 (M1.46)–(M1.47) 不启用，或用按车龄×细分×月的优惠模型做敏感性。
3. 切换窗口内的“再定价”须用成交价度量。

## MF5【记号仍有一符多义（与文首“避免一符多义”的声明不符）】

| 符号 | 冲突（行号） | 建议 |
|---|---|---|
| $\omega$ | 配置权重 $\omega_{\ell jt}$（59）、口碑分项权重 $\omega_k$（333）、转移率权重 $\omega^L_{ij}$（518）、成本冲击 $\omega_{jt}$（682） | 配置权重 $\varpi_{\ell jt}$，分项权重 $\omega^{Q}_k$，转移率权重 $\varsigma^L_{ij}$，保留 $\omega_{jt}$ 为成本冲击（BLP 惯例） |
| $\nu$ | 口味抽样 $\nu_i,\nu_{ip},\nu_{id}$ 与 GMM 残差 $\nu_{jmt}$（347、584） | 残差改记 $\upsilon_{jmt}$ |
| $w$ | 相对楔子 $w_j$ 与成本移动项 $w_{jt}$（682） | 成本移动项改记 $\mathbf z^{mc}_{jt}$ |
| $S$ | 存活概率 $S_a$（74）与展示状态 $S_{jt}$（411）；$S_{jt}$ 在混合展示月又作“看到新标签的比例” | 展示指示改记 $I^{show}_{jt}$，比例改记 $\varpi^{show}_{jt}$ |
| $H$ | 硬件 $H_j$（426）、首任持有期 $H$（74）、原假设 $H_0$ | 硬件 $\mathcal H_j$，持有期 $H^{own}$ |
| 准差分 | §M1.6.4 为 $\xi-\rho_\xi\xi_{-1}$，(M1.42) 为 $\Delta\xi-\rho_\xi\Delta\xi_{-1}$ | 统一为对固定效应后残差准差分，并说明固定效应随 $\delta,X_1$ 一起准差分 |

改完后同步更新文首记号表（目前缺 $S_a$、$C_j$、$\omega$ 各义）。

## MF6【来源与制度事实标注】

1. 第 57 行“参照 Li（2018）与 Ji 等（2026）……[O·卡]”：本地没有 Li（2018）的卡片，“一半家庭”来自 Ji 等卡片的转述。改为“[O·卡：Ji 等 2026；Li 2018 经 Ji 卡转引]”。
2. 第 489 行与 §M1.12.1 的“2020 年起补贴前售价超过 30 万元（换电除外）不享受补贴”“$\bar P^{sub}=30$ 万元”：A09、A20 卡片中都没有，当前没有来源。补上政策文件（2020 年四部委补贴调整通知，财建〔2020〕86 号）并标为制度事实，或标 [外]。
3. 第 63 行把 TC11-2021-01 只挂在混动与插混下。项目制度记忆写明它同时规定 GB/T 18386.1—2021（BEV）与 GB/T 19753—2021（HEV/PHEV）的 CCC 换版时钟。
4. 第 712 行把 GHVB 的 $\Delta WTP=\Delta P-P_0(\Delta Q/Q)/\eta_D$ 列在 [O·卡] 下。卡片注明该式是派生式（期刊正文未印），项目记忆也称其为带条件的 [D] 局部换算。改标为“[O·卡] 中的派生式 [D]”。
5. 第 395 行 §M1.7.4 标题标 [O]，但 (M1.30) 含 $\exp(V_{i0mt})$，是 BLP (6.6)(6.7)(6.10) 的推广。改为 [O]+[D]。
6. 第 416 行把 $T^{show}_j$ 的数据来源写成“能耗标识备案系统的启用日与作废日”。按工信厅联通装〔2024〕43 号第三（四）款，2024 年起的启用日期就是**备案日期**，不是消费者实际接触日；库存旧标车辆会造成新旧并存月。应写明备案启用日只是 $T^{show}$ 的代理，须用销售展示数据或首次销售月校正，并保留 Dual 月份处理。

## MF7【三处措辞越级（claim ladder）】

1. **§M1.14 P3（第 702 行）**：“$b^W_d$ 显著，说明存在与能源成本无关的标签通道。”$b^W$ 依靠 $K$ 的变异与 $K$ 乘项区分。若 $K$ 误设（例如里程对油价有反弹，有效成本尺度弱于比例），误设会载到 $b^W$ 上。改为“在 $K$ 构造正确的维持假设下，与存在非能源成本的标签通道一致”。
2. **(M1.35)(ii) 后与 P3（第 485、702 行）把“残值”列为不乘 $K$ 的通道**。情形 B 下，转售价资本化后续车主的能源成本，与 $\bar K$（油价 × 后续车主里程）成比例，因此残值通道会载到乘 $K$ 的项上。只有“标签作为认证质量信号影响残值”的部分才不乘 $K$。改写，或删去“残值”。
3. **情景表 (a) 行 PHEV“↓（降幅最大）”（第 465 行）**：在分项标签做法下，PHEV 组的降幅取决于 $(w^{F,CS},w^{E,CD},w^{R,CD})$ 与 $UF_i$，稿件没有给出分项楔子，也没有推导。改为“↓（幅度取决于分项楔子）”。

---

# 6 建议项

- **S1 (M1.7b) 的单位**：把转售价写成货币量 $P^u_{mt}=P^{u,serv}_{mt}-\varphi^0\bar K^{F,0}_{mt}\bar e_{0,m}$，再写

$$
V^{B}_{i0}=\Big(\frac{\Phi_{i0}}{\sigma_\varepsilon}-\alpha_iP^{u,serv}_{mt}\Big)-\alpha_i\,o_i\,\varphi^{0}\big(K^{F,0}_{imt}-\bar K^{F,0}_{mt}\big)\bar e_{0,m}.
$$

  “$(m,t)$ 均值为零”改为“近似为零”（须边际二手买家的 $K$ 等于置换者按 $\alpha_i$ 加权的均值）。
- **S2 $\bar w_d$ 的口径**：写明是销量加权还是简单平均；楔子离散大时用 $E[1/(1+w)]$，不用 $1/(1+\bar w)$。ICE 下差 $1.9\times10^{-3}$，PHEV 下不可忽略。
- **S3 配置到车型的聚合**：若有配置层销量，车型份额应写成配置层选择概率之和，而不是用加权平均标签代入非线性效用（structural-model-building 第 4 步的 mean-index 警示）。否则把 $e^{agg}$ 的方差按 $\partial\delta/\partial L$ 进入推断。
- **S4 跨期替代作为竞争解释**：月度静态模型中，“本月不买”包含推迟购买。2022-06 购置税减半开始、2022-12 提前购买、2023-01 多政策叠加，都会让静态模型把跨期替代读成 $\xi$。建议在 rival 表中单列，并做领先/滞后月份诊断。
- **S5 中国油价的鞅假设**：国内成品油价按发改委约 10 个工作日调价、有上下限，鞅假设借自美欧文献。建议给一个简单检验（$\Delta\pi_{t+h}$ 对 $t$ 期信息回归），或用国际原油期货换算的预期作稳健性。
- **S6 $\varphi=\exp(\tilde\varphi)$**：这一参数化使“标签不被计价”（$\varphi_{d,c}=0$）无法检验。建议用带边界的参数化，并采用边界推断（Andrews 1999 类）。
- **S7 (M1.46)(M1.47) 的市场下标**：消费者价写 $p_{jmt}$，导数写 $\partial s_{kmt}/\partial p_{jmt}$，与全国统一的 $p^s_{jt}$ 区分。
- **S8 情景表 BEV 列**：把正文“须计入 $L^E$ 变化”落实到表格，两种 $(w^R,w^E)$ 符号组合分别给方向。
- **S9 $\eta_i$ 的年金**：$A$ 是年度量，$\eta_i$ 隐含年金因子。建议写 $\eta_i=\tilde\eta_i\Lambda_i$（$\tilde\eta$ 为每年的负效用），便于与 Barwick 等（2026）的终身 WTP 外部校准对接。
- **S10 B0 退化表**：按构造协议，在附录给一张代表类型 $z^\ast$ 处的份额、导数与 (M1.47) 回放表，证明 B0 与 M0 精确嵌套。
- **S11 2024 年格式改革的识别作用**：GB 22757.1/.2—2023 改变了展示格式而不改变工况。若字段不变而格式变，它可作为“纯展示变化”的安慰剂或显著性检验；若字段变，则是新的信息变化。建议在 §M1.8.1 说明两种用法。
- **S12 例 A 的 $c$**：附录写明 $c=\alpha\varphi KL^N=1.26$ 对应的 $(\alpha,\varphi,K,L^N)$ 组合，便于读者复核量级。

---

# 7 对第 2 轮意见的逐条核对

| 第 2 轮条目 | 状态 | 依据（第 3 版位置） |
|---|---|---|
| **MF1** 外部选项与二手车市场假设一致性；$\varphi^0$ 识别；与“γ 不可识别”冲突 | **已解决**（遗留新问题） | §M1.2.1 改为持有至报废基准，并给完善转售的分段 $K^F$；§M1.2.4 情形 A/B 分开，(M1.7b) 为偏离式；“期限不对称”已注明；表中 $\varphi^0$ 行改为“仅类型间异质性，基准外部固定”；§M1.14 加了“$\varphi^0$ 若自由估计会分离 $\gamma_{\mathrm I}$ 与 $\zeta$，本稿不依赖”。新问题：$o_i$ 专属项与首购者结构缺失、例 C 设定（本轮 MF2）；(M1.7b) 单位（S1） |
| **MF2** BEV 能源成本估值率的识别行 | **已解决** | 表中新增 $\varphi_{\mathrm B,N},\varphi_{\mathrm B,X}$ 行（变异、矩、rival、支持、联合秩），并给两条退路与 PHEV 说明 |
| **MF3** 三组矩 | **已按建议修改，但建议措辞本身过强** | (M1.42a)–(M1.42c) 已写入。“二者之间的过度识别检验就是跳变是否外生的检验”是联合检验，主比值识别来源须固定（本轮 MF1，V4） |
| **MF4** A-FE 与组层面外推 | **已解决** | 维持假设 A-FE、情景表标题“结构模型推出，非由共同成分直接识别”、交错队列留出检验与同一简约算子 $R(\cdot)$ 的验证式 |
| **MF5** (M1.35)(i) 的秩条件 | **已解决** | “$\operatorname{rank}[KL^X,KW]=2$ 当且仅当 $w_j$ 在动力内不是常数……须报告缩放条件数，基准中不同时放开” |
| **MF6** (M1.44) 的功效条件 | **已解决** | 加了 $\operatorname{Cov}(\tilde O_j,\tilde L_j)\ne0$ 条件、“不拒绝不能作为比例信念成立的证据”和“拒绝不自动支持双信源” |
| **MF7** 比例信念的微观基础与 RE 锚点 | **已按建议修改，但 RE 锚点只是近似** | 微观基础、$\zeta^{RE}$、信念校准指数、两个命名的区分都已写入。新工况下 RE 信念弹性 $b<1$，“(b) 正是 RE 基准”须改为一阶近似（本轮 MF3，V3、V8） |
| **MF8** 政策时钟与信息集 | **已解决**（小瑕疵） | 六种时钟；GB 22757.1/.2—2023 与 2024-09-01 换标；$(S^{cycle},S^{format})$ 与甜甜圈；$T^{show}$ 数据来源；PHEV 按实际展示字段；BEV 两种符号。小瑕疵：TC11 也管 BEV、启用日即备案日（本轮 MF6-3、MF6-6） |
| **MF9** 供给矩 $\ln mc$ 与 $mc^{eff}$ | **已解决** | 水平形式 $mc^{eff}=w'\gamma^{mc}+\omega$，或把 $\lambda$ 作参数；写明“M1 基准只用需求矩” |
| **MF10** 记号冲突 | **部分解决** | $W_j\to\mathrm{wt}_j$、$\kappa\to\vartheta$、$N\to\mathcal C$、$p^c\to p$、$t^c\to t^{ct}$、$\gamma^c\to\gamma^{mc}$、$\rho_\xi$、$\mathbf d_i$、$\tilde\Phi$ 都改了，并加了记号表。仍有 $\omega,\nu,w,S,H$ 多义（本轮 MF5） |
| **MF11** 渲染 | **已解决** | (M1.35) 与 (M1.45) 用 aligned 分行，本轮溢出检查只剩 0.116pt 表格；“情形 (ii)”不再被解析为列表；`u^{\ast}` |
| **MF12** 来源标注 | **已解决**（出现新的小问题） | (M1.8) 改 [O·卡]，图例区分 [O]/[O·卡]；RS 嵌套措辞改正；GRV A.3“附录本地未读”；AKS“经 GRV 卡转引 [外]”；Li（2026）语境改正；Gandhi–Houde [外] 经 Kaneko–Toyama。新的小问题见本轮 MF6 |
| S1 比值作主报告对象 | **已解决** | 表中注明对 $K$ 乘性误设不变，P2 写明。但比值的识别来源须按本轮 MF1 固定 |
| S2 (M1.34a) 的用途与适用范围 | **已解决** | 第 2 点注明简化式只在同一动力、共同 $\varphi,K$ 时成立，定量预测须精确重解，插混一阶近似不可靠 |
| S3 退化为代表类型 | **已解决** | §M1.13 第 1 条“退化为预定代表类型 $z^\ast$，非线性输入在 $z^\ast$ 处计算” |
| S4 联合类型分布的数据方案 | **已解决** | §M1.7.4“数据来源与降级方案” |
| S5 $\Lambda$ 按动力、$r$ 敏感性 | **已解决** | §M1.3.1 口径说明 (iii) |
| S6 (M1.3) 的可加可分 | **已解决** | (M1.3) 后括注 |
| S7 准差分下的浓缩 | **已解决** | §M1.10.4“对准差分后的 $\delta$ 与 $X_1$ 应用 (M1.43)”。残差记号前后不一（本轮 MF5） |
| S8 $\theta_2$ 维数与简约基准 | **已解决** | §M1.7.3“简约基准：混动并入燃油车、跨动力共用 γ、$a_y$ 固定、$\varphi^0$ 固定” |
| S9 两个相关系数的来源 | **已解决** | 附录末注明 $+0.056$ 来自第 1 轮审稿人设定，统一改用例 C 的 $+0.33$。例 C 本身的设定问题见本轮 MF2 |
| S10 BEV 行补 $L^E$ | **基本解决** | A-FE 段末“纯电行还须计入中国工况下电耗标签 $L^E$ 的变化”；情景表本身仍只按 $w^R$ 分（本轮 S8） |
| 维度表中的零星项：(M1.24a) 的“$\le0$”；$\psi_{i,d}$ 含义；$\Phi$ 未除 $\sigma_\varepsilon$；“市场均值处的 Dirac”；$\ln mc$；(M1.43) 准差分 | **全部已解决** | (M1.24a) 写“$\le0$（$\varkappa>0$ 时严格小于 0）”；§M1.7.2 定义 $\psi_{i,d}$；$\tilde\Phi$；§M1.13；§M1.12.3；§M1.10.4 |

---

# 8 验算记录

环境：Python 3（`python3 -I`），numpy、scipy、sympy 1.14.0。全部为合成检验，不涉及项目数据，**不代表经验识别**（技能红线：公式内部自洽不证明排除限制成立，也不证明已用数据估计过）。

## 8.1 结果汇总

| 编号 | 检验对象 | 结果 |
|---|---|---|
| R0 | `tools/m1_examples.py` | 例 A：$s_0=0.22$ 时 ICE1 $0.1950\to0.2035$（精确 $+0.00854$，一阶 $+0.00898$），BEV $0.1950\to0.2087$，外部 $0.2200\to0.2355$；$s_0=0.58$ 时 $0.1050\to0.1061$。例 B：$(0.952,0.167)$、$0.1679$、$0.0851$。例 C：corr $-0.098/+0.328$，转移→最省油车 $0.1509/0.1065$，→外部 $0.2947/0.2514$。例 D：(3.4) 方向误差 $8.88\times10^{-16}$，转置方向 0.0113。与附录逐格一致 |
| V1 | 符号代数（(M1.12)(M1.22)(M1.24)(M1.24a)(M1.33)(M1.34)(M1.39a)(M1.45)） | 全部精确成立 |
| V2 | 数字（(M1.10)(M1.11)、市场规模、Jensen 差） | $\Lambda=7.7217$，$K^F=6949.6$，3746 元，7645/22239 元；内部份额 0.082/0.163/0.041/0.583；$E[1/(1+w)]-1/(1+\bar w)=1.92\times10^{-3}$ |
| V3 | RE 锚点 | ICE 型楔子下 $E[T/L^X\mid L^X]$ 十分位极差 3.5%，PHEV 型 55%；改革前恒定 → MF3 |
| V4 | 过度识别解释 | 展示时点外生、双信源：$\varphi^K_N=0.990$，$\varphi^K_X=0.944$，$\varphi^L=0.559$（真值 $\gamma\kappa=0.540$）→ MF1 |
| V5 | 例 C 对置换比例与 $\psi^v$ 的敏感性 | 置换比例 1/0.5/0 → corr $-0.098/+0.095/+0.328$ → MF2 |
| V6 | 例 C 对旧车年金因子的敏感性 | $\Lambda_0=6/4/3/2$（全置换）→ corr $-0.098/+0.106/+0.181/+0.241$ → MF2 |
| V7 | 替代出行成本修正 | 50% 置换、$c^{alt}=0.6$ 元/km → corr $-0.158$（$\Lambda_0=6$）、$-0.012$（$\Lambda_0=3$） |
| V8 | RE 弹性公式 | 回归斜率 0.9515/0.7995/0.5003 对公式 0.9518/0.8000/0.5000；改革前斜率 1.000 |
| P1 | PDF 构建与溢出 | `build_pdf.sh` 成功 24 页；xelatex 无错误、无缺字；Overfull 只有 3 处 0.116pt（表格对齐）；目检第 12–14、19–22 页正常 |
| P2 | GitHub 写法 | 无 `\{`、`\}`；数学内无 `*`；表格数学内无裸 `\|`；`$$` 块前有空行 |

## 8.2 代码与输出（逐字）

### V1 sym_checks.py

```python
import sympy as sp
a,K,phX,phN,LN,W,w,wb = sp.symbols('alpha K phi_X phi_N L_N W w wbar', positive=True)
LX = LN + W
du = -a*K*(phX*LX - phN*LN)
dec1 = -a*K*phX*W - a*K*(phX-phN)*LN
dec2 = -a*K*(phN*W + (phX-phN)*LX)
print("M1.33 path1 ok:", sp.simplify(du-dec1)==0, " path2 ok:", sp.simplify(du-dec2)==0)
print("M1.34 naive:", sp.simplify(du.subs(phX, phN) - (-a*K*phN*W))==0)
avg = du.subs({phX: phN/(1+wb), W: w*LN})
print("M1.34 avg:", sp.simplify(avg - (-a*K*phN*LN*(w-wb)/(1+wb)))==0)
D,R,lam,n,eta,C,Cb,kap = sp.symbols('D R lambda n eta C Cbar kappa', positive=True)
A = n*sp.integrate((D-R)*lam*sp.exp(-lam*D),(D,R,sp.oo))
print("A' = -n Pr(D>R):", sp.simplify(sp.diff(A,R) + n*sp.exp(-lam*R))==0)
print("A''= n g(R):", sp.simplify(sp.diff(A,R,2) - n*lam*sp.exp(-lam*R))==0)
u = -eta*(C/Cb)**(-kap)*A
print("du/dR>0:", sp.simplify(sp.diff(u,R)), " d2u/dRdC:", sp.simplify(sp.diff(u,R,C)))
Dd,mu,h = sp.symbols('D_d mu htilde', positive=True)
g = sp.exp(-Dd/mu)/mu
UF = h*(sp.integrate(Dd*g,(Dd,0,R)) + R*sp.integrate(g,(Dd,R,sp.oo)))/mu
print("UF'(R) = h Pr(D>R)/E[D]:", sp.simplify(sp.diff(UF,R) - h*sp.exp(-R/mu)/mu)==0)
KF,KE,LFCD,LFCS,LECD,phi,zR,LR = sp.symbols('K_F K_E L_FCD L_FCS L_ECD phi zeta_R L_R', positive=True)
UFf = sp.Function('UF'); x = sp.Symbol('x')
G = KF*(UFf(zR*LR)*LFCD + (1-UFf(zR*LR))*LFCS) + KE*UFf(zR*LR)*LECD
target = -a*phi*zR*(KF*(LFCD-LFCS)+KE*LECD)*sp.Subs(sp.Derivative(UFf(x),x),x,zR*LR)
print("M1.39a ok:", sp.simplify(sp.diff(-a*phi*G, LR) - target.doit())==0)
ps,tct,tv,tp,sub,F = sp.symbols('p_s t_ct t_v t_p sub F', positive=True)
Pret = ps*(1+tct)*(1+tv); pc = Pret + tp*Pret/(1+tv) - sub + F
print("M1.45 p ok:", sp.simplify(pc - (ps*(1+tct)*(1+tv+tp) - sub + F))==0, "; dp/dps =", sp.factor(sp.diff(pc,ps)))
print("Ji consistent:", sp.simplify(pc - (Pret*(1+tv+tp)/(1+tv) - sub + F))==0)
```

```text
M1.33 path1 ok: True  path2 ok: True
M1.34 naive: True
M1.34 avg: True
A' = -n Pr(D>R): True
A''= n g(R): True
du/dR>0: eta*n*(Cbar/C)**kappa*exp(-R*lambda)  d2u/dRdC: -C**(-kappa - 1)*Cbar**kappa*eta*kappa*n*exp(-R*lambda)
UF'(R) = h Pr(D>R)/E[D]: True
M1.39a ok: True
M1.45 p ok: True ; dp/dps = (t_ct + 1)*(t_p + t_v + 1)
Ji consistent: True
```

### V2–V3 num_checks.py

```python
import numpy as np
r, A = 0.05, 10
Lam = sum(1/(1+r)**a for a in range(1, A+1)); KF = 7.5*12000*Lam/100
print(f"[1] Lambda={Lam:.4f}, K^F={KF:.1f}; 7.0*7.7% -> {KF*7*0.077:.0f} yuan")
for pe in (0.55, 1.6): print(f"    BEV PV at {pe}: {pe*12000*Lam/100*15:.0f} yuan")
for hb in (0.5, 0.25, 1.0, 0.07): print(f"    hbar={hb}: monthly inside share={2e7/12/(hb*4.9e8/12):.3f}")
rng = np.random.default_rng(1)
med, q1, q3 = 0.077, 0.048, 0.114; sd = (q3-q1)/1.349
w = rng.normal(med, sd, 2_000_000)
print(f"[2] E[1/(1+w)]={np.mean(1/(1+w)):.5f}, 1/(1+mean w)={1/(1+w.mean()):.5f}, gap={np.mean(1/(1+w))-1/(1+w.mean()):.2e}")
N = 2_000_000
LN = np.exp(rng.normal(np.log(7.0), 0.20, N)); T = np.exp(rng.normal(np.log(1.25), 0.08, N))*LN
for wsd, wmu in ((sd, med), (0.25, 0.30)):
    LX = LN*(1+rng.normal(wmu, wsd, N)); b = np.quantile(LX, np.linspace(0,1,11)); idx = np.digitize(LX, b[1:-1])
    zz = np.array([np.mean(T[idx==k]/LX[idx==k]) for k in range(10)])
    print(f"[3] wedge sd={wsd:.3f}: E[T/L^X|decile]={np.round(zz,4)} range/mean={(zz.max()-zz.min())/zz.mean():.4f}")
```

```text
[1] Lambda=7.7217, K^F=6949.6 yuan per (L/100km); 7.0*7.7%=0.539 L/100km -> 3746 yuan
    BEV PV at 0.55 yuan/kWh, 15 kWh/100km: 7645 yuan
    BEV PV at 1.6 yuan/kWh, 15 kWh/100km: 22239 yuan
    hbar=0.5: monthly inside share=0.082
    hbar=0.25: monthly inside share=0.163
    hbar=1.0: monthly inside share=0.041
    hbar=0.07: monthly inside share=0.583
[2] ICE wedge sd~0.0489: E[1/(1+w)]=0.93040, 1/(1+mean w)=0.92847, gap=1.92e-03
[3] E[T/L^X | decile of L^X] = [1.18777 1.17946 1.17435 1.1707  1.16828 1.16532 1.16193 1.15842 1.15447
 1.14664]  range/mean = 0.0353
    E[T/L^N | decile of L^N] = [1.25373 1.25398 1.25392 1.25399 1.2542  1.25406 1.25395 1.25378 1.25404
 1.2542 ]
    with wedge sd=0.25: E[T/L^X|decile] = [1.35686 1.14879 1.07707 1.02877 0.99073 0.95782 0.92735 0.89554 0.86121
 0.80544]  range/mean = 0.549
```

（上面 V2–V3 代码是运行脚本的精简版，输出为原脚本逐字输出。）

### V4 overid_sim.py（过度识别的解释）

```python
import numpy as np
rng = np.random.default_rng(7)
J, Tm = 400, 48; alpha, gamma, kappa = 1.0, 0.9, 0.6
LN = np.exp(rng.normal(np.log(7.0), 0.2, J)); w = rng.normal(0.077, 0.049, J); LX = LN*(1+w)
Ttrue = 1.25*LN*np.exp(rng.normal(0, 0.08, J)); O = Ttrue*np.exp(rng.normal(0, 0.05, J))
Tsw = rng.integers(12, 36, J)                                   # EXOGENOUS switch months
Kt = 1.0 + 0.25*np.sin(np.arange(Tm)/5.0) + 0.05*rng.normal(size=Tm); Kbar = Kt.mean()
rows = []
for j in range(J):
    for t in range(Tm):
        post = t >= Tsw[j]; L = LX[j] if post else LN[j]
        B = kappa*L + (1-kappa)*O[j]                            # two-source belief, label part naive
        rows.append((j, t, post, L, -alpha*gamma*Kt[t]*B + rng.normal(0, 0.02)))
j_, t_, post_, L_, y_ = map(np.array, zip(*rows))
def twfe(v, g1, g2, it=50):
    v = v.astype(float).copy()
    for _ in range(it):
        v -= np.bincount(g1, v)[g1]/np.bincount(g1)[g1]; v -= np.bincount(g2, v)[g2]/np.bincount(g2)[g2]
    return v
Y = twfe(y_, j_, t_)
X = np.column_stack([twfe((Kt[t_]-Kbar)*L_, j_, t_), twfe(Kbar*L_, j_, t_)])
b = np.linalg.lstsq(X, Y, rcond=None)[0]
print(f"(M1.44) estimates: phi^K={-b[0]/alpha:.4f}, phi^L={-b[1]/alpha:.4f}; gamma*kappa={gamma*kappa:.4f}")
for name, m in (("pre (M1.42a-type)", ~post_.astype(bool)), ("post (M1.42b-type)", post_.astype(bool))):
    _, ji = np.unique(j_[m], return_inverse=True); _, ti = np.unique(t_[m], return_inverse=True)
    Ym = twfe(y_[m], ji, ti); Xm = twfe(Kt[t_[m]]*L_[m], ji, ti)
    print(f"phi from {name} oil variation = {-(Xm@Ym)/(Xm@Xm)/alpha:.4f}")
print(f"phi_X from label jump (M1.42c-type, = phi^L) = {-b[1]/alpha:.4f}")
```

```text
(M1.44) estimates: phi^K=0.9626, phi^L=0.5591; gamma*kappa=0.5400
phi_N from pre-period oil variation (M1.42a-type) = 0.9899
phi_X from post-period oil variation (M1.42b-type) = 0.9441
phi_X from label jump (M1.42c-type, = phi^L)       = 0.5591
ratio oil-based phi_X/phi_N = 0.9537  (truth: naive => 1)
```

解读：展示时点外生（抽样与需求冲击独立），(M1.42b) 型与 (M1.42c) 型估计仍然相差 0.944 对 0.559，J 检验会拒绝，但原因是信念结构而非跳变内生。$\varphi^L_X/\varphi^K_N=0.565$，$R^K=0.954$；标签部分真值天真，$R^L=1$。

### V5 exC_sens.py（置换比例与里程相关拥车价值）

```python
import numpy as np
rng = np.random.default_rng(20261008); N = 400000
VKT = np.exp(rng.normal(np.log(12000), 0.5, N)); alpha = np.exp(rng.normal(np.log(0.10), 0.3, N))
L = np.array([5.0, 6.5, 8.0]); p = np.array([140.0, 120.0, 100.0]); xi = np.ones(3)
Ki = 7.5*VKT*6.0/100/1000; phi = 0.8; e0 = 8.5
def run(o_share, psi_v=0.0, include=True, target=0.5):
    o = (rng.random(N) < o_share).astype(float) if o_share < 1 else np.ones(N)
    def probs(shift):
        V = xi[None,:] + shift + psi_v*np.log(VKT/12000)[:,None] - alpha[:,None]*(p[None,:] + phi*Ki[:,None]*L[None,:])
        V0 = -alpha*o*phi*Ki*e0 if include else np.zeros(N)
        mx = np.maximum(V.max(1), V0); eV = np.exp(V-mx[:,None]); e0v = np.exp(V0-mx); D = e0v+eV.sum(1)
        return eV/D[:,None], e0v/D
    lo, hi = -50.0, 80.0
    for _ in range(70):
        mid = 0.5*(lo+hi); _, P0 = probs(mid); lo, hi = (mid, hi) if P0.mean() > target else (lo, mid)
    P, P0 = probs(0.5*(lo+hi)); j = 1; wt = alpha*phi*Ki; den = (wt*P[:,j]*(1-P[:,j])).mean()
    return np.corrcoef(Ki, P0)[0,1], (wt*P[:,j]*P[:,0]).mean()/den, (wt*P[:,j]*P0).mean()/den
```

```text
o_share  psi_v  outside_cost  corr(K,P0)  DR_L->eff  DR_L->out
  1.00   0.00  included      -0.098     0.151      0.295
  1.00   1.00  included      -0.229     0.166      0.266
  0.50   0.00  included      +0.095     0.143      0.225
  0.50   1.00  included      +0.012     0.151      0.210
  0.00   0.00  included      +0.328     0.106      0.251
  0.00   1.00  included      +0.250     0.114      0.249
  --     0.00  omitted       +0.328     0.106      0.251
```

### V6 exC_horizon.py（旧车剩余年金因子）

```python
# 同 V5 的消费者与产品；外部选项改为 V0 = -alpha*o*phi*K0*e0，K0 = 7.5*VKT*Lam0/100/1000
for Lam0 in (6.0, 4.0, 3.0, 2.0):
    print(f"annuity factor old car Lambda0={Lam0}: corr(K,P0) all replacers = {run(Lam0):+.3f}; 50% replacers = {run(Lam0, 0.5):+.3f}")
```

```text
annuity factor old car Lambda0=6.0: corr(K,P0) all replacers = -0.098; 50% replacers = +0.095
annuity factor old car Lambda0=4.0: corr(K,P0) all replacers = +0.106; 50% replacers = +0.200
annuity factor old car Lambda0=3.0: corr(K,P0) all replacers = +0.181; 50% replacers = +0.244
annuity factor old car Lambda0=2.0: corr(K,P0) all replacers = +0.241; 50% replacers = +0.280
```

### V7 exC_fix.py（首购者替代出行成本修正，MF2 的建议式）

```python
# 50% 置换者；V0 = -alpha*(o*phi*K0*e0 + (1-o)*Kalt)，Kalt = c_alt*VKT*6/1000（千元）
for Lam0 in (6.0, 3.0):
    for c_alt in (0.0, 0.3, 0.6):
        c, de, do = run(Lam0, c_alt)
        print(f"Lambda0={Lam0}, c_alt={c_alt} yuan/km: corr(K,P0)={c:+.3f}, DR_L->most efficient={de:.3f}, DR_L->outside={do:.3f}")
```

```text
Lambda0=6.0, c_alt=0.0 yuan/km: corr(K,P0)=+0.095, DR_L->most efficient=0.143, DR_L->outside=0.225
Lambda0=6.0, c_alt=0.3 yuan/km: corr(K,P0)=+0.023, DR_L->most efficient=0.140, DR_L->outside=0.278
Lambda0=6.0, c_alt=0.6 yuan/km: corr(K,P0)=-0.158, DR_L->most efficient=0.160, DR_L->outside=0.286
Lambda0=3.0, c_alt=0.0 yuan/km: corr(K,P0)=+0.244, DR_L->most efficient=0.116, DR_L->outside=0.258
Lambda0=3.0, c_alt=0.3 yuan/km: corr(K,P0)=+0.162, DR_L->most efficient=0.120, DR_L->outside=0.285
Lambda0=3.0, c_alt=0.6 yuan/km: corr(K,P0)=-0.012, DR_L->most efficient=0.150, DR_L->outside=0.249
```

### V8 re_elasticity.py（RE 信念弹性公式）

```python
import numpy as np
rng = np.random.default_rng(3); N = 2_000_000
for sL, sw in [(0.20, 0.045), (0.20, 0.10), (0.20, 0.20)]:
    lnLN = rng.normal(np.log(7.0), sL, N); lnr = rng.normal(np.log(1.25), 0.08, N); lnw = rng.normal(np.log(1.077), sw, N)
    lnT = lnr + lnLN; lnLX = lnLN + lnw
    print(sL, sw, np.cov(lnT, lnLX)[0,1]/np.var(lnLX), sL**2/(sL**2+sw**2), np.cov(lnT, lnLN)[0,1]/np.var(lnLN))
```

```text
s_L=0.2, s_w=0.045: OLS slope of ln T on ln L^X = 0.9515; formula s_L^2/(s_L^2+s_w^2) = 0.9518; pre-reform slope (on ln L^N) = 0.9998
s_L=0.2, s_w=0.1: OLS slope of ln T on ln L^X = 0.7995; formula s_L^2/(s_L^2+s_w^2) = 0.8000; pre-reform slope (on ln L^N) = 0.9998
s_L=0.2, s_w=0.2: OLS slope of ln T on ln L^X = 0.5003; formula s_L^2/(s_L^2+s_w^2) = 0.5000; pre-reform slope (on ln L^N) = 1.0003
```

### R0 tools/m1_examples.py 输出（逐字）

```text
[A] s0=0.2200: du_ICE1=-0.0252, mean P*du=-0.0713; s_ICE1 0.1950 -> 0.2035 (exact d=+0.00854, first-order +0.00898); BEV 0.1950->0.2087; outside 0.2200->0.2355
[A] s0=0.5800: du_ICE1=-0.0252, mean P*du=-0.0384; s_ICE1 0.1050 -> 0.1061 (exact d=+0.00115, first-order +0.00138); BEV 0.1050->0.1089; outside 0.5800->0.6013
[B] shrink weights per subscore=[0.952381 0.166667], sum omega*Q_k=0.1679; overall-score posterior=0.0851 (lam_all=0.2837)
[C] outside cost included=True: mean s0=0.500; label diversion to most efficient (k=0) 0.1509 vs price diversion 0.1096; to outside label 0.2947 vs price 0.2955; corr(K,P0)=-0.098; check sum label=1.000000
[C] outside cost included=False: mean s0=0.500; label diversion to most efficient (k=0) 0.1065 vs price diversion 0.0885; to outside label 0.2514 vs price 0.2181; corr(K,P0)=+0.328; check sum label=1.000000
== D. supply side: Delta-matrix orientation with product-specific tax factors ==
equilibrium producer prices: [7.6551 8.8926 8.1377 9.3455]
mc recovered, BLP (3.4) orientation: [6.  7.  6.5 7.5]  max error 8.88e-16
mc recovered, transposed orientation: [6.006667 6.988687 6.503254 7.493636]  max error 0.0113
```

### P1 渲染

```text
built .../scratchpad/review_M1_r3.pdf   (Pages: 24, A4)
Overfull \hbox (0.11597pt too wide) in alignment ... (x3, 表格对齐)
LaTeX errors / missing characters: 0
```

---

# 9 对用户问题的回应核对

| 用户问题（A2 要点） | 稿件回答 | 评价 |
|---|---|---|
| 政策如何加入 BLP、放在效用哪部分 | 经 $\varphi_{d,c}KL$ 进入广义价格；BEV 续航便利项；机械通道进 $p$ 与 $mc^{eff}$ | 清楚、正确 |
| 前 $n$ 期外推后作差以何种形式进入 | 楔子定义跳变、构造无改革反事实标签与预定工具；效用中是展示标签 | 正确；外推验证跨度 ≤1 年已注明 |
| 燃油经济性/续航单列、算边际效应 | (M1.36)–(M1.39a)，含 PHEV 链式项、WTP、标签转移率 | 正确；转移率受外部选项结构影响（MF2） |
| 口碑整体 vs 分项 | 收缩后验；整体分是受限特例，可检验；能耗分项不进口味项 | 有经济学基础，动态内生性已处理 |
| 标签上调后需求升/降的解释 | (M1.34a) 相对效用、情景表；再估值须在完整系统中估 | 正确；主比值的识别来源须固定（MF1）；RE 基准为近似（MF3） |
| 新能源与燃油车双向替代、电池 | 情景表给两方向条件；容量经续航、密度经质量—电耗—续航与补贴 | 方向正确；PHEV“降幅最大”无推导支持（MF7） |
| 数据为市场—年月—车型 | 产品 = 车型、配置聚合、上险量、市场规模与外部份额、时钟 | 适配良好；价格口径须交代（MF4） |

SCORE: 87
