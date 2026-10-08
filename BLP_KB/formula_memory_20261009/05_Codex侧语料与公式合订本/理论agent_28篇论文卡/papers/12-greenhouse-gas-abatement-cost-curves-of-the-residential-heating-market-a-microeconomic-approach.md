# Structural Model Stable Card: Greenhouse Gas Abatement Cost Curves of the Residential Heating Market: A Microeconomic Approach

## Identity
- domain: `structural_models`
- internal_card_id: `structural::96LPI5MZ::core`
- rank: `12`
- item_key: `96LPI5MZ`
- classification: `canonical BLP demand-supply`
- classification_note: Canonical differentiated-product demand and supply system with welfare or counterfactual use.
- journal: `Environmental and Resource Economics`
- date: `2017-00-00 2017`
- authors: Caroline Löffler, Harald Hecking
- internal_card_path: `D:\codex\economics_theory_agent_complete_gpt55_xhigh\kb\03_structural_models\blp_structural_corpus\papers\12-greenhouse-gas-abatement-cost-curves-of-the-residential-heating-market-a-microeconomic-approach.md`
- source_paper_memory_path: `D:\codex\blp_structural_memory_2026-04-18\memories\papers\12_96lpi5mz.md`
- source_paper_json_path: `D:\codex\blp_structural_memory_2026-04-18\memories\json\12_96lpi5mz.json`
- source_master_memory_path: `D:\codex\blp_structural_memory_2026-04-18\memories\blp_structural_enhanced_master_memory.md`

## Citation Memory
- reference: Löffler, C., & Hecking, H. (2017). Greenhouse Gas Abatement Cost Curves of the Residential Heating Market: A Microeconomic Approach. Environmental and Resource Economics. https://doi.org/10.1007/s10640-016-0052-0
- parenthetical: (Löffler & Hecking, 2017)
- narrative: Löffler and Hecking (2017)

## Story Logic
- The paper builds greenhouse-gas abatement cost curves for the residential heating market using a microeconomic approach.
- Its key message is that welfare-based abatement costs are generally higher than simple engineering equipment costs.
- The important twist is that once consumer behavior is modeled explicitly, policy rankings can change, and subsidies may dominate carbon taxes under misperception.
- Real-world tension or puzzle: abatement cost curves are often built from technical costs, not from household welfare.
- Why the puzzle matters now: climate policy should reflect actual consumer decisions in durable-energy markets.
- What the literature already explains: technical abatement is cheaper on paper than it may be in welfare terms.
- What is still missing or weakly identified: a microeconomic, welfare-based cost curve for residential heating.
- The paper's move: estimate costs from household choice and welfare, not just equipment engineering.
- Main payoff: the true marginal cost of abatement can be substantially higher, and behavioral errors can flip policy rankings.

## Structural Core
- Research design type: welfare-based cost-curve construction.
- Structural model class or reduced-form design: household choice model for residential heating technologies.
- Key equations or choice objects: heating-system adoption, costs, and welfare under alternative policies.
- Endogeneity problem: equipment costs, preferences, and policy incentives affect observed adoption jointly.
- Identification strategy: recover household willingness to pay and compare policy counterfactuals.
- What assumptions are doing the heavy lifting: stable preferences and the chosen welfare metric over the heating choice set.

## Data And Measurement
- Unit of observation: residential heating choices / household-level technology adoption.
- Market definition: residential heating market.
- Main dependent variable: greenhouse-gas abatement cost.
- Core explanatory variables: technology costs, consumer preferences, carbon tax, and subsidy design.
- Instruments / moments / shocks: not fully extracted from OCR; likely product-market moments and policy scenarios.
- Important sample restrictions: residential heating sector only; OCR capture of the detailed data section was partial.

## Mechanisms, Results, And Counterfactuals
- Baseline result: welfare-based abatement costs are generally higher than technical equipment costs.
- Mechanism evidence: household welfare and behavioral distortions matter for the cost curve.
- Heterogeneity evidence: if households maximize utility, carbon taxes are welfare-efficient; with misperceptions, subsidies can have lower marginal abatement costs.
- Welfare or counterfactual result: policy ranking depends on behavioral assumptions, not just engineering costs.
- Limits the authors admit: the curve is micro-founded but still depends on model specification and the policy scenario set.

## Writing Memory
- Introduction move sequence: engineering benchmark -> welfare critique -> micro approach -> policy ranking.
- Section order: background, model, data, estimation, cost curves, policy comparison, conclusion.
- Where the paper turns from setup to payoff: when the welfare-based curve overtakes the technical-cost benchmark.
- How tables/figures are used to move the argument: cost-curve figures and policy-comparison tables likely drive the result; OCR clearly supported the headline conclusions.
- Best framing sentence pattern: "A technical cost curve is not the same as a welfare cost curve."
- Best transition pattern: move from engineering cost to household welfare.
- Best contribution sentence pattern: "We build a microeconomic abatement curve rather than a purely technical one."
- Best limitation or implication move: "Behavioral assumptions can reverse the ranking of carbon tax and subsidy instruments."
- Durable economics-writing principle: policy cost curves should be built on the welfare metric that policy actually cares about.
- Durable structural-model principle: consumer misperceptions can make a subsidy cheaper at the margin than a carbon tax.
- Reusable empirical design idea: translate technology adoption into abatement cost curves using household welfare.
- Follow-up paper to pair with this one: a micro-welfare study of residential electrification or heat-pump adoption.
- 把模型估计直接连到政策反事实，而不是只停留在弹性或系数。
- 在模型前先铺设数据与制度背景，让后面的结构设定看起来是被场景逼出来的。
- 以后如果要调用这篇文献，不要只记结论，优先调用它的故事推进顺序、模型嵌入位置、以及政策反事实是如何从模型里走出来的。
- 如果后续需要更细的公式级回忆，可以直接回到对应 OCR JSON 的 equation chunks 与 model/estimation section excerpt。

## Evidence Anchors
- intro: page 5 | heating market – a microeconomic approach Caroline Dieckh¨onera,∗∗, Harald Heckinga,∗∗ aInstitute of Energy Economics at the University of Cologne (EWI), Vogelsanger Str. 321, 50827 Cologne, German...
- data: page 9 | rent bottom-up models and models to analyze residential energy consumption, i.e. mainly technology-based energy demand modeling approaches. These bottom-up models are based on extensive disaggregat...
- model: page 6 | costs. There are microeconomic analyses that investigate the impact of environmental policies: Tra (2010) evaluates the beneﬁts of air quality improvements in a discrete choice locational equilibri...
- results: page 5 | abatement cost curves of the residential heating sector. By accounting for household behavior, we ﬁnd that welfare-based abatement costs are generally higher than pure technical equipment costs. Ou...
- conclusion: page 10 | would be obtained under an allowance market that developed under a cap and trade system. They come to the conclusion that these marginal abatement costs are not closely related to the marginal welf...

## Reuse Notes
- Use this card when deciding whether a structural model is needed, what endogenous object must be recovered, and which counterfactual or welfare question is actually identified.
- Reopen the full paper memory or fulltext only when equation-level structure, instruments, or moment conditions matter.

## Summary
- The paper builds greenhouse-gas abatement cost curves for the residential heating market using a microeconomic approach. Its key message is that welfare-based abatement costs are generally higher than simple engineering equipment costs.
