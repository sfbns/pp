# CHECKPOINT BLP 经典改造篇与近期改造文献推荐（2026-10-02 起）

## 用户要求原话要点
- 「根据本地所有的关于 blp 模型中，根据记忆映射，根据 zotero 中也可以读取，挑出经典改造 blp 模型的一篇，然后再推荐 5 篇完全使用 blp 模型且进行改造的近期英文文献（可以是 working paper）」
- 2026-10-02 中途追加：「先把刚刚的任务和你完成的情况写入临时记忆，后续方便断点续联」

## 判据（blp-model-building skill）
- 称 BLP 须在全文同时看到：① 份额反演 ② 多产品 Bertrand 一阶条件 ③ 由加价反推边际成本；索引里的 classification 字段不算证据
- 证据层级分开写：fulltext-grounded / manual close reading（本次逐篇读了模型段）/ equation-level（本次未做逐式核验）
- 出处一律 Crossref 核实，DOI 不凭记忆；工作论文做期刊版升级检查

## 已完成（全部可复核）
1. 读记忆与记忆映射：资产七层图、28 篇语料分类错误、需求侧 49 篇、Zotero 本地 API、下载路径、`D:\codex\research-memory\fuel_econ_lit_2026_refresh_20260920\MEMORY_MAP.md`
2. 语料盘点：28 篇主语料索引、blp40/blp40s 深读包、`D:\auto-demand-lit-2026-09\` 49 篇表、Zotero 只读拉取 891 个顶层条目 → `zotero_top_items.json`
3. 三标记核验脚本 `marker_check.py`（结果 `marker_check.csv`、上下文 `marker_snippets.md`）；模型段抽取 `model_passages.py`
4. Crossref 核实 `crossref_verify.py` → `crossref_results.json`（2026-10-02）

## 结论（已核实，待写成报告）
### 经典改造篇：Petrin (2002) JPE 110(4): 705–729, doi:10.1086/340779（Zotero Z47HEXTA）
- 本地 PDF `D:\codex\research-memory\pdfs\Z47HEXTA_Petrin_2002.pdf` 是 52 页工作论文版，文字层整页坏字体；MinerU OCR 也只有表格图注可读 → 用页面图像核（`pageimg\petrin_p05–p19.png`）
- 改造：第 3.2 节在 BLP 的 GMM 里加二手调查（CEX）微观矩共 11 个＝3 个收入组购车概率 + 4 类家庭车买家平均家庭规模 + 4 类户主年龄 30–60 概率（WP p.15–16）；价格敏感度按三个收入组分段（p.10）；家庭规模与面包车/旅行车口味交互（p.11）
- 三标记：p.16 份额矩 s_j(δ(θ),θ)=s_j 用 Berry(1994) 反演；p.12 多产品 Bertrand-Nash，反解一阶条件得 mc，ln mc = Wτ+ω
- 数据：1981–1993 年 916 车型；CEX 1987–1992 约 3 万户、2660 笔新车购买（p.14）
- 备选经典：Grigolon & Verboven (2014) REStat 96(5): 916–935（RCNL），Zotero L42D4LX5

### 五篇近期（全部全文核过三标记 + 模型段人工阅读）
| # | 文献 | 改造位置 | 核验要点（页码为本地全文） |
|---|---|---|---|
| 1 | Grieco, Murry & Yurukoglu (2024) QJE 139(2): 1201–1253, doi:10.1093/qje/qjad047（本地 `J03.txt` 为 2023-03-09 作者版；Zotero P5D5GNTW 等） | 需求侧识别与福利 | CEX(1980–2005)+MRI(1992–2018) 人口矩 + MaritzCX 第二选择矩（1991/1999/2005/2015）p.7、13、16；Pakes 等(1993) 分解年度需求冲击为质量与外部选项价值→外部选项稳健的消费者剩余 p.2、4；Nash-Bertrand 反推 mc（摘要） |
| 2 | Hong, Kim & Verboven (2026) SSRN doi:10.2139/ssrn.7124440（本地 `W07.txt` 2026-09 版，标题页作者顺序 Hong/Kim/Verboven；CEPR DP21757 据卡片；Zotero QESK3F7I） | 需求侧异质性 | RC logit（Berry 1994；BLP 1995）产品-省-年 2012–2023 + 个人年里程与第二选择微观矩 p.3；每公里使用成本有随机系数与里程交互（表 4 p.22）；式(13) p^G = mc − (Ω∘∇s)^{-1}s 反推 mc p.24；结果：把纯电补贴改给混动多减排 47%，电力碳强度需降约 45% |
| 3 | Kaneko & Toyama (2025) JIE 73(1): 186–233, doi:10.1111/joie.12406（本地 `D:\fuel-econ-lit-2026\raw_text\P10_Kaneko2024_JIE.txt`；Zotero M2DXI3L4） | 需求函数形式 | 收入效应 f(y−p) 非参数化，带形状约束的筛估计嵌入嵌套不动点；收缩映射求 δ；VI(i) 节多产品 Bertrand 估 mc；日本汽车市场，补贴转嫁与兼并模拟，转嫁率与兼并效应高于参数模型 ⚠ 只讲价格曲率，不要写成「续航价值曲率」（记忆映射已撤回旧说法） |
| 4 | Barwick, Kwon & Li (2024) NBER WP w32264, doi:10.3386/w32264（另 SSRN 4771240；Crossref 未见期刊版；Zotero EWKUYMLW；本地中译 `D:\fuel-econ-lit-2026\translations\P02_...中译.md`） | 供给侧内生属性 | 价格、电池容量、车重三条 FOC 式(11)–(13) 含续航约束影子价格 λ_j；15 个收入组微观矩 + 嵌套收缩映射；34,329 观测（497 ICE/38 PHEV/164 BEV）；中国按续航 100/150/250 km 阶梯补贴（2/3.6/4.4 万元）导致车型缩小、损福利；按电池容量补贴福利最高 |
| 5 | Alé-Chilet, Chen, Li & Reynaert (2026) ReStud 93(1): 35–71, doi:10.1093/restud/rdaf024（本地 `J10.txt` 期刊版；Zotero 8VKC5Q74） | 供给侧合规属性与行为假设 | RCNL 需求（国家-年市场）p.18；式(13) mc = p + (Ω⊙S)^{-1}s p.21；用未合谋企业尿素罐选择 FOC 估「边际预期违规罚金」函数，合谋参与约束给罚金下降的界 p.3、20；欧洲 2007–2018；污染致福利减少 15.7–55.7 亿欧元 |

### 备选与配套（已核或已定性）
- Remmy (2026) AEJ:EP 18(2): 107–140, doi:10.1257/pol.20230294（Zotero I9HCTKI7）：价格与续航两条 FOC 式(3)(4) + 间接网络效应 + 充电站进入；与第 4 篇同属内生属性，作替换候选
- Barwick, Collison, Goldberg, Li & Wang (2026) NBER w35334（R26TG2LW）：全球市场、品牌层随机系数、中美调查微观矩、欧盟反补贴税样本外验证
- Barwick, Kwon, Li & Zahur (2025) NBER w33378（VF3L436T）：下游 Bertrand + 上游 Nash-in-Nash 讨价还价 + 干中学
- Heeney, Knittel & Mandia (2026) NBER w35023（HLZPRWWF）：供给侧加零部件成本不完全转嫁参数
- Heid, Remmy & Reynaert (2024) CEPR DP19631（UQQSSRIQ）：与电力市场联合均衡
- Ji, Wang, Zheng & Fan (2026) JAERE 13(1): 1–40, doi:10.1086/737533（GCNMC2Y9，有全文中译）：标准 BLP + 9 个收入组微观矩，属应用不算改造
- Barahona, Otero & Otero (2023) Econometrica 91(3): 839–868, doi:10.3982/ecta19603（S925QHZD）：标签政策 + 产品重构，概念上离工况标签最近；★本地与 Zotero 附件都只有线上附录，正文未核
- Van Biesebroeck & Verboven (2026) JEL 64(3): 984–1033, doi:10.1257/jel.20251792（W8KX625V）：BLP 在汽车业需求侧与供给侧被如何改造的综述，作路线图
- 排除：Allcott 等 (2024) NBER w33032 是校准的四层嵌套 logit，不算 BLP

## 状态：已完成（2026-10-02）
- 报告已交付 `D:\blp-lit-recommend-20261002\BLP经典改造与近期改造文献推荐_20261002.md`（文风自查通过；三处数字已回原句核对：Grieco「logit 福利增幅约为本模型 5 倍」、HKV 里程 60–80 km、BKL 2015–2018 年 40 城占 69%）
- 若用户要继续：可按 Q05 做法对五篇关键公式逐页看图核验；或把五篇在 Zotero 建一个分类（写入走 `D:\zotero-import-2026\zimport.py` 的 req() 骨架）

## 坑（别再踩）
- PDF 文字层的「ﬁ」连字会让 first-order、firms 匹配不上 → 先 unicodedata.normalize("NFKC")
- Petrin 本地 PDF 与 OCR 都是坏字体 → 只能渲染页面图像读
- Barahona 本地两份都是 Supplement，不能当正文引用
- Hong–Kim–Verboven 在 SSRN 元数据里作者顺序是 Kim 在前，按论文标题页写 Hong, Kim & Verboven
- 中文落盘用 Write 工具；暂存区可能被别的窗口清空，所有中间件都在本目录
