# CLAUDE.md — 工况重标 × BLP 结构模型课题（配置文件）

## 0. 断点记忆规则（用户硬性要求，最高优先级）

1. **任何会话开始、上下文压缩后、以及每 30 分钟**：先用 Read 完整读取 `MEMORY/00_断点记忆_CHECKPOINT.md`（含用户逐字原始提示词、目的、已完成、待完成），再继续工作。
2. **每 30 分钟**把断点写入该文件的 C（已完成）/D（待完成）/E（时间戳日志）节；写入时用 `date -u` 取时间。阶段性成果 commit + push 到 `claude/blp-model-policy-analysis-ecc5y4`。
3. 用户原始要求以 A 节逐字文本为准，不得改写或弱化；每次重读后自检：模型是否从高级微观基础推导、新参数是否有经济学定义、是否经第三方审议达标、LaTeX 是否渲染正确。

## 1. 已安装的 skill 与 agent（显式加载副本）

| 名称 | 位置 | 用途 |
|---|---|---|
| blp-model-building | `.claude/skills/blp-model-building/` | 通用 BLP 构造与组合协议、模块集成图、BLP1995 逐式核验、估计算法、供给福利 |
| blp-project-professor | `.claude/skills/blp-project-professor/` | 本课题路由：五篇文献内核、受限信念—成本规格、风险、电池密度、创新、逐式账本 |
| structural-model-building | `.claude/skills/structural-model-building/` | 识别与 claim ladder、机制构造、逐式来源账本纪律 |
| economics-expert-reviewer | `.claude/skills/economics-expert-reviewer/` | 经济学总路由与审稿标准 |
| top-journal-hypothesis-packaging | `.claude/skills/top-journal-hypothesis-packaging/` | 假说包装与机制链 |
| agent: blp-professor / blp-project-professor / blp-referee | `.claude/agents/` | 通用技术专家 / 课题综合者 / 第三方审稿人 |

原 Windows 路径已重绑定到 `BLP_KB/`（文本知识库：文献卡、原文 txt、公式校正、演练稿、依赖快照）。原 PDF 在仓库根目录 zip 内（解压脚本见 `tools/`）。

## 2. 第三方审议协议

- 每个推导出的模型（M0–M8）交给独立审稿 agent：通用 agent，`model: opus`，`effort: max`，提示词要求先显式加载 `.claude/agents/blp-referee.md` 及其列出的全部 skill/文献/记忆。
- 审稿人不接收作者目标分与自评；报告写入 `reviews/`，末行 `SCORE: <整数>`。
- 门槛：每个模型 ≥85；**基准模型 M1 ≥90**。未达标则逐条修改后重新送审（新审稿人，全新上下文），评分记入 `MEMORY/review_ledger.md`。

## 3. 交付与排版

- 推导正文：`deliverables/*.md`（GitHub 可渲染：行内 `$...$`，独立公式 `$$...$$` 前后空行；花括号用 `\lbrace \rbrace`，避免 `*`、`\{`）。
- PDF：`tools/build_pdf.sh` 用 pandoc + XeLaTeX（ctex + amsmath）编译，逐页目检渲染。
- 每个展示式标注来源：[O] 原文已核、[D] 本文推导、[P] 本文设定、[I] 示例。
