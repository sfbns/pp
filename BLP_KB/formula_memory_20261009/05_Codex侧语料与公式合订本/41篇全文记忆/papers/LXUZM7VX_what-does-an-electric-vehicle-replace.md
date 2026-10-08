---
name: paper_lxuzm7vx_what-does-an-electric-vehicle-replace
description: Fulltext memory for What does an electric vehicle replace?; stores story logic, BLP model construction, estimation, counterfactual use, and writing structure.
type: reference
---

# What does an electric vehicle replace?

## Citation
- Key: `LXUZM7VX`
- DOI: `10.1016/j.jeem.2021.102432`
- Journal: Journal of Environmental Economics and Management
- Year: 2021
- OCR source PDF: `D:\codex\tmp\blp_full_read_20260417\staged_pdfs\LXUZM7VX.pdf`
- OCR JSON: `D:/codex/tmp/blp_full_read_20260417/parsed_all/LXUZM7VX/LXUZM7VX.llm.json`
- Digest JSON: `D:/codex/tmp/blp_full_read_20260417/digests/LXUZM7VX.json`

## Read Status
- 本记忆基于全文 OCR 解析结果整理，不是只看题目、摘要或 Zotero 元数据。
- OCR 流程使用 MinerU 优先、DirectML 加速、输出 `llm.md` / `llm.json` / `chunks.jsonl`。

## Story Question
- The emissions reductions from the adoption of a new transportation technology depend on the emissions from the new technology relative to those from the displaced technology.

## Story Logic
- 故事起点：In this study, we fill this gap by focusing on the second factor and illustrate the critical role this channel plays in determining the environmental benefits of EVs.1 More specifically, we examine what EV buyers would have purchased had EVs been unavailable.
- 制度/市场切口：We do so by estimating a random coefficients discrete choice model of new vehicle demand and simulating counterfactual sales with EVs no longer subsidized or removed from the new vehicle market.
- 模型推进：核心推进动作是把差异化产品需求或供给均衡模型嵌入实证问题，而不是停留在 reduced-form。
- 结论落点：We do so by estimating a random coefficients discrete choice model of new vehicle demand and simulating counterfactual sales with EVs no longer subsidized or removed from the new vehicle market.

## BLP Model Memory
- BLP positioning: canonical BLP demand-supply
- Evidence hits: random coefficients, discrete choice, marginal cost, welfare, counterfactual, instrument
- Demand side: 需求侧基本可以判定为随机系数离散选择，是最接近经典 BLP 的主干写法。
- Utility construction: 效用写法围绕价格、产品属性、不可观测质量以及个体异质性展开，等价于把平均效用和个体偏离拆开理解。
- Heterogeneity: 异质性是关键层：作者依赖收入、偏好差异、使用场景或消费者类型来刻画不同群体的替代弹性。
- Supply side: 供给侧较轻或被外生化，论文重心更偏需求恢复、替代矩阵和消费者/社会福利。
- Identification / estimation: 识别依赖工具变量、GMM 或其他矩条件来处理价格与产品属性的内生性。
- Counterfactual / welfare: 模型的终点不是参数本身，而是福利、反事实和政策比较。

## Writing Memory
- 这篇文章的正文结构大体按下面的顺序推进：
- 1. Introduction
- Journal of Environmental Economics and Management 107 (2021) 102432
- 2. Data description
- 4.2. Identification
- 6. Counterfactual analysis
- 7. Discussion
- What does an electric vehicle replace?
- a r t i c l e i n f o
- a b s t r a c t
- Contents lists available at ScienceDirect
- ELSEVIER
- Journal of Environmental Economics and Management

## Reusable Writing Moves
- 在模型章节之前先把市场、制度、样本和关键摩擦讲透，让后面的结构设定像是被场景推出而不是凭空假设。
- 把模型的价值落在反事实与福利，而不是只汇报需求系数和价格弹性。

## OCR Anchors
- introduction: `1. Introduction` (p.0) - 1. Introduction The diffusion of plug-in hybrid and fully electric vehicles (EVs), coupled with cleaner electricity generation, offers a promising pathway to reduce air pollution from on-road vehicles and to strengthen energy security.
- background: `Journal of Environmental Economics and Management 107 (2021) 102432` (p.0) - Journal of Environmental Economics and Management 107 (2021) 102432
- data: `2. Data description` (p.2) - 2. Data description We use three data sets to estimate the model of vehicle demand.
- estimation: `4.2. Identification` (p.8) - 4.2. Identification Consumer utility is composed of three parts: mean utility, observed heterogeneity, and unobserved heterogeneity.
- counterfactual: `6. Counterfactual analysis` (p.13) - 6. Counterfactual analysis In this section, we conduct simulations to examine the counterfactual vehicle fleet where we remove all EV models from the choice sets and where the EV subsidy were removed.
- conclusion: `7. Discussion` (p.18) - 7. Discussion The results from our analysis come with several caveats.

## Memory Notes
- 后续回忆这篇论文时，优先调用它的故事梯子、模型嵌入位置、识别策略和反事实落点，而不是只记结论。
- 如果需要公式级别细节，可以直接回到对应 `llm.json` 的 equation chunks 与 model / estimation section。
