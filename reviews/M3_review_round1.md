# M3 第三方审稿报告（第 1 轮）

- **审稿对象**：`deliverables/M3_机制二_短视与资本化.md`（第 1 版，257 行，SHA256 `5549531a…b31b57c17`）。本审未修改该文件。
- **审稿人**：blp_referee（独立第三方，显式加载 explicit-load）
- **日期**：2026-10-08
- **结论**：**主要修改（major revision）**。总分 **62/100**。发现 2 项致命项（触发总分上限 70，本次不起约束作用）。

---

## 0. 加载与独立性声明

**实际用 Read 打开的文件**

1. 角色：`.claude/agents/blp-referee.md`。
2. 技能：
   - `blp-model-building/SKILL.md`；
   - `references/构造与组合协议.md`（重点读 §4.1 D04 C×I 秩、§5 W）；
   - `references/模块集成图.md`（§3 C/I 行、§4 兼容性规则 1、6）；
   - `technical/micro_foundations.md`；
   - `technical/extension_genealogy.md`（D4 GRV、D5 Lu、B1 GHVB、B2 Li、§6 模式 A/G/H、§9 第 10 条）；
   - `blp-project-professor/SKILL.md`、`five-paper-kernel.md`、`constructive-model-design.md`（V6-M01/M02）、`model-formula-ledger.md`；
   - `structural-model-building/references/identification_and_claim_ladder.md`（§2、§7、§9）与 `mechanism_construction_and_theory.md`（§1–§4）。
3. 文献与记忆：
   - 文献卡 A05 GRV2018、A14 GHVB2021、A14b GHVB2019WP、A15 RS2021、A04 HKV2026；
   - 精读卡 P15；
   - `project_china_driving_cycle.md`（§10 Li 2026、§13 写作红线，并通读 §1–§20）。
4. 背景（不评分）：M1、M2 全文，用于核对 $K,T,B,\kappa,\zeta,m,W,\varphi$、M2-A/B/C、(M2.11)–(M2.22) 等记号。
5. 用户原始要求：`MEMORY/00_断点记忆_CHECKPOINT.md` 的 A 节（逐字）。

**独立性**
- 未读作者自评、采纳说明，也未读 `reviews/` 下其他审稿报告。
- 用户逐字提示词（A1）中出现了分数门槛。本审不以其为参照，按角色细则逐项独立打分。

---

## 1. 总分与总体判断

**总分：62 / 100**

**做得好的地方**
- 结构清楚，基本覆盖用户关于“短视”的问题：如何放进效用、可量化指标、与 BLP 共同估计、突变的作用。
- 多数展示式的代数经验算正确：(M3.4)–(M3.6)、(M3.7)(M3.8) 的定义与数值、(M3.10)(M3.11)、(M3.13)–(M3.15)。
- 有两处有价值的推导：(M3.4) 贷款修正；(M3.14)/(M3.15) 关于“共同资本化与纯电自身 $\gamma_B$”的区分。
- 有若干正确的纪律：对 1 而非对 0 检验，承认尺度不可分，不把 $\gamma<1$ 写成“已证明短视”。

**核心问题**：本文最关键的识别论证（§M3.4.2–§M3.4.3“识别三角”“突变到底识别了什么”）存在逻辑错误。
- “油价变化可把 $\gamma$ 从乘积中分离”不成立：比例信念下秩为 1，双信源下秩为 2，结构参数有 3 个。
- “大幅下降 ⇒ $\gamma\kappa\zeta\approx1$ ⇒ 不短视且相信标签”的推断不成立：$\zeta>1$，且在表示不变基准下理性者不反应。
- $\gamma$ 与信任的分离实际完全来自 M2-A 对 $\zeta$ 的校准，却被表述为由“第二类变异”识别。

**另外三项重大问题**
- §M3.6 的“注意上升 vs 信息外溢”判别式交叉偏导写错。
- 现时偏好推导与 M1.2 的完全资本市场原语相矛盾（在作者自己的预算约束下 $\gamma=1$）。
- 有限注意微观基础意味着 $\gamma$ 随油价内生变化，与“用油价识别 $\gamma$”相冲突。

**次要问题**
- M3.0 承诺的福利推导缺失。
- 新非线性参数的矩条件与工具没有给出。
- 两处展示式在 PDF 中被截出版心，多处符号冲突。

---

## 2. 八维度分项得分

| 维度 | 满分 | 得分 | 主要理由 |
|---|---:|---:|---|
| 经济学基础与原语（偏好、预算、时序、信息集） | 15 | **9** | 理性基准与三种来源的思路正确。但 (M3.3) 的 $\gamma=\beta$ 依赖未声明的“无借贷/效用定义在货币流上”，与 M1.2 Fisher 分离矛盾（验算 A2：$\beta=0.5$ 时 $\gamma=1$）。有限注意下 $\gamma$ 内生于 $K,\alpha_i$ 与选择集，与常数 $\gamma_d$ 不一致。现时偏好的长期福利基准忽略了服务流同样被 $\beta$ 折扣。外部选项能源成本缺位。 |
| 数学推导正确 | 20 | **14** | (M3.4)(M3.5)(M3.6)(M3.10)(M3.11)(M3.13)–(M3.15) 均正确；$r^*=17.15\%$、$S^*=4.63$ 正确。扣分点：§M3.6 交叉偏导断言错误；(M3.12)(M3.16) 用 $\delta$ 表示属于 $\mu$ 的对象；离散 $S$ 写成偏导；$r^*$“解唯一”缺定义域；“短视损失”把一阶楔子当福利损失，与作者自己的 (M3.5) 二阶结论矛盾。 |
| BLP/结构模型一致性 | 15 | **10** | $\gamma_d$ 与 $\alpha_iK_{imt}$ 相乘、进 $\mu$、属 $\theta_2$，位置正确。缺：新增非线性参数的矩条件/工具；$m_{j,t-1}$ 的内生性（由滞后销量累积，M2 已提，M3 未继承）；生成变量 $\hat\zeta$、$m$、$K$ 的推断；外部选项在油价识别下的处理；PHEV 多指标信念。 |
| 新参数的经济学构造与含义 | 10 | **7** | $\gamma$ 的 MRS 定义，$r^*$、$S^*$、WTP 的等价表示，$\varsigma_d$、$\gamma_{dm}$ 构造清楚；$\gamma_B$ 的讨论有洞见。扣分：“短视指数”给复合参数冠以心理机制名；“短视损失”误名；$\gamma$ 未对主观成本 $\widehat{PVE}$ 定义；$S^*$ 一符两义。 |
| 识别论证（变异、排除、秩、rival、falsifier） | 15 | **7** | 有尺度敏感性网格、同动力内识别、$\gamma_B$ 弱识别、雅可比 SVD 报告、对 1 检验、证伪表。但识别三角秩不足；分离依赖校准；“大幅下降 ⇒ 不短视”推断错误；P-M3-5 判别式错误；内生注意污染油价识别；竞争解释（风险、残值/持有期、里程误感知、油价预期）未进判别表；贷款比例内生。 |
| 文献一致性与来源标注 | 10 | **6** | GRV 0.91、GHVB 0.16–0.39 与约 3 年回收期、AW 0.76、Li 0.80/1.17（对 1 不显著）的数字正确。扣分：Laibson/Gabaix/DellaVigna/Hausman/Allcott–Wozny 标 [O]/[O·卡]，但本地无对应精读卡；“车贷渗透率约一半 [D]”无来源且标签错；GRV 识别来源描述不完整（77% 来自车型内发动机截面差异）；未报 Li (2026) 差值显著。 |
| 回应用户问题与数据适配（市场—月—车型） | 10 | **6** | 回答了如何放入、可量化指标、共同估计、对需求的作用；外部里程分布与城市层 $z_m$ 的数据适配合理。扣分：对用户直觉的“严格回答”含错误推断；“需求反而增加”一侧未明确回答（$\gamma$ 不能翻转符号）；“续航突变对短视”未回应；M3.0 承诺的福利推导缺失。 |
| LaTeX 规范与可读性 | 5 | **3** | 可编译（pandoc+XeLaTeX，8 页）。但 (M3.5)(M3.9) 各溢出约 70pt，PDF 中右端被截断。符号冲突：$H$、$W$、$\delta$、$\beta$、$S^*$、$v$；§M3.6 与式 (M3.6) 同号。 |
| **合计** | 100 | **62** | 致命项上限 70 不起约束作用 |

---

## 3. 致命项（任一出现总分上限 70）

### F-1 识别核心论证把“校准/假设”表述为“由变异识别”，并含两处推断错误（§M3.4.2–§M3.4.3，L134–L164）

**(a) 油价变化不能把 $\gamma$ 从信念乘积中分离。**

由 (M3.9)，能源成本项为
$$
-\alpha_iK_{imt}\big[a^L L_{jt}+a^R m_{j,t-1}\big],\qquad a^L=\gamma\kappa\zeta,\quad a^R=\gamma(1-\kappa).
$$
效用只通过 $(a^L,a^R)$ 依赖于 $(\gamma,\kappa,\zeta)$，因此任何矩的 Jacobian 对 $(\gamma,\kappa,\zeta)$ 的秩都不超过 2。油价反应
$$
\partial u/\partial K=-\alpha(a^LL+a^Rm)
$$
只是这两个系数的线性组合，不增加秩。
- 验算 F：$(a^L,a^R,\text{油价反应})$ 对 $(\gamma,\kappa,\zeta)$ 的奇异值为 $[8.31,\,1.11,\,0]$。
- 用 40 个月油价变化的模拟 logit 份额验证：双信源下归一化奇异值为 $[1.41,\,1.00,\,0]$。
- M1 比例信念（$\kappa=1$）下，对 $(\gamma,\zeta)$ 的奇异值为 $[1.41,\,0]$，即秩 1。这与作者自己的 (M1.44) 一致：油价与标签反应给出同一个 $\varphi=\gamma\zeta$。

因此以下表述均不成立：
- L144“油价变化……识别‘对信念的资本化’”；
- L164“只有加入油价变化（识别 $\gamma B$）**或**车主实测（识别 $\gamma(1-\kappa)$），才能把 $\gamma$ 从乘积中分离出来”；
- L134 标题“三类变异、三个对象”。

车主实测一途也只给出 $\gamma(1-\kappa)$，与 $\gamma\kappa\zeta$ 合起来仍是 2 个方程 3 个未知数。只有用 M2-A 外部固定 $\hat\zeta$，验算中 $(\gamma,\kappa)$ 才满秩（奇异值 $[1.008,\,0.992]$）。所以 L164“本课题用第二类变异把信任与资本化分开”实为“在 $\zeta$ 按理性怀疑校准的假设下分开”。

这一假设对结论影响很大：$\partial\ln\gamma/\partial\ln\hat\zeta=-\kappa$。若消费者实际的偏差校正不足（$\zeta<\hat\zeta$），会被读成更低的 $\gamma$。也就是说，用户最想区分的“信念 vs 短视”，在这里是被**假设**合并的，而不是被数据区分的。

这属于细则中的“把校准/假设说成已识别”。L150 与 L249 虽有条件性措辞，但 L134–L146 与 L164 的方法贡献表述及“油价识别 $\gamma$”是实质性错误。

**(b) “大幅下降 ⇒ $\gamma\kappa\zeta$ 接近 1 ⇒ 不短视且相信标签同时成立”（L164）在本文自己的参数空间中不成立。**

1. $\zeta$ 是感知真实/标签比（M1 参数定义 3：$\zeta=1.3$ 表示认为真实油耗高 30%），NEDC 下理性怀疑意味着 $\zeta>1$。M2-A 的 $\hat\zeta=\overline{m/L}$ 正是大于 1 的量。取 $\hat\zeta=1.3$、$\kappa=1$、$\gamma=0.77$，即得 $\gamma\kappa\zeta=1.0$。“足额下降”与明显的低资本化完全相容。
2. 在表示不变（RI，M1.20）基准下，验算 I 得
$$
\Delta B_j=\kappa\zeta_0L^N_j\,\frac{w_j-\bar w_d}{1+\bar w_d}.
$$
平均楔子车型的 $\Delta B=0$。即使 $\gamma=\kappa=\zeta=1$，完全理性、理解换尺的消费者也不会因平均楔子减少需求。此时大幅下降更像是天真读数（未意识到换尺）的证据，而不是“理性、不短视”的证据。

由此，用户直觉“下降多 ⇒ 不短视”被作者在错误的条件下背书，结论方向可能反转。

### F-2 §M3.6“注意上升 vs 信息外溢”判别式的交叉偏导写错（L216；P-M3-5，L240）

作者断言：信息外溢“改变信念水平（对 $L$ 的反应不变、需求截距下降）”，注意上升“改变资本化（对油价的反应增强）”。验算 H 的交叉偏导如下：

| 机制 | $\partial^2u/\partial K\,\partial\cdot$ | $\partial^2u/\partial L\,\partial\cdot$ | $\partial^2u/\partial m\,\partial\cdot$ |
|---|---|---|---|
| 注意 $\gamma\uparrow$ | $-\alpha B$ | $-\alpha\kappa\zeta K$ | $-\alpha(1-\kappa)K$ |
| 外溢 $\hat\beta\uparrow$（M2.8 水平式） | $-\alpha\gamma\kappa\neq0$ | $0$ | $0$ |
| 外溢 $\zeta\uparrow$（M2.21/M3.9 比例式，估计所用） | $-\alpha\gamma\kappa L\neq0$ | $-\alpha\gamma\kappa K\neq0$ | $0$ |

由表可得：
- 信息外溢同样使未切换车型的油价敏感度 $|\partial u/\partial K|$ 上升，方向与注意相同。它的效应 $-\alpha_i\gamma\kappa K_{imt}\Delta\hat\beta$ 随 $K_{imt}$ 变化，不是“截距”。
- 在估计所用的比例式下，“对 $L$ 的反应不变”也不成立。
- 按 P-M3-5 的规则，“切换后对油价敏感度上升，且溢出到未切换车型 ⇒ 注意上升”会把信息外溢误判为注意上升。

能区分二者的是车主实测斜率（注意使其上升，外溢不改变它）以及 $a^L/a^R$ 比值（注意下不变，比例式外溢下上升）。这是“导数错误导致机制结论反转”。

---

## 4. 逐式问题清单（式号 / 行号）

**(M3.1) L22–26** ✓ 与 (M1.8)(M1.10) 一致。
- 省略了 M1.8 中的 $-PVR$，未作说明。
- $p_j$ 与 M1 的 $p_{jmt}$ 下标不一致。（轻）

**(M3.2) L28–32** ✓ 理性基准比值为 1。
- 在含信念的决策效用中，应对主观成本定义：$\gamma\equiv\dfrac{\partial u/\partial\widehat{PVE}}{\partial u/\partial p}$，$\widehat{PVE}=KB$。否则信念与资本化在定义层就混在一起。
- $\alpha_i$ 异质时应逐消费者定义比值，避免 GHVB D.4 的“均值之比”问题。（轻—中）

**(M3.3) L40–48**
- 代数在“逐期货币即效用、无借贷、逐期边际效用恒定”下成立（验算 A1：MRS $=\beta\delta$，按现值换算 $\gamma=\beta$）。
- 但 L22 明确以 M1.2–M1.8 为基础，M1.2 是完全资本市场 + Fisher 分离。在该预算约束下，车辆的货币流只经终身财富现值进入，现时偏好不改变 $p$ 与 $PVE$ 的 1:1 权衡，$\gamma\equiv1$（验算 A2：$\beta=0.5$、log 效用，$\gamma=1.000000$）。
- 无借贷且效用凹时 $\gamma=\beta\,u'(c_1)/u'(c_0)$（验算 A3：0.4）。
- 必须显式更换原语（流动性约束/手到口，或窄框架、效用定义在货币流上），并说明“货币流上的现时偏好”经验证据薄弱。（重大）
- L48“服务流的 $\beta$ 折扣被 $\Phi$ 吸收”只对识别成立，对长期福利基准不成立（见 M3.2.4 表）。

**(M3.4) L50–56** 代数正确（验算 B）：
- $\alpha'=\alpha(1-\ell+\beta\ell)$，$\gamma_{eff}=\beta/(1-\ell+\beta\ell)$；
- $\partial\gamma_{eff}/\partial\ell=\beta(1-\beta)/(1-\ell+\beta\ell)^2\ge0$；
- $\ell=0$ 时为 $\beta$，$\ell=1$ 时为 1。

问题：
- (i)“车贷渗透率约一半，[D]”是无来源的经验陈述，不是推导。
- (ii) 贷款需要信贷可得，与 (M3.3) 所需的“无借贷”原语矛盾，应写成“部分受约束”的混合模型。
- (iii) $\ell$ 内生：现时偏好者更偏好分期；0 息/贴息分期本身是价格折让（按市场利率计的还款现值小于 $\ell p$）。
- (iv) $\alpha'$ 随 $\ell$ 变化，但 (M3.17) 只让 $\gamma$ 随贷款渗透率变化。（中）

**(M3.5) L58–69** 正确（验算 C）：$H=\alpha^2G'MG=\alpha^2\mathrm{Var}_P(G)=0.188657$，两式完全相等。

二阶近似的相对误差：
| $\theta$ | 0.99 | 0.9 | 0.6 | 0.3 |
|---|---:|---:|---:|---:|
| 近似相对精确值 | 0.6% | 6% | 高估损失约 26% | 高估损失约 50% |

需写明：
- 尺度归一 $\sigma_\varepsilon=1$（一般有 $\nabla^2LS=M/\sigma$）；
- 方差在含 outside 的全选择集上计算，$G_0=0$ 等于假设外部选项成本被正确感知；
- 近似只对小扭曲成立。

$W(\theta)$ 与 (M3.12) 的楔子 $W_j$ 同名。PDF 中该式右端“$\ge0$”被截断（overfull 70.7pt）。（轻—中）

**(M3.6) L71–77** FOC、SOC、比较静态均正确（验算 D）。

**重大概念问题（内生注意）**：$\theta^*$ 依赖 $H=\alpha_i^2K_{imt}^2\mathrm{Var}_P(B)$，因此 $\gamma_{imt}$ 随油价/里程、$\alpha_i$（收入）与选择集变化，与 (M3.9) 的常数 $\gamma_d$ 不一致。油价同时移动 $K$ 与 $\gamma$：
$$
\frac{d[\gamma(K)K]}{dK}=\gamma(3-2\gamma).
$$
按油价反应读出的“$\gamma$”：
| 真 $\gamma$ | 0.3 | 0.6 | 0.9 |
|---|---:|---:|---:|
| 油价反应读出值 | 0.72 | 1.08 | 1.08 |

后果：
- §M3.4.2 的“油价识别 $\gamma$”与 P-M3-6 在作者自己提出的微观基础下失效。
- 反事实（燃油税等改变 $H$）须重解 $\theta^*$。

另外两点：
- L77“更可信的标签降低 $c$”把 M2 的信任（$\kappa,\zeta$）与处理成本 $c$ 混为一谈，识别上不可分。
- 比较静态遗漏 $\partial\theta^*/\partial\alpha_i>0$（低收入者更注意）。这与信贷约束的收入梯度预测方向相反，是更锐利的判别。

**(M3.7) L79–87** 定义正确。此处 $S^*$ 指“以 $r^*$ 贴现、截断于 $S^*$”，L112 的 $S^*$ 却是“不贴现回收期”，一符两义。（轻）

**§M3.2.4 表 L89–97** 预测列大体正确。福利列有三处问题：
- (i) $\beta$–$\delta$ 下长期基准不只是“$\gamma=1$”。服务流同样被折扣；若服务流全在未来，长期效用为 $U^{LR}=(U^D+\lambda p)/\beta-\lambda p$，内部性是 $(1-\beta)(\Phi^{LR}-PVE)$，而不是 $(1-\beta)PVE$。
- (ii)“只有降低 $c$ 的政策增进福利”过强。需要推导：规划者的信息成本，以及改变利害 $H$ 的政策会改变 $\theta^*$。应引 Sallee (2014)、Allcott–Mullainathan–Taubinsky (2014)。
- (iii) 缺 $\gamma\neq1$ 的竞争来源：风险/不确定性、残值与持有期、里程误感知、油价预期非鞅（构造协议 §4.1，claim ladder §9）。（中—重）

**(M3.8) L101–117** 数值正确（验算 E）：
- $\Lambda(5\%,10)=7.7217$，$0.6\Lambda=4.6330$；
- $r^*=17.15\%$（文中 17.2%；$\Lambda(17.2\%,10)=4.6249$，可接受）；
- $S^*=4.633$；
- delta 方法 $dr^*/d\gamma=\Lambda(r,H)/\partial_r\Lambda(r^*,H)=-0.4599$，与有限差分一致。

问题：
- (i)“短视指数”给复合参数冠以心理机制名，违背 claim ladder §2/§7 与项目 §6“$\chi<1$ 只能写与短视一致”。
- (ii)“解唯一”须加定义域。$\gamma>\Lambda(0,H)/\Lambda(r,H)$（例中 1.295）时 $r^*<0$、$S^*>H$：$\gamma=1.3$ 时 $r^*=-0.07\%$、$S^*=10.04$；$\gamma=1.6$ 时 $r^*=-3.7\%$。作者允许 $\gamma\in[0,2]$，并引用 Li NEV 1.17。
- (iii) $WTP=\gamma K$ 是每单位**信念**油耗的支付意愿；每单位**标签**为 $\gamma\kappa\zeta K$（M3.10）。
- (iv) “与 $K$ 的差即每单位油耗的短视损失”混淆了楔子与福利损失。按作者自己的 (M3.5)，福利损失是 $(1-\gamma)$ 的二阶量（验算 J：$\gamma=0.6$ 时线性楔子 2780 元/(L/100km)，二阶期望损失约 204 元/人，[I]）。
- (v) 标准误未纳入 $\hat\zeta$、$m$、$K$ 的生成误差。

**(M3.9) L121–132** 位置正确：$\gamma_d$ 与 $\alpha_iK_{imt}$ 相乘、进 $\mu$、属 $\theta_2$。

问题：
- (i) PDF 中 $m_{j,t-1}$ 被截断（overfull 69.9pt）。
- (ii) PHEV 的多指标信念（$B^{F,CD},B^{F,CS},B^{E,CD}$ 与 $UF(B^R)$）未写。
- (iii) 续航项不乘 $\gamma$，与“$\beta$ 被 $\eta_i$ 吸收”一致，但应明说：因此续航突变不提供 $\gamma$ 的信息。这正是用户问的“续航里程突变对短视”。
- (iv) 外部选项能源成本缺位。油价是核心识别源，同时改变旧车油费；$K_i$ 异质时 $-\alpha\gamma K_ie_0$ 相当于与里程相关的内部常数随机系数，$\xi_{d,m,t}$ 只吸收其均值。
- (v) “在 $[0,2]$ 内无约束估计”自相矛盾；$\kappa\in(0,1)$ 的参数化未给。
- (vi) 新增非线性参数 $(\gamma\ \text{或}\ a^L,a^R;\ \kappa;\ \varsigma;\ \pi_\gamma)$ 的矩条件与工具未列。$m_{j,t-1}$ 由累积评论构成，依赖滞后销量与 $\xi$；若 $\Delta\xi$ 序列相关，则 $E[K m\,\Delta\xi]\neq0$（M2 §M2.8.2 已提，M3 未继承）。

**(M3.10) L134–146** 三个导数正确（验算 F）。
- “三类变异、三个对象”误导：$\gamma B=a^LL+a^Rm$ 不独立（F-1）。
- “标签跳变只改变 $L$”与 M2 (M2.11) 的三项分解矛盾：切换同时改变 $\kappa_{d,s}$、$\zeta_{d,s}$ 或 $\hat\beta$。在 M2-A 下 $\hat\zeta$ 按工况重校准，跳变识别的是 $\gamma\kappa_1\zeta_1L^X-\gamma\kappa_0\zeta_0L^N$。

**(M3.11) L148–154** 代数正确（sympy：$\gamma=a^L/\hat\zeta+a^R$，$\kappa=a^L/(a^L+a^R\hat\zeta)$）。
- 但它完全依赖 $\hat\zeta$，弹性 $-\kappa$（F-1）。
- L154“油价……对 $\gamma$ 提供额外的过度识别信息”应改为“对乘法可分性 $K\times B$ 提供过度识别检验”。

**(M3.12) L156–164**
- 天真信念下 $\Delta B=\kappa\zeta W$ 正确。
- 写作 $\Delta\delta_j$ 与 M1.29 的 $\delta/\mu$ 划分矛盾：能源项在 $\mu$，$\delta$ 由反演确定且含 $\xi$。平均效用变化应为 $-\gamma\kappa\zeta W_j\,E[\alpha_iK_{imt}]$，一般不等于 $\bar\alpha\bar K$。
- 推断错误见 F-1(b)。
- “天真”与 (M3.11) 的 M2-A 维持假设（按工况重校准 $\zeta$）不一致。

**§M3.4.4 L166–172**
- 第 1 条 ✓。
- 第 2 条：基准 $\gamma_B=\gamma_I$ 下，跨动力的里程分选也进入 $\gamma$ 的识别。若 $\psi_{i,d}$ 与 $VKT_i$ 相关（网约/营运车辆高里程且受 NEV 政策约束），会混淆。
- 第 3 条：给定 $K^E$ 水平，BEV 截面 $L^E$ 差异也能识别 $a^L_B$；弱点主要在 $K^E$ 尺度（家充比例 $h$）的校准，而不仅是电价时序。
- 第 4 条：“$\gamma$ **只**从油价 × 能耗差异的交互识别”与 §M3.4.2（标签跳变、车主实测）及 M1.11（谱系内发动机截面差异）自相矛盾。把 GRV 归为油价交互识别也不完整：GRV 方差分解中 77% 来自燃料类型内发动机差异，二次趋势 <0.01%，同发动机油价变化约 10%。外部选项成本的异质部分不被固定效应吸收。
- 第 5 条 ✓，但雅可比应对全部新参数 $(\gamma_d,\kappa_{d,0},\kappa_{d,1},\varsigma_d,\pi_\gamma)$ 连同价格参数联合报告。

**(M3.13) L180–186** ✓（验算 G）。
- “放大器的倒数”不准确：$\gamma$ 是传导系数，$1-\gamma$ 是衰减，不是倒数。
- 应补一句：$\gamma\ge0$ 只缩放、不翻转 $\Delta V$ 的符号，所以“标签变差、需求上升”不可能由短视解释。这正是用户第二种情形的答案。

**(M3.14) L188–196** ✓。

**(M3.15) L198–202** ✓，是有价值的澄清。建议补充 Li (2026) 的差值 $0.3661\,(0.1124)$ 显著；按 (M3.15)，其含义是“对电费的权重更高”，而不是“更看重节能”。

**(M3.16) L206–214** 参数化可行。
- “$\partial^2\delta/\partial K\partial S$”中 $S$ 离散，应写差分 $\Delta_S(\partial\cdot/\partial K)$；且对象在 $\mu$ 而非 $\delta$。
- 识别依赖 $\hat\zeta_{d,1}$ 的校准；若校准有偏，$\Delta\gamma$ 会吸收误差。

**溢出检验 L216** 错误，见 F-2。

**(M3.17) L220–228** 规格可行，并声明为条件关联 ✓。
- (i) $z_m$ 含油价水平，而油价同时在 $K$ 中，$\gamma(\pi)$ 只能由给定 $\pi$ 下的跨产品差异识别，与“油价识别 $\gamma$”的叙事冲突。
- (ii) 若市场为全国层面，$z_m$ 没有截面变异。
- (iii) 未写出注意理论“$\gamma$ 随 $\alpha_i$ 上升”的反向预测。

**P-M3 表 L232–241**
| 编号 | 判断 |
|---|---|
| P-M3-1 | ✓ 对 1 检验 |
| P-M3-2 | 与“油价识别 $\gamma$”循环 |
| P-M3-3 | 被 $\ell$ 内生与贴息的价格效应污染 |
| P-M3-4 | 缺注意理论的反向预测 |
| P-M3-5 | 错误（F-2） |
| P-M3-6 | “拒绝”还可能来自内生注意、$K$ 尺度错误、油价预期非鞅、外部选项油费遗漏，不能只归为“第三信源” |

**§M3.9 L245–249** ✓ 嵌套与边界正确。

**§M3.10 来源 L253–257 与 §M3.2 标签**
- Laibson (1997)、Gabaix (2014)、DellaVigna (2009)、Hausman (1979)、Allcott–Wozny (2014) 在本地知识库**无精读卡**，只在 A05/A14/A15 卡中被转述。
- L40 标 [O]、L60 标 [O·卡]、L81 标 [O·卡]，应改为“外部已发表理论，本地未核读”或“经 GRV/GHVB 卡转述”。

**M3.0 L14** “三种理论的福利含义有何不同？——§M3.7–M3.8”指向错误：§M3.7–§M3.8 没有福利推导。

**LaTeX 整体**
- 两处溢出截断。
- 符号冲突：
  - $H$：寿命 vs 注意利害；
  - $W$：期望效用 vs 楔子；
  - $\delta$：贴现因子 vs 平均效用；
  - $\beta$：现时偏好 vs M2 的 $\hat\beta$ vs 口味 $\beta_i$；
  - $S^*$：两义；
  - $v$：M1 的 $v_\tau$ vs M2 的 $v_j$。
- §M3.6 与式 (M3.6) 同号。

---

## 5. 必须修改项（按优先级）

**M-1（对应 F-1）重写 §M3.4.2–§M3.4.3。**

先写清秩的结构：2 个可识别系数 $(a^L,a^R)$ 对应 3 个结构参数 $(\gamma,\kappa,\zeta)$。油价变化只提供乘法可分性检验，不提供分离。

$\gamma$ 与信任的分离只能来自以下之一：
- M2-A 的 $\hat\zeta$ 校准；
- M2-B 的精度函数形式（评论很多的车型上 $\kappa\to0$，$B\approx m$）；
- “$B$ 已知”（如 $B=T$）。

$\gamma$、指数、$r^*$、$S^*$ 都要标为“条件于该约束”，并报告 $\gamma$ 对 $\hat\zeta$ 的敏感性（弹性 $-\kappa$）。

对用户直觉的回答改为：
- (1) 下降幅度识别的是 $\varphi_{d,1}=\gamma\kappa\zeta$（天真）或 $\varphi$ 乘相对楔子（RI），而不是 $\gamma$；
- (2) NEDC 下 $\zeta>1$，$\varphi\approx1$ 与 $\gamma<1$ 相容；
- (3) 理解换尺的理性者对平均楔子不反应，大幅下降反而指向天真读数；
- (4) 先用第二信源加 $\zeta$ 约束固定 $\kappa\zeta$，才能谈 $\gamma$。

**M-2（对应 F-2）重写 §M3.6 溢出检验与 P-M3-5。**
- 承认信息外溢同样提高油价敏感度；它的效应随 $K_{imt}$ 变化，不是截距。
- 改用可区分统计量：未切换车型的车主实测斜率 $a^R$ 的变化（注意下上升，外溢下不变），以及 $a^L/a^R$ 的变化（注意下不变，比例式外溢下上升）。
- 写出上表三种情形的交叉偏导。

**M-3（M3.3 原语）**
- 明写 $\gamma=\beta$ 所需的原语（流动性约束/手到口，或效用定义在货币流上）。
- 说明在 M1.2 完全资本市场下 $\gamma=1$。
- 与 (M3.4) 调和：贷款意味着信贷可得，可用“部分消费者受约束”的混合模型，并讨论 $\ell$ 内生。
- 引用货币流上现时偏好的证据并标注其有限性。

**M-4（内生注意）** 二选一：
- (a) 把 $\gamma_d$ 声明为“as-if”结构常数，删去“注意理论蕴含常数 $\gamma$”的暗示；
- (b) 结构化 $\gamma_{imt}=H_{imt}/(H_{imt}+c)$，并承认油价反应识别的是 $\gamma(3-2\gamma)$。

两种做法都需相应修改 P-M3-2/P-M3-6，并在反事实中重解 $\theta^*$。

**M-5（福利，兑现 M3.0 承诺）** 统一用作者自己的 (M3.5) 体验效用公式：
$$
CS^{exp}_i=\tfrac1{\alpha_i}\Big[LS(V^D_i)+\textstyle\sum_jP_{ij}(V^D)(V^N_{ij}-V^D_{ij})\Big],
$$
按三种来源给出规范效用 $V^N$：
- 现时偏好：长期基准，须同时重标服务流；
- 理性注意：扣除注意成本 $\tfrac12c\theta^2$，并讨论改变 $H$ 的政策；
- 信贷约束：无内部性。

把“短视损失 $(1-\gamma)K$”改名为“低估楔子”，并给出二阶福利损失。引用 Allcott (2013)、Sallee (2014)、AMT (2014) 以及 GRV 的 misoptimization loss。

**M-6（BLP 估计闭环）**
- 列出新增 $\theta_2$ 及参数化：$\gamma=\exp(\cdot)$，$\kappa=\mathrm{logit}^{-1}(\cdot)$。
- 写出识别它们的矩与工具：$Z$ 含 $\bar K_{mt}L_{jt}$、$\bar K_{mt}m_{j,t-1}$、$Z^W$、与里程分布矩的交互。
- 写出 $L$、$m$ 在固定效应条件下的外生性假设；处理 $m_{j,t-1}$ 的滞后销量内生性（如用预定评论、滞后评论数作工具，或做领先检验）。
- 推断要覆盖生成变量（$\hat\zeta$、$m$、$K$）与聚类层级。
- 把 (M3.12)(M3.16) 中的 $\delta$ 改为 $\mu$ 或份额响应。
- 处理外部选项能源成本：纳入 $-\alpha_i\gamma K_{imt}e_{0}$ 或论证可忽略。

**M-7（命名与 claim ladder）**
- “短视指数”改为“资本化缺口/低估指数 $UI_d\equiv1-\gamma_d$（与短视等解释一致）”。
- 在 §M3.2.4 表与 §M3.8 中加入竞争解释及其可区分预测：风险/不确定性、残值与持有期、里程误感知、油价预期。

**M-8（$r^*$、$S^*$ 定义域）**
- 给出 $\gamma>\Lambda(0,H)/\Lambda(r,H)$ 时 $r^*<0$、$S^*>H$ 的处理。
- 统一 $S^*$ 的定义。
- 按 GRV 同时报告无尺度的 $\gamma\Lambda$（所需回收期）。

**M-9（来源标注）**
- 修正 Laibson/Gabaix/DellaVigna/Hausman/Allcott–Wozny 的 [O]/[O·卡] 标签。
- “车贷渗透率约一半”补来源或改为 [I]。
- 准确描述 GRV 的变异来源（77% 截面发动机差异）。
- 补 Li (2026) 差值显著这一事实。

**M-10（LaTeX）**
- (M3.5)(M3.9) 改用 `aligned`/`split` 换行，消除截断。
- 消解 $H$、$W$、$\delta$、$\beta$、$S^*$、$v$ 的符号冲突，例如注意利害记 $\mathcal H$，贴现因子记 $\varrho$，现时偏好记 $\beta^{PB}$。
- 章节号与式号不要同名。

---

## 6. 建议修改项

- **S-1** 明确回答用户的“需求反而增加”：$\gamma\ge0$ 不翻转符号，需求上升必须来自 $\Delta B<0$（可信度红利）、价格或竞品变化，不可能来自短视。
- **S-2** 回应“续航突变对短视”。续航不便若只以自由的 $\eta_i$ 进效用，会吸收 $\beta$，续航跳变不提供 $\gamma$ 的信息。若把绕行/补能时间货币化，则 $\gamma$ 适用，可据此设计检验。
- **S-3** P-M3-4 补注意理论的反向预测（$\gamma$ 随 $\alpha_i$ 上升），把收入梯度变成两理论的判别。
- **S-4** P-M3-3 改为利用外生信贷供给冲击（地区信贷政策、厂商贴息政策变化），区分贴息带来的价格效应与 $\beta$ 机制，否则降格为描述性关联。
- **S-5** 里程分布：说明是购买者条件分布还是总体分布（GRV 在线附录 A.3 的映射）；单独处理网约/营运高里程车。
- **S-6** 基准 $\gamma_B=\gamma_I$ 时，做 $\psi_{i,d}$ 与 $VKT_i$ 相关的稳健性检验，以检验“绿色偏好 × 里程”对 $\gamma$ 的污染。
- **S-7** 若采用注意理论，$\gamma_i$ 与 $\alpha_i$ 相关，报告时须逐抽样计算比率（GHVB D.4 的纪律）。
- **S-8** 报告 (M3.5) 二阶近似的精度：用精确 $W(\theta)$ 对照（本审例中 $\theta=0.6$ 时误差约 26%）。
- **S-9** 说明中国成品油价调整机制（含地板价/天花板价、税费调整）对油价有效变异的影响，并按 GRV 做“控制变量后燃油成本残差方差分解”。
- **S-10** 附一个小型蒙特卡洛：M2-A 下 $(\gamma,\kappa)$ 可恢复；$\hat\zeta$ 有偏时 $\gamma$ 的偏差为 $-\kappa\times$（$\hat\zeta$ 的相对偏差）；不校准 $\zeta$ 时脊线不可识别。

---

## 7. 实际计算与结果

**环境与命令**
- 脚本：`python3 -I verify_m3.py`（全文见附录，numpy/sympy/scipy）。
- 编译：`bash tools/build_pdf.sh deliverables/M3_机制二_短视与资本化.md /tmp/m3_review.pdf`，以及 pandoc 生成 .tex 后 xelatex 两遍。

**A. (M3.3)**
- 手到口、线性效用：MRS $=\beta\delta$，按现值换算 $\gamma=\beta$ ✓。
- 完全资本市场、$\beta=0.5$、log 效用：$\gamma=1.000000$。
- 无借贷、log 效用：$\gamma=0.400=\beta\,u'(c_1)/u'(c_0)$。

**B. (M3.4)**
- $\alpha'=\alpha(1-\ell+\beta\ell)$，$\gamma_{eff}=\beta/(1-\ell+\beta\ell)$；
- $\partial\gamma_{eff}/\partial\ell=-\beta(\beta-1)/(\cdot)^2\ge0$；
- 端点为 $\beta$ 与 1 ✓。

**C. (M3.5)**（$J=8$ 加 outside，$G_0=0$，$\alpha=1.3$）
- $H=\alpha^2G'MG=0.188657=\alpha^2\mathrm{Var}_P(G)$ ✓。
- 精确 $W-LS$ 与二阶近似：

| $\theta$ | 精确 | 二阶近似 | 相对误差 |
|---|---:|---:|---:|
| 0.99 | −0.000009 | −0.000009 | −0.6% |
| 0.90 | −0.000890 | −0.000943 | −5.7% |
| 0.60 | −0.011939 | −0.015093 | −20.9% |
| 0.30 | −0.030755 | −0.046221 | −33.5% |

**D. (M3.6)**
- $\theta^*=H/(H+c)$，SOC $=H+c$，$\partial\theta^*/\partial H=c/(H+c)^2$，$\partial\theta^*/\partial c=-H/(H+c)^2$ ✓。
- 内生注意：$d[\gamma(K)K]/dK=\gamma(3-2\gamma)$；真 $\gamma=0.3/0.6/0.9$ 时，油价反应读出 $0.72/1.08/1.08$。

**E. (M3.7)(M3.8)**
- $\Lambda(5\%,10)=7.7217$，$0.6\Lambda=4.6330$，$r^*=17.1515\%$，$\Lambda(17.2\%,10)=4.6249$，$S^*=4.633$ ✓。
- $dr^*/d\gamma$：公式 $-0.45985$，有限差分 $-0.45985$ ✓。
- $\gamma>1$ 的情形：

| $\gamma$ | $r^*$ | $S^*$ |
|---|---:|---:|
| 1.17 | 1.89% | 9.03 |
| 1.30 | −0.07% | 10.04（超过 $H$） |
| 1.60 | −3.67% | 12.35（超过 $H$） |

**F. (M3.10)(M3.11) 与秩**
- 三个导数 ✓；M2-A 解 $\gamma=a^L/\hat\zeta+a^R$，$\kappa=a^L/(a^L+a^R\hat\zeta)$ ✓。
- 结构映射奇异值 $[8.313,\,1.112,\,0]$。
- 模拟份额 Jacobian 的归一化奇异值：

| 情形 | 奇异值 | 秩 |
|---|---|---|
| M1 比例信念 + 40 个月油价，对 $(\gamma,\zeta)$ | $[1.414,\,0]$ | 1 |
| 双信源，对 $(\gamma,\kappa,\zeta)$ | $[1.414,\,1.001,\,0]$ | 2 |
| 固定 $\zeta$，对 $(\gamma,\kappa)$ | $[1.008,\,0.992]$ | 2（满秩） |

**G. (M3.13)–(M3.15)**
- $\partial\Delta V/\partial\gamma=-\alpha K\Delta B$；
- $\partial(V_b-V_f)/\partial\gamma=\alpha(K_FB_f-K_EB_b)$；
- $\partial(V_b-V_f)/\partial\gamma_B=-\alpha K_EB_b$ ✓。

**H. (M3.16)** 交叉偏导见 F-2 表：外溢下 $\partial^2u/\partial K\partial\hat\beta=-\alpha\gamma\kappa\neq0$。

**I. (M3.12)**
- 天真：$\Delta B=L_N\kappa w\zeta_0$；
- RI：$\Delta B=L_N\kappa\zeta_0(w-\bar w)/(1+\bar w)$，当 $w=\bar w$ 时为 0。

**J. 量级 [I]**（$\alpha=5/150000$，$K^F=6950$ 元/(L/100km)，5 档油耗份额加权）
- $\gamma=0.6$：线性楔子 2780 元/(L/100km)，二阶期望损失约 204 元/人；
- $\gamma=0.9$：线性楔子 695 元/(L/100km)，二阶期望损失约 13 元/人。

**LaTeX**
- `build_pdf.sh` 构建成功（8 页）。
- xelatex 日志：`Overfull \hbox (70.67pt)`，对应 (M3.5)，渲染页 3 右端“$\ge0$”被截；`Overfull \hbox (69.86pt)`，对应 (M3.9)，渲染页 5 右端 $m_{j,t-1}$ 被截。
- 无缺字警告。

---

## 8. 应保留的优点

- (M3.4) 贷款修正正确而有新意：“贷款比例越高，测得 $\gamma$ 越接近 1”是解释跨地区差异时真实需要控制的通道。前提是先修正 (M3.3) 的原语。
- (M3.5)(M3.6) 把注意收益写成 $\alpha^2\mathrm{Var}_P(G)$，与 logsum 体验效用公式一致，推导干净。
- (M3.14)(M3.15) 的“共同资本化 vs 纯电自身 $\gamma_B$”辨析，直接纠正了“NEV $\gamma$ 更高 = 更看重节能”这一常见误读。
- 一贯坚持对 1 检验，承认尺度不可分并给出敏感性网格，把城市梯度写成条件关联，$\gamma<1$ 只写“与短视一致”。

---

## 附录：验算脚本（`verify_m3.py`，完整可复现）

```python
#!/usr/bin/env python3
# 第三方审稿人对 M3（短视与资本化）的逐式验算脚本
import numpy as np
import sympy as sp
from scipy.optimize import brentq
from scipy.special import logsumexp
SEP = "=" * 78
# A. (M3.3)
b, d, lam, p, E1, r = sp.symbols('beta delta lambda p E1 r', positive=True)
U_htm = -lam*p - b*d*lam*E1
mrs_htm = sp.diff(U_htm, E1)/sp.diff(U_htm, p)
print("A1 MRS =", sp.simplify(mrs_htm), "; gamma =", sp.simplify(mrs_htm/d))
bb, rr = 0.5, 0.05; dd = 1/(1+rr)
def V_perfect(pp_, EE_, W=100.0):
    Y = W - pp_ - EE_/(1+rr); c0s = Y/(1+bb*dd); c1s = (Y - c0s)*(1+rr)
    return np.log(c0s) + bb*dd*np.log(c1s)
eps = 1e-6
g_pm = ((V_perfect(10,5+eps)-V_perfect(10,5-eps))/(V_perfect(10+eps,5)-V_perfect(10-eps,5)))/dd
print("A2 perfect capital market gamma =", g_pm)
def V_htm(pp_, EE_, y0=30.0, y1=30.0): return np.log(y0-pp_) + bb*dd*np.log(y1-EE_)
g_h = ((V_htm(10,5+eps)-V_htm(10,5-eps))/(V_htm(10+eps,5)-V_htm(10-eps,5)))/dd
print("A3 no-borrowing log gamma =", g_h, "vs", bb*(30-10)/(30-5))
# B. (M3.4)
l, PVE, a = sp.symbols('ell PVE alpha', positive=True)
DV = -a*((1-l)*p + b*l*p + b*PVE)
ge = sp.simplify(sp.diff(DV, PVE)/sp.diff(DV, p))
print("B gamma_eff =", ge, "; d/dell =", sp.simplify(sp.diff(ge, l)))
# C. (M3.5)
rng = np.random.default_rng(7); J = 8
V = np.r_[0.0, rng.normal(0, 1, J)]; G = np.r_[0.0, rng.normal(1.0, 0.25, J)]; alpha = 1.3
P_of = lambda v: np.exp(v - logsumexp(v))
def W_exact(th):
    Vt = V + (1-th)*alpha*G; return logsumexp(Vt) + P_of(Vt) @ (V - Vt)
P0 = P_of(V); M = np.diag(P0) - np.outer(P0, P0); H = alpha**2 * G @ M @ G
print("C H =", H, "alpha^2 Var =", alpha**2*(P0@G**2-(P0@G)**2))
for th in [0.99, 0.9, 0.6, 0.3]:
    print(" theta", th, W_exact(th)-logsumexp(V), -0.5*(1-th)**2*H)
# D. (M3.6) + 内生注意
th, Hs, c = sp.symbols('theta H c', positive=True)
obj = sp.Rational(1,2)*(1-th)**2*Hs + sp.Rational(1,2)*c*th**2
ths = sp.solve(sp.diff(obj, th), th)[0]; print("D theta* =", ths)
K, A = sp.symbols('K A', positive=True); g = sp.symbols('g', positive=True)
resp = sp.simplify(sp.diff(A*K**2/(A*K**2+c)*K, K)).subs(c, A*K**2*(1-g)/g)
print("D d[gamma(K)K]/dK =", sp.factor(sp.simplify(resp)))
# E. (M3.7)(M3.8)
Lam = lambda rate, Hh: np.sum(1/(1+rate)**np.arange(1, Hh+1))
L0 = Lam(0.05, 10); rstar = brentq(lambda x: Lam(x,10)-0.6*L0, 1e-6, 2)
print("E Lambda =", L0, "r* =", rstar, "S* =", 0.6*L0)
# F. 秩：结构映射与模拟份额 Jacobian
gm, ka, ze = sp.symbols('gamma kappa zeta', positive=True); Lv, mv = 6.5, 7.8
Jm = sp.Matrix([gm*ka*ze, gm*(1-ka), gm*ka*ze*Lv+gm*(1-ka)*mv]).jacobian([gm, ka, ze])
print("F SVD =", np.linalg.svd(np.array(Jm.subs({gm:0.7, ka:0.6, ze:1.2}).evalf(), float), compute_uv=False))
rng = np.random.default_rng(3); T, Jp = 40, 10
Kt = 0.2*(1+0.3*rng.standard_normal(T)); Lj = rng.uniform(5, 9, Jp); mj = Lj*rng.uniform(1.05, 1.35, Jp)
xi = rng.normal(0, 0.5, (T, Jp))
def logshares(t, free=True):
    g_, k_, z_ = t; k_ = k_ if free else 1.0
    v = xi - g_*Kt[:, None]*(k_*z_*Lj[None, :] + (1-k_)*mj[None, :]); va = np.c_[np.zeros(T), v]
    return (va - logsumexp(va, axis=1, keepdims=True))[:, 1:].ravel()
def nj(f, t0, h=1e-6):
    t0 = np.asarray(t0, float); f0 = f(t0); Jc = np.zeros((f0.size, t0.size))
    for k_ in range(t0.size):
        e_ = np.zeros_like(t0); e_[k_] = h; Jc[:, k_] = (f(t0+e_)-f(t0-e_))/(2*h)
    return Jc
for lab, Jx in [("M1 (gamma,zeta)", nj(lambda t: logshares(t, False), [0.7,0.6,1.2])[:, [0,2]]),
                ("dual (g,k,z)", nj(logshares, [0.7,0.6,1.2])),
                ("zeta fixed (g,k)", nj(logshares, [0.7,0.6,1.2])[:, [0,1]])]:
    print("F", lab, np.linalg.svd(Jx/np.linalg.norm(Jx, axis=0), compute_uv=False))
# H. (M3.16) 交叉偏导
Ls, ms, bh = sp.symbols('L m betahat')
u_lev = -a*gm*K*(ka*(Ls+bh) + (1-ka)*ms); u_rat = -a*gm*K*(ka*ze*Ls + (1-ka)*ms)
for nm, u_, par in [("attention", u_rat, gm), ("spill level", u_lev, bh), ("spill ratio", u_rat, ze)]:
    print("H", nm, sp.factor(sp.diff(u_, K, par)), sp.factor(sp.diff(u_, Ls, par)), sp.factor(sp.diff(u_, ms, par)))
# I. (M3.12) RI
LN, w, wbar, z0 = sp.symbols('L_N w wbar zeta0', positive=True)
dB_RI = ka*(z0/(1+wbar))*LN*(1+w) - ka*z0*LN
print("I RI DeltaB =", sp.factor(dB_RI), "; at w=wbar:", sp.simplify(dB_RI.subs(w, wbar)))
```

SCORE: 62
