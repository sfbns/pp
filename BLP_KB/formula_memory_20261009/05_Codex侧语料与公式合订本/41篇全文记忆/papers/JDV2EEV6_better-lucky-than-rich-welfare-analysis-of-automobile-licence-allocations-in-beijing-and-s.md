---
name: paper_jdv2eev6_better-lucky-than-rich-welfare-analysis-of-automobile-licence-allocations-in-beijing-and-s
description: Fulltext memory for Better Lucky Than Rich? Welfare Analysis of Automobile Licence Allocations in Beijing and Shanghai; stores story logic, BLP model construction, estimation, counterfactual use, and writing structure.
type: reference
---

# Better Lucky Than Rich? Welfare Analysis of Automobile Licence Allocations in Beijing and Shanghai

## Citation
- Key: `JDV2EEV6`
- DOI: `10.1093/restud/rdx067`
- Journal: The Review of Economic Studies
- Year: 2018
- OCR source PDF: `D:\codex\tmp\blp_full_read_20260417\staged_pdfs\JDV2EEV6.pdf`
- OCR JSON: `D:/codex/tmp/blp_full_read_20260417/parsed_all/JDV2EEV6/JDV2EEV6.llm.json`
- Digest JSON: `D:/codex/tmp/blp_full_read_20260417/digests/JDV2EEV6.json`

## Read Status
- 本记忆基于全文 OCR 解析结果整理，不是只看题目、摘要或 Zotero 元数据。
- OCR 流程使用 MinerU 优先、DirectML 加速、输出 `llm.md` / `llm.json` / `chunks.jsonl`。

## Story Question
- Economists often favour market-based mechanisms over non-market based mechanisms to allocate scarce public resources on grounds of economic efficiency and revenue generation.

## Story Logic
- 故事起点：Advance access publication 17 November 2017 The editor in charge of this paper was Jerome Adda.
- 制度/市场切口：A uniform-price auction would have generated nearly 20 billion Yuan to Beijing municipal government, more than covering all its subsidies to the local public transit system 1.
- 模型推进：核心推进动作是把差异化产品需求或供给均衡模型嵌入实证问题，而不是停留在 reduced-form。
- 结论落点：When the usage of the resources in question generates type-dependent negative externalities, the welfare comparison can become ambiguous.

## BLP Model Memory
- BLP positioning: BLP-style differentiated-product demand
- Evidence hits: random coefficients, discrete choice, welfare, counterfactual, instrument, gmm
- Demand side: 全文表明作者在做结构化产品需求分析，但 OCR 证据不足以把需求形式精确钉死到某个 logit 变体。
- Utility construction: 模型核心仍然是“价格 + 产品属性 + 未观测质量”决定选择概率，再由市场份额把需求参数识别出来。
- Heterogeneity: 异质性是关键层：作者依赖收入、偏好差异、使用场景或消费者类型来刻画不同群体的替代弹性。
- Supply side: 供给侧并非完全缺席，作者至少把进入、定价或市场结构响应嵌进均衡框架。
- Identification / estimation: 识别依赖工具变量、GMM 或其他矩条件来处理价格与产品属性的内生性。
- Counterfactual / welfare: 模型的终点不是参数本身，而是福利、反事实和政策比较。

## Writing Memory
- 这篇文章的正文结构大体按下面的顺序推进：
- 1. INTRODUCTION
- 3.1. Background
- 3.3. Data description
- 5. IDENTIFICATION AND ESTIMATION
- 7. WELFARE ANALYSIS
- 8. CONCLUSION
- Better Lucky Than Rich? Welfare Analysis of Automobile Licence Allocations in Beijing and Shanghai
- SHANJUN LI Cornell University and NBER
- REVIEW OF ECONOMIC STUDIES
- SHANJUN LI LOTTERY VERSUS AUCTION IN LICENSE ALLOCATION
- 2. ALLOCATION MECHANISMS AND EXTERNALITIES
- 3. POLICY AND DATA DESCRIPTION

## Reusable Writing Moves
- 在模型章节之前先把市场、制度、样本和关键摩擦讲透，让后面的结构设定像是被场景推出而不是凭空假设。
- 把模型的价值落在反事实与福利，而不是只汇报需求系数和价格弹性。

## OCR Anchors
- introduction: `1. INTRODUCTION` (p.0) - 1. INTRODUCTION Market-based mechanisms (e.g.
- background: `3.1. Background` (p.7) - 3.1. Background During the past three decades, China has embarked on an extraordinary journey of economic growth with its GDP growing at about 10% a year.
- data: `3.3. Data description` (p.9) - 3.3. Data description Our analysis focuses on policies in Beijing and Shanghai and we bring two nearby cities, Nanjing and Tianjin into analysis to facilitate identification.
- estimation: `5. IDENTIFICATION AND ESTIMATION` (p.17) - 5. IDENTIFICATION AND ESTIMATION
- counterfactual: `7. WELFARE ANALYSIS` (p.28) - 7. WELFARE ANALYSIS The purpose of this section is to compare welfare consequences under the lottery and auction systems and we focus on 2012 for illustration.
- conclusion: `8. CONCLUSION` (p.36) - 8. CONCLUSION Air pollution and traffic congestion are arguably two of the most pressing issues for China’s urban residents.

## Memory Notes
- 后续回忆这篇论文时，优先调用它的故事梯子、模型嵌入位置、识别策略和反事实落点，而不是只记结论。
- 如果需要公式级别细节，可以直接回到对应 `llm.json` 的 equation chunks 与 model / estimation section。
