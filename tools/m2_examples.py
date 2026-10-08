"""Reproducible numeric illustrations for M2 (certification-bias convergence and label precision weight).
All numbers are illustrative [I], not estimates."""
import numpy as np
from scipy.stats import norm

print("== A. label precision weight kappa vs number of owner reports n ==")
s0, se, tau = 1.0, 1.5, 0.35          # prior sd | characteristics, per-report noise sd, perceived label noise sd (L/100km)
for sb in (0.0, 0.5):                 # sd of the non-diversifiable owner-report component b_j
    row = []
    for n in (0, 5, 20, 100, 500, 2000, np.inf):
        sO2 = sb**2 + (se**2/n if n > 0 else np.inf)
        if sO2 == 0:
            v = 0.0                      # owner reports reveal T exactly
        else:
            v = 1/(1/s0**2 + (1/sO2 if np.isfinite(sO2) else 0.0))
        row.append(v/(v+tau**2))
    print(f"sigma_b={sb}: " + " ".join(f"{k:.3f}" for k in row))

print("== B. symmetric (Shapley) decomposition of Delta B ==")
LN, w, O = 7.0, 0.077, 8.5
LX = LN*(1+w); W = LX-LN
def decomp(k0, k1, z0, z1):
    kb, zb, Lb = (k0+k1)/2, (z0+z1)/2, (LN+LX)/2
    ellb = (z0*LN + z1*LX)/2
    num = kb*zb*W; rev = kb*(z1-z0)*Lb; wt = (k1-k0)*(ellb-O)
    tot = k1*z1*LX + (1-k1)*O - (k0*z0*LN + (1-k0)*O)
    return num, rev, wt, tot
cases = {"naive": (0.6,0.6,1.30,1.30,8.5), "known-average": (0.6,0.6,1.30,1.30/1.077,8.5),
         "precision up, O=8.5": (0.5,0.65,1.30,1.30/1.077,8.5), "precision up, O=9.6": (0.5,0.65,1.30,1.30/1.077,9.6),
         "precision down,O=8.5": (0.6,0.45,1.30,1.30/1.077,8.5), "credulous": (0.6,0.6,1.30,1.093,8.5)}
for k,(a,b,c,d,Ok) in cases.items():
    O = Ok
    num, rev, wt, tot = decomp(a,b,c,d)
    print(f"{k:22s} numeric={num:+.4f} revaluation={rev:+.4f} weight={wt:+.4f} sum={num+rev+wt:+.4f} check={tot:+.4f}")

O = 8.5
print("== C. calibration: corrective vs credulous ==")
zt_N = 1.30; zt_X = zt_N/1.077          # objective truth/label ratios
for name, z0, z1 in (("corrective", 1.45, 1.25), ("credulous", 1.30, 1.093)):
    b0 = (z0-zt_N)*LN; b1 = (z1*LX - zt_X*LX)
    print(f"{name:10s} label-implied bias before={b0:+.3f} after={b1:+.3f} (L/100km), |bias| {'falls' if abs(b1)<abs(b0) else 'rises'}")

print("== D. relative credibility (homogeneous logit) ==")
delta = np.array([1.0, 0.8, 0.5, 0.2]); c = 0.8
dB = np.array([0.30, 0.60, 0.60, 0.0])
def sh(d):
    e = np.exp(d); return e/(1+e.sum())
s_old = sh(delta); s_new = sh(delta - c*dB)
print("shares before", np.round(s_old,4), "after", np.round(s_new,4))
print("share-weighted mean dB (incl. outside, dB_0=0) =", round(float(s_old@dB),4), "; product 1 dB=0.30, share change", round(float(s_new[0]-s_old[0]),4))

print("== E. allowable wedge: own-neutral W* and market-neutral W** ==")
k0,k1,z0,z1 = 0.5,0.6,1.30,1.30/1.077
Wstar = (k0*z0*LN + (k1-k0)*O - k1*z1*LN)/(k1*z1)
print(f"W* = {Wstar:.4f} L/100km (w* = {Wstar/LN:.4f}); naive -> 0; known-average -> wbar*LN = {0.077*LN:.4f}")
# market-neutral: competitors' share-weighted belief change (homogeneous logit, product 1 of example D)
dBtilde = float((s_old[1:]@dB[1:])/(1-s_old[0]))
print(f"competitor-weighted dB~ = {dBtilde:.4f};  W** = W* + dB~/(k1 z1) = {Wstar + dBtilde/(k1*z1):.4f}")

print("== F. BEV expected range shortfall with posterior uncertainty ==")
B, D = 380.0, 400.0
for sd in (1e-9, 20, 40, 60):
    mu = D-B; z = mu/sd
    print(f"sd={sd:>5.0f}: E[(D-T)+] = {mu*norm.cdf(z)+sd*norm.pdf(z):.3f}")

print("== G. martingale property: rational expectations => powertrain-average belief unchanged ==")
rng = np.random.default_rng(20261008)
J = 200000; mu = 8.0
T = mu + s0*rng.standard_normal(J)
sb, n = 0.5, 20
Obar = T + sb*rng.standard_normal(J) + se/np.sqrt(n)*rng.standard_normal(J)
sO2 = sb**2 + se**2/n; v = 1/(1/s0**2 + 1/sO2)
Otil = v*(mu/s0**2 + Obar/sO2)
zN0, zX0, tN, tX = 1.30, 1.30/1.077, 0.60, 0.35      # objective ratios and label noise sd (old, new)
LN_ = (T - tN*rng.standard_normal(J))/zN0
LX_ = (T - tX*rng.standard_normal(J))/zX0
def belief(z, L, t):
    k = v/(v+t**2); return k*z*L + (1-k)*Otil
BN = belief(zN0, LN_, tN); BX = belief(zX0, LX_, tX)
dB = BX - BN
print(f"RE: mean dB = {dB.mean():+.4f}, share of models with dB<0 = {(dB<0).mean():.3f}, sd(B) {BN.std():.3f}->{BX.std():.3f}")
BN_os = belief(1.45, LN_, tN)                         # over-skeptical under NEDC
dB_os = BX - BN_os
print(f"over-skeptical NEDC (zeta_N=1.45): mean dB = {dB_os.mean():+.4f}, share dB<0 = {(dB_os<0).mean():.3f}")
