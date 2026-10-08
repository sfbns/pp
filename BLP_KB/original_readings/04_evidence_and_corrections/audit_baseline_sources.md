# BLP 基础与既往推荐档案：来源审计（2026-10-07）

## question_received

定位 BLP 基础原文、已存在的公式更正 MD、1994/2004 的可用性，以及 2026-10-02 既往五篇推荐与 Petrin 的原文和 MD。只读源文件，不把本轮定位升级为全篇精读。既往推荐档案不等于本轮正式五篇推荐。

## source_scope

- 已读本地任务协议、literature_scout 私有路由、orchestration-contract。
- 查询记忆注册表 MEMORY.md 第 214–216 行，路由至 20260920 燃油经济性校正层；该层原文件已在本轮重开。
- 已重开 `D:\fuel-econ-lit-2026\CHECKPOINT.md`、`manifest.json`，以及增强包 `PACKAGE_MANIFEST.md`、来源/语料索引。
- 已重开 `D:\blp-lit-recommend-20261002\BLP经典改造与近期改造文献推荐_20261002.md`、`CHECKPOINT.md` 与 `D:\blp-structural-skill-config\VERIFICATION_LEDGER.md`。
- Zotero 只读 SQLite `mode=ro` 首次查询报 `sqlite3.OperationalError: database is locked`。改为 `mode=ro&immutable=1` 后成功：只读主库快照，不读取正在写入的 WAL，不能宣称最新未落盘条目不存在。附件路径逐一实测存在；没有修改 Zotero、安装插件或改变配置。

## answer

### A. 本轮可打包的 BLP 原始基础

| 角色 | 已验证绝对路径 | 状态与许可 |
|---|---|---|
| 原始论文 PDF | `D:\codex\blp.pdf` | Berry, Levinsohn & Pakes (1995)，58 个 PDF 页，标题页刊载 Econometrica 63(4):841–890。本轮检查标题并重新打开期刊 p.865 / PDF 第26页的原页图。不是本轮全篇重读。 |
| 已有精读笔记 | `D:\codex\blp_1995_deep_reading_notes.md` | 自称以 PDF 为公式权威的已有深读笔记；10.6 节已写出自价格负、交叉价格正的正确导数。不是逐页全文翻译。 |
| 已更正 walkthrough MD | `D:\codex\research-memory\BLP_structural_models_memory_skills_configs_2026-08-24\03_economics_theory_agent\kb\03_structural_models\foundations\01-user-verified-blp-model-construction-walkthrough-2026-05-20.md` | 文件有 2026-10-07 更正说明，§31 修回 (6.9b) 前置负号并把导数索引改为 μ_iq。材料本身记录来源为 user-reported formula recheck，不应说成新认证的完整全文翻译。 |
| 同更正内容的 curated 源 | `D:\codex\research-memory\BLP_structural_models_memory_skills_configs_2026-08-24\03_economics_theory_agent\notes\curated\blp_model_construction_walkthrough_2026-05-20.md` | 与基础卡同为增强包的已修订副本。打包任选一份主阅读版，避免重复误计。 |
| 校正记录 | `D:\blp-structural-skill-config\VERIFICATION_LEDGER.md` | A3/A4、G1/G2 记录 6.9b 的原页依据与副本修复；A6 还提示原文 (6.13) 模拟器归一化疑问，不可宣称全书公式已无误。 |
| 本轮原页截图 | `D:\codex\output\blp_bundle_20261007\_baseline_audit\BLP1995_pdfpage26_journal865.png` | 本轮从 `D:\codex\blp.pdf` 渲染并目视复核，原页式 (6.9b) 确有前置负号，原页也确实印作 μ_ij 对 p_q 的导数。 |

原始 PDF SHA256：`A7F6E505C4CF2B2CE72BFEA5D700454571400E99F7AB9501F7AE9302CBE06D75`。同哈希 Zotero 附件：`C:\Users\于舒奕\Zotero\storage\7NJ3LIMT\1772521156_42578_b69d7d0b6a2dd2aedf3bb79d1b20fd96.pdf`。另一附件 `C:\Users\于舒奕\Zotero\storage\EF5MGVTH\99BY6NKV_BLP_1995.pdf` 实测存在但哈希不同，不应叫字节相同副本。

**不要直接复用旧 ZIP 作为已修正版。** 增强包 `PACKAGE_MANIFEST.md` 明示：`D:\codex\BLP_structural_models_memory_skills_configs_2026-08-24.zip` 仍含 6.9b 修正前的版本。

**1994 / 2004 缺口：** 已核增强包的 28 篇标题、相关本地索引和 Zotero 主库题名搜索。未定位 Berry (1994) *Estimating Discrete-Choice Models of Product Differentiation* 或 Berry–Levinsohn–Pakes (2004) *Differentiated Products Demand Systems from a Combination of Micro and Macro Data: The New Car Market* 的可用原文附件及完成阅读凭证。不能宣称全机不存在；本轮基础部分只装 1995 已足够，不把二者当作本地已读推荐。

### B. 2026-10-02 既往五篇 + Petrin：文件存在与类型

| 文献 / 旧推荐角色 | 原文 PDF（逐一路径实测存在） | 本地 MD / 记录（如实区分） |
|---|---|---|
| Grieco–Murry–Yurukoglu (2024)，旧五篇1 | `D:\auto-demand-lit-2026-09\原文PDF\J03_Grieco_2024_QJE_author.pdf`，67页；标题页为 March 9, 2023 作者稿 | 英文抽取 MD：`D:\数据说明段_支撑文献md包_20260930\08_Grieco_Murry_Yurukoglu_2024_QJE_美国汽车业市场势力演变_WP版原文.md`。已有阅读卡：`D:\codex\research-memory\BLP_structural_models_memory_skills_configs_2026-08-24\01_primary_enhanced_corpus\memories\papers\22_p5d5gntw.md`。未定位独立“逐式校正全文 MD”。 |
| Hong–Kim–Verboven (2026)，旧五篇2 | `D:\auto-demand-lit-2026-09\原文PDF\W07_Hong_2026_CEPR_author.pdf`，73页；标题页 September 2026 | 原文抽取为 TXT：`D:\auto-demand-lit-2026-09\fulltext\W07.txt`；阅读卡为 JSON：`D:\auto-demand-lit-2026-09\cards\W07.json`。未定位已有逐式校正全文 MD；若转换 TXT 为 MD，须标“格式转换，未新增公式核验”。 |
| Kaneko–Toyama (2025)，旧五篇3 | `C:\Users\于舒奕\Downloads\The J Industrial Economics - 2024 - Kaneko - Demand Estimation with Flexible Income Effect  An Application to Pass‐Through.pdf`，48页；正文刊载 March 2025 | 中文全文 MD：`D:\fuel-econ-lit-2026\translations\P10_Kaneko_Toyama_2025_弹性收入效应需求估计_中译.md`；原文 TXT：`D:\fuel-econ-lit-2026\raw_text\P10_Kaneko2024_JIE.txt`。CHECKPOINT 记录完整性复核与缺段补齐，不等于逐式校正通过。 |
| Barwick–Kwon–Li (2024)，旧五篇4 | `C:\Users\于舒奕\Downloads\w32264.pdf`，57页；NBER 32264，March 2024 | 中文全文 MD：`D:\fuel-econ-lit-2026\translations\P02_Barwick_Kwon_Li_2024_属性型补贴与市场势力_中译.md`；英文抽取 MD：`D:\codex\output\blp_driving_cycle_structural_research_20260824\iteration3_new_papers_20260824\01_ocr\barwick_kwon_li_attribute_subsidies_ev\text_layer.pages.md`；另一打包原文 MD：`D:\数据说明段_支撑文献md包_20260930\01_Barwick_Kwon_Li_2024_NBERw32264_属性型补贴与市场势力_原文.md`。抽取/译文不能泛称逐式修正版。 |
| Alé-Chilet–Chen–Li–Reynaert (2026)，旧五篇5 | `D:\auto-demand-lit-2026-09\原文PDF\J10_AleChilet_2026_REStud_journal.pdf`，37页，正式版 | 原文 TXT：`D:\auto-demand-lit-2026-09\fulltext\J10.txt`；阅读卡 JSON：`D:\auto-demand-lit-2026-09\cards\J10.json`。10-02 推荐报告已在10-07添加式(13)符号更正注，**这是报告校正，不是改过整篇原文 MD**。 |
| Petrin (2002)，旧经典改造篇 | `D:\codex\research-memory\pdfs\Z47HEXTA_Petrin_2002.pdf`，52页工作论文版；文字层坏字体，本轮确认提取为控制字符 | 已有短阅读笔记：`D:\codex\research-memory\deep-reading\blp40s_20260403\notes\25_z47hexta.md`；OCR MD：`D:\codex\research-memory\deep-reading\blp40s_20260403\ocr-25\25_z47hexta\25_z47hexta.llm.md`（仅路由，不能当可靠全文）。10-02 CHECKPOINT 明示仅 PDF 第5–19页经图像阅读，不是完整精读凭证。 |

旧推荐来源：[2026-10-02 报告](D:/blp-lit-recommend-20261002/BLP经典改造与近期改造文献推荐_20261002.md)。其自身明确：五篇近期论文只到全文定位及模型段人工阅读，未逐式推导；Petrin 仅相关页面图像读。不能替换为“这六篇已完整精读并逐式校正”。

### C. 17 篇 fuel-econ 批次与“公式修正后的 MD”边界

`D:\fuel-econ-lit-2026\translations` 的 17 个 MD 确实存在；`CHECKPOINT.md` 记录“逐篇全文中译（LaTeX公式）17/17”和第二轮全文完整性复核。其记录的是节标题、截断声明、缺段补齐和部分回源核验，不是 17 篇每一公式的独立审计。文件名没有“公式校正全文版”，也未定位一套后继逐式修订全文 MD。

可随包附加的纠错层为：

- `D:\codex\research-memory\fuel_econ_lit_2026_refresh_20260920\01_source_status_and_anchor_ledger.md`
- `D:\codex\research-memory\fuel_econ_lit_2026_refresh_20260920\02_project_relevance_and_correction_ledger.md`
- `D:\codex\research-memory\fuel_econ_lit_2026_refresh_20260920\03_model_identification_update.md`

其中 MEMORY_MAP 明示“本轮没有把17篇逐篇重新从第一页读到最后一页”，并撤回残值必然改变斜率、P10 不能表达续航曲率等旧说法。故推荐采用“已有全文译文 + 关键公式/主张校正账本”的诚实命名，不冒充“整篇已逐式校正版”。

## mechanism_chain

BLP 原始基准：异质消费者偏好与价格/属性 → 个体离散选择 → 聚合市场份额 → 多产品厂商定价一阶条件 → 份额反演与 IV/GMM → 需求、加价、成本和反事实。6.9b 是份额价格导数到供给侧加价矩阵的接口；漏前置负号会让替代品交叉导数与该接口失配。

## predictions

在当前 walkthrough 的 Cobb–Douglas 规格 μ_iq=α log(y_i-p_q)+…、α>0、y_i>p_q 下，自价格导数为负，交叉价格导数为正。这一检查是公式内生一致性，不是数据上的因果检验。原页式(6.9b)索引按经济意义更正后的计算式为：

\[
\frac{\partial s_j}{\partial p_q}=-\int f_j f_q\frac{\partial\mu_{iq}}{\partial p_q}\,dP_0>0,\quad q\ne j.
\]

## rival_and_falsifier

“原文抽取为 MD / 带 LaTeX 的翻译 / 精读卡 / 公式校正后的全文”是四种不同对象。反证现有批次已经逐式校正的直接证据是：原 CHECKPOINT 仍逐项列出原文公式问题，20260920 仍撤回旧主张，10-07 账本仍标 Fournel/Allcott 的5+3条没有新轮逐页复核。格式转换不能填补这个证据缺口。

## handoff

主执行者可以将上述六篇放入“既往推荐档案”，本轮正式五篇使用已确定的 P02 / GRV / Xing / R&S / P01，基础使用 BLP1995 PDF + 更正 walkthrough。若用户真正要每篇公式校正全文，需对入选 MD 的公式逐式回 PDF，并将修订应用于副本；不要把本次打包本身说成已完成全批次公式校正。

## confidence_and_limits

已验证：所有表列 PDF 路径存在，页数、标题页版本与哈希可取；1995 p.865 已目视重开；walkthrough 6.9b 更正说明存在。未验证：六篇全部公式、17篇全文译文逐式准确性、1994/2004 全机不存在或最新 Zotero WAL 中无条目。所有源文件保持只读，本轮新增仅本审计 memo 与原页图。
