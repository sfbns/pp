# Structural Model Stable Card: Fiscal Policy and CO2 Emissions of New Passenger Cars in the EU

## Identity
- domain: `structural_models`
- internal_card_id: `structural::99RBFASI::core`
- rank: `10`
- item_key: `99RBFASI`
- classification: `BLP-adjacent structural policy model`
- classification_note: Policy-oriented structural model that borrows the BLP logic but adapts the state, choice, or market environment.
- journal: `Environmental and Resource Economics`
- date: `2018-00-00 2018`
- authors: Reyer Gerlagh, Inge van den Bijgaart, Hans Nijland, Thomas Michielsen
- internal_card_path: `D:\codex\economics_theory_agent_complete_gpt55_xhigh\kb\03_structural_models\blp_structural_corpus\papers\10-fiscal-policy-and-co2-emissions-of-new-passenger-cars-in-the-eu.md`
- source_paper_memory_path: `D:\codex\blp_structural_memory_2026-04-18\memories\papers\10_99rbfasi.md`
- source_paper_json_path: `D:\codex\blp_structural_memory_2026-04-18\memories\json\10_99rbfasi.json`
- source_master_memory_path: `D:\codex\blp_structural_memory_2026-04-18\memories\blp_structural_enhanced_master_memory.md`

## Citation Memory
- reference: Gerlagh, R., Bijgaart, I. v. d., Nijland, H., & Michielsen, T. (2018). Fiscal Policy and CO2 Emissions of New Passenger Cars in the EU. Environmental and Resource Economics. https://doi.org/10.1007/s10640-016-0067-6
- parenthetical: (Gerlagh et al., 2018)
- narrative: Gerlagh et al. (2018)

## Story Logic
- The paper studies how different fiscal policies change the CO2 intensity of new passenger cars in the EU.
- It finds that registration taxes with stronger CO2 sensitivity reduce emissions intensity, while fuel taxes also push toward more efficient cars.
- Annual road taxes, by contrast, have little or even adverse effect.
- Real-world tension or puzzle: EU countries use several car taxes, but their emissions effects are not the same.
- Why the puzzle matters now: climate policy needs to know which tax margin actually changes vehicle choices.
- What the literature already explains: car taxation should affect efficiency and fuel mix, but evidence is fragmented.
- What is still missing or weakly identified: a comparative estimate across registration, fuel, and annual taxes.
- The paper's move: evaluate those fiscal instruments in a common EU car-market framework.
- Main payoff: not all car taxes are equal; some are much better aligned with CO2 goals.

## Structural Core
- Research design type: comparative policy evaluation with market-level CO2 outcomes.
- Structural model class or reduced-form design: vehicle-choice framework linking taxes to vehicle attributes.
- Key equations or choice objects: new-car choice over emissions, fuel type, and other specifications.
- Endogeneity problem: tax regimes co-evolve with consumer demand and policy goals.
- Identification strategy: exploit cross-country and policy variation in fiscal instruments.
- What assumptions are doing the heavy lifting: comparability across markets and stable response to tax incentives.
- BLP positioning: BLP-adjacent structural policy model
- Evidence hits: bertrand, welfare, instrument
- Demand side: 全文表明作者在做结构化产品需求分析，但 OCR 证据不足以把需求形式精确钉死到某个 logit 变体。
- Utility construction: 效用写法围绕价格、产品属性、不可观测质量以及个体异质性展开，等价于把平均效用和个体偏离拆开理解。
- Heterogeneity: 异质性是关键层：作者依赖收入、偏好差异、使用场景或消费者类型来刻画不同群体的替代弹性。
- Supply side: 供给侧是显式的：通常包含多产品定价、边际成本恢复、markup 变化和均衡反事实。
- Identification / estimation: 识别依赖工具变量、GMM 或其他矩条件来处理价格与产品属性的内生性。
- Counterfactual / welfare: 论文明确把模型用于税收、补贴、禁令、标签或进入政策的反事实分析。

## Data And Measurement
- Unit of observation: new passenger cars.
- Market definition: EU passenger-car markets.
- Main dependent variable: CO2 intensity of the average new car.
- Core explanatory variables: registration taxes, fuel taxes, and annual road taxes.
- Instruments / moments / shocks: policy variation across countries and time.
- Important sample restrictions: new cars in the EU; precise country coverage is in the paper, but the OCR read was clear on the main design.

## Mechanisms, Results, And Counterfactuals
- Baseline result: higher CO2-sensitivity of registration taxes reduces CO2 intensity by about 1.3%.
- Mechanism evidence: the same policy increases diesel share by about 6.5 percentage points.
- Heterogeneity evidence: higher fuel taxes also induce more efficient cars, while higher diesel fuel taxes reduce diesel share.
- Welfare or counterfactual result: annual road taxes show little or negative effect on CO2 intensity.
- Limits the authors admit: policy effects differ by tax type, so no single fiscal instrument is dominant in every context.

## Writing Memory
- Introduction move sequence: emissions problem -> tax toolkit -> comparison gap -> result summary.
- Section order: policy context, empirical design, results, robustness, conclusion.
- Where the paper turns from setup to payoff: when registration taxes are shown to beat annual taxes on CO2 alignment.
- How tables/figures are used to move the argument: results tables and policy-comparison figures likely do the heavy lifting; OCR was clear on the headline estimates.
- Best framing sentence pattern: "The question is not whether taxes matter, but which tax margin matters."
- Best transition pattern: move from policy inventory to instrument comparison.
- Best contribution sentence pattern: "We compare the emissions effects of the main fiscal tools in one market."
- Best limitation or implication move: "A tax instrument is only as good as the margin it actually changes."
- Durable economics-writing principle: policy menus should be evaluated instrument by instrument, not as a single lump.
- Durable structural-model principle: CO2 outcomes are mediated by substitution toward fuel type and vehicle efficiency.
- Reusable empirical design idea: compare policy types that target the same market but different choice margins.
- Follow-up paper to pair with this one: a cross-country comparison of registration taxes versus feebates on vehicle emissions.
- 这篇文章的正文结构大体按下面的顺序推进：
- 1 Introduction
- 1 See European Commission (2016).
- 4 Data
- 3 Model
- 6 Results
- 7 Discussion
- Fiscal Policy and \mathbf { C O } _ { 2 } Emissions of New Passenger Cars in the EU
- Reyer Gerlagh1 Inge van den Bijgaart1,4 Hans Nijland2 Thomas Michielsen3
- Accepted: 23 September 2016
- CrossMark
- 1 Tilburg University, Tilburg, Netherlands
- 2 PBL Netherlands Environmental Assessment Agency, The Hague, Netherlands
- 在模型章节之前先把市场、制度、样本和关键摩擦讲透，让后面的结构设定像是被场景推出而不是凭空假设。
- 正文常见顺序是“模型设定 -> 识别/估计 -> 结果 -> 政策反事实”，避免一上来就堆公式。
- 后续回忆这篇论文时，优先调用它的故事梯子、模型嵌入位置、识别策略和反事实落点，而不是只记结论。
- 如果需要公式级别细节，可以直接回到对应 `llm.json` 的 equation chunks 与 model / estimation section。

## Evidence Anchors
- intro: page 1 | the EU Reyer Gerlagh1 · Inge van den Bijgaart1,4 · Hans Nijland2 · Thomas Michielsen3 Accepted: 23 September 2016 © The Author(s) 2016. This article is published with open access at Springerlink.co...
- data: page 1 | model that generates predictions regarding the effect of ﬁscal policies on average CO2 emissions of new cars, and then test the model empirically. Our empirical strategy combines a diverse series o...
- model: page 1 | s article is published with open access at Springerlink.com Abstract To what extent have national ﬁscal policies contributed to the decarbonisation of newly sold passenger cars? We construct a simp...
- results: page 3 | existing literature: ﬁrst, unlike most studies, our study deals with the effects of car taxes in multiple countries, thus controlling for year-speciﬁc effects. This makes it easier to generalize ou...
- conclusion: page 20 | emissions for the diesel ﬂeet but also induce substi- tution of petrol cars for diesel cars. The ﬁnding is consistent with Ryan et al. (2009), but a subtle and important distinction from the genera...

## Reuse Notes
- Use this card when deciding whether a structural model is needed, what endogenous object must be recovered, and which counterfactual or welfare question is actually identified.
- Reopen the full paper memory or fulltext only when equation-level structure, instruments, or moment conditions matter.

## Summary
- The paper studies how different fiscal policies change the CO2 intensity of new passenger cars in the EU. It finds that registration taxes with stronger CO2 sensitivity reduce emissions intensity, while fuel taxes also push toward more efficient cars.
