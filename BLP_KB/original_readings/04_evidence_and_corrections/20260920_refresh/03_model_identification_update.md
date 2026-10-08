# 信念增广 micro-BLP 与实际标签事件研究：模型与识别更新

## 1. 经济对象分解

令 \(j\) 为严格配置谱系，\(m\) 为市场，\(t\) 为月份，\(g(j)\in\{ICE,HEV,PHEV,BEV\}\) 为动力类型，\(c_{jt}\) 为标签所用工况。

真实道路状态写为：

\[
q^{\mathrm{true}}_{jmt}
=
\bigl(FC^{\mathrm{road}}_{jmt},
EC^{\mathrm{road}}_{jmt},
R^{\mathrm{effective}}_{jmt}\bigr).
\]

消费者看到的官方标签是：

\[
L_{jmt}^{c}
=g_c\!\left(q^{\mathrm{true}}_{jmt},d_{jmt}\right)
+\nu_{jmt}^{c},
\]

其中 \(d_{jmt}\) 是硬件、软件和测试设计，\(\nu\) 是测试/披露楔子。观察到的新旧工况差必须分解为：

\[
\Delta L_j^{\mathrm{obs}}
=
\Delta L_j^{\mathrm{mechanical}}
+
\Delta L_j^{\mathrm{engineering}}
+
\Delta L_j^{\mathrm{testing/disclosure}}.
\tag{1}
\]

只有第一项接近“纯口径换算”。

## 2. 标签、注意、理解、信任与信念

令 \(A_i\) 为是否注意，\(C_i\) 为理解/换算能力，\(T_i\) 为对标签的信任，\(\mathcal I\) 为其他信息。消费者对真实状态的后验是一个一般信念算子：

\[
\widehat q_{ijmt}
=
\mathcal B_i\!\left(
L_{jmt}^{c_{jt}},c_{jt},\mathcal I_{imt};
A_i,C_i,T_i
\right).
\tag{2}
\]

这里不能把 \(A_i,C_i,T_i\) 塞入未观察质量 \(\xi\)，也不能仅凭聚合销量分别识别它们。若需要一个便于估计的受限版本，可写：

\[
\widehat{PVOC}_{ijmt}
=
\omega_{ijmt}PVOC(L_{jmt}^{c_{jt}})
+(1-\omega_{ijmt})PVOC(B_{ijmt}),
\qquad 0\le\omega_{ijmt}\le1,
\tag{3}
\]

其中 \(\omega\) 是注意、理解与信任共同决定的标签权重，\(B_{ijmt}\) 是先验或其他道路信息。没有信息实验或调查矩时，应把 \(\omega\) 当成复合权重，不把它解释成某一种心理机制。

### 2.1 标签表示不变性基准

若新旧标签之间存在消费者已知的一一映射

\[
L_j^{new}=h(L_j^{old}),
\]

而且消费者用两种标签形成相同的真实道路后验：

\[
\mathcal B_i(L_j^{new},new,\mathcal I_i)
=
\mathcal B_i(L_j^{old},old,\mathcal I_i),
\tag{3a}
\]

则在价格、物理属性、选择集和其他政策不变时，纯粹换一种标尺不应改变选择概率。任何销量效应都必须由误解/低注意/低信任、信号精度变化、真实工程变化、供给响应或其他明确原语来解释。

## 3. 基准需求效用

建议的信念增广随机系数效用为：

\[
\begin{aligned}
u_{ijmt}
={}&x_{jmt}'\beta_i
+\zeta_{i,g(j)}
+\xi_{jmt}
-\alpha_i p_{jmt} \\
&-\alpha_i\phi_{i,g(j)}\widehat{PVOC}_{ijmt}
+\alpha_i\widehat{PVResale}_{ijmt} \\
&-\kappa_i
\mathcal A_i\!\left(
\widehat R_{ijmt},N_{mt}
\right)
+\varepsilon_{ijmt}.
\end{aligned}
\tag{4}
\]

其中：

- \(x_{jmt}\)：可观测车辆属性；
- \(\zeta\)：动力类型固有偏好，不能与成本或续航机制混称；
- \(\xi\)：消费者和研究者均未观察的产品质量；
- \(p\)：成交净价，而非只用指导价时不加说明；
- \(\phi\)：未来使用成本相对购车价的资本化程度；
- \(\widehat{PVOC}\)：主观预期使用成本现值；
- \(\widehat{PVResale}\)：主观预期残值现值；
- \(\mathcal A_i(\widehat R,N)\)：给定续航和充电网络 \(N\) 的预期出行缺口/续航不便；
- \(\kappa\)：续航不便的边际权重。

广义价格因此是：

\[
GC_{ijmt}
=p_{jmt}
+\phi_{i,g(j)}\widehat{PVOC}_{ijmt}
-\widehat{PVResale}_{ijmt}.
\tag{5}
\]

残值在基准中是广义价格的加性项，而不是自动改变 \(\alpha\)。

完全资本化基准为 \(\phi=1\)，但只有在信念、注意/理解/信任、里程、持有期、贴现率、能源价格和残值均被正确控制时，\(\phi<1\) 才能较强地解释为未来成本低估。否则识别的是复合资本化不足。

## 4. ICE、BEV 与 PHEV 的成本对象不能硬统一

ICE/HEV 的运行成本可由油耗、燃油价格、行驶里程、存活/持有期和贴现形成：

\[
PVOC_{ijmt}^{ICE}
=
\sum_{\tau=1}^{H_i}
\frac{
S_{i\tau}KM_{i\tau}\,
E_i[P^{fuel}_{m,t+\tau}]\,
FC_{ijmt}/100
}{(1+r_i)^\tau}.
\tag{6}
\]

BEV 的电力运行成本需要真实或可信电耗，而续航 \(R\) 另进入续航不便项。仅有标称续航时，不能把它机械换成 RMB/100km。

PHEV 必须允许电驱份额 \(\lambda\) 与两套能耗同时进入：

\[
PVOC_{ijmt}^{PHEV}
=
\sum_{\tau=1}^{H_i}
\frac{S_{i\tau}KM_{i\tau}}{(1+r_i)^\tau}
\left[
\lambda_{i\tau}P^{elec}_{m,t+\tau}EC_{ijmt}
+(1-\lambda_{i\tau})P^{fuel}_{m,t+\tau}FC_{ijmt}
\right].
\tag{7}
\]

若 \(\lambda\)、燃油消耗、电耗和纯电续航不完整，PHEV 应单独报告，不能用一个交互虚拟变量假装已经统一量纲。

## 5. 续航价值的微观基础

令 \(D_i\) 为出行需求，\(R\) 为消费者相信的有效续航：

\[
\mathcal A_i(R)=\mathbb E[(D_i-R)_+].
\tag{8}
\]

则：

\[
\frac{\partial \mathcal A_i}{\partial R}
=-\Pr(D_i>R),
\qquad
\frac{\partial^2\mathcal A_i}{\partial R^2}
=f_{D_i}(R)\ge0.
\tag{9}
\]

从式 (4) 得：

\[
\frac{\partial u_i}{\partial R}
=\kappa_i\Pr(D_i>R)>0,
\qquad
\frac{\partial^2u_i}{\partial R^2}
=-\kappa_i f_{D_i}(R)\le0.
\tag{10}
\]

这给出低续航区边际价值更高、长途需求异质性和充电网络降低续航边际价值的理论基础。经验估计可以用分段样条、单调样条或预期缺口模拟；不需要误引 P10 来证明续航曲率。

## 6. BLP 份额与可识别对象

给定类型分布 \(F(\theta_i,A_i,C_i,T_i,D_i)\)，模型份额为：

\[
s_{jmt}(\Theta)
=
\int
\Pr\!\left(
u_{ijmt}\ge u_{ikmt},\ \forall k\in\mathcal J_{mt}\cup\{0\}
\right)
dF_i.
\tag{11}
\]

outside option \(0\) 必须由潜在购车市场规模 \(M_{mt}\) 定义：

\[
s_{0mt}=1-\sum_{j\in\mathcal J_{mt}}\frac{q_{jmt}}{M_{mt}}.
\tag{12}
\]

把当月总销量当作 \(M_{mt}\) 会令 outside 恒为零，不能用于福利或市场扩张反事实。至少应对“不购新车”“购买二手车”“潜在换购家庭”三种边界做敏感性分析。

仅有全国车型销量和属性时，一般可识别的是标签、未来成本和动力偏好的**复合反应**。要把 \(\phi\)、\(\omega\)、注意、信任和认知分别识别，必须增加外生信息处理或微观矩。

### 6.1 BLP 分解、反演与需求矩

把效用写为：

\[
u_{ijmt}=\delta_{jmt}+\mu_{ijmt}+\varepsilon_{ijmt},
\tag{12a}
\]

其中 \(\delta\) 是平均效用，\(\mu\) 是消费者异质性。条件于模拟类型的选择概率为：

\[
P_{ijmt}
=
\frac{\exp(\delta_{jmt}+\mu_{ijmt})}
{1+\sum_{k\in\mathcal J_{mt}}\exp(\delta_{kmt}+\mu_{ikmt})}.
\tag{12b}
\]

给定非线性参数，可用标准 contraction 恢复平均效用：

\[
\delta^{(h+1)}_{jmt}
=
\delta^{(h)}_{jmt}
+\log s^{obs}_{jmt}
-\log s_{jmt}\!\left(\delta^{(h)},\theta_2\right).
\tag{12c}
\]

随后由线性部分得到 \(\xi_{jmt}(\theta)\)，用式 (13) 的工具矩估计。若存在大量真实零份额，需要更适合零值/小份额的处理；不能对零份额直接取对数后继续标准 contraction。

## 7. 微观矩与替代模式

优先矩包括：

1. 第一选择为 ICE/HEV/PHEV/BEV 时的第二选择动力和车型分布；
2. 不同收入、年行驶里程、持有期和长途出行频率人群的动力份额；
3. 标签阅读率、能否识别 NEDC/WLTC/CLTC、共同量纲换算误差和标签信任；
4. 改革前后对燃油成本、有效续航和残值的主观预期；
5. 城市油价、电价、充电条件和限购政策下的份额差异；
6. 购买与租赁/融资选择，以及残值担保使用。

P08 证明二选择矩对替代结构有价值，但不许可预先把动力类型固定成一个正确 nest。应比较随机系数、候选 nesting tree 和外部 diversion 的拟合。

## 8. 价格与属性内生性

需求矩为：

\[
\mathbb E[Z_{jmt}'\xi_{jmt}]=0.
\tag{13}
\]

候选 \(Z\) 包括：

- 与效用未观察质量正交的投入成本、税费、汇率、运输或供应商成本；
- BLP sums/differentiation IV，但必须检查弱工具和产品定位内生性；
- 同企业与竞争企业的预定产品特征，在重新论证排除限制后使用；
- 可信的法定阈值或外生资格变化。

禁止：

- 用标签本身作为价格 IV，因为标签直接进入消费者效用；
- 因为预测楔子使用改革前属性，就自动声称它排除了工程和产品定位路径；
- 直接移植 P02/P10 的工具而不重建中国场景中的排除限制。

## 9. 实际黄色标签事件研究

设 \(G_j\) 为消费者实际看到新黄色标签的首月。目标 group-time 效应为：

\[
ATT(g,t)
=
\mathbb E\!\left[
Y_{jt}(g)-Y_{jt}(\infty)
\mid G_j=g
\right].
\tag{14}
\]

再按事件时间 \(e=t-g\) 聚合 cohort-specific 效应。不要把传统 TWFE 中已处理车型当对照。

如果 \(G_j\) 由企业根据改款、库存和预期需求选择，则式 (14) 的因果解释需要：

\[
G_j\perp\{Y_{jt}(0),Y_{jt}(1)\}_t
\mid X_j,\alpha_j,\lambda_t,
\tag{15}
\]

以及 no anticipation、风险集可比和 cohort 条件平行趋势。条件不成立时，这一设计应称“实际采用事件关联”。

连续预定暴露 \(W_j^0\) 可写为：

\[
Y_{jt}
=\alpha_j+\lambda_t
+\sum_{e\ne-1}
\pi_e W_j^0\mathbf 1\{t-\tau^{law}=e\}
+X_{jt}'\gamma+\varepsilon_{jt}.
\tag{16}
\]

\(\pi_e\) 识别的是每单位预定暴露的差异化响应，要求不同 \(W_j^0\) 上的条件剂量平行趋势和共同支持；它不是“平均标签效应”，也没有自动生成未处理对照。

## 10. 事件研究与 BLP 的连接

两者承担不同任务：

- 事件研究检查销量/价格变化是否紧贴实际可见标签启用，并揭示预趋势、库存和改款风险；
- BLP 解释替代到 ICE、HEV、PHEV、BEV 还是 outside，并分解固定价格需求效应、重新定价和产品属性响应。

推荐先把事件研究作为外部验证。若要把 reduced-form 估计写成最小距离矩，必须联合处理同一数据产生的协方差：

\[
g^{RF}(\Theta)
=
\widehat\beta^{RF}
-\beta^{model}(\Theta),
\qquad
\widehat\Theta
=\arg\min_\Theta
g^{RF}(\Theta)'Wg^{RF}(\Theta).
\tag{17}
\]

不能一边用同一销量估计 BLP，一边把事件研究系数当独立外部矩而忽略重复使用数据。

## 11. 多产品 Bertrand 供给

企业 \(f\) 对其产品 \(j\in\mathcal J_f\) 的一阶条件是：

\[
s_j
+\sum_{r\in\mathcal J_f}
(p_r-mc_r)
\frac{\partial s_r}{\partial p_j}
=0.
\tag{18}
\]

定义：

\[
\Delta_{jr}
=
-\mathbf 1\{f(j)=f(r)\}
\frac{\partial s_r}{\partial p_j},
\tag{19}
\]

则在矩阵可逆和内点定价条件下：

\[
p-mc=\Delta^{-1}s.
\tag{20}
\]

P02 允许进一步让企业选择电池、重量、续航等属性，但这需要属性一阶条件、成本函数和额外工具。没有这些数据时，先做“冻结属性、允许重新定价”的短期反事实；再把内生属性作为有数据门槛的中期扩展。

若消费者支付价 \(p^c\) 与企业收到的价格 \(p^s\) 因税费、补贴或经销商返利而不同，利润 margin 应写为 \(p^s+b^s-mc\)，需求导数还要显式乘入 \(\partial p^c/\partial p^s\)。不能默认补贴一比一传递或用指导价代替成交价而不做敏感性分析。

## 12. 建议的反事实阶梯

1. **信息归一化**：所有消费者看到同一共同真实道路指标；隔离标签表示效应。
2. **完全理解/完全信任**：令标签权重或正确换算概率达到 1；比较信息摩擦损失。
3. **固定价格与固定产品集合**：只保留需求侧信念变化。
4. **允许 Bertrand 重新定价**：加入均衡价格反馈。
5. **允许属性适配和进入退出**：需要 P02 式供给识别。
6. **加入二手市场**：需要 P09 式数据和动态结构。
7. **加入电池学习或创新**：只有持续冲击和动态状态变量到位后，才启用 P01/P06。

每一层都应报告 ICE、HEV、PHEV、BEV、outside 的份额变化、消费者剩余、利润和适用的环境结果。真实道路排放福利还需要实际能耗和发电/燃油排放因子，不能由标签值直接代替。

对错误信念，必须区分：

- **决策福利**：以消费者当时相信的标签和成本计算选择效用；
- **体验福利**：保留消费者按决策效用作出的实际选择，再用真实道路能耗、真实续航不便和真实残值评价。

形式上，若

\[
j_i^*=\arg\max_j u_{ij}^{decision},
\]

则体验福利评价 \(u_{ij_i^*}^{experienced}\)。不能让消费者先按“真实效用”重新优化，再把那个新 logsum 冒充原政策下的体验福利。
