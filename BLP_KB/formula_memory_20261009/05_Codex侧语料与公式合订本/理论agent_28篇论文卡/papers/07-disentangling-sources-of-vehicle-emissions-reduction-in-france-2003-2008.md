# Structural Model Stable Card: Disentangling sources of vehicle emissions reduction in France: 2003–2008

## Identity
- domain: `structural_models`
- internal_card_id: `structural::9HUJHUTJ::core`
- rank: `7`
- item_key: `9HUJHUTJ`
- classification: `canonical BLP demand-supply`
- classification_note: Canonical differentiated-product demand and supply system with welfare or counterfactual use.
- journal: `International Journal of Industrial Organization`
- date: `2016-00-00 2016`
- authors: Xavier D’Haultfoeuille, Isis Durrmeyer, Philippe Février
- internal_card_path: `D:\codex\economics_theory_agent_complete_gpt55_xhigh\kb\03_structural_models\blp_structural_corpus\papers\07-disentangling-sources-of-vehicle-emissions-reduction-in-france-2003-2008.md`
- source_paper_memory_path: `D:\codex\blp_structural_memory_2026-04-18\memories\papers\07_9hujhutj.md`
- source_paper_json_path: `D:\codex\blp_structural_memory_2026-04-18\memories\json\07_9hujhutj.json`
- source_master_memory_path: `D:\codex\blp_structural_memory_2026-04-18\memories\blp_structural_enhanced_master_memory.md`

## Citation Memory
- reference: D’Haultfoeuille, X., Durrmeyer, I., & Février, P. (2016). Disentangling sources of vehicle emissions reduction in France: 2003–2008. International Journal of Industrial Organization. https://doi.org/10.1016/j.ijindorg.2016.05.002
- parenthetical: (D’Haultfoeuille et al., 2016)
- narrative: D’Haultfoeuille et al. (2016)

## Story Logic
- The paper decomposes the fall in vehicle emissions in France between 2003 and 2008.
- Its main finding is that policy mattered, but not all policy instruments mattered equally.
- A large share of the emissions decline is attributed to changing preferences, while registration-tax CO2 sensitivity and feebate design also matter.
- Real-world tension or puzzle: emissions from new vehicles were falling, but the drivers of that decline were not obvious.
- Why the puzzle matters now: policy makers need to know whether taxes, fuel prices, or preference shifts are doing the work.
- What the literature already explains: emission outcomes respond to both fiscal policy and consumer choice.
- What is still missing or weakly identified: a source-by-source decomposition of the decline.
- The paper's move: separate the effects of registration taxes, annual taxes, fuel prices, and preference shifts.
- Main payoff: policy is important, but changing consumer preference explains a surprisingly large part of the decline.

## Structural Core
- Research design type: structural decomposition / policy attribution.
- Structural model class or reduced-form design: vehicle-choice model with emissions and tax policy.
- Key equations or choice objects: household choice among car models under tax schedules and fuel costs.
- Endogeneity problem: emissions, prices, and taxes are jointly shaped by market equilibrium.
- Identification strategy: use the structure of taxes and market variation to isolate channels.
- What assumptions are doing the heavy lifting: stable demand and correct mapping from policy to vehicle attributes.
- BLP positioning: canonical BLP demand-supply
- Evidence hits: mixed logit, nested logit, bertrand, marginal cost, welfare, counterfactual, instrument
- Demand side: 需求侧更像嵌套 logit / 分层离散选择，保留了产品空间替代结构，但异质性比经典 BLP 更轻。
- Utility construction: 效用写法围绕价格、产品属性、不可观测质量以及个体异质性展开，等价于把平均效用和个体偏离拆开理解。
- Heterogeneity: 异质性是关键层：作者依赖收入、偏好差异、使用场景或消费者类型来刻画不同群体的替代弹性。
- Supply side: 供给侧较轻或被外生化，论文重心更偏需求恢复、替代矩阵和消费者/社会福利。
- Identification / estimation: 识别主要靠制度冲击或自然实验，把外生变化灌进结构模型。
- Counterfactual / welfare: 论文明确把模型用于税收、补贴、禁令、标签或进入政策的反事实分析。

## Data And Measurement
- Unit of observation: new passenger cars / market choices in France.
- Market definition: French vehicle market over 2003-2008.
- Main dependent variable: vehicle emissions intensity.
- Core explanatory variables: registration taxes, annual taxes, feebate incentives, and fuel prices.
- Instruments / moments / shocks: tax schedule variation and market shares.
- Important sample restrictions: French new-car market during the study window; OCR gave the broad design more clearly than every data detail.

## Mechanisms, Results, And Counterfactuals
- Baseline result: registration taxes that are more CO2-sensitive reduce CO2 intensity, with a reported elasticity of about 0.1% per 1% increase.
- Mechanism evidence: feebate design has a crowding-in effect, suggesting policy can shift the composition of purchases.
- Heterogeneity evidence: annual taxes have little effect, so not all recurring taxes work the same way.
- Welfare or counterfactual result: changing preferences accounts for roughly 40% of the overall emissions decline.
- Limits the authors admit: the decomposition depends on the quality of the structural attribution, so some channel shares are model-based rather than directly observed.

## Writing Memory
- Introduction move sequence: emissions decline -> attribution puzzle -> decomposition strategy -> main shares.
- Section order: policy context, model, data, estimation, decomposition results, conclusion.
- Where the paper turns from setup to payoff: when it separates preference change from tax effects.
- How tables/figures are used to move the argument: tables likely show channel shares and policy elasticities; OCR was sufficient for the headline numbers but not for every exhibit label.
- Best framing sentence pattern: "When an outcome moves, the key question is which channel moved it."
- Best transition pattern: move from aggregate trend to channel decomposition.
- Best contribution sentence pattern: "We disentangle the sources of the emissions decline."
- Best limitation or implication move: "Policy design matters, but demand-side preference shifts can be just as important."
- Durable economics-writing principle: decomposition is stronger than correlation when multiple policy channels move together.
- Durable structural-model principle: taxes should be interpreted through the choice margin they actually move.
- Reusable empirical design idea: build a policy attribution exercise around a real observed aggregate decline.
- Follow-up paper to pair with this one: a study that decomposes CO2 reductions into pricing, technology, and preference channels in another market.
- 这篇文章的正文结构大体按下面的顺序推进：
- 1. Introduction
- 4. Estimation results
- 5. Conclusion
- Disentangling sources of vehicle emissions reduction in France: 2003-2008✩
- a r t i c l e i n f o
- a b s t r a c t
- International Journal of Industrial Organization 47 (2016) 186-229
- Contents lists available at ScienceDirect
- International Journal of Industrial Organization
- 2. Environmental policies and evolution of \mathbf { C O _ { 2 } } emissions
- 2.1. Energy labels and the feebate system
- 2.2. Evolution of C O _ { 2 } emissions
- 典型 BLP 写法是先提出现实政策问题，再说明为什么需要结构模型，最后把替代关系转成福利与政策比较。
- 后续回忆这篇论文时，优先调用它的故事梯子、模型嵌入位置、识别策略和反事实落点，而不是只记结论。
- 如果需要公式级别细节，可以直接回到对应 `llm.json` 的 equation chunks 与 model / estimation section。

## Evidence Anchors
- intro: page 2 | X. D’Haultfœuille et al. / International Journal of Industrial Organization 47 (2016) 186–229 187 1. Introduction In this paper, we study the evolution of carbon dioxide (CO 2 ) emissions of new ve...
- data: page 1 | reserved. ✩ We would like to thank the editor and two anonymous referees for their constructive comments. We acknowledge Pierre-Louis Debar and Julien Mollet from the CCFA for providing us with the...
- model: page 1 | o policies introduced during that time: the energy label requirement, which went into eﬀect in the end of 2005, and a feebate based on CO 2 emissions of new vehicles in 2008. We estimate a ﬂexible...
- results: page 1 | ebate based on CO 2 emissions of new vehicles in 2008. We estimate a ﬂexible model of demand for automobiles that incorporates consumers’ heterogeneity and valuation of vehicle CO 2 emissions. Our...
- conclusion: page 31 | reased by about 50%. Even though other phenomena are probably in play in 2009, these evo- lutions suggest that the sharp changes following the introduction of the feebate are not temporary. 22 5. C...

## Reuse Notes
- Use this card when deciding whether a structural model is needed, what endogenous object must be recovered, and which counterfactual or welfare question is actually identified.
- Reopen the full paper memory or fulltext only when equation-level structure, instruments, or moment conditions matter.

## Summary
- The paper decomposes the fall in vehicle emissions in France between 2003 and 2008. Its main finding is that policy mattered, but not all policy instruments mattered equally.
