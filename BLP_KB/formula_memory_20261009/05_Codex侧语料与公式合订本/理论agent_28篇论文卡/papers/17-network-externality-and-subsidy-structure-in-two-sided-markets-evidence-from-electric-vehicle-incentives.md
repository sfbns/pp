# Structural Model Stable Card: Network Externality and Subsidy Structure in Two-Sided Markets: Evidence from Electric Vehicle Incentives

## Identity
- domain: `structural_models`
- internal_card_id: `structural::F8UTG3XW::core`
- rank: `17`
- item_key: `F8UTG3XW`
- classification: `canonical BLP demand-supply`
- classification_note: Canonical differentiated-product demand and supply system with welfare or counterfactual use.
- journal: `American Economic Journal: Economic Policy`
- date: `2021-00-00 2021`
- authors: Katalin Springel
- internal_card_path: `D:\codex\economics_theory_agent_complete_gpt55_xhigh\kb\03_structural_models\blp_structural_corpus\papers\17-network-externality-and-subsidy-structure-in-two-sided-markets-evidence-from-electric-vehicle-incentives.md`
- source_paper_memory_path: `D:\codex\blp_structural_memory_2026-04-18\memories\papers\17_f8utg3xw.md`
- source_paper_json_path: `D:\codex\blp_structural_memory_2026-04-18\memories\json\17_f8utg3xw.json`
- source_master_memory_path: `D:\codex\blp_structural_memory_2026-04-18\memories\blp_structural_enhanced_master_memory.md`

## Citation Memory
- reference: Springel, K. (2021). Network Externality and Subsidy Structure in Two-Sided Markets: Evidence from Electric Vehicle Incentives. American Economic Journal: Economic Policy. https://doi.org/10.1257/pol.20190131
- parenthetical: (Springel, 2021)
- narrative: Springel (2021)

## Story Logic
- The paper asks whether, in the EV market viewed as a two-sided market, one dollar of subsidy should go to car buyers or to charging stations.
- Its answer is no: subsidy allocation is not neutral once buyer demand and charging-station entry are linked through network externalities.
- Using Norway registry data and a structural model of vehicle choice plus station entry, the paper shows that station subsidies are more effective at low spending levels, but that this ranking can reverse as spending rises because station-side returns taper off faster.
- Real-world puzzle: governments often subsidize both EV purchases and charging infrastructure, but policy debates usually compare totals rather than the allocation across sides.
- Why this matters: in a two-sided market the same budget can generate different adoption outcomes depending on which side gets the subsidy.
- What existing theory gives: price structure is non-neutral in two-sided markets, and EV adoption is shaped by charging-network externalities.
- What is still missing: paper-level empirical evidence on how subsidy allocation works once flexible substitution in vehicle demand and charging-station entry are jointly modeled.
- The paper's move: combine a two-sided market perspective with an empirically estimated structural model of EV demand and station entry in Norway.
- Main payoff: the policy ranking depends on the level of spending and on the strength of demand-side and infrastructure-side primitives, not just on the headline budget.

## Structural Core
- Research design type: structural two-sided market estimation with counterfactual policy simulations.
- Structural core: a demand system for vehicle choice is linked to a charging-station entry equation so EV demand and infrastructure evolve through indirect network effects.
- Choice objects: consumers choose among vehicles with flexible substitution patterns; station providers choose whether to enter given expected EV demand and subsidies.
- Endogeneity problem: EV subsidies, charging infrastructure, and EV adoption are jointly determined.
- Identification logic: use large-scale Norwegian registry data, observed subsidy variation, and the joint demand-entry structure to back out demand and entry primitives relevant for counterfactuals.
- Heavy-lifting assumptions: network effects operate through charging availability, the estimated demand system captures substitution patterns well enough for out-of-sample policy simulations, and entry responds to market-side profitability.

## Data And Measurement
- Market setting: Norway, one of the world's most important EV adoption environments during the sample period.
- Main data: large-scale vehicle registry data, charging-station information, and policy/subsidy measures.
- Core outcome variables: EV purchases or sales, charging-station entry, and policy spending by subsidy type.
- Key explanatory variables: buyer-side EV price subsidies, station-side subsidies, and charging availability.
- Measurement goal: recover both the direct effect of subsidies and the indirect network effect created when station expansion feeds back into EV demand.

## Mechanisms, Results, And Counterfactuals
- Descriptive finding: EV purchases are positively related to both consumer price subsidies and charging-station subsidies.
- Baseline structural result: the model estimates both vehicle demand and charging-station entry, then uses them to compare buyer-side and station-side subsidy allocations.
- Core policy result: at relatively low spending levels, station subsidies generate more additional EV purchases than buyer subsidies.
- Quantitative illustration from the paper: 100 million NOK spent on station subsidies yields about 835 additional EV purchases, while the same amount spent on buyer subsidies yields about 387 additional EV purchases relative to no-subsidy counterfactuals.
- Mechanism: station subsidies relax the charging-network bottleneck and amplify adoption through indirect network effects.
- Nonlinearity: the advantage of station subsidies diminishes faster as spending rises, so subsidy-ranking can reverse at higher spending levels.

## Writing Memory
- Introduction move sequence: policy puzzle -> two-sided market intuition -> empirical gap -> Norway setting -> headline counterfactual result.
- Section order: introduction -> industry and policy background -> data -> empirical framework -> results -> policy counterfactuals -> conclusion.
- The paper turns from setup to payoff when it states that the same subsidy budget may have different impacts depending on which side receives it.
- Tables and figures are used to connect descriptive subsidy-adoption patterns to the structural counterfactuals, especially the budget-to-adoption comparisons.
- Best framing move: ask not only whether subsidies work, but whether the allocation of subsidies across market sides is itself a first-order policy choice.
- Best transition move: move from network externalities as intuition to a structural model that quantifies policy non-neutrality.
- Best contribution template: existing work shows the market has indirect network effects; we show that those effects make subsidy allocation non-neutral and quantify the ranking.
- Best interpretation habit: report where the policy ranking holds, then immediately note where it may reverse as the market matures or spending rises.
- Durable structural-model lesson: in a networked adoption market, the relevant counterfactual is often not more subsidy versus less subsidy, but who receives the subsidy.
- Durable writing lesson: the paper earns the right to use a structural model by making the policy-ranking question explicit before estimation.
- Reuse rule: when citing this paper later, pair its headline result with the qualifier that station-side superiority is strongest at lower spending levels and weakens as infrastructure saturation rises.
- Citation-ready short takeaway: in EV two-sided markets, subsidy allocation is non-neutral because infrastructure support and buyer incentives operate through different feedback loops.
- 典型写法是先讲现实难题，再说明 reduced-form 不够，于是转向结构模型来回答替代、均衡与福利问题。
- 以后如果要调用这篇文献，不要只记结论，优先调用它的故事推进顺序、模型嵌入位置、以及政策反事实是如何从模型里走出来的。
- 如果后续需要更细的公式级回忆，可以直接回到对应 OCR JSON 的 equation chunks 与 model/estimation section excerpt。

## Evidence Anchors
- intro: page 4 | Abstract Essays in Industrial Organization and Environmental Economics by Katalin Springel Doctor of Philosophy in Economics University of California, Berkeley Professor Benjamin Handel, Chair This...
- data: page 4 | work externalities to determine which side of the market is more efficient to subsidize depending on key vehicle demand and charging station supply primitives. I use new, large-scale vehicle regist...
- model: page 4 | n this work, I consider whether this non-neutrality in the price allocation carries over to the case of subsidies (or taxes) in two-sided markets. Specifically, I develop a stylistic two-sided mark...
- results: page 7 | in Two-Sided Markets: Evidence from text Electric Vehicle Incentives 32 text 2.1 Introduction 32 text 2.2 Industry and Policy Background 37 text 2.3 Data . 40 text 2.4 Empirical Framework 43 text 2...
- conclusion: page 7 | text 1 It is not Easy Being ‘Green’: Subsidy Non-Neutrality in Two-Sided Markets 1 text 1.1 Introduction 1 text 1.2 Literature Review 2 text 1.3 Modeling Framework 4 text 1.4 Simulations 10 text 1....

## Reuse Notes
- Use this card when deciding whether a structural model is needed, what endogenous object must be recovered, and which counterfactual or welfare question is actually identified.
- Reopen the full paper memory or fulltext only when equation-level structure, instruments, or moment conditions matter.

## Summary
- The paper asks whether, in the EV market viewed as a two-sided market, one dollar of subsidy should go to car buyers or to charging stations. Its answer is no: subsidy allocation is not neutral once buyer demand and charging-station entry are linked through network externalities.
