# GRV (2018)：未来燃油成本资本化的 BLP 模型公式校核

范围：模型核心与解释修订，不是整篇中文翻译逐式认证。原文PDF6–8／期刊198–200已回源视觉核对；本轮全文阅读记录见04文件夹。

## 1. source-exact：效用与燃油成本
\[
u_{ijk}=x_{jk}\beta_i^x-\alpha_i(p_{jk}+\gamma G_{ijk})+\xi_{jk}+\varepsilon_{ijk}.
\]
\[
G_{ijk}=\mathbb E\!\left[\sum_{s=1}^{S}(1+r)^{-s}\beta_i^m e_{jk}g_{ks}\right].
\]
在原文的能源价格预期限制下：
\[
G_{ijk}=\rho\beta_i^m e_{jk}g_k,\qquad
u_{ijk}=x_{jk}\beta_i^x-\alpha_i(p_{jk}+\gamma\rho\beta_i^m e_{jk}g_k)+\xi_{jk}+\varepsilon_{ijk}.
\]
这里e是L/km；若中国数据是L/100km，必须除以100。beta_i^m是行驶里程，不是油耗偏好。

## 2. 校正解释
gamma=1是给定里程、贴现与寿命基准下完全资本化；gamma、rho与里程尺度不能同时任意估计。
不要把旧卡“约0.91”写成已经证明普遍短视：原文不能拒绝正确估值。它是研究短视/资本化的BLP母本，不是先验后验学习模型。
表5为模型比较固定gamma=1；福利讨论的部分计算采用完全竞争简化，不能把所有表都叫统一Bertrand+估计gamma结果。

项目用途：把标签影响写入主观预期燃油成本，再考虑资本化；不能把误信和短视混为一体。
