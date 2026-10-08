# Structural Model Stable Card: What does an electric vehicle replace?

## Identity
- domain: `structural_models`
- internal_card_id: `structural::LXUZM7VX::core`
- rank: `27`
- item_key: `LXUZM7VX`
- classification: `canonical BLP demand-supply`
- classification_note: Canonical differentiated-product demand and supply system with welfare or counterfactual use.
- journal: `Journal of Environmental Economics and Management`
- date: `2021-00-00 2021`
- authors: Jianwei Xing, Benjamin Leard, Shanjun Li
- internal_card_path: `D:\codex\economics_theory_agent_complete_gpt55_xhigh\kb\03_structural_models\blp_structural_corpus\papers\27-what-does-an-electric-vehicle-replace.md`
- source_paper_memory_path: `D:\codex\blp_structural_memory_2026-04-18\memories\papers\27_lxuzm7vx.md`
- source_paper_json_path: `D:\codex\blp_structural_memory_2026-04-18\memories\json\27_lxuzm7vx.json`
- source_master_memory_path: `D:\codex\blp_structural_memory_2026-04-18\memories\blp_structural_enhanced_master_memory.md`

## Citation Memory
- reference: Xing, J., Leard, B., & Li, S. (2021). What does an electric vehicle replace?. Journal of Environmental Economics and Management. https://doi.org/10.1016/j.jeem.2021.102432
- parenthetical: (Xing et al., 2021)
- narrative: Xing et al. (2021)

## Story Logic
- The paper asks what vehicles EVs actually replace, because emissions benefits depend on the substitute, not just on the new EV sale.
- Its answer is that replacement is non-random and EVs often displace gasoline cars with above-average fuel economy.
- The payoff is a more realistic emissions accounting and a better basis for subsidy design.
- Real-world tension or puzzle: an EV policy can look good on adoption counts while still replacing relatively efficient gasoline cars.
- Why the puzzle matters now: emissions policy needs counterfactual replacement, not just sales growth.
- What the literature already explains: many studies estimate EV adoption, but fewer infer the full substitution matrix.
- What is still missing or weakly identified: the mapping from an EV purchase to the gasoline car it replaces.
- The paper's move: estimate a random-coefficients demand model with second-choice data and counterfactual removal of EVs.
- Main payoff: emissions benefits are smaller than naive replacement assumptions would imply.

## Structural Core
- Research design type: structural demand estimation with counterfactual simulation.
- Structural model class or reduced-form design: random-coefficients discrete choice model.
- Key equations or choice objects: vehicle demand, substitution patterns, and cross-price elasticities.
- Endogeneity problem: substitution is not random, and simple replacement assumptions are too coarse.
- Identification strategy: combine household survey data, vehicle characteristics, registrations, and second-choice information.
- What assumptions are doing the heavy lifting: the demand system and the interpretation of reported second choices.
- BLP positioning: canonical BLP demand-supply
- Evidence hits: random coefficients, discrete choice, marginal cost, welfare, counterfactual, instrument
- Demand side: 需求侧基本可以判定为随机系数离散选择，是最接近经典 BLP 的主干写法。
- Utility construction: 效用写法围绕价格、产品属性、不可观测质量以及个体异质性展开，等价于把平均效用和个体偏离拆开理解。
- Heterogeneity: 异质性是关键层：作者依赖收入、偏好差异、使用场景或消费者类型来刻画不同群体的替代弹性。
- Supply side: 供给侧较轻或被外生化，论文重心更偏需求恢复、替代矩阵和消费者/社会福利。
- Identification / estimation: 识别依赖工具变量、GMM 或其他矩条件来处理价格与产品属性的内生性。
- Counterfactual / welfare: 模型的终点不是参数本身，而是福利、反事实和政策比较。

## Data And Measurement
- Unit of observation: household vehicle choice / market share information.
- Market definition: US new-vehicle market with EV alternatives.
- Main dependent variable: vehicle choice and implied replacement pattern.
- Core explanatory variables: vehicle price, characteristics, EV availability, and fuel economy.
- Instruments / moments / shocks: the counterfactual is built from the estimated demand system rather than a quasi-experimental shock.
- Important sample restrictions: some EV models lack substitute-choice data, and the paper notes this limitation.

## Mechanisms, Results, And Counterfactuals
- Baseline result: EVs replace gasoline cars with higher-than-average fuel economy.
- Mechanism evidence: second-choice data show that many EV buyers were also considering hybrids or plug-in hybrids.
- Heterogeneity evidence: the replacement pattern differs across EV models and consumer groups.
- Welfare or counterfactual result: ignoring non-random replacement overstates emissions benefits; the paper also compares the current uniform subsidy with alternatives that induce more incremental EV purchases.
- Limits the authors admit: some EV models are missing substitute-choice data, so exact replacement shares are not equally precise everywhere.

## Writing Memory
- Introduction move sequence: emissions puzzle -> replacement assumption problem -> data and model -> policy implication.
- Section order: intro -> stylized model -> data -> demand estimation -> counterfactuals -> conclusion.
- Where the paper turns from setup to payoff: once it shows that replacement patterns are non-random.
- How tables/figures are used to move the argument: second-choice tables and counterfactual emissions tables do the core work.
- Best framing sentence pattern: "The relevant counterfactual is not whether an EV is purchased, but what it displaces."
- Best transition pattern: "We next estimate the replacement pattern rather than impose one."
- Best contribution sentence pattern: "A better emissions calculation starts with a better demand model."
- Best limitation or implication move: always say what part of the replacement matrix is data-driven and what part is assumed.
- Durable economics-writing principle: when a policy effect depends on the substitute, estimate the substitute.
- Durable structural-model principle: cross-price elasticities are the bridge from demand to emissions accounting.
- Reusable empirical design idea: second-choice data can upgrade a standard demand model into a policy-evaluation tool.
- Follow-up paper to pair with this one: any EV emissions paper that needs a realistic replacement baseline.
- 这篇文章的正文结构大体按下面的顺序推进：
- 1. Introduction
- Journal of Environmental Economics and Management 107 (2021) 102432
- 2. Data description
- 4.2. Identification
- 6. Counterfactual analysis
- 7. Discussion
- What does an electric vehicle replace?
- a r t i c l e i n f o
- a b s t r a c t
- Contents lists available at ScienceDirect
- ELSEVIER
- Journal of Environmental Economics and Management
- 在模型章节之前先把市场、制度、样本和关键摩擦讲透，让后面的结构设定像是被场景推出而不是凭空假设。
- 把模型的价值落在反事实与福利，而不是只汇报需求系数和价格弹性。
- 后续回忆这篇论文时，优先调用它的故事梯子、模型嵌入位置、识别策略和反事实落点，而不是只记结论。
- 如果需要公式级别细节，可以直接回到对应 `llm.json` 的 equation chunks 与 model / estimation section。

## Evidence Anchors
- intro: page 1 | dy designs, we ﬁnd that a subsidy designed to provide greater incentives to low-income households would have been more cost effective and less regressive. © 2021 Elsevier Inc. All rights reserved....
- data: page 1 | December 2019 Revised 28 November 2020 Accepted 11 February 2021 Available online 17 March 2021 JEL classiﬁcation: L91 Q48 Q51 Keywords: Electric vehicles Substitution Demand estimation Second choi...
- model: page 1 | te the emissions reductions from electric vehicles (EVs) by identifying which vehicles would have been purchased had EVs not been available. We do so by estimating a random coeﬃcients discrete choi...
- results: page 1 | e. We do so by estimating a random coeﬃcients discrete choice model of new vehicle demand and simulating counterfactual sales with EVs no longer subsidized or removed from the new vehicle market. O...
- conclusion: page  | 

## Reuse Notes
- Use this card when deciding whether a structural model is needed, what endogenous object must be recovered, and which counterfactual or welfare question is actually identified.
- Reopen the full paper memory or fulltext only when equation-level structure, instruments, or moment conditions matter.

## Summary
- The paper asks what vehicles EVs actually replace, because emissions benefits depend on the substitute, not just on the new EV sale. Its answer is that replacement is non-random and EVs often displace gasoline cars with above-average fuel economy.
