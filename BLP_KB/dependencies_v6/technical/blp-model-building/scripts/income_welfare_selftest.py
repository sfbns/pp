"""Individual money-metric roots with income effects, not a logsum shortcut.

Synthetic fixed observed type and fixed taste-shock distribution/preferences.
These are EX ANTE expected-max-utility compensation roots for this type, not
the mean/distribution of ex post shock-specific CV/EV. CV is money given after
a price increase to restore old expected utility; EV is removed before it.
"""
import numpy as np
from scipy.optimize import brentq
from scipy.special import logsumexp

def main():
    y=30.;p0=np.array([0.,6.,12.]);p1=np.array([0.,9.,15.])
    x=np.array([0.,1.2,1.8]);alpha=1.4
    def eu(p,income):
        assert np.all(income-p>0)
        return float(logsumexp(alpha*np.log(income-p)+x))
    old=eu(p0,y);new=eu(p1,y)
    cv=brentq(lambda c:eu(p1,y+c)-old,0.,15.,xtol=1e-12)
    ev=brentq(lambda e:eu(p0,y-e)-new,0.,10.,xtol=1e-12)
    assert cv>0 and ev>0 and abs(cv-ev)>1e-3
    assert abs(eu(p1,y+cv)-old)<1e-12 and abs(eu(p0,y-ev)-new)<1e-12
    # Dividing by a constant price coefficient is not money-metric income welfare.
    shortcut=(old-new)/alpha
    assert abs(shortcut-cv)>1.
    print(f"[PASS] nonlinear-income CV={cv:.9f}; EV={ev:.9f}; constant-alpha-logsum-shortcut={shortcut:.9f}")
    print("[PASS] both individual utility-restoration roots have residual below 1e-12; CV/EV conventions explicit")
    print("ALL PASS; illustration not an estimated welfare effect")
if __name__=='__main__':main()
