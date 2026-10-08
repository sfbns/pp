# GRV (2018) 本轮全文阅读完成证明

```yaml
paper: Consumer Valuation of Fuel Costs and Tax Policy - Evidence from the European Car Market
authors: Laura Grigolon; Mathias Reynaert; Frank Verboven
doi: 10.1257/pol.20160078
date: 2026-10-07
status: completed
fulltext_pages_read: 33
fulltext_pages_total: 33
pdf_page_range: 1-33
journal_page_range: 193-225
online_supplement_read: false
source_status: source-verified; complete local main-text reading
```

## 1. 完成口径与执行证据

本轮依次打开并阅读下列四个**无省略、无截断**的原始 PDF 页级文字输出，覆盖本地文件的全部 33 页：正文、脚注、表格内容、图形文字/图注和参考文献。每个分块均完整返回且 exit 0，随后逐页形成下面的内容锚点与阅读记录，最后才记为 completed。不是“脚本扫过所有页”就自动把阅读状态升级。

本文件没有内嵌的在线附录，正文多次引用的 Online Appendix A/B 不在这 33 页内；**没有下载/阅读全文在线附录，亦不把引用它们的主文视为已经读过附录**。图 1/2 的文字、坐标与图注已读，但本轮没有逐个目测图中数据点，不据此新增精确读图数值。核心成本与效用式 PDF p.8 在本轮已查看原始 PDF 渲染图；不声称每个脚注公式都重新视觉认证。

原始 PDF：

`D:\codex\research-memory\BLP_structural_models_memory_skills_configs_2026-08-24\01_primary_enhanced_corpus\source_pdfs\04_5twrwep3.pdf`

旧原文全文 TXT：

`D:\codex\research-memory\BLP_structural_models_memory_skills_configs_2026-08-24\01_primary_enhanced_corpus\raw\fulltext\04_5twrwep3.fulltext.txt`

逐篇模型卡：

`D:\codex\research-memory\BLP_structural_models_memory_skills_configs_2026-08-24\01_primary_enhanced_corpus\memories\papers\04_5twrwep3.md`

[AEA 官方落地页](https://www.aeaweb.org/articles?id=10.1257/pol.20160078) 本轮已打开，刊物、卷期、页码与 DOI 一致。本地 PDF 早已存在，无需用户再下载。

## 2. 源文件与全文哈希

| 对象 | SHA256 |
|---|---|
| 原始 PDF 字节 | `5D729774CBE07F5281ED09097CAF3F224BE24A2260417E766D8D361B5E8670DF` |
| 本轮原 PDF 抽取的全部页级文字 | `DAB5C1D06FB4C12DEEE851059150C557253B664BD90D4C635111542D7D67CA1F` |
| 既有 `.fulltext.txt` 文件原始字节 | `B42012C9AF1BE51196EBD3B8A929B7C3A36D93886F1B0C91693B19D3AB52704E` |

本轮全文文字哈希定义：PyMuPDF `get_text()` 依次抽取 33 页，以单个 LF 拼接所有页面，再对 UTF-8 字节计算 SHA256。总字符数 114312（包含 32 个页间 LF）。既有 TXT 含额外页标记/换行，所以哈希与本轮直接抽取字符串不同，不能误判原文不同。

四个阅读块的字符数不含块内加入的页间 LF；下面的块哈希则以 LF 拼接该块页文字后按 UTF-8 计算。

| 块 | PDF 页范围 | 期刊页范围 | 页文字字符数 | 块全文 SHA256 | 结果 |
|---|---|---|---:|---|---|
| C1 | 1–8 | 193–200 | 29842 | `82BF2DA6FF85992C77D196449D3DD76B3890D4842FAFF2555D18CA9BEC255313` | 全部阅读；exit 0 |
| C2 | 9–16 | 201–208 | 24647 | `5DF10D924094623DA8FD7A741F6F068CB02519FF421AC3B8BB976C77ACB4F87C` | 全部阅读；exit 0 |
| C3 | 17–24 | 209–216 | 29278 | `50E65D2BB86A7374997130D7E711A6138FDBD3AB1C63227D459836EEA85FEE85` | 全部阅读；exit 0 |
| C4 | 25–33 | 217–225 | 30513 | `646C3AE378B634202E54A3A50E5399D28C07D3BABFBB034AAF2408054259157B` | 全部阅读；exit 0 |

## 3. 逐页内容锚点与阅读记录

| PDF / journal 页 | 字符数 | 实际阅读的内容及关键锚点 |
|---|---:|---|
| 1 / 193 | 3347 | 标题、作者、摘要、利益声明；争论是燃油税与产品税如何影响购买及使用。研究同时考虑资本化不足与里程异质性，不是单纯证明短视。 |
| 2 / 194 | 3939 | 两步任务：先估未来燃料估值，再比较收入等价税。明确以 BLP aggregate random-coefficients logit 为基础；七国 1998–2011，同车型汽油/柴油引擎差构成主要信息。 |
| 3 / 195 | 4263 | 主结论及限制：每 1 欧元未来节省约资本化 0.91 欧元，不能拒绝正确估值；里程异质性改变税的 targeting，额外成本异质性使优势减弱。强短视可翻转税排序。 |
| 4 / 196 | 4045 | 福利含决策消费者剩余、错误优化损失、外部性和税收。文献对照强调忽略异质性的 sorting bias；二手车和报废反应不在其新车数据研究内。 |
| 5 / 197 | 4172 | 里程高的消费者更受能源税影响而选择节油车型；区分 attentiveness 异质性、里程异质性与产品质量；说明 BLP 原来随机“miles per dollar”项需关联实际里程。 |
| 6 / 198 | 3152 | §I.A，市场为 country/year、车辆为 model×engine、含 outside；式 (1) 是价钱加未来燃料成本进入效用的跨期预算基础。 |
| 7 / 199 | 3733 | 式 (2) 给预期现值；gamma 为 attention/future-valuation 参数；里程异质但对油价完全无弹性。维持燃料价格、寿命、贴现和里程假设才能解释 gamma。 |
| 8 / 200 | 3191 | 油价随机游走；式 (3) G=rho×里程×L/km×油价，式 (4) rho 为有限期贴现和，式 (5) RC utility；gamma/rho 与里程尺度不可自由分开。原页核心公式本轮已视觉核。 |
| 9 / 201 | 3447 | 固定 r/S 得 gamma，或固定 gamma 得隐含利率/回收期；式 (6) 积分 logit 份额，Monte Carlo；燃油税与产品税进入效用的位置不同。 |
| 10 / 202 | 3612 | 税对份额的导数以及 outside 项；相同里程且 gamma=1 时收入等价税有同等需求效应，gamma<1 时能源税弱；里程异质时税排序不再机械。 |
| 11 / 203 | 3604 | §II，JATO七国新车、配置—引擎单位、平均800配置；建议零售价及其折扣潜在偏误；油耗以 L/100km 收集，需求模型用 L/km。 |
| 12 / 204 | 1349 | 图1燃油价格时间与国家差异、图注/坐标；2008和2011峰值、柴油折价；起接英国 NTS 里程来源。文字使用2000年欧元，图注使用2005年欧元，引用基年时需额外核数据，不能默默统一。 |
| 13 / 205 | 2845 | UK NTS 20000人、偏右里程分布和图2；将英国分布用于其他国家并用Eurostat均值稳健性；GDP/人缩放价和成本，人口定义潜在市场。 |
| 14 / 206 | 2613 | 表1/2已读；柴油份额、引擎数、价格与油耗差；表1观测数行82151而注释82166存在文本内不一致，应保留而不任改。 |
| 15 / 207 | 3782 | §III 参数分布限制；观察到的是购车条件下里程分布，模型需非条件分布，主文指向在线A.3映射；其他属性正态、对角方差，价格敏感度alpha/y_t。 |
| 16 / 208 | 3395 | 式 (7) 可估复合系数alpha gamma rho；式(8)车型FE、国家趋势/二次项、上市月数FE；发动机内燃料成本变异分解说明并非主要依赖时间油价。 |
| 17 / 209 | 3362 | BLP contraction与GMM；核心假设是条件于车型FE除价格外特征外生；BLP特征和IV，亦试成本IV。该维护假设不能无条件移植至中国内生工程属性。 |
| 18 / 210 | 3314 | 最优IV二阶段；98市场、500准随机draws、100里程节点×5其他draws、内循环1e-12/外优化1e-6/50起点；比较logit、仅里程RC、全RC。 |
| 19 / 211 | 3977 | 表3完整阅读；RCII gamma=0.91、SE0.18，gamma rho=8.84；F=291只在所报logit第一阶段，不能冒充所有非线性参数强识别。表中价/成本负号是估计系数报告，需与效用负项记号区别。 |
| 20 / 212 | 3987 | 属性均值/方差、country×diesel解释边界；多种油价/里程/FE稳健性。额外燃料类型RC难估，额外成本异质性独立引入且扩大方差。 |
| 21 / 213 | 3878 | 设r=6%、S=15（偏有利于发现低估）以解释gamma；RCI 0.77；寿命随里程变化的稳健性采用最大250000km并加报废率。主文给脚注表达，未读它引用的在线数值表。 |
| 22 / 214 | 3494 | RCII资本化不足统计不显著，误优化成本约40欧/车，可能与理性不注意相容而非证明。§V分别用收入等价比较有效性与外部性等价比较福利，两种基准不得混称。 |
| 23 / 215 | 3610 | 德国2011 counterfactual；多产品Bertrand、常数MC、FOC反推MC与新均衡；比较gamma=.5/.91/1。不声称由多起点证明唯一均衡。 |
| 24 / 216 | 3656 | 表4完整阅读；燃油税/product税对油耗四分位销量与价格；说明产品税对构成更强不意味着对总燃料使用更强；“prices”变化与含税消费者支出区别。 |
| 25 / 217 | 2944 | 表5完整阅读；为了干净跨模型比较此表将gamma设1，不能把此表数字冒充全为估计gamma=.91。简单logit outside替代不合理大；RC分里程与属性才改变税目标性。 |
| 26 / 218 | 3513 | RCII燃油用量降18.1% vs产品税12.0%是表5基准；强短视gamma=.5可翻转；额外非里程异质性弱化目标性；开始分燃料税讨论。 |
| 27 / 219 | 3285 | 表6完整阅读；分别提高汽油/柴油税，使用量变化大于市场份额变化，因高里程者选择变化；柴油空气污染与CO2不是同一外部性。正文写1998平均0.50与表7显示差距不吻合，精确引用须另核。 |
| 28 / 220 | 2915 | 表7全部国家、年份、油价gap、油耗gap、柴油份额及三种归一反事实已读；差别分解是结构反事实，不是准实验估计的占比。 |
| 29 / 221 | 3835 | §V.B 福利；决策CS+belief error，外部性取能合理化既有税的水平；外部性等价产品税；主文福利计算先设完全竞争简化，不要误说所有福利数字都来自Bertrand。 |
| 30 / 222 | 3022 | 表8完整阅读；一般外部性和柴油外部性两个场景；税收、CS、belief error、外部性与福利逐列。图表题/注也有0.50与正文0.20口径差，不修原文、不把它们无条件混用。 |
| 31 / 223 | 3816 | §VI结论及参考文献开头；可复用贡献是里程异质性加资本化权重而不是证明普遍短视。读至Bento等sorting-bias文献条目。 |
| 32 / 224 | 4832 | 参考文献全部阅读：Berry1994、BLP1995/1999、Busse等、NTS、Fullerton/West、Grigolon数据出处、Hausman、Jacobsen等；这是文献表阅读，不意味着每篇引用都读过。 |
| 33 / 225 | 2351 | 参考文献余部全部阅读：Klier/Linn、Nevo、Petrin、Reynaert/Verboven、Sallee、Verboven等；本地文件在参考文献结束，无内嵌online appendix。 |

## 4. 读后判断：为什么值得作为严格 BLP 推荐

1. 严格 RC demand：p.2/6/9/17 可串起 BLP demand、异质里程、份额反演和 IV/GMM。
2. 严格供给扩展：p.23 明确多产品 Bertrand、MC恢复和重新定价；福利小节又明确完全竞争简化，须按场景而非全篇贴一个标签。
3. 对用户“短视”模块最关键的是 p.8/15 的识别限制、p.19/22 的不可拒绝正确估值，及 p.25 的使用量与平均油耗分离。不能因为标题涉及 future cost valuation 就把gamma<1当确定事实。
4. 不能取代信念模型：本文基准没有估计真实道路油耗的 prior/posterior，主要聚焦未来成本资本化与里程选择。真实—标签差距的认知母本仍用R&S (2021)。

## 5. 复核命令口径

```python
import fitz, hashlib
pdf = fitz.open(PDF_PATH)
texts = [page.get_text() for page in pdf]
for lo, hi in [(1,8),(9,16),(17,24),(25,33)]:
    print('\n'.join(f'=== PDF PAGE {i+1} ===\n{texts[i]}'
                    for i in range(lo-1, hi)))
sha = hashlib.sha256(('\n'.join(texts)).encode('utf-8')).hexdigest()
```

Python stdout 使用UTF-8，本轮四块原文阅读均成功。命令和hash只提供内容可复现性；**完成判定还依赖实际逐块读取和上面的逐页主旨记录**。原始PDF和旧全文文件保持不变。
