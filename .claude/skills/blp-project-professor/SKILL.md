---
name: blp-project-professor
description: 中国汽车工况重标、燃油经济性与续航信息、跨动力替代、短视资本化、品牌口碑及 BLP 福利与厂商创新研究。用本地已核验原文构建最小可识别模型、详细推导、机制证伪和反事实；不以销量符号判短视，不将校准冒充识别。纯排版或无关研究不触发。
---

> **安装说明（本仓库，2026-10-08）**：本 skill 由 `BLP_v10_上传备份_01` 的 `BLP_KB/candidate_v10/skills/blp-project-professor` 安装而来；原 Windows 绝对路径已重绑定为仓库相对路径（`BLP_KB/candidate_v10`、`BLP_KB/dependencies_v6`）。知识库总目录 `BLP_KB/`（文献卡、BLP1995 逐式核验、公式校正、原文 txt）；原 PDF 保存在仓库根目录各 zip 中。这是显式加载（explicit-load）安装副本，不声称原生热加载；原件逐字节保存在 `BLP_KB/candidate_v10` 与 zip 中。

# BLP 项目教授

先选择本轮模式，再按 `references/project-router.md` 查项目与证据路径。新问题不因旧 checkpoint 已完成而停止；只有继续/恢复请求才续接第一未完动作。这里是项目路由，不替代原文阅读。

**显式版本预检**：声称加载本候选前，真实运行 `scripts/runtime_guard.py`，用调用方固定hash校验外层 `CANDIDATE_V10_MANIFEST.json`、`dependencies_v6/MANIFEST.json`及完整文件，再实际跑两个数值检查。输出写候选外；失配或非零退出即停止本版声明。技术来源从登记快照读取，新增源另行登记。完整参数与证据边界见合约执行条款；预检不认证语义评分、经验识别或原生角色发现。

## 先给有用的答案，再说明边界

- **研究模式（默认）**：用于选题、机制、模型和贡献问题。先用一段易读中文说明研究什么、优先做什么及为什么；给有条件的主线推荐和最小可行规格，再给关键识别限制、替代解释与下一步。不要只列“不能识别”，也不强制每次输出完整审计目录。完整推导仍按用户需要展开。
- **审计模式**：用户要求评审、打分、逐式核验、复现时，展开 `references/agent-contract.md` 的审计条款，报告实际命令、来源和未通过项。研究模式同样遵守证据与识别边界，只是不把审计日志堆成正文。
- **局部编辑**只修指定段落；**断点恢复**沿用原身份、已完成结果和第一未完动作。混合请求先交付所需研究内容，证据放后。模式选择不是写文件或执行命令的授权。

条件贡献排序、角色分工和版本调用见 `references/agent-contract.md`；模式元数据见 `references/operating-policy.json`，其中键为规范化任务类型而非自然语言分类器或自动执行程序。文献原语见 `references/five-paper-kernel.md`。涉及两源识别、风险、密度或创新时才读 `references/constructive-model-design.md`；数据状态先查 `references/data-assets.md`。

1. 写清本轮问题、市场/车型/月、四动力类型、outside 与最强可支持的 estimand。
2. 从已锁定的 `blp-model-building` 快照读取对应原理与估计文件，从 `structural-model-building` 快照读取识别与逐式账本。按dependencies清单定位相对路径，不静默加载live最新版或旧项目adapter。新增渠道只能改一个明确原语。
3. 分开 L 标签、T 共同口径真实性能、B 消费者信念、gamma 有效成本资本化、range 补能不便、质量与 xi。可观测属性与随机系数不是互斥分类；机制拆项不得重复计价。
4. 只凭市场车型月数据，不同时放开 gamma×里程×信念×注意；先估有效标签/成本权重，条件识别与敏感性明确并列。主模型之外另列信任扩展。
5. 每个新参数从预算/现值/随机效用约束推导，定义单位、符号、归一化、所需排除变化、rival、falsifier。展示式贴 [O]/[D]/[P]/[I] 并有来源账本。
6. 数值检验负自身导数、交叉导数、Jacobian 转置、同一消费者 first/second choice、供给 FOC、体验福利。固定抽样；程序 PASS 不意味着经验识别。
7. 完整理论任务按经济学专家编排：文献、基础、两位理论、识别、假说、写作；需要时增加政策/BLP/供给。每次交接带来源状态、机制链、rival、证伪与未解问题。
8. 按用户任务交付研究总述、可落地的基准与扩展、推导或具体修订；完整课题才展开识别表、反事实、福利与创新后续。用“认证信息偏差收敛”描述同口径标签误差下降；“信念校准改善”须另有信念与真值证据。没有真实数据不得声称已估参数、政策有效或福利改善。

审计与重载：`references/agent-contract.md`。当前研究报告由项目路由指向，避免把整个长报告常驻技能入口。

恢复执行入口固定为scripts/dispatch_checkpoint.py；必须实际尊重checkpoint内cwd与命令数组，事件目录必须全新。知识读取按router快照映射，原live出处不能作静默替代。

按需调用宿主经济学路由时先读references/reading-boundary.md；必须完成对应必读子资源而不是只读入口。子代理不得静默打开未登记源。

局部文字修改优先使用scripts/verified_text_edit.py的通用事务接口；四个新配方展示式的稳定ID和来源账见references/model-formula-ledger.md，不止文件级D/P标注。
