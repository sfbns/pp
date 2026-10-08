# Structural Model Stable Card: Hurdles and steps: Estimating demand for solar photovoltaics

## Identity
- domain: `structural_models`
- internal_card_id: `structural::JKYIT7SD::core`
- rank: `14`
- item_key: `JKYIT7SD`
- classification: `BLP-adjacent structural policy model`
- classification_note: Policy-oriented structural model that borrows the BLP logic but adapts the state, choice, or market environment.
- journal: `Quantitative Economics`
- date: `2019-00-00 2019`
- authors: Kenneth Gillingham, Tsvetan Tsvetanov
- internal_card_path: `D:\codex\economics_theory_agent_complete_gpt55_xhigh\kb\03_structural_models\blp_structural_corpus\papers\14-hurdles-and-steps-estimating-demand-for-solar-photovoltaics.md`
- source_paper_memory_path: `D:\codex\blp_structural_memory_2026-04-18\memories\papers\14_jkyit7sd.md`
- source_paper_json_path: `D:\codex\blp_structural_memory_2026-04-18\memories\json\14_jkyit7sd.json`
- source_master_memory_path: `D:\codex\blp_structural_memory_2026-04-18\memories\blp_structural_enhanced_master_memory.md`

## Citation Memory
- reference: Gillingham, K., & Tsvetanov, T. (2019). Hurdles and steps: Estimating demand for solar photovoltaics. Quantitative Economics. https://doi.org/10.3982/QE919
- parenthetical: (Gillingham & Tsvetanov, 2019)
- narrative: Gillingham and Tsvetanov (2019)

## Story Logic
- The paper solves a demand estimation problem for solar PV adoption when the data are sparse, zero-heavy, and price is endogenous.
- Its answer is a Poisson hurdle model with fixed effects and IV that separates adoption from intensity and allows the authors to recover a usable price elasticity.
- The result matters because it turns a hard policy question, whether subsidies change real PV uptake, into a counterfactual the paper can quantify.
- Real-world tension or puzzle: many blocks never install PV at all, while the positive adopters are highly heterogeneous.
- Why the puzzle matters now: state incentives and installer pricing can move adoption, but simple count models miss the zero mass and endogeneity.
- What the literature already explains: standard count models or generic discrete-choice approaches handle only part of the problem.
- What is still missing or weakly identified: a design that jointly handles zeros, fixed effects, and endogenous price.
- The paper's move: build an IV Poisson hurdle specification tailored to PV adoption.
- Main payoff: the paper can run policy counterfactuals, including a halving of state incentives and the implied emissions cost.

## Structural Core
- Research design type: reduced-form structural count-data model with a first-stage adoption hurdle.
- Structural model class or reduced-form design: Poisson hurdle with fixed effects.
- Key equations or choice objects: one process for whether adoption occurs, a second for how many systems are adopted conditional on crossing the hurdle.
- Endogeneity problem: PV price is correlated with unobserved demand shifters.
- Identification strategy: instrument price inside the hurdle framework and use panel fixed effects to absorb time-invariant local heterogeneity.
- What assumptions are doing the heavy lifting: the exclusion restriction for price instruments and the separability between participation and intensity.
- BLP positioning: BLP-adjacent structural policy model
- Evidence hits: discrete choice, marginal cost, welfare, counterfactual, instrument, gmm
- Demand side: 全文表明作者在做结构化产品需求分析，但 OCR 证据不足以把需求形式精确钉死到某个 logit 变体。
- Utility construction: 效用写法围绕价格、产品属性、不可观测质量以及个体异质性展开，等价于把平均效用和个体偏离拆开理解。
- Heterogeneity: 异质性是关键层：作者依赖收入、偏好差异、使用场景或消费者类型来刻画不同群体的替代弹性。
- Supply side: 供给侧较轻或被外生化，论文重心更偏需求恢复、替代矩阵和消费者/社会福利。
- Identification / estimation: 识别依赖工具变量、GMM 或其他矩条件来处理价格与产品属性的内生性。
- Counterfactual / welfare: 模型的终点不是参数本身，而是福利、反事实和政策比较。

## Data And Measurement
- Unit of observation: fine geographic panel data on PV adoption.
- Market definition: local PV demand market over time.
- Main dependent variable: PV installation count.
- Core explanatory variables: PV price and policy incentive measures.
- Instruments / moments / shocks: the paper uses an instrument set for price; the exact set is described in the empirical section.
- Important sample restrictions: the model is built to handle excess zeros and local heterogeneity, so those features are central rather than trimmed away.

## Mechanisms, Results, And Counterfactuals
- Baseline result: estimated price elasticity is about `-0.65`.
- Mechanism evidence: the hurdle structure shows that the extensive margin matters, not just count intensity.
- Heterogeneity evidence: local fixed effects absorb large site-specific differences in adoption propensity.
- Welfare or counterfactual result: halving state incentives is associated with about 9 percent fewer installs in Connecticut in 2014; the implied abatement cost is reported around `$364/tCO2` under the natural-gas displacement assumption.
- Limits the authors admit: the exact policy welfare answer depends on what PV displaces and on the maintained instrument assumptions.

## Writing Memory
- Introduction move sequence: puzzle -> three empirical challenges -> model choice -> policy payoff.
- Section order: intro -> data -> model -> estimation -> counterfactuals -> conclusion.
- Where the paper turns from setup to payoff: once the hurdle model is introduced and the price endogeneity issue is resolved.
- How tables/figures are used to move the argument: they likely carry the adoption patterns and the elasticity/counterfactual results, though some figure detail is not fully visible in the text extraction.
- Best framing sentence pattern: "This paper addresses three challenges at once: zero inflation, heterogeneity, and endogenous price."
- Best transition pattern: "Having solved the estimation problem, we can now answer the policy question."
- Best contribution sentence pattern: "We develop a model that is new enough to identify what policy design changes adoption."
- Best limitation or implication move: always translate elasticities into a concrete policy counterfactual and then into cost per ton.
- Durable economics-writing principle: list the empirical frictions before the method, so the method feels necessary rather than decorative.
- Durable structural-model principle: separate participation from intensity when zeros are economically meaningful.
- Reusable empirical design idea: IV plus fixed effects can make nonlinear count models policy-relevant.
- Follow-up paper to pair with this one: any paper on zero-heavy technology adoption with local policy variation.
- 这篇文章的正文结构大体按下面的顺序推进：
- 1. Introduction
- 2. Background on solar PV policies in Connecticut
- 3. Data
- 6. Results
- 7. Policy analysis
- 8. Conclusions
- Hurdles and steps: Estimating demand for solar photovoltaics
- Kenneth Gillingham
- Tsvetan Tsvetanov Department of Economics, University of Kansas
- Quantitative Economics 10 (2019), 275-310
- Gillingham and Tsvetanov
- Quantitative Economics 10 (2019)
- 在模型章节之前先把市场、制度、样本和关键摩擦讲透，让后面的结构设定像是被场景推出而不是凭空假设。
- 把模型的价值落在反事实与福利，而不是只汇报需求系数和价格弹性。
- 后续回忆这篇论文时，优先调用它的故事梯子、模型嵌入位置、识别策略和反事实落点，而不是只记结论。
- 如果需要公式级别细节，可以直接回到对应 `llm.json` 的 equation chunks 与 model / estimation section。

## Evidence Anchors
- intro: page 1 | omise for modeling the demand for many new technologies. Keywords. Count data, hurdle model, ﬁxed effects, instrumental variables, Pois- son, energy policy. JEL classification. C33, C36, Q42, Q48....
- data: page 1 | t of Economics, University of Kansas This paper estimates demand for residential solar photovoltaic (PV) systems using a new approach to address three empirical challenges that often arise with cou...
- model: page 1 | est a subsidy program cost of $364/tCO2 assuming solar displaces natural gas. Our Poisson hurdle approach holds promise for modeling the demand for many new technologies. Keywords. Count data, hurd...
- results: page 3 | m and Tsvetanov (2019)) suggesting that solar PV demand in CT is more similar to the many other contexts where consumers do not appear to treat adoption as a dynamic “buy-or-wait” decision. Using o...
- conclusion: page  | 

## Reuse Notes
- Use this card when deciding whether a structural model is needed, what endogenous object must be recovered, and which counterfactual or welfare question is actually identified.
- Reopen the full paper memory or fulltext only when equation-level structure, instruments, or moment conditions matter.

## Summary
- The paper solves a demand estimation problem for solar PV adoption when the data are sparse, zero-heavy, and price is endogenous. Its answer is a Poisson hurdle model with fixed effects and IV that separates adoption from intensity and allows the authors to recover a usable pr...
