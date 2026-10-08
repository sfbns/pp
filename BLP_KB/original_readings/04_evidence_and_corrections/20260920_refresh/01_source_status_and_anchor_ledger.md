# 来源状态、版本关系与原文锚点台账

## 1. 清单结构

原始入口：

- [manifest.json](D:/fuel-econ-lit-2026/manifest.json)
- [文献名录](D:/fuel-econ-lit-2026/00_文献名录.md)
- [原批次完成记录](D:/fuel-econ-lit-2026/CHECKPOINT.md)
- [精读卡目录](D:/fuel-econ-lit-2026/cards/)
- [全文中译目录](D:/fuel-econ-lit-2026/translations/)
- [带页标记原文目录](D:/fuel-econ-lit-2026/raw_text/)

结构模型公式的基准来源另包括：

- [Berry, Levinsohn and Pakes (1995) 本地原文](D:/codex/blp.pdf)
- [既有 BLP 公式来源与审计台账](D:/codex/output/blp_driving_cycle_structural_research_20260824/formula_source_ledger.md)

本轮写入的 BLP 份额反演、需求工具矩和多产品 Bertrand 一阶条件均按上述公式台账复核；信念、标签和续航不便部分是本项目的显式扩展，不能冒充 BLP (1995) 原文设定。

19 个 manifest 项目的去重关系是：

- P07 与 P07b：同一论文的两个文件；抽取文本完全相同；
- P15 与 P17：同一研究的期刊版和早期工作论文版，以 P15 期刊版为准；
- 因而得到 17 份独立文档，其中 P05 是讲义，严格说是 16 篇论文加 1 套讲义。

## 2. 关键论文证据台账

| ID | 论文与版本 | 本轮证据状态 | 对当前项目最可靠的用途 | 关键本地锚点 |
|---|---|---|---|---|
| P01 | Barwick et al. (2025), *Drive Down the Cost* | 选定页 source-verified，其余 card-backed | 长期电池学习和成本反馈；不进短期标签基准 | [卡片](D:/fuel-econ-lit-2026/cards/P01_Barwick_Kwon_Li_Zahur_2025_精读卡.md)；原 PDF pp. 2–5, 13–22, 31, 57–58 |
| P02 | Barwick, Kwon & Li (2024), *Attribute-based Subsidies and Market Power* | source-verified | 内生属性、价格、续航技术前沿、多产品供给和微观矩 | [数据与设定](D:/fuel-econ-lit-2026/raw_text/P02_w32264.txt:761)；[属性选择](D:/fuel-econ-lit-2026/raw_text/P02_w32264.txt:917)；[技术前沿](D:/fuel-econ-lit-2026/raw_text/P02_w32264.txt:951)；[IV 与微观矩](D:/fuel-econ-lit-2026/raw_text/P02_w32264.txt:1098) |
| P03 | Xia & Zhang (2025), *Energy Economics* | source-verified | 中国 CAFC 下产品组合与技术采用；是需求标签效应的供给侧 rival | [原文](D:/fuel-econ-lit-2026/raw_text/P03_EE2025_775.txt:19)；原 PDF pp. 1–4, 10–11 |
| P04 | Leard, Linn & Springel (2023), RFF WP | 关键段 source-verified | 精细车型 twins、属性—价格联合内生和分配效应 | [数据](D:/fuel-econ-lit-2026/raw_text/P04_WP2304.txt:453)；[维护性假设](D:/fuel-econ-lit-2026/raw_text/P04_WP2304.txt:892)；[产品内变异](D:/fuel-econ-lit-2026/raw_text/P04_WP2304.txt:1037)；[outside](D:/fuel-econ-lit-2026/raw_text/P04_WP2304.txt:2793) |
| P05 | Barwick et al. (2025), ASSA slides | card-backed；非正式论文 | 只可作为研究方向线索；不能承担识别或精确数值引用 | [卡片](D:/fuel-econ-lit-2026/cards/P05_Barwick等_2025_精读卡.md) |
| P06 | Zhang & Popp (2026), NBER 34763 | 摘要和选定页 source-verified | 长期创新响应；不解释即时月份需求跳跃 | [卡片](D:/fuel-econ-lit-2026/cards/P06_Zhang_Popp_2026_精读卡.md)；原 PDF pp. 2, 5–7, 13, 30–32 |
| P07 | Schloter (2022), *Transport Policy* | card-backed | EV 与汽油车折旧的描述性背景 | [卡片](D:/fuel-econ-lit-2026/cards/P07_Schloter_2022_精读卡.md) |
| P08 | Allcott et al. (2026 revision), NBER 33032 | source-verified | second-choice、动力替代、outside、静态 Bertrand | [数据](D:/fuel-econ-lit-2026/raw_text/P08_w33032.txt:116)；[事件研究](D:/fuel-econ-lit-2026/raw_text/P08_w33032.txt:797)；[需求结构](D:/fuel-econ-lit-2026/raw_text/P08_w33032.txt:924)；[市场规模](D:/fuel-econ-lit-2026/raw_text/P08_w33032.txt:1237)；[二选择矩](D:/fuel-econ-lit-2026/raw_text/P08_w33032.txt:1276) |
| P09 | Gavazza, Lizzeri & Roketskiy (2014), *AER* | 关键段 source-verified | 二手市场、匹配和稳态一般均衡；仅作动态扩展 | [作用链](D:/fuel-econ-lit-2026/raw_text/P09_Gavazza2014.txt:126)；[短期政策边界](D:/fuel-econ-lit-2026/raw_text/P09_Gavazza2014.txt:184)；[横向差异抽象](D:/fuel-econ-lit-2026/raw_text/P09_Gavazza2014.txt:257) |
| P10 | Kaneko & Toyama (2025), *JIE* | source-verified + 公式页视觉核验 | 价格—可支配收入曲率和传递率稳健性 | [正确曲率边界](D:/fuel-econ-lit-2026/raw_text/P10_Kaneko2024_JIE.txt:562)；[市场与 outside](D:/fuel-econ-lit-2026/raw_text/P10_Kaneko2024_JIE.txt:1337)；[税制 IV](D:/fuel-econ-lit-2026/raw_text/P10_Kaneko2024_JIE.txt:1594)；[排除限制](D:/fuel-econ-lit-2026/raw_text/P10_Kaneko2024_JIE.txt:1716) |
| P11 | Roberson et al. (2024), *ERL* | source-verified | 续航与挂牌保值率的条件关联；残值测量动机 | [卡片](D:/fuel-econ-lit-2026/cards/P11_Roberson_2024_精读卡.md) |
| P12 | Andreassen & Lind (2024), *ERE* | source-verified | 挪威低续航组与折旧关联；新旧工况换算的方法提示 | [卡片](D:/fuel-econ-lit-2026/cards/P12_Andreassen_Lind_2024_精读卡.md) |
| P13 | Zhang & Zhao (2021), *AOR* | card-backed；模型存在已记录问题 | “残值焦虑/担保”概念参照；不作为 BLP 参数依据 | [卡片](D:/fuel-econ-lit-2026/cards/P13_Zhang_Zhao_2021_精读卡.md) |
| P14 | Yan, Lin & Chen (2026), *TR-A* | source-verified | 设计工况认知、注意、信任调查的启发 | [研究对象与 HCM](D:/fuel-econ-lit-2026/raw_text/P14_TRA_S0965856426001679.txt:23)；原 PDF pp. 1, 3–5, 10–14 |
| P15 | Gillingham, Houde & van Benthem (2021), *AEJ: Policy* | source-verified + 公式页视觉核验 | 可见评级、价格反应和未来燃料成本资本化的直接母本 | [myopia 定义](D:/fuel-econ-lit-2026/raw_text/P15_Gillingham2021_Myopia.txt:87)；[不能分解机制](D:/fuel-econ-lit-2026/raw_text/P15_Gillingham2021_Myopia.txt:174)；[DID](D:/fuel-econ-lit-2026/raw_text/P15_Gillingham2021_Myopia.txt:321)；[SUTVA](D:/fuel-econ-lit-2026/raw_text/P15_Gillingham2021_Myopia.txt:617)；[连续成本楔子](D:/fuel-econ-lit-2026/raw_text/P15_Gillingham2021_Myopia.txt:1160)；[价格等于 WTP 的条件](D:/fuel-econ-lit-2026/raw_text/P15_Gillingham2021_Myopia.txt:1179) |
| P16 | Bento, Gillingham & Roth (2017), NBER 23340 | card-backed | 规制引起的属性分布与安全外部性；非核心 | [卡片](D:/fuel-econ-lit-2026/cards/P16_Bento_Gillingham_Roth_2017_精读卡.md) |
| P17 | P15 的 2019 NBER 早期版 | 版本对照 | 不独立累计证据；数值冲突以 P15 为准 | [原文](D:/fuel-econ-lit-2026/raw_text/P17_w25845.txt) |
| P18 | Bai et al. (2022 WP) | source-verified，但已被正式版取代 | 多维度工程足迹方法；不能解决单一销量 outcome 的对照组 | [产品内维度设计](D:/fuel-econ-lit-2026/raw_text/P18_w27644.txt:648)；[数据单位](D:/fuel-econ-lit-2026/raw_text/P18_w27644.txt:759) |

## 3. 两篇本地较新正式论文

### 3.1 P18 的 AER 2025 正式版

本地正式版：

- [Bai et al. (2025), *Quid Pro Quo, Knowledge Spillovers, and Industrial Quality Upgrading*](D:/codex/aer/bai-et-al-2025-quid-pro-quo-knowledge-spillovers-and-industrial-quality-upgrading-evidence-from-the-chinese-auto.pdf)
- SHA256：`2D06C0AC4668C52858CD5DAC7B662B030166045C05E2B55A283BB2D9DAB08D72`
- 正式出处：*American Economic Review* 115(11): 3825–3852；DOI [10.1257/aer.20221501](https://doi.org/10.1257/aer.20221501)。

正式版必须替代旧工作论文数字：

- 正式版主结果为领先合资车型某质量维度高 1 个标准差时，关联自主车型该维度约高 `0.098` 个标准差；
- 股权关联知识溢出贡献了 2001–2014 年关联自主车型相对质量改善的 `8.3%`；
- 旧工作论文中的 `0.087` 和 `3.8%–19.5%` 不应再作为正式引用值。

对本项目的许可边界：其“车型内部跨多个质量维度”的设计可以用于诊断真实工程适配发生在哪些属性；销量在车型—月份只有一个数值，不能复制到多个属性维度后伪造识别。

### 3.2 AER 2026 的报告卡与可见指标理论

本地原文：

- [Hörner & Samuelson (2026), *What You Don't Know May Be Good for You*](D:/codex/aer/hörner-samuelson-2026-what-you-don-t-know-may-be-good-for-you.pdf)
- SHA256：`DA1B6FAB39622513E2CEB665DD14276A561AABD39783A0EB67652DCE4A0D1803`

原文允许的项目映射是：公开报告卡或可见指标可能改变被评价者选择对象和投入维度，从而诱发回避、选择和 Goodhart 式扭曲。对汽车的应用只能写成**理论 rival**：工况标签可能改变企业的测试、标定、披露、广告或车型组合。该文没有直接证明汽车企业已经操纵工况。

## 4. 公式视觉核验记录

本轮对以下页面进行了 PDF 视觉核验，而非仅依赖纯文本：

- P15：AEJ: Policy 正文 p. 222–223，式 (2) 与价格资本化条件；
- P02：需求效用与城市×年份×动力固定效应页；
- P08：多层嵌套误差结构、份额和价格导数页；
- P10：式 (24)–(25) 的半参数收入效用、Bernstein 逼近和连续性条件页。

视觉核验支持的关键边界是：P10 的非线性对象是 (f(y-p))，不是续航效用 (h(R))；P15 的价格反应等于 WTP 需要数量/供给条件，不能直接从价格系数推出完整需求效应。
