---
name: blp-model-building
description: 从经济问题构造通用 BLP 需求或需求—供给系统；按原语组合人口与第二选择微观矩、成本资本化/信念、收入效应、RCNL、内生属性、网络和动态模块，逐项审查识别、退化、数值实现与反事实边界。不是汽车工况项目模板。
---

> **安装说明（本仓库，2026-10-08）**：本 skill 由 `BLP_v10_上传备份_01` 的 `BLP_KB/candidate_v10/skills/blp-model-building` 安装而来；原 Windows 绝对路径已重绑定为仓库相对路径（`BLP_KB/candidate_v10`、`BLP_KB/dependencies_v6`）。知识库总目录 `BLP_KB/`（文献卡、BLP1995 逐式核验、公式校正、原文 txt）；原 PDF 保存在仓库根目录各 zip 中。这是显式加载（explicit-load）安装副本，不声称原生热加载；原件逐字节保存在 `BLP_KB/candidate_v10` 与 zip 中。

# 通用 BLP 模型构造

先定义要回答的替代、均衡或福利对象，再选最小充分模型。BLP 需求侧不强制估供给；资本化不等于短视，信念权重不等于注意/信任，网络条件需求不等于网络均衡，干中学不等于专利创新。

## 三个工作文件

1. [模块集成图](references/模块集成图.md)：按问题选模块、依赖顺序、文献接口与禁配条件。
2. [构造与组合协议](references/构造与组合协议.md)：实际推导、观测映射、矩、算法、反事实、退化和失败后的降级；也是 `blp_professor` 的执行合约。
3. [文献模块来源账本](references/文献模块来源账本.json)：每个文献节点的固定快照路径、SHA256、真实行锚、来源状态及可用范围。先查节点，再打开相应内容；目录/题名命中不算阅读。

## 最短调用

输入不全时只补问影响模型选择的未知量，其余用 `TARGET / MARKET / OUTSIDE / POLICY / STATE` 槽位，先给条件模型。

按顺序交付：**经济问题 → 原语与时序 → 最小版方程 → 参数—变异—矩 → 升级版及不兼容项 → 算法与可运行检验 → 反事实不变量 → 未识别对象**。窄问题只交付相关切片，不填满所有模块；多机制问题必须给接口推导，不能逐篇列文献后把公式并排相加。

## 固定来源与运行边界

本轮冻结评测的候选根 `BLP_KB/candidate_v10`；依赖根 `BLP_KB/dependencies_v6`。本轮仅从依赖根的 `MANIFEST.json` 和 `REGISTERED_READ_MAP.json` 精确定位已登记来源。旧参考里的外部绝对路径仅是 provenance，不能随链接静默加载。

实际候选运行复用候选根 `scripts/runtime_guard.py`，由外层控制器传入最终冻结的候选/依赖 manifest 身份，不自行猜参数或伪造冻结值。仅解析 TOML、阅读 skill 或跑合成脚本不等于原生角色已发现、估计已完成或识别已成立。本轮新来源须先另行授权、登记和冻结；当前缺源就限定主张，不浏览补洞。这是冻结评测约束，不是永久禁止检索：后续实际研究若用户已授权文献扩展，可在该范围内只读检索Zotero/本地/官方原文，无需逐文件重复询问；新增源先登记哈希、版本与来源状态，完成必要核验后使用，不改本轮冻结依赖，也不因取得全文声称读完。

通用请求不得自动加载工况课题适配器或 `project/*`。明确点名项目才由项目入口接管；通用模型的市场、产品、机制和参数不继承项目预设。

## 附：技术底座（已随安装复制）

`references/technical/` = 依赖快照 `technical/blp-model-building/references`（BLP1995 逐式核验 `blp1995_verified_equations.md`、微观基础 `micro_foundations.md`、估计算法 `estimation_algorithm_and_code.md`、识别与微观矩、供给福利反事实、改造谱系、工况项目 `project_china_driving_cycle.md`）；`scripts/` = 自检脚本（`blp_selftest.py` 等）与 `candidate_v10/scripts`。演练稿：`BLP_KB/formula_memory_20261009/01_演练稿/A_主版本_理论agent_kb_foundations/`。
