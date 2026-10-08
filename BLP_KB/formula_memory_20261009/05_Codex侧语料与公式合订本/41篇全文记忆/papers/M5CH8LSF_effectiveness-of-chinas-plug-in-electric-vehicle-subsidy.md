---
name: paper_m5ch8lsf_effectiveness-of-chinas-plug-in-electric-vehicle-subsidy
description: Fulltext memory for Effectiveness of China's plug-in electric vehicle subsidy; stores story logic, BLP model construction, estimation, counterfactual use, and writing structure.
type: reference
---

# Effectiveness of China's plug-in electric vehicle subsidy

## Citation
- Key: `M5CH8LSF`
- DOI: `10.1016/j.eneco.2020.104773`
- Journal: Energy Economics
- Year: 2020
- OCR source PDF: `D:\codex\tmp\blp_full_read_20260417\staged_pdfs\M5CH8LSF.pdf`
- OCR JSON: `D:/codex/tmp/blp_full_read_20260417/parsed_all/M5CH8LSF/M5CH8LSF.llm.json`
- Digest JSON: `D:/codex/tmp/blp_full_read_20260417/digests/M5CH8LSF.json`

## Read Status
- 本记忆基于全文 OCR 解析结果整理，不是只看题目、摘要或 Zotero 元数据。
- OCR 流程使用 MinerU 优先、DirectML 加速、输出 `llm.md` / `llm.json` / `chunks.jsonl`。

## Story Question
- In this paper, we explore the impact and cost-effectiveness of the Chinese PEV subsidy program.

## Story Logic
- 故事起点：In this paper, we explore the impact and cost-effectiveness of the Chinese PEV subsidy program.
- 制度/市场切口：Subsidies for promoting plug-in electric vehicle (PEV) adoption are a key component of China's overall plan for reducing local air pollution and greenhouse gas emissions from the light-duty vehicle sector.
- 模型推进：核心推进动作是把差异化产品需求或供给均衡模型嵌入实证问题，而不是停留在 reduced-form。
- 结论落点：Subsidies for promoting plug-in electric vehicle (PEV) adoption are a key component of China's overall plan for reducing local air pollution and greenhouse gas emissions from the light-duty vehicle sector.

## BLP Model Memory
- BLP positioning: BLP-style differentiated-product demand
- Evidence hits: random coefficients, mixed logit, discrete choice, welfare, counterfactual, instrument
- Demand side: 需求侧是结构化离散选择/差异化产品需求系统，重点是恢复替代关系与价格弹性。
- Utility construction: 效用写法围绕价格、产品属性、不可观测质量以及个体异质性展开，等价于把平均效用和个体偏离拆开理解。
- Heterogeneity: 异质性是关键层：作者依赖收入、偏好差异、使用场景或消费者类型来刻画不同群体的替代弹性。
- Supply side: 供给侧较轻或被外生化，论文重心更偏需求恢复、替代矩阵和消费者/社会福利。
- Identification / estimation: 识别依赖工具变量、GMM 或其他矩条件来处理价格与产品属性的内生性。
- Counterfactual / welfare: 模型的终点不是参数本身，而是福利、反事实和政策比较。

## Writing Memory
- 这篇文章的正文结构大体按下面的顺序推进：
- INTRODUCTION
- Journal Pre-proof
- DATA
- RESULTS & DISCUSSION
- Counterfactual Simulation Analysis
- CONCLUSION
- PII: S0140-9883(20)30113-4
- Reference: ENEECO 104773
- To appear in: Energy Economics
- Received date: 11 November 2019
- Revised date: 12 March 2020
- Accepted date: 23 April 2020

## Reusable Writing Moves
- 在模型章节之前先把市场、制度、样本和关键摩擦讲透，让后面的结构设定像是被场景推出而不是凭空假设。
- 把模型的价值落在反事实与福利，而不是只汇报需求系数和价格弹性。

## OCR Anchors
- abstract: `ABSTRACT` (p.1) - ABSTRACT Subsidies for promoting plug-in electric vehicle (PEV) adoption are a key component of China‟s overall plan for reducing local air pollution and greenhouse gas emissions from the light-duty vehicle sector. In this paper, we explore the impact and cost-effectiveness of the Chinese PEV subsidy program.
- introduction: `INTRODUCTION` (p.2) - INTRODUCTION China, the world‟s largest emitter of carbon dioxide in terms of total emissions, has announced ambitious climate goals in recent years. These include reducing carbon intensity of GDP by 40-45 percent of 2005 levels by 2020 and by 60-65 percent of 2005 levels by 2030 (Xu et al., 2017).
- background: `Journal Pre-proof` (p.2) - Journal Pre-proof 2 China would have declined by 21% had the subsidy been halved without any countervailing measures. Indeed, recent media reports suggest a drop in PEV sales over the past four months since the subsidy cuts were implemented (Moss, 2019; Shane, 2019; Shepherd, 2019a, b).
- data: `DATA` (p.3) - DATA The primary data set, purchased from J.D. Power and Associates1, is a survey of Chinese consumers who purchased a new model year 2017 vehicle (specifically, who purchased a new vehicle between October 2016 and September 2017).
- results: `RESULTS & DISCUSSION` (p.6) - RESULTS & DISCUSSION
- counterfactual: `Counterfactual Simulation Analysis` (p.7) - Counterfactual Simulation Analysis Table 4 compares the predicted counterfactual fleet if PEVs were unavailable for purchase in China to the current fleet with existing subsidies in China. Without PEVs, fleet fuel economy would be 12.38 km/L, roughly 2% lower than the current 12.62 km/L, with more of the improvement coming from high income consumers, who are more likely to purchase PEVs.
- conclusion: `CONCLUSION` (p.10) - CONCLUSION Despite China‟s ambitious goal to have five million NEVs on the road by 2020, there is uncertainty over the future of the subsidy program. This paper seeks to shed light on the effectiveness of these subsidies with the intent of informing policy makers in the face of future program uncertainty.

## Memory Notes
- 后续回忆这篇论文时，优先调用它的故事梯子、模型嵌入位置、识别策略和反事实落点，而不是只记结论。
- 如果需要公式级别细节，可以直接回到对应 `llm.json` 的 equation chunks 与 model / estimation section。
