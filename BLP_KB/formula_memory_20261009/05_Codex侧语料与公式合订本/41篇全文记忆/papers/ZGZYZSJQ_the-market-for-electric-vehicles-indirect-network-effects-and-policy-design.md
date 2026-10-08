---
name: paper_zgzyzsjq_the-market-for-electric-vehicles-indirect-network-effects-and-policy-design
description: Fulltext memory for The Market for Electric Vehicles: Indirect Network Effects and Policy Design; stores story logic, BLP model construction, estimation, counterfactual use, and writing structure.
type: reference
---

# The Market for Electric Vehicles: Indirect Network Effects and Policy Design

## Citation
- Key: `ZGZYZSJQ`
- DOI: `10.1086/689702`
- Journal: Journal of the Association of Environmental and Resource Economists
- Year: 2017
- OCR source PDF: `D:\codex\tmp\blp_full_read_20260417\staged_pdfs\ZGZYZSJQ.pdf`
- OCR JSON: `D:/codex/tmp/blp_full_read_20260417/parsed_all/ZGZYZSJQ/ZGZYZSJQ.llm.json`
- Digest JSON: `D:/codex/tmp/blp_full_read_20260417/digests/ZGZYZSJQ.json`

## Read Status
- 本记忆基于全文 OCR 解析结果整理，不是只看题目、摘要或 Zotero 元数据。
- OCR 流程使用 MinerU 优先、DirectML 加速、输出 `llm.md` / `llm.json` / `chunks.jsonl`。

## Story Question
- The market for plug-in electric vehicles (EVs) exhibits indirect network effects due to the interdependence between EV adoption and charging station investment.

## Story Logic
- 故事起点：The market for plug-in electric vehicles (EVs) exhibits indirect network effects due to the interdependence between EV adoption and charging station investment.
- 制度/市场切口：The federal income tax credit of up to $7,500 for EV buyers contributed to about 40% of EV sales during 2011-13, with feedback loops explaining 40% of that increase.
- 模型推进：核心推进动作是把差异化产品需求或供给均衡模型嵌入实证问题，而不是停留在 reduced-form。
- 结论落点：The federal income tax credit of up to $7,500 for EV buyers contributed to about 40% of EV sales during 2011-13, with feedback loops explaining 40% of that increase.

## BLP Model Memory
- BLP positioning: BLP-adjacent structural policy model
- Evidence hits: discrete choice, marginal cost, markup, counterfactual, instrument, gmm
- Demand side: 需求侧是结构化离散选择/差异化产品需求系统，重点是恢复替代关系与价格弹性。
- Utility construction: 效用写法围绕价格、产品属性、不可观测质量以及个体异质性展开，等价于把平均效用和个体偏离拆开理解。
- Heterogeneity: 异质性是关键层：作者依赖收入、偏好差异、使用场景或消费者类型来刻画不同群体的替代弹性。
- Supply side: 供给侧并非完全缺席，作者至少把进入、定价或市场结构响应嵌进均衡框架。
- Identification / estimation: 识别依赖工具变量、GMM 或其他矩条件来处理价格与产品属性的内生性。
- Counterfactual / welfare: 模型的终点不是参数本身，而是福利、反事实和政策比较。

## Writing Memory
- 这篇文章的正文结构大体按下面的顺序推进：
- 1.1. Industry Background
- 1.3. Data
- 2.1. Model Setup and Properties
- 4. ESTIMATION RESULTS
- 2.2. Implications on Policy Choices
- 6. CONCLUSION
- The Market for Electric Vehicles: Indirect Network Effects and Policy Design
- Shanjun Li, Lang Tong, Jianwei Xing, Yiyi Zhou
- The Market for Electric Vehicles
- 1. INDUSTRY AND POLICY BACKGROUND AND DATA
- 1.2. Government Policy
- 2. A MODEL OF INDIRECT NETWORK EFFECTS

## Reusable Writing Moves
- 在模型章节之前先把市场、制度、样本和关键摩擦讲透，让后面的结构设定像是被场景推出而不是凭空假设。
- 把模型的价值落在反事实与福利，而不是只汇报需求系数和价格弹性。

## OCR Anchors
- background: `1.1. Industry Background` (p.4) - 1.1. Industry Background Tesla Motors played a significant role in the comeback of electric vehicles by introducing Tesla Roadster, an all-electric sports car, in 2006 and beginning general production in March 2008.
- data: `1.3. Data` (p.9) - 1.3. Data We construct a panel data set consisting of quarterly EV sales by vehicle model and the number of charging stations available at 353 MSAs from 2011 to 2013.
- model: `2.1. Model Setup and Properties` (p.12) - 2.1. Model Setup and Properties We assume that EV sales q _ { t } ( N _ { t } , p _ { t } , x _ { t } ) depends on the number of public charging stations in the market (Nt), the price of the EV \left( { { p } _ { t } } \right) , and other product characteristics combined \left( x _ { t } \right) that affect consumers’ choice, such as the fuel cost.14 The installed base of EVs is the cumulative sum of EV sales minus scrappage by the time t , denoted by Q _ { t } = \Sigma _ { b = 1 } ^ { t } q _ { b } { * } s _ { t , b } , where s _ { t ^ { \prime } b } is the survival rate at time t for EVs sold in time h.
- estimation: `4. ESTIMATION RESULTS` (p.23) - 4. ESTIMATION RESULTS We first present parameter estimates for equations (4) and (5).
- counterfactual: `2.2. Implications on Policy Choices` (p.13) - 2.2. Implications on Policy Choices Now we conduct simulations to understand how feedback loops magnify policy shocks and their implications on policy choices.
- conclusion: `6. CONCLUSION` (p.39) - 6. CONCLUSION This study first demonstrates through a stylized model that positive indirect network effects in both EV demand and charging station deployment give rise to feedback loops that amplify shocks to the system and have important policy implications.

## Memory Notes
- 后续回忆这篇论文时，优先调用它的故事梯子、模型嵌入位置、识别策略和反事实落点，而不是只记结论。
- 如果需要公式级别细节，可以直接回到对应 `llm.json` 的 equation chunks 与 model / estimation section。
