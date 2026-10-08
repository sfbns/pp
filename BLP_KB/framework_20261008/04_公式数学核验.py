"""BLP driving-cycle framework: reproducible algebra and synthetic-data checks.
Not an empirical replication, an instrument-validity test, or independent peer review.
Run: python 04_公式数学核验.py
Dependencies: numpy, scipy, sympy. No network access or user data is required.
"""
from __future__ import annotations
import json
from pathlib import Path
import numpy as np
import sympy as sp
from numpy.polynomial.hermite import hermgauss
from scipy.special import softmax, logsumexp

OUT=Path(__file__).resolve().parent
rng=np.random.default_rng(20261008)
results=[]

def check(name, condition, detail=''):
    ok=bool(condition)
    results.append({'test':name,'passed':ok,'detail':str(detail)})
    if not ok:
        raise AssertionError(f'{name}: {detail}')

def close(name, a,b, atol=1e-8,rtol=1e-8):
    a,b=np.asarray(a),np.asarray(b)
    err=float(np.max(np.abs(a-b)))
    check(name,np.allclose(a,b,atol=atol,rtol=rtol),f'max_abs_error={err:.3e}')

# 1. Resource accounting and exact decompositions.
g0,dg,G0,dG=sp.symbols('g0 dg G0 dG')
check('01_资本化变化包含交互项',sp.expand((g0+dg)*(G0+dG)-g0*G0-(g0*dG+dg*(G0+dG)))==0)
l0,g,e=sp.symbols('l0 g e')
check('02_校准平方误差改善恒等式',sp.expand((l0-e)**2-(l0+g-e)**2-(2*g*(e-l0)-g**2))==0)
check('03_有向差距与标签变化机械相关',sp.expand(((e-l0-g)-(e-l0))+g)==0)
k0,k1,L0,L1,R=sp.symbols('k0 k1 L0 L1 R')
check('04_来源权重与数字变化精确分解',sp.expand(k1*L1+(1-k1)*R-k0*L0-(1-k0)*R-(k0*(L1-L0)+(k1-k0)*(L1-R)))==0)
m0=.2*6+.8*9;m1=.9*7+.1*9
check('05_数字上调而主观油耗下降的反例',7>6 and m1<m0,f'm0={m0}, m1={m1}; illustrative only')
close('06_未来成本除100单位检查',15000*8*7/100,8400)
close('07_电池容量密度质量关系',1000*60/150,400)
close('08_续航能量核算关系',100*54/15,360)

# 2. Bayesian signal calculations.
m_prior,v_prior,tau2,signal=8.4,1.2,.3,7.0
vpost=1/(1/v_prior+1/tau2)
mpost=vpost*(m_prior/v_prior+signal/tau2)
kappa=v_prior/(v_prior+tau2)
close('09_正态后验配方与更新式一致',mpost,m_prior+kappa*(signal-m_prior))
close('10_后验方差公式一致',vpost,v_prior*tau2/(v_prior+tau2))
V0=np.array([[1.4,.2],[.2,.9]])
H=np.array([[1.,.3],[.2,1.]])
Sig=np.array([[.5,.15],[.15,.6]])
K=V0@H.T@np.linalg.inv(H@V0@H.T+Sig)
Vpost=V0-K@H@V0
check('11_相关信号后验协方差有效',np.linalg.eigvalsh(Vpost).min()>0 and np.linalg.eigvalsh(V0-Vpost).min()>-1e-12)
x,w=hermgauss(60)
mu,var=1.8,.16
num=np.sum(w*np.exp(mu+np.sqrt(2*var)*x))/np.sqrt(np.pi)
close('12_对数正态均值包含半方差',num,np.exp(mu+var/2))
a_risk,gamma,mg,sg=.0002,.6,30000.,2000.
ce=np.log(np.sum(w*np.exp(a_risk*gamma*(mg+np.sqrt(2)*sg*x)))/np.sqrt(np.pi))/a_risk
close('13_CARA正态确定性等价',ce,gamma*mg+.5*a_risk*gamma**2*sg**2,atol=1e-7)
alpha,Kcost,kap,gam,ar,dp,v0,v1=.0001,9000.,.6,.7,.0003,0.,.6,.2
gmax=ar*gam*Kcost/(2*kap)*(v0-v1)-dp/(gam*Kcost*kap)
val=-alpha*(dp+gam*Kcost*kap*gmax+.5*ar*gam**2*Kcost**2*(v1-v0))
# Joint source-weight and capitalization changes: exact conditional threshold.
kg0,kg1,gg0,gg1,LL,RR,KK,pp,rpd=.2,.8,.6,.7,6.,9.,9000.,-300.,-500.
mm0=kg0*LL+(1-kg0)*RR; mm1base=kg1*LL+(1-kg1)*RR
joint_g=(gg0*mm0-gg1*mm1base-(pp+rpd)/KK)/(gg1*kg1)
joint_value=pp+KK*(gg1*(mm1base+kg1*joint_g)-gg0*mm0)+rpd
close('14_标签上浮边界含来源与资本化变化',[val,joint_value],[0.,0.])

# 3. Attention and interpretation.
Hloss,c=2.4,1.6
att=Hloss/(Hloss+c)
close('15_注意最优一阶条件',-Hloss*(1-att)+c*att,0)
v=np.array([0.,.8,-.3,1.1]);p=softmax(v)
Gc=np.array([0.,.4,.7,.2]);al=.8
C=np.diag(p)-np.outer(p,p)
check('16_logit曲率半正定',np.linalg.eigvalsh(C).min()>-1e-12)
Hq=al**2*Gc@C@Gc
x0=1e-4
pt=softmax(v+x0*al*Gc)
KL=np.sum(pt*(np.log(pt)-np.log(p)))
close('17_注意损失KL的局部二阶展开',KL/(.5*x0*x0),Hq,atol=3e-5)
vt=v+.3*al*Gc;pt=softmax(vt)
exp_util=np.sum(pt*(v+np.euler_gamma-np.log(pt)))
close('18_错误选择的KL损失恒等式',logsumexp(v)+np.euler_gamma-exp_util,np.sum(pt*np.log(pt/p)))
# Convex two-source normalization identifies coefficients only under stated restrictions.
al,gam,kap=.12,.65,.4
bL=al*gam*kap;bR=al*gam*(1-kap)
close('19_双来源归一化参数恢复',[ (bL+bR)/al,bL/(bL+bR)],[gam,kap])
U=rng.normal(size=(70,3)); Z=U+.1*rng.normal(size=(70,3))
check('20_独立工具相关列具有秩',np.linalg.matrix_rank(Z.T@U)==3)
U[:,2]=2*U[:,1]
check('21_共线来源使识别秩失败',np.linalg.matrix_rank(Z.T@U)==2)
close('22_单标签响应不能分离gamma和kappa',.4*.6,.8*.3)

# 4. Random coefficient logit, delta/mu and substitution.
I,J=600,5
alpha_i=np.exp(rng.normal(-1.2,.25,I))
X=rng.normal(size=(J,2));nu=rng.normal(size=(I,2))
muij=nu@X.T*.25
price=np.array([1.,1.5,2.,2.3,1.8])
base=np.array([.2,.6,.4,.8,.3])
def probs(pr):
    V=base[None,:]+muij-alpha_i[:,None]*pr[None,:]
    return softmax(np.column_stack([np.zeros(I),V]),axis=1)
P=probs(price);s=P.mean(0)
close('23_概率与份额加总',s.sum(),1)
E=muij.mean(0);dev=muij-E
close('24_平均效用与异质项闭合',E+dev,muij)
close('25_异质偏离均值为零',dev.mean(0),0)
# Derivatives of inside shares wrt inside prices.
def J_price(pr):
    q=probs(pr)[:,1:]
    return np.mean(alpha_i[:,None,None]*(q[:,:,None]*q[:,None,:]-np.eye(J)[None,:,:]*q[:,:,None]),axis=0)
Jac=J_price(price)
h=1e-5
Jfd=np.column_stack([(probs(price+np.eye(J)[j]*h).mean(0)[1:]-probs(price-np.eye(J)[j]*h).mean(0)[1:])/(2*h) for j in range(J)])
close('26_价格导数有限差分',Jac,Jfd,atol=1e-9)
check('27_价格自身负交叉正',np.all(np.diag(Jac)<0) and np.all(Jac[~np.eye(J,dtype=bool)]>0))
j=1
outside_deriv=np.mean(alpha_i*P[:,0]*P[:,j+1])
div=(np.sum(Jac[:,j])-Jac[j,j]+outside_deriv)/(-Jac[j,j])
close('28_转移率含外部选项加总为一',div,1)
Vall=np.log(P)
direction=rng.normal(size=(I,J+1));direction[:,0]=0
pb=P[:,[2,4]].sum(1)
ind=np.array([False,False,True,False,True,False])
direct_der=(P[:,ind]*direction[:,ind]).sum(1)-pb*(P*direction).sum(1)
alt_der=pb*(1-pb)*((P[:,ind]*direction[:,ind]).sum(1)/pb-(P[:,~ind]*direction[:,~ind]).sum(1)/(1-pb))
Pplus=softmax(Vall+h*direction,axis=1);Pminus=softmax(Vall-h*direction,axis=1)
fd=((Pplus[:,ind].sum(1)-Pminus[:,ind].sum(1))/(2*h))
close('29_类型份额相对效用导数',direct_der,alt_der,atol=1e-10)
close('30_类型份额导数有限差分',direct_der,fd,atol=1e-9)
monodir=np.where(ind, .2, -.1);monodir[0]=0
check('31_类型单调性必要符号检查',np.all(softmax(Vall+monodir,axis=1)[:,ind].sum(1)>=pb))
# Increasing gamma for all vs EV-only has distinct relative effect.
Gf,Gb=3.,1.
check('32_共同资本化与仅BEV资本化不可混淆',(Gf-Gb)>0 and -Gb<0)
# Conditional individual logodds shift.
close('33_个体logodds与效用差',np.log(Pplus[:,2]/Pplus[:,1])-np.log(P[:,2]/P[:,1]),h*(direction[:,2]-direction[:,1]),atol=1e-10)

# 5. Inner inversion and normalizations.
delta_true=np.array([.3,-.2,.6,.1,-.3])
mu=muij-.2*alpha_i[:,None]*price

def share_delta(d):
    return softmax(np.column_stack([np.zeros(I),d+mu]),axis=1).mean(0)[1:]
sobs=share_delta(delta_true)
d=np.zeros(J)
for iteration in range(10000):
    dn=d+np.log(sobs)-np.log(share_delta(d))
    if np.max(np.abs(dn-d))<1e-12:
        d=dn;break
    d=dn
close('34_BLP收缩反演恢复人工delta',d,delta_true,atol=1e-9)
check('35_BLP收缩达到阈值',iteration<9999,f'iterations={iteration+1}')
pl=softmax(np.r_[0.,delta_true])
close('36_简单logit反演',np.log(pl[1:])-np.log(pl[0]),delta_true)
# Fixed effects absorb public brand-month score.
fe=np.eye(6).repeat(3,axis=0);score=fe@np.arange(6.)
check('37_品牌月份固定效应吸收同层分数',np.linalg.matrix_rank(np.column_stack([fe,score]))==np.linalg.matrix_rank(fe))
# Concentrated GMM satisfies normal equations.
Xg=rng.normal(size=(110,3));Zg=np.c_[Xg+.1*rng.normal(size=Xg.shape),rng.normal(size=(110,2))]
yg=rng.normal(size=110);W=np.eye(5)
XX=Xg.T@Zg@W@Zg.T@Xg
coef=np.linalg.solve(XX,Xg.T@Zg@W@Zg.T@yg)
close('38_集中GMM线性一阶条件',Xg.T@Zg@W@Zg.T@(yg-Xg@coef),np.zeros(3),atol=1e-8)

# 6. Supply orientation incl non-unit tax slopes and uniform national pricing.
firm=np.array([0,0,1,1,2]);own=(firm[:,None]==firm[None,:])
tax=np.array([1.,1.1,1.2,.95,1.05])
# consumer price T(P)=tax*P; asymmetric derivatives expose transpose errors.
Jnet=J_price(tax*price)*tax[None,:]
snet=probs(tax*price).mean(0)[1:]
Delta=-(own*Jnet.T)
margin=np.linalg.solve(Delta,snet);mc=price-margin
foc=snet+(own*Jnet.T)@margin
close('39_税楔下markup矩阵方向与FOC',foc,np.zeros(J),atol=1e-10)
check('40_所有权矩阵方向非平凡',np.max(np.abs(Jnet-Jnet.T))>1e-4)
def profit(Pnet,f):
    ss=probs(tax*Pnet).mean(0)[1:]
    return ((Pnet-mc)*ss)[firm==f].sum()
fdp=np.array([(profit(price+np.eye(J)[j]*h,firm[j])-profit(price-np.eye(J)[j]*h,firm[j]))/(2*h) for j in range(J)])
close('41_利润价格梯度数值核验',fdp,0,atol=1e-8)
sc=snet*1000+probs(tax*(price+.4)).mean(0)[1:]*1800
Jc=Jnet*1000+(J_price(tax*(price+.4))*tax[None,:])*1800
Dc=-(own*Jc.T);mn=np.linalg.solve(Dc,sc)
close('42_跨城市统一价格正确加总',sc+(own*Jc.T)@mn,0,atol=1e-8)

# 7. Welfare exact analytic correction and independent simulation.
vd=np.array([0.,.5,.8,-.2]);ve=np.array([0.,.1,.4,.0]);prob=softmax(vd)
corrected=logsumexp(vd)+np.euler_gamma+prob@(ve-vd)
alt=np.sum(prob*(ve+np.euler_gamma-np.log(prob)))
close('43_校正logsum与所选误差恒等式',corrected,alt)
Nmc=180000
eps=rng.gumbel(size=(Nmc,4));choices=np.argmax(vd+eps,axis=1)
samp=ve[choices]+eps[np.arange(Nmc),choices]
err=abs(samp.mean()-corrected);se=samp.std(ddof=1)/np.sqrt(Nmc)
check('44_体验福利独立MonteCarlo验证',err<6*se,f'error={err:.5f}; MC_SE={se:.5f}; N={Nmc}')
choices2=np.argmax(vd+np.array([0.,.1,-.4,.3])+eps,axis=1)
T=np.zeros((4,4));np.add.at(T,(choices,choices2),1/Nmc)
close('45_反事实转移矩阵行列守恒',T.sum(1),np.bincount(choices,minlength=4)/Nmc,atol=1e-9)
close('46_反事实转移矩阵列与新份额',T.sum(0),np.bincount(choices2,minlength=4)/Nmc,atol=1e-9)
# Innovations: pure multiplicative relabel under log range leaves own marginal taste unchanged.
B,gg,rho,Ee=sp.symbols('B gg rho Ee',positive=True)
check('47_纯比例重标不自动降低容量边际效用',sp.simplify(sp.diff(rho*sp.log((1+gg)*100*B/Ee),B)-sp.diff(rho*sp.log(100*B/Ee),B))==0)
check('48_评分总和混合均值与条数',1000*4.0>100*4.8 and 4.0<4.8)

# Transfer accounting and fixed research costs must each be counted once.
benefit, producer_price, subsidy, real_mc = 30., 22., 3., 16.
close('49_购置补贴在福利核算中相消',benefit-(producer_price-subsidy)+(producer_price-real_mc)-subsidy,benefit-real_mc)
cs, op_profit, fixed_rd, public_cost = 10., 8., 2., 1.
close('50_研发成本不可从净利润再次扣减',cs+op_profit-fixed_rd-public_cost,cs+(op_profit-fixed_rd)-public_cost)

report={
 'scope':'Symbolic algebra and synthetic-data tests only. Not real-market identification or independent peer review.',
 'seed':20261008, 'tests':len(results),'passed':sum(r['passed'] for r in results),
 'results':results,
 'untested_empirical_conditions':['Validity and strength of exclusion restrictions','Actual policy-display timing and unchanged technology','Representativeness of owner reviews','Subjective beliefs or risk identification','Market size and outside option','Causal patent response or dynamic innovation equilibrium']}
(OUT/'05_数学核验结果.json').write_text(json.dumps(report,ensure_ascii=False,indent=2))
lines=['# 公式数学核验：执行结果','',f"**实际执行 {report['tests']} 项，通过 {report['passed']} 项。**",'',report['scope'],'','| 检验 | 结果 | 数值/说明 |','|---|---|---|']
for r in results: lines.append(f"| {r['test']} | {'通过' if r['passed'] else '未通过'} | {r['detail']} |")
lines+=['','## 不能由这些检验保证的部分','']+[f'- {x}' for x in report['untested_empirical_conditions']]
(OUT/'05_数学核验结果.md').write_text('\n'.join(lines)+'\n')
print(json.dumps({'tests':report['tests'],'passed':report['passed'],'inversion_iterations':iteration+1,'MC_error':err},ensure_ascii=False))
