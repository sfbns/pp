# 核验账本：Codex BLP/结构模型记忆逐条判定

日期：2026-08-25　审阅者：Claude Opus 5　对象：本机全部 BLP / 结构模型记忆与交付

判定分四档：**PASS**（核过，结论成立）· **CORRECTED**（发现错误，已给出更正）· **CAVEAT**（结论成立但有必须同时说明的边界）· **BLOCKED**（无法核验，原因已记）。

---

## A. 公式层

| # | 被核对象 | 核验方式 | 判定 | 结论 |
|---|---|---|---|---|
| A1 | BLP(1995) (3.1)(3.2)(3.3)(3.4)(3.5)(3.6)(4.1) | 读渲染原页 `audit_pages\blp_pdf_p14.png`(期刊 p.853)、`p15.png`(p.854) | **PASS** | 与本地 walkthrough 逐字一致；`Δ_jr=−∂s_r/∂p_j`（同厂）方向正确；向量 FOC 与 `p=mc+Δ^{-1}s` 在原文确实未编号，walkthrough 处理正确 |
| A2 | (6.8) 收缩映射、`ξ_j=δ_j−x_jβ` | `blp_pdf_p26.png`(p.865) | **PASS** | 一致。walkthrough 对"为什么没有 `+αp_j`"的解释正确（完整规格里价格走 `α log(y_i−p_j)` 非线性部分） |
| A3 | **(6.9b) 交叉价格导数** | `blp_pdf_p26.png` | **CORRECTED** | **本地 walkthrough 第 31 条漏掉前置负号。** 原页为 `∂s_j/∂p_q = ∫ −f_j·f_q·[∂μ/∂p_q]P_0(dν)`。漏负号 ⇒ 交叉导数反号 ⇒ Δ 非对角元反号 ⇒ markup 与 mc 全错。(6.9a) 抄对。**2026-10-07 已修**：8 份副本全部补回负号并改写为 `∂μ_iq/∂p_q`，见文末 G 节 |
| A4 | (6.9b) 原文自身 | 同上 | **CORRECTED（原文错）** | 原页印 `f_j(ν, ξ, x, p, θ)`，应为 `f_j(ν, δ, …)`；印 `[∂μ_ij/∂p_q]`，但 `μ_ij` 不含 `p_q`（q≠j），照抄得零，经济上应为 `[∂μ_iq/∂p_q]` |
| A5 | (6.10)(6.11)(6.12)、`s̄=1−s_0=Σs_j` | `blp_pdf_p27.png`(p.866)、`p28.png`(p.867) | **PASS** | 一致 |
| A6 | **(6.13) importance-sampling 模拟器** | `blp_pdf_p28.png` | **CORRECTED（原文错）** | 原页印 `Σ_{i=1}^{ns}[s̄(θ',P_0)/f̄(ν_i,θ')]f_j(ν_i,θ)`，**无 `1/ns`**。按 accepted draws 推导 `E[Σ] = ns·s̄·s_j`，须除以 `ns·s̄`（等价 `(1/ns)Σ_{accepted} f_j/f̄`）。walkthrough 忠实照抄了原文，这一条不是 walkthrough 的错 |
| A7 | walkthrough 其余各式 (2.1)–(2.7)、(5.1)–(5.8)、(6.1)–(6.7)、(6.14)、附录 I | 对 OCR 全文与原页交叉 | **PASS** | 内容与原文一致，是可信的教学底稿 |
| A8 | 项目主报告 §8.2 价格导数 | 独立推导 | **PASS** | `∂s_j/∂p_j = −∫α_iP_ij(1−P_ij)dF < 0`、`∂s_k/∂p_j = ∫α_iP_ijP_ikdF > 0` 在线性 `−α_i p_j` 下正确；文中明确提醒不能与 `α log(y−p)` 版混用 |
| A9 | 项目 `DERIV-LAMBDA-01`、`RANGE-DERIV-01`、`CF-SHAPLEY-01`、`SUP-JAC-01` | 独立推导 | **PASS** | `∂P_ij/∂λ_i=−α_iP_ij(G_ij−Σ_kP_ikG_ik)`、`∂E[(D−R)_+]/∂R=−Pr(D>R)`、Shapley 权重、`Δ=−(Jᵀ⊙H)` 全部正确 |
| A10 | Fournel 半对数百分比更正 | `exp(b)−1` | **PASS** | `exp(0.267)−1=+30.6%`、`exp(−0.667)−1=−48.7%`，Codex 的更正正确 |

## B. 交付完整性层（我独立复算）

| # | 声明 | 复算结果 | 判定 |
|---|---|---|---|
| B1 | 主报告 SHA256 `844E0BE4…D22FCA` | 完全一致 | **PASS** |
| B2 | 公式账本 SHA256 `8F7E7B15…99CAEA` | 完全一致 | **PASS** |
| B3 | iter5 统一模型 SHA256 `D25C407EF1C7EF97E1F4DCE8C1B7A000CAEB76D0C495AB411C85FA2B72C4465E` | 完全一致 | **PASS** |
| B4 | 主报告"80 个展示公式、80 唯一 ID、账本零缺失零孤儿" | 实测 80 个 `formula-id`，全唯一，全部在账本中 | **PASS** |
| B5 | iter5"78 标签全唯一、账本 78/78 覆盖" | 实测 78 个 `\tag{}`，全唯一，账本零缺失零孤儿 | **PASS** |
| B6 | iter5"行内 284/284、行间 79/79、aligned 3/3、零乱码" | 实测完全吻合，U+FFFD 计数 0 | **PASS** |
| B7 | iter3"70/70 组公式配对、70 唯一标签" | 实测 70 个 `\tag{}`，全唯一，账本零缺失 | **PASS** |
| B8 | iter4"新增 15 组公式" | 实测 15 个 `\tag{}`，全唯一 | **PASS** |
| B9 | 三份终审 `RELEASE PASS` 均绑定同一 model SHA | 三份文件头部 SHA 与 B3 一致 | **PASS** |
| B10 | "MinerU 强化公式 OCR 未成功，改用 300 dpi 原页人工复核" | `mineru-api-client-*` 输出目录确为空 | **PASS（诚实记录）** |

## C. 文献事实层

| # | 被核对象 | 核验方式 | 判定 | 结论 |
|---|---|---|---|---|
| C1 | Li (2026) 系数 0.8005/1.1666 与标准误 0.1942/0.2533 | 直接读原 PDF 第 10 页 Table 4 | **PASS** | 数字完全一致 |
| C2 | "两者分别与 1 的差异都不显著；有统计支持的是两类权重之差" | 原文报 `γ_diff = 0.3661***(0.1124)`，t≈3.26 | **PASS** | Codex 结论正确。**注意**：按独立性自拼 SE≈0.32 会误判为不显著，说明两估计强正相关，必须用作者报的差值 SE |
| C3 | "Li 用 2022–2025 车型—城市—月数据" | 原文 §3.1 | **PASS** | June 2022 – June 2025，model-city-month，1,146,659 观测 |
| C4 | Li 的 RCL 列可信度 | 我另行读表 | **新增 CAVEAT** | 该列 `Σ_α = 0.0010 (0.8451)` 完全测不准，`Σ_x(NEV) = 2.5828***`；异质性几乎全落在 NEV 品味上，`γ` 与 NEV 随机系数分离很弱。这是可写进定位段的额外弹药 |
| C5 | 工信部 11 组同代码配对百分比 | 逐行复算 | **PASS** | 全部正确（6.71/6.79/5.85/5.93/5.47/6.19/6.93/6.93/3.25/−10.71/−13.46） |
| C6 | 四个国标发布/实施日期 | 与报告附录官方链接一致 | **PASS（未上网复核）** | 报告已给 samr.gov.cn 官方标准页链接；本轮未联网，按已记录的原文入口采信 |

## D. 语料记忆层

| # | 被核对象 | 判定 | 结论 |
|---|---|---|---|
| D1 | 28 篇语料的类型分布 | **CORRECTED** | 两次构建不一致：atlas(2026-04-17) 14/10/4 vs 增强建(2026-04-18) 17/9/1/1。逐篇比对**恰好 4 篇不同，全部是增强建往上升级**：`I6ZAU5HX`、`JDV2EEV6`、`EPWJ8S9T`、`B9VX97UN` |
| D2 | `I6ZAU5HX` = canonical BLP demand-supply | **CORRECTED（硬错）** | 索引写 canonical，**它自己的卡片第 60–61 行写 "reduced-form policy evaluation / difference-in-differences plus synthetic controls"**。同一构建内部自相矛盾，这篇没有结构需求系统。判据：canonical 须同时具备份额反演 + 多产品 Bertrand FOC + 边际成本反推 |
| D3 | 语料 APA 串 | **CAVEAT** | 统一缺卷期页（Li 2018 ReStud 缺 85(4),2389–2428；Clinton & Steinberg 缺 JEEM 98,102255）。进正文前必须走 `apa-citation` |
| D4 | SOURCE_MAP.csv 里的 40 条来源路径 | **CAVEAT** | 其中 `C:\Users\于\.codex\*` 全部已失效（Codex home 已迁到 `D:\codex\.codex-home\`）；另有 6 条 `D:\codex\*` 原位文件已不在。zip 与其解包目录是唯一完整副本 |
| D5 | `D:\codex\econ-model-agent\src\` | **CAVEAT** | 已被删；`blp.py` 等结构代码只存在于解包件 `07_structural_model_code\` |
| D6 | 三级证据分层（fulltext-grounded / manual close reading / equation-proof-level） | **PASS** | 这套分层设计正确且本项目确实遵守（例如明确不把在线附录算作已读、不把 UUID .tmp 缺失文件计入分母、不冒充 MinerU OCR 成功） |

## E. 设计判断层（我同意的部分）

| # | 判断 | 我的评价 |
|---|---|---|
| E1 | 2021 日历切换不是主 RD | **同意。** 阈值附近同时有疫情、芯片、补贴与双积分、换代、清库、季节性，横截面连续性不可信；无差异边界是"边际消费者"刻画，不是外生 running variable |
| E2 | B0 必须是"类型分布退化"而非"先取均值再代入" | **同意且重要。** `G(E[ω]) ≠ E[G(ω)]`，取均值版不能参加"方差归零回到基准"的等价测试 |
| E3 | 不把动力类型当主 nest | **同意。** 否则把要估的跨动力替代写进误差结构 |
| E4 | `χ = γ/α` 逐消费者算，`E[γ/α] ≠ E[γ]/E[α]` | **同意。** 另注：Li (2026) 把 γ 写在括号内直接估比率，规避了这个问题，是可借鉴的参数化 |
| E5 | 份额反演后的拟合值送回简约式不算验证 | **同意，且是本套材料里最有价值的一条方法论。** 反演令 `s^model=s^obs`，那是恒等式 |
| E6 | 宣传楔子 `D` 不能升级为认证楔子 `G` | **同意。** 这条把"证据能支持什么"和"想说什么"分开，是整套证据包的价值所在 |
| E7 | Shapley 只能分配已分别识别的机制 | **同意。** 复合项 `γ·a·ϑ` 拆成三个"因果贡献率"是假的 |
| E8 | 审计通过 ≠ 排除限制成立 | **同意，且已写进两个 skill 的红线** |

## F. 未能核验

| # | 对象 | 原因 |
|---|---|---|
| F1 | `01dcafaa-…-.tmp` 等四个 UUID 文件 | 文件不存在；Codex 已如实标记为 BLOCKED，未推测论文身份。**做法正确** |
| F2 | 各篇原文在线附录 | 本地 PDF 未包含；Codex 已明确不算作已读 |
| F3 | 国标官方页当前内容 | 本轮未联网 |
| F4 | Fournel / Allcott 原文公式问题的 5+3 条 | 未开原 PDF 逐页复核；仅核了其中的半对数百分比换算（正确）。其余按 Codex 已记录的页码采信，**若要写进论文须自行复开原页** |

---

## 总判定

Codex 这套材料的**事实层与完整性层可信**：所有可机械复算的声明（哈希、公式配平、账本覆盖、百分比、系数）我全部复算通过，且它在做不到的地方（MinerU OCR 失败、文件缺失、在线附录）都如实标注而没有虚报。
**需要修正的是三处**：BLP walkthrough 的 (6.9b) 漏负号（实质错误，会传播到 markup 与福利）；语料分类里 `I6ZAU5HX` 的 canonical 标签与自己的卡片矛盾（另有 3 篇跨构建不一致）；APA 串统一缺卷期页。
这三处已写进 `C:\Users\于舒奕\.claude\skills\blp-model-building\references\` 与 Claude 记忆，调用 skill 时会自动带出。

---

## G. 2026-10-07 修正记录（Claude Opus 5.5）

| # | 对象 | 动作 | 判定 |
|---|---|---|---|
| G1 | (6.9b) 原页复核 | 重新打开 `D:\codex\output\blp_driving_cycle_structural_research_20260824\audit_pages\blp_pdf_p26.png`（journal p.865） | **PASS**：原页积分号内确有前置负号；`f_j(ν, ξ, …)` 与 `∂μ_ij/∂p_q` 两处印刷笔误也确认 |
| G2 | walkthrough 8 份副本 | 脚本 `D:\blp-structural-skill-config\work_20261007\fix_walkthrough_69b.py` 逐份替换第 31 条交叉导数块，补负号、写 `∂μ_iq/∂p_q`、加 q≠j 与带日期的更正说明；每份断言旧块恰好出现一次 | **FIXED**：两组内容新 SHA-256 为 `FDDE3C60…` 与 `2DC2055E…`，8 份均验到负号、`μ_iq` 与更正说明各 1 处 |
| G3 | 0824 包完整性清单 | `FILE_INVENTORY.csv` 两行改为新大小、时间、SHA-256；`PACKAGE_MANIFEST.md` 追加 Post-pack Amendment | **DONE**：CSV 往返序列化先验证字节一致后才改写 |
| G4 | 0809 bundle | `_README.md` 追加修订说明；`_bundle_manifest.csv` 只记大小不记哈希，保持原样 | **DONE** |
| G5 | 其他转录 (6.9b) 的文件 | 全盘 grep `6.9b` 与交叉导数写法 | **PASS**：`structural_demand_referee.md` 用准线性特例，符号正确；`blp_1995_deep_reading_notes.md` 只列式号；Modern IO 教材 OCR 里的 6.9b 是图号 |
| G6 | 未改动 | `D:\codex\BLP_structural_models_memory_skills_configs_2026-08-24.zip` 是归档快照，内含旧版，未改 | **CAVEAT** |

修改前的 8 份原件与旧 `FILE_INVENTORY.csv` 备份在 `D:\blp-structural-skill-config\work_20261007\backup_before_69b_fix\`。

---

## H. 2026-10-07 第一轮盲评后的修正（Claude Opus 5.5）

第一轮评审意见逐条处理如下（评审报告与分数另存评审目录，不在本账本里）。下表每条都由我对原文或数值重新核过才改，没有直接采信评审意见。

| # | 对象 | 核验 | 改动 | 判定 |
|---|---|---|---|---|
| H1 | Xing, Leard & Li (2021) 替代方向 | 原文 `D:\数据说明段_支撑文献md包_20260930\14_Xing_Leard_Li_2021_JEEM_电动车替代了什么_原文.md` 第 30 行：被替代汽油车的燃油经济性比车队平均高 4.2 mpg，12% 替代混动，忽略非随机替代会把减排收益高估 39% | blp `extension_genealogy.md` X2 改正；原稿把 fuel economy 误译成"油耗" | **FIXED** |
| H2 | Gillingham, Houde & van Benthem 边界式 | Python 复算：`ΔWTP = ΔP − P_0·(ΔQ/Q)/η_D` 在 P_0 = 24,500 时复现期刊表 7 六格（498/600/335/355/90/−12），在 P_1 = 24,206 时复现工作论文表 D.1 十格（`D:\fuel-econ-lit-2026\raw_text\P17_w25845.txt` PAGE 52；其表注写的是 24,500）；脚注 26（同文件第 3192 行）的 `ΔP + ΔP·ΔQ/η_D` 在所有格子都约等于 294，是笔误 | blp B1 改为 [D] 反推式并记笔误；项目文件第 18 节第 1 条；P15 卡 `D:\fuel-econ-lit-2026\cards\P15_Gillingham2021_消费者短视_精读卡.md` 加更正注；记忆 `reference_cycle_switch_identification_paths.md` 与 `reference_blp_extension_genealogy.md` 改正；自检 T4a–T4c | **FIXED** |
| H3 | Alé-Chilet 等 (2026) 式 (13) 符号 | `D:\auto-demand-lit-2026-09\fulltext\J10.txt` 第 1120–1127 行定义 `S_jh = −∂s_h/∂p_j`，却印 `mc = p + (Ω⊙S)^{-1}s`；两产品 logit 数值验证照抄得 mc > p | blp S3 写明正确式 `mc = p − (Ω⊙S)^{-1}s`；SKILL.md 常错第 3 条列入；10-02 报告 `D:\blp-lit-recommend-20261002\BLP经典改造与近期改造文献推荐_20261002.md` 第 67 行加更正注；自检 T5 | **FIXED** |
| H4 | 动态离散选择识别 | Magnac & Thesmar (2002) 与 Abbring & Daljord (2020) 经 Crossref 核实；Chou & Derdenger (2025) 原文 `D:\auto-demand-lit-2026-09\fulltext\J07.txt` 第 60–72、168–182 行 | structural `when_and_which_model.md` 两行与 `mechanism_construction_and_theory.md` 动态一行改为"贴现因子与流量效用不能同时非参数识别"；新增 `estimation_recipes.md` 第 3 节 | **FIXED** |
| H5 | Small–Rosen 式 (4.4) | 卡片 `D:\codex\output\blp_driving_cycle_structural_research_20260824\iteration5_welfare_nested_pricing_20260825\03_pass1_cards\small_rosen_pass1.md`：(4.4) 是 `∂e/∂q = −(1/λ)∂v/∂q` | blp `micro_foundations.md` §8(a) 改标注 | **FIXED** |
| H6 | "交叉导数非负"验收项 | Remmy (J01) 在间接网络效应下报告负交叉价格弹性 | SKILL.md 与 `estimation_algorithm_and_code.md` §4 限定为无网络或互补项的模型 | **FIXED** |
| H7 | Conlon–Gortmaker (2020) 的 [O] 标签 | 新渲染 p.7、9、12 页图，连同原有 p.5、6、8、19，存 `D:\blp-structural-skill-config\work_20261007\pageimg\` | [O] 只留给这七页；其余页标文本层；记下 p.8 脚注 17 的 `α_i > 0` 与式 (26) 的 `α_i = ∂u/∂p < 0` 同文两种约定 | **FIXED** |
| H8 | structural 次要项 | Weyl–Fabinger 结论限垄断或对称寡头（Kaneko & Toyama p.196）；θ 定义在共同成分 w̄_d 上；"三条""五步"计数；目录级引用改为文件加行号 | 逐条改正；`identification_and_claim_ladder.md` 补 9 处本机来源 | **FIXED** |
| H9 | 可操作性缺口 | 新脚本全部在本机跑通：`blp_selftest.py` 8 组 19 项 ALL PASS（系统 Python 3.12.5 + numpy 2.3.3 与隔离虚拟环境均通过）；`pyblp_minimal_example.py`（pyblp 1.2.0，Nevo 规格，CHECKS PASS）；`structural_selftest.py` 8 项 ALL PASS | blp 加 `scripts\` 两个脚本；structural 加六层递进表、六类模型族路由、`estimation_recipes.md` 与 `scripts\structural_selftest.py`；三个脚本加 UTF-8 输出，避免 GBK 控制台打印希腊字母时崩溃 | **DONE** |
| H10 | 新增经典引文 | 20 条（Rust、Hotz–Miller、Magnac–Thesmar、Abbring–Daljord、BBL、Aguirregabiria–Mira、Bresnahan–Reiss、Ciliberto–Tamer、GPV、OP、ACF、DLW、Choo–Siow、Allen–Arkolakis、Chetty、Tamer、McFadden、Pakes–Pollard、Hansen、Weyl–Fabinger）Crossref 题名重合度全部 1.0，输出 `D:\blp-structural-skill-config\work_20261007\crossref_canonical_output.txt` | 只写作者、年份、期刊，卷期页与 DOI 留在输出文件里 | **PASS** |
| H11 | 未改动 | 评审建议把项目文件第 1–13 节压成变更记录 | 保留原文，只在文件顶部加"第 0–13 节各节现状"，逐节写明仍有效或已被哪一节取代。理由是第 2、4、6、7、9、11、13 节仍是现行口径，删掉会丢信息 | **KEPT** |

---

## I. 2026-10-07 第二轮评审后的修正（Claude Opus 5.5）

第二轮评审意见逐条处理如下。每条同样先核原文或重跑数值再改。

| # | 对象 | 核验 | 改动 | 判定 |
|---|---|---|---|---|
| I1 | blp 项目文件第 18 节 θ 定义 | `D:\blp-cycle-did-design\AGENT_REVIEW_SYNTHESIS_20260826.md` 第 14–20、177–197 行：理性更新者对产品特有成分反应，[0,1] 只对共同换尺成分成立 | 改为与 structural `mechanism_construction_and_theory.md` 第 3(c) 节同一定义 `θ = (∂ln q/∂w̄_d)/(∂ln q/∂log π)` | **FIXED** |
| I2 | blp 项目文件第 13 节"可以写：识别…资本化" | 台账 `03_model_identification_update.md` 第 132 行"否则识别的是复合资本化不足"、`04_go_no_go_and_next_steps.md` 第 4 节 | 改为"在所设里程、持有期、折现与信念校准下估计复合资本化比率；有微观矩时才写识别" | **FIXED** |
| I3 | pyblp 示例的估计结果 | pyblp 1.2.0 源码 `Problem.solve` 的 `sigma_bounds` 说明：支持边界的优化器下 σ 对角元默认非负。本机重跑：不设界 BFGS（gtol 1E-5）目标 4.5615、价格系数 −62.73、投影梯度 5.6E-06、约化 Hessian 特征值最小 3.2E-05，σ_sugar = −0.0058；L-BFGS-B 默认下界时 σ_sugar 卡在 0、目标 4.7214、价格系数 −60.18。输出 `D:\blp-structural-skill-config\work_20261007\pyblp_example_run_r3.txt` | 示例改用不设界 BFGS 并打印诊断，诊断不过即 CHECKS FAILED；`--show-bound-trap` 复现下界陷阱；`estimation_algorithm_and_code.md` 第 0.4 节给"非负约束不必需"加上积分节点须对称的限定，第 6 节换成新结果 | **FIXED** |
| I4 | `micro_foundations.md` 第 11 行页图清单 | 页图目录实有 p05、06、07、08、09、12、19 七张 | 改列七张 | **FIXED** |
| I5 | `blp_selftest.py` 的 T1c、T1d、T3 是恒等式 | 读码属实（T1d 乘字面 0.0；T1c 把已知为正的值取反；T3 代数恒等） | T1c、T1d 改为与有限差分 Jacobian 比，∂μ/∂p 由模型数值求出；T3 先用数值导数解出单产品 Bertrand 均衡再对闭式；19 项 ALL PASS | **FIXED** |
| I6 | structural 账本协议第 4 节标题计数 | 节内是五处原文问题加三处约定差异 | 标题改为"五处原文问题与三处约定差异" | **FIXED** |
| I7 | J07 引用行号 | `D:\auto-demand-lit-2026-09\fulltext\J07.txt` 第 60–64 行（估出含贴现因子的全部原语、不限定信念）、第 168–176 行（现有 DDC 识别结果不适用）、第 209–211 行（比现有文献多恢复贴现因子） | `when_and_which_model.md` 与 `estimation_recipes.md` 按这三处分别引用，删去"多数文献把贴现因子当已知"这句较强的转述 | **FIXED** |
| I8 | `structural_selftest.py` 的 T6b 自比自、T3 只覆盖线性 | 读码属实 | T6b 改为同一模型同一抽样、类型 `ω*·exp(σz)`：σ = 0 恰等于基准，差距按 σ² 收缩（5.0E-03、1.3E-03、3.2E-04）；T3 改名为线性特例，`estimation_recipes.md` 第 2 节写明 `(1 + 1/S)` 恰好成立的条件（频率模拟器或同结构模拟样本），光滑模拟器放大更小 | **FIXED** |
| I9 | 评审建议的配方缺口 | 新增三项数值检验均在本机通过：T7a Hotz–Miller CCP 映射在真值处为不动点；T7b 两步 CCP 估计还原 (0.254, 3.04)；T8 GPV 反推估值内部平均误差 0.0016；T9 DLW 比值等于 P/MC = 1.5 | `estimation_recipes.md` 第 3 节加 CCP 最小配方与 Hotz–Miller 估值公式，新增第 7 节六类模型族各一条路由级配方（全部 [D]）；新增引文 Bond, Hashemi, Kaplan & Zoch (2021) 与 Levinsohn & Petrin (2003) 经 Crossref 核实，输出 `D:\blp-structural-skill-config\work_20261007\crossref_round3_output.txt`；NFXP 外层由 Nelder-Mead 改为 BFGS，与"不要用 Nelder-Mead"一致 | **DONE** |
| I10 | 未改动 | 评审仍建议把项目文件被取代的第 5、8、12 节移到附录 | 保留，理由同 H11 | **KEPT** |
