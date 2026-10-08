# Structural Model Stable Card: Better Lucky Than Rich? Welfare Analysis of Automobile Licence Allocations in Beijing and Shanghai

## Identity
- domain: `structural_models`
- internal_card_id: `structural::JDV2EEV6::core`
- rank: `1`
- item_key: `JDV2EEV6`
- classification: `canonical BLP demand-supply`
- classification_note: Canonical differentiated-product demand and supply system with welfare or counterfactual use.
- journal: `The Review of Economic Studies`
- date: `2018-00-00 2018`
- authors: Shanjun Li
- internal_card_path: `D:\codex\economics_theory_agent_complete_gpt55_xhigh\kb\03_structural_models\blp_structural_corpus\papers\01-better-lucky-than-rich-welfare-analysis-of-automobile-licence-allocations-in-beijing-and-shanghai.md`
- source_paper_memory_path: `D:\codex\blp_structural_memory_2026-04-18\memories\papers\01_jdv2eev6.md`
- source_paper_json_path: `D:\codex\blp_structural_memory_2026-04-18\memories\json\01_jdv2eev6.json`
- source_master_memory_path: `D:\codex\blp_structural_memory_2026-04-18\memories\blp_structural_enhanced_master_memory.md`

## Citation Memory
- reference: Li, S. (2018). Better Lucky Than Rich? Welfare Analysis of Automobile Licence Allocations in Beijing and Shanghai. The Review of Economic Studies. https://doi.org/10.1093/restud/rdx067
- parenthetical: (Li, 2018)
- narrative: Li (2018)

## Story Logic
- The paper asks how much welfare is lost when a city restricts car ownership with a lottery rather than a uniform-price auction.
- Its answer is that Beijing's lottery design creates large misallocation costs, even though it lowers some externalities relative to pure market allocation.
- The key takeaway is that "fair" allocation can be much more expensive than it looks once households differ in willingness to pay and usage intensity.
- Real-world tension or puzzle: Beijing and Shanghai both ration car licenses, but they use very different allocation rules.
- Why the puzzle matters now: when quantity controls are unavoidable, the allocation rule itself becomes a major policy lever.
- What the literature already explains: car ownership regulation can reduce congestion and pollution, but not the welfare ranking of allocation mechanisms.
- What is still missing or weakly identified: the welfare comparison between lottery and auction under realistic heterogeneity.
- The paper's move: build a welfare counterfactual for the two systems using the same restricted market.
- Main payoff: the allocation mechanism itself has first-order welfare consequences; quantity control is not enough.

## Structural Core
- Research design type: structural welfare comparison / counterfactual policy analysis.
- Structural model class or reduced-form design: demand-and-allocation framework with observed license rules and market outcomes.
- Key equations or choice objects: household choice over vehicle ownership under a binding license constraint.
- Endogeneity problem: observed ownership mixes reflect both preferences and policy rationing.
- Identification strategy: recover demand/welfare objects from market behavior, then simulate alternative allocation rules.
- What assumptions are doing the heavy lifting: stable preferences and counterfactual policy comparability.

## Data And Measurement
- Unit of observation: households / car-market choices under city-level license regimes.
- Market definition: Beijing versus Shanghai automobile ownership market.
- Main dependent variable: welfare under alternative license allocation rules.
- Core explanatory variables: license availability, household willingness to pay, and policy design.
- Instruments / moments / shocks: not fully extracted from OCR; likely policy-rule variation rather than an external instrument.
- Important sample restrictions: cities under rationing regimes; exact restriction details were not fully recoverable from OCR.

## Mechanisms, Results, And Counterfactuals
- Baseline result: Beijing's lottery generates very large welfare loss; the paper states roughly 30 billion Yuan in 2012 alone.
- Mechanism evidence: the lottery misallocates scarce licenses away from higher-value users.
- Heterogeneity evidence: the welfare ranking depends on how much the license cap binds across households.
- Welfare or counterfactual result: a uniform-price auction would have raised roughly 20 billion Yuan in the cited year.
- Limits the authors admit: the externality-reducing aspect of rationing is real, so the question is not "lottery versus no policy" but "lottery versus better allocation."

## Writing Memory
- Introduction move sequence: puzzle -> policy context -> welfare gap -> mechanism -> quantitative result.
- Section order: policy setting, model, data, estimation, welfare counterfactuals, conclusion.
- Where the paper turns from setup to payoff: once the auction-versus-lottery counterfactual is introduced.
- How tables/figures are used to move the argument: they likely anchor the policy comparison and welfare decomposition; OCR extraction was too noisy to map every table confidently.
- Best framing sentence pattern: "Two cities face the same constraint, but different allocation rules create different welfare outcomes."
- Best transition pattern: move from externality control to misallocation cost.
- Best contribution sentence pattern: "We show that the rule used to allocate scarce licenses matters as much as the cap itself."
- Best limitation or implication move: "The policy is not whether to ration, but how to ration."
- Durable economics-writing principle: always separate the policy instrument from the allocation rule that implements it.
- Durable structural-model principle: welfare comparisons become credible when the counterfactual keeps the same constraint but changes the assignment mechanism.
- Reusable empirical design idea: compare institutions that solve the same scarcity problem with different market mechanisms.
- Follow-up paper to pair with this one: a paper on congestion pricing versus lotteries in the same city.
- 把模型估计直接连到政策反事实，而不是只停留在弹性或系数。
- 以后如果要调用这篇文献，不要只记结论，优先调用它的故事推进顺序、模型嵌入位置、以及政策反事实是如何从模型里走出来的。
- 如果后续需要更细的公式级回忆，可以直接回到对应 OCR JSON 的 equation chunks 与 model/estimation section excerpt。

## Evidence Anchors
- intro: page 1 | ich led to wide discontent due to long delays. The FCC ﬁnally adopted auctions in The editor in charge of this paper was Jerome Adda. 1 Downloaded from https://academic.oup.com/restud/advance-artic...
- data: page 3 | sumers with high WTP tend to have high income. At the same time, high-income households on average buy less fuel-efﬁcient vehicles and drive more than low-income households as household travel surv...
- model: page 3 | hould inform WTP for a licence, the additional cost that consumers have to bear to own a vehicle. To estimate consumer surplus from vehicle ownership, we estimate a random coefﬁcients discrete choi...
- results: page 12 | ssumption that the allocation mechanisms in Shanghai and Beijing are not likely to affect ﬁrms price-setting behavior or local dealer incentives. This assumption should not be a driving factor in o...
- conclusion: page 30 | in the black market in Beijing was about 200,000 Yuan in 2012 even though there is a large legal risk in such transactions. Truncating the maximum WTP to 200,000 Yuan do not qualitatively affect th...

## Reuse Notes
- Use this card when deciding whether a structural model is needed, what endogenous object must be recovered, and which counterfactual or welfare question is actually identified.
- Reopen the full paper memory or fulltext only when equation-level structure, instruments, or moment conditions matter.

## Summary
- The paper asks how much welfare is lost when a city restricts car ownership with a lottery rather than a uniform-price auction. Its answer is that Beijing's lottery design creates large misallocation costs, even though it lowers some externalities relative to pure market alloc...
