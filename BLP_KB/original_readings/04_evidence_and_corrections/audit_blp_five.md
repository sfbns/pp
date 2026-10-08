# 五篇 BLP 推荐准入审计（2026-10-07）

## question_received

从本地已有全文阅读记忆中选出恰好五篇可用于中国 NEDC→WLTC/CLTC 研究的真正 BLP 应用，并核验 PDF、个体记忆、页锚点及完成证明。不能用普通 logit、DID 或“引用过 BLP”的论文凑数。

## source_scope

阅读了本代理 QUESTION_PROTOCOL、blp_professor 私有记忆、BLP 基础/增强/扩展/驾驶工况/汽车 EV skills、20260920 fuel-economy MEMORY_MAP，以及相关的少量个体卡。没有重读全库。桥接45篇库没有被拿来证明任何论文是 BLP。

本次对下列四篇重开原始 PDF 关键模型页，并渲染后实际视觉检查公式；其余全文阅读状态继承各自可审计旧记录，不冒充本轮逐句重读。

## answer

最终推荐组合：

1. Grigolon, Reynaert & Verboven (2018)：未来燃油成本估值、里程异质性与资本化，RC-BLP + 多产品 Bertrand。
2. Reynaert & Sallee (2021), *Who Benefits When Firms Game Corrective Policies?*：真实与标记油耗差距；由信念专职代理另外核验其本地 PDF/BLP 实现和阅读证据。本代理不对未重开的模型页背书。
3. Barwick, Kwon & Li (2024), NBER WP 32264：RC-BLP + 价格、车重、电池容量内生属性。
4. Xing, Leard & Li (2021)：RC-BLP demand-only；以新车购买条件样本估计，没有外部选项，也没有供给重新定价。这一边界必须随推荐一起说。
5. Barwick, Kwon, Li & Zahur (2025, revised August 2025), NBER WP 33378：RC-BLP 下游需求/价格 + 上游电池讨价还价与干中学。用于长期扩展，不是即时标签需求的母本。

第2篇的最终路径和状态以另一代理交付为准；若其证据失败，不得将本清单写成“已完全确认五篇”。

### 精确本地来源（四篇本代理已核）

根目录 `R = D:\codex\research-memory\BLP_structural_models_memory_skills_configs_2026-08-24\01_primary_enhanced_corpus`。

|论文|原始 PDF|个体卡/记忆|全文层与完成记录|模型页|
|---|---|---|---|---|
|GRV2018|`R\source_pdfs\04_5twrwep3.pdf`|`R\memories\papers\04_5twrwep3.md`|`R\raw\fulltext\04_5twrwep3.fulltext.json`、同名 `.txt`；`R\audits\csv_manifest_fulltext_audit_2026-04-18.md`|PDF6–9=期刊198–201：效用/成本/份额；PDF15–18=207–210：GMM/IV/反演；PDF23=215：Bertrand成本恢复与均衡反事实|
|Xing2021|`R\source_pdfs\27_lxuzm7vx.pdf`|`R\memories\papers\27_lxuzm7vx.md`|`R\raw\fulltext\27_lxuzm7vx.fulltext.json`、同名 `.txt`；上述28篇审计|PDF8：式(12)与conditional新车市场限制；PDF9：式(13)首选/次选概率、式(14)MLE、式(15)反演；PDF9–10：价格IV与随机系数识别|
|P02 Barwick2024|`C:\Users\于舒奕\Downloads\w32264.pdf`|`D:\fuel-econ-lit-2026\cards\P02_Barwick_Kwon_Li_2024_精读卡.md`|`D:\fuel-econ-lit-2026\raw_text\P02_w32264.txt`；`D:\fuel-econ-lit-2026\CHECKPOINT.md`|PDF20=正文18：式(8)效用；PDF21=19：份额及价格/属性选择；PDF22–23=20–21：前沿、成本、价格/属性FOC；PDF24–25=22–23：IV/GMM/微观矩|
|P01 Barwick2025|`C:\Users\于舒奕\Downloads\w33378.pdf`|`D:\fuel-econ-lit-2026\cards\P01_Barwick_Kwon_Li_Zahur_2025_精读卡.md`|`D:\fuel-econ-lit-2026\raw_text\P01_w33378.txt`；上述CHECKPOINT|PDF13=正文11：式(2)RC-BLP效用；PDF14=12：式(3)下游Bertrand；PDF18–19=16–17：价格异质性、9个IV及104个微观矩；PDF20–22=18–20：干中学成本及经验IV|

这里表内 `R\...` 是精确根目录缩写，原始 PDF 和全文层均在本轮确认存在。旧路径 `D:\codex\blp_structural_memory_2026-04-18\source_pdfs\...` 和其 `raw\fulltext\...` 当前不存在，打包必须使用导入归档路径，不能沿旧卡直接复制失效路径。

### MD 与“公式修正”状态

- P02 全文中译 MD：`D:\fuel-econ-lit-2026\translations\P02_Barwick_Kwon_Li_2024_属性型补贴与市场势力_中译.md`。
- P01 全文中译 MD：`D:\fuel-econ-lit-2026\translations\P01_Barwick_Kwon_Li_Zahur_2025_把成本打下来_中译.md`（本轮确认精确文件名）。
- GRV、Xing 有个体阅读记忆 MD；本代理没有发现其“全文所有公式逐项修正”的完成证明。应明确称“阅读记忆 + 本次关键公式回源笔记”，不能称“全篇公式已修正”。
- 本次视觉核验只覆盖下面四个核心效用式。保留原译文并另附核验笔记比把未经核对的整篇MD统一改标签更诚实。

### 已观察完成状态

- GRV、Xing：各33页PDF、全文JSON `page_count=33`、33个非空页、对应TXT和个体memory存在。20260418审计写明28/28全文依据与个体卡完整；也明确不证明统一逐句人工精读或所有公式复核。
- P01、P02：PDF分别72/57页，对应raw页标记分别72/57；CHECKPOINT写明17/17卡片/全文中译完成及第二轮全文完整性复核。该记录也列出图形附录、表格抽取等限制。本轮没有把该历史记录升级为重新逐句精读。

### source-exact 核心公式（视觉回源）

**P01 PDF13/正文11，式(2)**：

```tex
U_{ijct}=\alpha_i(p_{jct}-\phi_{jct})+X_{jct}\beta_i+\xi_{jct}+\varepsilon_{ijct}.
```

原文价格项是正号；其 `alpha_i` 是有符号价格系数，不是 P02 的正成本权重。PDF18/正文16给 `alpha_i=alpha_1+alpha_{c(i)}/y_i+sigma_p nu_i^p`，不能直接换成 P02 的 lognormal 参数化，不能无据断言每个模拟消费者的系数均为负。

**P02 PDF20/正文18，式(8)**：

```tex
u_{ijmt}=-\alpha_i(\widetilde P_{jmt}-b_{jmt})+x_{jmt}\beta_i+\xi_{jmt}+\varepsilon_{ijmt}.
```

该页明确 `alpha_i=exp(alpha_1+alpha_2 log(y_im)+sigma_p nu_ip)`。原文后续对随机项分布的文字有需谨慎解释之处，最小核心笔记不应擅自重写其分布。

**GRV PDF6/期刊198，式(1)**：

```tex
u_{ijk}=x_{jk}\beta_i^x-\alpha_i(p_{jk}+\gamma G_{ijk})+\xi_{jk}+\varepsilon_{ijk}.
```

PDF7/199，式(2)：`G_ijk=E[sum_{s=1}^S (1+r)^{-s} beta_i^m e_jk g_ks]`。注意 `e` 为升/公里，不是升/百公里；中国L/100km资料必须除100。PDF8/200说明 `gamma rho` 与里程尺度非分别识别，须外部里程分布。故该文中的未来成本权重可作短视模块，但低资本化不能跳过信念、注意、寿命、折现与里程假设直接命名为短视。

**Xing PDF8，式(12)**：

```tex
u_{ij}=\sum_{k=1}^{K}x_{jk}\beta_k-\alpha_1\ln p_j+\xi_j
+\alpha_2\frac{\ln p_j}{Y_i}
+\sum_{kr}x_{jk}z_{ir}\beta^o_{kr}
+\sum_kx_{jk}v_{ik}\beta^u_k+\varepsilon_{ij}.
```

价格是对数价格，收入交互是 `ln(p_j)/Y_i`。PDF9式(15)是已观察份额减模型份额的log反演更新，不是一般线性logit份额回归。本文首选/次选MLE+反演后价格IV，是 BLP demand 的有边界实现，不应改写成canonical联合需求供给GMM。

四张已经打开看过的原文图：

- `D:\codex\output\blp_bundle_20261007\audit_pages\P01_PDFp13.png`
- `D:\codex\output\blp_bundle_20261007\audit_pages\P02_PDFp20.png`
- `D:\codex\output\blp_bundle_20261007\audit_pages\GRV2018_PDFp6.png`
- `D:\codex\output\blp_bundle_20261007\audit_pages\XLL2021_PDFp8.png`

## mechanism_chain

项目机制推论（不是上述论文已证明的中国结果）：工况/可见标签规则变化 → 消费者面对油耗或续航信号不同 → 预期使用成本或有效续航信念变化 → 车型与动力类型替代 → 厂商重新定价/工程属性调整 → 销量、福利与排放。GRV支持成本与里程模块；Xing支持异质替代与次选模块；P02支持内生属性供给模块；P01支持长期上游成本反馈，不能充当即时认知识别。

## predictions

若信念渠道成立，控制同硬件道路性能后，标签修订应改变消费者主观道路油耗预期；高预期里程者预期货币成本变化较大，选择反应条件性更大。若只发生口径变化且消费者已准确知道道路油耗、完全不使用标签，则标签数字本身不必改变购买效用。若供给渠道成立，价格/属性/组合可随补贴或测试规则变化；固定属性反事实不能冒充长期均衡。

## rival_and_falsifier

最近竞争解释是同步硬件改型、企业广告/披露、促销与补贴、充电条件和产品退出。保持硬件相同、测量实际展示日期、直接测主观道路油耗与标签认识、分别检验价格/工程/销售变化，可以判别。标签改但主观预期不改、只有真实属性改，削弱纯信念故事；所有消费者的品味参数改变不是默认解释。

## handoff

1. 信念代理完成R&S的精确版本/BLP/本地阅读证明；打包器据此锁定第五篇身份。
2. 打包器确认P01全文译文精确文件名，复制实际文件，生成所有包内相对链接与哈希清单。
3. 为GRV/Xing附“核心公式回源笔记”即可；如果用户需要完整全文逐公式修正，须另行逐式审核，不得以此次四张图代替。

## confidence_and_limits

四篇的模型分类、关键效用式及所述页锚为本轮原文核验；历史全文阅读完成边界来自可审计记录。追加任务已在本轮读完Xing33页全文（包括本地已包含附录、图表和参考文献），独立完成证明见同目录 `xing_completion_20261007.md`；此前对Xing“仅沿用旧阅读证据”的状态由该补证扩展。尚未回源R&S。本文没有证明标签改革的因果效应、消费者短视、完整micro-BLP识别或全篇MD公式无误。

### 排除与provenance纠错

- P04 Leard–Linn–Springel2023：个体卡明确为分组固定效应logit，作者明确放弃BLP随机系数。不计入“严格BLP五篇”；可以保留为供给竞争解释参考。
- P15 Gillingham–Houde–van Benthem2021：可见评级自然实验/价格资本化，不冒充RC-BLP；可附在原批次，但严格BLP短视主推荐用GRV。
- 旧库 `17_f8utg3xw.pdf`：实际91页学位论文，其中第2章与Springel主题相符，不是索引声称的2021 AEJ正式版。未进入五篇。
- 旧库 `22_p5d5gntw.pdf`：实际March9,2023工作论文，不能以QJE2024正式版身份打包；模型是BLP，但本次未采用。
