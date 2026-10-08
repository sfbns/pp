---
name: paper_3xdzxltp_winners-and-losers-the-distributional-effects-of-the-french-feebate-on-the-automobile-mark
description: Fulltext memory for Winners and Losers: the Distributional Effects of the French Feebate on the Automobile Market; stores story logic, BLP model construction, estimation, counterfactual use, and writing structure.
type: reference
---

# Winners and Losers: the Distributional Effects of the French Feebate on the Automobile Market

## Citation
- Key: `3XDZXLTP`
- DOI: `10.1093/ej/ueab084`
- Journal: The Economic Journal
- Year: 2022
- OCR source PDF: `D:\codex\tmp\blp_full_read_20260417\staged_pdfs\3XDZXLTP.pdf`
- OCR JSON: `D:/codex/tmp/blp_full_read_20260417/parsed_all/3XDZXLTP/3XDZXLTP.llm.json`
- Digest JSON: `D:/codex/tmp/blp_full_read_20260417/digests/3XDZXLTP.json`

## Read Status
- 本记忆基于全文 OCR 解析结果整理，不是只看题目、摘要或 Zotero 元数据。
- OCR 流程使用 MinerU 优先、DirectML 加速、输出 `llm.md` / `llm.json` / `chunks.jsonl`。

## Story Question
- Abstract I quantify the welfare and environmental gains and losses from a policy establishing an environmental tax/subsidy for new cars in France in 2008.

## Story Logic
- 故事起点：1 This paper evaluates the 2008 French feebate policy and analyses its distributional effects.
- 制度/市场切口：Abstract I quantify the welfare and environmental gains and losses from a policy establishing an environmental tax/subsidy for new cars in France in 2008.
- 模型推进：I use a structural model for the demand and supply of new automobiles to simulate the market equilibrium (car prices and market shares of the different car models) without the feebate regulation.
- 结论落点：Abstract I quantify the welfare and environmental gains and losses from a policy establishing an environmental tax/subsidy for new cars in France in 2008.

## BLP Model Memory
- BLP positioning: canonical BLP demand-supply
- Evidence hits: random coefficients, discrete choice, marginal cost, welfare, counterfactual, instrument
- Demand side: 需求侧基本可以判定为随机系数离散选择，是最接近经典 BLP 的主干写法。
- Utility construction: 效用写法围绕价格、产品属性、不可观测质量以及个体异质性展开，等价于把平均效用和个体偏离拆开理解。
- Heterogeneity: 异质性是关键层：作者依赖收入、偏好差异、使用场景或消费者类型来刻画不同群体的替代弹性。
- Supply side: 供给侧是显式的：通常包含多产品定价、边际成本恢复、markup 变化和均衡反事实。
- Identification / estimation: 识别依赖工具变量、GMM 或其他矩条件来处理价格与产品属性的内生性。
- Counterfactual / welfare: 模型的终点不是参数本身，而是福利、反事实和政策比较。

## Writing Memory
- 这篇文章的正文结构大体按下面的顺序推进：
- 1 Introduction
- 2 Institutional details and data
- 2.2 Data
- 3 Model
- 3.4 Estimation
- 3.5 Discussion
- October 2021
- “Winners and Losers: The Distributional Effects of the French Feebate on the Automobile Market”
- Isis Durrmeyer
- Toulouse School of Economics
- Winners and Losers: The Distributional Effects of the French Feebate on the Automobile Market
- Short title: Winners & losers from the French feebate

## Reusable Writing Moves
- 在模型章节之前先把市场、制度、样本和关键摩擦讲透，让后面的结构设定像是被场景推出而不是凭空假设。
- 把模型的价值落在反事实与福利，而不是只汇报需求系数和价格弹性。

## OCR Anchors
- abstract: `Abstract` (p.1) - Abstract I quantify the welfare and environmental gains and losses from a policy establishing an environmental tax/subsidy for new cars in France in 2008. I estimate a structural model of demand and supply that features heterogeneity in consumer preferences to go beyond the average policy effects and analyse distributional aspects.
- introduction: `1 Introduction` (p.1) - 1 Introduction Policy evaluation tends to focus on the average or overall impact, often neglecting the importance of distributional effects. For instance, the long-lasting “yellow vests” protests in France, which began in October 2018 and destabilised the government, illustrate the crucial role of distributional effects for public policy acceptance.
- background: `2 Institutional details and data` (p.6) - 2 Institutional details and data
- data: `2.2 Data` (p.7) - 2.2 Data In this analysis, I combine two main datasets. The first one was obtained from the French Syndicate of Car Manufacturers (“Comit´e des Constructeurs Fran¸cais d’Automobiles”, CCFA) and contains information about new car characteristics and sales from 2003 to 2008 at the municipality level.
- model: `3 Model` (p.11) - 3 Model In this section, I present a model of demand and supply for new automobiles both under and in the absence of the feebate regulation. The model allows for heterogeneous preferences related to demographic characteristics.
- estimation: `3.4 Estimation` (p.15) - 3.4 Estimation I estimate the parameters of utility using the generalised method of moments. I use the standard aggregate demand and supply moments, as in Berry et al.
- conclusion: `3.5 Discussion` (p.17) - 3.5 Discussion The model is static and abstracts from the dynamic aspects related to the car purchase decision. Because a car is a durable good that is used for several years and can be sold on a second-hand car market, consumer anticipation of future car prices and characteristics and second-hand car market characteristics play a role in the purchase decisions.

## Memory Notes
- 后续回忆这篇论文时，优先调用它的故事梯子、模型嵌入位置、识别策略和反事实落点，而不是只记结论。
- 如果需要公式级别细节，可以直接回到对应 `llm.json` 的 equation chunks 与 model / estimation section。
