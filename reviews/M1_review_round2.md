---
title: "M1 基准 BLP 模型：第三方审稿报告（第 2 轮）"
date: "2026-10-08"
lang: zh-CN
---

# 0 审稿信息

- **审议对象**：`deliverables/M1_基准BLP模型.md`（第 2 版，“按第 1 轮第三方审议全面修订”，(M1.1)–(M1.47)，含 (M1.7a)(M1.20a)(M1.24a)(M1.34a)(M1.39a)，共 52 个编号展示式）。
- **审稿人**：blp_referee（独立第三方，全新上下文）。先完成本轮独立评审与打分，之后才读取第 1 轮报告做逐条核对；评分只依据当前稿件，未参考上一轮分数，未读作者自评或目标分。
- **结论**：**中等修改（major-minor revision）**。**无致命项**。核心机器（份额、反演、IV/GMM、供给 FOC 的方向与税楔子）全部数值验证正确；第 1 轮的致命项已彻底修正。剩余问题集中在：外部选项的微观基础与识别（新引入的问题）、BEV 能源成本估值的识别缺口、切换后矩的选择、跨动力组层面结论的外推性质、政策时钟/信息集（漏 2024 年标签标准）、若干识别论断的条件、记号冲突与一处公式渲染截断。
- **总分：81 / 100**。

## 0.1 实际显式加载（Read）的文件

1. 角色与评分细则：`.claude/agents/blp-referee.md`。
2. 技能：`blp-model-building/SKILL.md`、`references/构造与组合协议.md`、`references/模块集成图.md`、`references/technical/blp1995_verified_equations.md`、`micro_foundations.md`、`supply_welfare_counterfactual.md`、`project_china_driving_cycle.md`（检索项目事实）；`blp-project-professor/SKILL.md`、`references/five-paper-kernel.md`、`constructive-model-design.md`、`model-formula-ledger.md`；`structural-model-building/SKILL.md`、`references/identification_and_claim_ladder.md`、`mechanism_construction_and_theory.md`；`economics-expert-reviewer/SKILL.md`、`references/review-standard.md`、`evidence-boundaries.md`；`top-journal-hypothesis-packaging/SKILL.md`。
3. 知识库核对：`BLP_KB/literature_memory/BLP_结构模型原文/` 的 A05 GRV2018（式 (1)–(5)、γρ、γ=0.91、在线附录 A.3、外部品 $u_{i00}=\varepsilon_{i00}$）、A09 BKL2024（$\alpha_i=\exp(\alpha_1+\alpha_2\log y+\sigma_p\nu)$、$\alpha_2=-1.21\,(0.12)$、容量只经续航、$\log(\text{range})$、$u_{i0}=0$）、A14 GHVB2021（0.16–0.39、均值之比高估、$\Delta WTP$ 换算）、A15 RS2021（$\tilde x=x-(1-\alpha)g$）、A20 Ji 等 2026（一半家庭、税楔子两式、9 个微观矩、$\ln p$、弹性 −3.85/−2.46/−2.88、“开 5 年旧燃油车”外部选项、spec 3 变号）、A23 Barwick 等 2026（续航与充电互为替代）；Li（2026）$\Sigma_\alpha$ 见 `formula_memory_20261009/04_核验账本与校正/VERIFICATION_LEDGER.md` 与 18 篇 JSON 包；政策时钟见 `dependencies_v6/project/national_model_sales_identification_memory.md` 与 `dependencies_v6/technical/blp-model-building/references/current-project-adapter.md`。
4. 用户原始要求：`MEMORY/00_断点记忆_CHECKPOINT.md` A 节（A1–A4 逐字）。按“市场—年月—车型聚合数据（非家庭调查）”“政策 = NEDC→WLTC/CLTC 工况切换”判断数据适配。
5. 实际运行：`tools/m1_examples.py`（输出与附录三张表逐格一致）、`tools/build_pdf.sh`（成功，21 页）、xelatex 日志、`pdftoppm` 逐页目检、技能自检 `blp_selftest.py`（ALL PASS），以及本轮自写的 7 个验算脚本（第 8 节）。

---

# 1 总体评价

**贡献与长处。** 第 2 版是一份完成度很高的基准模型推导。经济学链条完整：跨期预算 → Fisher 分离 → 准线性一阶近似 → 随机效用与 EV1 尺度归一化 → 由 CRRA 推出 $\ln\alpha_i$ 对收入的弹性 $a_y=-\rho_c$；生命周期能源成本 $K$ 从里程、衰减、存活、贴现与油价鞅逐项构造，量纲与数字全对；PHEV 电驱份额 $UF$ 与 BEV 续航缺口 $A(R)$ 都从出行距离分布推出，导数方向与曲率正确；口碑用正态共轭后验并给出“整体分 = 受限特例”的精确限制与近似条件。政策进入方式回答得清楚：工况切换不是虚拟变量，而是标签状态的跳变，经“标签 → 信念 → 广义价格 → 相对效用 → 份额”进入，楔子只承担“定义跳变、反事实标签、预定工具”三种用途。第 1 轮的致命项（把份额变化等同于本产品效用变化）已用 (M1.34a) 彻底修正，并配有情景表与可复现的数值例；供给侧补齐了增值税、消费税、购置税、补贴上限，$\Delta$ 的方向与“税率不同则不对称”的论断正确；识别表补上了竞争解释、支持与秩三栏；命名纪律好（$\varphi=\gamma\zeta$ 称“标签成本估值率”，不叫短视或信任）。

**主要剩余问题（按后果排序）。**

1. **外部选项（新引入）**：(i) 与 §M1.2.1 用来论证“整车寿命口径”的“完善二手车市场”假设不一致——在同一假设下旧车剩余能源成本已资本化进转售价，只有“自身成本偏离市场资本化成本”的部分进入相对效用；该假设还要求各任车主里程相同。(ii) 识别表称 $\varphi^0$ 由“总份额对油价的反应”识别，但这一变异正是 $\xi_{d,m,t}$ 吸收的 $(m,t)$ 层变化（稿件 §M1.2.4 自己也这样写）；数值上 $\partial\delta/\partial\varphi^0$ 只有约 1.2%–1.5% 留在组内。(iii) $\varphi^0=\gamma_{\mathrm I}$ 若真可识别，M1 内即可分离 $\gamma_{\mathrm I}$ 与 $\zeta_{\mathrm I,c}$，与 §M1.14“γ 在 M1 中不能单独回答”矛盾。
2. **BEV（及 PHEV 电耗部分）能源成本估值率 $\varphi_{\mathrm B,c}$ 的识别没有论证**：识别表只写“油价”变异，而中国居民电价几乎不随时间变化。
3. **切换后完全放弃 $K\times L$ 矩**缺乏依据，使 $\varphi_{d,X}$ 只依赖可能很弱的 $Z^W$。
4. **跨动力组层面的预测（情景表）是函数形式外推**：$\xi_{d,m,t}$ 吸收了同动力同月的共同跳变，须写出维持假设并给验证。
5. **政策时钟与信息集不完整**：样本内 2024-07-01 生效的 GB 22757.1/.2—2023 标签标准（既有车型 2024-09-01 前换标）没有编码；PHEV 各期实际展示的标签字段未核。
6. 两处识别论断缺条件：(M1.35)(i) 的“不可分”只在楔子同质时成立；(M1.44) 的检验只有在先验/口碑信源与标签相关时才有功效。
7. 记号冲突（$W_j$ 同时是楔子与整备质量、$\kappa$ 同时是税导数与信念权重、$N$、$c$ 多义），(M1.35) 在 PDF 中越出页边被截字。

这些都可以在一轮修改内解决；修好之后，基准模型达到很高水准是现实的。

---

# 2 八维度得分

| 维度 | 满分 | 得分 | 扣分理由 |
|---|---:|---:|---|
| 经济学基础与原语（偏好、预算、时序、信息集） | 15 | **11.5** | 推导链完整、时序清楚、$L/T/B$ 严格分开。扣分：外部选项与完善转售假设不一致，整车寿命口径的“等价”需各任车主里程相同（MF1，−1.5）；比例信念 $B=\zeta L$ 缺微观基础与理性预期锚点（MF7，−0.5）；政策时钟漏 2024 年标签标准、PHEV 展示字段未定（MF8，−1）；(M1.3) 需要的“车辆服务与消费加性可分”未写明（−0.5） |
| 数学推导正确（逐步可验证、符号/单位/方向） | 20 | **18** | 约 35 个式子经 sympy/数值验证无误（第 8 节）。扣分：(M1.34a) 第 2 点的简化式跨动力混用单位与 $\varphi$；一阶近似对大楔子（PHEV +59.3%）误差可观却未提示；§M1.13 “退化为市场均值处的 Dirac”措辞与构造协议的代表类型退化不一致；$\ln mc$ 用于可能为负的 $mc^{eff}$；(M1.43) 在准差分下未相应改写（合计 −2） |
| BLP/结构模型一致性（份额、反演、IV/GMM、正规化、outside） | 15 | **12** | 份额、收缩映射（含 $V_{i0}\ne0$）、价格在 $\mu$ 时 $\xi=\delta-x\beta$、浓缩、FOC 方向与 $\kappa$ 全对。扣分：外部选项的正规化与可识别部分处理有误（MF1，−1.5）；组层面结论依赖被 $\xi_{d,m,t}$ 吸收的共同成分（MF4，−1）；供给矩与 $mc^{eff}$ 不一致（MF9，−0.5） |
| 新参数的经济学构造与含义 | 10 | **8** | $\alpha_i,K,\zeta,\varphi,\eta,\chi,\varkappa,UF,\theta_k,b^W,\kappa_{jt}$ 均有定义、单位与符号。扣分：$\varphi^0$ 的经济含义（$=\gamma_{\mathrm I}$）与“γ 不可识别”冲突（−1）；$\zeta$ 缺 RE 锚点、无法与“认证信息偏差收敛/信念校准改善”对接（−0.5）；$\psi_{i,d}$ 的经济含义未定义（−0.5） |
| 识别论证（变异、排除、秩、rival、falsifier） | 15 | **11** | 五栏登记表、固定效应吸收表、联合检验的维持假设、弱工具警示都做得好。扣分：$\varphi^0$ 行错误（−1）；缺 $\varphi_{\mathrm B,c}$ 行（−1）；切换后矩选择（−0.75）；组层面外推未标明（−0.5）；(M1.35)(i) 与 (M1.44) 论断缺条件（−0.75） |
| 文献一致性与来源标注（不冒称原式） | 10 | **8.5** | GRV、BKL、Ji 等、GHVB、RS、Barwick 等、Li（2026）、BLP 各处数字与原卡一致。扣分：(M1.8) 标 [O] 与 §M1.15 的 [O·卡] 不一致、图例把“已核卡片”也算 [O]；“$B=\zeta L$ 是 RS 不含真值成分的特例”只对 $\zeta=1$ 成立；GRV 在线附录 A.3 未读却标 [O·卡]；AKS 2013 为转引；Li（2026）为城市—月数据却放在“仅有全国数据时”的语境（合计 −1.5） |
| 回应用户问题与数据适配（市场—月—车型） | 10 | **9** | 五个子问题逐一回答，产品 = 车型、配置聚合、上险量、市场规模与外部份额、整备质量缺失都处理了。扣分：联合类型分布（收入、里程、家充、日行驶分布、长途次数、置换状态）的中国数据来源与降级方案未给（−0.5）；$T^{show}$ 的数据来源（标识备案启用日）未写（−0.5） |
| LaTeX 规范与可读性 | 5 | **3** | 编译通过、无缺字、52 个展示式编号唯一、GitHub 安全写法基本到位。扣分：(M1.35) 越界 84pt、“识别”二字被截掉；其后段落被 pandoc 解析为罗马数字列表；(M1.45) 越界 22pt；记号冲突较多（MF10）；`u^{*}` 违反本项目排版规则 |
| **合计** | **100** | **81** | 无致命项，无上限约束 |

---

# 3 致命项

**无。** 逐条对照细则：

- 导数方向或符号错误导致结论反转：未发现。(M1.33)–(M1.34a)、(M1.36)–(M1.39a)、(M1.46)–(M1.47) 全部经数值验证（第 8 节 V5–V10）。
- 把校准/假设说成已识别：曾考虑 MF1(b)（$\varphi^0$ 行把被固定效应吸收的变异写成识别来源）。未判为致命，理由是：$\varphi^0$ 是次要参数，稿件 §M1.2.4 已承认其 $(m,t)$ 均值被吸收，核心估计对象 $\varphi_{d,c}$ 的识别不受影响；但必须修改。$\zeta^R_{\mathrm B,N}=1$ 已明确写成识别假设，合格。
- 福利公式误用：M1 不计算福利。
- 份额/反演/FOC 核心式错误：无。
- 不回应用户核心问题：否，回应完整。

---

# 4 逐式核验清单

| 式号 | 结论 | 说明（验算编号见第 8 节） |
|---|---|---|
| (M1.1) | 通过 | 市场规模数字复核：$\bar h=0.5$ 时月内部份额 0.082、外部 0.918；$\bar h=0.07$ 时 0.583（V1） |
| (M1.2)–(M1.3) | 通过；假设需补 | 现值预算正确；Fisher 分离需“车辆服务与消费加性可分”；“首任持有期+残值 = 整车寿命”需各任车主里程相同（MF1） |
| (M1.4)–(M1.5) | 通过 | 一阶展开与尺度归一化正确；(M1.8)(M1.15) 中 $\Phi_{ij}$ 应为 $\Phi_{ij}/\sigma_\varepsilon$（MF10） |
| (M1.6) | 通过 | sympy：CRRA 下 $d\ln\lambda/d\ln\mathcal W=-\rho_c$；BKL $\alpha_2=-1.21\,(0.12)$ 与卡一致（V5） |
| (M1.7)/(M1.7a) | **问题** | 与完善转售假设冲突、期限不对称、识别与固定效应矛盾（MF1） |
| (M1.8) | 通过；标注 | GRV 式 (1) 在 γ=1 的情形；[O]/[O·卡] 不一致（MF12） |
| (M1.9)–(M1.11) | 通过 | $\Lambda=7.7217$，$K^F=6949.6$，0.539 L/100km → 3746 元；家充/公充 7645/22239 元（V1） |
| (M1.12) | 通过 | 对数正态日距离下 $\partial UF/\partial R$ 解析式与数值导数一致到 7 位（V2） |
| (M1.13) | 通过；信息集 | 代数正确；PHEV 各期实际展示字段待核（MF8） |
| (M1.14)–(M1.15) | 通过 | — |
| (M1.16) | 设定 [P] | 建议补微观基础与 RE 锚点（MF7） |
| (M1.17)–(M1.18) | 通过 | sympy：MRS $=\varphi$（V5） |
| (M1.19)–(M1.20a) | 通过 | sympy：$B_{post}/B_{pre}=(1+w)/(1+\bar w)$；(b) 在比例信念类中恰为 RE 基准（MF7） |
| (M1.21)–(M1.24a) | 通过 | $A'=-n\Pr(D>R)$、$A''=ng(R)$ 数值一致；交叉偏导 $-8.7725\times10^{-3}$（V3、V14）。(M1.24a) 的“$<0$”应为“$\le0$（$\varkappa>0$ 时 $<0$）” |
| (M1.25)–(M1.26) | 通过 | 例 B 逐数复核；蒙特卡洛回归斜率 $(0.4759,0.0835)$ 对理论 $(0.4762,0.0833)$（V4） |
| (M1.27)–(M1.30) | 通过 | 结构一致；外部选项项见 MF1 |
| (M1.31) | 通过；时钟 | 需扩展到 2024 年格式时钟（MF8） |
| (M1.32) | 通过 | — |
| (M1.33)–(M1.34) | 通过 | sympy：两种路径分解、天真与已知平均换算两式残差均为 0（V5） |
| (M1.34a) | 通过 | 异质 RC logit（含外部选项能源成本）中复核：楔子最小的 ICE1 效用下降但份额上升（$s_0=0.3$：$+0.0104$；$s_0=0.6$：$+0.0048$）。一阶近似对大冲击误差大（ICE2 精确 $-0.0029$，一阶 $-0.0010$）（V7） |
| (M1.35) | **问题** | (i) 的“不可分”只在楔子同质时成立（MF5，V12）；渲染截断（MF11） |
| (M1.36)–(M1.38) | 通过 | 解析导数与有限差分最大误差 $3.7\times10^{-13}$；加总残差 $-9.4\times10^{-12}$；转移率和为 1（V6） |
| (M1.39)–(M1.39a) | 通过 | BEV 续航导数解析/数值均为 $2.442606\times10^{-6}$；$\partial G/\partial UF=K^F(L^{F,CD}-L^{F,CS})+K^EL^{E,CD}$（V6b、V5） |
| (M1.40) | 通过 | $V_{i0}\ne0$ 时收缩映射 27 次收敛，$\delta$ 误差 $2.5\times10^{-13}$（V8） |
| (M1.41) | 通过；推论需补 | 共同跳变被吸收后组层面结论的性质（MF4） |
| (M1.42)–(M1.43) | 通过 | 浓缩闭式解与 BFGS 最大差 $7\times10^{-9}$（V9）；准差分时需对准差分后的 $\delta$、$X_1$ 浓缩（S7） |
| (M1.44) | 通过；功效条件 | MF6（V13） |
| (M1.45) | 通过 | sympy：$p^c$ 因式分解与 $\kappa=(1+t^c)(1+t^v+t^p)$ 精确，与 Ji 等两式一致（V5）；排版越界（MF11） |
| (M1.46)–(M1.47) | 通过 | 4 产品 2 企业、ICE 含税 NEV 免税：按 (3.4) 方向精确还原 mc $=[6,7,6.5,7.5]$；转置方向最大误差 0.062；税率相同时两方向一致（V10） |

---

# 5 必须修改项

## MF1【外部选项：与二手车市场假设不一致；$\varphi^0$ 的识别论断与固定效应矛盾；与“γ 在 M1 不可识别”冲突】

**位置**：§M1.2.1（“在完善的二手车市场中……两种口径在完全市场下等价”）；(M1.7)/(M1.7a)；(M1.28) 末行及“$\varphi^0_{\mathrm I,N}=\gamma_{\mathrm I}$”；§M1.11 表 $\varphi^0$ 行；§M1.14“不能单独回答 γ”。

**问题 (a)：微观基础前后不一致。** §M1.2.1 用“完善二手车市场使转售价资本化后续车主的能源成本”论证整车寿命口径。同一假设下，置换型消费者买新车时以市场价 $P^u_{mt}$ 卖掉旧车，而 $P^u$ 已资本化旧车剩余能源成本。写出两条预算（价格以元计，$\bar K^{F,0}_{mt}$ 为边际二手买家的成本尺度）：

$$
U^{keep}_{i}=\Phi_{i0}-\alpha_i\gamma_{\mathrm I}K^{F,0}_{imt}\bar e_{0,m},\qquad
U^{buy}_{ij}=\Phi_{ij}-\alpha_i\big(p^c_{jmt}+\gamma_dK_{imt}B_{ijmt}\big)+\alpha_iP^u_{mt},
$$

$$
P^u_{mt}=\frac{\bar\Phi_0}{\alpha}-\gamma_{\mathrm I}\bar K^{F,0}_{mt}\bar e_{0,m}
\quad\Longrightarrow\quad
V_{i0}=\frac{\Phi_{i0}-\bar\Phi_0}{\sigma_\varepsilon}-\alpha_i\,o_i\,\gamma_{\mathrm I}\big(K^{F,0}_{imt}-\bar K^{F,0}_{mt}\big)\bar e_{0,m}.
$$

旧车能源成本只以“自身成本偏离市场资本化成本”的形式进入，其 $(m,t)$ 均值为零。若坚持 (M1.7) 的全额形式，就必须假设置换者报废旧车或二手市场不完善——但这又削弱 §M1.2.1 的等价论证。同一份推导不能对新车用完善转售、对旧车用无转售。

**同一假设的第二个后果**：§M1.2.1 的“首任持有期+残值 = 整车寿命成本”只有在各任车主里程相同（或首任车主持有到报废）时成立。里程异质时，完善转售下首任车主的成本尺度应为

$$
K^F_{imt}=\frac{\pi^F_{mt}}{100}\Big[VKT_i\,\Lambda(r;1,H)+\overline{VKT}^{\,next}\,\Lambda(r;H+1,\bar A)\Big],\qquad
\Lambda(r;a_1,a_2)\equiv\sum_{a=a_1}^{a_2}\frac{S_a v_a}{(1+r)^a},
$$

而不是 $VKT_i\Lambda(r,\bar A)$。这直接改变 $K_i$ 的离散度，也就改变 (M1.38) 的转移权重与 GRV 式分选。也可以沿用 GRV 的“持有至报废”假设（GRV 式 (2) 用个体里程乘 $S$ 年），但应明说，而不是用完善转售来论证。

**期限不对称**：新车按 $\bar A$ 年计、外部选项只按剩余 $\bar A_0$ 年计，$\bar A_0$ 之后的替换成本没有入账，需说明这是静态模型的近似。

**问题 (b)：识别论断错误。** §M1.11 表称 $\varphi^0$ 由“油价 × 市场旧车油耗 × 置换比例”识别，矩为“总份额对油价的反应”。但 §M1.2.4 自己写明“动力×市场×月固定效应也只吸收其 $(m,t)$ 均值”，§M1.10.2 也把 $K_{mt}$ 主效应列为被 $\xi_{d,m,t}$ 吸收。总份额对油价的反应正是 $(m,t)$ 层变化，被全部吸收。$\varphi^0$ 只剩类型间异质性这一条途径（油价变化通过 $\alpha_io_iK_i$ 的离散度改变各内部产品的买家构成），非常弱。验算 V11：$\partial\delta/\partial\varphi^0$ 的范数只有 1.2%–1.5% 留在 $(d,m,t)$ 组内，$\partial\delta/\partial\varphi_{\mathrm I,N}$ 为 14.5%。

**问题 (c)：逻辑冲突。** (M1.28) 规定 $\varphi^0=\gamma_{\mathrm I}$，而 $\varphi_{\mathrm I,c}=\gamma_{\mathrm I}\zeta_{\mathrm I,c}$。若 $\varphi^0$ 如表所说可识别，则 M1 内即得 $\gamma_{\mathrm I}=\varphi^0$、$\zeta_{\mathrm I,c}=\varphi_{\mathrm I,c}/\varphi^0$，与 §M1.4.2 末句和 §M1.14“γ 与信息权重在 M1 中只以乘积出现”直接矛盾。

**修改**：二选一并贯通全文。

1. **完善转售版**：用上面的偏离项 $V_{i0}$；§M1.2.1 的等价改写为“各任车主里程相同或首任车主持有至报废”，否则用分段 $K^F_{imt}$。
2. **无转售版**：保留 (M1.7)，删去或限定 §M1.2.1 的完善转售论证，并处理期限对齐。

两种版本都要：(i) 把 §M1.11 的 $\varphi^0$ 行改为“仅由类型间异质性识别，预期很弱；基准中固定 $\varphi^0$ 于外部值（M3 的 $\gamma_{\mathrm I}$ 或 GRV 的 0.91），报告敏感性”；(ii) 在 §M1.14 加一句：“$\varphi^0$ 若自由估计，会在 M1 内分离 $\gamma_{\mathrm I}$ 与 $\zeta_{\mathrm I,c}$；这条途径只靠函数形式与类型分布，本稿不依赖它，因此仍把 γ 视为 M1 不可识别。”

## MF2【缺 BEV（及 PHEV 电耗部分）能源成本估值率的识别论证】

**位置**：§M1.11 表 $\varphi_{d,N}$、$\varphi_{d,X}$ 两行（只写“油价”变异）；(M1.11)(M1.27)。

**问题**：$\varphi_{\mathrm B,c}=\gamma_{\mathrm B}\zeta^E_{\mathrm B,c}$ 乘 $K^EL^E$，$K^E$ 的变动来自居民电价、公共快充价（含服务费）与家充可得性 $h_i$。中国居民电价多年基本不变，时间变异很小；在 $\xi_{\mathrm B,m,t}$ 之下，$\varphi_{\mathrm B,N}$ 只能靠“城市间电价/家充比例 × 车型电耗标签”的截面交互识别。竞争解释是城市对小车或高能效车型的口味（与收入、拥堵、限牌相关），以及补能密度 $N_{mt}$（它同时进入 $\chi(N)A(R)$）。表中没有这一行，读者会以为 $\varphi_{\mathrm B}$ 与 $\varphi_{\mathrm I}$ 同样由油价识别。这对用户最关心的新能源与燃油车替代至关重要。

**修改**：补一行，并给退路。

| 参数 | 识别变异 | 矩 | rival | 有效支持 | 局部秩 |
|---|---|---|---|---|---|
| $\varphi_{\mathrm B,N},\varphi_{\mathrm B,X}$ | 城市间与跨期的公共充电价格/服务费、分时电价调整、家充比例 × $L^E_j$；CLTC 下 $L^E$ 的跳变（比值） | $E[(\bar K^E_{mt}L^E_{jt})\nu]$ | 城市口味、补能密度、地方 NEV 政策 | 居民电价时间变异小 | 与 $\varkappa,\bar\eta$ 的联合秩 |

退路：(a) 施加 $\gamma_{\mathrm B}=\gamma_{\mathrm I}$（A-γ 的跨动力版本，可在有支持时检验），只估 $\zeta_{\mathrm B,X}/\zeta_{\mathrm B,N}$；(b) 或固定 $\varphi_{\mathrm B,N}$ 于外部值，报告敏感性。同时说明 PHEV 的 $\varphi_{\mathrm P,c}$ 同乘油、电两部分，其识别主要来自油价部分。

## MF3【$\varphi_{d,X}$ 的矩选择：切换后完全放弃 $K\times L$ 矩缺乏依据】

**位置**：§M1.11 表 $\varphi_{d,X}$ 行（“切换后只用 $E[Z^W\nu]$ 及其交互，不再用 $E[KL\nu]$，因展示时点可能内生”）。

**问题**：展示时点内生，污染的是利用跳变本身（前后对比）的矩。切换后、同一产品内部由油价时间变化带来的 $(K_{mt}-\bar K^{post}_{jm})L^X_j$ 变异，只要油价波动与 $\nu$ 无关，仍然有效；产品“何时进入新状态”的选择若只与 $\nu$ 的水平相关，会被产品×状态均值吸收。完全放弃这组矩，$\varphi_{d,X}$ 就只能靠可能很弱的 $Z^W$（项目层楔子对属性 $R^2\approx0.30$）。（上一轮建议“切换后只用 $Z^W$”，本轮认为过于保守。）

**修改**：写成三组矩：

$$
E\Big[(K_{mt}-\bar K^{pre}_{jm})L^N_j\,\nu_{jmt}\,\mathbf 1\lbrace t<T_j\rbrace\Big]=0,\qquad
E\Big[(K_{mt}-\bar K^{post}_{jm})L^X_j\,\nu_{jmt}\,\mathbf 1\lbrace t\ge T_j\rbrace\Big]=0,\qquad
E\big[Z^W_{jt}\,\nu_{jmt}\big]=0.
$$

第一组识别 $\varphi_{d,N}$，第二、三组识别 $\varphi_{d,X}$，第二组与第三组之间的过度识别检验就是“跳变是否外生”的检验。若担心 $L^X$ 本身因认证策略而内生，那是另一个问题，应单列并给工具。

## MF4【跨动力组层面的预测是函数形式外推，需写出维持假设并给验证】

**位置**：§M1.8.4 情景预测表；§M1.10.2 表第 3 行；§M1.14 P1、P4。

**问题**：$\xi_{d,m,t}$ 吸收了同动力同月的共同跳变，所以识别 $\varphi$ 的只是同一动力内的相对变化（加交错时点）。情景表中“ICE/HEV 组↓、BEV 组↑、外部↑”这类组层面结论，是把组内相对变化估出的 $\varphi$ 外推到被固定效应吸收的共同成分上，维持假设是“$\xi_{d,m,t}$ 不含标签引起的成分”。跨动力替代方向正是用户最关心的问题，必须讲清哪些是识别出来的、哪些是模型推出的（claim ladder 第 7 节）。

**修改**：

1. 写出维持假设 **A-FE**：$\xi_{d,m,t}$ 与标签的共同跳变无关，即共同成分与车型差异成分由同一 $\varphi_{d,c}$ 计价。
2. 情景表标题注明“结构模型推出，非由共同成分直接识别”。
3. 给验证：用交错切换队列（2021-07 起新申请、2023-01 前在产车型）做组层面的留出检验；按 claim ladder 第 5 节，用同一简约式算子作用于模拟数据，再与 M0 事件研究系数比较：

$$
\hat\beta^{model,cf}(\hat\theta)=R\big(q^{policy}(\hat\theta;\xi^{base})\big)-R\big(q^{no\,policy}(\hat\theta;\xi^{base})\big).
$$

## MF5【(M1.35)(i) 的“不可分”只在楔子同质时成立】

**位置**：(M1.35)(i)。

**问题**：切换后 (i) 的项为 $-\alpha_iK\big[(\varphi_d+b^K)L^X-b^KL^N\big]$，M1 为 $-\alpha_iK\varphi_{d,X}L^X$，两者在 $(KL^X,KL^N)$ 坐标里是不同的限制。只要楔子 $w_j$ 在动力内有离散，$[KL^X,\,KW]$ 列满秩，$b^K$ 与 $\varphi_{d,X}-\varphi_{d,N}$ 就能分开（虽然很弱）；只有 $w_j$ 在动力内相同时才不可分。验算 V12：$w$ 在 4.8%–11.4% 间分布时，缩放奇异值为 $(1.407,\,0.140)$、条件数 10.1；$w$ 恒为 7.7% 时第二奇异值为 0。上一轮建议的措辞也有这个漏洞。

**修改**：改为“$b^K_d$ 能否与 $\varphi_{d,X}-\varphi_{d,N}$ 分开，取决于动力内楔子的离散度：$\operatorname{rank}[KL^X,\,KW]=2$ 当且仅当 $w_j$ 不是常数。实际楔子离散有限，分离很弱，应报告缩放条件数，基准中不同时放开二者。”

## MF6【(M1.44) 的检验功效条件】

**位置**：§M1.11.1。

**问题**：双信源 $B=\kappa\zeta L+(1-\kappa)m$ 下，油价反应中的 $(1-\kappa)m(K-\bar K)$ 部分，只有当 $m_j$ 与 $L_j$（去掉固定效应后）相关时才会载到 $\varphi^K$ 上；若二者无关，$\varphi^K=\varphi^L=\gamma\kappa\zeta$，检验没有功效。验算 V13：真值 $\gamma\kappa\zeta=0.648$；$m$ 与 $L$ 无关时估得 $(\varphi^L,\varphi^K)=(0.648,\,0.645)$，相关时为 $(0.660,\,0.951)$。

**修改**：在“二者不等，$H_0$ 被拒绝”前加条件“当先验或口碑信源 $m_j$ 与标签在固定效应残差上相关，即 $\operatorname{Cov}(\tilde m_j,\tilde L_j)\ne0$ 时”；并写明“不拒绝 $H_0$ 不能作为比例信念成立的证据”。

## MF7【比例信念的微观基础与理性预期锚点】

**位置**：(M1.16)、参数定义 3、§M1.4.3。

**问题**：$\zeta$ 是 M1 政策通道的核心参数，目前只是 [P] 设定。用户要求新参数“从基础经济学理论定义并构造”。这里只需几行就能给出微观基础，还能顺带得到一个可检验的理性基准，并为“认证信息偏差收敛”与“信念校准改善”提供可操作的区分。

**修改**：增加如下推导。若消费者认为真实能耗与标签之比在 $(d,c)$ 内与标签独立，

$$
T_{jm}=\zeta^{true}_{d,c}\,L_{jt}\,\eta_{jm},\qquad E[\eta_{jm}\mid L_{jt},d,c]=1,
$$

则只看当期标签的消费者的条件期望为

$$
B_{jt}=E[T_{jm}\mid L_{jt},d,c]=\zeta_{d,c}L_{jt},\qquad \zeta^{RE}_{d,c}\equiv E\big[T/L\mid d,c\big].
$$

定义信念校准指数 $\zeta_{d,c}/\zeta^{RE}_{d,c}$，其中 $\zeta^{RE}$ 用车主实测或道路测试数据外部构造（属外部矩或校准，不由销量识别）。在真实能耗不变、$w\perp T/L^N$ 时，

$$
\frac{\zeta^{RE}_{d,X}}{\zeta^{RE}_{d,N}}=\frac{E[T/L^X]}{E[T/L^N]}=E\Big[\frac{1}{1+w}\Big]\approx\frac{1}{1+\bar w_d}.
$$

因此在“只用当期标签”的信息集下，基准 (b) 正是比例信念类中的理性预期基准，(a) 天真是偏离 RE 的基准。“认证信息偏差收敛”可定义为 $E|\ln(T/L)|$ 跨工况下降（标签精度），“信念校准改善”定义为 $|\zeta_{d,c}/\zeta^{RE}_{d,c}-1|$ 下降。两者不同，符合技能的命名纪律。

## MF8【政策时钟与信息集：漏掉 2024 年标签标准；PHEV 标签字段须按实际展示确定】

**位置**：§M1.1.2 时序；(M1.31)；§M1.8.6；(M1.13) 之后一段；§M1.10.3 的 $Elig^{law}$。

**问题**：项目适配层与销量识别记忆写明（`current-project-adapter.md`；`national_model_sales_identification_memory.md` §2.2）：

- GB 22757.1/.2—2023 于 2024-07-01 实施，既有车型 2024-09-01 前换标，是与 2021 年工况切换相区分的标签制度改革；
- PHEV 的 CCC 换版时钟（TC11-2021-01）不同于 ICE 的 2021-07/2023-01；
- 过渡期标识按车型实际采用的工况分别标注（装备中心〔2021〕290 号）；
- 需求研究首选“官方能耗标识启用日”；
- “新标签不得无证据假定所有 BEV 续航上升”。

稿件时序只写了 2021-07、2023-01 与 BEV 自愿切换，样本内的第二次标签格式改革没有编码，§M1.8.6 的混杂清单里也没有它。PHEV 用分项标签 $(L^{R,CD},L^{F,CS},L^{E,CD})$ 形成信念，但没有核对 NEDC 期、WLTC 期与 2024 年新格式下实际展示了哪些字段。

**修改**：

1. 时序加入“标签标准生效与换标截止”时钟，把 $S_{jt}$ 扩展为 $(S^{cycle}_{jt},S^{format}_{jt})$；至少在 2024-07 至 2024-09 设甜甜圈并做稳健性。
2. 写明 $T^{show}_j$ 的数据来源：能耗标识备案系统的启用日与作废日。
3. PHEV 按每个时期实际展示的字段构造 $B$。若某期只展示综合值，该期只能用综合值；字段结构本身的变化也是信息变化，此时 $\varphi_{\mathrm P,N}$ 与 $\varphi_{\mathrm P,X}$ 不再是同一映射下可比的参数。
4. 情景表中“BEV 续航楔子小幅为正”标为假设，两种符号都给出预测。

## MF9【供给矩：$\ln mc$ 与 $mc^{eff}$ 不一致】

**位置**：§M1.12.3。

**问题**：反推得到的是 $mc^{eff}=mc-\lambda^Ca^C-\lambda^Na^N$，成本方程却写 $\ln mc_{jt}=w'\gamma^c+\omega$。$\lambda$ 未知时 $mc$ 不可得；NEV 积分价格高时 $mc^{eff}$ 可能为负，取对数不可行。

**修改**：M1 中改写为水平形式 $mc^{eff}_{jt}=w_{jt}'\gamma^{mc}+\omega_{jt}$，或把 $\lambda$ 作为待估参数并写出其识别（指向 M6）；并注明 M1 的估计中供给矩是否启用。

## MF10【记号冲突：声明“避免一符多义”但未做到】

| 符号 | 冲突 | 建议 |
|---|---|---|
| $W_j$ | 楔子 (M1.32) 与“整备质量 $W_j$”（§M1.10.3 表第 1 行、§M1.10.4 交互工具），同节同符号 | 整备质量记 $\mathrm{wt}_j$ |
| $\kappa$ | 税楔子导数 $\kappa_{jt}$ (M1.45) 与双信源信念权重 $\kappa$ (M1.44)，相邻两节；记忆约定 κ 为信任权重 | 税导数记 $\vartheta_{jt}$ |
| $N$ | NEDC 状态 $c=N$、补能密度 $N_{mt}$（同在 (M1.28)）、样本量 $N$ (M1.42)、$N(0,1)$ | 补能密度记 $\mathcal C_{mt}$，样本量记 $N_{obs}$ |
| $c$ | 工况状态，同时有 $p^c$、$t^c$、$\gamma^c$、$c_a$、$c_{ij}$、$c^P_{ij}$、$\bar c_i$ | 消费者价记 $p^{\mathrm{cons}}$，消费税记 $t^{\mathrm{ct}}$，成本参数记 $\gamma^{mc}$ |
| $\varrho$ | AR(1) 系数 $\varrho_\xi$ 与其他支出 $\varrho_{jmt}$ | AR 系数记 $\rho_\xi$ |
| $D$ | 人口特征 $D_i$ 与距离 $D^{day},D^{long}$、转移率 $D^L$ | 人口特征记 $\mathbf d_i$ |
| $\Phi_{ij}$ | (M1.5) 中为 $\Phi_{ij}/\sigma_\varepsilon$，(M1.8)(M1.15) 未除 | 令 $\tilde\Phi_{ij}\equiv\Phi_{ij}/\sigma_\varepsilon$ |

并在文首给一张记号表。

## MF11【渲染】

1. (M1.35) 在 PDF 中越出右边界 84pt，“识别”二字被截掉（第 13 页）。改为两行 `aligned`，或拆成 (M1.35a)(M1.35b) 两个展示式。
2. (M1.35) 之后以“(ii) 中不乘……”开头的段落被 pandoc 解析为罗马数字列表（PDF 中显示为缩进的列表项 (ii)），GitHub 下则是普通文字，两端不一致。改为“情形 (ii) 中……”。
3. (M1.45) 越界 22pt，用 `aligned` 分行。
4. (M1.8) 的 `u^{*}` 按本项目排版规则改为 `u^{\ast}`。

## MF12【来源标注的几处不实或不一致】

1. (M1.8) 标 [O]，§M1.15 对同一 GRV 式 (1)–(5) 标 [O·卡]；文首图例把“已核卡片”也算 [O]，与技能的 [O]（本轮对原页逐字核）/[O·卡]（卡片记为原页核验、本轮未再开页）区分不一致。统一为 [O·卡]，或附本轮原页核验记录。
2. “RS 的 $\tilde x=x-(1-\alpha)g$……本稿比例信念 $B=\zeta L$ 是其不含真值成分的特例”：不含真值成分即 $\alpha=0$，得 $\tilde x=m=L$，只对应 $\zeta=1$；$\zeta\ne1$ 时 $B=\zeta L$ 不在 RS 族内。改为“$\zeta=1$ 时与 RS 的 $\alpha=0$ 重合；一般 $\zeta$ 是对标签的比例校正；两族由 M2 的 $B=\alpha_TT+(1-\alpha_T)\zeta L$ 共同嵌套”。
3. “GRV 在线附录 A.3 的做法 [O·卡]”：五篇内核明确写 GRV“在线附录不算已读”，卡片只知道正文指向 A.3。改为“GRV 正文指向其在线附录 A.3（未读）”。
4. “Anderson–Kellogg–Sallee 2013 [O·卡]”：本地无此文卡片，是 GRV 卡的转述。改为“经 GRV 转引”。
5. Li（2026）的 $\Sigma_\alpha=0.0010\,(0.8451)$ 来自车型—城市—月数据（1,146,659 个观测），不是“仅有全国数据”的例子。改写语境：它说明即使有城市数据，价格随机系数也难识别。
6. 差异化工具（“特征空间距离小于一个标准差的竞品数”）是 Gandhi–Houde（2019）的构造。本地只有 Kaneko–Toyama 原文转引，应注明来源并标为文献提及。

---

# 6 建议项

- **S1 突出稳健的核心对象**：$\varphi_{d,X}/\varphi_{d,N}$（P2）对 $K$ 的乘性误设（$r$、$\bar A$、里程尺度）不变，而 $\varphi$ 的水平一比一受其影响。建议在 §M1.4.2 与 §M1.14 明说，把比值作为主报告对象。
- **S2 (M1.34a) 的用途**：一阶式用于解释；定量预测必须精确重解份额（PHEV 综合油耗楔子 +59.3%，一阶近似不可靠；V7 中 ICE2 的一阶误差已达 2/3）。第 2 点的简化式 $-\int\alpha_iK_iP_{ij}(W_j-\sum_kP_{ik}W_k)dF$ 只在同一动力、共同 $\varphi$ 与 $K$ 时成立，跨动力应写 $\sum_kP_{ik}\Delta u_{ik}$。
- **S3 §M1.13 退化**：改为“令类型分布退化为预定代表类型 $z^\ast$（该类型保留自身的日行驶与长途分布）”，避免“非线性输入取市场均值”的 mean-index 近似（构造协议 §2.2）。
- **S4 联合类型分布的数据方案**：给出可行来源与降级方案，例如家庭金融或追踪调查（收入—拥车）、全国出行调查或车联网数据（里程、日行驶与长途分布）、城市层私桩比例（家充）；只有边际分布时用独立 copula 加相关性敏感性。
- **S5 $\Lambda$ 按动力设定**：BEV 电池衰减影响 $S_a$、$v_a$ 与续航；$r$ 的选择（车贷利率还是存款利率）单列敏感性。
- **S6 (M1.3)**：写明“车辆服务流与消费加性可分”是 Fisher 分离式成立的前提。
- **S7 准差分下的浓缩**：AR(1) 时对准差分后的 $\delta$ 与 $X_1$ 应用 (M1.43)。
- **S8 $\theta_2$ 维数**：$\varphi_{d,c}$ 有 8 个，加 $\varphi^0,\zeta^R,\bar\eta,\varkappa,a_0,a_y,\sigma_p,\sigma_d,\Pi,\Sigma$，对聚合数据偏多。建议给一个简约基准（如 HEV 并入 ICE、跨动力共用 γ），并标明哪些参数固定或校准。
- **S9 两个相关系数**：§M1.2.4 引的 $+0.056$ 来自上一轮审稿人的参数设定，§M1.9 与例 C 的 $+0.33$ 来自本稿设定，应注明二者来源不同。
- **S10 情景表的 BEV 一行**：补上 CLTC 下电耗标签 $L^E$ 的变化，不只是续航。

---

# 7 对上一轮意见的逐条核对

| 上一轮条目 | 状态 | 依据（第 2 版位置） |
|---|---|---|
| **F1** 份额变化须看相对效用 | **已解决** | (M1.34a) 方框式、三点结论、情景表、例 A；§M1.4.2 不再有旧论断；P1 改写。本轮在异质 RC logit 中复核成立（V7） |
| 必改 1 = F1 重写与情景表 | 已解决 | 同上 |
| 必改 2 (M1.44) 恒等式 | **已解决**（残留功效条件） | 改为按变异来源分开的嵌套模型 $\varphi^L,\varphi^K$，列出外部选项、里程反弹、二手车价、均值回复等 rival，删除“信任”命名。功效条件见本轮 MF6 |
| 必改 3 供给税账户与 Δ 方向 | **已解决** | (M1.45) 纳入增值税、消费税、购置税、补贴及上限；$\kappa_{jt}$；(M1.47) 方向与“税率不同则不对称”论断正确（V10 复核） |
| 必改 4 外部选项能源成本 | **部分解决** | 加入 (M1.7)/(M1.7a)，删去“由 $\psi_{i,d}$ 吸收”。但引出新问题：与完善转售假设冲突、$\varphi^0$ 识别论断错、与“γ 不可识别”矛盾（本轮 MF1） |
| 必改 5 (M1.20) 改名与限定 | **已解决** | 改称“已知平均换算”，新增真正的表示不变性 (M1.20a)；A-γ 写为维持假设；“理性推断”移至 M2 |
| 必改 6 记号统一 | **部分解决** | $w_j$ 统一为相对楔子；工况改记 $c$；$D^{day}/D^{long}$ 区分；说明 $\pi$。新增 $W_j$、$\kappa$、$N$、$c$、$\varrho$、$D$ 冲突（本轮 MF10） |
| 必改 7 (M1.37) WTP 符号 | **已解决** | $WTP_i(\Delta L=-1)=(\partial V/\partial L)/(\partial V/\partial p)=\varphi K$ |
| 必改 8 (M1.35) 论断 | 已按上一轮措辞修改 | 但该措辞本身需加“动力内楔子有离散”的条件（本轮 MF5，V12） |
| 必改 9 固定效应吸收 | **已解决** | §M1.10.2 吸收对象表；但 §M1.11 的 $\varphi^0$ 行与之矛盾（本轮 MF1） |
| 必改 10 识别表 | **大部分解决** | rival、支持、秩三栏齐全；$a_y,\sigma_p$ 有成本×收入交互与微观矩；$\widetilde Q$ 改为准差分与深滞后。“切换后只用 $Z^W$”照上一轮建议处理，本轮认为过于保守（本轮 MF3） |
| 必改 11 数据层级 | **已解决** | 产品 = 车型；配置聚合规则、固定配置篮子、测量误差与自助法；说明 GRV 型车型内变异不可得及替代识别；整备质量缺失 60%–65% |
| 必改 12 市场规模 | **已解决** | $\bar h=0.5$，敏感性 $\lbrace0.25,1\rbrace$，要求报告外部份额分布（V1 复核数字） |
| 必改 13 $K$ 校准与 $\varphi$ 解释 | **已解决** | “$\varphi$ 只在外部给定的 $K$ 尺度下识别”，$r\times\bar A\times VKT$ 敏感性网格，里程分布映射 |
| 必改 14 $\zeta^R_0=1$ | **已解决** | 写明是识别假设，敏感性 $\lbrace0.7,0.8,1\rbrace$，按动力分开 |
| S1 PHEV 续航边际效应 | 已解决 | (M1.39a)，链式项与符号正确（V5） |
| S2 类型联合分布 | 已解决 | §M1.7.4 联合抽样或 copula；$365E[D]=VKT$；$\tilde h=h\bar c$。数据来源未给（本轮 S4） |
| S3 混合展示 | 已解决 | §M1.8.1 用选择概率混合 |
| S4 楔子四项分解 | 已解决 | §M1.8.2 |
| S5 口碑与 $x$ 重叠 | 已解决 | §M1.6.1 |
| S6 (M1.26) 拆分 | 已解决 | 精确限制 + 近似条件 + 例 B（V4 复核） |
| S7 来源标注 | 大部分解决 | GRV (7) 标文字层，Ji 等 $\ln p$ 已注明，RV2014 删除，锂价论断改写。仍有 [O]/[O·卡] 不一致等（本轮 MF12） |
| S8 GHVB、RS 对接 | 已解决 | §M1.15；RS 嵌套措辞不准（本轮 MF12） |
| S9 CAFC 两侧 | 已解决 | §M1.12.3 |
| S10 诊断区间出处 | 已解决 | Ji 等弹性 −3.85/−2.46/−2.88 |
| S11 “闭式”措辞 | 已解决 | “需模拟计算” |
| S12 分解的路径依赖 | 已解决 | (M1.33) 后注明两种写法 |
| S13 退化清单 | 已解决 | 补齐各类型变量；措辞需改为代表类型（本轮 S3） |
| S14 残值 | 以整车寿命口径化解 | 但该口径的完善转售论证引出本轮 MF1(a) |
| S15 补贴口径 | 已解决 | BEV 与 PHEV 分开 |
| S16 排版 | 部分解决 | 原 (M1.24)(M1.39) 越界已消除；新出现 (M1.35) 截断与 (M1.45) 越界（本轮 MF11）；“钢价指数”已写成数学式，但 $W_j$ 与楔子冲突（本轮 MF10） |
| S17 跨市场表述 | 已解决 | §M1.9 区分市场内（里程）与跨市场（油价） |

---

# 8 验算记录

环境：Python 3（`python3 -I`），numpy 2.5.3、scipy 1.18.1、sympy 1.14.0。全部为合成检验，不涉及项目数据，不代表经验识别（技能红线：公式内部自洽不证明排除限制成立）。

## 8.1 结果汇总

| 编号 | 检验对象 | 结果 |
|---|---|---|
| R0 | `tools/m1_examples.py` | 例 A：$s_0=0.22$ 时 ICE1 $0.1950\to0.2035$（精确 $+0.00854$，一阶 $+0.00898$），$s_0=0.58$ 时 $0.1050\to0.1061$；例 B：$(0.952,0.167)$、$0.1679$、$0.0851$；例 C：corr $-0.098/+0.328$，标签转移→最省油车 $0.1509/0.1065$，→外部 $0.2947/0.2514$。与附录表逐格一致 |
| R1 | `blp_selftest.py` | 19 项 ALL PASS（(6.9b) 负号与下标、Δ 方向、单产品 logit 加价、logsum、$A'(R)$、$A''(R)$ 等） |
| R2 | PDF 构建 | `build_pdf.sh` 成功，21 页；xelatex 无缺字；Overfull：第 930 行即 (M1.35) 84.07pt（目检：“识别”被截），第 1309 行即 (M1.45) 22.44pt，表格对齐 0.116pt×3；(M1.35) 后段落被转为 `enumerate`（罗马数字从 ii 起） |
| R3 | GitHub 写法 | 52 个 `$$` 块前后均有空行；无 `\{`；无表格内 `|`；唯一 `*` 在 (M1.8) `u^{*}` |
| V1 | (M1.10)(M1.11)、市场规模 | 见下方输出；全部与正文一致 |
| V2 | (M1.12) | 解析 $\partial UF/\partial R$ 与数值导数一致 |
| V3 | (M1.21)(M1.22) | $A'$、$A''$ 与解析式一致 |
| V4 | (M1.25)(M1.26)、例 B | 一致；蒙特卡洛回归验证“分项后验 = 总体后验加权和”与“整体分收缩权重 0.284” |
| V5 | (M1.6)(M1.18)(M1.20)(M1.33)(M1.34)(M1.39a)(M1.45) 符号代数 | 全部精确成立 |
| V6/V6b | (M1.36)–(M1.39) | 解析与有限差分误差 $\le4\times10^{-13}$；加总与转移率和为 1 |
| V7 | (M1.34a) 异质 RC logit | 规则成立；一阶近似对大冲击误差大 |
| V8 | (M1.40) | $V_{i0}\ne0$ 下收敛 |
| V9 | (M1.43) | 浓缩闭式解 = 数值最小化 |
| V10 | (M1.45)–(M1.47) | (3.4) 方向精确还原 mc；转置方向误差 0.062；同税率时两方向相同 |
| V11 | $\varphi^0$ 的组内识别变异 | 组内占比 1.2%–1.5%（对照 $\varphi_{\mathrm I,N}$ 为 14.5%） → MF1 |
| V12 | (M1.35)(i) 秩 | 楔子离散：条件数 10.1；楔子同质：秩亏 → MF5 |
| V13 | (M1.44) 功效 | $m\perp L$ 时 $\varphi^K\approx\varphi^L$，无功效 → MF6 |
| V14 | (M1.24a) 符号 | 交叉偏导为负，与解析式一致 |

## 8.2 输出（逐字）

```text
##### v1_algebra
=== V1 numbers ===
Lambda(5%,10)=7.7217; K^F=6949.6 yuan/(L/100km); 7.0*7.7%=0.539 L/100km -> PV 3746 yuan
BEV pi_E=0.55: K^E*15 = 7645 yuan
BEV pi_E=1.6: K^E*15 = 22239 yuan
hbar=0.5: monthly M=20.42M, inside share=0.082, outside=0.918
hbar=0.07: monthly M=2.86M, inside share=0.583, outside=0.417
peak month with hbar=0.07 needs monthly sales of 2.32 M
=== V5 symbolic ===
M1.33 decomposition 1 exact: True ; decomposition 2 exact: True
M1.34 naive: True
M1.34 avg  : True
M1.20 B_post/B_pre: (w + 1)/(wbar + 1)
M1.18 MRS: phi
M1.6 dln(lambda)/dln(W) = -rho_c
M1.45 p^c factorization exact: True ; kappa = (t_c + 1)*(t_p + t_v + 1)
Ji-consistency dp/dps: True
M1.39a dG/dUF = K_E*L_ECD + K_F*L_FCD - K_F*L_FCS
##### v2_range_uf
=== V2 UF derivative (M1.12) ===
R=30.0: UF=0.4581, dUF/dR numeric=1.050431e-02, analytic=1.050431e-02
R=60.0: UF=0.6592, dUF/dR numeric=3.947540e-03, analytic=3.947540e-03
R=100.0: UF=0.7500, dUF/dR numeric=1.195796e-03, analytic=1.195796e-03
=== V3 range-shortfall A(R) (M1.21-22) ===
R=300.0: A'=-2.283682 vs -n*Pr(D>R)=-2.283682;  A''=1.269808e-02 vs n*g(R)=1.269808e-02
R=450.0: A'=-0.981785 vs -n*Pr(D>R)=-0.981785;  A''=5.486566e-03 vs n*g(R)=5.486566e-03
R=600.0: A'=-0.433601 vs -n*Pr(D>R)=-0.433601;  A''=2.293237e-03 vs n*g(R)=2.293237e-03
=== V14 cross-partial sign (M1.24a) ===
d2u/dRdN numeric=-8.772496e-03, analytic=-8.772493e-03 (negative => substitutes)
=== V4 Bayes shrinkage / example B (M1.25-26) ===
lambda_k= [0.9524 0.1667]  sum omega Q_k= 0.1679  lam_all= 0.2837  Q_all= 0.0851
MC regression of sum(omega q) on subscore means: coefs [0.4759 0.0835]  (theory omega*lambda = [0.4762 0.0833] )
MC regression on overall mean only: slope 0.2833 (theory lam_all = 0.2837 )
##### v3_rc_logit
shares [0.0003 0.0006 0.0011 0.0016] outside 0.9965
=== V6 label derivatives (M1.36) vs finite differences ===
finite diff: [ 1.040e-06 -1.814e-04  2.430e-06  7.130e-06]  analytic: [ 1.040e-06 -1.814e-04  2.430e-06  7.130e-06]  max abs err: 3.7418246432374073e-13
adding-up: sum_k ds_k/dL_j + ds_0/dL_j = -9.435269406055102e-12
label diversion (M1.38): [0.0058 0.     0.0134 0.0393] to outside 0.9415 sum 1.0
=== V6b BEV range derivative (M1.39) via a range term ===
ds_B/dL^R finite diff=2.442606e-06, analytic=2.442606e-06
=== V7 relative-utility rule (M1.34a) under heterogeneity ===
own du (mean): [-0.0509 -0.3967 -0.6104  0.    ]
exact ds: [-7.00e-06 -1.18e-04 -2.94e-04  1.00e-05]  first-order (M1.34a): [-7.00e-06 -1.38e-04 -3.64e-04  1.30e-05]
homogeneous-rule threshold check: sign(exact) = [-1. -1. -1.  1.]  ; ICE1 has lowest wedge and gains share despite du<0: False
=== V8 contraction with V_i0 != 0 (M1.40) ===
converged in 27 iterations; recovered delta [1.  1.2 1.1 1.3]  true [1.  1.2 1.1 1.3]  max err 2.489120021209601e-13
##### v3b_relutil
s0=0.300: inside s=[0.0382 0.1384 0.4291 0.0942]; exact ds=[ 0.01036 -0.00288 -0.06395  0.02725]; first-order=[ 0.00995 -0.00099 -0.06715  0.02743]; outside 0.3000->0.3292
s0=0.600: inside s=[0.0258 0.0843 0.2267 0.0633]; exact ds=[ 0.00477 -0.00623 -0.04259  0.01307]; first-order=[ 0.00488 -0.00561 -0.04714  0.01388]; outside 0.6000->0.6310
##### v4_gmm_supply
=== V9 concentration (M1.43) ===
concentrated: [ 0.99710269  0.49874218 -0.30093134]  numerical argmin: [ 0.99710268  0.49874218 -0.30093135]  max diff: 6.982678102396278e-09
=== V10 supply with tax wedge (M1.45-47) ===
equilibrium p^s: [8.2392 9.398  8.7146 9.8725]  FOC residual: 1.942890293094024e-16
Jacobian dS/dpc symmetric? max|J-J'| = 8.673617379884035e-19
recovered mc (3.4 direction): [6.  7.  6.5 7.5]  max err 3.552713678800501e-15
recovered mc (transposed)   : [6.058324 6.971355 6.561915 7.482142]  max err 0.061915484479466265
with common kappa, Delta - Delta' max: 8.673617379884035e-19
##### v5_phi0_ident
(piF, param, ||d delta/d theta||, ||within-(d,m,t) part||, ratio)
 6.0 phi0       8.4854    0.1294  0.0153
 6.0 phi_IN    11.5342    1.6907  0.1466
 7.5 phi0       9.4006    0.1187  0.0126
 7.5 phi_IN    12.3525    1.7809  0.1442
 9.0 phi0       9.7440    0.1195  0.0123
 9.0 phi_IN    13.5838    1.9667  0.1448
##### v6_ident_claims
=== V12 (M1.35)(i) ===
heterogeneous w (IQR-like 4.8%-11.4%): scaled singular values [1.40731 0.13954], condition number 10.1
homogeneous w=7.7%: scaled singular values [1.41421 0.     ], condition number 11040614520251846.0
=== V13 nested test (M1.44): two-source belief B = k*z*L + (1-k)*m ===
true gamma*kappa*zeta = 0.648
m uncorrelated with L: (phi^L, phi^K) = [0.6484 0.6447]
m correlated with L  : (phi^L, phi^K) = [0.6599 0.9508]
```

说明：v3_rc_logit 的第一段（V6–V8）在价格量级使外部份额为 0.9965 的设定下运行，只用于导数、加总与收缩映射检验；V7 的结论以 v3b_relutil（外部份额校准到 0.3 与 0.6）为准。V11 中 $\partial\delta/\partial\varphi^0$ 在每个市场内几乎是常数（如 $\pi^F=7.5$ 时 12 个产品取值在 $-2.69$ 到 $-2.83$ 之间），故被 $(d,m,t)$ 固定效应吸收。

## 8.3 代码

### v1_algebra.py（闭式数字与符号代数）

```python
import numpy as np, sympy as sp
r, A = 0.05, 10
Lam = sum(1/(1+r)**a for a in range(1, A+1)); K = 7.5*12000*Lam/100
print(f"Lambda(5%,10)={Lam:.4f}; K^F={K:.1f}; PV {7.0*0.077*K:.0f}")
for pe in (0.55, 1.6): print(pe, round(pe*12000*Lam/100*15))
HH, sales = 490e6, 20e6
for h in (0.5, 0.07):
    M = h*HH/12; s_in = sales/12/M; print(h, round(M/1e6,2), round(s_in,3), round(1-s_in,3))
a,K,phN,phX,LN,w,wb,W = sp.symbols('alpha K phi_N phi_X L_N w wbar W', positive=True)
LX = LN + W; du = -a*K*(phX*LX - phN*LN)
print(sp.simplify(du-(-a*K*phX*W - a*K*(phX-phN)*LN))==0, sp.simplify(du+a*K*(phN*W+(phX-phN)*LX))==0)
du_w = du.subs(W, w*LN)
print(sp.simplify(du_w.subs(phX,phN)+a*K*phN*w*LN)==0,
      sp.simplify(du_w.subs(phX,phN/(1+wb))+a*K*phN*LN*(w-wb)/(1+wb))==0)
zN,zX = sp.symbols('zeta_N zeta_X', positive=True)
print(sp.simplify(((zX*(1+w)*LN)/(zN*LN)).subs(zX, zN/(1+wb))))
p,G,phi = sp.symbols('p G phi'); u = -a*(p+phi*G); print(sp.simplify(sp.diff(u,G)/sp.diff(u,p)))
Wl,rho = sp.symbols('W rho_c', positive=True); print(sp.simplify(sp.diff(sp.log(Wl**(-rho)),Wl)*Wl))
ps,tc,tv,tp = sp.symbols('p_s t_c t_v t_p', positive=True)
Pret = ps*(1+tc)*(1+tv); pc = Pret + tp*Pret/(1+tv)
print(sp.simplify(pc - ps*(1+tc)*(1+tv+tp))==0, sp.factor(sp.diff(pc,ps)))
print(sp.simplify(sp.diff(Pret*(1+tv+tp)/(1+tv),ps)-(1+tc)*(1+tv+tp))==0)
UF,KF,KE,LFCD,LFCS,LECD = sp.symbols('UF K_F K_E L_FCD L_FCS L_ECD')
print(sp.expand(sp.diff(KF*(UF*LFCD+(1-UF)*LFCS)+KE*UF*LECD, UF)))
```

### v2_range_uf.py（$UF$、$A(R)$、交叉偏导、贝叶斯收缩）

```python
import numpy as np
from scipy import stats, integrate
Dday = stats.lognorm(s=0.7, scale=35.0); ht = 0.8
UF = lambda R: ht*integrate.quad(lambda x: Dday.sf(x), 0, R)[0]/Dday.mean()
for R in (30.,60.,100.):
    h=1e-4; print(R, (UF(R+h)-UF(R-h))/(2*h), ht*Dday.sf(R)/Dday.mean())
Dl = stats.lognorm(s=0.6, scale=250.0); n=6.0
A = lambda R: n*integrate.quad(lambda D:(D-R)*Dl.pdf(D), R, np.inf)[0]
for R in (300.,450.,600.):
    h=1e-2; print(R,(A(R+h)-A(R-h))/(2*h),-n*Dl.sf(R),(A(R+h)-2*A(R)+A(R-h))/h**2,n*Dl.pdf(R))
eta,kap = 0.02,0.5; chi = lambda N: N**(-kap); u = lambda R,N: -eta*chi(N)*A(R)
R0,N0,h = 400.,1.3,1e-3
print((u(R0+h,N0+h)-u(R0+h,N0-h)-u(R0-h,N0+h)+u(R0-h,N0-h))/(4*h*h), eta*(-kap/N0*chi(N0))*n*Dl.sf(R0))
n=20; sq2=np.array([.04,.04]); se2=np.array([.04,4.]); rb=np.array([.3,.3]); om=np.array([.5,.5])
lam=n*sq2/(n*sq2+se2); lam_all=n*(om**2*sq2).sum()/(n*(om**2*sq2).sum()+(om**2*se2).sum())
print(lam, (om*lam*rb).sum(), lam_all, lam_all*(om*rb).sum())
rng=np.random.default_rng(1); S=400000
q=rng.normal(0,np.sqrt(sq2),(S,2)); rbar=q+rng.normal(0,np.sqrt(se2/n),(S,2)); target=(om*q).sum(1)
print(np.linalg.lstsq(np.c_[np.ones(S),rbar],target,rcond=None)[0][1:], np.polyfit((om*rbar).sum(1),target,1)[0])
```

### v3b_relutil.py（异质 RC logit 中的相对效用规则，外部份额校准）

```python
import numpy as np
rng=np.random.default_rng(7); NS=40000
VKT=np.exp(rng.normal(np.log(12000),0.5,NS)); alpha=np.exp(rng.normal(np.log(0.10),0.3,NS))
o=(rng.uniform(size=NS)<0.6).astype(float); K=7.5*VKT*6/100/1000; KE=0.55*VKT*6/100/1000
phi=np.array([0.8,0.8,0.8,0.6]); L=np.array([5.0,6.5,8.0,15.0]); p=np.array([140.,120.,100.,160.])
base=np.array([1.0,1.2,1.1,1.3]); Km=np.c_[K,K,K,KE]; V0=-alpha*o*0.8*K*8.5
def sh(V,V0):
    m=np.maximum(V.max(1),V0); eV=np.exp(V-m[:,None]); e0=np.exp(V0-m); D=e0+eV.sum(1); return eV/D[:,None], e0/D
V_of=lambda c:(base+c)[None,:]-alpha[:,None]*(p[None,:]+phi[None,:]*Km*L[None,:])
def calib(t):
    lo,hi=-30,60
    for _ in range(80):
        mid=(lo+hi)/2; lo,hi=((mid,hi) if sh(V_of(mid),V0)[1].mean()>t else (lo,mid))
    return (lo+hi)/2
wedge=np.array([0.02,0.12,0.15,0.0])
for t in (0.3,0.6):
    V=V_of(calib(t)); P1,P01=sh(V,V0); du=-(alpha[:,None]*Km)*(phi*L)[None,:]*wedge[None,:]
    P2,P02=sh(V+du,V0)
    print(P01.mean(), P2.mean(0)-P1.mean(0), (P1*(du-(P1*du).sum(1,keepdims=True))).mean(0), P02.mean())
```

（v3_rc_logit.py 的 V6/V6b/V8 部分与上面同一模型结构：对 $L_j$、$L^R_j$ 做中心差分并与 (M1.36)(M1.39) 的积分式比较，转移率按 (M1.38) 计算；收缩映射按 (M1.40) 迭代至 $\lVert\delta^{h+1}-\delta^h\rVert_\infty<10^{-12}$。）

### v4_gmm_supply.py（浓缩与带税楔子的供给 FOC）

```python
import numpy as np
from scipy.optimize import minimize, fsolve
rng=np.random.default_rng(3)
N=500; X=np.c_[np.ones(N),rng.normal(size=(N,2))]; Z=np.c_[X,rng.normal(size=(N,3))]
delta=X@np.array([1.,0.5,-0.3])+rng.normal(scale=0.2,size=N); Wm=np.linalg.inv(Z.T@Z/N)
th=np.linalg.solve(X.T@Z@Wm@Z.T@X, X.T@Z@Wm@Z.T@delta)
obj=lambda t:((Z.T@(delta-X@t))/N)@Wm@((Z.T@(delta-X@t))/N)
print(th, minimize(obj,np.zeros(3),method='BFGS',options={'gtol':1e-12}).x)
NS=20000; alpha=np.exp(rng.normal(np.log(0.6),0.3,NS)); J=4; firm=np.array([0,0,1,1])
kappa=np.array([(1.05)*(1.23),1.13,(1.05)*(1.23),1.13])      # ICE: (1+tc)(1+tv+tp); NEV: 1+tv
xi=np.array([4.0,4.3,3.8,4.6]); mc=np.array([6.,7.,6.5,7.5]); sub=np.array([0.,0.8,0.,0.8])
def jac(pc):
    V=xi[None,:]-alpha[:,None]*pc[None,:]; m=np.maximum(V.max(1),0); eV=np.exp(V-m[:,None])
    P=eV/(np.exp(-m)+eV.sum(1))[:,None]
    Jm=np.array([[((alpha*P[:,k]*P[:,j]).mean() if k!=j else -(alpha*P[:,k]*(1-P[:,k])).mean())
                  for j in range(J)] for k in range(J)])      # Jm[k,j] = ds_k/dpc_j
    return Jm, P.mean(0)
O=(firm[:,None]==firm[None,:]).astype(float)
foc=lambda ps:(lambda Js:Js[1]+kappa*((O*Js[0].T)@(ps-mc)))(jac(kappa*ps-sub))
ps=fsolve(foc, mc*1.3, xtol=1e-13); Jm,s=jac(kappa*ps-sub)
D34=-(O*(kappa[:,None]*Jm.T))                                # Delta_jk = -O_jk kappa_j ds_k/dpc_j
print(ps-np.linalg.solve(D34,s), ps-np.linalg.solve(D34.T,s))
```

### v5_phi0_ident.py（$\varphi^0$ 在 $(d,m,t)$ 组内留下多少变异）

```python
import numpy as np
rng=np.random.default_rng(11); NS=20000
VKT=np.exp(rng.normal(np.log(12000),0.5,NS)); a=np.exp(rng.normal(np.log(0.10),0.3,NS)); o=(rng.uniform(size=NS)<0.6).astype(float)
Lam=6.0; e0=8.5; nI,nB=8,4; J=nI+nB
L=np.r_[np.linspace(5.0,9.0,nI),np.linspace(12.,18.,nB)]; p=np.r_[np.linspace(150,90,nI),np.linspace(220,140,nB)]
isB=np.r_[np.zeros(nI),np.ones(nB)].astype(bool); phiI,phiB=0.8,0.6
def shares(delta,piF,phi0,phiN=phiI):
    K=piF*VKT*Lam/100/1000; KE=0.55*VKT*Lam/100/1000
    Km=np.where(isB[None,:],KE[:,None],K[:,None]); ph=np.where(isB,phiB,phiN)
    V=delta[None,:]-a[:,None]*(p[None,:]+ph[None,:]*Km*L[None,:]); V0=-a*o*phi0*K*e0
    m=np.maximum(V.max(1),V0); eV=np.exp(V-m[:,None]); e0v=np.exp(V0-m)
    return (eV/(e0v+eV.sum(1))[:,None]).mean(0)
def invert(s,piF,phi0,phiN=phiI):
    d=np.zeros(J)
    for _ in range(3000):
        new=d+np.log(s)-np.log(shares(d,piF,phi0,phiN))
        if np.abs(new-d).max()<1e-12: return new
        d=new
    return d
within=lambda v: np.where(isB, v-v[isB].mean(), v-v[~isB].mean())
for piF in (6.0,7.5,9.0):
    d_true=np.r_[np.full(nI,13.0),np.full(nB,13.5)]+rng.normal(scale=0.3,size=J); s=shares(d_true,piF,0.8); h=1e-3
    g0=(invert(s,piF,0.8+h)-invert(s,piF,0.8-h))/(2*h); gN=(invert(s,piF,0.8,phiI+h)-invert(s,piF,0.8,phiI-h))/(2*h)
    for nm,v in (('phi0',g0),('phi_IN',gN)): print(piF,nm,np.linalg.norm(within(v))/np.linalg.norm(v))
```

### v6_ident_claims.py（(M1.35)(i) 的秩与 (M1.44) 的功效）

```python
import numpy as np
rng=np.random.default_rng(0); n=200; Kt=rng.uniform(5,9,n); LN=rng.uniform(5,9,n)
for wv in (rng.uniform(0.048,0.114,n), np.full(n,0.077)):
    X=np.c_[Kt*(1+wv)*LN, Kt*wv*LN]; sv=np.linalg.svd(X/np.linalg.norm(X,axis=0),compute_uv=False); print(sv, sv[0]/sv[-1])
gam,kap,zet=0.9,0.6,1.2; rng=np.random.default_rng(5); J=300; T=60; Kbar=7.0
Kt=Kbar+rng.normal(0,0.8,T); LNj=rng.uniform(5,9,J); wj=rng.uniform(0.04,0.12,J); Tsw=rng.integers(15,45,J)
def run(m):
    y=[];X=[];g=[]
    for j in range(J):
        for t in range(T):
            Ljt=LNj[j]*(1+wj[j]) if t>=Tsw[j] else LNj[j]
            y.append(-gam*Kt[t]*(kap*zet*Ljt+(1-kap)*m[j])); X.append([Kbar*Ljt,(Kt[t]-Kbar)*Ljt]); g.append(j)
    y=np.array(y); X=np.array(X); g=np.array(g); tt=np.tile(np.arange(T),J)
    def dm(v):
        v=v.copy()
        for _ in range(30): v-=np.bincount(g,v)[g]/np.bincount(g)[g]; v-=np.bincount(tt,v)[tt]/np.bincount(tt)[tt]
        return v
    return -np.linalg.lstsq(np.c_[dm(X[:,0]),dm(X[:,1])],dm(y),rcond=None)[0]   # (phi^L, phi^K), lineage+month FE
print(gam*kap*zet, run(rng.uniform(6,8,J)), run(0.9*LNj+rng.normal(0,0.2,J)))
```

---

# 9 对用户问题的回应核对

| 用户问题（A2 要点） | 稿件回答 | 评价 |
|---|---|---|
| 政策如何加入 BLP、放在效用哪部分 | 经 $\varphi_{d,c}KL$ 进入广义价格；BEV 续航便利项；机械通道进 $p^c$ 与 $mc^{eff}$ | 清楚、正确，是全稿最好的部分 |
| 前 $n$ 期外推后作差以何种形式进入 | 楔子用于定义跳变、无改革反事实、预定工具；效用中是展示标签 | 正确；外推验证跨度 ≤1 年已注明 |
| 燃油经济性/续航单列、算边际效应 | (M1.36)–(M1.39a)，含 PHEV 链式项、WTP、标签转移率 | 正确（全部数值复核） |
| 口碑整体 vs 分项 | 收缩后验；整体分是受限特例并可检验；能耗分项不进口味项 | 有经济学基础，动态内生性已处理 |
| 标签上调后需求升/降的解释 | (M1.34a) 相对效用、情景表、再估值须在完整系统中估 $\varphi_{d,X}\ne\varphi_{d,N}$ | 正确；组层面方向的识别性质需标明（MF4） |
| 新能源替代与电池 | 情景表给两方向条件；容量经续航、密度经质量—电耗—续航与补贴 | 方向正确；BEV 能源成本估值的识别缺口（MF2） |
| 数据为市场—年月—车型 | 产品 = 车型、配置聚合、上险量、市场规模与外部份额 | 适配良好；政策时钟与 PHEV 字段需补（MF8），联合类型分布的数据来源需补（S4） |

SCORE: 81
