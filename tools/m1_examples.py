import numpy as np
np.set_printoptions(precision=6, suppress=True)

# ---------- Example A: relative utility (homogeneous logit), naive belief ----------
# 3 ICE + 1 BEV, delta_j=0 for inside goods, outside delta0 set to hit target s0.
# Naive belief: Delta u_j = -c * w_j for ICE (w = relative wedge), 0 for BEV.
w = np.array([0.02, 0.12, 0.15, 0.0])
c = 1.26   # = alpha*phi*K*L^N  (utility units per unit relative wedge)
du = -c * w
def shares(delta, delta0):
    e = np.exp(delta); e0 = np.exp(delta0)
    D = e0 + e.sum()
    return e / D, e0 / D
for s0_target in [0.22, 0.58]:
    J = 4
    e0 = s0_target * J / (1 - s0_target)
    d0 = np.log(e0)
    s_old, s0_old = shares(np.zeros(4), d0)
    s_new, s0_new = shares(du, d0)
    lin = s_old * (du - (s_old * du).sum())
    print(f"[A] s0={s0_old:.4f}: du_ICE1={du[0]:.4f}, mean P*du={(s_old*du).sum():.4f}; "
          f"s_ICE1 {s_old[0]:.4f} -> {s_new[0]:.4f} (exact d={s_new[0]-s_old[0]:+.5f}, first-order {lin[0]:+.5f}); "
          f"BEV {s_old[3]:.4f}->{s_new[3]:.4f}; outside {s0_old:.4f}->{s0_new:.4f}")

# ---------- Example B: ratings shrinkage, overall vs subscores ----------
# two subscores k=1,2, weights omega=(0.5,0.5); prior mean 0, prior var sq2_k; noise var se2_k; n reviews
n = 20
qbar = np.array([0.0, 0.0])
sq2 = np.array([0.04, 0.04])     # prior variance of quality
se2 = np.array([0.04, 4.0])      # per-review noise variance (k=2 much noisier)
rbar = np.array([0.30, 0.30])    # observed average subscores (deviation from prior mean)
lam = n*sq2/(n*sq2+se2)          # shrinkage weights
Qk = qbar + lam*(rbar-qbar)
omega = np.array([0.5, 0.5])
sum_omega_Q = (omega*Qk).sum()
# overall score r_all = sum omega_k r_k  -> signal on q_all = sum omega_k q_k; noise var = sum omega^2 se2 / n
sq2_all = (omega**2*sq2).sum()
se2_all = (omega**2*se2).sum()
lam_all = n*sq2_all/(n*sq2_all+se2_all)
Q_all = lam_all*(omega*rbar).sum()
print(f"[B] shrink weights per subscore={lam}, sum omega*Q_k={sum_omega_Q:.4f}; overall-score posterior={Q_all:.4f} (lam_all={lam_all:.4f})")

# ---------- Example C: label diversion vs price diversion, role of outside-option energy cost ----------
rng = np.random.default_rng(20261008)
N = 400000
# consumer heterogeneity: income-driven alpha, VKT lognormal
lnVKT = rng.normal(np.log(12000), 0.5, N)        # km/yr
VKT = np.exp(lnVKT)
alpha = np.exp(rng.normal(np.log(0.10), 0.3, N))  # utils per 1000 yuan
# products: ICE with labels L (L/100km), price (1000 yuan)
L = np.array([5.0, 6.5, 8.0])
p = np.array([140.0, 120.0, 100.0])
xi = np.array([1.0, 1.0, 1.0])
pi_f = 7.5          # yuan/L
Lambda = 6.0        # discounted lifetime-years factor (years-equivalent)
phi = 0.8           # label valuation ratio
e0 = 8.5            # old car fuel consumption (L/100km)
def K(): return pi_f*VKT*Lambda/100/1000   # 1000 yuan per (L/100km)
Ki = K()
def probs(include_outside_cost, shift=0.0):
    V = (xi[None,:]+shift) - alpha[:,None]*(p[None,:] + phi*Ki[:,None]*L[None,:])
    V0 = -alpha*phi*Ki*e0 if include_outside_cost else np.zeros(N)
    V0 = V0 + 0.0
    m = np.maximum(V.max(1), V0)
    eV = np.exp(V - m[:,None]); e0v = np.exp(V0 - m)
    D = e0v + eV.sum(1)
    return eV/D[:,None], e0v/D
from math import isclose
def calib(inc, target=0.5):
    lo, hi = -50.0, 80.0
    for _ in range(80):
        mid = 0.5*(lo+hi)
        _, P0 = probs(inc, mid)
        if P0.mean() > target: lo = mid
        else: hi = mid
    return 0.5*(lo+hi)
for inc in [True, False]:
    sh = calib(inc)
    P, P0 = probs(inc, sh)
    # shift outside utility level so that mean outside share ~ 0.5 for comparability
    j = 1  # perturb middle car's label/price
    wL = alpha*phi*Ki   # weight for label
    wp = alpha          # weight for price
    def diversion(wt):
        num = (wt[:,None]*P[:,[j]]*P).mean(0)
        den = (wt*P[:,j]*(1-P[:,j])).mean()
        dk = num/den; dk[j] = np.nan
        d0 = (wt*P[:,j]*P0).mean()/den
        return dk, d0
    dL, dL0 = diversion(wL); dp, dp0 = diversion(wp)
    corr = np.corrcoef(Ki, P0)[0,1]
    print(f"[C] outside cost included={inc}: mean s0={P0.mean():.3f}; label diversion to most efficient (k=0) {dL[0]:.4f} vs price diversion {dp[0]:.4f}; "
          f"to outside label {dL0:.4f} vs price {dp0:.4f}; corr(K,P0)={corr:+.3f}; check sum label={np.nansum(dL)+dL0:.6f}")
