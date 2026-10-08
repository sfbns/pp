---
name: paper_9x84a7qk_local-protectionism-market-structure-and-social-welfare-chinas-automobile-market
description: Fulltext memory for Local Protectionism, Market Structure, and Social Welfare: China’s Automobile Market; stores story logic, BLP model construction, estimation, counterfactual use, and writing structure.
type: reference
---

# Local Protectionism, Market Structure, and Social Welfare: China’s Automobile Market

## Citation
- Key: `9X84A7QK`
- DOI: `10.1257/pol.20180513`
- Journal: American Economic Journal: Economic Policy
- Year: 2021
- OCR source PDF: `D:\codex\tmp\blp_full_read_20260417\staged_pdfs\9X84A7QK.pdf`
- OCR JSON: `D:/codex/tmp/blp_full_read_20260417/parsed_all/9X84A7QK/9X84A7QK.llm.json`
- Digest JSON: `D:/codex/tmp/blp_full_read_20260417/digests/9X84A7QK.json`

## Read Status
- 本记忆基于全文 OCR 解析结果整理，不是只看题目、摘要或 Zotero 元数据。
- OCR 流程使用 MinerU 优先、DirectML 加速、输出 `llm.md` / `llm.json` / `chunks.jsonl`。

## Story Question
- This study documents the presence of local protectionism and quantifies its impacts on market competition and social welfare in the context of China’s automobile market.

## Story Logic
- 故事起点：Our analysis focuses on interregional trade and the home bias we study is a province-of-origin effect (based on the location of vehicle assembly) within a country.
- 制度/市场切口：Through county border analysis, falsification tests, and a consumer survey, we uncover protectionist policies such as subsidies to local brands as the primary contributing factor to the observed home bias.
- 模型推进：We then set up and estimate a market equilibrium model to quantify the impact of local protection, controlling for other demand and supply factors.
- 结论落点：This study documents the presence of local protectionism and quantifies its impacts on market competition and social welfare in the context of China’s automobile market.

## BLP Model Memory
- BLP positioning: canonical BLP demand-supply
- Evidence hits: random coefficients, discrete choice, bertrand, marginal cost, markup, welfare, counterfactual, instrument, gmm
- Demand side: 需求侧是结构化离散选择/差异化产品需求系统，重点是恢复替代关系与价格弹性。
- Utility construction: 效用写法围绕价格、产品属性、不可观测质量以及个体异质性展开，等价于把平均效用和个体偏离拆开理解。
- Heterogeneity: 异质性是关键层：作者依赖收入、偏好差异、使用场景或消费者类型来刻画不同群体的替代弹性。
- Supply side: 供给侧是显式的：通常包含多产品定价、边际成本恢复、markup 变化和均衡反事实。
- Identification / estimation: 识别依赖工具变量、GMM 或其他矩条件来处理价格与产品属性的内生性。
- Counterfactual / welfare: 模型的终点不是参数本身，而是福利、反事实和政策比较。

## Writing Memory
- 这篇文章的正文结构大体按下面的顺序推进：
- 1 Introduction
- 2 Background and Data
- 2.3 Data
- 5.2 Supply
- 5.3 Identification and Estimation
- 7.2 Welfare Analysis
- 8 Conclusion
- LOCAL PROTECTIONISM, MARKET STRUCTURE, AND SOCIAL WELFARE: CHINA'S AUTOMOBILE MARKET
- Panle Jia Barwick Shengmao Cao Shanjun Li
- ABSTRACT
- Shengmao Cao
- Economics Department

## Reusable Writing Moves
- 在模型章节之前先把市场、制度、样本和关键摩擦讲透，让后面的结构设定像是被场景推出而不是凭空假设。
- 把模型的价值落在反事实与福利，而不是只汇报需求系数和价格弹性。

## OCR Anchors
- abstract: `ABSTRACT` (p.1) - ABSTRACT While China has made great strides in transforming its centrally-planned economy to a marketoriented economy, there still exist widespread interregional trade barriers, such as policies and practices that protect local firms against competition from non-local firms. This study documents the presence of local protectionism and quantifies its impacts on market competition and social welfare in the context of China’s automobile market.
- introduction: `1 Introduction` (p.2) - 1 Introduction Since the implementation of market reform and open-up policy in 1978, China has made great strides in transforming its centrally-planned economy to a market-oriented economy. By recognizing private ownership, unleashing entrepreneurial spirit, and promoting international trade, the reform has led to an unprecedented economic growth with an annual GDP growth rate of 10 percent for over 35 years.1 Despite tremendous progress made in integrating with the world economy, China’s domestic market still exhibits widespread interregional barriers to trade that limit the mobility of goods and services.
- background: `2 Background and Data` (p.6) - 2 Background and Data In this section, we first present anecdotal evidence of local protectionism and discuss the relevant institutional background. We then provide an overview of China’s automobile industry and describe the data.
- data: `2.3 Data` (p.10) - 2.3 Data Our analysis is based on four main data sets: (1) the universe of vehicle registration records from 2009 to 2011 that is compiled by the State Administration of Industry and Commerce, (2) trim level vehicle attributes from R. L.
- model: `5.2 Supply` (p.28) - 5.2 Supply We estimate the demand and supply equations separately. Our supply-side specification follows Berry et al.
- estimation: `5.3 Identification and Estimation` (p.30) - 5.3 Identification and Estimation Our discussion of identification focuses on two sets of key parameters: a) the price discounts \rho _ { 1 } , \rho _ { 2 } and \rho _ { 3 } that capture the extent of local protectionism, and b) the coefficients that measure consumer price sensitivity. We then briefly describe how all parameters are estimated.
- counterfactual: `7.2 Welfare Analysis` (p.40) - 7.2 Welfare Analysis We first evaluate the welfare consequences of local protectionism on consumer surplus. To do so, we make two important assumptions: a) revenue neutrality of government subsidies, and b) all subsidies are financed via a lump-sum tax.
- conclusion: `8 Conclusion` (p.46) - 8 Conclusion Based on the census of new passenger vehicle registrations from 2009 to 2011 in China, we provide strong evidence of local protectionism in China’s automobile market using a regression discontinuity design, a series of falsification tests, and a number of consumer surveys. Through a structural model of vehicle demand and supply, we then quantify the impacts of local protectionism on market outcomes and show that local protection significantly reduces consumer welfare.

## Memory Notes
- 后续回忆这篇论文时，优先调用它的故事梯子、模型嵌入位置、识别策略和反事实落点，而不是只记结论。
- 如果需要公式级别细节，可以直接回到对应 `llm.json` 的 equation chunks 与 model / estimation section。
