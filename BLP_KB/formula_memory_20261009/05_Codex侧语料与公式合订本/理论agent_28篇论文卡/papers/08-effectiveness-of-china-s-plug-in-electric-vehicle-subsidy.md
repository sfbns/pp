# Structural Model Stable Card: Effectiveness of China's plug-in electric vehicle subsidy

## Identity
- domain: `structural_models`
- internal_card_id: `structural::M5CH8LSF::core`
- rank: `8`
- item_key: `M5CH8LSF`
- classification: `BLP-style differentiated-product demand`
- classification_note: Differentiated-product demand card with BLP-style substitution and heterogeneity as the main reusable object.
- journal: `Energy Economics`
- date: `2020-00-00 2020`
- authors: Tamara L. Sheldon, Rubal Dua
- internal_card_path: `D:\codex\economics_theory_agent_complete_gpt55_xhigh\kb\03_structural_models\blp_structural_corpus\papers\08-effectiveness-of-china-s-plug-in-electric-vehicle-subsidy.md`
- source_paper_memory_path: `D:\codex\blp_structural_memory_2026-04-18\memories\papers\08_m5ch8lsf.md`
- source_paper_json_path: `D:\codex\blp_structural_memory_2026-04-18\memories\json\08_m5ch8lsf.json`
- source_master_memory_path: `D:\codex\blp_structural_memory_2026-04-18\memories\blp_structural_enhanced_master_memory.md`

## Citation Memory
- reference: Sheldon, T. L., & Dua, R. (2020). Effectiveness of China's plug-in electric vehicle subsidy. Energy Economics. https://doi.org/10.1016/j.eneco.2020.104773
- parenthetical: (Sheldon & Dua, 2020)
- narrative: Sheldon and Dua (2020)

## Story Logic
- The paper asks whether China's plug-in electric vehicle subsidy actually improved energy and fuel outcomes.
- It finds that subsidies did improve fleet fuel economy and reduced gasoline use, but the cost per liter saved was high.
- The policy lesson is that subsidy design and targeting matter more than headline generosity.
- Real-world tension or puzzle: China used large subsidies to accelerate electric-vehicle adoption.
- Why the puzzle matters now: expensive subsidies are only justified if they produce large and durable fuel savings.
- What the literature already explains: EV incentives can move adoption, but cost-effectiveness is often unclear.
- What is still missing or weakly identified: a welfare-relevant evaluation of the subsidy's actual fuel-saving payoff.
- The paper's move: estimate how the subsidy changed fleet composition and fuel use.
- Main payoff: the policy worked, but not efficiently enough to justify unqualified scaling.

## Structural Core
- Research design type: policy effectiveness evaluation with counterfactual targeting.
- Structural model class or reduced-form design: market outcome analysis of EV adoption and fleet fuel economy.
- Key equations or choice objects: vehicle choice, subsidy response, and implied fuel consumption.
- Endogeneity problem: subsidy receipt, income, and vehicle choice are jointly determined.
- Identification strategy: compare subsidy exposure across consumer groups and policy regimes.
- What assumptions are doing the heavy lifting: that observed changes can be attributed to subsidy design rather than unrelated market shocks.
- BLP positioning: BLP-style differentiated-product demand
- Evidence hits: random coefficients, mixed logit, discrete choice, welfare, counterfactual, instrument
- Demand side: 需求侧是结构化离散选择/差异化产品需求系统，重点是恢复替代关系与价格弹性。
- Utility construction: 效用写法围绕价格、产品属性、不可观测质量以及个体异质性展开，等价于把平均效用和个体偏离拆开理解。
- Heterogeneity: 异质性是关键层：作者依赖收入、偏好差异、使用场景或消费者类型来刻画不同群体的替代弹性。
- Supply side: 供给侧较轻或被外生化，论文重心更偏需求恢复、替代矩阵和消费者/社会福利。
- Identification / estimation: 识别依赖工具变量、GMM 或其他矩条件来处理价格与产品属性的内生性。
- Counterfactual / welfare: 模型的终点不是参数本身，而是福利、反事实和政策比较。

## Data And Measurement
- Unit of observation: vehicle sales / consumers in the Chinese plug-in EV market.
- Market definition: China's plug-in electric vehicle market.
- Main dependent variable: fleet fuel economy and gasoline consumption.
- Core explanatory variables: subsidy generosity, consumer income, and vehicle attributes.
- Instruments / moments / shocks: not fully extracted from OCR; the policy schedule and income targeting are the main design variation.
- Important sample restrictions: plug-in EVs in China; exact years and segmentation are not fully recoverable from OCR.

## Mechanisms, Results, And Counterfactuals
- Baseline result: subsidies improved fleet fuel economy by about 2%.
- Mechanism evidence: gasoline use fell by about 6.66 billion liters.
- Heterogeneity evidence: subsidies are more cost-effective when reduced for high-income consumers and increased for low-income consumers.
- Welfare or counterfactual result: the paper reports a cost of roughly 1.90 USD per liter saved.
- Limits the authors admit: a blunt subsidy cut would reduce market share sharply, about 21% if halved without offsetting measures.

## Writing Memory
- Introduction move sequence: policy ambition -> cost-effectiveness puzzle -> evaluation design -> headline result.
- Section order: background, empirical strategy, data, results, counterfactuals, conclusion.
- Where the paper turns from setup to payoff: when it converts adoption effects into fuel-saving and cost numbers.
- How tables/figures are used to move the argument: tables likely report fuel economy, gasoline savings, and subgroup targeting; OCR supports the headline figures clearly.
- Best framing sentence pattern: "An incentive can be effective and still be too expensive."
- Best transition pattern: move from adoption to real resource savings.
- Best contribution sentence pattern: "We evaluate the subsidy on both environmental and fiscal grounds."
- Best limitation or implication move: "Targeting matters more than blanket generosity."
- Durable economics-writing principle: policy effectiveness and policy cost-effectiveness are different claims.
- Durable structural-model principle: subsidy design should be evaluated through the consumer groups it actually changes.
- Reusable empirical design idea: pair adoption effects with physical outcome metrics like fuel use.
- Follow-up paper to pair with this one: a targeted EV incentive study with explicit income-based heterogeneity.
- 这篇文章的正文结构大体按下面的顺序推进：
- INTRODUCTION
- Journal Pre-proof
- DATA
- RESULTS & DISCUSSION
- Counterfactual Simulation Analysis
- CONCLUSION
- PII: S0140-9883(20)30113-4
- Reference: ENEECO 104773
- To appear in: Energy Economics
- Received date: 11 November 2019
- Revised date: 12 March 2020
- Accepted date: 23 April 2020
- 在模型章节之前先把市场、制度、样本和关键摩擦讲透，让后面的结构设定像是被场景推出而不是凭空假设。
- 把模型的价值落在反事实与福利，而不是只汇报需求系数和价格弹性。
- 后续回忆这篇论文时，优先调用它的故事梯子、模型嵌入位置、识别策略和反事实落点，而不是只记结论。
- 如果需要公式级别细节，可以直接回到对应 `llm.json` 的 equation chunks 与 model / estimation section。

## Evidence Anchors
- intro: page 2 | t of Economics, University of South Carolina, 1014 Greene St., Columbia, SC 29208, USA bKing Abdullah Petroleum Studies and Research Center (KAPSARC), P.O. Box 88550, Riyadh 11672, Saudi Arabia ABS...
- data: page 4 | the same reduced budget, had zero PEV subsidies been given to high-income consumers and higher subsidies been given to low-income consumers, the PEV market share would have declined by only 8%. DAT...
- model: page 2 | tion and greenhouse gas emissions from the light-duty vehicle sector. In this paper, we explore the impact and cost-effectiveness of the Chinese PEV subsidy program. In particular, a vehicle choice...
- results: page 2 | ated using a large random sample of individual level, model year 2017 Chinese new vehicle purchases. The choice model is then used to predict PEV market share under alternative policies. Simulation...
- conclusion: page 11 | Journal Pre-proof 10 CONCLUSION Despite China‟s ambitious goal to have five million NEVs on the road by 2020, there is uncertainty over the future of the subsidy program. This paper seeks to shed l...

## Reuse Notes
- Use this card when deciding whether a structural model is needed, what endogenous object must be recovered, and which counterfactual or welfare question is actually identified.
- Reopen the full paper memory or fulltext only when equation-level structure, instruments, or moment conditions matter.

## Summary
- The paper asks whether China's plug-in electric vehicle subsidy actually improved energy and fuel outcomes. It finds that subsidies did improve fleet fuel economy and reduced gasoline use, but the cost per liter saved was high.
