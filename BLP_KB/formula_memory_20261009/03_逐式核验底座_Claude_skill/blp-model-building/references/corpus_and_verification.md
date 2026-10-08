# 本机 BLP 语料地图与核验纪律

## 0. 2026-10-07 复核补记

- 下表七层路径全部仍在。逐项清单（全部 Claude/Codex 记忆与 skill、项目目录、重复副本）见 `D:\blp-structural-skill-config\BLP与结构模型_记忆和skill清单_20261007.md`。
- **walkthrough 的 (6.9b) 漏负号已于 2026-10-07 在全部 8 份副本中修正**（补负号、改写为 `∂μ_iq/∂p_q`、加带日期的更正说明），记录见 `D:\blp-structural-skill-config\VERIFICATION_LEDGER.md` G 节；0824 包的 `FILE_INVENTORY.csv` 已更新哈希；归档 zip 未改，内含旧版。
- 新增第八层 **Codex agent**：`D:\codex\.codex-home\agents\blp-professor.toml`、`structural-professor.toml`，私有记忆在 `D:\codex\economics_theory_agent_complete_gpt55_xhigh\kb\08_hypothesis_packaging_45\agent_memories\`。
- 08-25 以后新增语料：燃油经济性 17 篇 `D:\fuel-econ-lit-2026\`、需求侧结构模型 49 篇 `D:\auto-demand-lit-2026-09\`、BLP 改造篇 `D:\blp-lit-recommend-20261002\`、纠错台账 `D:\codex\research-memory\fuel_econ_lit_2026_refresh_20260920\`。怎么用见 `extension_genealogy.md`。
- **检索索引已重建**（2026-10-07）：`D:\econ-research-craft-config\index.jsonl` 由 1,046 块扩到 4,156 块，收入两个结构 skill、28 篇论文记忆、中文精读、全文记忆、atlas、40 篇笔记、iteration3–5 精读卡、燃油经济 17 篇、需求侧 49 篇、09-20 台账、工况 DiD 十轮、项目报告、Codex BLP skills、按节切分的 BLP 原文与按页切分的 PyBLP 原文。用法 `python C:\Users\于舒奕\.claude\skills\econ-research-craft\scripts\find_reference.py --query "<问题>" --corpus <标签>`，标签表见 `C:\Users\于舒奕\.claude\skills\econ-research-craft\references\retrieval-workflow.md`。旧索引备份 `D:\econ-research-craft-config\index.jsonl.bak_20261007`。

## 1. 七层资产（2026-08-25 全盘实测）

| 层 | 路径 | 内容 |
|---|---|---|
| 0 打包总集 | `D:\codex\BLP_structural_models_memory_skills_configs_2026-08-24.zip`；**已解包到** `D:\codex\research-memory\BLP_structural_models_memory_skills_configs_2026-08-24\` | 988 payload；`SOURCE_MAP.csv` 逐条来源与状态；`FILE_INVENTORY.csv` 每文件 SHA-256 |
| 1 活项目 | `D:\codex\output\blp_driving_cycle_structural_research_20260824\` | 见 `project_china_driving_cycle.md` |
| 2 增强语料 | `D:\codex\blp_structural_memory_2026-04-18\` | 28 篇 paper memory（`memories\papers\*.md` + `memories\json\*.json`）、4 份 master memory、`indexes\blp_paper_memory_index.json`、`manifests\blp_zotero_collection_manifest.json`、`audits\` |
| 3 全文/中文精读 | `D:\codex\blp_fulltext_memory_2026-04-17\`（41）、`D:\codex\research-memory\blp_chinese_close_reading_memory_2026-04-17\`（28 篇中文） | 故事阶梯、模型骨架、写作模仿 |
| 4 理论 agent KB | `D:\codex\economics_theory_agent_complete_gpt55_xhigh\kb\03_structural_models\`（foundations + blp_structural_corpus + classifications）与 `\kb\04_literature\structural_papers\`（28 卡）；镜像 `D:\econ_agent_local\` | 含 user-verified BLP 构造 walkthrough |
| 5 Codex skills | `D:\codex\.codex-home\skills\`：`blp-driving-cycle-structural-research`（项目路由）·`blp-structural-models-enhanced-memory`·`blp-fulltext-reading-memory`·`blp-model-improvement-map`·`auto-ev-structural-models` | Codex 侧入口 |
| 6 代码 | 解包件 `07_structural_model_code\` | `blp.py` 等 8 模块 |
| 7 深读包 | `D:\codex\research-memory\deep-reading\{blp40_20260403, blp40s_20260403, blp-writing-pack-2026-04-03}`；PDF 在 `research-memory\pdfs\blp_1995_citing_2026-03-21\`（15 篇）与 `pdfs\99BY6NKV_BLP_1995.pdf`；`blp.pdf` 在 `D:\codex\` | 40 篇综合稿 `blp40s_20260403\synthesis_structural_writing_memory.md`；atlas `research-memory\blp_model_atlas_2026-04-17.md`（181KB） |

**已失效路径**（SOURCE_MAP 里写着但现在不存在）：`C:\Users\于\.codex\*` 全部（真实 Codex home 已迁到 `D:\codex\.codex-home\`）；`D:\codex\blp_model_atlas_2026-04-17.md`、`D:\codex\output\structural_models_full_inventory_2026-04-23.*`、`D:\codex\output\wltc_cltc_blp_idea_integrated.md`、`D:\codex\blp-fulltext-reading-memory\`、`D:\codex\auto-ev-structural-models\`、`D:\codex\econ-model-agent\src\`。

## 2. ★ 语料分类标签的已知错误

同一批 28 篇，两次构建的类型分布不同：
- 2026-04-17 atlas：标准 BLP 需求-供给 **14** / 邻近政策模型 10 / 风格差异化需求 4
- 2026-04-18 增强建：canonical **17** / adjacent 9 / style 1 / related 1

逐篇比对**恰好 4 篇不一致，全部是增强建往上升级**：

| Key | 论文 | 2026-04-18 | 2026-04-17 |
|---|---|---|---|
| `I6ZAU5HX` | Clinton & Steinberg (2019) Providing the Spark, JEEM | canonical | 邻近政策模型 |
| `JDV2EEV6` | Li (2018) Better Lucky Than Rich, ReStud | canonical | 风格差异化需求 |
| `EPWJ8S9T` | Huse, Lucinda & Cardoso (2020) 巴西能效标签, Energy Policy | canonical | 风格差异化需求 |
| `B9VX97UN` | 挪威 BEV 异质消费者, TR Part C | BLP-related | 风格差异化需求 |

**硬错误**：`I6ZAU5HX` 索引写 canonical BLP demand-supply，而**它自己的 paper memory 卡片第 60–61 行写着 "reduced-form policy evaluation / difference-in-differences plus synthetic controls"** —— 同一次构建内部自相矛盾，这篇根本没有结构需求系统。

**判据**：称一篇为 canonical BLP demand-supply，必须在其卡片或全文里同时看到 ① 份额反演 ② 多产品 Bertrand FOC ③ 由 markup 反推边际成本。三缺一就降级。**索引里的 `classification` 字段不构成证明。**

## 3. 证据层级三分（引用时必须点明）

- `fulltext-grounded corpus read`：有原始 PDF + 页级 fulltext JSON/TXT + 结构化 paper memory。这是默认可宣称的层级。
- `manual close reading`：有人工强化/重写的笔记，或本次任务里逐节对照过页级全文/PDF。**不能从一篇推广到整个语料。**
- `equation/proof-level manual review`：公式、推导、证明步骤对原页逐条核过。没做过就绝不能宣称。

**绝不把三级压成一句"全部精读过"。** 给实质结论时，引具体那一篇的 APA 与其卡片/页级全文，不要只引语料 master memory。

## 4. APA 必修

语料里的 APA 串**统一缺卷期页**（例：Li (2018) ReStud 缺 85(4), 2389–2428；Clinton & Steinberg 缺 JEEM 98, 102255）。进正文前一律走 `apa-citation` 技能补齐并核实；Crossref 按相关度排序会让工作论文版压过期刊版，必做升级检查。语料里的 APA master 在 `D:\codex\blp_structural_memory_2026-04-18\memories\blp_apa_citation_master.md`。

## 5. 28 篇语料的可复用模式（master memory 提炼）

**构造模式**
1. 从一个具体的差异化选择对象出发（车型、EV vs ICE、家电、带标签产品、平台选项）；
2. 估计之前先讲清**缺失的政策相关边际**：替代、网络反馈、属性扭曲、配给、进入、替换；
3. 只有当收益要求反事实、福利或均衡传导时才上结构层；
4. 识别通常走故事里点名的那个内生边际：价格、充电站、产品属性、EV 存量、政策暴露；
5. 反事实的价值在于"被替代的是谁""价格或进入如何反应""放开反馈后哪种工具占优"。

**期刊分布**（28 篇）：AEJ:EP 5 · EER 2 · ERE 2 · ReStat 2 · AER 2 · JEEM 2 · ReStud 1 · JPE 1 · Energy Policy 1 · IJIO 1 · Energy Economics 1 · Econometrica 1 · RAND 1 · QE 1 · QJE 1 · JAERE 1 · JPAM 1 · TR-C 1 · EJ 1。

**写作模式**（40 篇深读包 + 28 篇语料一致）
故事阶梯：现实市场/政策争论 → reduced-form 回答不了替代、均衡与福利 → 自然过渡到结构模型。
**顶刊几乎从不把"我们用了 BLP"当卖点**；卖点是"这个结构模型让我回答了别的方法答不了的问题"。
贡献句模板：**existing work misses margin M; design D identifies M; that changes policy conclusion P.**
章节序：Intro → Background/Data → Model → Identification/Estimation → Results → Counterfactual/Welfare → Conclusion。数据与制度放模型之前，作用是为设定、市场定义与识别假设做前置正当化。
排序纪律：**baseline 在 mechanism 之前，mechanism 在 welfare 之前，welfare 在规范主张之前。**
文献综述按"缺失的边际"分组，不按作者时间排。

**高频词**（28/28 出现）：counterfactual · welfare · equilibrium · heterogeneity；其后 identification strategy 23 · fuel economy 21 · substitution 21 · discrete choice 20 · marginal cost 20 · GMM 19 · market definition 18 · IV 16 · outside option 15 · differentiated product 14 · markup 13 · random coefficients 12。

## 6. 深读包里的方法父文献（本机已双遍精读）

| 环节 | 论文 | 作用 |
|---|---|---|
| 事件事实与 rival explanations | Miller & Weinberg (2017) MillerCoors | reduced form 记事实 → 结构基准检验 → 外部材料约束机制 → 逐通道反事实 |
| aggregate + micro BLP 实现 | Conlon & Gortmaker (PyBLP micro data) | 抽样、权重、微观矩、第二选择与联合协方差的正确写法 |
| 非参数识别边界 | Berry & Haile (2024) | 防止从条件价格需求跨越到内生属性/标签的因果效应 |
| 内生属性与企业设计 | Barwick, Kwon & Li (2024) 属性型补贴与市场势力 | 价格 + 工程属性 + 成本的联合均衡；**但不等于操纵识别** |
| 未来成本资本化与 VMT | Lu (2023) | 有单位的生命周期成本与驾驶异质性；`γ` 不能无条件叫短视 |
| 价格反馈、福利与分配 | Durrmeyer (2022, EJ) 法国 feebate | 需求异质性 → 价格反馈 → 成本反推 → 均衡反事实 → 分配福利 |
| nested logit 误差结构 | Galichon | `λ^{NL} = 1 − ρ`，同巢相关 `= 2ρ − ρ²`；nest 参数**不是**行为机制参数 |
| NL/RC/RCNL 比较 | Grigolon & Verboven | 模型选择按替代、diversion、市场界定和反事实对象验证，不能只比平均弹性或 GMM 目标值 |
| 均衡定价求解 | Morrow & Skerlos | `ζ` 固定点较稳，但无唯一性定理；小残差 ≠ 利润最大 |
| 福利识别边界 | Bhattacharya | 收入效应下逐个体根求 CV/EV；质量变化不由选择概率点识别 |

2026-10-07 补充的方法父文献（本轮用于 `micro_foundations.md` 与 `estimation_algorithm_and_code.md` 第 0 节）：

| 环节 | 论文 | 本机位置与核验状态 |
|---|---|---|
| 模型、NFXP、容差、优化、积分、定价固定点、近似最优工具 | Conlon & Gortmaker (2020) *RAND* 51(4), 1108–1161（Crossref 2026-10-07 核实） | 全文 `D:\codex\research-memory\deep-reading\blp40s_20260403\fulltext\30_bfp23mj2.fulltext.txt`；p.5、6、19 原页已核（图在 `D:\blp-structural-skill-config\work_20261007\pageimg\`） |
| 离散选择福利的支出函数基础与 logsum 成立条件 | Rosen & Small (1979) NBER WP 319（正式版 Small & Rosen 1981 *Econometrica*） | 卡 `D:\codex\output\blp_driving_cycle_structural_research_20260824\iteration5_welfare_nested_pricing_20260825\03_pass1_cards\small_rosen_pass1.md` |
| nested logit 的随机效用表示 | Galichon (2022) *Econometric Theory* | 同目录 `galichon_pass1.md` |
| 微观矩的经典做法 | Petrin (2002) JPE | 只能看页面图 `D:\blp-lit-recommend-20261002\pageimg\petrin_p05–p19.png` |

**这六到十篇共同否定的做法**：把日历时点直接当 RD · 把改革后新旧标签差当纯外生冲击 · 把 `γ<1` 直接叫心理短视 · 把不同物理单位的指标换算后共用一个裸变量 · 从销量和价格 FOC 自动推出企业操纵。
