# Xing–Leard–Li (2021) 本轮全文阅读补证

## question_received

对 *What does an electric vehicle replace?* 本地33页PDF进行实际分块全文阅读，覆盖正文、文件已包含的附录、图表和参考文献；记录逐页内容锚、原始文件哈希、阅读块和明确完成证明。不能以“脚本计算33页”代替阅读，不能把未取得的外部在线附录算作完成。

## source_scope

版本：Xing, J., Leard, B., & Li, S. (2021). *What does an electric vehicle replace?* Journal of Environmental Economics and Management, 107, 102432. DOI: https://doi.org/10.1016/j.jeem.2021.102432 。PDF第一页显示2021-03-17 available online。

- 原始PDF（本轮主读来源）：`D:\codex\research-memory\BLP_structural_models_memory_skills_configs_2026-08-24\01_primary_enhanced_corpus\source_pdfs\27_lxuzm7vx.pdf`
- 页级JSON（已核存在与33个非空页）：`D:\codex\research-memory\BLP_structural_models_memory_skills_configs_2026-08-24\01_primary_enhanced_corpus\raw\fulltext\27_lxuzm7vx.fulltext.json`
- TXT：`D:\codex\research-memory\BLP_structural_models_memory_skills_configs_2026-08-24\01_primary_enhanced_corpus\raw\fulltext\27_lxuzm7vx.fulltext.txt`
- 原个体阅读记忆：`D:\codex\research-memory\BLP_structural_models_memory_skills_configs_2026-08-24\01_primary_enhanced_corpus\memories\papers\27_lxuzm7vx.md`
- 原完成边界审计：`D:\codex\research-memory\BLP_structural_models_memory_skills_configs_2026-08-24\01_primary_enhanced_corpus\audits\csv_manifest_fulltext_audit_2026-04-18.md`

### SHA256（本轮实算）

|文件|SHA256|
|---|---|
|PDF|`174D8650AF63A6ABC25F97195C7697D2B42793838FE84210220DD236AD06DCC7`|
|页级JSON|`5B05C9896B91CD3ADFE109C4822C51D853A771809D8338DA604FCE997FAD7236`|
|TXT|`632E34052CACC47909C55640B022F8DA4C7FB1EB207ABD1991BAC6E265CE9836`|
|原个体卡|`3649735702BAA3A95C3DFC6D0C690D7D0DC01894B544ADCB45C273446BA59A99`|

## answer

**completed：本地这份33页PDF已在本轮分六块实际读完。** 此次包括PDF内附录A–G、表1–8/A1–A8、图1–3/A1–A3及参考文献页。不是只读摘要、卡片或脚本扫描。所有页的全文抽取均直接送入本轮阅读上下文；图形页另渲染和视觉查看，正文核心式(12)、式(13)及附录疑点也做视觉回源。

模型准入结论：**随机系数 BLP demand-only implementation（首选/次选MLE + BLP份额反演 + 均值效用价格IV）**。不是canonical联合需求供给GMM；市场是新车购买条件样本，无购买/二手车/公交外部选项未建模，反事实没有厂商价格或充电网供给响应。不能把旧索引的canonical demand-supply标签原样沿用。

### 分块阅读覆盖记录

|块|PDF页|实际阅读输出chunk_id|阅读后内容判断|
|---|---|---|---|
|1|1–6|`647935`|摘要与问题、数据来源、选择型抽样权重、第二选择分布、替代排放理论起点|
|2|7–12|`21ae87`|复合替代品/额外性、效用、首选次选联合MLE、份额反演、价格IV、异质性识别、参数及去掉次选对照|
|3|13–18|`936c68`|弹性表、移除EV、移除补贴、收入定向补贴、福利/排放与分配比较|
|4|19–24|`2fcadd`|敏感性、明确边界与长期遗漏、结论、附录背景/文献/VMT/联合似然及梯度|
|5|25–29|`994f7b`|隐函数与弹性导数、混动销量反事实、表A1–A6及MSRP稳健性|
|6|30–33|`1b20de`|排放损害表、无第二选择反事实、附录三幅图与完整参考文献页|

以上chunk_id是本轮工具输出的证据定位，不是论文来源ID。另有早于六块的模型页8–10阅读不重复计数。渲染页31出现MuPDF结构树告警 `format error: No common ancestor in structure tree`，进程exit0，PNG成功生成并已实际视觉打开；未把该告警静默写成渲染失败或省略页面。

### 逐页内容锚与阅读要点

|PDF页|锚|阅读要点|
|---|---|---|
|1|标题/摘要/Introduction|研究排放收益需知道EV替代什么；RC离散选择估计及移除EV/补贴反事实；不是假定每辆EV替代平均汽油车。|
|2|Introduction贡献与非额外性|偏好排序使EV买家也喜欢高效非EV；次选数据用于估计而不是直接一对一指定替代；additionality与替代结构分开。|
|3|§2 Data description|MaritzCX五个model-year2010–14、11,628样本、全收EV并随机抽非EV；采用Manski–Lerman choice-based sample权重。|
|4|Table1|家庭收入、教育、城市化、价格、油耗及每年424/404/418/441/459个选择；超抽样导致样本均值不是人口均值。|
|5|Table2/数据匹配与成交价|EV首选/次选车型；Wards属性、IHS注册份额、model-year×make×model×fuel匹配；成交价含税、对credit领取不直接调整。|
|6|Fig1/§3/式1–2|各动力买家的次选动力构成有强异质性；E=sum(e_j q_j)，EV补贴经各车型价格导数影响排放。图已视觉检查。|
|7|式3–9/§3.1–3.2|复合替代品排放按替代导数/交叉弹性加权；依赖总新车数量固定；非额外比例N=q无补贴/q有补贴。|
|8|式10–12/§4.1|additionality取决于自价格弹性；明确conditional新车选择、不含outside；效用为均值+人口交互+正态随机偏好；价格为ln(p)。|
|9|式13–15/§4.2|首选与剔除首选后的次选概率在同一随机偏好下相乘再积分；MLE估异质性、反演匹配份额、价格IV恢复均值效用。公式已视觉核验。|
|10|§4.2/§5.1|人口×属性识别观察异质性；首选/次选属性相关与时间选择集变化识别随机偏好；4个RC分别油耗、加速、轻卡、AFV。|
|11|Table3/150Halton|OLS/IV均值参数、含/不含第二选择的异质性估计；150Halton draws；去掉第二选择只移除一类识别信息，不删人口交互。|
|12|§5.2|次选大幅提高未观察异质性估计精度；条件市场弹性较完整outside模型小；早期样本同动力替代受EV选择少限制。|
|13|Table4|车型交叉弹性矩阵、价格和同一抽样权重/模拟draw；廉价车型自身价格反应通常更大，不能把某个EV交叉弹性移植中国。|
|14|Table5/§6.1|按动力汇总的弹性；移除EV后所有EV购买者必须选另一新车；替代品集中于中型/高效车辆，使用外部VMT估计核算排放。|
|15|Fig2/§6.2|移除EV的动力/油耗替代组成与消费者福利损失；开始补贴移除反事实。图已视觉查看。|
|16|Table6|补贴移除销量变化、替代动力、五收入组私人消费者福利；解释非额外性和环境收益，承认维持2014条件。|
|17|Fig3/§6.3|真实替代核算与平均汽油车假定核算不同；两种定向补贴：高收入取消、低收入另加2000/4000。图已视觉查看。|
|18|Table7|总预算、EV销量、CO2及收入组私人福利比较；定向补贴潜在更省钱且较不累退；不是外生政策因果估计。|
|19|Table8/§6.4/§7起点|改弹性或EV价格做情景敏感性；2014早期市场特征限制外推；开始讨论空间电网排放。|
|20|§7 caveats|空间发电排放、VMT反弹、无outside、full pass-through假设；遗漏outside的排放偏误方向不确定，不能给固定方向。|
|21|§7/§8|无厂商价格/产品及充电网长期响应；CAFE/GHG重叠约束可能抵消收益；2014 choice set不代表后续SUV/轻卡EV。|
|22|§8结尾/AppendixA|主要结论和政策目标、BEV/PHEV成本与补贴制度背景；本页结论数值与前表有差异，保留来源警示。|
|23|AppendixB/C/D|补充文献、NHTS odometer四阶年龄曲线预测25岁VMT；开始重述效用和联合似然。|
|24|AppendixD|模拟首选/次选联合概率与梯度展开；发现+1分母、混合概率对数分解与正文不一致，已视觉核验。|
|25|AppendixD/E|隐函数求反演效用导数、加权score、份额与自身价格导数；scalar inverse写法需完整Jacobian归一化解释，+1也与conditional设定不一致。|
|26|AppendixE/F|交叉价格导数使用受影响车型k的边际效用；3个维持hybrid补贴场景：EV竞争影响小，混动补贴退出的模型反事实作用更大。|
|27|AppendixG TablesA1/A2|2000–17动力份额与车型数，2018读取的全国平均grid排放；不能当作当前或中国参数。|
|28|TablesA3/A4|EV/非EV买家人口、租赁及充电差异；用MSRP替代成交价的估计稳健性，非新的因果识别。|
|29|TablesA5/A6|移除EV的销量/福利分组；不同segment×fuel预测lifetime VMT；消费福利不含排放。|
|30|TablesA7/A8|各污染物损害核算合计50.9million；不含次选估计下替代与补贴结果不同，支持次选数据的作用边界。|
|31|FigA1/A2|次选segment：PHEV/BEV更偏cars；价格越高自价格弹性绝对值越小。两图已视觉读图，不以两条caption代替。|
|32|FigA3|无hybrid补贴下实际/移除EV/移除EV补贴曲线很近；保留hybrid补贴下曲线更高。两panel和图注已视觉查看。|
|33|References|BLP1995/2004、Train–Winston2007、Petrin2002、Manski–Lerman1977、排放/补贴/网络先例；参考文献页已完整浏览，未额外声称参考文献全部原文读过。|

## mechanism_chain

论文链：购车者人口与未观察偏好 → 首选/次选车型属性共同相关 → 识别异质性与替代矩阵 → 移除EV或补贴 → 新车购买条件内的再分配 → 给定VMT和排放因子下的排放变化。补贴另通过价敏识别边际购买者/非额外性。作者没有估消费者对工况标签的先验更新，本项目借用的是异质替代/第二选择模块，不是信念识别结果。

## predictions

同类属性强首选/次选相关应对应较大相应taste dispersion；去掉第二选择会降低未观察异质性估计精度；以平均汽油车代替结构上被挤出的车辆可产生排放核算差异。以上预测分别由论文模型、估计和反事实承担，不是中国标签政策因果结论。

## rival_and_falsifier

第二选择报告未必是实际缺货时会买的产品；外部选项、价格重定、产品设计、VMT和电网排放异质性都可能改变反事实。可用实际库存/退出后的替代、保留样本预测、第三方second-choice验证及不同choice set检验，不以同样本份额拟合作独立验证。

### 原文公式疑点与正确使用边界

以下均来自原始PDF视觉回源，不是擅自改写原文。它们说明为什么不能宣称“原文/全篇公式没有问题”，但本轮没有审作者代码，不能据此断言其实际估计代码或结果错误。

1. **PDF9式(13) vs PDF24 AppendixD**：正文首选分母为新车集的sum(exp(v))；附录却写1+sum(exp(v))。按PDF8、14、20明确的conditional新车市场设定，不应无声加outside。若实际有基准车型，其归一化必须说明，不能同时对全部新车求和再加1。
2. **PDF24混合似然**：正文正确的联合对象是同一taste draw下先乘后积分。一般RC情形，`log(mean_r(a_r*b_r)) != log(mean_r(a_r))+log(mean_r(b_r))`。附录中间一行作了后一分解，后续又使用联合概率导数。用于笔记/实现应保持联合混合概率，不能照抄错误等号。
3. **PDF25反演导数**：份额对所有产品mean utility有交叉导数，应使用完整份额Jacobian；无outside条件市场还要固定一个效用归一化。单个产品diagonal derivative的倒数不能一般替代整个矩阵逆。
4. **PDF25–26弹性**：若P_ij已积分，必须在taste draw条件概率上先求乘积/导数，再对draw和消费者加权平均；不能一般把积分后的P_ij直接平方而当作E[P_ij(v)^2]。

实现核验式（`standard-derived`，不是声称原文逐字公式）：定义新车choice set J、`V_ij(v)=delta_j+mu_ij(v)`、`P_ij(v)=exp(V_ij(v))/sum_{g in J}exp(V_ig(v))`。则

```tex
P_{ijh}=\int P_{ij}(v)\,
 \frac{\exp V_{ih}(v)}{\sum_{g\in\mathcal J\setminus\{j\}}\exp V_{ig}(v)}\,dF(v),
\qquad \ell=\sum_i w_i\log P_{ij_i h_i}.
```

模拟时同一draw同时进入两个因子。给一个参考新车r，固定delta_r=0，令s_{-r}为余下独立份额，正确隐函数是

```tex
\frac{\partial\delta_{-r}}{\partial\theta}
=-\left(\frac{\partial s_{-r}}{\partial\delta_{-r}}\right)^{-1}
 \frac{\partial s_{-r}}{\partial\theta}.
```

这是对conditional市场最小实现口径的代数说明，尚未对该论文计算代码执行任何复现或数值测试。

### 数值/文稿内部差异（保留而不擅自修源）

- 摘要PDF1和正文PDF15写39%，导言PDF2写27%。
- 正文PDF16/附表A7写环境收益50.9million，结论PDF22写73.8million。
- PDF14部分CO2文字单位与周边billion数量级不一致，PDF18叙述中的0.92省略表7的million限定。
- 这些差异禁止跨段落无条件拼接精确数值；目前用户任务不需要引用结果数值，推荐只用模型结构和机制边界。

## handoff

打包器可把本文件作为本地“全文已读”的新增证明，并附原始个体卡+PDF+页级JSON。核心公式笔记以正文式(12)/(13)/(15)为锚，保留本文件AppendixD/E疑点。若用户要求全文每个公式全部修正，还需独立逐式审计与实现验证；本次阅读完成不等于论文代码复现或全公式证明完成。

## confidence_and_limits

`fulltext_read_complete_local_pdf`：完成；范围精确到上述33页。`key_formula_visual_review`：完成，PDF8/9/24/25已视觉核验。`all_formula_proofs_checked`：否。`empirical_replication`：否。`external_online_appendix_read`：未声称。原PDF、原卡和原全文层均未修改；新增文件只扩展阅读证据。

## completion_proof

```json
{
  "paper_key": "LXUZM7VX",
  "paper_doi": "10.1016/j.jeem.2021.102432",
  "read_date_client": "2026-10-07",
  "source_pdf_sha256": "174D8650AF63A6ABC25F97195C7697D2B42793838FE84210220DD236AD06DCC7",
  "page_count": 33,
  "read_chunks": [[1,6],[7,12],[13,18],[19,24],[25,29],[30,33]],
  "all_local_pdf_pages_read": true,
  "missing_local_pdf_pages": [],
  "included_appendices_read": ["A","B","C","D","E","F","G"],
  "figure_pages_visually_read": [6,15,17,31,32],
  "key_formula_pages_visually_read": [8,9,24,25],
  "status": "completed",
  "scope": "This 33-page local PDF only, including its appendices and references",
  "all_equations_proved_or_replication_completed": false,
  "original_files_modified": false
}
```
