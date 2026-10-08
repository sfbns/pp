# Structural Model Stable Card: Consumer response to energy label policies: Evidence from the Brazilian energy label program

## Identity
- domain: `structural_models`
- internal_card_id: `structural::EPWJ8S9T::core`
- rank: `6`
- item_key: `EPWJ8S9T`
- classification: `canonical BLP demand-supply`
- classification_note: Canonical differentiated-product demand and supply system with welfare or counterfactual use.
- journal: `Energy Policy`
- date: `2020-00-00 2020`
- authors: Cristian Huse, Claudio Lucinda, Andre Ribeiro Cardoso
- internal_card_path: `D:\codex\economics_theory_agent_complete_gpt55_xhigh\kb\03_structural_models\blp_structural_corpus\papers\06-consumer-response-to-energy-label-policies-evidence-from-the-brazilian-energy-label-program.md`
- source_paper_memory_path: `D:\codex\blp_structural_memory_2026-04-18\memories\papers\06_epwj8s9t.md`
- source_paper_json_path: `D:\codex\blp_structural_memory_2026-04-18\memories\json\06_epwj8s9t.json`
- source_master_memory_path: `D:\codex\blp_structural_memory_2026-04-18\memories\blp_structural_enhanced_master_memory.md`

## Citation Memory
- reference: Huse, C., Lucinda, C., & Cardoso, A. R. (2020). Consumer response to energy label policies: Evidence from the Brazilian energy label program. Energy Policy. https://doi.org/10.1016/j.enpol.2019.111207
- parenthetical: (Huse et al., 2020)
- narrative: Huse et al. (2020)

## Story Logic
- The paper evaluates a mandatory energy-label policy in the Brazilian refrigerator market.
- Its result is that labels modestly raise valuation for efficiency, but do not fully close the efficiency gap.
- The main lesson is that information policy can move demand, yet equilibrium sorting across products may remain weak.
- Real-world tension or puzzle: energy labels are supposed to help consumers reward efficient products.
- Why the puzzle matters now: if labels barely change choices, disclosure policy may be too weak to deliver energy savings.
- What the literature already explains: labels can affect attention, valuation, and product selection.
- What is still missing or weakly identified: market-level evidence on how a real labeling mandate changes demand.
- The paper's move: study the Brazilian refrigerator label program.
- Main payoff: labels help, but not enough to eliminate the gap or trigger large switching.

## Structural Core
- Research design type: policy evaluation / demand response analysis.
- Structural model class or reduced-form design: market-demand analysis around a labeling intervention.
- Key equations or choice objects: consumer valuation of product energy efficiency and other refrigerator attributes.
- Endogeneity problem: label adoption is policy-driven, but product portfolios and demand responses are endogenous.
- Identification strategy: exploit the policy change to compare consumer response before and after labeling.
- What assumptions are doing the heavy lifting: comparability of demand environments and stable product characteristics apart from the policy.

## Data And Measurement
- Unit of observation: refrigerator products and market choices.
- Market definition: Brazilian refrigerator market.
- Main dependent variable: valuation and choice response to efficiency labels.
- Core explanatory variables: label presence, energy efficiency, and product characteristics.
- Instruments / moments / shocks: the label mandate itself is the key policy shock.
- Important sample restrictions: refrigerator market only; OCR extraction was noisy in some spots, so exact sample design may need verification against the PDF if used in a formal writeup.

## Mechanisms, Results, And Counterfactuals
- Baseline result: mandatory labels modestly increase mean valuation for efficient products.
- Mechanism evidence: information improves product evaluation, but does not create dramatic switching.
- Heterogeneity evidence: the distribution of valuations does not become equalized across products.
- Welfare or counterfactual result: the policy cannot eliminate the energy-efficiency gap on its own.
- Limits the authors admit: the effect size is modest, so labels are not a full substitute for stronger policy.

## Writing Memory
- Introduction move sequence: puzzle -> policy -> market setting -> identification -> result.
- Section order: background, empirical design, data, results, robustness, conclusion.
- Where the paper turns from setup to payoff: once the valuation shift is shown to be modest.
- How tables/figures are used to move the argument: tables likely show pre/post valuation and distributional shifts; OCR was partly noisy, so this is a cautious inference.
- Best framing sentence pattern: "Information policy can improve decisions without fully solving the allocation problem."
- Best transition pattern: move from consumer attention to market sorting.
- Best contribution sentence pattern: "We show that mandatory labels shift valuation, but only modestly."
- Best limitation or implication move: "Labels are useful, but they are not a complete efficiency policy."
- Durable economics-writing principle: policy evaluation should report both mean effects and the remaining gap.
- Durable structural-model principle: information changes demand only if it materially changes valuation or attention.
- Reusable empirical design idea: evaluate mandates by looking at product-market response, not just survey opinions.
- Follow-up paper to pair with this one: another appliance-label or disclosure-policy paper with explicit counterfactual welfare calculations.
- 在模型前先铺设数据与制度背景，让后面的结构设定看起来是被场景逼出来的。
- 以后如果要调用这篇文献，不要只记结论，优先调用它的故事推进顺序、模型嵌入位置、以及政策反事实是如何从模型里走出来的。
- 如果后续需要更细的公式级回忆，可以直接回到对应 OCR JSON 的 equation chunks 与 model/estimation section excerpt。

## Evidence Anchors
- intro: page 1 | switching and heterogeneity in responses. All in all, while the PBE program aimed to both reduce energy consumption and increase energy efficiency, we can only claim robust evidence of the latter....
- data: page 1 | nformation programs Refrigerators A B S T R A C T The PBE program made the adoption of energy labels mandatory in the Brazilian refrigerator market. In this paper, we examine the effects of PBE usi...
- model: page 1 | doption of energy labels mandatory in the Brazilian refrigerator market. In this paper, we examine the effects of PBE using data from a nationally representative sample of households and a structur...
- results: page 1 | on of energy costs by Brazilian consumers. However, the program is unable to eliminate the energy efficiency gap, in that consumers undervalue energy costs both pre-and post-PBE. Moreover, our poli...
- conclusion: page  | 

## Reuse Notes
- Use this card when deciding whether a structural model is needed, what endogenous object must be recovered, and which counterfactual or welfare question is actually identified.
- Reopen the full paper memory or fulltext only when equation-level structure, instruments, or moment conditions matter.

## Summary
- The paper evaluates a mandatory energy-label policy in the Brazilian refrigerator market. Its result is that labels modestly raise valuation for efficiency, but do not fully close the efficiency gap.
