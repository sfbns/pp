"""Independent standard algebra examples for production regression guards.
No Chinese estimates, no claim to certify an original paper's theorem.
"""
import numpy as np
from scipy.optimize import brentq
from scipy.special import expit

def main():
    # Strictly log-concave q(p)=exp(-p^2), declining but positive marginal cost.
    p=1.;q=np.exp(-p*p);qp=-2*p*q;qpp=(4*p*p-2)*q
    cprime=-1.;c0=.5+q
    denominator=2-q*qpp/(qp*qp)-cprime*qp
    analytic=1/denominator
    def foc(price,shift):
        quantity=np.exp(-price*price)
        return quantity+(price-(c0+shift-quantity))*(-2*price*quantity)
    h=1e-6
    plus=brentq(lambda x:foc(x,h),.9,1.1,xtol=1e-14)
    minus=brentq(lambda x:foc(x,-h),.9,1.1,xtol=1e-14)
    fd=(plus-minus)/(2*h)
    assert abs(fd-analytic)<1e-8 and analytic>1 and qp*denominator<0
    assert c0-q>0 and q*qpp-qp*qp<0
    print(f'[PASS] strictly log-concave demand with declining MC: pass-through={analytic:.9f}, FD={fd:.9f}>1, local SOC negative; constant-MC result cannot be generalized')
    # Literal linear-price logit counterexample to the old routing-table claim.
    # q<=.4 keeps MC positive everywhere feasible; the optimum q=.3 is interior.
    p=2.;q=.3;v=p+np.log(q/(1-q));qp=-q*(1-q);qpp=q*(1-q)*(1-2*q)
    cp=-4.;mc=p-1/(1-q);c0=mc-cp*q
    denom=2-q*qpp/(qp*qp)-cp*qp
    rho=1/denom
    def logit_foc(price,shift):
        quantity=expit(v-price)
        return quantity+(price-c0-cp*quantity-shift)*(-quantity*(1-quantity))
    plus=brentq(lambda x:logit_foc(x,h),1.9,2.1,xtol=1e-14)
    minus=brentq(lambda x:logit_foc(x,-h),1.9,2.1,xtol=1e-14)
    fd=(plus-minus)/(2*h)
    soc=qp*denom
    assert mc>0 and c0+cp*.4>0 and q<.4 and soc<0 and rho>1 and abs(fd-rho)<1e-8
    # Profit as a function of q has curvature -1/[q(1-q)^2]-cp <0:
    # min 1/[q(1-q)^2]=27/4 >4, hence the interior optimum is unique.
    assert 27/4 > -cp
    constant_mc_rho=1/(2-q*qpp/(qp*qp))
    assert 0<constant_mc_rho<1
    print(f'[PASS] linear-price logit declining MC: pass-through={rho:.9f}, FD={fd:.9f}, MC={mc:.9f}, SOC={soc:.9f}; constant-MC comparator={constant_mc_rho:.9f}<1; positive-cost feasible capacity=.4, nonbinding at optimum')
    # Smooth, unbiased moment simulator with large extra zero-mean noise.
    S=2.;data_variance=1.;simulation_variance=100.
    exact=data_variance;simulated=data_variance+simulation_variance/S
    assert simulated/exact==51. and simulated/exact>1+1/S
    print('[PASS] smooth unbiased simulator theta+10Z: S=2 covariance factor=51, not below 1.5; smoothness alone is not variance reduction')
    print('ALL PASS; local illustrative algebra, not an empirical conclusion')
if __name__=='__main__':main()
