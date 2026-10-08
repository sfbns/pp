# Xing–Leard–Li (2021)：BLP需求、首选—次选矩的公式校核

原文PDF8式(12)已视觉核验；33/33页全文补证及原文内部不一致见04文件夹。

## 1. source-exact：保留对数价格
\[
u_{ij}=\sum_{k=1}^K x_{jk}\beta_k-\alpha_1\ln p_j+\xi_j
+\alpha_2\frac{\ln p_j}{Y_i}
+\sum_{kr}x_{jk}z_{ir}\beta^o_{kr}
+\sum_kx_{jk}v_{ik}\beta^u_k+\varepsilon_{ij}.
\]
不能把ln(p)随手改成p。该文条件于新车购买；没有outside option，且不估供给。BLP需求侧不是完整需求供给均衡。

## 2. standard-derived：同一类型下的首选—次选概率
令v_ij为上式非epsilon部分；其正确混合概率对象是
\[
\Pr(j,h\mid d_i)=\int
\frac{e^{v_{ij}}}{\sum_{k\in J}e^{v_{ik}}}
\frac{e^{v_{ih}}}{\sum_{k\in J\setminus\{j\}}e^{v_{ik}}}
\,dF(\nu_i\mid d_i),\quad h\ne j.
\]
必须先在同一消费者draw下相乘，再积分；一般不等于两个边际积分之积。
本轮核到附录D与正文式(13)在outside分母及混合概率的log分解上有不一致；保留原PDF不改。不能由排版问题断言原作者代码错。
conditional市场反演需基准效用归一化；导数一般须完整归一化Jacobian，不可仅逆每个对角元素。
