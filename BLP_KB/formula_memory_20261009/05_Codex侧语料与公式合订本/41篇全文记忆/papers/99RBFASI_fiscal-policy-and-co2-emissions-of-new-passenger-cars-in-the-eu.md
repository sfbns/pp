---
name: paper_99rbfasi_fiscal-policy-and-co2-emissions-of-new-passenger-cars-in-the-eu
description: Fulltext memory for Fiscal Policy and CO2 Emissions of New Passenger Cars in the EU; stores story logic, BLP model construction, estimation, counterfactual use, and writing structure.
type: reference
---

# Fiscal Policy and CO2 Emissions of New Passenger Cars in the EU

## Citation
- Key: `99RBFASI`
- DOI: `10.1007/s10640-016-0067-6`
- Journal: Environmental and Resource Economics
- Year: 2018
- OCR source PDF: `D:\codex\tmp\blp_full_read_20260417\staged_pdfs\99RBFASI.pdf`
- OCR JSON: `D:/codex/tmp/blp_full_read_20260417/parsed_all/99RBFASI/99RBFASI.llm.json`
- Digest JSON: `D:/codex/tmp/blp_full_read_20260417/digests/99RBFASI.json`

## Read Status
- 本记忆基于全文 OCR 解析结果整理，不是只看题目、摘要或 Zotero 元数据。
- OCR 流程使用 MinerU 优先、DirectML 加速、输出 `llm.md` / `llm.json` / `chunks.jsonl`。

## Story Question
- To what extent have national fiscal policies contributed to the decarbonisation of newly sold passenger cars?

## Story Logic
- 故事起点：To what extent have national fiscal policies contributed to the decarbonisation of newly sold passenger cars?
- 制度/市场切口：First, we use a large database of vehicle-specific taxes in 15 EU countries over 2001-2010 to construct a measure for the vehicle registration and annual road tax levels, and separately, for the $$\hbox {CO}_{2}$$ sensitivity of these taxes.
- 模型推进：核心推进动作是把差异化产品需求或供给均衡模型嵌入实证问题，而不是停留在 reduced-form。
- 结论落点：First, we use a large database of vehicle-specific taxes in 15 EU countries over 2001-2010 to construct a measure for the vehicle registration and annual road tax levels, and separately, for the $$\hbox {CO}_{2}$$ sensitivity of these taxes.

## BLP Model Memory
- BLP positioning: BLP-adjacent structural policy model
- Evidence hits: bertrand, welfare, instrument
- Demand side: 全文表明作者在做结构化产品需求分析，但 OCR 证据不足以把需求形式精确钉死到某个 logit 变体。
- Utility construction: 效用写法围绕价格、产品属性、不可观测质量以及个体异质性展开，等价于把平均效用和个体偏离拆开理解。
- Heterogeneity: 异质性是关键层：作者依赖收入、偏好差异、使用场景或消费者类型来刻画不同群体的替代弹性。
- Supply side: 供给侧是显式的：通常包含多产品定价、边际成本恢复、markup 变化和均衡反事实。
- Identification / estimation: 识别依赖工具变量、GMM 或其他矩条件来处理价格与产品属性的内生性。
- Counterfactual / welfare: 论文明确把模型用于税收、补贴、禁令、标签或进入政策的反事实分析。

## Writing Memory
- 这篇文章的正文结构大体按下面的顺序推进：
- 1 Introduction
- 1 See European Commission (2016).
- 4 Data
- 3 Model
- 6 Results
- 7 Discussion
- Fiscal Policy and \mathbf { C O } _ { 2 } Emissions of New Passenger Cars in the EU
- Reyer Gerlagh1 Inge van den Bijgaart1,4 Hans Nijland2 Thomas Michielsen3
- Accepted: 23 September 2016
- CrossMark
- 1 Tilburg University, Tilburg, Netherlands
- 2 PBL Netherlands Environmental Assessment Agency, The Hague, Netherlands

## Reusable Writing Moves
- 在模型章节之前先把市场、制度、样本和关键摩擦讲透，让后面的结构设定像是被场景推出而不是凭空假设。
- 正文常见顺序是“模型设定 -> 识别/估计 -> 结果 -> 政策反事实”，避免一上来就堆公式。

## OCR Anchors
- introduction: `1 Introduction` (p.1) - 1 Introduction Transport accounts for about 23 % of energy-related \mathrm { C O } _ { 2 } emissions (Sims and Schaeffer 2014), and 15 % of global greenhouse gas emissions (Blanco et al. 2014).
- background: `1 See European Commission (2016).` (p.1) - 1 See European Commission (2016). 2 See Figs.
- data: `4 Data` (p.6) - 4 Data Here we describe the data used for the empirical analysis. The dependent variable of interest is the average \mathrm { C O } _ { 2 } intensity of newly purchased vehicles, which depends on substitution patterns between more and less fuel efficient cars, but also on common fuel efficiency improvements over all cars, which in our econometric strategy is absorbed by time fixed effects.
- model: `3 Model` (p.4) - 3 Model We illustrate the effect of vehicle purchase taxes on the average emission intensity with a simple model. We consider two car types.
- results: `6 Results` (p.12) - 6 Results
- conclusion: `7 Discussion` (p.19) - 7 Discussion We find empirical evidence that fiscal vehicle policies significantly affect emission intensities of new bought cars. A greater \mathrm { C O } _ { 2 } -sensitivity of registration taxes lead to the purchase of more fuel-efficient cars.

## Memory Notes
- 后续回忆这篇论文时，优先调用它的故事梯子、模型嵌入位置、识别策略和反事实落点，而不是只记结论。
- 如果需要公式级别细节，可以直接回到对应 `llm.json` 的 equation chunks 与 model / estimation section。
