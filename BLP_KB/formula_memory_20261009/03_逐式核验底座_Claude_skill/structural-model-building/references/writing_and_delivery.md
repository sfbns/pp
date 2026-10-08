# 结构论文的写法与交付

蒸馏自 28 篇 BLP 语料 + 40 篇深读包的写作综合稿（`D:\codex\research-memory\deep-reading\blp40s_20260403\synthesis_structural_writing_memory.md`、`D:\codex\blp_fulltext_memory_2026-04-17\writing_synthesis.md`）。

## 1. 三条故事阶梯（顶刊反复出现）

**A 政策设计阶梯**：政策工具已在用 → 现有争论把它当成显然的、一维的 → 真正缺的是它到底移动了哪个市场边际（需求、替代、创新、基础设施、福利归宿）→ 设计能隔离该边际 → 收益不是"政策有没有用"，而是"哪种设计占优、为什么"。
→ 写政策论文围绕**工具比较**，不要围绕泛泛的褒贬；把**有效性、成本有效性、福利排序**三件事分开。

**B 均衡/反馈阶梯**：结果与其他市场对象联合决定 → reduced-form 漏掉反馈 → 显式写出均衡对象 → 识别聚焦在阻断朴素推断的那个内生边际 → 只有联立系统被估计/校准后反事实才可信。
→ 价格、属性、基础设施或进入会内生反应时，**第一段就说**；报任何弹性或政策效应之前先讲清市场系统。

**C 替代/替换阶梯**：政策或技术改变的是选择集，不只是平均需求 → 关键经验对象是替代品、第二选择、替换边际 → 福利取决于谁被挤掉 → 因此直接估弹性、考虑集或替换模式。
→ 把 **"X 到底替代了谁"当成核心经济问题**，不是脚注。耐用品要把未来运营成本、质量与 outside option 写明。

## 2. 贡献句模板

> existing work misses margin **M**; design **D** identifies **M**; that changes policy conclusion **P**.

不要只写"这个题目重要"。三个动作缺一不可：① 经验空白（现有文献测不好什么）；② 设计/方法动作（什么新估计、工具或数据组合让它可测）；③ 政策或福利收益（测出来改变了哪个实际决定或排序）。

**顶刊几乎从不把"我们用了结构模型"当卖点。** 卖点是"这个模型让我回答了别的方法答不了的问题"。模型章节要回答两个问题：为什么这个模型适合这个市场；为什么它能支撑后面的反事实。

## 3. 章节序与排序纪律

标准序：Intro（谜题与利害）→ 前人做对了什么 → 前人漏了什么 → 设计/模型预告 → 数据与制度背景 → 识别或模型 → 基准结果 → 机制/异质性 → 福利/反事实/设计比较 → 结论（带条件的政策含义）。

- **数据与制度放在模型之前**，作用不是铺陈素材，而是为模型设定、市场定义和识别假设做**前置正当化**。
- **baseline 在 mechanism 之前，mechanism 在 welfare 之前，welfare 在规范主张之前。**
- 结果章先讲机制与弹性，再讲福利与政策含义；**福利是全文终点，不是附录式补充**。
- 文献综述形式短、功能重：按"缺失的边际"分组，不按作者时间排；引用同时做三件事——定位本文、验证方法谱系、说明现有假设为何太窄。空白句必须带 because。

## 4. 可复用句式

**框架**："The relevant question is not whether the policy moves outcomes, but which margin it moves and at what welfare cost." · "Average effects are insufficient because the policy changes the equilibrium allocation across products, consumers, or technologies." · "The key empirical object is the substitute/replacement margin."

**贡献**："We show that once X is modeled endogenously, the policy ranking changes." · "We quantify a parameter that policy discussions typically take as given." · "Our contribution is to connect design D to welfare object W in an observed market."

**过渡**："Having established the institutional margin, we now model the equilibrium response." · "The identifying variation comes from …" · "This distinction matters because …"

**局限**："The policy ranking is conditional on the estimated strength of …" · "The gain in realism comes with computational cost." · "These results should be interpreted as short-run equilibrium effects."

## 5. 交付顺序（做咨询/给用户报告时）

1. 推荐的研究问题与 estimand（把总效应、组内重配、跨组替代、机制、均衡反馈、福利**分开写**）
2. 制度时点与精确处理状态
3. 数据单位、市场、产品、成交价、市场规模、outside
4. 暴露/处理变量的构造与共同支持审计
5. 受限结构基准
6. 主模型
7. 逐参数识别与微观矩
8. 边际效应、替代与选择边界
9. 供给侧（先只做重新定价）
10. 机制与异质性
11. 反事实体系（登记状态向量）
12. 福利（分轨）
13. 一致性检验与失败模式
14. **最小数据决策树**：版本 A/B/C/D 各能做什么、不能说什么

## 6. 停止条件

缺市场规模、outside share、成交价、产品级结果或必需微观矩时：
**明说"最强可辩护的版本是什么、缺哪一块数据卡住了下一层"**，并给出该版本下允许的措辞。
不要用复杂数值替代缺失的数据变异；不要在数据不足时把设计写得更复杂来"补偿"。

## 7. 用户 house style（与本机既有偏好一致）

- 输出不用引用块；中文报告不用破折号与冒号式构造，段落过渡要强。
- 文件路径一律给完整路径；多交付件用表格。
- 交付物存 D 盘，不堆桌面。
- 引用绝不引 MDPI；APA 必须核实卷期页（走 `apa-citation`）。
- 稳健性表述禁用"并非由 XX 驱动"式否定归因。
- `significant` 只作统计义。
