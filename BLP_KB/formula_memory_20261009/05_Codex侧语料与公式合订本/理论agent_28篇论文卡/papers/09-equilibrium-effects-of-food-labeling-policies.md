# Structural Model Stable Card: Equilibrium Effects of Food Labeling Policies

## Identity
- domain: `structural_models`
- internal_card_id: `structural::S925QHZD::core`
- rank: `9`
- item_key: `S925QHZD`
- classification: `canonical BLP demand-supply`
- classification_note: Canonical differentiated-product demand and supply system with welfare or counterfactual use.
- journal: `Econometrica`
- date: `2023-00-00 2023`
- authors: Nano Barahona, Cristóbal Otero, Sebastián Otero
- internal_card_path: `D:\codex\economics_theory_agent_complete_gpt55_xhigh\kb\03_structural_models\blp_structural_corpus\papers\09-equilibrium-effects-of-food-labeling-policies.md`
- source_paper_memory_path: `D:\codex\blp_structural_memory_2026-04-18\memories\papers\09_s925qhzd.md`
- source_paper_json_path: `D:\codex\blp_structural_memory_2026-04-18\memories\json\09_s925qhzd.json`
- source_master_memory_path: `D:\codex\blp_structural_memory_2026-04-18\memories\blp_structural_enhanced_master_memory.md`

## Citation Memory
- reference: Barahona, N., Otero, C., & Otero, S. (2023). Equilibrium Effects of Food Labeling Policies. Econometrica. https://doi.org/10.3982/ecta19603
- parenthetical: (Barahona et al., 2023)
- narrative: Barahona et al. (2023)

## Story Logic
- 这份本地文件是主文的补充材料，不是完整主文，因此我把它当作“主模型的稳健性与细化机制”来读。
- 从补充材料能稳定看出的主旨是：食品标签政策不仅影响需求，还会改变产品重配方、价格、markup 和均衡福利。
- 现实问题是，营养标签的目标不是只让消费者“少买一点”，而是让市场在均衡中变得更健康。
- 如果厂商会重配方，单看销量会低估政策影响；如果只看标签可见性，也会漏掉 equilibrium effects。
- 这份补充材料反复围绕“calorie / sugar concentration、reformulation、markups、welfare”做稳健性检查，说明主文的故事重点是均衡而不是简单需求冲击。

## Structural Core
- 主模型是结构化需求-供给框架，消费者效用含有产品营养属性，厂商面对重配方和价格调整。
- 补充材料里尤其强调 taste invariant / reformulation robustness，说明作者担心标签改变了“味道”而不只是显性属性。
- 识别的核心不是单一政策哑变量，而是把标签政策放进需求、供给和重配方同时决定的系统里。
- BLP positioning: canonical BLP demand-supply
- Evidence hits: random coefficients, nested logit, marginal cost, markup, welfare, counterfactual, instrument, gmm
- Demand side: 全文表明作者在做结构化产品需求分析，但 OCR 证据不足以把需求形式精确钉死到某个 logit 变体。
- Utility construction: 模型核心仍然是“价格 + 产品属性 + 未观测质量”决定选择概率，再由市场份额把需求参数识别出来。
- Heterogeneity: 异质性信息没有被 OCR 关键词强烈命中，但从论文主题看，替代关系至少在产品层面而不是代表性消费者层面展开。
- Supply side: 供给侧是显式的：通常包含多产品定价、边际成本恢复、markup 变化和均衡反事实。
- Identification / estimation: 识别依赖工具变量、GMM 或其他矩条件来处理价格与产品属性的内生性。
- Counterfactual / welfare: 模型的终点不是参数本身，而是福利、反事实和政策比较。

## Data And Measurement
- 研究对象是 ready-to-eat cereals，补充材料中多次提到 pre- and post-legislation 的产品分布。
- 关键测量包括 calories、sugar concentration、markups、product counts，以及不同营养分组的需求变化。
- 该文件主要提供附录图表和稳健性，而不是完整主文的数据叙事。

## Mechanisms, Results, And Counterfactuals
- 补充材料显示，低/高卡路里产品的需求变化并不简单地按“越不健康越受打击”排序。
- 结论侧重于：重配方和消费者响应共同决定了均衡结果，单看销量会失真。
- 这类结论的价值在于，把标签政策写成“均衡重组”而不是“需求缩放”。

## Writing Memory
- 这类文章最关键的结构是：主文讲核心故事，补充材料专门处理 taste、样本和参数敏感性。
- 对你最有用的写法是把“均衡结果”放在正文，把“为什么不是别的机制”留给附录。
- 这篇文章适合学的写法是：把政策评估写成“需求、供给、重配方、福利”的链条，而不是单一回归表。
- 另一点是：用补充材料系统处理稳健性，别让正文变成参数争论。
- Durable economics-writing principle: 标签政策应按均衡系统来写，不能只看平均销量。
- Durable empirical idea: 当厂商会重配方时，营养政策的效果必须同时看 demand 和 supply。
- Uncertainty note: this local file is the supplement only, so a few main-paper details are inferred from the appendix structure.
- 这篇文章的正文结构大体按下面的顺序推进：
- Introduction
- Background / Data
- Model
- Estimation
- Results
- Counterfactual / Welfare
- Conclusion
- 把模型的价值落在反事实与福利，而不是只汇报需求系数和价格弹性。
- 后续回忆这篇论文时，优先调用它的故事梯子、模型嵌入位置、识别策略和反事实落点，而不是只记结论。
- 如果需要公式级别细节，可以直接回到对应 `llm.json` 的 equation chunks 与 model / estimation section。

## Evidence Anchors
- intro: page 14 | e taste of products. This assumption simpliﬁes the ﬁrm’s problem of choosing wjt in the absence of regulation, which we use to estimate νj from the ﬁrst-order conditions. This assumption is driven...
- data: page 3 | in sugar and calories as a function of the average prior belief about their nutritional content. In Panel (a), we focus on sugar content. Products in yellow diamonds are products that bunched in th...
- model: page 7 | EQUILIBRIUM EFFECTS OF FOOD LABELING POLICIES 7 APPENDIX C: DEMAND MODEL DISCUSSION C.1. Stockpiling We assume static demand. However, cereal is a storable product, which can lead to dynamic incent...
- results: page 2 | om the demand and supply models presented in Sections 4 and 5. We then run our main counterfactuals and calculate the changes in consumer welfare under the different parameters. We show that our ma...
- conclusion: page  | 

## Reuse Notes
- Use this card when deciding whether a structural model is needed, what endogenous object must be recovered, and which counterfactual or welfare question is actually identified.
- Reopen the full paper memory or fulltext only when equation-level structure, instruments, or moment conditions matter.

## Summary
- 这份本地文件是主文的补充材料，不是完整主文，因此我把它当作“主模型的稳健性与细化机制”来读。 从补充材料能稳定看出的主旨是：食品标签政策不仅影响需求，还会改变产品重配方、价格、markup 和均衡福利。
