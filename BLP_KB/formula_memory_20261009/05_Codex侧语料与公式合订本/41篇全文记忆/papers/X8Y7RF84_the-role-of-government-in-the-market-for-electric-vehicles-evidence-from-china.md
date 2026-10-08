---
name: paper_x8y7rf84_the-role-of-government-in-the-market-for-electric-vehicles-evidence-from-china
description: Fulltext memory for The Role of Government in the Market for Electric Vehicles: Evidence from China; stores story logic, BLP model construction, estimation, counterfactual use, and writing structure.
type: reference
---

# The Role of Government in the Market for Electric Vehicles: Evidence from China

## Citation
- Key: `X8Y7RF84`
- DOI: `10.1002/pam.22362`
- Journal: Journal of Policy Analysis and Management
- Year: 2022
- OCR source PDF: `D:\codex\tmp\blp_full_read_20260417\staged_pdfs\X8Y7RF84.pdf`
- OCR JSON: `D:/codex/tmp/blp_full_read_20260417/parsed_all/X8Y7RF84/X8Y7RF84.llm.json`
- Digest JSON: `D:/codex/tmp/blp_full_read_20260417/digests/X8Y7RF84.json`

## Read Status
- 本记忆基于全文 OCR 解析结果整理，不是只看题目、摘要或 Zotero 元数据。
- OCR 流程使用 MinerU 优先、DirectML 加速、输出 `llm.md` / `llm.json` / `chunks.jsonl`。

## Story Question
- This paper is a product of the Office of the Chief Economist, Infrastructure Vice Presidency.

## Story Logic
- 故事起点：This paper is a product of the Office of the Chief Economist, Infrastructure Vice Presidency.
- 制度/市场切口：This study examines the effectiveness of various policy measures that underlie the rapid development of the EV market in China, by far the world's largest such market.
- 模型推进：The empirical framework addresses the potential endogeneity of key variables, such as local policies and charging infrastructure, by using a city‐border‐regression design and instrumental variable approach.
- 结论落点：This study examines the effectiveness of various policy measures that underlie the rapid development of the EV market in China, by far the world's largest such market.

## BLP Model Memory
- BLP positioning: BLP-adjacent structural policy model
- Evidence hits: discrete choice, welfare, counterfactual, instrument
- Demand side: 全文表明作者在做结构化产品需求分析，但 OCR 证据不足以把需求形式精确钉死到某个 logit 变体。
- Utility construction: 模型核心仍然是“价格 + 产品属性 + 未观测质量”决定选择概率，再由市场份额把需求参数识别出来。
- Heterogeneity: 异质性是关键层：作者依赖收入、偏好差异、使用场景或消费者类型来刻画不同群体的替代弹性。
- Supply side: 供给侧较轻或被外生化，论文重心更偏需求恢复、替代矩阵和消费者/社会福利。
- Identification / estimation: 识别依赖工具变量、GMM 或其他矩条件来处理价格与产品属性的内生性。
- Counterfactual / welfare: 模型的终点不是参数本身，而是福利、反事实和政策比较。

## Writing Memory
- 这篇文章的正文结构大体按下面的顺序推进：
- 1 Introduction
- 2 Industry Background and Data Description
- 2.3 Data Description
- 3.2 Identification Strategy
- 5 Policy Analysis
- 6 Conclusion
- The Role of Government in the Market for Electric Vehicles
- Shanjun Li
- Xianglei Zhu
- Yiding Ma
- Fan Zhang
- Hui Zhou

## Reusable Writing Moves
- 在模型章节之前先把市场、制度、样本和关键摩擦讲透，让后面的结构设定像是被场景推出而不是凭空假设。
- 把模型的价值落在反事实与福利，而不是只汇报需求系数和价格弹性。

## OCR Anchors
- abstract: `Abstract` (p.1) - Abstract To promote the development and diffusion of electric vehicles, central and local governments in many countries have adopted various incentive programs. This study examines the policy and market drivers behind the rapid development of the electric vehicle market in China, by far the largest one in the world.
- introduction: `1 Introduction` (p.3) - 1 Introduction The study presents a comprehensive empirical analysis on various driving forces with a focus on the role of government behind the rapid growth of the electric vehicle (EV) market in China based on the most detailed data ever complied on this important market. An electrified transportation system together with a clean electricity grid holds the promise to reduce fossil fuel usage, local pollution, and greenhouse gas emissions (GHGs).
- background: `2 Industry Background and Data Description` (p.7) - 2 Industry Background and Data Description
- data: `2.3 Data Description` (p.14) - 2.3 Data Description Vehicle data We obtain EVs sales at the city-quarter-trim level from 2015 to 2018. Our sample of analysis has 150 cities.
- estimation: `3.2 Identification Strategy` (p.19) - 3.2 Identification Strategy We address the first two sources of endogeneity, unobserved product attributes and simultaneity using the instrumental variable method. For the third source of endogeneity, we use a cityborder regression design to address selection of local policies.
- counterfactual: `5 Policy Analysis` (p.27) - 5 Policy Analysis In this section, we conduct simulations to examine the role of the underlying driving factors behind the dramatic growth of China’s EV market. Based on the model estimates, we simulate the counterfactual EV sales by removing each policy or non-policy factor one at a time.
- conclusion: `6 Conclusion` (p.30) - 6 Conclusion This study provides to our knowledge the first empirical analysis on the underlying driving factors behind the rapid growth of the world’s largest EV market, China. The analysis is based on the most comprehensive data on China’s EV market including EV sales, charging infrastructure, and various central and local policies during 2015-2018.

## Memory Notes
- 后续回忆这篇论文时，优先调用它的故事梯子、模型嵌入位置、识别策略和反事实落点，而不是只记结论。
- 如果需要公式级别细节，可以直接回到对应 `llm.json` 的 equation chunks 与 model / estimation section。
