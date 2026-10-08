---
name: paper_fmisyr9z_fuel-taxation-emissions-policy-and-competitive-advantage-in-the-diffusion-of-european-dies
description: Fulltext memory for Fuel taxation, emissions policy, and competitive advantage in the diffusion of European diesel automobiles; stores story logic, BLP model construction, estimation, counterfactual use, and writing structure.
type: reference
---

# Fuel taxation, emissions policy, and competitive advantage in the diffusion of European diesel automobiles

## Citation
- Key: `FMISYR9Z`
- DOI: `10.1111/1756-2171.12243`
- Journal: The RAND Journal of Economics
- Year: 2018
- OCR source PDF: `D:\codex\tmp\blp_full_read_20260417\staged_pdfs\FMISYR9Z.pdf`
- OCR JSON: `D:/codex/tmp/blp_full_read_20260417/parsed_all/FMISYR9Z/FMISYR9Z.llm.json`
- Digest JSON: `D:/codex/tmp/blp_full_read_20260417/digests/FMISYR9Z.json`

## Read Status
- 本记忆基于全文 OCR 解析结果整理，不是只看题目、摘要或 Zotero 元数据。
- OCR 流程使用 MinerU 优先、DirectML 加速、输出 `llm.md` / `llm.json` / `chunks.jsonl`。

## Story Question
- Economic integration agreements have significantly decreased import tariffs.

## Story Logic
- 故事起点：Economic integration agreements have significantly decreased import tariffs.
- 制度/市场切口：We show that (a) European fuel taxes and vehicle emissions policy favored diesel vehicles, a technology popular with European consumers but largely offered only by domestic automakers; (b) European automakers benefited from pro‐diesel fuel taxes and a lenient NO x emissions policy to earn significant profits from diesel cars; and (c) that both policies amounted to significant nontariff trade policies equivalent to an import tariff between two to three times the official rate 1.
- 模型推进：核心推进动作是把差异化产品需求或供给均衡模型嵌入实证问题，而不是停留在 reduced-form。
- 结论落点：We show that (a) European fuel taxes and vehicle emissions policy favored diesel vehicles, a technology popular with European consumers but largely offered only by domestic automakers; (b) European automakers benefited from pro‐diesel fuel taxes and a lenient NO x emissions policy to earn significant profits from diesel cars; and (c) that both policies amounted to significant nontariff trade policies equivalent to an import tariff between two to three times the official rate 1.

## BLP Model Memory
- BLP positioning: canonical BLP demand-supply
- Evidence hits: random coefficients, nested logit, discrete choice, bertrand, marginal cost, markup, welfare, counterfactual, instrument, gmm
- Demand side: 需求侧基本可以判定为随机系数离散选择，是最接近经典 BLP 的主干写法。
- Utility construction: 效用写法围绕价格、产品属性、不可观测质量以及个体异质性展开，等价于把平均效用和个体偏离拆开理解。
- Heterogeneity: 异质性是关键层：作者依赖收入、偏好差异、使用场景或消费者类型来刻画不同群体的替代弹性。
- Supply side: 供给侧是显式的：通常包含多产品定价、边际成本恢复、markup 变化和均衡反事实。
- Identification / estimation: 识别依赖工具变量、GMM 或其他矩条件来处理价格与产品属性的内生性。
- Counterfactual / welfare: 论文明确把模型用于税收、补贴、禁令、标签或进入政策的反事实分析。

## Writing Memory
- 这篇文章的正文结构大体按下面的顺序推进：
- 1. Introduction
- Check for updates
- SAMPLE VARIATION OF HOUSEHOLD INCOME
- 5. Estimation
- 7. Concluding remarks
- Fuel taxation, emissions policy, and competitive advantage in the diffusion of European diesel automobiles
- MIRAVETE, MORAL AND THURK
- THE RAND JOURNAL OF ECONOMICS
- 2. The European market for diesel automobiles in the 1990s
- 3. Why are diesels popular in Europe?
- 4. An equilibrium oligopoly model of the automobile industry
- CROSS-PRICE ELASTICITIES

## Reusable Writing Moves
- 在模型章节之前先把市场、制度、样本和关键摩擦讲透，让后面的结构设定像是被场景推出而不是凭空假设。

## OCR Anchors
- introduction: `1. Introduction` (p.0) - 1. Introduction Multilateral trade agreements among countries have driven import tariffs to historic lows (Bergstrand, Larch, and Yotov, 2015).
- background: `Check for updates` (p.0) - Check for updates ∗ The University of Texas at Austin, Centre for Competition Policy/UEA, and CEPR; miravete@eco.utexas.edu. ∗∗ UNED, Paseo Senda del Rey, GRiEE and GRIPICO; mjmoral@cee.uned.es.
- data: `SAMPLE VARIATION OF HOUSEHOLD INCOME` (p.13) - SAMPLE VARIATION OF HOUSEHOLD INCOME Source: Encuesta Continua de Presupuestos Familiares, INE (Spanish Statistical Agency). characteristics and implied marginal costs, where the latter depends on variation in price and market shares via the price coefficient α, plus the shocks to fuel price and steel prices.
- estimation: `5. Estimation` (p.11) - 5. Estimation We define the structural parameters of the model as \theta = [ \alpha , \beta , \gamma , \Sigma , \rho _ { \xi } , \sigma _ { \nu } ^ { 2 } ] and construct the demand-side structural error by creating quasidifferenced moments of consumer mean utility (4a) taking advantage of the \mathbf { A R } ( 1 ) process in which unobserved product quality evolves: Define the demand-side structural error as \varepsilon ^ { D } ( \theta ) = \nu and the supply-side structural error as \varepsilon ^ { S } ( \theta ) = \omega .
- conclusion: `7. Concluding remarks` (p.26) - 7. Concluding remarks The goal in this article was to estimate the tariff-equivalence of two European domestic policies, which favored the domestic automobile industry.

## Memory Notes
- 后续回忆这篇论文时，优先调用它的故事梯子、模型嵌入位置、识别策略和反事实落点，而不是只记结论。
- 如果需要公式级别细节，可以直接回到对应 `llm.json` 的 equation chunks 与 model / estimation section。
