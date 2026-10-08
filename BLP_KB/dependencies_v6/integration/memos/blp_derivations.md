# 中国驾驶工况重标：从零建立 aggregate RC-BLP 的推导与边界

日期：2026-10-08。角色：BLP / structural professor。责任文件仅为本备忘录、同目录 `numerical_blp_checks.py` 和 `results.json`；未修改原文、旧技能、旧记忆或其他代理的产物。

## question_received

在只有车型—市场—年月聚合数据、可外接收入分布的条件下，如何把 ICE、HEV、PHEV、BEV 与 outside 纳入随机系数 BLP，区分工况标签、真实能耗、消费者信念、运行成本资本化、续航便利和电池技术，得到正确的替代、供给与福利反事实？哪些参数目前可估计，哪些必须固定、另取微观矩或另建动态模型？

## source_scope

### 来源优先级与阅读状态

先读 QUESTION_PROTOCOL、BLP 私有记忆及 baseline/enhanced/improvement/driving-cycle/auto-EV skills，继而原文回源。没有用45篇桥接卡证明某文是BLP，也没有在本轮声称新增论文完成全文阅读。

本文标记：**source-exact**＝列明原文式的忠实转写；**standard-derived**＝在明确假设下的标准推导，不冒充原文原式；**project-extension**＝本项目新增设定，须额外数据及识别；**illustrative-only**＝合成数值检验，不是估计结果。

本轮重开 BLP 原始 PDF 的9、10、14、15、25、26页及原始页面图，重开P01/P02下面关键页；其余关键页依前一轮已回源记录。全文阅读完成口径继承各自完成证明，**本轮仅为目标页公式复核，不是重新通读六篇**。原始印刷页码与PDF页码分别列示。

令 `R = D:\codex\research-memory\BLP_structural_models_memory_skills_configs_2026-08-24\01_primary_enhanced_corpus`。

|原始来源及文件|本备忘录所用原文锚点|本地阅读/边界证据|
|---|---|---|
|Berry–Levinsohn–Pakes1995，`D:\codex\blp.pdf`|PDF9/期刊848：式2.5线性价格RC、2.6 Cobb–Douglas；PDF10/849：式2.7收入与outside；PDF14–15/853–854：3.2–3.6利润、FOC、加价、成本、矩；PDF25–26/864–865：6.6–6.9积分、反演、导数|`D:\codex\blp_1995_deep_reading_notes.md`；`D:\codex\output\blp_bundle_20261007\audit_baseline_sources.md`。本轮再次检查原式，不把线性价格简式冒充论文实证的收入规格。|
|GRV2018，`R\source_pdfs\04_5twrwep3.pdf`|PDF6–9/198–201：式1–5效用、未来成本与里程；PDF15–18/207–210：反演、GMM/IV；PDF23/215：Bertrand反事实|个体卡`R\memories\papers\04_5twrwep3.md`；`D:\codex\output\blp_bundle_20261007\grv_completion_20261007.md`：本地33/33页完成；未读外部online appendix。|
|Reynaert–Sallee2021，`D:\codex\output\reynaert_sallee_2021_source.pdf`|PDF18/389：真实属性、gaming与awareness；PDF25/396：RC-BLP效用、outside、GMM；PDF29/400：awareness不能识别、experienced utility|`D:\codex\reynaert_sallee_2021_gaming_china_cycle_close_read_20260822.md`：本地主文41/41；在线附录仅定点读。`D:\codex\output\blp_bundle_20261007\audit_belief_myopia.md`。awareness是情景参数，不是可信度的已识别估计。|
|Barwick–Kwon–Li2024，`C:\Users\于舒奕\Downloads\w32264.pdf`，March2024版本|PDF20–23/正文18–21：式8效用、outside、价格/容量/重量选择、式9–13前沿/FOC；PDF24–25/22–23：IV及微观矩|`D:\fuel-econ-lit-2026\cards\P02_Barwick_Kwon_Li_2024_精读卡.md`；`D:\fuel-econ-lit-2026\CHECKPOINT.md`：历史全文翻译与完整性记录；57页。原文容量不直接入需求是一项条件排除假设，不是工程定理。|
|Xing–Leard–Li2021，`R\source_pdfs\27_lxuzm7vx.pdf`|PDF8：式12；PDF9：式13首选/次选联合概率、14似然、15反演；PDF20–21：局限|`R\memories\papers\27_lxuzm7vx.md`；`D:\codex\output\blp_bundle_20261007\xing_completion_20261007.md`：33/33实际全文补读。**conditional新车需求，没有outside、没有供给重定价**；不照抄其附录与正文不一致的概率/导数表达。|
|Barwick–Kwon–Li–Zahur2025，`C:\Users\于舒奕\Downloads\w33378.pdf`，RevisedAug2025版本|PDF13–14/11–12：式2 RC-BLP、式3下游FOC；PDF18–20/16–18：收入异质性、IV/微观矩、式7电池干中学|`D:\fuel-econ-lit-2026\cards\P01_Barwick_Kwon_Li_Zahur_2025_精读卡.md`及同一CHECKPOINT；72页。选择集是EV+outside，非EV在outside；上游讨价还价/LBD不是专利创新模型。|

原始PDF均保留原字节。旧绝对路径 `D:\codex\blp_structural_memory_2026-04-18` 已失效；本表 `R` 指向现存导入层，不沿失效旧卡寻址。项目恢复边界见 `D:\codex\output\blp_driving_cycle_structural_research_20260824\00_DURABLE_TASK_BRIEF.md` 及 `formula_source_ledger.md`。本文不是对旧80条公式账本或整篇译文的全量重新认证。

## answer

### 1. 先定义决策与市场，而不是先拟合销量

**project-extension。** 市场 \(m\) 是购车决策地理单元，\(t\) 是月或年；若只有全国车型月销量，则 \(m\) 只有全国，不能虚构城市异质性。产品 \(j\) 是在该市场时点确实可购买的稳定配置，含动力类型 \(a_j\in\{ICE,HEV,PHEV,BEV\}\)。换代、容量变化、发动机或真实效率变化不能仅因同一车名而当作不变产品。

一次选择集 \(\mathcal J_{mt}\cup\{0\}\)；outside 0＝本期不买新乘用车（可能继续用旧车、买二手车、公共交通等的合成选项），**不是“其他燃料车”**。\(q_{jmt}\) 是单位销量，\(M_{mt}\) 是有经济含义的潜在决策单位数：

\[
s_{jmt}=q_{jmt}/M_{mt},\qquad s_{0mt}=1-\sum_{j\in\mathcal J_{mt}}s_{jmt}>0.
\]

不能以新车销量总和作 \(M\) 却仍声称包含outside。月度模型中“所有家庭每月独立重新选择一次”是很强的静态购车风险集假设；应解释风险集、检查年度聚合和替换周期。否则outside质量与购买延迟混合，长期补贴/信息反事实需要动态耐用品模型。若只有新车条件份额，退回Xing式conditional需求并停止声称新车总量、outside分流或总社会福利已被识别。

消费者类型 \(i=(y_i,d_i,\nu_i)\sim F_{mt}\)，包括收入、里程/充电条件、偏好抽样。外接收入是**潜在消费者总体**收入分布，而非新车购买者收入分布；后者是模型的条件结果。无城市数据就不能拟合城市收入交互。IID极值冲击的尺度固定为1，不可再自由估计统一效用尺度。

### 2. 三种能耗与两种运行成本

**project-extension。** 分开物理真实能耗 \(e^T\)、按某工况认证的数值 \(e^C\)、消费者实际见到的标签 \(L\)。注册/认证的法律日期、车型证书切换日、网站/门店展示日是三个处理对象。政策可以先改变 \(e^C,L\)，不改变硬件和 \(e^T\)；厂商之后才可能改变硬件。

真实每公里费用（货币/km）为：

\[
\begin{aligned}
c^T_{ijh}&=g^F_h f^T_{ijh}/100, &&j\in\{ICE,HEV\};\\
c^T_{ijh}&=g^E_{ih} e^T_{ijh}/100, &&j\in BEV;\\
c^T_{ijh}&=\{a_{ijh}[g^E_{ih}e^T_{CD,ijh}+g^F_hf^T_{CD,ijh}]
 +(1-a_{ijh})[g^E_{ih}e^T_{CS,ijh}+g^F_hf^T_{CS,ijh}]\}/100,
 &&j\in PHEV.
\end{aligned}
\]

\(f\) 用L/100km，\(e\) 用kWh/100km，油价元/L、电价元/kWh；\(CD/CS\) 是耗电/保电运行状态，\(a\) 为距离份额，取决于可用纯电续航、出行链及充电条件。混动PHEV在CD模式可能烧油；不能无条件设为零。若认证“综合油耗”已经按utility factor加权，不能再次乘 \(1-a\) 后又叠加同一分项造成重复加权。无实际里程/充电数据，PHEV的运行成本只能在外部校准情景下构建，不能仅由销量估计真实 \(a\)。

\[
C^T_{ijmt}=E\!\left[\sum_{h=1}^{H_i} d_i(h)\,A_i(h)\,\ell_{ih}\,c^T_{ij,t+h}\right],\qquad
\widehat C_{ijmt}=E_i\!\left[\sum_{h=1}^{\widehat H_i}\widehat d_i(h)\widehat A_i(h)\widehat\ell_{ih}\widehat c_{ij,t+h}\mid I_{imt}\right].
\]

\(d(h)\)是折现权重，\(A(h)\)是仍承担该车运行成本的概率/持有状态，\(\ell\)是里程。应直接对乘积取期望；费用、里程、生存/持有不独立时不能替换成期望的乘积。若仅计首任车主持有期，出售残值/未来效率资本化须一致处理；不能既计算全寿命运行成本又重复加入同一未来成本的残值收益。保养、燃料与电费、充电时间、续航不便不得重复计算。

**source-exact（GRV式1、2，PDF6–7）：**
\[
u_{ijk}=x_{jk}\beta_i^x-\alpha_i(p_{jk}+\gamma G_{ijk})+\xi_{jk}+\varepsilon_{ijk},\qquad
G_{ijk}=E\sum_{h=1}^{S}(1+r)^{-h}\beta_i^m e_{jk}g_{k,h}.
\]
该文 \(e\) 为L/km，本项目单位需要除100。其PDF8明确运行成本现值尺度与里程需外部锚定。

### 3. 标签差距首先是信念映射，不自动是边际效用变化

**source-exact（R&S，PDF18）：** 真实坏属性 \(x\)，message \(x-g\)，awareness \(a\) 下 \(\widetilde x=a x+(1-a)(x-g)\)。这是一种便利的情景信念，不是已估计的贝叶斯先验或信任参数；该文PDF29明确awareness不能据其数据准确识别。

**project-extension。** 更一般地：
\[
\widehat e_{ijmt}=B_i(L_{jmt},\text{cycle}_{jmt},\text{prior}_{ijmt},\text{experience}_i,\text{attention}_i,\text{reliability}_i).
\]
“先验经验”是购买前关于真实能耗的信念分布/均值；经验是形成该分布的信息。“信任”可影响信号可靠性；“注意”可决定是否接收信号；“短视/资本化”是给未来费用的决策权重；它们不是一个参数的不同名称。例如正态信号下后验均值为精度加权 \(\widehat e=(\tau_0e_0+\tau_LL)/(\tau_0+\tau_L)\)，信任改变主观精度 \(\tau_L\)，而不是直接改变真实节能的偏好系数。该例只是一种可检验建模选择，非本地论文已证实的心理过程。

同一消费者对真实费用的偏好 \(-\alpha_i\gamma_i\)可以不变，而标签改变其决策所用 \(\widehat e\)。约化回归中“油耗系数变化”可能仅是 \(\partial\widehat e/\partial L\) 改变，不能因此说所有消费者的内在边际效用都变了。反之标签也可能带来独立环保形象/显著性效用；这是另一条需单独识别的偏好渠道，不能由销量自动区分。

### 4. 一个可估计的需求核心，以及不应同时自由估计的对象

**project-extension。** 暂以类型内对货币线性的规格为主：
\[
\begin{aligned}
u^d_{ijmt}&=v^d_{ijmt}+\varepsilon_{ijmt},\\
v^d_{ijmt}&=X_{jmt}'\beta_i+\mathrm{FE}_{jmt}+\xi_{jmt}
-\alpha_i[p^{net}_{jmt}+\gamma\widehat C_{ijmt}]
-\kappa_i h(\widehat R_{ijmt},A_{imt},T_i),\\
v^d_{i0mt}&=0,\qquad \varepsilon_{ijmt}\stackrel{iid}{\sim}EV1.
\end{aligned}
\]

\(p^{net}\)是交易总支出，含适用税费、扣除现金补贴；不能拿MSRP当净交易价又在另一项重复补贴。\(h\ge0\) 是范围/充电不便，随可用续航降低、随充电可达性改善而降低；须与已货币化的充电时间分开。动力类型截距/随机系数是其他口味的合成，不自动是环保偏好、信任或续航焦虑。\(\xi\) 是计量者不可见、消费者/厂商可能知晓的质量，不是每个新机制的自由吸收器。

一种受约束的异质性为 \(\alpha_i=\exp(a_0+a_y\log y_i+\sigma_\alpha\nu_{\alpha i})>0\)，\(\beta_i=\bar\beta+\Pi d_i+\Sigma\nu_i\)。这是**项目参数化**；P02式8确有正的指数价格权重，但P01式2是 \(+\alpha_i(p-\phi)\) 的有符号系数，不能把两文符号/分布拼接。仅有聚合数据应先选少数关键随机系数；允许完整协方差、动力截距、信念异质性、里程异质性全部自由通常没有相应矩支撑。

若 \(\widehat C=\rho\,\ell\,b\,c_j\)，则效用只出现 \(\gamma\rho\ell b\)。将 \(\gamma\) 乘常数、里程除同一常数不变预测；若信念是比例 \(b\)，它亦进入同一乘积。**不得同时自由估计\(\gamma\)、里程尺度、折现/寿命尺度和比例信念。** 外部收入分布并不解决这一不可分离性。可用外部里程与持有期固定 \(C\)，先固定belief再估资本化；或固定资本化、借直接belief矩识别信念。也可只报告复合成本权重/敏感性区间。

低 \(\gamma\) 只能先称“相对现值成本的低资本化”；它可能来自不注意、不同燃油预期/里程/寿命、融资约束、转售、风险或折现。只有把这些对象及规范基准锚定后，才能把差额命名为短视。销量上升/下降的符号不是这项锚定。

### 5. 容量、能量密度与续航不能无约束地一起做“偏好”

**project-extension。** 理想工程关系（不作为实证恒等式强塞数据）：
\[
m^{bat}_j=1000B_j/d_j,\quad m^{total}_j=m^{chassis}_j+m^{bat}_j,\quad
R^T_{ij}\simeq100\,u_j B_j/e^T_{ij}.
\]

\(B\)：kWh，\(d\)：Wh/kg，\(u\)：可用容量比例；电芯、包、系统能量密度口径不可混用。能量密度影响重量、效率、成本及可能的可用空间/安全；容量本身可以只通过续航影响需求，也可能有充电速度、寿命、配置质量等未控直接渠道。P02 PDF21采用“控制续航后容量无直接需求效应”，P01 PDF19亦以此作为一组成本IV的排除假设；**这不是可不加验证移植到当前中国市场的定理**。

基线需求放可用续航与可解释属性，容量/密度放工程和成本块；若要估直接容量偏好，必须有控制续航/重量后的独立变异及额外矩。若续航与容量近乎函数对应，同时无约束放容量、密度、重量、续航及其政策交互，很容易秩弱和重复归因。实车道路效率改善与认证口径重标应拆开。

### 6. 份额、导数与个体/总体替代

**standard-derived；对应BLP PDF25–26。** 省略 \(mt\)：
\[
P_{ij}=\frac{\exp(v^d_{ij})}{1+\sum_{r=1}^{J}\exp(v^d_{ir})},\quad
P_{i0}=\frac1{1+\sum_r\exp(v^d_{ir})},\quad
s_j=\int P_{ij}\,dF(i).
\]

设仅自身价格进入自身确定效用，\(b_{ik}=\partial v^d_{ik}/\partial p_k<0\)。**以需求为行、价格为列**定义 \(D_{jk}=\partial s_j/\partial p_k\)：
\[
\boxed{D_{jk}=\int P_{ij}(\mathbf1\{j=k\}-P_{ik})b_{ik}\,dF(i)}.
\]

outside行也适用，\(\mathbf1\{0=k\}=0\)。线性货币基线 \(b_{ik}=-\alpha_i\)：own \(D_{jj}<0\)，cross及outside \(D_{jk}>0\)；每列含outside加总为0。矩阵对称仅在这类每类型对各产品价格边际效用相同的规格中成立。

**standard-derived（BLP式2.6/2.7收入形式）：** 若 \(v_{ij}=a\log(y_i-p_j)+\cdots-a\log y_i\)，\(b_{ik}=-a/(y_i-p_k)\)，故 \(D_{jk}\ne D_{kj}\) 一般成立。必须保证所有抽样 \(y_i>p_j\)，否则收入域不成立；不能把低收入不能现金全款买车粗暴删掉后假装无融资模型。该规格是收入效应示例，实际车贷/跨期预算需要单独设计。

价格弹性 \(\epsilon_{jk}=D_{jk}p_k/s_j\)。局部降流比（单独提高 \(j\) 价格、固定其他对象）为 \(\mathrm{DR}_{j\to k}=D_{kj}/(-D_{jj})\)，\(k\ne j\) 包括outside，合计1。它是边际替代预测，不是观察到的逐人“原本必买某车却实际改买”的转移矩阵。

聚合导数是个体导数的积分，不是把总体份额放进单一logit公式，亦不是平均消费者的导数。动力组 \(G\) 对统一改变 \(H\) 组每个产品价格的反应是 \(\sum_{j\in G}\sum_{k\in H}D_{jk}\)；只求前一个和对应单产品价格冲击，不能把两种对象混淆。

若政策 \(z\) 同时改变多个产品效用，令 \(a_{ij}=\partial v^d_{ij}/\partial z\)，连outside一并保留：
\[
\frac{\partial s_j}{\partial z}=\int P_{ij}\left(a_{ij}-\sum_{k=0}^{J}P_{ik}a_{ik}\right)dF(i).
\]
即使所有车的自身标签都“改善”，相对改善、outside、价格响应也可能使某车销量下降。只有单个产品自身效用改善、其他效用/价格/风险集固定时，才能得自身份额增加的条件预测。

**standard-derived，Xing正文式13的边界应用。** 条件新车选择集中的首选 \(j\)、次选 \(h\ne j\) 联合概率为
\[
\int P^{new}_{ij}\frac{\exp V_{ih}}{\sum_{k\ne j}\exp V_{ik}}dF_{new}(i).
\]
两项在**同一类型积分内**，不能分别积分再相乘。若本项目有outside却调查仅覆盖新车买家，要显式条件化和选择加权；不能直接把总体 \(F\) 当 \(F_{new}\)。次选矩能帮助识别替代，但并不自动识别belief或真实里程。

### 7. 反演与识别是两件事

**standard-derived，BLP式6.8。** 任一明确分解 \(v^d_{ij}=\delta_j(\theta_1)+\mu_{ij}(\theta_2)\) 均可，前提是价格/成本不漏计、不重复计；例如 \(\delta=X\bar\beta-\bar\alpha p+FE+\xi\)，其余放 \(\mu\)。给定非线性参数及正份额：
\[
\delta^{n+1}_j=\delta^n_j+\log s^{obs}_j-\log s_j(\delta^n,\theta_2).
\]

模拟积分使用固定节点、权重和稳定log-sum-exp，收敛误差小于目标函数梯度精度；检查不同抽样和多起点。零销量、缺车与未进入不可一概加任意小常数：核验choice set，解释聚合/删失方案并做敏感性。

令 \(J_\delta=\partial s/\partial\delta=\int[\mathrm{diag}(P_{i,inside})-P_{i,inside}P_{i,inside}']dF\)。反演的隐函数导数是**完整矩阵逆**：
\[
\frac{d\delta}{d\theta_2}=-J_\delta^{-1}\frac{\partial s}{\partial\theta_2}\Big|_\delta.
\]
不可逐产品用一个标量own导数替代。需求GMM为 \(E[Z^d\xi]=0\)，供给可加 \(E[Z^s\omega]=0\)；微观矩可用 \(E[y\mid j]=\int y_iP_{ij}dF/s_j\) 或收入组购买份额。**外部总体收入分布不是购买微观矩**。识别要看排除限制和堆叠矩对参数的Jacobian秩/曲率，反演精确拟合份额并不识别每个随机系数。

价格、标签版本/切换、真实效率、续航、容量、密度和choice set都可能内生。竞品属性/差异化IV、成本IV仅在其排除假设成立时可用；能源价格×预定能耗需排除同期需求/显著性/宏观渠道。强固定效应有助控制共同冲击，也可能吸收处理变异；先列出剩余变异。法规机械重标可提供信息变异的设计，但法律日期不是消费者暴露日期，亦可能同时改变税补、准入或供给。

反事实保持的是**参数、真实偏好及指定不变的\(\xi\)**，不是机械固定含价格的 \(\delta\)。改变价格必须更新 \(\delta,\mu\) 中所有价格项。反事实不重新按旧销量反演 \(\delta\)：否则会把政策效应强制吸收回未观测质量、重新得到旧份额。

### 8. 多产品Bertrand：转置、收入效应、税与多市场

**source-exact，BLP PDF14式3.2–3.4；standard-derived矩阵翻译。** 固定属性、单市场、消费者价等于厂商单位收入价，厂商 \(f\) 利润
\[
\Pi_f=M\sum_{r\in\mathcal F_f}(p_r-mc_r)s_r(p)-FC_f.
\]
令 \(H_{jr}=1\{j,r\text{同厂}\}\)，对厂商自己的 \(p_j\) 求导：
\[
0=s_j+\sum_r H_{jr}(p_r-mc_r)\underbrace{\frac{\partial s_r}{\partial p_j}}_{D_{rj}}.
\]
因此对本文的行列约定：
\[
\boxed{\Delta=-H\odot D^{\top},\quad \eta=p-mc=\Delta^{-1}s,\quad mc=p-\eta.}
\]

原BLP的 \(\Delta_{jr}\) 本来就按 \(-\partial s_r/\partial p_j\) 定义；不是原文遗漏转置。只有把软件Jacobian改为本文 \(D_{jk}\) 约定时才显式转置。线性价格下对称会掩盖错置；收入效应下会直接错算FOC与成本。负成本/异常加价不能简单裁为零，应查价格、M、所有权、导数、行为假设和供给约束。

**project-extension。** 有税/补贴时先定义厂商决策价 \(P\)、单位收入 \(r_j(P_j)\)、消费者支出 \(c_j(P_j)\)：
\[
0=r'_j(P_j)Q_j+\sum_{k\in\mathcal F_f}[r_k(P_k)-mc_k]\frac{\partial Q_k(c(P))}{\partial P_j}.
\]
税率/现金补贴传导必须按该链式求导，不把消费者与厂商价格混为一列。全国统一MSRP但本地税补不同时，利润和FOC应对 \(m\) 加总 \(Q_j=\sum_mM_ms_{jm}\)，价格导数亦加总；不能每个城市各自反推一个“全国统一价格”均衡。若实际由经销商定价，就需说明厂商/经销商两层结构或把当前结果仅称定价近似。品牌、母公司、合资的共同定价集合需要所有权/行为证据，不能仅按品牌字符串建立 \(H\)。

给定固定成本与属性，反事实均衡解 \(F(p,z)=0\)；在 \(F_p\) 非奇异的局部：
\[
\frac{dp^*}{dz}=-F_p^{-1}F_z,\qquad
\frac{ds^*}{dz}=s_z+D\frac{dp^*}{dz}.
\]
计算须检查FOC残差、经济域/成本、厂商own-price Hessian和多起点。局部解或负定Hessian不证明全局唯一均衡。单纯固定价格需求反事实与供给重定价反事实须分列，不能称同一个“政策总效应”。

**project-extension，P02给出来源模板而非直接估计许可。** 属性 \(a_j\) 由厂商选择时：
\[
0=\sum_{k\in\mathcal F_f}(r_k-mc_k)\frac{\partial Q_k}{\partial a_j}
-Q_j\frac{\partial mc_j}{\partial a_j}-\frac{\partial FC_j}{\partial a_j}
+\lambda_j\frac{\partial G_j}{\partial a_j},
\quad \lambda_j\ge0,\ G_j\ge0,\ \lambda_jG_j=0.
\]
若属性改变别的产品成本，成本项也须对那些产品加总。\(G\) 是法规/补贴门槛约束；门槛非光滑时FOC仅适用区间内部/给定门槛档位，须比较离散换档/产品设计利润。短期先固定硬件；中期再估前沿、成本和固定设计成本；不能把标签切换的短期销量反应直接说成厂商效率创新。

### 9. decision welfare 与 experienced welfare：保持同一决策

**project-extension的规范选择。** 先明确“experienced”评价哪些偏好：同一真实口味和使用便利，将信念费用换成真实费用；若把决策资本化 \(\gamma\) 换为1，必须另行证明规范贴现/持有期基准，否则偏好差异被误称行为损失。报告 \(\gamma^E=\gamma^D\) 与外部规范基准的敏感性。未识别真实成本/信念时不报告点识别纠偏福利。

**standard-derived；R&S PDF29提供decision/experienced边界。** 对类型 \(i\)、制度 \(r\in\{0,1\}\)，定义 \(L_i^d(r)=\log\sum_{j=0}^J\exp v^d_{ij}(r)\)，
\[
W_i^e(r)=L_i^d(r)+\sum_{j=0}^JP^d_{ij}(r)[v^e_{ij}(r)-v^d_{ij}(r)].
\]
公共Euler常数在差分中抵消。推导：在同一 \(\varepsilon_i\) 下按 \(v^d+\varepsilon\) 选 \(j^d\)，其真实效用＝决策最大效用+\(v^e_{ij^d}-v^d_{ij^d}\)，再取期望。不能按 \(v^e\) 重新最优化后把logsum称作原错误选择的experienced福利。

类型内货币效用线性、同一 \(\alpha_i>0\) 在两制度固定时：
\[
\Delta CS^d=\int\frac{L_i^d(1)-L_i^d(0)}{\alpha_i}dF(i),\qquad
\Delta CS^e=\int\frac{W_i^e(1)-W_i^e(0)}{\alpha_i}dF(i).
\]
必须先按类型除其货币边际效用，再积分；不能以“平均logsum变化/平均alpha”代替。真信息oracle \(L_i^e=\log\sum_j e^{v^e_{ij}}\) 是相同 \,\(\varepsilon\) 评价下的最优选择上界，且
\[
L_i^e-W_i^e=KL(P_i^d\Vert P_i^e)\ge0.
\]
只有固定价格、choice set、真实效用和信息获取成本，且新信息使选择准确最大化同一真实效用时，纠正信息的experienced gain非负；不推广为均衡净福利必增。坏消息可降低decision logsum而提高experienced福利，二者符号不必一致。

收入效应下没有常数 \(\alpha_i\) 可除。须在**完整绝对效用含outside收入项**中定义货币补偿：例如正确belief的ex-ante CV \(c_i\) 解 \(E\max u_i^{1}(y_i-c_i)=E\max u_i^{0}(y_i)\)。\(\alpha\log y\) 的outside基准在价格导数/选择概率中可归一化，但在收入转移福利中不可丢掉。ex-ante CV不等于先求每个极值冲击实现的CV再取期望。带决策偏差的experienced CV还要明确转移是否改变决策、belief及哪些选择规则；其转移—福利函数未必单调，不能未经验证宣称根存在唯一。

若算社会福利，须结合重新定价的企业利润、财政收入/支出、真实使用带来的外部损害与真实资源成本；税补是转移，不能既在CS价格中计入又作为独立资源收益重复加总。损害依真实里程/能耗，标签值不能替代。充电/研发/设计固定成本及财政融资边际成本按命名反事实另计。没有可辩护 \(M\) 就没有市场总量福利的识别。

### 10. 专利创新必须另立动态块

**project-extension，不是上述论文的source-exact创新模型。** 静态BLP将给定技术下的均衡需求和利润写作 \(\Pi_f^*(S_t,z_t)\)。另建知识状态 \(K\)、经验 \(E\)、竞争/供应商网络与政策状态 \(S\)：
\[
\begin{aligned}
V_f(S_t)&=\max_{RD_{ft}\ge0}\{\Pi_f^*(S_t,z_t)-C_f^{RD}(RD_{ft},S_t)
+\beta_fE[V_f(S_{t+1})\mid S_t,RD_{ft}]\},\\
K_{f,t+1}&=(1-\delta_K)K_{ft}+g_f(RD_{ft})+\mathrm{spillover}_{ft}+\zeta_{ft},\\
E_{f,t+1}&=E_{ft}+q_{ft},\qquad
mc_{f,t+1},e^T_{f,t+1},d_{f,t+1}=T(K_{f,t+1},E_{f,t+1},\text{inputs},\text{design}).
\end{aligned}
\]
创新投入先作出，产出有随机性/时滞；专利申请/授权/质量是知识或研发产出的带噪测量，如 \(E[patent^{app}_{f,t+\ell}\mid RD,K,\mathrm{filing\ rules}]\)，不是 \(K\) 本身。申请到授权时滞、分类和授权选择需另建测量层。P01识别的是累计生产经验的LBD，不等于专利研发；P02属性选择不等于技术前沿创新。

“重标改变相对需求/利润 → 改变真实效率或信息gaming的回报 → 改变研发/设计 → 后续专利/技术/成本”每个箭头需要自己的变异。市场扩大可能提高研发回报，利润压缩也可能降低融资能力；静态销量正负不决定创新方向。当前没有研发/企业专利匹配、产出滞后、技术和知识转移信息，不估完整动态博弈。先做预定技术暴露的创新约化证据，再决定是否值得加动态结构。

### 11. 分阶段可估计方案与停止规则

|阶段|实际对象与可做的事|不能声称|
|---|---|---|
|A：数据/政策审计与RF|车型稳定ID、销量、上市/退出、真实展示、同硬件机械标签差、税补/价格、固定效应与预趋势；连续强度事件研究可作起点|无交易价/M/可辩护choice set时，不能说完整BLP已经可估；日历2021附近不自动构成RDD|
|B：aggregate需求|明确M、净交易价、外部总体收入、外部里程/寿命/预期固定；先少数RC；固定belief和资本化之一（必要时两者都固定），用有效IV识别价格/替代|不能把拟合销量解释为已识别短视、信任、先验、注意或PHEV实际电动里程|
|C：机制扩展|直接belief/感知标签、认知实验、里程/充电、真实能耗、首选/次选和购买者收入矩；检验参数秩、竞争解释|一份外部收入分布不能同时替代这些数据；信念与偏好仅在额外变异下区分|
|D：短期供给/福利|所有权、成交价/厂商价税映射、固定硬件Bertrand、mc恢复、FOC/多解核验；固定价与重定价、decision/experienced分开|没有企业行为/真实使用证据，不给唯一真实成本、真实外部损害和确定净福利|
|E：中长期|先有产品设计/前沿/固定成本数据再内生属性；有研发/专利/时滞和状态数据再动态创新|不能把当期容量/密度、专利计数或销量直接命名为政策诱致创新|

## mechanism_chain

**主链：** 法规/认证口径与落实时间 → 固定硬件的标签及可比性变化 → 实际接触、主观可靠性与belief更新 → 感知现值运行成本/续航不便变化 → 各类型相对效用与outside选择变化 → 厂商短期重新定价 → 购买量、动力间替代、真实使用与experienced福利。

**必须单列的竞争链：** 同一规则 → 税补/准入门槛变化、认证/合规成本 → 净价格或choice set/产品设计变化 → 购买量。以及宏观能源价格、收入、供给短缺、充电网络、换代与品牌需求冲击。中长期再从预期利润回报进入研发/设计，不把最后一条倒写成当期心理机制。

## predictions

1. **条件预测：** 同硬件、只提高某车被感知的每公里费用、固定其他产品/价格/outside，且 \(\gamma,\alpha>0\)，该车份额下降；分流到其他车和outside。联合重标或均衡重定价不保证每个销量符号。
2. **成本机制预测：** 其他条件相同，外部证据支持的更高预期里程、较长持有期或较高燃料价格提高同一感知能耗差的货币影响。不能用销量估出的“高里程”再循环证明该机制。
3. **信息预测：** 已准确知道真实能耗的消费者对纯标签重标的成本belief反应应弱；有先验偏差且确实见到可信标签者应更强。反应也可能来自显著性或形象，故需先验/后验感知测量。
4. **续航边界：** BEV可用续航/充电不便并非燃油成本的符号翻转；PHEV的成本反应依实际充电与出行距离。不能由BEV销量反向直接推断消费者不信标签。
5. **供给预测：** 同一需求变化在多产品所有权下引致内部替代与重新定价；方向依Jacobian、成本和竞争结构，非“需求增加所以所有价格必涨”。

## rival_and_falsifier

|偏好机制/竞争解释|有区分力的证据或证伪|证据边界|
|---|---|---|
|belief修正 vs真实技术改善|同硬件版本、道路能耗不变、标签变化；先验/后验真实费用的直接测量|同车名不等于同硬件；只有注册标签不能证明消费者接触|
|belief变化 vs共同燃油偏好变化|信息随机化/分期展示、事前先验偏差×信息处理的反应，以及价格/税补恒定的对照|单一聚合油耗系数变化不区分两者|
|低资本化 vs里程/折现/寿命/转售|外部实际里程、持有期、预期价格与二手残值；在多组合理校准下仍低资本化|未外部锚定乘积时不可命名短视|
|信任 vs注意/渠道暴露|信息是否被看到、内容回忆、主观精度/可信度、来源随机化|搜索热度不是信任测量，销量不是awareness测量|
|标签信息 vs税补/准入/供给|选择门槛/净价格/上架变化明确不动的机械重标样本；政策异质性与安慰剂时点|控制当前成交价可能截断均衡中介，要报告总效应与固定价不同估计对象|
|需求提高 vs创新|事前技术暴露、研发/申请及授权时序、效率/密度的真实进步且非分类变化|市场份额、专利数或容量上升各自均不足以证明创新机制|

负控包括未重标/未展示车型、政策前伪切换、非相关属性、同硬件不变的道路效率；不能把不显著安慰剂写成证明无混杂。能否因果识别仍由政策与识别代理审定。

## handoff

交识别代理：确认M/静态风险集、展示而非法规处理、同硬件连接、价税映射、供给所有权、参数乘积的外部锚、IV与微观矩的秩/排除。交政策代理：核对认证/展示/税补/准入各时间线。交数据代理：确认真实/标签/道路能耗单位、PHEV综合与分项、容量/电芯/包密度口径。交写作整合：只把条件替代机制写成理论预测；不能写成已识别的信任、短视、总福利或创新结论。

推荐先实现B阶段最小可识别需求，再逐层开放C/D/E；数值程序可复用作单元测试，不是生产估计器。

## confidence_and_limits

公式的概率、反演、矩阵转置与线性货币experienced福利推导置信度高；项目belief、usage、属性工程、定价和创新设定是明确的新增假设。现有聚合数据不识别这些全部原语，本文没有报告中国市场估计、因果结果或净福利符号。正文引用的五篇都保留其模型边界，不把Xing的conditional模型假装有outside或供给，不把P01干中学假装专利创新。

### 实际运行与literal证据

命令：

```powershell
python 'D:\codex\output\blp_skill_integration_20261008\memos\numerical_blp_checks.py'
```

**illustrative-only。** 第一次14项检查全部通过，增加隐函数均衡导数及首选/次选检查后再次实际运行，最终16/16通过，exit 0，stderr空。结果与脚本SHA保存在 `D:\codex\output\blp_skill_integration_20261008\memos\results.json`。这是合成数据公式检查，不是中国数据、校准参数建议或均衡唯一性证明。Monte Carlo固定seed=20261008、40万类型/Gumbel抽样；同一决策冲击用于experienced比较。

以下最终一次stdout原样收录（不是手动舍入摘要）：

```text
analytic_vs_finite_difference_linear: PASS {"max_abs_error": 3.19063872544767e-12, "step": 1e-05}
outside_adding_up_and_gross_substitution: PASS {"inside_shares": [0.16770557699773433, 0.1840131398141902, 0.19971435547695437, 0.19643892564383408], "max_column_sum": 5.204170427930421e-18, "outside_share": 0.25212800206728697}
local_diversion_including_outside: PASS {"from_ICE_to_outside_HEV_PHEV_BEV": [0.37183341305793227, 0.22509472004840805, 0.21494755772752747, 0.18812430916613201], "sum": 0.9999999999999998}
aggregate_not_representative_consumer: PASS {"individual_aggregation_error": 0.0, "maximum_derivative_gap": 0.0027562372521365078}
simultaneous_policy_derivative: PASS {"max_abs_error": 1.5785012186242398e-12, "share_response": [-0.021609658471064788, -0.015687837820542477, -0.049173017299591434, 0.006382182677412815, 0.0800883309137859]}
capitalization_mileage_belief_product_nonidentification: PASS {"max_probability_difference": 0.0, "parameter_sets": [[0.8, 1.25, 0.9], [1.0, 1.0, 0.9]]}
BLP_inversion_recovers_delta: PASS {"iterations": 58, "max_delta_error": 9.325873406851315e-14, "stop_tolerance": 1e-13}
nonlinear_income_price_jacobian: PASS {"max_asymmetry": 0.0006562942305645015, "max_fd_error": 3.2965817575725254e-12}
Bertrand_transpose_and_cost_recovery: PASS {"correct_FOC_residual": 1.3877787807814457e-17, "marginal_cost": [3.7695202024519965, 6.647188228985954, 11.775663775609004, 15.500295740591953], "markup": [8.230479797548004, 8.352811771014046, 6.224336224390995, 6.4997042594080465], "wrong_untransposed_FOC_residual": 0.0040710635440938114}
repriced_local_equilibrium: PASS {"equilibrium_prices": [11.851851137038825, 14.827398060415378, 18.166562853130348, 22.20208758165239], "max_FOC_residual": 2.2537527399890678e-14, "note": "A locally valid candidate, not a global uniqueness proof", "own_profit_Hessian_eigenvalues": [-0.05333468769099823, -0.033049410201357564, -0.023165162632115485, -0.016975004726755342], "solver_success": true}
implicit_equilibrium_derivative: PASS {"Fp_condition_number": 4.089487998388146, "max_abs_error": 7.028183590662707e-11, "price_response": [-0.14251748434312428, -0.16606700215710854, 0.1536476359563355, 0.18580494559750554]}
experienced_welfare_and_oracle_KL_identity: PASS {"decision_monetary_change": -0.3257754620403777, "experienced_monetary_change": 0.004041117667644268, "max_KL_identity_error": 7.22078646875346e-17, "note": "Bad news can lower decision logsum while correct information raises experienced welfare at fixed prices", "oracle_utility_gaps": [0.001770318605435417, 0.0007591775554987024, 0.00030391159981757454, 0.00011182509051499423]}
same_draw_selected_experience_Monte_Carlo: PASS {"abs_error": 3.928242037090288e-06, "analytic_change": 0.004041117667644268, "observations": 400000, "seed": 20261008, "simulation_change": 0.004037189425607178, "standard_error": 5.904185204603064e-05}
conditional_first_second_joint_same_type_integral: PASS {"joint_probability_sum": 1.0, "maximum_binomial_SE": 0.0004663995721369497, "note": "No outside; stipulated conditional buyer-type weights; not population weights or a claim about actual switching", "simulation_max_abs_error": 0.0005531326230596989, "wrong_product_of_integrals_gap": 0.008707124325749924}
income_effect_exact_exante_CV: PASS {"exact_CV": 0.1905539725522385, "local_MU_approximation": 0.1908066192582968, "note": "Correct beliefs; full outside income retained; ex-ante CV, not expected ex-post CV", "welfare_root_residual": 0.0}
energy_units_and_engineering_identity: PASS {"annual_PHEV_yuan": 3408.0, "battery_mass_kg": 300.0, "idealized_range_km": 400.0, "note": "No second addition of an already utility-factor-weighted PHEV fuel metric"}
SUMMARY: 16/16 checks passed; exit=0
```

来源检查的一个工具错误也保留：首次Python打印P02原文时，Windows默认GBK无法编码 `\u0338`，工具exit 1（`UnicodeEncodeError: 'gbk' codec can't encode character '\u0338'`）；加入 `sys.stdout.reconfigure(encoding='utf-8')` 后相同PDF关键页检查exit 0。该错误是终端编码，不是原文读取失败或数值检验失败。

### 自有产物绝对路径与验证口径

1. `D:\codex\output\blp_skill_integration_20261008\memos\blp_derivations.md`
2. `D:\codex\output\blp_skill_integration_20261008\memos\numerical_blp_checks.py`
3. `D:\codex\output\blp_skill_integration_20261008\memos\results.json`

提交前重开三文件；核对16项全部passed、exit0、stderr空、JSON中脚本hash匹配、本文stdout与JSON逐字一致。已修复写入时丢失的inline math开定界符，126对inline与23对display匹配。Markdown用Pandoc的 `markdown+tex_math_single_backslash` 实际解析至MathJax HTML流并丢弃stdout，exit0；未生成额外输出文件。这是解析检查，不是逐式TeX编译认证。

保留构建工具错误：首次Pandoc使用 `-o NUL` 在当前环境返回 `NUL: withFile: permission denied`、exit1；改为stdout管道 `| Out-Null` 后观察 `PANDOC_PARSE_EXIT=0`。没有把这个设备路径错误说成文件权限或项目构建失败。没有生成或修改本任务以外的角色文件。
