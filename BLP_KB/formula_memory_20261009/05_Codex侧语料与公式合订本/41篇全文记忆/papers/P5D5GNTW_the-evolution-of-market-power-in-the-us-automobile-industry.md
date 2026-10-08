---
name: paper_p5d5gntw_the-evolution-of-market-power-in-the-us-automobile-industry
description: Fulltext memory for The Evolution of Market Power in the U.S. Automobile Industry; stores story logic, BLP model construction, estimation, counterfactual use, and writing structure.
type: reference
---

# The Evolution of Market Power in the U.S. Automobile Industry

## Citation
- Key: `P5D5GNTW`
- DOI: `10.1093/qje/qjad047`
- Journal: The Quarterly Journal of Economics
- Year: 2024
- OCR source PDF: `D:\codex\tmp\blp_full_read_20260417\staged_pdfs\P5D5GNTW.pdf`
- OCR JSON: `D:/codex/tmp/blp_full_read_20260417/parsed_all/P5D5GNTW/P5D5GNTW.llm.json`
- Digest JSON: `D:/codex/tmp/blp_full_read_20260417/digests/P5D5GNTW.json`

## Read Status
- 本记忆基于全文 OCR 解析结果整理，不是只看题目、摘要或 Zotero 元数据。
- OCR 流程使用 MinerU 优先、DirectML 加速、输出 `llm.md` / `llm.json` / `chunks.jsonl`。

## Story Question
- We estimate a demand model using product-level data on market shares, prices, and attributes, and consumer-level data on demographics, purchases, and stated second choices.

## Story Logic
- 故事起点：We estimate a demand model using product-level data on market shares, prices, and attributes, and consumer-level data on demographics, purchases, and stated second choices.
- 制度/市场切口：This work complements a recent academic and policy literature analyzing long-term trends in market power and sales concentration from a macroeconomic perspective (De Loecker et al., 2020; Autor et al., 2020) with an industry-specific approach.
- 模型推进：We estimate a demand model using product-level data on market shares, prices, and attributes, and consumer-level data on demographics, purchases, and stated second choices.
- 结论落点：Abstract We construct measures of industry performance and welfare in the U.S.

## BLP Model Memory
- BLP positioning: canonical BLP demand-supply
- Evidence hits: random coefficients, discrete choice, bertrand, marginal cost, markup, welfare, counterfactual, instrument, gmm
- Demand side: 需求侧是结构化离散选择/差异化产品需求系统，重点是恢复替代关系与价格弹性。
- Utility construction: 模型核心仍然是“价格 + 产品属性 + 未观测质量”决定选择概率，再由市场份额把需求参数识别出来。
- Heterogeneity: 异质性是关键层：作者依赖收入、偏好差异、使用场景或消费者类型来刻画不同群体的替代弹性。
- Supply side: 供给侧是显式的：通常包含多产品定价、边际成本恢复、markup 变化和均衡反事实。
- Identification / estimation: 识别依赖工具变量、GMM 或其他矩条件来处理价格与产品属性的内生性。
- Counterfactual / welfare: 模型的终点不是参数本身，而是福利、反事实和政策比较。

## Writing Memory
- 这篇文章的正文结构大体按下面的顺序推进：
- 1 Introduction
- 2 Data
- 4 Model
- 5 Estimation and Results
- 7 Conclusion
- The Evolution of Market Power in the US Automobile Industry∗ *
- March 9, 2023
- Abstract
- 2.1 Automobile Market Data
- 2.2 Price Instrument
- 2.3 Consumer Choices and Demographics
- 2.4 Second Choices

## Reusable Writing Moves
- 在模型章节之前先把市场、制度、样本和关键摩擦讲透，让后面的结构设定像是被场景推出而不是凭空假设。
- 把模型的价值落在反事实与福利，而不是只汇报需求系数和价格弹性。

## OCR Anchors
- abstract: `Abstract` (p.0) - Abstract We construct measures of industry performance and welfare in the U.S. automobile market from 1980 to 2018.
- introduction: `1 Introduction` (p.0) - 1 Introduction From 1980 to 2018, the U.S. automobile industry experienced numerous technological and regulatory changes and its market structure changed dramatically.
- data: `2 Data` (p.3) - 2 Data We compiled a data set covering 1980 through 2018 consisting of automobile characteristics and market shares, individual consumer choices and demographic information, and consumer survey responses regarding alternate “second choice” products. This section describes the data sources and presents basic descriptive information.
- model: `4 Model` (p.8) - 4 Model Our framework is a differentiated product demand and oligopoly pricing model following Berry et al. (1995), which is standard in the industrial organization literature.
- estimation: `5 Estimation and Results` (p.11) - 5 Estimation and Results We estimate the model using GMM, closely following the procedures outlined by Petrin (2002) and Berry et al. (2004).
- conclusion: `7 Conclusion` (p.26) - 7 Conclusion Antitrust policy has come under scrutiny in the U.S. in recent years.

## Memory Notes
- 后续回忆这篇论文时，优先调用它的故事梯子、模型嵌入位置、识别策略和反事实落点，而不是只记结论。
- 如果需要公式级别细节，可以直接回到对应 `llm.json` 的 equation chunks 与 model / estimation section。
