---
name: paper_jkyit7sd_hurdles-and-steps-estimating-demand-for-solar-photovoltaics
description: Fulltext memory for Hurdles and steps: Estimating demand for solar photovoltaics; stores story logic, BLP model construction, estimation, counterfactual use, and writing structure.
type: reference
---

# Hurdles and steps: Estimating demand for solar photovoltaics

## Citation
- Key: `JKYIT7SD`
- DOI: `10.3982/QE919`
- Journal: Quantitative Economics
- Year: 2019
- OCR source PDF: `D:\codex\tmp\blp_full_read_20260417\staged_pdfs\JKYIT7SD.pdf`
- OCR JSON: `D:/codex/tmp/blp_full_read_20260417/parsed_all/JKYIT7SD/JKYIT7SD.llm.json`
- Digest JSON: `D:/codex/tmp/blp_full_read_20260417/digests/JKYIT7SD.json`

## Read Status
- 本记忆基于全文 OCR 解析结果整理，不是只看题目、摘要或 Zotero 元数据。
- OCR 流程使用 MinerU 优先、DirectML 加速、输出 `llm.md` / `llm.json` / `chunks.jsonl`。

## Story Question
- This paper estimates demand for residential solar photovoltaic (PV) systems using a new approach to address three empirical challenges that often arise with countdata: excess zeros, unobserved heterogeneity, and endogeneity of price.

## Story Logic
- 故事起点：This paper estimates demand for residential solar photovoltaic (PV) systems using a new approach to address three empirical challenges that often arise with countdata: excess zeros, unobserved heterogeneity, and endogeneity of price.
- 制度/市场切口：Our re-sults imply a price elasticity of demand for solar PV systems of -0/periodori65.C o u n t e r factual policy simulations indicate that reducing state financial incentives in halfwould have led to 9%fewer new installations in Connecticut in 2014.
- 模型推进：核心推进动作是把差异化产品需求或供给均衡模型嵌入实证问题，而不是停留在 reduced-form。
- 结论落点：Our re-sults imply a price elasticity of demand for solar PV systems of -0/periodori65.C o u n t e r factual policy simulations indicate that reducing state financial incentives in halfwould have led to 9%fewer new installations in Connecticut in 2014.

## BLP Model Memory
- BLP positioning: BLP-adjacent structural policy model
- Evidence hits: discrete choice, marginal cost, welfare, counterfactual, instrument, gmm
- Demand side: 全文表明作者在做结构化产品需求分析，但 OCR 证据不足以把需求形式精确钉死到某个 logit 变体。
- Utility construction: 效用写法围绕价格、产品属性、不可观测质量以及个体异质性展开，等价于把平均效用和个体偏离拆开理解。
- Heterogeneity: 异质性是关键层：作者依赖收入、偏好差异、使用场景或消费者类型来刻画不同群体的替代弹性。
- Supply side: 供给侧较轻或被外生化，论文重心更偏需求恢复、替代矩阵和消费者/社会福利。
- Identification / estimation: 识别依赖工具变量、GMM 或其他矩条件来处理价格与产品属性的内生性。
- Counterfactual / welfare: 模型的终点不是参数本身，而是福利、反事实和政策比较。

## Writing Memory
- 这篇文章的正文结构大体按下面的顺序推进：
- 1. Introduction
- 2. Background on solar PV policies in Connecticut
- 3. Data
- 6. Results
- 7. Policy analysis
- 8. Conclusions
- Hurdles and steps: Estimating demand for solar photovoltaics
- Kenneth Gillingham
- Tsvetan Tsvetanov Department of Economics, University of Kansas
- Quantitative Economics 10 (2019), 275-310
- Gillingham and Tsvetanov
- Quantitative Economics 10 (2019)

## Reusable Writing Moves
- 在模型章节之前先把市场、制度、样本和关键摩擦讲透，让后面的结构设定像是被场景推出而不是凭空假设。
- 把模型的价值落在反事实与福利，而不是只汇报需求系数和价格弹性。

## OCR Anchors
- introduction: `1. Introduction` (p.0) - 1. Introduction The market for rooftop solar photovoltaic (PV) systems has been growing rapidly around the world in the past decade.
- background: `2. Background on solar PV policies in Connecticut` (p.3) - 2. Background on solar PV policies in Connecticut Despite receiving fewer hours of sun than more southerly regions,2 CT has a robust and growing market for solar PV systems, due to high electricity prices, many owneroccupied homes, and considerable state support for PV systems.
- data: `3. Data` (p.5) - 3. Data Our primary dataset contains nearly all residential solar PV system installations in CT from the period 2008-2014.
- results: `6. Results` (p.20) - 6. Results
- counterfactual: `7. Policy analysis` (p.24) - 7. Policy analysis In this section, we highlight what our results imply for policies in the solar PV market in CT through a set of simple counterfactual simulations.
- conclusion: `8. Conclusions` (p.28) - 8. Conclusions This study estimates the demand for solar PV systems using a new empirical approach: a Poisson hurdle model with fixed effects and instrumental variables.

## Memory Notes
- 后续回忆这篇论文时，优先调用它的故事梯子、模型嵌入位置、识别策略和反事实落点，而不是只记结论。
- 如果需要公式级别细节，可以直接回到对应 `llm.json` 的 equation chunks 与 model / estimation section。
