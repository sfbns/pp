"""Toy RC-logit demand/supply checks. No empirical BLP identification claim."""
from pathlib import Path
import argparse
import hashlib
import json
import numpy as np

parser = argparse.ArgumentParser()
parser.add_argument('--out')
args = parser.parse_args()
rows = []

def check(name, condition, observed):
    rows.append({'name': name, 'passed': bool(condition), 'observed': observed})

# Rows are products; columns are fixed heterogeneous consumers. No fresh draws.
price = np.array([2.0, 2.5, 3.2, 4.0])
alpha = np.array([.4, .7, 1.1, 1.5])
weight = np.array([.1, .2, .3, .4])
nonprice = np.array([[.3,.5,.4,.6],[.8,.6,.5,.4],[1.1,.9,.6,.3],[1.0,1.3,.9,.4]])
ownership = np.equal.outer([0,0,1,2], [0,0,1,2]).astype(float)

def individual(p):
    v = nonprice - p[:,None] * alpha[None,:]
    maximum = np.maximum(0, v.max(axis=0))
    numer = np.exp(v - maximum)
    denominator = np.exp(-maximum) + numer.sum(axis=0)
    return numer / denominator, np.exp(-maximum) / denominator

def shares(p):
    return individual(p)[0] @ weight

prob, outside = individual(price)
share = shares(price)
check('probability_including_outside_sums_to_one', np.allclose(prob.sum(axis=0)+outside,1), {'individual_sums':(prob.sum(axis=0)+outside).tolist()})
J = np.empty((4,4))
for j in range(4):
    for k in range(4):
        J[j,k] = np.dot(weight, -alpha*prob[j]*((1 if j==k else 0)-prob[k]))
step = 1e-5
fd = np.column_stack([(shares(price+step*np.eye(4)[k])-shares(price-step*np.eye(4)[k]))/(2*step) for k in range(4)])
check('analytical_ds_j_dp_k_matches_finite_difference', np.max(np.abs(J-fd))<1e-9, {'max_absolute_error':float(np.max(np.abs(J-fd))), 'convention':'row j share, column k price'})
check('own_negative_cross_positive_given_positive_alpha', np.all(np.diag(J)<0) and np.all(J[~np.eye(4,dtype=bool)]>0), {'own':np.diag(J).tolist(), 'min_cross':float(J[~np.eye(4,dtype=bool)].min())})

# BLP mean-utility inversion with fixed heterogeneity and outside utility zero.
v_true = nonprice-price[:,None]*alpha[None,:]
delta_true = v_true @ weight
mu = v_true-delta_true[:,None]
def shares_delta(delta):
    value=delta[:,None]+mu
    mx=np.maximum(0,value.max(axis=0))
    e=np.exp(value-mx)
    return (e/(np.exp(-mx)+e.sum(axis=0)))@weight
delta=np.zeros(4)
for iteration in range(1,5001):
    update=np.log(share)-np.log(shares_delta(delta))
    delta=delta+update
    if np.max(np.abs(update))<1e-12:break
check('fixed_draw_BLP_contraction_recovers_mean_utility', iteration<5000 and np.max(np.abs(delta-delta_true))<1e-10 and np.max(np.abs(shares_delta(delta)-share))<1e-11, {'iterations':iteration,'max_delta_error':float(np.max(np.abs(delta-delta_true))),'max_share_error':float(np.max(np.abs(shares_delta(delta)-share))),'condition':'fixed heterogeneous tastes, positive observed shares, same fixed consumers/weights, outside normalized to zero; no GMM parameter estimate'})
# FOC for price j: s_j + sum_k O_jk (p_k-c_k) ds_k/dp_j = 0.
Delta = -ownership*J.T
markup = np.linalg.solve(Delta, share)
cost = price-markup
residual = share + (ownership*J.T)@markup
check('multi_product_bertrand_FOC_orientation', np.max(np.abs(residual))<1e-12, {'max_FOC_residual':float(np.max(np.abs(residual))), 'Delta':'-ownership * J.T', 'markups':markup.tolist(), 'recovered_mc':cost.tolist(), 'scope':'static toy costs inferred from these synthetic prices, not observed costs or equilibrium uniqueness'})

# Each product-specific alpha is still positive but makes J nonsymmetric:
aj = alpha[None,:]*np.array([1.,1.1,1.2,1.3])[:,None]
J_asym = np.array([[-np.dot(weight,aj[k]*prob[j]*((1 if j==k else 0)-prob[k])) for k in range(4)] for j in range(4)])
Da = -ownership*J_asym.T
ma = np.linalg.solve(Da,share)
wrong = share + (ownership*J_asym)@ma
check('transpose_negative_control_nonsymmetric_generalization', np.max(np.abs(wrong))>1e-5 and np.max(np.abs(share+(ownership*J_asym.T)@ma))<1e-12, {'wrong_transpose_max_residual':float(np.max(np.abs(wrong))), 'scope':'synthetic product-specific price slopes demonstrate orientation; not a welfare-normalized baseline'})

# Conditional second choice k after removing first-choice j, for the SAME i.
j,k = 0,2
joint = float(np.dot(weight,prob[j]*prob[k]/(1-prob[j])))
incorrect = float(np.dot(weight,prob[j])*np.dot(weight,prob[k]/(1-prob[j])))
check('first_second_same_consumer_multiply_before_integrate', abs(joint-incorrect)>1e-5, {'joint':joint,'incorrect_product_of_integrals':incorrect,'assumption':'independent type-I EV shocks conditional on fixed consumer tastes; j removed'})

def money_logsum(p):
    v = nonprice-p[:,None]*alpha[None,:]
    m = np.maximum(0,v.max(axis=0))
    lse = m+np.log(np.exp(-m)+np.exp(v-m).sum(axis=0))
    return float(np.dot(weight,lse/alpha))

wstep = (money_logsum(price+step*np.eye(4)[0])-money_logsum(price-step*np.eye(4)[0]))/(2*step)
check('heterogeneous_alpha_money_logsum_price_derivative', abs(wstep+share[0])<1e-9, {'derivative':wstep,'negative_share':float(-share[0]),'condition':'fixed positive alpha and fixed tastes; only price changes; average logsum_i/alpha_i'})
check('money_logsum_not_divide_by_mean_alpha', abs(money_logsum(price)-float(np.dot(weight,((np.log1p(np.exp(nonprice-price[:,None]*alpha).sum(axis=0))))))/float(weight@alpha))>1e-3, {'scope':'integrate money normalization per consumer, not average utility divided by mean alpha'})

# Experienced welfare: fixed chosen probabilities, true utility, and EV entropy.
V = nonprice-price[:,None]*alpha
entropy = -(prob*np.log(prob)).sum(axis=0)-outside*np.log(outside)
experienced = float(np.dot(weight,((prob*V).sum(axis=0)+entropy)/alpha))
check('decision_equals_experience_when_beliefs_true', abs(experienced-money_logsum(price))<1e-12, {'experience':experienced,'decision':money_logsum(price),'condition':'no belief error, same true/decision utility, EV normalization constant omitted in both'})
biased_V = V + np.array([.5,0,0,0])[:,None]
mx = np.maximum(0,biased_V.max(axis=0))
bp = np.exp(biased_V-mx)/(np.exp(-mx)+np.exp(biased_V-mx).sum(axis=0))
bo = np.exp(-mx)/(np.exp(-mx)+np.exp(biased_V-mx).sum(axis=0))
bh = -(bp*np.log(bp)).sum(axis=0)-bo*np.log(bo)
exp_b = float(np.dot(weight,((bp*V).sum(axis=0)+bh)/alpha))
decision_b = float(np.dot(weight,((bp*biased_V).sum(axis=0)+bh)/alpha))
check('decision_logsum_not_experienced_welfare_under_bias', abs(decision_b-exp_b)>1e-3 and exp_b < experienced, {'decision_biased':decision_b,'experience_biased_choice':exp_b,'corrected_choice_experience':experienced,'scope':'synthetic fixed-menu no-repricing demonstration, not China net policy welfare'})

result = {'status':'PASS' if all(r['passed'] for r in rows) else 'FAIL','scope':'fixed-draw synthetic RC-logit demand, BLP mean-utility inversion, static multi-product supply and welfare identities; no GMM parameter estimation, empirical exclusion, global equilibrium or performance grade','script_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),'checks':rows}
output = json.dumps(result,ensure_ascii=False,indent=2)+'\n'
if args.out:
    target = Path(args.out)
    target.parent.mkdir(parents=True,exist_ok=True)
    target.write_text(output,encoding='utf8')
print(output,end='')
raise SystemExit(0 if result['status']=='PASS' else 1)
