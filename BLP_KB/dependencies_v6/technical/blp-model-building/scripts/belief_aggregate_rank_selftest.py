"""A sufficiency counterexample, not an identification claim for Chinese data.

Homogeneous logit is a restricted BLP case. Known priors/scale and independent
aggregate variation can identify a belief weight without a household survey.
The counterexamples show what fails when those maintained conditions are dropped.
No files are written; all inputs and output are synthetic and deterministic.
"""
import json
import numpy as np
from scipy.special import expit,logit

checks=[]
def check(name,condition,**detail):
    checks.append(bool(condition))
    print(json.dumps({'name':name,'passed':bool(condition),**detail},ensure_ascii=False))

alpha=.02;gamma=.85;a=.60;intercept=1.20
mu=np.array([10.,8.,11.,9.,7.])
label=np.array([8.,10.,7.,8.,9.])
price=np.array([20.,22.,19.,21.,23.])
def shares(g,attention,prior,constant=intercept,mileage=1.):
    belief=prior+attention*(label-prior)
    return expit(constant-alpha*price-alpha*g*mileage*belief)

observed=shares(gamma,a,mu)
# All other utility primitives, outside utility, alpha and cost scale are known.
# In an empirical application these are restrictions to identify, not observations
# delivered by running this regression; omitted xi needs valid exclusion moments.
y=logit(observed)+alpha*price
X=np.column_stack([np.ones(len(mu)),-alpha*mu,-alpha*(label-mu)])
b=np.linalg.lstsq(X,y,rcond=None)[0]
check('known_prior_independent_aggregate_variation',np.linalg.matrix_rank(X)==3 and np.max(np.abs(b-[intercept,gamma,gamma*a]))<1e-12,
      rank=int(np.linalg.matrix_rank(X)),estimated_capitalization=float(b[1]),estimated_belief_weight=float(b[2]/b[1]),
      assumptions='Known priors, alpha, cost scale and specified nonenergy utility; independent excluded variation, no confounded xi; common parameters. Survey not logically necessary.')

prior=np.full(len(mu),10.)
Xc=np.column_stack([np.ones(len(mu)),-alpha*prior,-alpha*(label-prior)])
g2=.75;a2=gamma*a/g2;b02=intercept+alpha*10*(g2-gamma)
gap=float(np.max(np.abs(shares(gamma,a,prior)-shares(g2,a2,prior,b02))))
check('constant_prior_free_intercept_nonidentification',np.linalg.matrix_rank(Xc)==2 and gap<1e-14,
      rank=int(np.linalg.matrix_rank(Xc)),max_share_gap=gap,alternative_parameters=[float(b02),g2,a2])

gap=float(np.max(np.abs(shares(gamma,a,mu,mileage=1.)-shares(1.,a,mu,mileage=gamma))))
check('unknown_mileage_scale_confounds_capitalization',gap<1e-14,max_share_gap=gap,
      meaning='Identifies effective gamma times mileage scale, not each free parameter.')

att1,trust1=.8,.75;att2,trust2=.75,.8
gap=float(np.max(np.abs(shares(gamma,att1*trust1,mu)-shares(gamma,att2*trust2,mu))))
check('belief_weight_not_named_psychology',gap<1e-14,max_share_gap=gap,
      meaning='Even identified information weight does not separate attention from trust when only their product enters.')

# Mathematical full rank can still be economically weak. Noisy sample moments
# need weak-identification diagnostics and valid IV inference, not OLS certainty.
perturb=np.array([1.,-1.,2.,-2.,0.])*1e-9
weak_label=1.3*mu+perturb
Xw=np.column_stack([np.ones(len(mu)),-alpha*mu,-alpha*(weak_label-mu)])
sv=np.linalg.svd(Xw,compute_uv=False);condition=float(sv[0]/sv[-1])
check('formal_rank_not_strong_identification',np.linalg.matrix_rank(Xw)==3 and condition>1e9,
      rank=int(np.linalg.matrix_rank(Xw)),condition_number=condition,smallest_singular_value=float(sv[-1]))

J=np.column_stack([-alpha*(mu+a*(label-mu)),-alpha*gamma*(label-mu)])
h=1e-6
fd=np.column_stack([(logit(shares(gamma+h,a,mu))-logit(shares(gamma-h,a,mu)))/(2*h),
                    (logit(shares(gamma,a+h,mu))-logit(shares(gamma,a-h,mu)))/(2*h)])
err=float(np.max(np.abs(J-fd)))
check('primitive_derivatives_finite_difference',err<1e-8,max_abs_error=err,
      meaning='Does not prove exclusion restrictions or psychological myopia.')
ok=all(checks)
print(f'SUMMARY: {sum(checks)}/{len(checks)}; synthetic conditional rank checks only; exit={0 if ok else 1}')
raise SystemExit(0 if ok else 1)
