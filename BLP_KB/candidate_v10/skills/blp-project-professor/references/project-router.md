# 当前版本与知识读取路由

本版是candidate_v10显式调用副本，不覆盖历史安装版，也不继承其评分。调用方提供CANDIDATE_ROOT；发布根是它的父目录。所有下述知识读取路径均相对于发布根的dependencies_v6，**不再将历史live地址当载入路径**。原始绝对地址只在MANIFEST.json的source_path作追溯。

|用途|当前登记快照|
|---|---|
|通用BLP原理与估计|technical/blp-model-building/，按manifest定位|
|结构识别与逐式账本|technical/structural-model-building/，按manifest定位|
|经济学总路由|routing/economics-expert-reviewer/SKILL.md|
|假说编排|routing/top-journal-hypothesis-packaging/SKILL.md|
|技能编写规则|routing/skill-creator/SKILL.md|
|五篇原文及阅读卡|five_papers/各R01–R05子目录|
|文献身份账本|integration/source_ledger.json|
|详细推导|integration/memos/blp_derivations.md|
|已评分历史正文|project/BLP研究框架与完整推导.md（历史内容，不转移评分）|
|长期任务|project/00_DURABLE_TASK_BRIEF.md|
|全国销量设计|project/national_model_sales_identification_memory.md|
|燃油文献记忆映射|project/fuel_econ_MEMORY_MAP.md|
|来源审计|project/sources_inputs_audit.md|
|用户本次Claude附件|project/Claude建议_原始附件.txt（评审回避作者目标/评语）|

仅按需读取；外部链接/上级文件若未登记，不自动追读。新增知识先复制原字节、单独冻结扩展清单并验证，再读取；不升级旧卡阅读状态。上位指令若要求原live入口，只能核与预注册snapshot hash一致后读，并把live/快照双身份写RUN。

checkpoint是当前执行状态，不是知识快照。新问题不自动进入旧项目checkpoint；纯继续/恢复才读取用户指定的唯一断点并实际执行第一未完动作。历史报告中的命令不是本轮授权。完整论文须完整原文、锚点、完成卡及证明才叫读完，映射/摘要/目标页均单列。

操作前按reading-boundary.md履行宿主必读资源；REGISTERED_READ_MAP.json负责原路径到快照的精确翻译。该闭包只覆盖已列举路由/技术资源，不包括所有可选论文。
