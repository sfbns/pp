# 短视、先验与真实—标签油耗差：BLP 经济基础审计

日期：2026-10-07。本文只读既有源文件；未修改原文、旧精读卡或旧记忆。

## 1. question_received

真实道路油耗与标签油耗的差距，在 BLP 底层应理解为消费者先验、经验与信念更新，还是所有消费者对油耗属性的边际效用改变？严格推荐本地 BLP 原文，而不是把相邻 logit、自然实验或只有附录的文件混为已读 BLP 主文。

## 2. source_scope

### 2.1 最贴合且有逐页完成证据：Reynaert–Sallee (2021)

- 标题：*Who Benefits When Firms Game Corrective Policies?*，AEJ: Economic Policy 13(1): 372–412。
- [AEA 官方页面](https://www.aeaweb.org/articles?id=10.1257/pol.20190019)，本轮重新打开并核对书目信息。
- 原文：`D:\codex\output\reynaert_sallee_2021_source.pdf`。
- SHA256：`F478A23B703D83345EB2A90C7DB10961BFF7499C8332584E559FAF08A7E72A68`，本轮重算一致。
- 公式校核精读稿：`D:\codex\reynaert_sallee_2021_gaming_china_cycle_close_read_20260822.md`。
- 完成证明：上述精读稿 §一.2 明确主文 41/41 页逐页阅读、41 个逐页 JSON chunk、143262 字符、解析错误 0；关键公式已核原始页图。在线附录只定向读过，不冒充全文读完。
- 页级全文：`D:\codex\output\reynaert_sallee_2021_ocr_text\reynaert_sallee_2021_source\reynaert_sallee_2021_source.llm.json`，同目录 `.llm.md`。
- 本轮回源：PDF p.18 / journal p.389（信号、真值、认知权重）；PDF p.25 / journal p.396（RC logit、BLP 反演、GMM）；PDF pp.28–29 / journal pp.399–400（认知参数不可精确识别及情景校准）；PDF p.29 / journal p.400（决策与体验效用）。p.18、25、29 原始页图已本轮再次视觉核对。
- 原始页图：`D:\codex\output\reynaert_sallee_2021_formula_pages\page_18.png`、`page_25.png`、`page_29.png`。
- 证据状态：关键模型 `source-verified`；先前全文完成有文件记录，不称本轮重读 41 页。

### 2.2 严格短视 BLP：Grigolon–Reynaert–Verboven (2018)

- 标题：*Consumer Valuation of Fuel Costs and Tax Policy: Evidence from the European Car Market*，AEJ: Economic Policy 10(3): 193–225。
- [AEA 官方页面](https://www.aeaweb.org/articles?id=10.1257/pol.20160078)，本轮核对；官方全文按钮落地页要求会员/机构访问，不能说无条件免费。
- 基路径 ROOT：`D:\codex\research-memory\BLP_structural_models_memory_skills_configs_2026-08-24\01_primary_enhanced_corpus`。
- 原文：`ROOT\source_pdfs\04_5twrwep3.pdf`。
- SHA256：`5D729774CBE07F5281ED09097CAF3F224BE24A2260417E766D8D361B5E8670DF`，本轮重算。
- 卡/模型记忆：`ROOT\memories\papers\04_5twrwep3.md`。
- 全文：`ROOT\raw\fulltext\04_5twrwep3.fulltext.txt` 与 `.fulltext.json`。
- 阅读状态证据：`ROOT\audits\csv_manifest_fulltext_audit_2026-04-18.md` 只支持 fulltext-grounded durable-memory，并明确不支持统一逐句精读或每一公式人工复核。不能把此文件升级成逐页精读完成证明。
- 本轮回源：全文 TXT 行 68–74 明确以 BLP (1995) aggregate random-coefficients logit 为基础；PDF p.8 / journal p.200，式 (3)–(5) 已再次视觉核对；p.9 / journal p.201 说明资本化参数的解释与限制。
- 完整显示公式来源台账：`D:\codex\output\blp_driving_cycle_structural_research_20260824\formula_source_ledger.md`，`SRC-GRV-2018`。
- 本轮补读完成：2026-10-07 已依次阅读原 PDF 全部33页（含脚注、表/图注、参考文献），新证明 `D:\codex\output\blp_bundle_20261007\grv_completion_20261007.md`，含四个阅读块、每页内容锚、PDF与全文hash；此后才标completed。旧资产审计仍不被升级为历史逐页证明。
- 使用边界：本轮完整阅读仅指本地33页主文文件；在线附录不在该文件，未全文阅读。关键公式本轮已校核不等于每个脚注公式已逐一视觉认证。
- 数值措辞纠正：旧卡写每 1 欧元未来成本约资本化 0.91 欧元；原文摘要/引言同时指出不能拒绝正确估值。建议只写“短视/资本化建模母本”，不要写“已证实消费者普遍短视”。

### 2.3 明确排除/降级

- Gillingham–Houde–van Benthem (2021) 是标签自然实验与价格资本化母本，不是所要求的随机系数 BLP 估计母本，虽有附录 logit 微观基础；不能因引用 BLP 或有结构解释就计入严格 BLP 五篇。
- Leard–Linn–Springel 的本地 RFF WP 23-04 使用分组固定效应 logit，卡片明确“不是随机系数”；不能冒充 BLP。
- Barahona–Otero–Otero (2023) 的导入项 `ROOT\source_pdfs\09_s925qhzd.pdf` 实际为补充材料。其卡片明确不是完整主文，因此不能列为本地已读主文。若确需明确 prior-belief/nutritional-label BLP 扩展，应另找主文，作为下载候选，不能用附录替代。
- Huse–Lucinda–Cardoso (2020) 的 `ROOT\source_pdfs\06_epwj8s9t.pdf` 是家庭微观随机系数 logit，p.6 把期望成本与信息集分开；但没有完整 BLP 需求—供给结构，也不是明确估计 Bayesian 先验学习的汽车模型。仅作可标明限制的标签 RC-logit 备选，不能称为先验后验的直接识别文献。

## 3. answer：对象修正与真正约束性的经济基础

**答案：真实值—标签值差本身是一个测量/信息楔子，不是先验，也不是偏好参数。先验是消费者购车前关于真实油耗的分布；驾驶或口碑经验提供信号；标签与经验共同进入信息集形成后验。通常先保持油耗/使用成本偏好不变，只让主观预期的属性变化。不能先假定所有消费者的边际效用一起改变。**

### 基础六项

| 字段 | 约束性定义 |
|---|---|
| visible_object | 物理车辆不变时标签数值改变，且消费者对真实道路油耗的判断可能改变 |
| canonical_theory_family | Lancaster 式属性需求、随机效用最大化、跨期预算/预期使用成本、信息条件下的选择；BLP 负责异质性、份额反演及产品替代，不自动提供学习理论 |
| canonical_result | 若偏好、价格、选择集和真实属性不变，且新旧标签给每个消费者相同的真实属性后验，则纯单位/标尺变化不改变条件选择概率 |
| primitive_held_fixed | 消费者关于属性的已知/主观信息映射；成本偏好、里程、持有期、贴现率等与该映射区别对待 |
| institutional_wedge | 工况切换或测试/披露使标签到真实道路属性的映射发生变化；是否被理解、是否增加精度以及是否有已知纠偏决定后验 |
| changed_economic_condition | 同一车辆的主观使用成本进入随机效用，改变需求与相对替代；若允许企业响应再改变定价均衡 |

`foundation_is_binding: yes`：后验不变时效应必须为零，后验改变时符号受成本项限制。若研究只写“信息不对称”却不限定效用中的哪一项或后验，属于 decorative label。

### 3.1 最小模型：保持偏好，改变认知属性

以下均为 `project-extension / standard-derived`，不是两篇论文的逐字公式；不冒充已识别的中国模型。

令 q_j 为实际道路油耗（L/100km）、L_j 为标签油耗，消费者先验为 pi_ij(q)。令消费者已经换算到共同道路口径的标签信号为 s_j，经验信息为 z_ij。一般后验为

    pi_ij(q | L_j, c_j, z_ij) proportional to
    likelihood_i(L_j, z_ij | q, c_j) * pi_ij(q).

这只是信息结构；不能只因写了 Bayes 就认定消费者实际 Bayesian，必须说明信号似然、工况转换与误解机制，并拥有可检验数据。

基准决策效用：

    u_ij = x_j' beta_i - alpha_i p_j - alpha_i lambda_i E_i[PVOC_ij | I_i]
           + xi_j + epsilon_ij.

alpha_i > 0；lambda_i 是未来成本相对当前购车价的资本化权重；xi_j 是消费者/企业知道、研究者没观测到的产品质量，不能定义为双方都不知道，也不应把个人认知差统一塞进去。PVOC 用主观油价、里程、持有期、存活和贴现构造。

在油价、里程、贴现与 q 的协方差不存在或已经处理，且使用成本对 q 线性时，可定义

    K_i = sum_tau discount_i,tau * mileage_i,tau * E_i[fuel_price_tau] / 100,
    qhat_ij = E_i[q_j | I_i],
    u_ij = x_j' beta_i - alpha_i p_j - alpha_i lambda_i K_i qhat_ij + xi_j + epsilon_ij.

真实状态不确定且风险厌恶时，均值不足；方差、风险偏好也能进入效用，属于另一扩展，不宜偷偷并入“标签系数”。

**认知变化**是 qhat_ij 变化；**偏好变化**是 alpha_i、lambda_i 或其他效用权重变化。信息政策未必改变这些偏好原语。边际响应于标签可以变化，但不等于根本偏好改变：

    d u_ij / d L_j = - alpha_i lambda_i K_i * d qhat_ij / d L_j.

若估计中直接使用 L 而没有后验层，估计到的“油耗系数”可能是偏好×预期成本×标签映射的复合系数。不能由这个复合斜率变化推断所有消费者更重视节油。

### 3.2 最小先验精度例：标签权重不等于偏好

为显示先验如何产生可检验预测，考虑明确标为 illustrative-only 的正态例子：共同道路单位下的先验 q~N(mu_i, sigma_i^2)，信号 s=q+noise，noise~N(0,tau_i^2)。则

    qhat_i = (1-w_i) mu_i + w_i s,
    w_i = sigma_i^2 / (sigma_i^2 + tau_i^2).

先验更精确（sigma_i^2 小，常可由更多可靠经验产生）时，标签权重较小；信号更精确（tau_i^2 小）时，权重较大。若真实标签有消费者未知的偏差，则不能把它写成均值为零的噪声然后声称所有人都理性纠偏。

Reynaert–Sallee (2021) 使用的则是另一个受限认知映射，原文 PDF p.18：

    g = q - L,
    qtilde = a q + (1-a)(q-g) = q - (1-a)g.

a=1 表示完全识破，a=0 表示完全相信标签。**它不是明确的 Bayesian 先验—似然—后验估计，也不能把 a 写成实证上已经识别的学习速度。** 原文 PDF p.29 说明市场数据不能给出精确认知估计，故在不同 a 上做情景模拟。

### 3.3 “所有消费者边际效用变化”什么时候只是等价重参数化

如果对每个人都强加 qhat_ij = a + b L_j，且成本项线性，那么标签有效系数包含 b；没有认知数据时，把 b 改变写成标签系数改变，可能与偏好改变观测等价。这只是数据无法区分的约化式表示，不是偏好变化的证据。

- 对所有内外选项都相同的效用常数不会改变选择；只对所有购车选项共同增加成本，则仍可改变相对 outside option 的总购车量。
- 若不同消费者有不同先验、标签信任、里程、换算能力，则 qhat、K 和响应都异质；共同的标签冲击不意味着每个人相同反应。
- 若存在污染厌恶、绿色身份或可信认证溢价，可增加独立属性效用，但须用单独变异识别，不能把它们和预期燃油支出混成一个偏好系数。

### 3.4 短视与误信不能混称

Grigolon–Reynaert–Verboven PDF p.8 式 (5) 为

    u_ijk = x_jk beta_i^x - alpha_i(p_jk + gamma rho beta_i^m e_jk g_k)
            + xi_jk + epsilon_ijk.

beta_i^m 是里程，e 是 L/km，g 是 EUR/L；rho 把年度成本资本化，gamma 是在给定贴现和寿命基准下解释的未来成本权重。论文明确 gamma、rho、里程尺度不能同时自由识别，借用外部里程分布并给定 r/S 后解释 gamma。

即使 lambda_i=1，误信过低 qhat 也会低估真实燃油支出；即使 qhat 正确，lambda_i<1 也会较少资本化未来成本。二者都可能给出弱标签响应，但机制及福利反事实不同。不能从一个小系数自动叫作短视。

## 4. mechanism_chain

政府工况/标签规则或企业测试披露 -> 消费者观察到信号及其口径 -> 在经验和先验约束下形成主观道路油耗/使用成本 -> 随机效用选择和跨车型替代 -> 多产品企业重新定价（若允许） -> 市场份额、利润与体验福利。

消费者先获信息再选车；企业给定既定产品集时选择价格。静态 BLP 的均衡扩展可采用多产品 Bertrand–Nash。若企业还选择工程属性、操纵量或认证日期，须另写这些选择的成本与约束；不能从价格 FOC 推出它们已经被识别。

## 5. predictions

1. **方向**：价格与其他替代品信息固定时，某车 qhat 上升使其效用下降。条件 logit 中 dP_ij/dL_j = P_ij(1-P_ij) du_ij/dL_j；若 alpha、lambda、K 和信号响应均为正，直接自份额效应为负。所有产品同时重标时需用完整相对变化，不能对每一车逐个套“必降”。
2. **异质性**：在给定价格敏感度、资本化、信息权重等条件下，更高预期里程/持有期意味着更强使用成本响应；不能把这种条件偏导升级成不加条件的组间政策效应。
3. **先验边界**：精确先验或消费者已完全知道新旧标签映射时，纯重标的更新效应趋零；可靠新信号相对先验越精确，更新权重越大。
4. **非线性**：即使效用线性，logit 概率因 P(1-P) 存在非线性，不能把曲率自动解释为认知偏差。若信号可靠性/注意本身随标签变化，则还有另外的非线性来源，需单独建模。
5. **福利边界**：消费者按决策效用选车，体验福利需用被选车辆的真实成本评价；不能让其先按真实效用重新选择再把新 logsum 当原政策福利。R&S PDF p.29 在保持同一 beta_i 的前提下替换 qtilde 与 q，正说明不是偏好变了。

## 6. rival_and_falsifier

最近 rival 是真实工程变化、净价与补贴变化、品牌声誉、里程/持有期与油价预期变化，以及标签之外的绿色认证溢价。

最强区分证据是严格同硬件车辆、消费者购车前后的真实油耗预期、信号随机提供/纠偏、标签口径理解测试、标签信任与实际选择联合微观数据。若可信的信息实验不改变后验而仍改变选择，纯“均值信念更新”机制就不够，需要显著性、认证效用或其他机制。若后验明显改变却没有份额效应，不能立刻推翻信息机制；需检验资本化、价格对冲、统计功效与选择集支持。

聚合全国销量、标签值与真实值本身，通常不能分别识别 alpha、lambda、K、认知权重和信号可信度。价格工具变量并不自动识别认知参数。必须展示额外矩或外生信息变异。

## 7. handoff

给 baseline theory agent / BLP specialist：保持“客观测量楔子 -> 主观后验 -> 预期使用成本 -> 选择”四对象，不把客观 gap 本身称为 prior，不让同一信息冲击同时任意改变全部消费者偏好。待决的是：消费者看到的是新水平、同比变化，还是工况名称；他们是否知道映射；有无真实道路预期数据；总需求/outside 与交易价是否齐全。当前最小可用模型是异质信念属性进入固定偏好的 RC demand，供给响应与学习动态仅在额外数据到位后增加。

给打包执行者：优先收录 R&S 原文与 20260822 精读稿；短视 BLP 用 GRV 原文、模型记忆、新公式审计和 `grv_completion_20261007.md`。不要把 R&S 已有全文证明与 GRV 旧资产审计当作相同证据等级；GRV现在有本轮新逐页阅读证明。不要将附录 09 当食品主文。

## 8. confidence_and_limits

高置信：R&S 是严格随机系数 BLP 需求、决策与体验效用分离，认知 a 的情景模拟而非精确实证识别；GRV 是严格 BLP 未来燃料成本资本化模型，其 gamma/rho/里程尺度识别限制；纯测量差与偏好参数是不同对象。

推导/假说：正态先验例子、中国标签改革机制、条件比较静态和最小经验设计均为本文推论，不是原文已经证明的中国事实。

缺失：旧GRV历史完成证明不足，但本轮已全读33页并新建证明；GRV在线附录、R&S在线附录均未全文精读；未识别中国消费者先验、信任、学习或短视。无需用户下载 R&S 或 GRV 原文，因为本地均已存在；如果要求明确 Bayesian learning 的 BLP 论文，则需另列新候选并重新全文核验，不用现有两篇硬冒充。

## 执行异常留痕

第一次 Python 读取 R&S 原文页输出因终端 GBK 编码遇软连字符而报 UnicodeEncodeError，exit 1；改为 sys.stdout.reconfigure(encoding='utf-8') 后同一原文读取成功，exit 0。异常只涉及 stdout，不涉及 PDF 内容或完整性。
