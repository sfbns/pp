# Structural Model Stable Card: Consumer myopia, imperfect competition and the energy efficiency gap: Evidence from the UK refrigerator market

## Identity
- domain: `structural_models`
- internal_card_id: `structural::UNMC2I56::core`
- rank: `5`
- item_key: `UNMC2I56`
- classification: `canonical BLP demand-supply`
- classification_note: Canonical differentiated-product demand and supply system with welfare or counterfactual use.
- journal: `European Economic Review`
- date: `2017-00-00 2017`
- authors: François Cohen, Matthieu Glachant, Magnus Söderberg
- internal_card_path: `D:\codex\economics_theory_agent_complete_gpt55_xhigh\kb\03_structural_models\blp_structural_corpus\papers\05-consumer-myopia-imperfect-competition-and-the-energy-efficiency-gap-evidence-from-the-uk-refrigerator-market.md`
- source_paper_memory_path: `D:\codex\blp_structural_memory_2026-04-18\memories\papers\05_unmc2i56.md`
- source_paper_json_path: `D:\codex\blp_structural_memory_2026-04-18\memories\json\05_unmc2i56.json`
- source_master_memory_path: `D:\codex\blp_structural_memory_2026-04-18\memories\blp_structural_enhanced_master_memory.md`

## Citation Memory
- reference: Cohen, F., Glachant, M., & Söderberg, M. (2017). Consumer myopia, imperfect competition and the energy efficiency gap: Evidence from the UK refrigerator market. European Economic Review. https://doi.org/10.1016/j.euroecorev.2017.01.004
- parenthetical: (Cohen et al., 2017)
- narrative: Cohen et al. (2017)

## Story Logic
- The paper asks whether the energy efficiency gap in refrigerators is driven by consumer myopia and imperfect competition.
- It finds that consumers do undervalue future energy savings, but the resulting energy-use effect is modest.
- The broader implication is that the gap exists, but this market's inefficiency is smaller than the strongest behavioral stories suggest.
- Real-world tension or puzzle: energy-efficient appliances often do not sell as much as engineering calculations imply they should.
- Why the puzzle matters now: policy debates hinge on whether the gap is behavioral, market-power driven, or both.
- What the literature already explains: myopia and imperfect competition are both plausible explanations.
- What is still missing or weakly identified: a market-level decomposition of how much each channel actually matters.
- The paper's move: estimate demand and counterfactuals in the UK refrigerator market.
- Main payoff: myopia matters, but not enough to explain the whole gap.

## Structural Core
- Research design type: structural demand and counterfactual analysis.
- Structural model class or reduced-form design: refrigerator choice model with energy costs and imperfect competition.
- Key equations or choice objects: consumer utility over purchase price, operating cost, and product attributes.
- Endogeneity problem: observed prices and qualities reflect firm strategic pricing and consumer preferences.
- Identification strategy: infer willingness to pay and discounting from observed product choices and market structure.
- What assumptions are doing the heavy lifting: stable demand, credible fuel-cost expectations benchmark, and firm pricing behavior.
- BLP positioning: canonical BLP demand-supply
- Evidence hits: mixed logit, nested logit, discrete choice, bertrand, marginal cost, markup, welfare, counterfactual, instrument, gmm
- Demand side: 需求侧更像嵌套 logit / 分层离散选择，保留了产品空间替代结构，但异质性比经典 BLP 更轻。
- Utility construction: 模型核心仍然是“价格 + 产品属性 + 未观测质量”决定选择概率，再由市场份额把需求参数识别出来。
- Heterogeneity: 异质性信息没有被 OCR 关键词强烈命中，但从论文主题看，替代关系至少在产品层面而不是代表性消费者层面展开。
- Supply side: 供给侧是显式的：通常包含多产品定价、边际成本恢复、markup 变化和均衡反事实。
- Identification / estimation: 识别依赖工具变量、GMM 或其他矩条件来处理价格与产品属性的内生性。
- Counterfactual / welfare: 模型的终点不是参数本身，而是福利、反事实和政策比较。

## Data And Measurement
- Unit of observation: refrigerator products / market shares in the UK.
- Market definition: UK refrigerator retail market.
- Main dependent variable: product choice and implied energy consumption.
- Core explanatory variables: purchase price, operating cost, energy label / efficiency, and competition structure.
- Instruments / moments / shocks: not fully extracted from OCR; likely product market moments rather than a single external instrument.
- Important sample restrictions: refrigerator market only; precise sample window was not fully recoverable from OCR.

## Mechanisms, Results, And Counterfactuals
- Baseline result: average energy consumption is only about 7.2% higher than the perfect-competition, non-myopic benchmark.
- Mechanism evidence: consumers underestimate future energy savings by about 35%.
- Heterogeneity evidence: the myopia channel exists, but its aggregate effect is smaller than many policy arguments imply.
- Welfare or counterfactual result: imperfect competition lowers energy use somewhat, but the gap remains.
- Limits the authors admit: the paper is one market and one product category, so generalization should be cautious.

## Writing Memory
- Introduction move sequence: puzzle -> candidate explanations -> empirical gap -> market study -> result.
- Section order: background, model, data, estimation, counterfactuals, conclusion.
- Where the paper turns from setup to payoff: once the benchmark comparison shows the gap is smaller than expected.
- How tables/figures are used to move the argument: tables likely anchor the estimated discounting and counterfactual energy consumption; OCR did not fully expose every exhibit.
- Best framing sentence pattern: "The efficiency gap may be real, but its size is an empirical question."
- Best transition pattern: move from observed underinvestment to structural decomposition.
- Best contribution sentence pattern: "We quantify how much myopia and imperfect competition jointly matter."
- Best limitation or implication move: "Policy should be calibrated to the size of the gap, not its existence alone."
- Durable economics-writing principle: do not stop at identifying a gap; measure its magnitude.
- Durable structural-model principle: compare the observed market to a benchmark that separates behavior from structure.
- Reusable empirical design idea: decompose a policy problem into behavioral and market-power components.
- Follow-up paper to pair with this one: a study of appliance labels or operating-cost disclosure in another durable-good market.
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
- 在模型章节之前先把市场、制度、样本和关键摩擦讲透，让后面的结构设定像是被场景推出而不是凭空假设。
- 把模型的价值落在反事实与福利，而不是只汇报需求系数和价格弹性。
- 正文常见顺序是“模型设定 -> 识别/估计 -> 结果 -> 政策反事实”，避免一上来就堆公式。
- 后续回忆这篇论文时，优先调用它的故事梯子、模型嵌入位置、识别策略和反事实落点，而不是只记结论。
- 如果需要公式级别细节，可以直接回到对应 `llm.json` 的 equation chunks 与 model / estimation section。

## Evidence Anchors
- intro: page 3 | ndon School of Economics and Political Science, London, UK Matthieu Glachant, MINES ParisTech and PSL – Research University, Paris, France* Magnus Söderberg, University of Gothenburg, Sweden Abstra...
- data: page 3 | les markets and finds evidence that consumers underestimate future energy costs when purchasing a new appliance. We take a broader view and also consider the impact of imperfect competition. Using...
- model: page 7 | ient goods than on less efficient ones – as is the case in the UK refrigerator market in this paper – then subsidies should be lower than they would be if prices were equal to marginal costs.4 We m...
- results: page 9 | ioning of durable goods markets. Section 3 develops the conceptual framework. Section 4 presents the data. Section 5 outlines our empirical strategy and addresses identification issues. Estimation...
- conclusion: page 43 | , the profit loss is the same when shifting to perfect competition or shifting to perfect competition without myopia: it corresponds to the average profit in the “business-as- usual” situation. 8....

## Reuse Notes
- Use this card when deciding whether a structural model is needed, what endogenous object must be recovered, and which counterfactual or welfare question is actually identified.
- Reopen the full paper memory or fulltext only when equation-level structure, instruments, or moment conditions matter.

## Summary
- The paper asks whether the energy efficiency gap in refrigerators is driven by consumer myopia and imperfect competition. It finds that consumers do undervalue future energy savings, but the resulting energy-use effect is modest.
