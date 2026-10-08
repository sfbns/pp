---
name: paper_unmc2i56_consumer-myopia-imperfect-competition-and-the-energy-efficiency-gap-evidence-from-the-uk-r
description: Fulltext memory for Consumer myopia, imperfect competition and the energy efficiency gap: Evidence from the UK refrigerator market; stores story logic, BLP model construction, estimation, counterfactual use, and writing structure.
type: reference
---

# Consumer myopia, imperfect competition and the energy efficiency gap: Evidence from the UK refrigerator market

## Citation
- Key: `UNMC2I56`
- DOI: `10.1016/j.euroecorev.2017.01.004`
- Journal: European Economic Review
- Year: 2017
- OCR source PDF: `D:\codex\tmp\blp_full_read_20260417\staged_pdfs\UNMC2I56.pdf`
- OCR JSON: `D:/codex/tmp/blp_full_read_20260417/parsed_all/UNMC2I56/UNMC2I56.llm.json`
- Digest JSON: `D:/codex/tmp/blp_full_read_20260417/digests/UNMC2I56.json`

## Read Status
- 本记忆基于全文 OCR 解析结果整理，不是只看题目、摘要或 Zotero 元数据。
- OCR 流程使用 MinerU 优先、DirectML 加速、输出 `llm.md` / `llm.json` / `chunks.jsonl`。

## Story Question
- The empirical literature on the energy efficiency gap concentrates on demand inefficiencies in the energy -using durables markets and finds evidence that consumers underestimate future energy costs when purchasing a new appliance.

## Story Logic
- 故事起点：The empirical literature on the energy efficiency gap concentrates on demand inefficiencies in the energy -using durables markets and finds evidence that consumers underestimate future energy costs when purchasing a new appliance.
- 制度/市场切口：Introduction In energy and environmental policy circles, it is commonly believed that an “energy efficiency gap” exists between the desirable level of energy consumption and observed consumption (e.g.
- 模型推进：As a result, the market equilibrium maintains an energy efficiency gap defined as a wedge between the cost-minimizing level of energy efficiency and the level actually reached.
- 结论落点：Introduction In energy and environmental policy circles, it is commonly believed that an “energy efficiency gap” exists between the desirable level of energy consumption and observed consumption (e.g.

## BLP Model Memory
- BLP positioning: canonical BLP demand-supply
- Evidence hits: mixed logit, nested logit, discrete choice, bertrand, marginal cost, markup, welfare, counterfactual, instrument, gmm
- Demand side: 需求侧更像嵌套 logit / 分层离散选择，保留了产品空间替代结构，但异质性比经典 BLP 更轻。
- Utility construction: 模型核心仍然是“价格 + 产品属性 + 未观测质量”决定选择概率，再由市场份额把需求参数识别出来。
- Heterogeneity: 异质性信息没有被 OCR 关键词强烈命中，但从论文主题看，替代关系至少在产品层面而不是代表性消费者层面展开。
- Supply side: 供给侧是显式的：通常包含多产品定价、边际成本恢复、markup 变化和均衡反事实。
- Identification / estimation: 识别依赖工具变量、GMM 或其他矩条件来处理价格与产品属性的内生性。
- Counterfactual / welfare: 模型的终点不是参数本身，而是福利、反事实和政策比较。

## Writing Memory
- 这篇文章的正文结构大体按下面的顺序推进：
- 1. Introduction
- ACCEPTED MANUSCRIPT
- 4. Data
- 3.2 Supply
- 5. Estimation
- 6. Results
- 7. Counterfactual simulations
- 8. Conclusion
- Article (Accepted version) Refereed
- Available in LSE Research Online: February 2017
- LSE Research Online
- LSE THE LONDON SCHOOL OF ECONOMICS AND POLITICAL SCIENCE

## Reusable Writing Moves
- 在模型章节之前先把市场、制度、样本和关键摩擦讲透，让后面的结构设定像是被场景推出而不是凭空假设。
- 把模型的价值落在反事实与福利，而不是只汇报需求系数和价格弹性。
- 正文常见顺序是“模型设定 -> 识别/估计 -> 结果 -> 政策反事实”，避免一上来就堆公式。

## OCR Anchors
- abstract: `Abstract` (p.2) - Abstract The empirical literature on the energy efficiency gap concentrates on demand inefficiencies in the energy-using durables markets and finds evidence that consumers underestimate future energy costs when purchasing a new appliance. We take a broader view and also consider the impact of imperfect competition.
- introduction: `1. Introduction` (p.3) - 1. Introduction In energy and environmental policy circles, it is commonly believed that an “energy efficiency gap” exists between the desirable level of energy consumption and observed consumption (e.g.
- background: `ACCEPTED MANUSCRIPT` (p.3) - ACCEPTED MANUSCRIPT 2 This is only half of the picture, however. On the supply side, manufacturers of energy-using durables also make decisions.
- data: `4. Data` (p.17) - 4. Data We use market data from the refrigerator market in the UK on the product level from 2002 to 2007 collected by the market research company GfK Retail and Technology (received by the Department for Environment, Food and Rural Affairs).
- model: `3.2 Supply` (p.14) - 3.2 Supply In contrast to the demand equation, we adopt a reduced-form approach to assess the impact of imperfect competition on prices. Previous empirical contributions that examine supply-side issues (see the literature review above) generally adopt a structural approach in which multi-product manufacturers compete à la Bertrand.
- estimation: `5. Estimation` (p.25) - 5. Estimation In this section, we specify the different equations and discuss identification issues.
- results: `6. Results` (p.33) - 6. Results
- counterfactual: `7. Counterfactual simulations` (p.36) - 7. Counterfactual simulations In this section, we perform simulations to quantify the impact of the two identified market imperfections on energy consumption and consumer surplus.
- conclusion: `8. Conclusion` (p.42) - 8. Conclusion While the empirical literature on the energy efficiency gap in the residential sector has primarily focused on consumer behavior, this paper develops a comprehensive view of both demand-side and supply-side behaviors that occur in the UK refrigerator market.

## Memory Notes
- 后续回忆这篇论文时，优先调用它的故事梯子、模型嵌入位置、识别策略和反事实落点，而不是只记结论。
- 如果需要公式级别细节，可以直接回到对应 `llm.json` 的 equation chunks 与 model / estimation section。
