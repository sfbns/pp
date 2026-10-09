# M3 第三方审稿报告（第 2 轮）

- **审稿对象**：`deliverables/M3_机制二_短视与资本化.md`（第 2 版，397 行）。本审只读，未修改任何仓库文件。
- **背景（不评分）**：`deliverables/M1_基准BLP模型.md`（第 3 版）、`deliverables/M2_机制一_认证可信度.md`（第 2 版）。
- **审稿人**：独立第三方（blp-referee 配置，显式加载 explicit-load）。
- **日期**：2026-10-09
- **结论**：**中等修改（minor-to-major revision）**。总分 **81/100**，**无致命项**。

---

## 0. 加载与独立性声明

**实际读取的文件**

1. 角色与评分细则：`.claude/agents/blp-referee.md`。
2. 技能：
   - `blp-model-building/SKILL.md`、`references/构造与组合协议.md`（D01–D09，重点是 §4.1 C×I 秩、§5 W）、`references/模块集成图.md`；
   - `references/technical/` 下的 `blp1995_verified_equations.md`、`micro_foundations.md`、`supply_welfare_counterfactual.md`（§5 四条福利轨道，其中 (d) 要求单独规定规范货币边际效用 $\lambda^W$）；
   - `blp-project-professor/SKILL.md`、`five-paper-kernel.md`、`constructive-model-design.md`、`model-formula-ledger.md`（V6-M01/M02）；
   - `structural-model-building/SKILL.md`、`identification_and_claim_ladder.md`、`mechanism_construction_and_theory.md`；
   - `economics-expert-reviewer/SKILL.md`、`review-standard.md`、`evidence-boundaries.md`；`top-journal-hypothesis-packaging/SKILL.md`。
3. 文献卡与项目资料：A05 GRV2018（式 (1)–(5)、表 3、方差分解）、A14 GHVB2021（表 6、表 8、§6.6 精确与近似估值、§10 信任）、A15 RS2021（决策/体验效用）、`dependencies_v6/.../project_china_driving_cycle.md` §10（Li 2026）、`VERIFICATION_LEDGER.md` C1（Li 2026 Table 4 原页核对 PASS）。
4. 用户逐字要求：`MEMORY/00_断点记忆_CHECKPOINT.md` 的 A 节。
5. 复现脚本：`tools/m3_examples.py`（已运行，见 §8）。

**独立性**

- 未读作者自评或采纳说明。
- 先完成本轮独立评审与打分，之后才读第 1 轮报告 `reviews/M3_review_round1.md`，只用于 §7 的逐条核对。
- 评分只依据当前稿件，按细则给出，不参照任何达标线。

---

## 1. 总体评价

第 2 版是一次实质性重写，质量明显提高。

**做得好的地方**

- **命题 M3.0 正确且稳健**：完全资本市场下 $\gamma=1$，与时间偏好无关。本审在 3 期、老练型（sophisticated）准双曲模型中复核，两期能源费用的 $\gamma$ 都是 1.000000（验算 N1），说明该结论并不依赖两期模型的平凡性。
- **四类偏离的微观基础写清了原语**：
  - 现时偏好须配流动性约束；
  - 车贷修正 (M3.4)；
  - 有限注意由成本—收益内生推出 (M3.5)(M3.6)，并给出 $\theta(3-2\theta)$ 偏误与收入梯度；
  - 高隐含贴现率/短考虑期 (M3.7)；
  - 非短视竞争解释另列成表。
- **识别部分守住了主要红线**：
  - 秩结构写清，2 个约化系数对应 3 个结构参数，油价只检验乘法可分；
  - $\gamma$、$UI$、$r^{\ast}$、$S^{\ast}$ 都写明“条件于所选约束”；
  - 对 1 检验；指数命名为“资本化缺口”；$\gamma<1$ 只写“与短视等解释一致”。
- **对用户直觉“降得多 ⇒ 不短视”的回答严谨**：下降幅度识别的是 $\gamma\kappa\zeta$；NEDC 下若 $\zeta>1$，“足额下降”与低资本化相容；理解换尺的理性消费者对平均楔子不反应。
- **福利部分**改用体验效用公式 (M3.15)，并按 $\gamma<1$ 的来源分别给出规范效用；“短视损失”改名为“低估楔子”，并给出二阶损失。
- **代数与数值**：本审用 sympy/numpy 逐式复核，全部展示式代数正确，复现脚本输出与正文数字逐位一致。

**仍需修改的实质问题**（无一触发致命项，但都影响识别与福利结论的准确边界）

1. **§M3.5.3 货币化续航扩展重犯了第 1 轮 F-1 的逻辑**：续航跳变识别的是 $\gamma_{\mathrm B}\mathcal M\kappa^R\zeta^R$ 的乘积，给定 $\mathcal M$ 并不能识别 $\gamma_{\mathrm B}$；该项还缺年金因子，单位不闭合。
2. **秩断言与模型不一致**：“任何矩对 $(\gamma,\kappa,\zeta)$ 的雅可比秩至多为 2”对 (M3.9) 不成立，因为外部选项直接含 $\gamma_{\mathrm I}$。该方向虽弱，但存在；§M3.4.5 也未交代 $\varphi^0$ 是自由估计还是外部固定。
3. **内生注意对标签同样内生**：利害 $\mathcal H$ 随信念的方差变化，全行业的比例标签跳变会像油价一样移动 $\theta^{\ast}$。因此：
   - “给定 $K$ 的标签跳变反应识别 $\theta$ 本身”过强；
   - $\varphi^K/\varphi^L=3-2\theta$ 不是稳健预测；
   - 天真信念下内生注意会表现为 $\varphi_X/\varphi_N>1$，是“再估值”与 $\varsigma_d$ 的竞争解释。
4. **§M3.7 判别表遗漏 M2 的核心机制**：遗漏了精度权重 $\kappa$ 的变化；2 个统计量对 3 个机制，须声明“单机制”维持假设。
5. **福利**：
   - 现时偏好加车贷下，决策价格系数不等于规范货币边际效用；
   - 内部性公式漏了贷款项；
   - (M3.16) 的适用域未声明；
   - 例 F 不含外部选项，与“$P$ 含外部选项”矛盾。计入外部选项后损失量级与二阶近似精度都显著改变。

---

## 2. 八维度得分

| 维度 | 满分 | 得分 | 扣分理由 |
|---|---:|---:|---|
| 经济学基础与原语 | 15 | **13** | 理性基准（命题 M3.0）、流动性约束、车贷、内生注意、高贴现率都从预算约束与随机效用推出，正确。扣分：①“手到口”原语对新车买家的适用性未讨论（GHVB 卡记载新车买家通常不受资本约束；按 (M3.4)，贷款普及会把 $\gamma_{eff}$ 推向 1）；②(M3.5) 中外部选项“$G_0$……被正确感知”含糊，未说明 $\Delta_0=(1-\theta)\alpha G_0$ 还是 $\Delta_0=0$；③现时偏好下 $\varepsilon$ 的时序（当期冲击还是未来服务流）决定规范效用的尺度，未交代；④未认识到标签变化也改变注意利害 $\mathcal H$。 |
| 数学推导正确 | 20 | **16** | (M3.3)–(M3.8)、(M3.10)–(M3.16) 代数全部经 sympy/数值复核无误，命题 M3.0 在 3 期老练型模型中成立，无符号或方向错误。扣分：①秩断言对 (M3.9) 不成立（验算 N2：无固定效应时第三归一化奇异值 0.246；双向固定效应后 0.0021、条件数 668）；②“给定 $K$ 的标签跳变反应识别 $\theta$ 本身”过强（验算 N3：共同比例跳变读数 0.1325，与油价读数 0.1325 相同；5 产品市场中单产品跳变读数 0.089，而 $\theta=0.048$）；③§M3.5.3 识别结论错误且单位不闭合；④车贷下的现时偏好内部性漏 $-\alpha(1-\beta^{PB})\ell p$（sympy）；⑤例 F 与 $\mathcal H$ 的定义域不一致，计入外部选项后二阶近似误差可达 31%（验算 N4）。 |
| BLP/结构模型一致性 | 15 | **12** | $\gamma_d$ 进 $\mu$、属 $\theta_2$；参数化 $\exp$/logit；准差分新息、固定效应结构、生成变量全流程自助法、$\gamma=1$ 为内点检验，均正确。扣分：①估计闭环没有“外部选项”一项：$\varphi^0=\gamma_{\mathrm I}$ 是联合估计还是外部固定未交代，与 M1“$\varphi^0$ 外部固定”的口径不一致；②工程预测工具 $\widehat O^{eng}$ 在控制 $K\cdot L$ 后的相关性未论证（$L$ 本身也是硬件函数，二者可能高度共线），工具 4 与工具 2 实质重复；③需求新息记为 $\epsilon$，与 logit 冲击 $\varepsilon$ 及 M1 v3 的 $\nu$ 不一致；④福利以决策 $\alpha_i$ 作货币尺度，未单列规范 $\lambda^W$。 |
| 新参数的经济学构造与含义 | 10 | **8.5** | 已有经济学定义与单位：$\gamma$（对主观成本的 MRS）、$\beta^{PB}$、$\ell$、$\theta,c,\mathcal H$、$UI$（命名克制）、$r^{\ast}$ 与 $S^{\ast}$（含定义域）、$\pi_\gamma$。扣分：①$\varsigma_d$ 在 §M3.4.5 被称为“注意变化”，但按 §M3.7 它吸收任何制度间变化（显著性、利害、校准误差），命名越级；②$\mathcal M$ 只写“每缺口公里的货币成本”，与年度缺口 $\bar A_i$（km/年）相乘得到的是元/年，不是现值。 |
| 识别论证 | 15 | **11.5** | 已做到：秩逻辑、三种约束、条件化报告、尺度网格、残差方差分解（含中国油价调控机制）、纯电弱识别、联合奇异值、证伪表。扣分：①§M3.5.3 识别过度；②§M3.7 漏 $\kappa$ 通道且未声明单机制假设；③利害驱动的内生注意是 $\varsigma_d$ 与 $\varphi_X/\varphi_N$ 的竞争解释，未列；④约束 1（M2-A）机械施加“已知平均换算”，与 §M3.4.4 的“天真”读法互斥，未点明；⑤P-M3-4 的“低收入城市 $\gamma$ 更低”同样是“现时偏好 + 流动性约束”的预测；P-M3-6 把“双信源信念”和比例性的 $K$ 尺度错误列为拒绝原因，逻辑不对；⑥$\gamma(\pi^F)$ 与动量型（非鞅）油价预期、里程反弹观测等价，未提。 |
| 文献一致性与来源标注 | 10 | **7.5** | [O·卡] 逐项可核：GRV $\gamma=0.91\,(0.18)$、77% 方差份额、尺度不可分；GHVB 0.16–0.39；RS 决策/体验效用；Li 2026 三个数字（核验账本 C1 PASS）。[外] 引用基本贴切：Laibson、Gabaix、DellaVigna、Hausman、ANS 2015、Sallee 2014、Leggett 2002。扣分：①AMT 2014 被概括为“信息政策与燃油价格信号有矫正价值”，与其核心结论不符（内部性下能源税不足，需要对节能耐用品补贴或标准）；②GHVB 附录 D.4 讨论的是产品层的“均值之比 vs 比之均值”（$\widehat{\Delta P}/\overline{\Delta G}$），不是消费者层的 $E[\gamma_i\alpha_i]/E[\alpha_i]$，应写成“同一原理”；③把 $B=\widetilde O$ 称为 GRV、Allcott–Wozny 的隐含假设不准确，二者以官方（或调整后的）评级度量燃油成本，即“评级 = 信念 = 真值”；④GRV 的 0.91 取 $r=6\%$、$S=15$，本文例表取 $5\%$、10 年，同一 $\gamma\rho=8.84$ 在本文尺度下对应 $\gamma=1.145$，应以 $\gamma\Lambda$ 比较；⑤GHVB 0.16–0.39 未注 $r=4\%$；A05/A14 卡中可用的“接近完全估值”证据（BKZ 2013、SWF 2016）未引，文献图景偏向一侧。 |
| 回应用户问题与数据适配 | 10 | **8.5** | 已回答的用户问题：短视怎样放入 BLP、从微观基础推出、可量化指标与共同估计、突变识别什么、“降得多 ⇒ 不短视”的严格纠正、需求上升一侧、续航突变、福利、异质性；对市场—月—车型数据的限制交代诚实。扣分：①“需求上升不可能来自短视”未加“共同 $\gamma$”限定，而本文规格中 $\gamma_d$ 分动力；②续航货币化的回答有误；③未把约束 1 与“平均楔子车型大幅下降”的经验含义连起来：若下降明显，M2-A 被拒绝，只能靠约束 2；④城市层贷款渗透率、教育等 $z_m$ 的可得性被默认。 |
| LaTeX 规范与可读性 | 5 | **4** | PDF 编译成功（13 页），`\tag`、`aligned`、`\boxed`、表格渲染正确，仅 1 张表有 3 处 0.12pt 溢出（可忽略）。扣分：①数学中出现 `*` 共 31 处（27 处行内、4 处独立公式），违反项目排版规则（CLAUDE.md §3），GitHub 渲染有风险；②$\bar A$ 一符两义（最大车龄 vs 期望续航缺口），$\chi(N_{mt})$ 与 M1 v3 的 $\chi(\mathcal C_{mt})$ 不一致，$v_a$（里程衰减）与 $v_j$（后验方差）并存，节号与式号同名（如 §M3.6 与 (M3.6)）。 |
| **合计** | 100 | **81** | 无致命项 |

---

## 3. 致命项

**无。** 逐条对照细则的五类致命项：

- **导数方向或符号错误导致结论反转**：无。全部导数、比较静态、交叉偏导经 sympy 复核无误（验算 V1–V5）。
- **把校准/假设说成已识别**：主规格中没有。§M3.4.3 明写 $\gamma$ 条件于约束 1/2/3，§M3.4.6 明写尺度不可分。
  - §M3.5.3 的“给定外部 $\mathcal M$ 可识别 $\gamma_{\mathrm B}$”属于识别说过头：它遗漏了续航信念映射 $\kappa^R\zeta^R$ 的约束。
  - 但该处位于标明为“货币化扩展”的小节，且已声明依赖外部校准 $\mathcal M$；主规格未依赖它。因此列为最高优先级必须修改项，不按致命项处理。
  - 若第 3 版仍保留该结论，应视为致命。
- **福利公式在不适用条件下使用**：(M3.15) 本身正确（蒙特卡洛核对，验算 N5）。规范货币尺度与 (M3.16) 适用域的问题属于“条件未声明”，正文没有在不适用条件下给出数值结论。列为必须修改项。
- **份额/反演/FOC 核心式错误**：无。
- **完全不回应用户核心问题**：否，回应充分。

---

## 4. 逐式核验摘要

| 式/段 | 结论 | 说明 |
|---|---|---|
| (M3.1) | ✓ | 与 (M1.8) 一致。轻微记号问题：$\Phi_{ij}$ 未除 $\sigma_\varepsilon$，M1 用 $\tilde\Phi$；$p^c$ 与 M1 v3 的 $p_{jmt}$ 不一致。 |
| (M3.2) | ✓ | 对主观成本的 MRS，逐消费者定义。GHVB D.4 的引用须改写（MF-8）。 |
| 命题 M3.0 | ✓ | 两期例 A 与本审 3 期老练型 β–δ（验算 N1）都给出 $\gamma=1.000000$。 |
| (M3.3) | ✓ | $\partial U/\partial E_a\div\partial U/\partial p=\beta^{PB}(\varrho^D)^au'(c_a)/u'(c_0)$；数值 0.4 正确。 |
| (M3.4) | ✓ | $\gamma_{eff}=\beta/(1-\ell+\beta\ell)$，导数 $\beta(1-\beta)/(\cdot)^2$，端点为 $\beta$ 与 1（sympy）。 |
| (M3.5) | ✓ | 二阶展开 $LS-\tfrac12\Delta'[\operatorname{diag}P-PP']\Delta$ 正确。$G_0$ 的处理含糊；例 F 未含外部选项（MF-5）。 |
| (M3.6) | ✓ | $\theta^{\ast}=\mathcal H/(\mathcal H+c)$ 及两个比较静态正确。 |
| (M3.6a) | ✓（代数） | $d(\theta K)/dK=\theta(3-2\theta)$，最大值 9/8。但“标签跳变识别 $\theta$ 本身”过强（MF-3）。 |
| 推论 2 | ✓（偏效应） | 给定 $P$ 时 $\partial\theta^{\ast}/\partial\alpha>0$。$P$ 随 $\alpha$ 变化时，本审数值例中 $d\ln\mathcal H/d\ln\alpha$ 仍在 0.70–1.96 之间为正（验算 v5），宜注明条件。 |
| (M3.7) | ✓ | 定义正确，$r^{\ast}$ 与 $\bar A^{\ast}$ 的分工清楚。 |
| (M3.8) 与表 | ✓ | 独立重算 $\Lambda(5\%,10)=7.7217$、$\bar\gamma=1.2950$、$r^{\ast}$ 六个值、$\gamma\Lambda$ 六个值，全部一致。$dr^{\ast}/d\gamma$ 公式经 sympy 核对。 |
| (M3.9) | 位置 ✓ | 外部选项含 $\gamma_{\mathrm I}$，与秩断言冲突（MF-2）；$\bar A_i$ 一符两义；$\chi(N)$ 记号过时。 |
| (M3.10) | ✓ | 三个导数正确。秩断言须条件化（MF-2）。 |
| (M3.11) | ✓ | 反解与弹性 $-\kappa$ 正确（sympy）。 |
| (M3.12) | ✓ | 天真下 $-\gamma\kappa\zeta W_jE[\alpha_iK_{imt}]$，并说明一般不等于 $\bar\alpha\bar K$。 |
| (M3.13)(M3.14) | ✓ | 符号与 Li 2026 的解读一致（其 NEV 系数作用于 NEV 自身能源成本，见项目 §10）。 |
| (M3.15) | ✓ | 200 万次 EV1 抽样蒙特卡洛 2.0468，公式（含 Euler 常数）2.0482。货币尺度须规范化（MF-5）。 |
| (M3.16) | ✓（代数） | 适用域与外部选项问题见 MF-5。“楔子与损失量级完全不同”是拿不同单位的量作比较（S-9）。 |
| (M3.17) | 可行 | $\varsigma_d$ 命名与竞争解释见 MF-3、S-6。 |
| (M3.18) | 可行 | $\gamma(\pi^F)$ 与动量预期观测等价（S-4）。 |
| §M3.7 表 | ✓（三列偏导） | 缺 $\kappa$ 行（MF-4）。 |
| §M3.5.3 | ✗ | 识别过度、单位不闭合（MF-1）。 |
| §M3.4.4 第 5 点 | 部分 ✓ | 只在共同 $\gamma$ 下成立（MF-6）。 |

---

## 5. 必须修改项

按对结论的影响排序。

### MF-1（§M3.5.3，L286–L289）：货币化续航的识别与单位

**问题一：识别。** 在 (M3.9) 的双信源续航信念下，$B^R=\kappa^R\zeta^R_cL^R+(1-\kappa^R)\widetilde O^R$。货币化项对续航标签的导数（sympy 验算 v4）为

$$
\frac{\partial u}{\partial L^R_{jt}}=\alpha_i\,\gamma_{\mathrm B}\,\mathcal M\,\Lambda^R\,n^{long}_i\Pr\big(D^{long}>T^R\big)\,\kappa^R_c\,\zeta^R_c .
$$

续航跳变识别的是 $\gamma_{\mathrm B}\mathcal M\kappa^R\zeta^R_c$ 这个乘积。给定 $\mathcal M$，仍须固定 $\kappa^R\zeta^R$，才能识别 $\gamma_{\mathrm B}$——这正是 §M3.4.2 已纠正的逻辑，在此复发。

**问题二：单位。** $\bar A_i(\cdot)$ 是年度期望缺口（km/年，见 M1.21、M2.20）。$\mathcal M$ 若是“每缺口公里的货币成本”，则 $\mathcal M\bar A_i$ 是元/年，不能与购价和现值成本相加。

**修改方案**

- 写成 $-\alpha_i\gamma_{\mathrm B}\,\mathcal M\,\Lambda^R\,\bar{\mathcal A}_i(B^R,\Omega^R)$，其中 $\Lambda^R\equiv\sum_aS_a/(1+r)^a$，或把 $\mathcal M$ 定义为“每单位年缺口的现值成本”。
- 把结论改为：在 M1 的识别假设 $\zeta^R_{\mathrm B,N}=1$、且 $\kappa^R$ 受 M2-A/B 型约束（或 $\kappa^R=1$）时，给定 $\mathcal M$ 与 $\Lambda^R$ 可识别 $\gamma_{\mathrm B}$；否则只识别乘积。
- 若要利用缺口函数 $\bar{\mathcal A}$ 的曲率分离 $\zeta^R$ 的水平（M1 §M1.5.2 已指出“原则上进入曲率”），须明写这是函数形式识别。

### MF-2（(M3.9) L181、§M3.4.2 L197、§M3.4.5）：外部选项与秩断言

**问题。** (M3.9) 写的是 $u_{i0}=-\alpha_io_i\gamma_{\mathrm I}K^{F,0}_{imt}\bar e_{0,m}+\varepsilon_{i0}$。外部选项直接依赖 $\gamma_{\mathrm I}$，不经 $(\varphi^L,\varphi^O)$。因此“效用只经两个约化系数依赖于三个结构参数，因此任何矩……秩至多为 2”对本文自己的规格不成立。

本审模拟（异质里程、60% 置换型消费者，验算 N2/v3）：

| 设定 | 归一化奇异值 | 条件数 |
|---|---|---|
| 外部选项系数外部固定，无固定效应 | $[1.465,0.925,0]$ | — |
| 外部选项系数取 $\gamma$，无固定效应 | $[1.462,0.896,0.246]$ | — |
| 外部选项系数取 $\gamma$，双向固定效应 | $[1.409,1.008,0.0021]$ | 668 |

第三方向存在，但在固定效应下很弱。这与 M1 §M1.2.4 的判断一致：只靠函数形式与类型分布识别，“本稿不依赖它”。

**修改方案**

- 秩断言改为：

  > 在外部选项估值率 $\varphi^0$ 外部固定（或不利用外部选项变异）时，能源项对 $(\gamma,\kappa,\zeta)$ 的依赖只经 $(\varphi^L,\varphi^O)$，任何矩的雅可比秩 $\le2$。若令 $\varphi^0=\gamma_{\mathrm I}$，外部选项经 $o_iK_i$ 的类型异质性提供第三个函数形式方向，在 $\xi_{d,m,t}$ 下很弱，基准不依赖。

- §M3.4.5 增加“外部选项”条目，写明以下内容：
  - 基准中 $\varphi^0$ 固定于外部值，或按估得的 $\gamma_{\mathrm I}$ 迭代并报告二者差异；
  - $o_i$ 的来源；
  - 旧车剩余寿命 $\bar A_0$ 的敏感性。

### MF-3（§M3.2.2 L111、P-M3-2、§M3.7）：利害驱动的内生注意

**问题。** $\mathcal H=\alpha^2K^2\operatorname{Var}_P(B)$ 随信念的分布变化。全行业比例跳变 $B\to(1+\bar w)B$ 使 $\operatorname{Var}_P(B)$ 乘 $(1+\bar w)^2$，与 $K\to(1+\bar w)K$ 的作用完全相同。由此有三点后果（验算 N3，天真信念，5 档能耗，$\theta^{\ast}=0.048$）：

1. 共同比例跳变的读数（0.1325）与油价读数（0.1325）相同。因此 $\varphi^K/\varphi^L=3-2\theta$ 只在 $\varphi^L$ 来自“小份额产品的特有跳变”时成立。即使单产品跳变，在份额不小的市场中读数也是 0.089，而非 $\theta=0.048$。
2. 天真信念下，改革提高 $\mathcal H$，使 $\theta_X>\theta_N$：

   $$
   \frac{\varphi_{d,X}}{\varphi_{d,N}}=\frac{\theta_X}{\theta_N}=\frac{\mathcal H_X(\mathcal H_N+c)}{\mathcal H_N(\mathcal H_X+c)},\qquad \frac{\mathcal H_X}{\mathcal H_N}=\frac{\operatorname{Var}_{P}(B_X)}{\operatorname{Var}_{P}(B_N)}\approx(1+\bar w_d)^2 .
   $$

   数值上 $w=7.7\%$ 时比值为 1.14，方向与“已知平均换算”基准 $1/(1+\bar w)=0.929$ 相反。
3. 即使标签格式不变，$\varsigma_d>0$ 也会出现。因此 §M3.7 的“注意上升”至少有两个来源：显著性（$c$ 下降）与利害（$\mathcal H$ 上升）。§M3.2.2 末句“工况切换本身未改变标签格式”不足以排除注意变化。

**修改方案**

- 把“给定 $K$ 的标签跳变反应识别 $\theta$ 本身”改为“对小份额产品的特有标签变化，近似识别 $\theta\kappa\zeta$”。
- P-M3-2 限定为用特有跳变构造的 $\varphi^L$。
- 在 §M3.7 与 P-M3-5 中加入“利害驱动的注意”，其可区分预测是：$\varsigma_d$ 随动力内 $\operatorname{Var}_P(B)$ 的变化而变，并在已知平均换算（$\operatorname{Var}$ 近似不变）下消失。
- 在 M1 (M1.19) 的“天真”检验旁注明：内生注意可使天真信念下 $\varphi_X>\varphi_N$。

### MF-4（§M3.7 判别表，L335–L342）：遗漏精度权重通道

**问题。** (M3.9) 中 $\kappa_{d,c}$ 本就按制度变化（M2 的主机制）。交叉偏导（sympy）为：

$$
\frac{\partial^2u}{\partial K\,\partial\kappa}=-\alpha\gamma(\zeta L-\widetilde O),\qquad
\frac{\partial^2u}{\partial L\,\partial\kappa}=-\alpha\gamma\zeta K,\qquad
\frac{\partial^2u}{\partial\widetilde O\,\partial\kappa}=+\alpha\gamma K .
$$

因此 $\kappa$ 上升使 $\varphi^L$ 上升、$\varphi^O$ 下降，比值也随之改变。进一步：

$$
\Delta\ln\varphi^L=\Delta\ln\gamma+\Delta\ln\zeta+\frac{\Delta\kappa}{\kappa},\qquad
\Delta\ln\varphi^O=\Delta\ln\gamma-\frac{\Delta\kappa}{1-\kappa}.
$$

两个统计量对应三个机制，同时发生时无法分离。例如“注意上升 + $\kappa_N$ 下降”可表现为 $\varphi^O$ 上升、比值下降。

**修改方案**

- 表中增加“精度变化 $\kappa$”一行。
- 写明判别所需的“单机制”维持假设；或引入第三个统计量，例如 M2-B 的评论数梯度：它移动 $\kappa$，而不移动 $\gamma$ 与 $\zeta$。
- P-M3-5 相应改写。

### MF-5（§M3.6，L295–L321）：福利的货币尺度、内部性、适用域与外部选项

**(a) 货币尺度。** 现时偏好加车贷下，决策价格系数为 $\alpha^D_i=\alpha_i(1-\ell+\beta^{PB}\ell)$，长期自我的规范货币边际效用为 $\lambda^W_i=\alpha_i$（验算 v4）。(M3.15) 应写成

$$
CS^{E}_i=\frac{1}{\lambda^W_i}\Big[LS\big(V^D_i\big)+\sum_jP_{ij}\big(V^D_i\big)\big(V^N_{ij}-V^D_{ij}\big)\Big],
$$

并按来源逐行给出 $\lambda^W$。构造协议 §5 与技术文件 `supply_welfare_counterfactual.md` §5(d) 都要求单独规定规范货币边际效用，“沿用决策价格系数是规范假设，不是估计结果”。

**(b) 内部性漏项。** 现时偏好行在车贷下应为

$$
V^N_{ij}-V^D_{ij}=(1-\beta^{PB})\Big(\tilde\Phi^{LR}_{ij}-\alpha_i\widehat{PVE}_{ij}-\alpha_i\,\ell\,p^c_{jmt}\Big).
$$

表中只给出 $\ell=0$ 的情形，与本文自己引入的 (M3.4) 不一致（sympy 显示漏项为 $\alpha\ell p(\beta-1)$）。

**(c) (M3.16) 的适用域。** 它由 (M3.5) 推出，前提是“规范效用 = 完全资本化、决策只差 $(1-\gamma)\alpha G$”。

- 适用于：有限注意（未扣注意成本）与纯低估。
- 不适用于：现时偏好（服务流与贷款项同样被扭曲）、信贷约束（无内部性）。
- 理性注意下的净损失应扣除节省的注意成本 $\tfrac12c\theta^2$。

须逐项写明。

**(d) 外部选项。** (M3.5) 写“$P$ 含外部选项”，例 F 却只有 5 款车。本审计入外部选项（验算 N4，$\gamma=0.6$）：

| 情形 | 精确损失（元/人） | 二阶近似（元/人） |
|---|---:|---:|
| 仅内部选项（例 F） | 248.1 | 240.6 |
| $s_0=0.92$，首购者 $G_0=0$ | 617.5 | 425.6（误差 31%） |
| $s_0=0.92$，置换者 $G_0\approx$ 旧车成本 | 46.8 | 39.1 |
| $s_0=0.5$，$G_0=0$ | 1514.4 | 1500.6 |

量级取决于外部选项与 $o_i$ 构成，且广延边际（买还是不买）的扭曲可能占主导。

**修改方案**

- 明确 $\Delta_0=(1-\theta)\alpha G_0$：统一不注意，与 $\varphi^0=\gamma_{\mathrm I}$ 一致。
- 按 (M1.7) 的 $o_i$ 混合重算例 F，分报内部边际与广延边际。
- 说明二阶近似在外部份额高时可能失准。
- 另作建议（S-2）：说明现时偏好下 $\varepsilon$ 是当期冲击还是未来服务流；后者会使规范效用的尺度变为 $1/\beta^{PB}$。

### MF-6（§M3.4.4 第 4、5 点，L236–L237）：对用户问题的两处限定

**问题一：“需求上升不可能来自短视”只在共同 $\gamma$ 下成立。** 本文规格中 $\gamma_d$ 分动力，此时

$$
\Delta s_j\approx-\gamma_{d(j)}\Delta B_j\int\alpha_iK^{d(j)}_iP_{ij}(1-P_{ij})\,dF+\sum_{k\ne j}\gamma_{d(k)}\Delta B_k\int\alpha_iK^{d(k)}_iP_{ij}P_{ik}\,dF .
$$

当 $\Delta B_j>0$ 时，符号取决于 $\gamma_{d(k)}/\gamma_{d(j)}$。例如燃油车自身资本化低、插混资本化高，且插混标签恶化更多时，燃油车份额可以上升。若 $\gamma_i$ 与替代格局相关，聚合符号也可能改变。

修改方案：改为“在共同 $\gamma$ 下……；动力间 $\gamma_d$ 不同时，相对短视会改变跨动力权重，但不能单独使孤立产品的份额上升”，与 §M3.5.1 末句对齐。

**问题二：约束 1 与“天真”读法互斥。** 约束 1（M2-A）按工况校准 $\widehat\zeta_{d,c}$，同硬件下 $\widehat\zeta_X\approx\widehat\zeta_N/(1+\bar w)$，即机械施加“已知平均换算”。因此：

- 若平均楔子车型需求明显下降，数据拒绝 M2-A，只能用约束 2（或 3）谈 $\gamma$；
- 在约束 1 下，天真读法本身不可检验。

这正是用户问题的关键连接点，须在第 4 点写明。

### MF-7（§M3.4.5 工具，L243–L251）：工程预测工具的相关性

**问题。** $\widehat O^{eng}_j$ 是硬件函数，标签 $L_j$ 很大程度上也是硬件函数。在谱系固定效应下，$\bar K\widehat O^{eng}$ 与 $\bar KL$ 的剩余变异都来自“油价 × 截面”，可能高度共线。M1 记载楔子对属性的 $R^2\approx0.30$，说明“道路—测试差”可由硬件预测的部分有限。

**修改方案**

- 报告给定 $\bar KL$ 与固定效应后，$\bar K\widetilde O$ 对 $\bar K\widehat O^{eng}$ 的偏 F（Sanderson–Windmeijer）。
- 改用“工程预测差距”工具 $\bar K_{mt}\big(\widehat O^{eng}_j-\widehat\zeta^0_{d,c}L_j\big)$。可用的硬件特征包括小排量涡轮、启停、CVT、风阻、车重等，它们在道路与测试中表现不同。
- 加入制度特定工具 $S_{jt}\times\bar K_{mt}\widehat W_j(H_{j,pre})$，以识别 $\varphi^L_{d,X}$ 与 $\varphi^L_{d,N}$ 的差别。
- 工具 4（油价 × 工程预测）与工具 2 实质重复，应删除或说明差别（全国油价 vs 市场油价）。

### MF-8（文献标注）

1. **L321 AMT（2014）**：改写为“内部性存在时，仅靠能源税不足以纠正耐用品选择，需对节能产品补贴或施加标准（AMT 2014）”。不宜写“燃油价格信号有矫正价值”。
2. **L48 GHVB 附录 D.4**：改为“与 GHVB（2021）附录 D.4 在产品层量化的‘均值之比 ≠ 比之均值’偏误同一原理”。
3. **L219 约束 3**：GRV 与 Allcott–Wozny 以官方（或调整后）评级度量燃油成本，其隐含假设是“评级 = 信念 = 真值”，在本文记号中接近 $\kappa\zeta=1$（M2-C(i)），而不是 $B=\widetilde O$。另须指出：约束 3（$\kappa=0$）下标签跳变应无效应，这是可证伪推论。
4. **L165 GRV**：注明 $r=6\%$、$S=15$，并以无尺度的 $\gamma\rho=8.84$ 年与本文 $\gamma\Lambda$ 比较。在本文 $(5\%,10)$ 尺度下，同一 $\gamma\rho$ 对应 $\gamma=1.145$（验算 v4）。GHVB 注 $r=4\%$。
5. **补充“接近完全估值”的证据**：BKZ（2013）、Sallee–West–Fan（2016），可经 A05/A14 卡转述，标 [外]，使文献对照不偏向一侧。

### MF-9（记号与排版）

- 把 31 处 `^*` 改为 `^{\ast}`，包括 $r^{\ast}$、$S^{\ast}$、$\theta^{\ast}$、$\bar A^{\ast}$、$j^{\ast}$、$u^{\ast}$，以符合 CLAUDE.md §3 并消除 GitHub 强调符冲突。
- 期望续航缺口改名（如 $\bar{\mathcal A}_i$），与最大车龄 $\bar A$ 区分。
- $\chi(N_{mt})\to\chi(\mathcal C_{mt})$；需求新息 $\epsilon_{jmt}\to\nu_{jmt}$；$p^c$ 与 M1 v3 的 $p_{jmt}$ 统一。
- $v_a$（里程衰减）与 $v_j$（后验方差）择一改名；节号与式号区分（如式号用 (M3-1) 或节号用 §3.1）。

### MF-10（§M3.9 判别表）

- **P-M3-4**：“低收入城市 $\gamma$ 更低”的支持列应同时写“信贷约束”与“现时偏好 + 流动性约束”。二者靠 P-M3-3 的外生信贷冲击区分。
- **P-M3-6**：删去“双信源信念”（这是 M3 的维持模型，不是拒绝原因）与“$K$ 尺度错误”（比例性尺度错误同乘 $\varphi^K$ 与 $\varphi^L$，不导致拒绝）。保留并补充非比例误设：油价预期非鞅、里程反弹、利害驱动的内生注意（MF-3）、遗漏外部选项油费。

---

## 6. 建议项

- **S-1 现时偏好渠道的相关性**：讨论新车买家的流动性约束。贷款普及时，按 (M3.4) $\gamma_{eff}\to1$，现时偏好对新车 $\gamma$ 的贡献可能很小；可用车贷渗透率的外部数据给出 $\gamma_{eff}$ 的可行区间。
- **S-2 现时偏好下 $\varepsilon$ 的时序**：若 $\varepsilon$ 属于未来服务流，规范效用为 $(V^D+\varepsilon+\alpha^Dp\ldots)/\beta^{PB}$ 型重标，logsum 尺度改变；若属于当期冲击，则 (M3.15) 原式适用。
- **S-3 推论 2 的条件**：写明“给定选择概率，或 $\operatorname{Var}_P$ 对 $\alpha$ 的弹性大于 $-2$”。本审数值例中该条件成立（验算 v5）。
- **S-4 (M3.18)(i)**：$\gamma$ 随油价水平变化，与动量型（非鞅）油价预期、里程对油价的反应观测等价。建议用期货价或调查预期构造 $K$ 作稳健性（GRV 用过期货价）。
- **S-5 P-M3-1 的功效**：除对 1 检验外，报告 $\gamma$ 的置信区间与可检测的最小偏离；不能拒绝 1 时应说“精度不足以排除经济上重要的低估”，而不是“无低估”。
- **S-6 命名**：$\varsigma_d$ 称“制度间资本化变化”，不称“注意变化”。
- **S-7 小型蒙特卡洛**（第 1 轮 S-10 未采纳）：约束 1 下 $(\gamma,\kappa)$ 可恢复；$\widehat\zeta$ 有偏时，$\gamma$ 的相对偏差约为 $-\kappa$ 乘以 $\widehat\zeta$ 的相对偏差；不施加约束时，脊线不可识别。
- **S-8 L234 的措辞**：“NEDC 下 $\zeta>1$（消费者知道旧标签低报）”应改为假设句。
- **S-9 量级比较**：楔子（元/(L/100km)）与损失（元/人）单位不同，比较时应换算到同一口径，例如“楔子 × 选择集内能耗离散度”。
- **S-10 利用第二个时钟**：2024 年标签格式改革（GB 22757.1/.2—2023，M1 §M1.8.1）是检验处理成本 $c$（格式/显著性）的天然机会，可直接用于区分 MF-3 的两个注意来源。
- **S-11 里程分布口径**：继承 M1 的说明，写明里程分布是购车者条件分布还是潜在买家总体分布（GRV 在线附录 A.3 的映射问题）。
- **S-12 异质 $\gamma$ 的报告**：$\pi_\gamma\ne0$ 时，$UI$、$r^{\ast}$、$S^{\ast}$ 逐抽样计算后再汇总，不用平均 $\gamma$ 代入。

---

## 7. 对第 1 轮意见的逐条核对

| 第 1 轮条目 | 状态 | 依据（第 2 版位置） |
|---|---|---|
| **F-1** 油价不能分离 $\gamma$；“大幅下降 ⇒ 不短视”推断错误 | **已解决（原位置）**；同类逻辑在新位置复发 | §M3.4.2 写清秩结构（2 系数对 3 参数），油价只检验乘法可分；§M3.4.3 列三种约束并条件化；§M3.4.4 五点严格回答。但 §M3.5.3 货币化续航重犯“跳变识别 $\gamma$”的逻辑（本轮 MF-1）。 |
| **F-2** 注意 vs 外溢交叉偏导写错 | **已解决** | §M3.7 三列偏导经 sympy 复核正确，判别统计量改为 $\varphi^O$ 与 $\varphi^L/\varphi^O$。新问题是遗漏 $\kappa$ 通道（MF-4）。 |
| M-1 重写 §M3.4.2–§M3.4.3 | **已解决** | 同 F-1；(M3.11) 给出弹性 $-\kappa$ 与 $\widehat\zeta$ 网格要求。 |
| M-2 重写溢出检验与 P-M3-5 | **已解决** | §M3.7、P-M3-5。 |
| M-3 现时偏好原语 | **已解决** | 命题 M3.0、§M3.2.1 流动性约束、车贷作为专用信贷、ANS 2015 证据、$\ell$ 内生、贴息进入 $p^c$。遗留：新车买家适用性（S-1）。 |
| M-4 内生注意 | **基本解决** | as-if 基准加结构化扩展，$\theta(3-2\theta)$，P-M3-2/P-M3-6 已改，反事实重解 $\theta^{\ast}$。新问题：标签跳变同样移动 $\mathcal H$（MF-3）。 |
| M-5 福利 | **部分解决** | (M3.15)、按来源的规范效用表、“低估楔子”改名、(M3.16)、Allcott/Sallee/AMT 引用均已补。遗留：货币尺度 $\lambda^W$、车贷内部性漏项、(M3.16) 适用域、例 F 缺外部选项（MF-5）。 |
| M-6 BLP 估计闭环 | **部分解决** | 参数化、矩、五类工具、外生性、全流程自助法、$\delta\to\mu$ 均已补；外部选项已写入 (M3.9)。遗留：闭环中 $\varphi^0$ 的处理及其与秩断言的冲突（MF-2）、工具相关性（MF-7）。 |
| M-7 命名与竞争解释 | **已解决** | “资本化缺口指数”；§M3.2.4 竞争解释表含风险、残值/持有期、里程误感知、油价预期、尺度、外部选项。 |
| M-8 $r^{\ast}$、$S^{\ast}$ 定义域，$\gamma\Lambda$ | **已解决** | §M3.3 第 1–3 条；表含 $\gamma=1.17$、$1.30$。 |
| M-9 来源标注 | **已解决** | [外] 标签已改；车贷渗透率“本文不作经验断言”；GRV 77%；Li 差值。本轮另有引用准确性问题（MF-8）。 |
| M-10 LaTeX | **基本解决** | 70pt 溢出已消除（仅剩 3×0.12pt）；$\mathcal H$、$\beta^{PB}$、$\varrho^D$、$\mathcal W^E$ 已统一。遗留：节号与式号同名、$v$ 冲突；新增 $\bar A$ 两义与 31 处 `^*`（MF-9）。 |
| S-1 回答“需求反而增加” | **已采纳**，但表述过强 | §M3.4.4 第 5 点、§M3.5.1；缺“共同 $\gamma$”限定（MF-6）。 |
| S-2 续航突变对短视 | **已采纳**，扩展部分有误 | §M3.5.3（MF-1）。 |
| S-3 收入梯度的反向预测 | **已采纳** | 推论 2、P-M3-4。 |
| S-4 外生信贷冲击 | **已采纳** | P-M3-3。 |
| S-5 里程分布口径 | **未在 M3 处理** | M1 §M1.3.1 有说明，可接受（S-11）。 |
| S-6 $\psi_{i,d}$ 与 $VKT_i$ 相关 | **已采纳** | §M3.4.6 第 3 条。 |
| S-7 逐抽样比率 | **已采纳** | (M3.2) 逐消费者定义；GHVB 归属须改写（MF-8）。 |
| S-8 二阶近似精度 | **已采纳**，但只覆盖内部选项 | 例 F（MF-5(d)）。 |
| S-9 中国油价机制与残差方差分解 | **已采纳** | §M3.4.6 第 2 条。 |
| S-10 约束 1 下的蒙特卡洛 | **未采纳** | 本轮 S-7。 |

---

## 8. 验算记录

**环境与命令**

- `python3 -I tools/m3_examples.py`：输出与正文 §M3.11 的例 A–F 逐位一致。
- `bash tools/build_pdf.sh deliverables/M3_机制二_短视与资本化.md <scratchpad>/review_M3_r2.pdf`：成功，13 页。
- `bash tools/check_overfull.sh ...`：只有 3 处 0.11597pt 溢出，位于同一张表（可忽略）。
- `pdftoppm -r 70` 转图后目检第 3、4、7、10、11 页：中文、`\tag`、`aligned`、`\boxed`、表格均正确。
- 本审脚本存于 scratchpad 的 `verify/`，全部以 `python3 -I` 运行。

### 8.1 符号验算（v1_symbolic.py）

```python
import sympy as sp
b,l=sp.symbols('beta ell',positive=True); g=b/(1-l+b*l)
print(sp.simplify(sp.diff(g,l)-b*(1-b)/(1-l+b*l)**2)==0, sp.simplify(g.subs(l,0)), sp.simplify(g.subs(l,1)))
H,c,th,A,K=sp.symbols('H c theta A K',positive=True)
ts=sp.solve(sp.diff(sp.Rational(1,2)*(1-th)**2*H+sp.Rational(1,2)*c*th**2,th),th)[0]
thK=A*K**2/(A*K**2+c)
print(ts, sp.simplify(sp.diff(ts,H)), sp.simplify(sp.diff(ts,c)),
      sp.simplify(sp.diff(thK,K)-(2/K)*thK*(1-thK)), sp.simplify(sp.diff(thK*K,K)-thK*(3-2*thK)),
      sp.maximum(th*(3-2*th),th,sp.Interval(0,1)))
gm,ka,ze,zh=sp.symbols('gamma kappa zeta zetahat',positive=True)
phiL=gm*ka*ze; phiO=gm*(1-ka); gh=phiL/zh+phiO; kh=(phiL/zh)/(phiL/zh+phiO)
print(sp.simplify(gh.subs(zh,ze)), sp.simplify(kh.subs(zh,ze)), sp.simplify((sp.diff(gh,zh)*zh/gh).subs(zh,ze)))
print(sp.Matrix([phiL,phiO]).jacobian([gm,ka,ze]).rank(), sp.Matrix([gm*ze]).jacobian([gm,ze]).rank())
al,KK,L,O=sp.symbols('alpha K L O',positive=True); u=-al*gm*KK*(ka*ze*L+(1-ka)*O)
for p in (gm,ze,ka): print(p, sp.factor(sp.diff(u,KK,p)), sp.factor(sp.diff(u,L,p)), sp.factor(sp.diff(u,O,p)))
```

输出：

```
True beta 1
theta* = H/(H + c); dtheta/dH = c/(H + c)**2 ; dtheta/dc = -H/(H + c)**2
dtheta/dK - (2/K)theta(1-theta) = 0 ; d(theta K)/dK - theta(3-2theta) = 0 ; max = 9/8
gamma_hat = gamma ; kappa_hat = kappa ; dln gamma_hat/dln zetahat = -kappa
reparametrization rank (gamma,kappa,zeta) -> (phiL,phiO): 2 ; kappa=1 rank (gamma,zeta): 1
gamma : -alpha*(L*kappa*zeta - O*kappa + O) | -K*alpha*kappa*zeta | K*alpha*(kappa - 1)
zeta  : -L*alpha*gamma*kappa | -K*alpha*gamma*kappa | 0
kappa : -alpha*gamma*(L*zeta - O) | -K*alpha*gamma*zeta | K*alpha*gamma
d ln phiL/d ln gamma = 1, d ln phiO/d ln gamma = 1 ; zeta: 1, 0 ; kappa: 1/kappa, 1/(kappa-1)
dr*/dgamma = Lambda(r)/dLambda(r*)/dr*: True ; 0.77*1.3 = 1.001
```

### 8.2 数值验算（v2_numeric.py 摘要）

```python
# N1: 3 期老练型 beta-delta、完全资本市场、log 效用：自我1 消费 Y1/(1+beta*d)，自我0 最优化
# N2: 异质里程 + 60% 置换型；外部选项系数取 gamma 与外部固定 0.9 两种；对数份额对 (gamma,kappa,zeta) 的数值雅可比
# N3: theta* = H/(H+c)，H = alpha^2 K^2 Var_P(B)；比较油价、共同比例标签跳变、单产品跳变三种读数
# N4: 体验效用精确损失与二阶近似；分别不含外部选项、首购者 G0=0（s0=0.92、0.5）、置换者 G0=旧车成本
# N5: 200 万次 Gumbel 抽样蒙特卡洛核对 (M3.15)
```

输出：

```
N1 gamma via E1: 1.000000; via E2: 1.000000
N2 outside option fixed phi0=0.9: normalized SV = [1.46451 0.92477 0.     ]
N2 outside option tied to gamma : normalized SV = [1.46174 0.8959  0.24634]
N3 theta* = 0.0477; fuel-price reading = 0.1325 (local theta(3-2theta)=0.1386, gap because P also moves)
N3 common proportional label-jump reading = 0.1325 ; idiosyncratic single-product reading = 0.0894
N3 naive common jump w=7.7%: theta 0.0477 -> 0.0544; phi_X/phi_N = 1.1395 (known-average-conversion benchmark 0.9285)
N4 inside only            gamma=0.9: 15.17 / 15.03 ; gamma=0.6: 248.09 / 240.55
N4 s0=0.92, G0=0          gamma=0.9: 29.22 / 26.60 ; gamma=0.6: 617.51 / 425.61
N4 s0=0.92, G0=old car    gamma=0.9:  2.55 /  2.44 ; gamma=0.6:  46.79 /  39.10
N4 s0=0.5,  G0=0          gamma=0.9: 94.75 / 93.79 ; gamma=0.6: 1514.38 / 1500.59
N5 MC = 2.0468; formula (incl. Euler const) = 2.0482
```

### 8.3 固定效应下的秩（v3_rank_fe.py）

60 个月、12 个车型、600 个类型；对数份额做“月 × 产品”双向去均值后求雅可比。

```
two-way FE, outside phi0 fixed   : SV=[1.40873 1.00772 0.     ], cond=1.17e8
two-way FE, outside tied to gamma: SV=[1.40873 1.00771 0.00211], cond=668.3
```

### 8.4 续航货币化、车贷内部性、$r^{\ast}$ 表、GRV 尺度（v4_more.py）

```
du/dL^R = -Mcal*alpha*gamma_B*kappa_R*zeta_R*Abar'(kappa_R*zeta_R*L_R + (1-kappa_R)*O_R)
V^N - V^D = (beta - 1)*(PVE*alpha - Phi + alpha*ell*p)   -> table formula misses alpha*ell*p*(beta-1)
decision price coefficient alpha' = alpha*(beta*ell - ell + 1); normative = alpha
Lambda=7.7217, gamma_bar=1.2950; r*: 41.86% 17.15% 7.23% 5.00% 1.89% -0.07%; gamma*Lambda: 2.32 4.63 6.95 7.72 9.03 10.04
rho(6%,15)=9.712; GRV gamma*rho=8.84 -> gamma=0.910; same gamma*rho under (5%,10): gamma=1.145
```

### 8.5 收入梯度（v5_income_gradient.py）

5 款车，节能车更贵；$P$ 随 $\alpha$ 变化。

```
alpha*150000 :   1      2      5      10     20     40     80
dlnH/dlnalpha: 1.956  1.890  1.640  1.314  1.096  0.999  0.695   (始终为正)
theta*       : 0.004  0.016  0.075  0.184  0.340  0.514  0.665
```

### 8.6 复现脚本输出（tools/m3_examples.py）

```
A: perfect capital market gamma = 1.000000; hand-to-mouth (log) gamma = 0.400000
B: beta=0.5 -> 0.500 0.588 0.667 0.833 1.000; beta=0.7 -> 0.700 0.769 0.824 0.921 1.000
C: Lambda(5%,10)=7.7217; gamma_bar=1.2950; r* = 41.86/17.15/7.23/5.00/1.89/-0.07 %
D: theta(3-2theta) = 0.720/1.080/1.080
E: SV (gamma,zeta)=[1.414 0]; (gamma,kappa,zeta)=[1.414 1.001 0]; (gamma,kappa)=[1.008 0.992]
F: loss exact 15.17/248.09/772.17 ; 2nd-order 15.03/240.55/736.70 yuan
```

以上全部与正文一致。

**红线说明**：本审验算只证明公式内部自洽与数值复现，不证明任何排除限制成立，也不意味着模型已用真实数据估计过。

SCORE: 81
