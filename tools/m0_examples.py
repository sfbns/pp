"""Reproducible numeric illustrations for M0 (base regressions). Illustrative [I] only."""
import numpy as np
from scipy.optimize import brentq

print("== A. single-product logit: pass-through of a demand (label) shock vs a cost (compliance) shock ==")
alpha = 1/30000.0            # utils per yuan
def eq_price(dnp, mc, d0=0.0):
    # outside utility 0, other products absorbed into the outside option; s = exp(dnp - alpha p)/(1+exp(...))
    f = lambda p: p - mc - 1.0/(alpha*(1-1/(1+np.exp(-(dnp-alpha*p)))))
    return brentq(f, mc, mc+200/alpha)
mc0 = 150000.0
# choose dnp so that equilibrium share is 0.5%
target_s = 0.005
def share_at(dnp):
    p = eq_price(dnp, mc0); return 1/(1+np.exp(-(dnp-alpha*p)))
dnp0 = brentq(lambda d: share_at(d)-target_s, -5, 10)
p0 = eq_price(dnp0, mc0); s0 = share_at(dnp0)
p_label = eq_price(dnp0 - alpha*3750.0, mc0)        # label shock worth 3750 yuan of perceived cost (phi=1)
p_cost = eq_price(dnp0, mc0 + 1000.0)               # compliance-cost shock of 1000 yuan
print(f"s0={s0:.4f}, p0={p0:.1f}; label shock 3750 -> dp={p_label-p0:+.2f} (first order -3750*s={-3750*s0:+.2f}); "
      f"cost shock 1000 -> dp={p_cost-p0:+.2f} (first order 1000*(1-s)={1000*(1-s0):+.2f})")

print("== B. errors-in-variables with two regressors (naive truth: beta=-1, rho=0) ==")
rng = np.random.default_rng(20261008)
def eiv_sim(sd_w, R=200, J=600, rel=0.754):
    out = []
    for _ in range(R):
        LN = rng.uniform(5, 9, J)
        w = 0.077 + sd_w*rng.standard_normal(J)
        W = w*LN
        X2 = LN.copy()                         # S*G^N with K normalized to 1, switched period
        X1 = W.copy()                          # S*Delta G^W true
        # classical error in X1 with unconditional reliability rel
        sig_e = np.sqrt(np.var(X1)*(1-rel)/rel)
        X1t = X1 + sig_e*rng.standard_normal(J)
        y = -1.0*X1 + 0.0*X2 + 0.05*rng.standard_normal(J)
        X = np.column_stack([np.ones(J), X1t, X2])
        b = np.linalg.lstsq(X, y, rcond=None)[0]
        # conditional reliability of X1 given X2
        r = X1 - np.polyval(np.polyfit(X2, X1, 1), X2)
        lam_c = np.var(r)/(np.var(r)+sig_e**2)
        pi = np.polyfit(X2, X1, 1)[0]
        out.append((b[1], b[2], lam_c, pi))
    o = np.array(out).mean(0)
    return o
for sd_w in (0.012, 0.03):
    bh, rh, lam_c, pi = eiv_sim(sd_w)
    print(f"sd(w)={sd_w}: beta_hat={bh:.3f} (naive correction beta/0.754={bh/0.754:.3f}), rho_hat={rh:+.4f}, "
          f"conditional reliability={lam_c:.3f}, theory rho bias=(1-lam)*beta*pi={(1-lam_c)*(-1)*pi:+.4f}")

print("== C. rank of (S*DeltaG^W, S*G^N) after centering: condition number vs dispersion of relative wedge ==")
for sd_w in (0.0, 0.005, 0.01, 0.03):
    LN = rng.uniform(5, 9, 2000); w = 0.077 + sd_w*rng.standard_normal(2000)
    X = np.column_stack([w*LN, LN]); X = X - X.mean(0); X = X/np.linalg.norm(X, axis=0)
    sv = np.linalg.svd(X, compute_uv=False)
    print(f"sd(w)={sd_w}: singular values {np.round(sv,4)}, condition number {sv[0]/max(sv[1],1e-16):.3g}")
