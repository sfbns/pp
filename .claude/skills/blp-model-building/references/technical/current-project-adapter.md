# 当前项目适配层与纠错优先级（2026-10-08）

通用核心不依赖本项目。只在中国工况/标签/汽车信息研究时加载此文件。
项目根 D:\codex\output\blp_skill_integration_20261008；第一未完动作读取绝对路径 CHECKPOINT.json / CONTINUATION_CONTROLLER.json / NEXT_GOAL.md，先执行所绑定动作，再更新状态。过去“RELEASE PASS”只适用于原日期及原SHA，不认证本轮或迁移后版本。

当前证据与输入身份：
- D:\codex\output\blp_skill_integration_20261008\INPUT_MANIFEST.json，六份输入的原路径、复制路径和SHA；源文件不得覆盖。
- D:\codex\output\blp_skill_integration_20261008\source_ledger.json，逐项来源状态、原文版本/页码和政策官网锚点。
- D:\codex\output\blp_skill_integration_20261008\memos\blp_derivations.md，六篇基础/应用原文的目标页与既有完成证明。只有主文完成的，附录仍未完成。
- D:\codex\output\blp_skill_integration_20261008\BACKUP_MANIFEST.json，35份Claude技能配置原样备份。
- D:\codex\output\blp_skill_integration_20261008\EVALUATION_RUBRIC.md 与 evaluations，各轮独立结果保持不覆盖；未完成/低分不是PASS。

公式优先级：本轮明确撤回的旧规则 > 日期更早的报告/卡片。固定accepted抽样 q=fbar*p0/sbar，其份额为 mean_q[(sbar/fbar)*fj]；固定proposal计数为 mean_p0[I*fj/fbar]。不额外除sbar。买家样本必须用 dF_B=(1-P_i0)dF/s_B 或ratio-of-integrals；不能只条件化概率却继续总体F积分。两个可执行回归在 BLP技能 scripts/normalization_selftest.py 与 micro_sampling_selftest.py；general companion也以此为规范。

政策时钟不能合并：测试方法/车型准入 → 积分核算 → 标签标准生效 → 实际张贴/销售页展示 → 消费者实际接触。2021/2023检测与准入过渡不能直接充当2024标签展示日。GB22757.1/.2-2023发布2023-09-08，实施2024-07-01；适用车型、旧新申请和修订细则须按 source_ledger 的官方原条文与车型cohort逐项核，未核记待办。任何积分分值/补贴分档/BEV与PHEV适用范围在加入价格或IV前须官方核验；本文不认证全部EIDC范围。新标签不得无证据假定所有BEV续航上升。

2026-10-08重开官方通知补核：工信厅联通装〔2024〕43号成文2024-07-19、发布2024-07-23。第三（四）款规定启用日期是系统备案日期；第四款要求产品公告发布或取得CCC证书后15个工作日内备案；第七款自发布日起实施，新获批准/CCC车型及时备案粘贴，发布前已获批准/CCC车型在2024-09-01前补备案并更换。旧新cohort以通知发布界点及批准/证书日期划分，不能把成文日、标准实施日、备案日、截止日都叫消费者实际接触日。变更数据作新增标识、停产/停进口申请作废（第五款）。轻型商用车另有过渡附件，此处不扩大适用范围。来源：https://www.samr.gov.cn/zw/zfxxgk/fdzdgknr/rzjgs/art/2024/art_bce22a9fa293428cb0ff4bbb1f4db4c9.html 。逐车型真实张贴/网页展示仍待数据，不因法条核验而标完成。

用户口碑模块：inputs/BLP_品牌口碑建模与核验_20261007.zip 已审目录/文字/内部16项记录，未运行其代码且未完成外部评价。购车时已可见的总分可作内生质量代理，非能源分项可分开入可观测x，剩余ξ仍是未观察质量。能源/续航评分可能重复已有成本服务项；购买后评价、评论数和用户构成受销售、选择性评价、政策与产品质量共同影响，不能自动变成信任。优先预政策/滞后可见口碑并登记时间、样本和排除限制，不能把滞后当外生证明。

机制判别要求联合限制。里程高时成本渠道更强，但注意也可随使用强度上升；家充可缓解续航不便，也会改变电费与选择集。单个异质性不是排他证据。可交叉比较能源价格×预定里程、信息展示×先验/理解、家充×行程右尾，并给每个rival同样的预测机会。没有分离变化只称“与机制一致”。

数据最强层：全国车型—年月销量可估相对重配置，不能观察家庭实际转车路径；城市人口异质性须有地区车型销量。市场规模/价格/选择集/有效IV缺失则不报outside福利。企业专利是另一个企业—年份动态结果，不由静态BLP自动识别创新。

检索片段不替代局部状态：本技能内过去的语料数量、全部跑通与RELEASE文字均是历史记载，仅在原SHA和原作用域成立。当前的live-source检索已重建迁移技能片段；每次调用仍需重开该文件并检查当前checkpoint。
