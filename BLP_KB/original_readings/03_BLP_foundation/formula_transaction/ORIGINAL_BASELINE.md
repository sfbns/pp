# Structural Foundations Note: User-Verified BLP Model Construction Walkthrough (2026-05-20)

## Identity
- domain: `structural_models`
- internal_card_id: `structural_foundation::blp_model_construction_walkthrough_2026-05-20`
- card_family: `foundation_note`
- internal_card_path: `D:\codex\economics_theory_agent_complete_gpt55_xhigh\kb\03_structural_models\foundations\01-user-verified-blp-model-construction-walkthrough-2026-05-20.md`
- curated_source_path: `D:\codex\economics_theory_agent_complete_gpt55_xhigh\notes\curated\blp_model_construction_walkthrough_2026-05-20.md`
- source_master_memory_path: `D:\codex\blp_structural_memory_2026-04-18\memories\blp_structural_enhanced_master_memory.md`

## Provenance And Reuse Rule
- provenance: user-supplied or manually curated structural note stored inside the package.
- evidence_level: user-reported formula recheck against the original PDF; not independently equation-by-equation reverified by the assistant in this writeback step.
- notation_policy: preserve the notation in this note for later BLP follow-up answers unless the user explicitly requests a different notation.
- reuse_scope: use this note before reopening paper-level memories when the user wants a from-scratch walkthrough of how the BLP model is built and estimated.

## Curated Note Body
# User-Verified BLP Model Construction Walkthrough (2026-05-20)

## Status
- provenance: user-supplied structural note
- evidence_basis: user reports having rechecked the key formulas against the original PDF
- notation_policy: keep this notation stable in later BLP follow-up answers unless the user explicitly requests a different notation
- purpose: explain how the paper builds the BLP model from consumer utility to the estimable GMM system

先给一句总纲：**BLP 不是一条公式，而是一整套结构模型流程**。它的主线是“异质消费者效用 -> 聚合成市场份额 -> 多产品厂商 Nash 定价 -> 用份额反演恢复未观测质量 -> 用 IV/GMM 和模拟估计参数”。

## 一、这篇文章到底想解决什么问题

作者要解决两个老大难。第一，简单 logit/聚合需求会给出很不真实的替代模式：谁和谁更像、谁是更近的替代品，这种信息会丢失。第二，价格是内生的：厂商看得见产品的“隐藏质量”，计量经济学家看不见，所以价格会和未观测需求冲击相关，直接回归会偏。整篇文章的 BLP 框架，就是围绕这两个问题搭出来的。

## 二、第一层：从“单个消费者怎么选车”开始

### 1. 原始效用函数（未编号）

[
U(\zeta_i,p_j,x_j,\xi_j;\theta).
]

这里每个字母都很重要：

- `i`：消费者；
- `j`：产品；
- `p_j`：价格；
- `x_j`：可观测特征；
- `\xi_j`：不可观测特征；
- `\zeta_i`：消费者类型；
- `\theta`：要估计的参数。

直觉上，这一步是在说：**消费者比较的是每个车型给自己的总效用。**

### 2. 选择集合 `A_j`

式 `(2.1)` 定义：

[
A_j=\left\{\zeta:U(\zeta,p_j,x_j,\xi_j;\theta)\ge U(\zeta,p_r,x_r,\xi_r;\theta),\ \text{for } r=0,1,\ldots,J\right\}.
]

意思是，`A_j` 是所有会选择产品 `j` 的消费者类型集合。这里 `r=0` 很关键，它表示 outside good，也就是“不买这些车，把钱花到别处去”。

### 3. 市场份额：把个体选择聚合起来

式 `(2.2)`：

[
s_j(p,x,\xi;\theta)=\int_{\zeta\in A_j} P_0(d\zeta).
]

这里 `P_0(d\zeta)` 是消费者特征分布。这个式子的意思很直白：**市场份额就是会选这个车的消费者占比。** 如果市场总消费者数是 `M`，那么产品 `j` 的市场需求量就是

[
M,s_j(p,x,\xi;\theta).
]

所以，BLP 的需求系统本质上就是：**先写个体效用，再对消费者异质性积分。**

## 三、第二层：先看一个“简单但不够好”的基准 logit

### 4. 简单可分离效用：式 `(2.3)`

[
U(\zeta_i,p_j,x_j,\xi_j;\theta)=x_j\beta-\alpha p_j+\xi_j+\epsilon_{ij}\equiv \delta_j+\epsilon_{ij},
]

其中

[
\delta_j=x_j\beta-\alpha p_j+\xi_j.
]

这时：

- `\beta`：产品特征的平均效用权重；
- `\alpha`：价格系数；
- `\epsilon_{ij}`：个体 idiosyncratic 偏好误差；
- `\delta_j`：平均效用。

你可以把它理解为：

- `x_j\beta`：车型的平均吸引力；
- `-\alpha p_j`：价格越高越不受欢迎；
- `\xi_j`：隐藏吸引力；
- `\epsilon_{ij}`：每个人自己的小偏好。

### 5. 简单 logit 的市场份额：式 `(2.4)`

在 `\epsilon_{ij}` 独立同分布时，市场份额可以写成一个概率积分：

[
s_j=\int_{\epsilon}\prod_{q\neq j} P(\delta_j-\delta_q+\epsilon),P(d\epsilon).
]

如果 `\epsilon` 服从极值分布，就会进一步得到标准 logit 的封闭形式。这个式子的含义是：产品 `j` 的份额，就是“它的效用打败所有其他产品”的概率。

### 6. 为什么这还不是 BLP

这种可分离结构会产生不合理的替代模式：**替代只取决于市场份额，不取决于产品特征相似性。** 它无法表达“更像的车互相替代更强”。这就是 BLP 必须引入随机系数的原因。

## 四、第三层：BLP 的核心第一步——随机系数需求

### 7. 随机系数效用：式 `(2.5)`

[
U(\zeta_i,p_j,x_j,\xi_j;\theta)
=
x_j\bar\beta-\alpha p_j+\xi_j+\sum_k \sigma_k x_{jk}\nu_{ik}+\epsilon_{ij}.
]

这里新增的核心部分是

[
\sum_k \sigma_k x_{jk}\nu_{ik}.
]

它表示：消费者 `i` 对第 `k` 个特征的偏好不是固定的，而是会因人而异。

每个符号的意思：

- `\bar\beta_k`：平均偏好；
- `\nu_{ik}`：消费者 `i` 的偏好偏离；
- `\sigma_k`：异质性强度；
- `x_{jk}`：产品 `j` 在特征 `k` 上的水平。

于是，产品特征 `x_{jk}` 的边际效用对消费者 `i` 来说变成了

[
\bar\beta_k+\sigma_k \nu_{ik}.
]

这句非常重要：**同一辆车，对不同消费者的吸引力不一样。**

### 8. 平均效用和个体偏离的分解

论文把效用拆成两部分：

[
\delta_j=x_j\bar\beta-\alpha p_j+\xi_j,
]

[
\mu_{ij}=\sum_k \sigma_k x_{jk}\nu_{ik}+\epsilon_{ij}.
]

解释：

- `\delta_j`：共同看到的平均吸引力；
- `\mu_{ij}`：个体相对平均值的偏离。

这正是 BLP 想要的替代结构：更像的车会对同类偏好人群形成更强替代。

## 五、第四层：作者真正估计的 BLP 需求——把收入显式放进来

### 9. Cobb-Douglas 型效用：式 `(2.6)`

[
U(\zeta_i,p_j,x_j,\xi_j;\theta)=(y_i-p_j)^\alpha G(x_j,\xi_j,\nu_i)e^{\epsilon(i,j)}.
]

这里的关键是：

- `y_i`：收入；
- `y_i-p_j`：买完车以后剩下的钱；
- `\alpha`：剩余收入的重要性；
- `G(\cdot)`：车的特征与消费者偏好的匹配部分。

经济含义是：**离散选择里嵌着“买完车剩下多少钱还能消费别的东西”这个连续选择影子。**

### 10. 对数化后的可估计形式：式 `(2.7a)` 和 `(2.7b)`

令 `u_{ij}=\log U_{ij}`，论文经验规格是：

[
u_{ij}
=
\alpha \log(y_i-p_j)+x_j\bar\beta+\xi_j+\sum_k \sigma_k x_{jk}\nu_{ik}+\epsilon_{ij},
\qquad j=1,\ldots,J,
]

外部选项是

[
u_{i0}
=
\alpha \log(y_i)+\xi_0+\sigma_0\nu_{i0}+\epsilon_{i0}.
]

这里：

- `u_{ij}`：消费者 `i` 买车 `j` 的对数效用；
- `u_{i0}`：outside good 的对数效用；
- `\xi_0`：outside good 的平均效用；
- `\sigma_0\nu_{i0}`：outside good 上的随机系数。

这一步允许“不买车”的吸引力在不同人群里显著不同。作者还特别说明，和产品特征交互的消费者特征写成

[
\nu_i=(y_i,\nu_{i1},\ldots,\nu_{iK}).
]

也就是说，**收入本身也是消费者异质性的一部分。**

## 六、第五层：为什么价格内生，为什么要“反演” `\xi_j`

如果厂商看得见 `\xi_j`，而计量经济学家看不见，那么高隐藏质量的车往往会定更高的价，所以 `p_j` 和 `\xi_j` 正相关。这和传统 simultaneity 问题是同一种逻辑。区别在于，这里的需求是非线性的离散选择聚合需求，所以不能只靠普通线性 IV 直接解决，必须先把观测到的市场份额、价格和特征翻译回未观测质量 `\xi_j`。这就是 Berry inversion，也就是后面 `(6.8)` 收缩映射那一步。

## 七、第六层：供给侧——多产品厂商的 Nash 定价

### 11. 边际成本方程：式 `(3.1)`

[
\ln(mc_j)=w_j\gamma+\omega_j.
]

这里：

- `mc_j`：边际成本；
- `w_j`：成本侧可观测变量；
- `\gamma`：成本参数；
- `\omega_j`：未观测成本冲击。

### 12. 多产品厂商利润：式 `(3.2)`

[
\Pi_f=\sum_{j\in\mathcal F_f}(p_j-mc_j)M s_j(p,x,\xi;\theta).
]

这里 `\mathcal F_f` 是厂商 `f` 生产的产品集合，`M s_j` 是销量。

### 13. 定价一阶条件：式 `(3.3)`

[
s_j(p,x,\xi;\theta)
+
\sum_{r\in \mathcal F_f}(p_r-mc_r)\frac{\partial s_r(p,x,\xi;\theta)}{\partial p_j}
=0.
]

这句是供给侧的灵魂：

- 第一项：涨价带来单位利润增加；
- 第二项：涨价会改变本厂所有产品销量，要把内部蚕食算进去。

### 14. 构造 `\Delta` 矩阵：式 `(3.4)`

[
\Delta_{jr}
=
\begin{cases}
-\dfrac{\partial s_r}{\partial p_j}, & \text{如果 } j,r \text{ 属于同一厂商},\\[6pt]
0, & \text{否则}.
\end{cases}
]

这一步把“是否同一厂商”编码进矩阵。

### 15. 向量形式、加价率和定价方程：式 `(3.5)`、`(3.6)`

一阶条件写成向量形式：

[
s(p,x,\xi;\theta)-\Delta(p,x,\xi;\theta)[p-mc]=0.
]

解出来：

[
p=mc+\Delta(p,x,\xi;\theta)^{-1}s(p,x,\xi;\theta).
]

于是定义加价率向量

[
b(p,x,\xi;\theta)\equiv \Delta(p,x,\xi;\theta)^{-1}s(p,x,\xi;\theta).
]

再把 `mc` 的式子代回去，得到可估计供给方程：

[
\ln\big(p-b(p,x,\xi;\theta)\big)=w\gamma+\omega.
]

这条式子非常重要，因为它告诉你：**只要知道需求参数，就能算需求导数、再算 `\Delta`、再算 markup，最后就能从价格里剥出边际成本。**

## 八、第七层：工具变量和识别

### 16. 正交条件：式 `(4.1)`

[
E[\xi_j|z]=E[\omega_j|z]=0,
\qquad
z_j=[x_j,w_j],\ z=[z_1,\ldots,z_J].
]

意思是：未观测需求冲击 `\xi_j` 和未观测成本冲击 `\omega_j`，在给定所有产品的可观测特征和成本变量之后，条件均值为零。注意这里**故意不把价格和数量放进条件集**，因为它们本来就是内生结果。

### 17. 为什么 BLP 的工具变量要用“竞争对手特征”

产品 `j` 的加价率不仅取决于它自己，也取决于同厂其他产品和 rival 产品的特征。所以，竞争对手产品特征会影响均衡价格，却不直接进入产品 `j` 的未观测质量 `\xi_j`。这就是 BLP 经典工具变量直觉。

### 18. 最优工具变量思想：式 `(5.7)`

[
H_j(z)
=
E\left[
\begin{pmatrix}
\partial \xi_j(\theta_0,s^0,P_0)/\partial\theta\\
\partial \omega_j(\theta_0,s^0,P_0)/\partial\theta
\end{pmatrix}
\Bigg| z
\right]T(z_j)
=
D_j(z)T(z_j).
]

直觉是：**如果某个观测点上，结构冲击对参数变化特别敏感，那这个观测点就应该给更高权重。**

### 19. 可操作的 BLP 工具变量基函数：式 `(5.8)`

对特征 `z_{jk}` 而言，用：

[
z_{jk},
\qquad
\sum_{r\neq j,\ r\in \mathcal F_f} z_{rk},
\qquad
\sum_{r\neq j,\ r\notin \mathcal F_f} z_{rk}.
]

这三项分别表示：

1. 自己的第 `k` 个特征；
2. 同一厂商其他产品在第 `k` 个特征上的总和；
3. 竞争厂商产品在第 `k` 个特征上的总和。

这就是后面常说的 BLP instruments 原型：**own characteristics, same-firm sum, rival-firm sum**。

## 九、第八层：GMM 估计量是怎么搭起来的

### 20. 冲击的条件协方差：式 `(5.1)`、`(5.2)`

论文先设

[
E\big[(\xi_j,\omega_j)'(\xi_j,\omega_j)\mid z\big]=\Omega(z_j),
]

再定义标准化矩阵 `T(z)` 满足

[
T(z)'T(z)=\Omega(z)^{-1}.
]

### 21. 总体矩条件与样本矩条件：式 `(5.3)`、`(5.4)`

总体矩条件：

[
G^J(\theta)
=
E\left[
H_j(z)T(z_j)
\begin{pmatrix}
\xi_j(\theta,s^0,P_0)\\
\omega_j(\theta,s^0,P_0)
\end{pmatrix}
\right].
]

样本对应物：

[
G_J(\theta;s^0,P_0)
=
\frac1J
\sum_{j=1}^J
H_j(z)T(z_j)
\begin{pmatrix}
\xi_j(\theta,s^0,P_0)\\
\omega_j(\theta,s^0,P_0)
\end{pmatrix}.
]

这表示：对每组候选参数 `\theta`，你都能恢复“为了匹配市场数据而必须存在的” `\xi` 和 `\omega`，再检查这些结构误差是否和工具变量正交。

### 22. 真正最小化的目标函数：式 `(5.5)`

因为我们实际看到的是样本市场份额 `s^n`，而不是真实总体份额 `s^0`；同时消费者分布 `P_0` 也要靠模拟逼近，所以真正最小化的是

[
\left|G_J(\theta;s^n,P_{ns})\right|.
]

这里：

- `s^n`：样本市场份额；
- `P_{ns}`：用 `ns` 次模拟得到的消费者分布经验近似。

### 23. 渐近方差：式 `(5.6)`

论文给出估计量的渐近协方差为

[
(\Gamma'\Gamma)^{-1}\Gamma'
\left(\sum_{i=1}^3 V_i\right)
\Gamma(\Gamma'\Gamma)^{-1},
]

其中：

- `\Gamma`：矩条件对参数的导数；
- `V_1`：产品特征抽样过程带来的方差；
- `V_2`：消费者抽样带来的方差；
- `V_3`：模拟误差带来的方差。

所以 BLP 的标准误不仅有通常抽样误差，还会受到**模拟误差**影响。

### 24. 面板数据版本：按车型聚合矩条件

由于同一车型跨年份的未观测项会相关，作者不是把每个车型-年份都当独立观测，而是把同一车型在不同年份的矩条件加总：

[
g_m(\theta)
\equiv
\sum_t
\big[(f_{mt}(z)'\otimes I_2)\big]
\begin{pmatrix}
\xi_{mt}(\theta)\\
\omega_{mt}(\theta)
\end{pmatrix}.
]

这里 `m` 是车型，`t` 是年份，`\otimes` 是 Kronecker 积。目的就是让标准误允许**同一车型跨期相关**。

## 十、第九层：真正的“BLP 算法”——怎么从市场份额反推出 `\delta`、`\xi`、`\omega`

### 25. 统一写法：式 `(6.1)`

[
u_{ij}
=
\delta(x_j,p_j,\xi_j,\theta_1)
+
\mu(x_j,p_j,\nu_i,\theta_2)
+
\epsilon_{ij}.
]

这几乎就是 BLP 的总结构：**平均效用 + 异质性偏离 + logit 误差**。

### 26. 先看 logit 特例：式 `(6.2)` 到 `(6.5)`

logit 特例中，设 `\mu_{ij}=0`，于是

[
\delta_j=x_j\beta-\alpha p_j+\xi_j.
]

市场份额有封闭式：

[
s_j(p,x,\xi,\theta,P_0)
=
\frac{e^{\delta_j}}{1+\sum_{j=1}^J e^{\delta_j}}.
]

于是可直接反演：

[
\delta_j=\ln(s_j)-\ln(s_0).
]

所以 demand shock 可写成

[
\xi(s^n,p,x,\theta,P_0)
=
\ln(s_j^n)-\ln(s_0^n)-x_j\beta+\alpha p_j.
]

这一步是 Berry inversion 的最简单版本：**观测到份额，就能反推出平均效用 `\delta_j`。**

### 27. 完整 BLP：条件选择概率先算，再对消费者类型积分

条件份额：式 `(6.6)`

[
f_j(\nu_i,\delta,p,x,\theta)
=
\frac{\exp\big[\delta_j+\mu(x_j,p_j,\nu_i,\theta_2)\big]}
{1+\sum_{j=1}^J \exp\big[\delta_j+\mu(x_j,p_j,\nu_i,\theta_2)\big]}.
]

无条件市场份额：式 `(6.7)`

[
s_j(p,x,\xi,\theta,P_0)
=
\int
f_j(\nu_i,\delta(x,p,\xi),p,x,\theta),P_0(d\nu).
]

简单说：

- 先问：给定某种收入和偏好的人，会怎么买？
- 再问：所有类型的人加总起来，市场份额是多少？

### 28. 为什么这里不能像 logit 那样直接反演

因为 `(6.7)` 没有封闭解，所以 `\delta` 不能像 `\ln s_j - \ln s_0` 那样一步写出来。于是 BLP 采用数值反演。

### 29. BLP 收缩映射：式 `(6.8)`

[
T(s,\theta,P)[\delta_j]
=
\delta_j+\ln(s_j)-\ln[s_j(p,x,\delta,P;\theta)].
]

如果把样本份额 `s^n` 代进去，就迭代：

[
\delta \leftarrow \delta+\ln(s^n)-\ln[s(p,x,\delta,P_{ns};\theta)].
]

直觉是：

- 如果当前参数和 `\delta` 下模型预测份额太低，就把 `\delta_j` 往上调；
- 如果模型预测份额太高，就把 `\delta_j` 往下调。

不断重复，直到模型预测份额和观测份额一致。

### 30. 为什么完整 BLP 中 `\xi_j=\delta_j-x_j\beta`

论文在这一部分写：

[
\xi_j(\theta,s,P)=\delta_j(\theta,s,P)-x_j\beta.
]

很多初学者会困惑：为什么这里没有 `+\alpha p_j`？原因是**在完整 BLP 规格中，价格不是线性地单独放在 `\delta_j` 里，而是通过 `\alpha\log(y_i-p_j)` 进入异质性部分。** 所以完整模型里 `\delta_j` 本质上是 `x_j\beta+\xi_j`，而价格已经跑到非线性部分去了。

### 31. 需求导数：式 `(6.9a)`、`(6.9b)`

为了构造供给侧的 `\Delta`，需要市场份额对价格的导数。论文给出：

[
\frac{\partial s_j}{\partial p_j}
=
\int
f_j(\nu,\delta,x,p,\theta)\big(1-f_j(\nu,\delta,x,p,\theta)\big)
\left[\frac{\partial \mu_{ij}}{\partial p_j}\right]
P_0(d\nu),
]

[
\frac{\partial s_j}{\partial p_q}
=
\int
-\,f_j(\nu,\delta,x,p,\theta)\,f_q(\nu,\delta,x,p,\theta)
\left[\frac{\partial \mu_{iq}}{\partial p_q}\right]
P_0(d\nu),
\qquad q\neq j.
]

own-price 导数是“自己被选中概率 × 不被选中概率 × 价格对效用的影响”；cross-price 导数是“两个产品被共同比较的概率项 × 价格变动对相对效用的影响”，积分号内带负号。

**2026-10-07 更正（Claude 对原页 journal p.865 核过）。** 原页 (6.9b) 在积分号内印有前置负号，本稿旧版漏抄，现已补回。原页同式另有两处印刷笔误，本稿按经济含义改写。其一，原页第一个因子印作 `f_j(\nu,\xi,x,p,\theta)`，应为 `f_j(\nu,\delta,x,p,\theta)`，与 (6.9a) 及其余各式一致。其二，原页印作 `\partial\mu_{ij}/\partial p_q`，但 `q\neq j` 时 `\mu_{ij}` 不含 `p_q`，照抄会得零，应为 `\partial\mu_{iq}/\partial p_q`。在 BLP 规格 `\mu_{iq}=\alpha\log(y_i-p_q)+\dots` 下 `\partial\mu_{iq}/\partial p_q=-\alpha/(y_i-p_q)<0`，与前置负号相抵，替代品的交叉导数为正。漏掉负号会让 `\Delta` 的非对角元反号，markup、边际成本与福利随之全错。核验记录见 `D:\blp-structural-skill-config\VERIFICATION_LEDGER.md` 的 A3、A4 两条。

## 十一、第十层：模拟——因为积分算不动，所以用 Monte Carlo

### 32. 最简单模拟器：式 `(6.10)`

如果从 `P_0` 抽 `ns` 个消费者类型 `(\nu_1,\ldots,\nu_{ns})`，就可以用样本平均近似积分：

[
s_j(p,x,\xi,\theta,P_{ns})
\equiv
\frac1{ns}\sum_{i=1}^{ns} f_j(\nu_i,\delta,p,x,\theta).
]

这就是模拟市场份额。

### 33. 重要性抽样：式 `(6.11)` 到 `(6.13)`

作者进一步说，可以用 importance sampling 降低模拟方差。核心想法是：别平均地抽所有人，而要**更频繁地抽那些更可能买车的人**。

理想抽样分布是

[
P^*_{h_j}(dv,\theta)
=
\frac{f_j(v,\theta)p_0(v),dv}{s_j(\theta,P_0)}.
]

但这个“最优”分布没法直接用，因为它本身依赖未知的 `s_j(\theta,P_0)`。

于是作者先用一个初步一致估计 `\theta'` 来近似，并定义所有“买某辆车”的总概率：

[
\bar s(\theta)=1-s_0(\theta)=\sum_{j=1}^J s_j,
\qquad
\bar f(\nu,\theta')=\sum_{j=1}^J f_j(\nu,\theta').
]

然后得到加权模拟器：

[
s_j[\theta,P_h^*(\theta')_{ns}]
=
\sum_{i=1}^{ns}
\frac{\bar s(\theta',P_0)}{\bar f(\nu_i,\theta')}
f_j(\nu_i,\theta),
]

意思是：**过度抽样可能买车的人，再用权重校正回来。**

## 十二、第十一层：论文最终实际估计的经验规格

### 35. 最终效用式：式 `(6.14a)`、`(6.14b)`

[
u_{ijt}
=
\alpha \ln\!\big(e^{m_t+\sigma_y\nu_{iy}}-p_{jt}\big)
+
x_{jt}\bar\beta
+
\xi_{jt}
+
\sum_k \sigma_k x_{kjt}\nu_{ik}
+
\epsilon_{ijt},
]

[
u_{i0t}
=
\alpha \ln\!\big(e^{m_t+\sigma_y\nu_{iy}}\big)
+
\xi_{0t}
+
\sigma_0\nu_{i0}
+
\epsilon_{i0t}.
]

这里：

- `t`：年份；
- `m_t`、`\sigma_y`：当年收入分布参数；
- `e^{m_t+\sigma_y\nu_{iy}}`：把标准正态抽样变成对数正态收入；
- `x_{jt}`：当年车型特征；
- `\sigma_k`：特征偏好异质性强度。

这说明论文不是凭空假设收入分布，而是把外部数据直接喂进消费者异质性分布。

### 36. 最后怎么最小化：第 6.5 节

对于给定的 `(\alpha,\sigma)`，一阶条件对 `(\beta,\gamma)` 是线性的，所以可以把 `(\beta,\gamma)` concentrate out，只对非线性参数 `(\alpha,\sigma)` 做数值搜索。真正难找的是随机系数和收入项这些非线性参数；线性的那部分能在每一步顺手解掉。

## 十三、附录 I：为什么 `(6.8)` 一直迭代真的会收敛

作者在附录 I 证明，`(6.8)` 定义的映射是 contraction mapping。证明里最关键的两条导数公式是：

[
\frac{\partial f_j(\delta)}{\partial \delta_j}
=
1-\frac{1}{s_j}\frac{\partial s_j}{\partial \delta_j},
\qquad
\frac{\partial f_j(\delta)}{\partial \delta_k}
=
-\frac{1}{s_j}\frac{\partial s_j}{\partial \delta_k},
\quad k\neq j.
]

再利用市场份额函数的性质，可以证明这个映射的导数行和小于 1，所以它是压缩映射，固定点唯一。

作者还把市场份额写成

[
s_j(\delta)=e^{\delta_j}D_j(\delta),
]

其中

[
D_j(\delta)
=
\int
\frac{e^{\mu_i}}{1+\sum_k e^{\delta_k+\mu_i}}
,d\Phi(\mu).
]

对实务上最重要的一句是：**BLP 反演不是拍脑袋迭代，而是有严格数学保证的。**

## 十四、把整篇文章压成一句“实证操作流程”

如果以后自己做 BLP，实操上就是这 7 步：

1. 选好需求特征 `x_j`、成本特征 `w_j`、厂商归属 `\mathcal F_f`；
2. 给定消费者异质性分布 `P_0`；
3. 猜一组非线性参数 `(\alpha,\sigma)`；
4. 用收缩映射 `(6.8)` 从观测市场份额反推出 `\delta`；
5. 从 `\delta` 得到需求冲击 `\xi`，再利用需求导数和供给方程得到 markup 与成本冲击 `\omega`；
6. 用 `\xi,\omega` 和工具变量构造 GMM 矩条件；
7. 更新参数直到矩条件尽可能接近 0。

## 十五、最应该记住的 5 个关键词

第一，`\delta_j`：平均效用。  
第二，`\mu_{ij}`：个体异质性偏离。  
第三，`\xi_j`：未观测产品质量，是价格内生的根源。  
第四，`\Delta^{-1}s`：由需求导数推出来的 markup。  
第五，`\delta \leftarrow \delta+\ln s^{obs}-\ln s^{model}`：BLP 反演的核心。

最简洁地说，**BLP 模型 = 随机系数离散选择需求 + Berry 份额反演 + 多产品 Nash 定价 + IV/GMM + 模拟积分**。
