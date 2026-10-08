"""Synthetic counterexamples to identifying information by a mean/residual split.

No actual policy identification, no estimated Chinese parameters, no scores.
NumPy only. Outputs stdout; never mutates an input or a frozen candidate.
"""
import json
import numpy as np

def shares(energy, other=np.array([-1.0, -1.2]), coefficient=.1):
    v=other-coefficient*np.asarray(energy)
    e=np.exp(np.r_[0.,v]-max(0.,float(v.max())))
    return e[1:]/e.sum()

f=np.array([6.,8.])
# A common uncertain log road-consumption multiplier A ~ N(0,1).
# A new signal y=A+nu, nu independent N(0,1), is realized at y=1.
# The rational posterior is N(.5,.5); E[exp(A)] is exp(m+v/2).
old=f*np.exp(.5)
new=f*np.exp(.5+.5*.5)
raw_change=np.log(new/old)
assert np.max(np.abs(raw_change-.25))<1e-14
s0=shares(old)
# World A: same printed labels arise only from a KNOWN unit conversion.
s_units=shares(new/np.exp(.25))
# World B: those same printed labels reflect genuinely new information.
s_info=shares(new)
assert np.max(np.abs(s_units-s0))<1e-14
assert np.all(s_info<s0)
print(json.dumps({'case':'same_common_display_change_two_information_structures',
 'passed':True,'common_log_change':raw_change.tolist(),
 'residual_log_change':(raw_change-raw_change.mean()).tolist(),
 'baseline_shares':s0.tolist(),'known_units_shares':s_units.tolist(),
 'rational_new_information_shares':s_info.tolist(),
 'interpretation':'A cross-product mean is an algebraic statistic, not identified pure remeasurement. Physical attributes can be fixed while rational beliefs change.'}))

eps=1e-5
def derivative(fun):return (fun(eps)-fun(-eps))/(2*eps)
def logq(m=.5,var=.5,logpi=0.):
    assert var>0
    return np.log(shares(f*np.exp(m+.5*var+logpi)))
price=derivative(lambda h:logq(logpi=h))
mean_only=derivative(lambda h:logq(m=.5+h))
# The printed value summarizes posterior log-location, while new information
# also decreases posterior variance. This is a local family of information
# states, not an assertion that China's policy has this variance derivative.
mean_and_precision=derivative(lambda h:logq(m=.5+h,var=.5-4*h))
ratio1=mean_only/price
ratio2=mean_and_precision/price
assert np.max(np.abs(ratio1-1))<1e-8
assert np.max(np.abs(ratio2+1))<1e-8
assert np.all(np.abs(price)>1e-6)
print(json.dumps({'case':'rational_response_ratio_not_generic_psychology_or_unit_interval',
 'passed':True,'denominator_log_energy_price_derivative':price.tolist(),
 'rational_mean_information_ratio':ratio1.tolist(),
 'rational_mean_plus_precision_ratio':ratio2.tolist(),
 'interpretation':'A [0,1] salience interpretation requires a defined noninformative display intervention, common monetary channel, identified denominator and no precision/other-equilibrium changes. It is not delivered by averaging labels.'}))
print('SUMMARY: 2/2; conditional synthetic counterexamples, no policy or psychology identification')
