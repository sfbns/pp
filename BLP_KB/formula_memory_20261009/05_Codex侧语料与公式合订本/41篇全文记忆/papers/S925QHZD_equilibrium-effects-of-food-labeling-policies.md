---
name: paper_s925qhzd_equilibrium-effects-of-food-labeling-policies
description: Fulltext memory for Equilibrium Effects of Food Labeling Policies; stores story logic, BLP model construction, estimation, counterfactual use, and writing structure.
type: reference
---

# Equilibrium Effects of Food Labeling Policies

## Citation
- Key: `S925QHZD`
- DOI: `10.3982/ecta19603`
- Journal: Econometrica
- Year: 2023
- OCR source PDF: `D:\codex\tmp\blp_full_read_20260417\staged_pdfs\S925QHZD.pdf`
- OCR JSON: `D:/codex/tmp/blp_full_read_20260417/parsed_all/S925QHZD/S925QHZD.llm.json`
- Digest JSON: `D:/codex/tmp/blp_full_read_20260417/digests/S925QHZD.json`

## Read Status
- 本记忆基于全文 OCR 解析结果整理，不是只看题目、摘要或 Zotero 元数据。
- OCR 流程使用 MinerU 优先、DirectML 加速、输出 `llm.md` / `llm.json` / `chunks.jsonl`。

## Story Question
- We study a regulation in Chile that mandates warning labels on products whose sugar or caloric concentration exceeds certain thresholds.

## Story Logic
- 故事起点：We study a regulation in Chile that mandates warning labels on products whose sugar or caloric concentration exceeds certain thresholds.
- 制度/市场切口：We study a regulation in Chile that mandates warning labels on products whose sugar or caloric concentration exceeds certain thresholds.
- 模型推进：We develop and estimate an equilibrium model of demand for food and firms' pricing and nutritional choices.
- 结论落点：We find that food labels increase consumer welfare by 1.8% of total expenditure, and that these effects are enhanced by firms' responses.

## BLP Model Memory
- BLP positioning: canonical BLP demand-supply
- Evidence hits: random coefficients, nested logit, marginal cost, markup, welfare, counterfactual, instrument, gmm
- Demand side: 全文表明作者在做结构化产品需求分析，但 OCR 证据不足以把需求形式精确钉死到某个 logit 变体。
- Utility construction: 模型核心仍然是“价格 + 产品属性 + 未观测质量”决定选择概率，再由市场份额把需求参数识别出来。
- Heterogeneity: 异质性信息没有被 OCR 关键词强烈命中，但从论文主题看，替代关系至少在产品层面而不是代表性消费者层面展开。
- Supply side: 供给侧是显式的：通常包含多产品定价、边际成本恢复、markup 变化和均衡反事实。
- Identification / estimation: 识别依赖工具变量、GMM 或其他矩条件来处理价格与产品属性的内生性。
- Counterfactual / welfare: 模型的终点不是参数本身，而是福利、反事实和政策比较。

## Writing Memory
- 这篇文章的正文结构大体按下面的顺序推进：
- Introduction
- Background / Data
- Model
- Estimation
- Results
- Counterfactual / Welfare
- Conclusion

## Reusable Writing Moves
- 把模型的价值落在反事实与福利，而不是只汇报需求系数和价格弹性。

## OCR Anchors
- 当前还没有稳定识别到标准 section heading，需要回到 OCR JSON 做人工定位。

## Memory Notes
- 后续回忆这篇论文时，优先调用它的故事梯子、模型嵌入位置、识别策略和反事实落点，而不是只记结论。
- 如果需要公式级别细节，可以直接回到对应 `llm.json` 的 equation chunks 与 model / estimation section。
