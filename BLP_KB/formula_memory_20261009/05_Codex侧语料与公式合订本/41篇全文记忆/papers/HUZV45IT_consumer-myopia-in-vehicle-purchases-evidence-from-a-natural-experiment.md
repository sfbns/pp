---
name: paper_huzv45it_consumer-myopia-in-vehicle-purchases-evidence-from-a-natural-experiment
description: Fulltext memory for Consumer Myopia in Vehicle Purchases: Evidence from a Natural Experiment; stores story logic, BLP model construction, estimation, counterfactual use, and writing structure.
type: reference
---

# Consumer Myopia in Vehicle Purchases: Evidence from a Natural Experiment

## Citation
- Key: `HUZV45IT`
- DOI: `10.1257/pol.20200322`
- Journal: American Economic Journal: Economic Policy
- Year: 2021
- OCR source PDF: `D:\codex\tmp\blp_full_read_20260417\staged_pdfs\HUZV45IT.pdf`
- OCR JSON: `D:/codex/tmp/blp_full_read_20260417/parsed_all/HUZV45IT/HUZV45IT.llm.json`
- Digest JSON: `D:/codex/tmp/blp_full_read_20260417/digests/HUZV45IT.json`

## Read Status
- 本记忆基于全文 OCR 解析结果整理，不是只看题目、摘要或 Zotero 元数据。
- OCR 流程使用 MinerU 优先、DirectML 加速、输出 `llm.md` / `llm.json` / `chunks.jsonl`。

## Story Question
- A central question in the analysis of fuel economy policy is whether consumers are myopic with regards to future fuel costs.

## Story Logic
- 故事起点：A central question in the analysis of fuel economy policy is whether consumers are myopic with regards to future fuel costs.
- 制度/市场切口：A central question in the analysis of fuel economy policy is whether consumers are myopic with regards to future fuel costs.
- 模型推进：We examine the short-run equilibrium effects of a restatement of fuel economy ratings that affected 1.6 million vehicles.
- 结论落点：A central question in the analysis of fuel economy policy is whether consumers are myopic with regards to future fuel costs.

## BLP Model Memory
- BLP positioning: BLP-adjacent structural policy model
- Evidence hits: discrete choice, bertrand, welfare, instrument
- Demand side: 全文表明作者在做结构化产品需求分析，但 OCR 证据不足以把需求形式精确钉死到某个 logit 变体。
- Utility construction: 模型核心仍然是“价格 + 产品属性 + 未观测质量”决定选择概率，再由市场份额把需求参数识别出来。
- Heterogeneity: 异质性信息没有被 OCR 关键词强烈命中，但从论文主题看，替代关系至少在产品层面而不是代表性消费者层面展开。
- Supply side: 供给侧是显式的：通常包含多产品定价、边际成本恢复、markup 变化和均衡反事实。
- Identification / estimation: 识别主要靠制度冲击或自然实验，把外生变化灌进结构模型。
- Counterfactual / welfare: 模型的终点不是参数本身，而是福利、反事实和政策比较。

## Writing Memory
- 这篇文章的正文结构大体按下面的顺序推进：
- 1 Introduction
- 2 The 2012 Fuel-Economy Rating Restatement
- 3 Data
- 4 The Equilibrium Effects of the Restatement
- 5 Implications for the Valuation of Fuel Economy
- 6 Conclusions
- CONSUMER MYOPIA IN VEHICLE PURCHASES: EVIDENCE FROM A NATURAL EXPERIMENT
- ABSTRACT
- 4.1 Effects on Transaction Prices
- 4.1.1 Robustness Checks
- 4.1.2 Heterogeneous Effects on Transaction Prices
- 4.2 Effects on Other Outcomes?

## Reusable Writing Moves
- 先用自然实验或制度冲击把识别抓牢，再让结构模型回答 reduced-form 无法覆盖的替代和福利问题。
- 在模型章节之前先把市场、制度、样本和关键摩擦讲透，让后面的结构设定像是被场景推出而不是凭空假设。
- 把模型的价值落在反事实与福利，而不是只汇报需求系数和价格弹性。

## OCR Anchors
- abstract: `ABSTRACT` (p.1) - ABSTRACT A central question in the analysis of fuel-economy policy is whether consumers are myopic with regards to future fuel costs. We provide the first evidence on consumer valuation of fuel economy from a natural experiment.
- introduction: `1 Introduction` (p.2) - 1 Introduction The transportation sector is now the largest contributor of carbon dioxide emissions in the United States and emissions from petroleum constituted 45% of all energy-related carbon dioxide emissions in 2017.1 Fuel-economy regulations are the dominant policy to reduce carbon dioxide emissions from the transportation sector in the United States and many other countries, despite economists long arguing for a Pigouvian gasoline tax to internalize climate change (and other) externalities (Parry and Small 2005). Fuel-economy standards require automakers to meet average fuel-economy targets for new light-duty vehicles.
- background: `2 The 2012 Fuel-Economy Rating Restatement` (p.5) - 2 The 2012 Fuel-Economy Rating Restatement The restatement was made public on November 2, 2012, when EPA stated in a press release that “in processing test data, Hyundai and Kia allegedly chose favorable results rather than average results from a large number of tests.”7 This was a result of a 2012 EPA audit of the model-year 2012 Hyundai Elantra, which revealed a large discrepancy between the test results and the self-reported fuel economy provided by Hyundai. Based on this finding, EPA expanded its investigation to other Hyundai and Kia vehicles, uncovering many more discrepancies, all of which overstated fuel economy.
- data: `3 Data` (p.6) - 3 Data Our first dataset contains all dealer-reported new vehicle transactions in the United States from August 2011 to June 2014 from R.L. Polk.
- results: `4 The Equilibrium Effects of the Restatement` (p.7) - 4 The Equilibrium Effects of the Restatement
- counterfactual: `5 Implications for the Valuation of Fuel Economy` (p.12) - 5 Implications for the Valuation of Fuel Economy
- conclusion: `6 Conclusions` (p.18) - 6 Conclusions This paper exploits an unexpected restatement in the EPA-rated fuel economy for thousands of vehicles. A highly desirable feature of this natural experiment is that the vehicles themselves are identical before and after the restatement, providing us with a clean source of variation in expected future fuel costs by consumers.

## Memory Notes
- 后续回忆这篇论文时，优先调用它的故事梯子、模型嵌入位置、识别策略和反事实落点，而不是只记结论。
- 如果需要公式级别细节，可以直接回到对应 `llm.json` 的 equation chunks 与 model / estimation section。
